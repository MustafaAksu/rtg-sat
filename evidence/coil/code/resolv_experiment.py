#!/usr/bin/env python3
"""
resolv_experiment.py — PREREG-MM1-RESOLVABILITY v1.0 execution.

Measures the stratified derivative-resolvability radius

    E_{T,s,d}(h) = || D_FD - D_sens ||_s / || D_sens ||_s
    h_res^{s,d}(T) = max{ h : E <= eps }

on the RANK observable Y = [lam_total, lam_Q1..Q4] over (kappa x IC), with the
RANK burn:lya ratio 7:20 preserved:  B = 70*2^m, L = 200*2^m, T = 270*2^m.

Strata are frozen from the ANCHOR baseline classification (a kappa is 'chaos' if
the anchor has >=1 chaotic IC there), never re-derived from perturbed waveforms.

Usage:
  python resolv_certificate.py
  python resolv_experiment.py --m 0 --dir u
  python resolv_experiment.py --all
  python resolv_experiment.py --summary
"""
import argparse, csv, math, os
import numpy as np

A_PAR, DT = 0.03, 0.10
A0 = math.asin(0.9125)/0.9125
C = (1.0 - A0)/4.0
ANCHOR = np.array([C/2 - 0.140, C/2 + 0.140, 0.0])
DIRS = {"u": np.array([1.0, -1.0, 0.0])/math.sqrt(2.0),
        "v": np.array([1.0, 1.0, -1.0])/math.sqrt(3.0)}
MS = list(range(7))                      # T = 270*2^m
K_LO, K_HI, DK = 0.5, 8.0, 0.01
PHI0 = [0.1, 0.5, 1.0, 2.0, 3.0]
U0 = [0.0, 0.5, -0.5, 2.0, -2.0]
N_IC = 25
EPS_PRIMARY = 0.10
EPS_SECONDARY = [0.05, 0.20]
HJ_PRIMARY = [0.01*2.0**(-j) for j in range(21)]
HJ_EXT = [0.01*2.0**(-j) for j in range(21, 41)]   # addendum v1.0.1: deterministic
HJ = HJ_PRIMARY + HJ_EXT
EXTRA_HALVINGS = 3
SMALL_SENS = 1e-12
CHAOS_EPS = 1e-3                          # only to FREEZE strata from the anchor

def BL(m):
    return 70*2**m, 200*2**m

def grid():
    n = int(round((K_HI - K_LO)/DK)) + 1
    return np.array([round(K_LO + DK*i, 6) for i in range(n)])

def hk(p, k):
    return np.sin(k*p) - k*np.sin(p)

def g(p, abc):
    return np.sin(p) + abc[0]*hk(p, 3) + abc[1]*hk(p, 5) + abc[2]*hk(p, 7)

def g1(p, abc):
    return (np.cos(p) + abc[0]*(3*np.cos(3*p) - 3*np.cos(p))
            + abc[1]*(5*np.cos(5*p) - 5*np.cos(p))
            + abc[2]*(7*np.cos(7*p) - 7*np.cos(p)))

def g2(p, abc):
    return (-np.sin(p) + abc[0]*(-9*np.sin(3*p) + 3*np.sin(p))
            + abc[1]*(-25*np.sin(5*p) + 5*np.sin(p))
            + abc[2]*(-49*np.sin(7*p) + 7*np.sin(p)))

def dg(p, d):
    return d[0]*hk(p, 3) + d[1]*hk(p, 5) + d[2]*hk(p, 7)

def dg1(p, d):
    return (d[0]*(3*np.cos(3*p) - 3*np.cos(p)) + d[1]*(5*np.cos(5*p) - 5*np.cos(p))
            + d[2]*(7*np.cos(7*p) - 7*np.cos(p)))

def guards(abc, tag):
    if abs(float(g1(np.array([0.0]), abc)[0]) - 1.0) > 1e-12:
        raise SystemExit(f"GUARD FAIL {tag}: g'(0)")
    phi = np.linspace(0, np.pi, 200001)
    v = g(phi, abc)
    if abs(float(np.abs(v).max()) - A0) > 1e-9:
        raise SystemExit(f"GUARD FAIL {tag}: max|g|")
    inner = v[(phi > 1e-9) & (phi < np.pi - 1e-9)]
    if int(np.sum(inner[:-1]*inner[1:] < 0)) != 0:
        raise SystemExit(f"GUARD FAIL {tag}: extra zero")

