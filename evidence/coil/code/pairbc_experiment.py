#!/usr/bin/env python3
"""
pairbc_experiment.py — PREREG-MM1-PAIRBC v1.0.3 execution.

Primary holdout : tri0 x {B, C}   (unseen before the prereg)
Replication     : path3 x {B, C}  (EXPLORE data already seen -> decision-free)
Anchor          : Pair A sentinel classifications only (execution guard)

The primary decision is a pure function of tri0 quantities (decide()); path3
cannot reach it. Pair-A reference thresholds are frozen literals.

Usage:
  python pairbc_certificate.py                          # gate, must exit 0
  python pairbc_experiment.py --anchor                  # sentinel guard, run first
  python pairbc_experiment.py --run tri0 B
  python pairbc_experiment.py --all
  python pairbc_experiment.py --decide
"""
import argparse, csv, math, os
import numpy as np

# ---------------- locked constants (C1) ----------------
A_PAIR  = {"A": 0.030, "B": 0.100, "C": 0.156}
DT_PAIR = {"A": 0.10,  "B": 0.10,  "C": 0.12}
K_LO, K_HI = 0.5, 15.0
D_COARSE, D_FINE = 0.25, 0.025
N_IC, CF_MIN = 25, 15
EPS_LAM, N_QUARTERS = 1e-3, 4
BURN_A = BURN_B = BURN_C = 70000
LYAP_A = LYAP_B = LYAP_C = 200000

# ---------------- frozen Pair-A references (C2/C7) ----------------
KAPPA_A_REF = {"tri0": 2.65, "path3": 2.35}

ANCHOR_SENTINELS = {"path3": {"neg": 2.30, "pos": 2.35},
                    "tri0":  {"neg": 2.60, "pos": 2.65}}

def set_anchor_result(rung, value):
    """Runtime anchor scans are recorded for provenance only. They MUST NOT
    change KAPPA_A_REF — the prereg freezes those as historical constants."""
    _ANCHOR_RUNTIME[rung] = value          # provenance only; never fed to decide()
_ANCHOR_RUNTIME = {}

# ---------------- topology ----------------
ADJ = {"path3": np.array([[0,1,0],[1,0,1],[0,1,0]], float),
       "tri0":  np.array([[0,1,1],[1,0,1],[1,1,0]], float)}

def stiffness_max(rung):
    """DEGREE-NORMALISED stiffness, matching the canonical N3 pipeline.
    Verified against the recorded K*_1 values (Pair A, gamma/dt = 3.0):
        path3 |sigma|max = 2.000 -> K* = 1.5000  (recorded 1.5000)
        tri0  |sigma|max = 1.500 -> K* = 2.0000  (recorded 2.0000)
    An unnormalised Laplacian gives 3.000 for both and does NOT reproduce them."""
    A = ADJ[rung]
    deg = A.sum(1)
    S = np.diag(1.0/deg) @ A - np.eye(A.shape[0])
    return max(abs(np.linalg.eigvals(S)))

def kstar(rung, pair):
    a, dt = A_PAIR[pair], DT_PAIR[pair]
    return (a/dt**2)/stiffness_max(rung)

# ---------------- IC ensemble (C3): dimensionless w0 is the invariant ----------------
def w0_ensemble():
    base = [0.0, 0.05, -0.05, 0.20, -0.20]
    return [(b1, b2) for b1 in base for b2 in base]      # 25 pairs

def u0_for_pair(pair):
    dt = DT_PAIR[pair]
    return [(a/dt, b/dt) for a, b in w0_ensemble()]

def phi0_ensemble():
    return [(0.1, 0.0), (1.0, 0.2), (2.0, -0.3), (0.5, 0.0), (3.0, 0.5)]

# ---------------- dynamics & classifier (C9) ----------------
def _force(th, A):
    """Degree-normalised: f_i = (1/deg_i) sum_j A_ij sin(th_j - th_i)."""
    deg = A.sum(1)
    return np.array([sum(A[i, j]*math.sin(th[j]-th[i]) for j in range(len(th)))/deg[i]
                     for i in range(len(th))])

