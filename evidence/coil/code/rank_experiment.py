#!/usr/bin/env python3
"""
rank_experiment.py — PREREG-MM1-RANK v1.0 execution.

Records the classifier's PRE-THRESHOLD output:
    Y(g) = [lambda_total, lambda_Q1..Q4] over (kappa x IC),  dim = 5*751*25 = 93875
at the anchor and at g0 +/- h*u, g0 +/- h*v for h in {0.01, 0.005, 0.0025},
then forms central differences, the 2-column matrix M_h, its singular values,
r(h) = sigma2/sigma1, and the finite-difference convergence guard.

Tangent directions (exactly preserve a+b+2c = C, hence A = A0):
    u = (1,-1,0)/sqrt(2)     v = (1,1,-1)/sqrt(3)

Usage:
  python rank_certificate.py                  # gate, must exit 0
  python rank_experiment.py --point anchor
  python rank_experiment.py --point p_u_0.01  (names: p|m _ u|v _ h)
  python rank_experiment.py --all
  python rank_experiment.py --analyze
"""
import argparse, csv, math, os
import numpy as np

A_PAR, DT = 0.03, 0.10
A0 = math.asin(0.9125)/0.9125
C = (1.0 - A0)/4.0
T_ANCHOR = -0.140
ANCHOR = np.array([C/2 + T_ANCHOR, C/2 - T_ANCHOR, 0.0])
U = np.array([1.0, -1.0, 0.0])/math.sqrt(2.0)
V = np.array([1.0, 1.0, -1.0])/math.sqrt(3.0)
HS = [0.01, 0.005, 0.0025]
K_LO, K_HI, D_SURVEY = 0.5, 8.0, 0.01
PHI0 = [0.1, 0.5, 1.0, 2.0, 3.0]
U0 = [0.0, 0.5, -0.5, 2.0, -2.0]
BURN, LYAP, N_IC = 70000, 200000, 25

def points():
    out = {"anchor": ANCHOR.copy()}
    for h in HS:
        for sgn, sl in ((+1, "p"), (-1, "m")):
            out[f"{sl}_u_{h}"] = ANCHOR + sgn*h*U
            out[f"{sl}_v_{h}"] = ANCHOR + sgn*h*V
    return out

def g(p, abc):
    a, b, c = abc
    return (np.sin(p) + a*(np.sin(3*p) - 3*np.sin(p))
            + b*(np.sin(5*p) - 5*np.sin(p)) + c*(np.sin(7*p) - 7*np.sin(p)))

def gp(p, abc):
    a, b, c = abc
    return (np.cos(p) + a*(3*np.cos(3*p) - 3*np.cos(p))
            + b*(5*np.cos(5*p) - 5*np.cos(p)) + c*(7*np.cos(7*p) - 7*np.cos(p)))

def survey_grid():
    n = int(round((K_HI - K_LO)/D_SURVEY)) + 1
    return [round(K_LO + D_SURVEY*i, 6) for i in range(n)]

def guards(name, abc):
    d = float(gp(np.array([0.0]), abc)[0])
    if abs(d - 1.0) > 1e-12:
        raise SystemExit(f"GUARD FAIL {name}: g'(0)={d}")
    phi = np.linspace(0, np.pi, 400001)
    v = g(phi, abc)
    mx = float(np.abs(v).max()); am = float(phi[int(np.argmax(np.abs(v)))])
    if abs(mx - A0) > 1e-9 or abs(am - np.pi/2) > 1e-4:
        raise SystemExit(f"GUARD FAIL {name}: max|g|={mx} at {am/np.pi:.4f}pi")
    inner = v[(phi > 1e-9) & (phi < np.pi - 1e-9)]
    if int(np.sum(inner[:-1]*inner[1:] < 0)) != 0:
        raise SystemExit(f"GUARD FAIL {name}: extra zero in (0,pi)")

def block(abc, kappas):
    """Return (lam_total, quarters) WITHOUT thresholding."""
    m = len(kappas)
    K = np.repeat(np.asarray(kappas, float), N_IC)
    phi = np.tile(np.array([p for p in PHI0 for _ in U0], float), m)
    w = np.tile(np.array([DT*u for _ in PHI0 for u in U0], float), m)
    a = A_PAR
    for _ in range(BURN):
        pn = phi + w
        w = (1 - a)*w - a*K*g(phi, abc)
        phi = pn
    v0 = np.ones_like(phi); v1 = np.zeros_like(phi)
    acc = np.zeros_like(phi); qa = np.zeros_like(phi)
    Q = np.zeros((4, phi.size))
    ql, qi, cnt = LYAP//4, 0, 0
    for _ in range(LYAP):
        d = -a*K*gp(phi, abc)
        n0 = v0 + v1
        n1 = d*v0 + (1 - a)*v1
        nr = np.sqrt(n0*n0 + n1*n1)
        nr = np.where(nr > 0, nr, 1e-300)
        l = np.log(nr)
        acc += l; qa += l; cnt += 1
        v0, v1 = n0/nr, n1/nr
        pn = phi + w
        w = (1 - a)*w - a*K*g(phi, abc)
        phi = pn
        if cnt == ql:
            Q[qi] = qa/ql; qa[:] = 0; cnt = 0; qi += 1
    return (acc/LYAP).reshape(m, N_IC), Q.reshape(4, m, N_IC)

