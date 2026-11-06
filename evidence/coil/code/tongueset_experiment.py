#!/usr/bin/env python3
"""
tongueset_experiment.py — PREREG-MM1-WAVEFORM-TONGUESET v1.0 execution.

Stage A : survey  kappa in [0.5, 8.0], step 0.01 (751 cells), full 25-IC protocol
Stage B : deterministic local refinement, step 0.0025, expand until two consecutive
          negatives on each side (rule fixed in the prereg, not chosen from data)
Geometry: maximal contiguous CF>=0.60 runs -> components with midpoint boundaries

Classifier is identical in both stages. Computation is blocked over (kappa x IC);
arithmetic is element-wise identical to the per-cell version (certified by G2).

Usage:
  python tongueset_certificate.py                     # gate, must exit 0
  python tongueset_experiment.py --t -0.300           # one waveform, both stages
  python tongueset_experiment.py --t -0.300 --stage A # survey only
  python tongueset_experiment.py --geometry           # build summary from CSVs
"""
import argparse, csv, math, os
import numpy as np

# ---------------- locked constants ----------------
A_PAR, DT = 0.03, 0.10
A0 = math.asin(0.9125)/0.9125
C = (1.0 - A0)/4.0
T_LOCKED = [-0.300, -0.220, -0.140, -0.060, 0.000, 0.008]
K_LO, K_HI, D_SURVEY, D_FINE = 0.5, 8.0, 0.01, 0.0025
PHI0 = [0.1, 0.5, 1.0, 2.0, 3.0]
U0 = [0.0, 0.5, -0.5, 2.0, -2.0]
BURN, LYAP, EPS = 70000, 200000, 1e-3
N_IC = 25
CF_MIN = 15          # >= 60% of 25
BLOCK = 25           # kappas per block

def g(p, t):
    a, b = C/2 + t, C/2 - t
    return np.sin(p) + a*(np.sin(3*p) - 3*np.sin(p)) + b*(np.sin(5*p) - 5*np.sin(p))

def gp(p, t):
    a, b = C/2 + t, C/2 - t
    return np.cos(p) + a*(3*np.cos(3*p) - 3*np.cos(p)) + b*(5*np.cos(5*p) - 5*np.cos(p))

def survey_grid():
    n = int(round((K_HI - K_LO)/D_SURVEY)) + 1
    return [round(K_LO + D_SURVEY*i, 6) for i in range(n)]

def guards(t):
    d = float(gp(np.array([0.0]), t)[0])
    if abs(d - 1.0) > 1e-9:
        raise SystemExit(f"GUARD FAIL t={t}: g'(0)={d}")
    phi = np.linspace(0, np.pi, 400001)
    v = g(phi, t)
    if abs(float(np.abs(v).max()) - A0) > 1e-9:
        raise SystemExit(f"GUARD FAIL t={t}: max|g|={np.abs(v).max()}")
    inner = v[(phi > 1e-9) & (phi < np.pi - 1e-9)]
    if int(np.sum(inner[:-1]*inner[1:] < 0)) != 0:
        raise SystemExit(f"GUARD FAIL t={t}: extra zero in (0,pi)")

def block(t, kappas):
    """Joint (kappa x IC) vectorization. Element-wise arithmetic identical to per-cell."""
    m = len(kappas)
    K = np.repeat(np.asarray(kappas, float), N_IC)
    phi = np.tile(np.array([p for p in PHI0 for _ in U0], float), m)
    w = np.tile(np.array([DT*u for _ in PHI0 for u in U0], float), m)
    a = A_PAR
    for _ in range(BURN):
        pn = phi + w
        w = (1 - a)*w - a*K*g(phi, t)
        phi = pn
    v0 = np.ones_like(phi); v1 = np.zeros_like(phi)
    acc = np.zeros_like(phi); qa = np.zeros_like(phi)
    Q = np.zeros((4, phi.size))
    ql, qi, cnt = LYAP//4, 0, 0
    for _ in range(LYAP):
        d = -a*K*gp(phi, t)
        n0 = v0 + v1
        n1 = d*v0 + (1 - a)*v1
        nr = np.sqrt(n0*n0 + n1*n1)
        nr = np.where(nr > 0, nr, 1e-300)
        l = np.log(nr)
        acc += l; qa += l; cnt += 1
        v0, v1 = n0/nr, n1/nr
        pn = phi + w
        w = (1 - a)*w - a*K*g(phi, t)
        phi = pn
        if cnt == ql:
            Q[qi] = qa/ql; qa[:] = 0; cnt = 0; qi += 1
    lam = (acc/LYAP).reshape(m, N_IC)
    ch = (lam > EPS) & np.all((Q > EPS).reshape(4, m, N_IC), axis=0)
    return ch.sum(axis=1), lam