def chaos_fraction(rung, pair, kappa):
    """CF over the 25-IC grid. per-update lambda + four-quarter persistence."""
    A = ADJ[rung]; n = A.shape[0]
    a, dt = A_PAIR[pair], DT_PAIR[pair]
    K = kappa*kstar(rung, pair)
    burn, lyap = BURN_A, LYAP_A
    ql = lyap//N_QUARTERS
    nch = 0
    ics = [(p, u) for p in phi0_ensemble() for u in u0_for_pair(pair)][:N_IC]
    for (p0, p1), (u0, u1) in ics:
        th = np.array([0.0, p0, p0+p1]); w = np.array([0.0, u0, u1])*dt
        ok = True
        for _ in range(burn):
            tn = th + w; w = (1-a)*w + dt*dt*K*_force(th, A); th = tn
            if not np.all(np.isfinite(th)): ok = False; break
        if not ok: continue
        v = np.zeros(2*n); v[0] = 1.0
        acc = 0.0; q = [0.0]*N_QUARTERS; qi = 0; cnt = 0
        for _ in range(lyap):
            S = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    if A[i, j]: S[i, j] = math.cos(th[j]-th[i])/A.sum(1)[i]
                S[i, i] = -sum(A[i, j]*math.cos(th[j]-th[i]) for j in range(n))/A.sum(1)[i]
            J = np.zeros((2*n, 2*n))
            J[:n, :n] = np.eye(n); J[:n, n:] = np.eye(n)
            J[n:, :n] = dt*dt*K*S; J[n:, n:] = (1-a)*np.eye(n)
            v = J@v; nr = np.linalg.norm(v)
            if nr == 0 or not np.isfinite(nr): ok = False; break
            acc += math.log(nr); q[qi] += math.log(nr)/ql; v /= nr
            tn = th + w; w = (1-a)*w + dt*dt*K*_force(th, A); th = tn
            cnt += 1
            if cnt == ql and qi < N_QUARTERS-1: qi += 1; cnt = 0
        if ok and acc/lyap > EPS_LAM and all(x > EPS_LAM for x in q):
            nch += 1
    return nch/N_IC

# ---------------- locked coarse -> refine search ----------------
def find_threshold(rung, pair, log=print):
    ks = [round(K_LO + D_COARSE*i, 6)
          for i in range(int(round((K_HI-K_LO)/D_COARSE))+1)]
    first = None; prev = None
    for k in ks:
        cf = chaos_fraction(rung, pair, k)
        log(f"    coarse {rung}/{pair} kappa={k:6.3f} CF={cf:.2f}")
        if cf >= CF_MIN/N_IC:
            first = k; break
        prev = k
    if first is None:
        return {"status": "RIGHT-CENSORED", "kappa_frac": None}
    if prev is None:
        return {"status": "LEFT-CENSORED", "kappa_frac": None}
    k = prev
    while k <= first + 1e-9:
        cf = chaos_fraction(rung, pair, round(k, 6))
        log(f"    fine   {rung}/{pair} kappa={k:6.4f} CF={cf:.2f}")
        if cf >= CF_MIN/N_IC:
            return {"status": "measured", "kappa_frac": round(k, 6)}
        k += D_FINE
    return {"status": "measured", "kappa_frac": first}

# ---------------- decision (C5/C6): tri0 quantities ONLY ----------------
def decide(p_bc, r_beta_B, r_beta_C, q_B, q_C, censored):
    """Primary verdict. Accepts ONLY primary-rung quantities."""
    if censored:
        return "P-cens"
    slope_beta = abs(p_bc - 1.0) <= 0.15
    slope_kap  = abs(p_bc) <= 0.15
    lvl_beta = abs(r_beta_B - 1.0) <= 0.15 and abs(r_beta_C - 1.0) <= 0.15
    lvl_kap  = abs(q_B - 1.0) <= 0.15 and abs(q_C - 1.0) <= 0.15
    if slope_beta and lvl_beta: return "P-beta"
    if slope_kap and lvl_kap:   return "P-kappa"
    if 0.15 < p_bc < 0.85:      return "P-ara"
    return "P-other"

def replication_report(primary_label, path3_label, censored):
    """C8: decision-free. Never returns a primary label."""
    if censored or path3_label is None:
        return "REPLICATION-CENSORED"
    return ("REPLICATION-CONCORDANT" if path3_label == primary_label
            else "REPLICATION-DISCORDANT")