def _init(ks):
    m = len(ks)
    K = np.repeat(np.asarray(ks, float), N_IC)
    phi = np.tile(np.array([p for p in PHI0 for _ in U0], float), m)
    w = np.tile(np.array([DT*u for _ in PHI0 for u in U0], float), m)
    return K, phi, w

def observable(abc, ks, B, L, return_quarters=False):
    """Y = [lam_total, lam_Q1..Q4] flattened. No thresholding."""
    K, phi, w = _init(ks)
    a = A_PAR
    for _ in range(B):
        pn = phi + w; w = (1 - a)*w - a*K*g(phi, abc); phi = pn
    v0 = np.ones_like(phi); v1 = np.zeros_like(phi)
    acc = np.zeros_like(phi); qa = np.zeros_like(phi)
    Q = np.zeros((4, phi.size))
    ql, qi, cnt = L//4, 0, 0
    for _ in range(L):
        d = -a*K*g1(phi, abc)
        n0 = v0 + v1; n1 = d*v0 + (1 - a)*v1
        nr = np.sqrt(n0*n0 + n1*n1); nr = np.where(nr > 0, nr, 1e-300)
        l = np.log(nr); acc += l; qa += l; cnt += 1
        v0, v1 = n0/nr, n1/nr
        pn = phi + w; w = (1 - a)*w - a*K*g(phi, abc); phi = pn
        if cnt == ql:
            Q[qi] = qa/ql; qa[:] = 0; cnt = 0; qi += 1
    lam = acc/L
    Y = np.concatenate([lam, Q.reshape(-1)])
    if return_quarters:
        return Y, lam.reshape(len(ks), N_IC), Q.reshape(4, len(ks), N_IC)
    return Y, lam.reshape(len(ks), N_IC)

def sensitivity(abc, dvec, ks, B, L):
    """Direct D_theta Y by forward sensitivity (state + Lyapunov layer)."""
    K, phi, w = _init(ks)
    a = A_PAR
    p = np.zeros_like(phi); q = np.zeros_like(phi)
    for _ in range(B):
        gp = g1(phi, abc)
        pn = phi + w; wn = (1 - a)*w - a*K*g(phi, abc)
        p, q = p + q, (1 - a)*q - a*K*(gp*p + dg(phi, dvec))
        phi, w = pn, wn
        if not np.all(np.isfinite(p)):
            return None, None
    z0 = np.ones_like(phi); z1 = np.zeros_like(phi)
    e0 = np.zeros_like(phi); e1 = np.zeros_like(phi)
    dacc = np.zeros_like(phi); dQ = np.zeros((4, phi.size)); qa = np.zeros_like(phi)
    ql, qi, cnt = L//4, 0, 0
    for _ in range(L):
        gp = g1(phi, abc)
        j10 = -a*K*gp
        jd10 = -a*K*(g2(phi, abc)*p + dg1(phi, dvec))
        r0 = z0 + z1
        r1 = j10*z0 + (1 - a)*z1
        rd0 = e0 + e1
        rd1 = jd10*z0 + j10*e0 + (1 - a)*e1
        al = np.sqrt(r0*r0 + r1*r1)
        if np.any(al <= 0.0):
            return None, None      # tangent collapse: exactness condition violated

        zn0, zn1 = r0/al, r1/al
        ald = zn0*rd0 + zn1*rd1
        contrib = ald/al
        dacc += contrib; qa += contrib; cnt += 1
        e0 = (rd0 - zn0*ald)/al
        e1 = (rd1 - zn1*ald)/al
        z0, z1 = zn0, zn1
        pn = phi + w; wn = (1 - a)*w - a*K*g(phi, abc)
        p, q = p + q, (1 - a)*q - a*K*(gp*p + dg(phi, dvec))
        phi, w = pn, wn
        if cnt == ql:
            dQ[qi] = qa/ql; qa[:] = 0; cnt = 0; qi += 1
        if not np.all(np.isfinite(dacc)):
            return None, None
    D = np.concatenate([dacc/L, dQ.reshape(-1)])
    return (D, True) if np.all(np.isfinite(D)) else (None, None)