def scan(t, kappas, tag, outdir, label):
    rows = []
    for i in range(0, len(kappas), BLOCK):
        chunk = kappas[i:i+BLOCK]
        n, lam = block(t, chunk)
        for j, k in enumerate(chunk):
            rows.append({"t": t, "kappa": k, "n_chaos": int(n[j]),
                         "cf": int(n[j])/N_IC,
                         "fracture": int(n[j]) >= CF_MIN,
                         "lam_max": f"{float(lam[j].max()):.8f}"})
        done = min(i+BLOCK, len(kappas))
        print(f"    [{label} t={t:+.3f}] {done}/{len(kappas)} cells", flush=True)
    path = os.path.join(outdir, f"ts_stage{label}_t{tag}.csv")
    with open(path, "w", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w_.writeheader(); w_.writerows(rows)
    return rows, path

def runs_of_positives(rows):
    """Maximal contiguous runs of fracture==True, as (i_start, i_end) index pairs."""
    out, s = [], None
    for i, r in enumerate(rows):
        f = r["fracture"] if isinstance(r["fracture"], bool) else r["fracture"] == "True"
        if f and s is None:
            s = i
        elif not f and s is not None:
            out.append((s, i-1)); s = None
    if s is not None:
        out.append((s, len(rows)-1))
    return out

def refine(t, survey_rows, tag, outdir):
    """Deterministic Stage-B: expand each positive run until two consecutive negatives."""
    ks = [r["kappa"] for r in survey_rows]
    todo = []
    for (i0, i1) in runs_of_positives(survey_rows):
        lo = max(K_LO, ks[max(i0-2, 0)])
        hi = min(K_HI, ks[min(i1+2, len(ks)-1)])
        todo.append((lo, hi))
    if not todo:
        print(f"    [B t={t:+.3f}] no positive survey run -> ABSENT-in-tested-domain")
        return [], None
    merged = []
    for lo, hi in sorted(todo):
        if merged and lo <= merged[-1][1] + 1e-9:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    all_rows = []
    for lo, hi in merged:
        while True:
            n = int(round((hi - lo)/D_FINE)) + 1
            grid = [round(lo + D_FINE*i, 6) for i in range(n)]
            rows, _ = scan(t, grid, tag, outdir, "B_part")
            all_rows.extend(rows)
            pos = runs_of_positives(rows)
            need_lo = bool(pos) and pos[0][0] < 2 and lo > K_LO
            need_hi = bool(pos) and pos[-1][1] > len(rows)-3 and hi < K_HI
            if not (need_lo or need_hi):
                break
            if need_lo:
                lo = max(K_LO, lo - 10*D_FINE)
            if need_hi:
                hi = min(K_HI, hi + 10*D_FINE)
            print(f"    [B t={t:+.3f}] expanding bracket -> [{lo}, {hi}]", flush=True)
    # Deterministic dedupe: bracket expansion re-scans overlapping kappas, so the
    # accumulated list can contain duplicates. Same kappa always yields the same
    # classification (deterministic map), so keeping one row per kappa is exact.
    by_kappa = {}
    for r in all_rows:
        by_kappa[r["kappa"]] = r
    all_rows = [by_kappa[k] for k in sorted(by_kappa)]
    path = os.path.join(outdir, f"ts_stageB_t{tag}.csv")
    with open(path, "w", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=list(all_rows[0].keys()))
        w_.writeheader(); w_.writerows(all_rows)
    return all_rows, path

def geometry(outdir):
    """Build the locked geometry summary from Stage-B CSVs (Stage-A if no B)."""
    out = []
    for t in T_LOCKED:
        tag = f"{t:+.3f}".replace('.', 'p')
        pb = os.path.join(outdir, f"ts_stageB_t{tag}.csv")
        pa = os.path.join(outdir, f"ts_stageA_t{tag}.csv")
        src = pb if os.path.exists(pb) else pa
        if not os.path.exists(src):
            continue
        rows = list(csv.DictReader(open(src)))
        for r in rows:
            r["kappa"] = float(r["kappa"]); r["fracture"] = r["fracture"] == "True"
        rows.sort(key=lambda r: r["kappa"])
        step = D_FINE if src == pb else D_SURVEY
        comps = []
        for (i0, i1) in runs_of_positives(rows):
            L = rows[i0]["kappa"] - step/2 if i0 > 0 else rows[i0]["kappa"]
            R = rows[i1]["kappa"] + step/2 if i1 < len(rows)-1 else rows[i1]["kappa"]
            cens = (i0 == 0 and abs(rows[0]["kappa"] - K_LO) < 1e-9) or \
                   (i1 == len(rows)-1 and abs(rows[-1]["kappa"] - K_HI) < 1e-9)
            comps.append((L, R, cens))
        total = sum(R-L for L, R, _ in comps)
        gaps = [comps[i+1][0] - comps[i][1] for i in range(len(comps)-1)]
        out.append({"t": t, "n_comp": len(comps),
                    "total_measure": f"{total:.6f}",
                    "components": " | ".join(f"[{L:.5f},{R:.5f}]{'*' if c else ''}"
                                             for L, R, c in comps) or "NONE",
                    "centers": " | ".join(f"{(L+R)/2:.5f}" for L, R, _ in comps) or "NONE",
                    "widths": " | ".join(f"{R-L:.5f}" for L, R, _ in comps) or "NONE",
                    "bounded_gaps": " | ".join(f"{g:.5f}" for g in gaps) or "NONE",
                    "source": os.path.basename(src),
                    "status": "ABSENT-in-tested-domain" if not comps else "PRESENT"})
    p = os.path.join(outdir, "ts_geometry_summary.csv")
    with open(p, "w", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w_.writeheader(); w_.writerows(out)
    for r in out:
        print(f"  t={r['t']:+.3f}  N_comp={r['n_comp']}  |T|={r['total_measure']}  "
              f"{r['components']}")
    print(f"  -> {p}   (* = censored at domain edge)")

# ---------------- T1: locked descriptor-free family-order test ----------------

def _intervals(outdir, t):
    """Component intervals for waveform t, from Stage-B if present else Stage-A."""
    tag = f"{t:+.3f}".replace('.', 'p')
    pb = os.path.join(outdir, f"ts_stageB_t{tag}.csv")
    pa = os.path.join(outdir, f"ts_stageA_t{tag}.csv")
    src = pb if os.path.exists(pb) else pa
    if not os.path.exists(src):
        raise SystemExit(f"T1: missing data for t={t} ({src})")
    rows = list(csv.DictReader(open(src)))
    for r in rows:
        r["kappa"] = float(r["kappa"]); r["fracture"] = r["fracture"] == "True"
    rows.sort(key=lambda r: r["kappa"])
    step = D_FINE if src == pb else D_SURVEY
    out = []
    for (i0, i1) in runs_of_positives(rows):
        L = rows[i0]["kappa"] - step/2 if i0 > 0 else rows[i0]["kappa"]
        R = rows[i1]["kappa"] + step/2 if i1 < len(rows)-1 else rows[i1]["kappa"]
        out.append((L, R))
    return out

def _measure(iv):
    return sum(b - a for a, b in iv)

def _inter_measure(A, B):
    tot = 0.0
    for a1, b1 in A:
        for a2, b2 in B:
            lo, hi = max(a1, a2), min(b1, b2)
            if hi > lo:
                tot += hi - lo
    return tot

def _symdiff(A, B):
    return _measure(A) + _measure(B) - 2*_inter_measure(A, B)

def _avg_ranks(x):
    """Average ranks (ties get the mean rank) — locked convention."""
    n = len(x)
    order = sorted(range(n), key=lambda i: x[i])
    ranks = [0.0]*n
    i = 0
    while i < n:
        j = i
        while j+1 < n and x[order[j+1]] == x[order[i]]:
            j += 1
        r = (i + j)/2.0 + 1.0
        for k in range(i, j+1):
            ranks[order[k]] = r
        i = j + 1
    return ranks

def _pearson(a, b):
    n = len(a)
    ma, mb = sum(a)/n, sum(b)/n
    va = sum((x-ma)**2 for x in a); vb = sum((y-mb)**2 for y in b)
    if va == 0 or vb == 0:
        return None                      # undefined -> T1 UNINFORMATIVE (not PASS)
    cov = sum((a[i]-ma)*(b[i]-mb) for i in range(n))
    return cov/math.sqrt(va*vb)

def _spearman(a, b):
    return _pearson(_avg_ranks(a), _avg_ranks(b))

def t1_test(outdir):
    """Locked: Spearman(d_ij, |t_i - t_j|) with exact 720-permutation one-sided p."""
    from itertools import permutations
    iv = {t: _intervals(outdir, t) for t in T_LOCKED}
    pairs = [(i, j) for i in range(6) for j in range(i+1, 6)]
    d = [_symdiff(iv[T_LOCKED[i]], iv[T_LOCKED[j]])/7.5 for i, j in pairs]

    def rho_for(labels):
        dt = [abs(labels[i] - labels[j]) for i, j in pairs]
        return _spearman(d, dt)

    rho_obs = rho_for(T_LOCKED)
    print("T1 — locked descriptor-free family-order test")
    for k, (i, j) in enumerate(pairs):
        print(f"    d({T_LOCKED[i]:+.3f},{T_LOCKED[j]:+.3f}) = {d[k]:.6f}")
    if rho_obs is None:
        print("  rho UNDEFINED (zero variance) -> T1 FAIL / UNINFORMATIVE")
        verdict, p = "UNINFORMATIVE", None
    else:
        ge = 0
        for perm in permutations(T_LOCKED):          # 720, identity included
            r = rho_for(list(perm))
            if r is not None and r >= rho_obs - 1e-12:
                ge += 1
        p = ge/720.0
        verdict = "PASS" if (rho_obs > 0 and p <= 0.05) else "FAIL"
        print(f"  rho_obs = {rho_obs:+.6f}")
        print(f"  exact one-sided p = {ge}/720 = {p:.6f}")
        print(f"  T1 verdict: {verdict}"
              + ("  (ordered family structure supported)" if verdict == "PASS"
                 else "  (simple monotone t-ordering rejected; NOT 'no waveform effect')"))
    # SECONDARY, DESCRIPTIVE ONLY (addendum v1.0.1 C) — cannot change the T1 verdict
    ctr = {t: [ (a+b)/2 for a, b in iv[t] ] for t in T_LOCKED}
    have = [k for k, (i, j) in enumerate(pairs)
            if ctr[T_LOCKED[i]] and ctr[T_LOCKED[j]]]
    if len(have) >= 3:
        dc = [min(abs(u-v) for u in ctr[T_LOCKED[pairs[k][0]]]
                  for v in ctr[T_LOCKED[pairs[k][1]]]) for k in have]
        dtc = [abs(T_LOCKED[pairs[k][0]] - T_LOCKED[pairs[k][1]]) for k in have]
        rc = _spearman(dc, dtc)
        print(f"  [SECONDARY, descriptive only] center-distance Spearman = "
              f"{'undefined' if rc is None else f'{rc:+.6f}'}  "
              f"(pairs used: {len(have)}/15) — does NOT affect the T1 verdict")
    else:
        print("  [SECONDARY] center-distance statistic not computable "
              "(fewer than 3 usable pairs)")

    path = os.path.join(outdir, "ts_T1_result.csv")
    with open(path, "w", newline="") as fh:
        w_ = csv.writer(fh)
        w_.writerow(["pair_i", "pair_j", "d_ij"])
        for k, (i, j) in enumerate(pairs):
            w_.writerow([T_LOCKED[i], T_LOCKED[j], f"{d[k]:.8f}"])
        w_.writerow([])
        w_.writerow(["rho_obs", "exact_p_720", "verdict"])
        w_.writerow(["" if rho_obs is None else f"{rho_obs:.8f}",
                     "" if p is None else f"{p:.8f}", verdict])
    print(f"  -> {path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=float)
    ap.add_argument("--stage", choices=["A", "B", "AB"], default="AB")
    ap.add_argument("--geometry", action="store_true")
    ap.add_argument("--t1", action="store_true")
    ap.add_argument("--outdir", default="out_tongueset")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    if a.geometry:
        geometry(a.outdir); return
    if a.t1:
        t1_test(a.outdir); return
    if a.t is None or not any(abs(a.t - x) < 1e-12 for x in T_LOCKED):
        raise SystemExit(f"--t must be one of the locked values {T_LOCKED}")
    guards(a.t)
    tag = f"{a.t:+.3f}".replace('.', 'p')
    rows = None
    if a.stage in ("A", "AB"):
        rows, p = scan(a.t, survey_grid(), tag, a.outdir, "A")
        npos = sum(1 for r in rows if r["fracture"])
        print(f"[ts A] t={a.t:+.3f}  positives={npos}/{len(rows)}  -> {p}")
    if a.stage in ("B", "AB"):
        if rows is None:
            pa = os.path.join(a.outdir, f"ts_stageA_t{tag}.csv")
            rows = list(csv.DictReader(open(pa)))
            for r in rows:
                r["kappa"] = float(r["kappa"]); r["fracture"] = r["fracture"] == "True"
        rb, pb = refine(a.t, rows, tag, a.outdir)
        if pb:
            print(f"[ts B] t={a.t:+.3f}  refined cells={len(rb)}  -> {pb}")

if __name__ == "__main__":
    main()