def metrics(rung, kB, kC):
    kA = KAPPA_A_REF[rung]                      # frozen literal (C7)
    aA, aB, aC = A_PAIR["A"], A_PAIR["B"], A_PAIR["C"]
    p = math.log(kC/kB)/math.log(aC/aB)
    return {"p_bc": p,
            "r_beta_B": (kB/kA)/(aB/aA), "r_beta_C": (kC/kA)/(aC/aA),
            "q_B": kB/kA, "q_C": kC/kA}

# ---------------- anchor guard (C4) ----------------
def anchor_guard(outdir):
    allok = True
    rows = []
    for rung, s in ANCHOR_SENTINELS.items():
        cf_neg = chaos_fraction(rung, "A", s["neg"])
        cf_pos = chaos_fraction(rung, "A", s["pos"])
        good = cf_neg < CF_MIN/N_IC <= cf_pos
        allok &= good
        rows.append({"rung": rung, "kappa_neg": s["neg"], "CF_neg": f"{cf_neg:.2f}",
                     "kappa_pos": s["pos"], "CF_pos": f"{cf_pos:.2f}",
                     "sentinel": "PASS" if good else "FAIL"})
        print(f"  anchor {rung}: CF({s['neg']})={cf_neg:.2f} (<0.60?)  "
              f"CF({s['pos']})={cf_pos:.2f} (>=0.60?)  -> {'PASS' if good else 'FAIL'}")
    _write(rows, outdir, "pairbc_anchor.csv")
    return allok

def _write(rows, outdir, name):
    p = os.path.join(outdir, name)
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"  -> {p}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--anchor", action="store_true")
    ap.add_argument("--run", nargs=2, metavar=("RUNG", "PAIR"))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--decide", action="store_true")
    ap.add_argument("--outdir", default="out_pairbc")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)

    if a.anchor:
        ok = anchor_guard(a.outdir)
        print("\nANCHOR GUARD:", "PASS" if ok else "FAIL — pipeline denetlenmeli, koşu durur")
        raise SystemExit(0 if ok else 1)

    def one(rung, pair):
        r = find_threshold(rung, pair)
        _write([{"rung": rung, "pair": pair, "status": r["status"],
                 "kappa_frac": r["kappa_frac"] if r["kappa_frac"] else ""}],
               a.outdir, f"pairbc_{rung}_{pair}.csv")
        print(f"[pairbc] {rung}/{pair}: {r['status']}  kappa_frac={r['kappa_frac']}")

    if a.run:  one(a.run[0], a.run[1]); return
    if a.all:
        for rung in ("tri0", "path3"):
            for pair in ("B", "C"): one(rung, pair)
        return
    if a.decide:
        def load(rung, pair):
            p = os.path.join(a.outdir, f"pairbc_{rung}_{pair}.csv")
            r = list(csv.DictReader(open(p)))[0]
            return r["status"], (float(r["kappa_frac"]) if r["kappa_frac"] else None)
        sT_B, kT_B = load("tri0", "B"); sT_C, kT_C = load("tri0", "C")
        cens_T = (sT_B != "measured") or (sT_C != "measured")
        if cens_T:
            label = decide(0, 1, 1, 1, 1, censored=True); m = {}
        else:
            m = metrics("tri0", kT_B, kT_C)
            label = decide(m["p_bc"], m["r_beta_B"], m["r_beta_C"],
                           m["q_B"], m["q_C"], censored=False)
        try:
            sP_B, kP_B = load("path3", "B"); sP_C, kP_C = load("path3", "C")
            cens_P = (sP_B != "measured") or (sP_C != "measured")
            if cens_P: plabel = None
            else:
                mp = metrics("path3", kP_B, kP_C)
                plabel = decide(mp["p_bc"], mp["r_beta_B"], mp["r_beta_C"],
                                mp["q_B"], mp["q_C"], censored=False)
        except FileNotFoundError:
            cens_P, plabel = True, None
        rep = replication_report(label, plabel, cens_P)
        print("\n=== PRIMARY (tri0 only) ===")
        for k, v in m.items(): print(f"  {k} = {v:+.5f}")
        print(f"  VERDICT: {label}")
        print(f"\n=== REPLICATION (path3, decision-free) ===\n  {rep}")
        _write([{"verdict": label, "replication": rep,
                 **{k: f"{v:.6f}" for k, v in m.items()}}],
               a.outdir, "pairbc_summary.csv")
        return
    raise SystemExit("give --anchor, --run RUNG PAIR, --all, or --decide")

if __name__ == "__main__":
    main()