def canonical_classifier(lam, Q):
    """CANONICAL programme CHAOS rule (unit-testable, no source introspection):
       C_ki = (lam_ki > 1e-3) AND (all four quarter values > 1e-3);  chaos_k = any_i C_ki."""
    C = (lam > CHAOS_EPS) & np.all(Q > CHAOS_EPS, axis=0)
    return C.any(axis=1)

def strata_masks(ks):
    """Freeze strata from the ANCHOR baseline at the ORIGINAL RANK horizon,
    using the CANONICAL programme classifier:
        C_ki = (lam_ki > 1e-3) AND (all four quarter values > 1e-3)
        chaos_k = exists i : C_ki
    (An earlier draft used lam only; that is NOT the inherited definition.)"""
    _, lam, Q = observable(ANCHOR, ks, 70000, 200000, return_quarters=True)
    chaos_k = canonical_classifier(lam, Q)
    nk = len(ks)
    def expand(mk):
        cell = np.repeat(mk, N_IC)
        return np.concatenate([cell] + [cell]*4)
    return {"all": np.ones(nk*N_IC*5, dtype=bool),
            "chaos": expand(chaos_k), "regular": expand(~chaos_k)}, chaos_k

ROW_FIELDS = ["T", "B", "L", "dir", "stratum", "status", "h_res", "eps",
              "S_norm", "C_chaos", "N90"] + [f"h_res_eps{e}" for e in EPS_SECONDARY]

def make_row(T, B, L, dname, stratum, status, h_res="", S_norm="", C_chaos="",
             N90="", eps_sec=None):
    """Single row factory: every row-producing path goes through here, so the CSV
    schema is rectangular no matter which branch wrote it."""
    r = {"T": T, "B": B, "L": L, "dir": dname, "stratum": stratum,
         "status": status, "h_res": h_res, "eps": EPS_PRIMARY,
         "S_norm": S_norm, "C_chaos": C_chaos, "N90": N90}
    for e in EPS_SECONDARY:
        r[f"h_res_eps{e}"] = (eps_sec or {}).get(e, "")
    return r

def snorm(x):
    """Scaled L2 norm: survives |x| ~ 1e300 where x**2 would overflow."""
    if x.size == 0:
        return 0.0
    mx = float(np.max(np.abs(x)))
    if not np.isfinite(mx):
        return float("inf")
    if mx == 0.0:
        return 0.0
    return mx*float(np.sqrt(np.sum((x/mx)**2)))

