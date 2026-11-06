#!/usr/bin/env python3
"""
isoa_experiment.py — PREREG-MM1-WAVEFORM-ISOA v1.0 execution.

Locked protocol (do not modify):
  a = gamma*dt = 0.03 ; reduced dyad  phi+ = phi + w ; w+ = (1-a)w - a*kappa*g_t(phi)
  25 ICs: phi0 in {0.1,0.5,1,2,3} x u0 in {0,+-0.5,+-2}, w0 = dt*u0, dt = 0.10
  burn-in 70,000 ; Lyapunov 200,000 (per-update)
  CHAOS iff lambda_max > 1e-3 AND all four quarter values > 1e-3
  FRACTURE iff CHAOS >= 15/25 (60%)
  kappa scan: 2.535 +- 0.16, step 0.005  (65 cells per waveform)

Usage:
  python isoa_certificate.py                 # gate: must exit 0 first
  python isoa_experiment.py --t -0.300       # one waveform
  python isoa_experiment.py --all            # all six, sequential
Outputs: out_isoa/isoa_t<TAG>.csv  (one row per kappa cell)
"""
import argparse, csv, math, os
import numpy as np

A_PAR, DT = 0.03, 0.10
A0 = math.asin(0.9125)/0.9125
C  = (1.0 - A0)/4.0
T_LOCKED = [-0.300, -0.220, -0.140, -0.060, 0.000, 0.008]
KAP_C, KAP_HALF, KAP_STEP = 2.535, 0.16, 0.005
PHI0 = [0.1, 0.5, 1.0, 2.0, 3.0]
U0   = [0.0, 0.5, -0.5, 2.0, -2.0]
BURN, LYAP, EPS = 70000, 200000, 1e-3

def g(phi, t):
    a, b = C/2 + t, C/2 - t
    return np.sin(phi) + a*(np.sin(3*phi) - 3*np.sin(phi)) + b*(np.sin(5*phi) - 5*np.sin(phi))

def gp(phi, t):
    a, b = C/2 + t, C/2 - t
    return np.cos(phi) + a*(3*np.cos(3*phi) - 3*np.cos(phi)) + b*(5*np.cos(5*phi) - 5*np.cos(phi))

def guard(t):
    """Locked pre-run guards (prereg section 6)."""
    d = float(gp(np.array([0.0]), t)[0])
    if abs(d - 1.0) > 1e-9:
        raise SystemExit(f"GUARD FAIL t={t}: g'(0)={d}")
    phi = np.linspace(0, np.pi, 400001)
    v = g(phi, t)
    if abs(np.abs(v).max() - A0) > 1e-9:
        raise SystemExit(f"GUARD FAIL t={t}: max|g|={np.abs(v).max()} != A0={A0}")
    inner = v[(phi > 1e-9) & (phi < np.pi - 1e-9)]
    if int(np.sum(inner[:-1]*inner[1:] < 0)) != 0:
        raise SystemExit(f"GUARD FAIL t={t}: extra zero in (0,pi) -> well-structure confound")

def cell(t, kappa):
    a, k = A_PAR, kappa
    phi = np.array([p for p in PHI0 for _ in U0], float)
    w   = np.array([DT*u for _ in PHI0 for u in U0], float)
    for _ in range(BURN):
        phin = phi + w
        w = (1 - a)*w - a*k*g(phi, t)
        phi = phin
        if not np.all(np.isfinite(phi)):
            break
    v0 = np.ones_like(phi); v1 = np.zeros_like(phi)
    acc = np.zeros_like(phi); q_acc = np.zeros_like(phi)
    quarters = np.zeros((4, phi.size))
    qlen, qi, cnt = LYAP//4, 0, 0
    for _ in range(LYAP):
        d = -a*k*gp(phi, t)
        nv0 = v0 + v1
        nv1 = d*v0 + (1 - a)*v1
        nrm = np.sqrt(nv0*nv0 + nv1*nv1)
        nrm = np.where(nrm > 0, nrm, 1e-300)
        l = np.log(nrm)
        acc += l; q_acc += l; cnt += 1
        v0, v1 = nv0/nrm, nv1/nrm
        phin = phi + w
        w = (1 - a)*w - a*k*g(phi, t)
        phi = phin
        if cnt == qlen:
            quarters[qi] = q_acc/qlen; q_acc[:] = 0; cnt = 0; qi += 1
    lam = acc/LYAP
    chaos = (lam > EPS) & np.all(quarters > EPS, axis=0)
    return int(chaos.sum()), float(np.nanmax(lam)), float(np.nanmedian(lam))

def run(t, outdir):
    guard(t)
    tag = f"{t:+.3f}".replace('.', 'p')
    path = os.path.join(outdir, f"isoa_t{tag}.csv")
    n_cells = int(round(2*KAP_HALF/KAP_STEP)) + 1
    hits = []
    with open(path, "w", newline="") as fh:
        w_ = csv.writer(fh)
        w_.writerow(["t", "kappa", "A0", "chi", "n_chaos", "fracture", "lam_max", "lam_median"])
        for i in range(n_cells):
            kap = round(KAP_C - KAP_HALF + KAP_STEP*i, 4)
            n, lmax, lmed = cell(t, kap)
            fr = n >= 15
            if fr:
                hits.append(kap)
            w_.writerow([t, kap, f"{A0:.10f}", f"{kap*A0:.6f}", n, fr,
                         f"{lmax:.6f}", f"{lmed:.6f}"])
    near = min(hits, key=lambda k: abs(k - KAP_C)) if hits else None
    print(f"[isoa] t={t:+.3f}  cells={n_cells}  FRACTURE cells={len(hits)}  "
          f"kappa_near={near}  -> {path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=float)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--outdir", default="out_isoa")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    if a.all:
        for t in T_LOCKED:
            run(t, a.outdir)
    elif a.t is not None:
        if not any(abs(a.t - x) < 1e-12 for x in T_LOCKED):
            raise SystemExit(f"t={a.t} is not in the locked set {T_LOCKED}")
        run(a.t, a.outdir)
    else:
        raise SystemExit("give --t <value> or --all")

if __name__ == "__main__":
    main()