def run_point(name, outdir, block_size=25):
    abc = points()[name]
    guards(name, abc)
    ks = survey_grid()
    rows = []
    for i in range(0, len(ks), block_size):
        chunk = ks[i:i+block_size]
        lam, Qs = block(abc, chunk)
        for j, k in enumerate(chunk):
            for ic in range(N_IC):
                rows.append([k, ic, f"{lam[j, ic]:.12e}"] +
                            [f"{Qs[q, j, ic]:.12e}" for q in range(4)])
        print(f"    [{name}] {min(i+block_size, len(ks))}/{len(ks)} cells", flush=True)
    path = os.path.join(outdir, f"rank_{name}.csv")
    with open(path, "w", newline="") as fh:
        w_ = csv.writer(fh)
        w_.writerow(["kappa", "ic", "lam_total", "q1", "q2", "q3", "q4"])
        w_.writerows(rows)
    print(f"[rank] {name}: abc=({abc[0]:.9f},{abc[1]:.9f},{abc[2]:.9f})  "
          f"rows={len(rows)}  -> {path}")

def load_Y(name, outdir):
    p = os.path.join(outdir, f"rank_{name}.csv")
    if not os.path.exists(p):
        return None
    arr = np.loadtxt(p, delimiter=",", skiprows=1, usecols=(2, 3, 4, 5, 6))
    return arr.reshape(-1)          # flat 5*751*25 in fixed order

def analyze(outdir):
    res = []
    dU, dV = {}, {}
    for h in HS:
        Yp_u, Ym_u = load_Y(f"p_u_{h}", outdir), load_Y(f"m_u_{h}", outdir)
        Yp_v, Ym_v = load_Y(f"p_v_{h}", outdir), load_Y(f"m_v_{h}", outdir)
        if any(x is None for x in (Yp_u, Ym_u, Yp_v, Ym_v)):
            print(f"  h={h}: MISSING runs"); continue
        du = (Yp_u - Ym_u)/(2*h); dv = (Yp_v - Ym_v)/(2*h)
        dU[h], dV[h] = du, dv
        M = np.column_stack([du, dv])
        sv = np.linalg.svd(M, compute_uv=False)
        s1, s2 = float(sv[0]), float(sv[1])
        res.append({"h": h, "sigma1": s1, "sigma2": s2,
                    "r": s2/s1 if s1 > 0 else float("nan"),
                    "s2_over_1e-6_s1": s2 > 1e-6*s1})
        print(f"  h={h:<7} sigma1={s1:.6e}  sigma2={s2:.6e}  r={s2/s1:.6e}  "
              f"above_floor={s2 > 1e-6*s1}")
    conv = []
    for h1, h2 in zip(HS[:-1], HS[1:]):
        if h1 in dU and h2 in dU:
            ru = np.linalg.norm(dU[h1]-dU[h2])/np.linalg.norm(dU[h2])
            rv = np.linalg.norm(dV[h1]-dV[h2])/np.linalg.norm(dV[h2])
            conv.append((h1, h2, ru, rv, ru <= 0.30 and rv <= 0.30))
            print(f"  convergence {h1}->{h2}: rho_u={ru:.4f}  rho_v={rv:.4f}  "
                  f"{'OK' if ru<=0.30 and rv<=0.30 else 'NOT CONVERGED'}")
    converged = bool(conv) and all(c[4] for c in conv)
    rs = [x["r"] for x in res]
    floor_ok = all(x["s2_over_1e-6_s1"] for x in res)
    shrinking = len(rs) >= 2 and all(rs[i+1] < 0.5*rs[i] for i in range(len(rs)-1))
    if not converged:
        verdict = "INCONCLUSIVE"
        note = "finite-difference responses do not converge under step halving"
    elif floor_ok and not shrinking:
        verdict = "R2"
        note = ("smooth local one-scalar factorization FALSIFIED in tested scope; "
                "d_local^{C1} >= 2")
    else:
        verdict = "R1"
        note = "one-scalar factorization NOT falsified; d=1 is NOT proven"
    p = os.path.join(outdir, "rank_summary.csv")
    with open(p, "w", newline="") as fh:
        w_ = csv.writer(fh)
        w_.writerow(["h", "sigma1", "sigma2", "r", "above_floor"])
        for x in res:
            w_.writerow([x["h"], f"{x['sigma1']:.9e}", f"{x['sigma2']:.9e}",
                         f"{x['r']:.9e}", x["s2_over_1e-6_s1"]])
        w_.writerow([])
        w_.writerow(["h1", "h2", "rho_conv_u", "rho_conv_v", "converged"])
        for c in conv:
            w_.writerow([c[0], c[1], f"{c[2]:.6f}", f"{c[3]:.6f}", c[4]])
        w_.writerow([])
        w_.writerow(["VERDICT", verdict, note])
    print(f"\nCONVERGED={converged}   VERDICT: {verdict}\n  {note}\n  -> {p}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--point")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--analyze", action="store_true")
    ap.add_argument("--outdir", default="out_rank")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    if a.analyze:
        analyze(a.outdir); return
    if a.all:
        for nm in points():
            run_point(nm, a.outdir)
        analyze(a.outdir); return
    if a.point:
        if a.point not in points():
            raise SystemExit(f"unknown point; valid: {list(points())}")
        run_point(a.point, a.outdir); return
    raise SystemExit("give --point <name>, --all, or --analyze")

if __name__ == "__main__":
    main()