def run(m, dname, outdir, masks):
    B, L = BL(m); T = B + L
    dvec = DIRS[dname]
    ks = grid()
    guards(ANCHOR, "anchor")
    D, ok = sensitivity(ANCHOR, dvec, ks, B, L)
    rows = []
    if D is None:
        for s in ("all", "regular", "chaos"):
            rows.append(make_row(T, B, L, dname, s, "SENSITIVITY-NUMERIC-CENSORED"))
        print(f"[resolv] T={T} d={dname}: SENSITIVITY-NUMERIC-CENSORED")
        _write(rows, outdir, T, dname)
        return True
    else:
        Sn = {s: snorm(D[masks[s]]) for s in masks}
        if any(not np.isfinite(Sn[s]) for s in masks):
            # scaled norm itself not representable -> precision overflow, NOT a small radius
            rows = [make_row(T, B, L, dname, st, "SENSITIVITY-NUMERIC-CENSORED",
                             S_norm="inf") for st in ("all", "regular", "chaos")]
            print(f"[resolv] T={T} d={dname}: SENSITIVITY-NUMERIC-CENSORED (norm overflow)")
            _write(rows, outdir, T, dname)
            return True
        Cch = ((Sn["chaos"]/Sn["all"])**2 if (Sn["all"] > 0 and np.isfinite(Sn["all"]))
               else float("nan"))
        mx = float(np.max(np.abs(D)))
        if not np.isfinite(mx) or mx == 0.0:
            N90 = -1
        else:
            ws = np.sort((np.abs(D)/mx)**2)[::-1]
            tot = float(np.sum(ws))
            N90 = int(np.searchsorted(np.cumsum(ws), 0.90*tot) + 1)
        E = {s: [] for s in masks}
        found = {s: None for s in masks}
        extra = {s: 0 for s in masks}
        for j, h in enumerate(HJ):
            for sgn in (+1, -1):
                pass
            Yp, _ = observable(ANCHOR + h*dvec, ks, B, L)
            Ym, _ = observable(ANCHOR - h*dvec, ks, B, L)
            fd = (Yp - Ym)/(2*h)
            for s in masks:
                mk = masks[s]
                den = Sn[s]
                if den < SMALL_SENS:
                    continue
                e = snorm(fd[mk] - D[mk])/den
                E[s].append((h, e))
                if found[s] is None and e <= EPS_PRIMARY:
                    found[s] = h
                elif found[s] is not None:
                    extra[s] += 1
            if all((found[s] is not None and extra[s] >= EXTRA_HALVINGS)
                   for s in masks if Sn[s] >= SMALL_SENS):
                break
        for s in ("all", "regular", "chaos"):
            if Sn[s] < SMALL_SENS:
                st, hres = "UNDEFINED-small-sensitivity", ""
            elif found[s] is None:
                st, hres = "LEFT-CENSORED", f"<{HJ[len(E[s])-1]:.3e}"
            elif abs(found[s] - HJ[0]) < 1e-15:
                st, hres = "RIGHT-CENSORED", f">={HJ[0]:.3e}"
            else:
                st, hres = "measured", f"{found[s]:.6e}"
            sec = {}
            for ee in EPS_SECONDARY:
                hh = next((h for h, e in E[s] if e <= ee), None)
                if hh is not None:
                    sec[ee] = f"{hh:.6e}"
                elif E[s]:
                    sec[ee] = f"SECONDARY-CENSORED:<{E[s][-1][0]:.3e}"
                else:
                    sec[ee] = "UNDEFINED-small-sensitivity"
            row = make_row(T, B, L, dname, s, st, h_res=hres,
                           S_norm=f"{Sn[s]:.6e}", C_chaos=f"{Cch:.6e}",
                           N90=N90, eps_sec=sec)
            rows.append(row)
            print(f"[resolv] T={T} d={dname} {s:>7}: {st:28s} h_res={hres}")
        pe = os.path.join(outdir, f"resolv_E_T{T}_{dname}.csv")
        with open(pe, "w", newline="") as fh:
            wr = csv.writer(fh); wr.writerow(["stratum", "h", "E"])
            for s in E:
                for h, e in E[s]:
                    wr.writerow([s, f"{h:.9e}", f"{e:.9e}"])
    _write(rows, outdir, T, dname)
    return False

def _write(rows, outdir, T, dname):
    p = os.path.join(outdir, f"resolv_T{T}_{dname}.csv")
    with open(p, "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=ROW_FIELDS, extrasaction="ignore")
        wr.writeheader(); wr.writerows(rows)

def _hres_info(r):
    """(kind, value) with kind in {measured, left, right, undef, censored}."""
    st = r["status"]
    if st == "measured":
        return ("measured", float(r["h_res"]))
    if st == "LEFT-CENSORED":
        return ("left", float(r["h_res"].lstrip("<")))       # h_res < value
    if st == "RIGHT-CENSORED":
        return ("right", float(r["h_res"].lstrip(">=")))     # h_res >= value
    if st == "UNDEFINED-small-sensitivity":
        return ("undef", None)
    return ("censored", None)

def _crossed(kind, val, thr=0.0025):
    """Did h_res drop below thr?  True / False / None(unresolved)."""
    if kind == "measured":
        return val < thr
    if kind == "left":
        return True if val <= thr else None     # h_res < val; if val<=thr it crossed
    if kind == "right":
        return False if val >= thr else None    # h_res >= val
    return None

def _min_over_dirs(infos):
    """Censor-aware min over directions (prereg: h_res^s = min_d h_res^{s,d})."""
    kinds = [k for k, _ in infos]
    if any(k == "censored" for k in kinds):
        return ("UNRESOLVED", "")
    usable = [(k, v) for k, v in infos if k != "undef"]
    if not usable:
        return ("UNDEFINED-small-sensitivity", "")
    if any(k == "left" for k, _ in usable):
        b = min(v for k, v in usable if k == "left")
        return ("LEFT-CENSORED", f"<{b:.6e}")
    meas = [v for k, v in usable if k == "measured"]
    if meas:
        return ("measured", f"{min(meas):.6e}")
    b = min(v for k, v in usable if k == "right")
    return ("RIGHT-CENSORED", f">={b:.6e}")

def summary(outdir):
    rows = []
    for f in sorted(os.listdir(outdir)):
        if f.startswith("resolv_T") and f.endswith(".csv") and "_E_" not in f:
            rows += list(csv.DictReader(open(os.path.join(outdir, f))))
    if not rows:
        raise SystemExit("no result files")
    rows.sort(key=lambda r: (int(r["T"]), r["dir"], r["stratum"]))
    p = os.path.join(outdir, "resolv_summary.csv")
    with open(p, "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=ROW_FIELDS, extrasaction="ignore")
        wr.writeheader()
        for r in rows:
            wr.writerow({k: r.get(k, "") for k in ROW_FIELDS})
    print(f"{'T':>7} {'dir':>4} {'stratum':>8} {'status':>30} {'h_res':>14} {'S_norm':>12}")
    for r in rows:
        print(f"{r['T']:>7} {r['dir']:>4} {r['stratum']:>8} {r['status']:>30} "
              f"{r['h_res']:>14} {r['S_norm']:>12}")

    # program-level min over directions (prereg-locked aggregation)
    Ts = sorted({int(r["T"]) for r in rows})
    agg = []
    print(f"\nProgram-level h_res^s(T) = min over {{u,v}} (censor-aware):")
    print(f"{'T':>7} {'stratum':>8} {'status':>26} {'h_res':>14}")
    for T in Ts:
        for s in ("all", "regular", "chaos"):
            infos = [_hres_info(r) for r in rows
                     if int(r["T"]) == T and r["stratum"] == s]
            if not infos:
                continue
            st, hv = _min_over_dirs(infos)
            agg.append({"T": T, "stratum": s, "status": st, "h_res_min_dir": hv})
            print(f"{T:>7} {s:>8} {st:>26} {hv:>14}")
    pa = os.path.join(outdir, "resolv_program_level.csv")
    with open(pa, "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=["T", "stratum", "status", "h_res_min_dir"])
        wr.writeheader(); wr.writerows(agg)

    # censor-aware T_cross
    print("\nT_cross (first T with h_res < 0.0025); censor-aware:")
    for s in ("all", "regular", "chaos"):
        for d in ("u", "v"):
            verdict = "not reached in ladder"
            for r in rows:
                if r["stratum"] != s or r["dir"] != d:
                    continue
                k, v = _hres_info(r)
                c = _crossed(k, v)
                if c is True:
                    verdict = f"T={r['T']}"
                    break
                if c is None and k == "censored":
                    verdict = "UNRESOLVED (numeric censor)"
                    break
                if k == "undef":
                    # h_res undefined at this T -> the FIRST crossing can no longer be located
                    verdict = "UNRESOLVED (small sensitivity)"
                    break
            print(f"  {s:>7} {d}: {verdict}")
    print(f"  -> {p}\n  -> {pa}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", type=int)
    ap.add_argument("--dir", choices=list(DIRS))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--outdir", default="out_resolv")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    if a.summary:
        summary(a.outdir); return
    print("freezing strata from anchor baseline (original RANK horizon)...", flush=True)
    masks, chaos_k = strata_masks(grid())
    print(f"  chaos kappas: {int(chaos_k.sum())}/{len(chaos_k)}", flush=True)
    if a.all:
        censored = {d: False for d in DIRS}
        for m in MS:
            for d in DIRS:
                if censored[d]:
                    B_, L_ = BL(m); T_ = B_ + L_
                    ph = [make_row(T_, B_, L_, d, st, "SENSITIVITY-NUMERIC-CENSORED")
                          for st in ("all", "regular", "chaos")]
                    _write(ph, a.outdir, T_, d)
                    print(f"[resolv] T={T_} d={d}: SENSITIVITY-NUMERIC-CENSORED "
                          f"(propagated from a lower T; prereg: 'that T and above')")
                    continue
                if run(m, d, a.outdir, masks):
                    censored[d] = True
        summary(a.outdir); return
    if a.m is None or a.dir is None:
        raise SystemExit("give --m <0..6> --dir u|v, or --all, or --summary")
    run(a.m, a.dir, a.outdir, masks)

if __name__ == "__main__":
    main()
