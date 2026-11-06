#!/usr/bin/env python3
"""
ortho_experiment.py — PREREG-MM1-WAVEFORM-ORTHO v1.0 execution.

Seven-harmonic family:  g = sin(phi) + a*h3 + b*h5 + c*h7 ,  h_k = sin(k phi) - k sin(phi)
  g'(0) = 1 for every (a,b,c);  g(pi/2) = 1 - 4a - 4b - 8c  ->  amplitude constraint a+b+2c = C
  a1 = 1 - 3a - 5b - 7c ;  H_high = (a^2+b^2+c^2)/(a1^2+a^2+b^2+c^2) ;  c3 = -1/6 - 4a - 20b - 56c

  Arm A (c3 exactly fixed, H_high varies):  a = a0+s, b = b0-3s, c = s
  Arm B (H_high exactly fixed, c3 varies):  locked (a,b,c) triples from the prereg table

Anchor is shared by both arms and is run ONCE.

Primary output: survey mask B_w over the common 751-cell grid and
D_mask(anchor, w) = |B_anchor XOR B_w| / 751.  Decision uses only D_mask == 0 vs > 0.

Usage:
  python ortho_certificate.py                 # gate, must exit 0
  python ortho_experiment.py --run anchor
  python ortho_experiment.py --run A1 ... A4 / B1 ... B4
  python ortho_experiment.py --all
  python ortho_experiment.py --summary
"""
import argparse, csv, math, os
import numpy as np

A_PAR, DT = 0.03, 0.10
A0 = math.asin(0.9125)/0.9125
C = (1.0 - A0)/4.0
K_LO, K_HI, D_SURVEY = 0.5, 8.0, 0.01
PHI0 = [0.1, 0.5, 1.0, 2.0, 3.0]
U0 = [0.0, 0.5, -0.5, 2.0, -2.0]
BURN, LYAP, EPS, N_IC, CF_MIN = 70000, 200000, 1e-3, 25, 15
BLOCK = 25

# Anchor is DERIVED exactly from the iso-A family at t = -0.140 (not from rounded
# table values): a = C/2 + t, b = C/2 - t, c = 0.  The prereg tables are display
# roundings; exact construction is the source of truth.
T_ANCHOR = -0.140
A_ANCHOR = C/2 + T_ANCHOR
B_ANCHOR = C/2 - T_ANCHOR

def _H_c3(a, b, c):
    a1 = 1 - 3*a - 5*b - 7*c
    return ((a*a + b*b + c*c)/(a1*a1 + a*a + b*b + c*c),
            -1/6 - 4*a - 20*b - 56*c)

C3_ANCHOR = _H_c3(A_ANCHOR, B_ANCHOR, 0.0)[1]
H0 = _H_c3(A_ANCHOR, B_ANCHOR, 0.0)[0]

def arm_A(s):
    """c3 exactly invariant: its s-coefficient is -4 + 60 - 56 = 0."""
    return (A_ANCHOR + s, B_ANCHOR - 3*s, s)

def arm_B(c, tol=1e-15, iters=200):
    """Solve H_high(b, c) = H0 exactly on the branch through the anchor, with the
    amplitude constraint a = C - b - 2c held exactly. Pure bisection (no scipy)."""
    f = lambda bb: _H_c3(C - bb - 2*c, bb, c)[0] - H0
    lo, hi = B_ANCHOR, B_ANCHOR
    step = 1e-4
    # expand around the anchor's b until a sign change appears on the anchor branch
    for _ in range(200000):
        if f(lo)*f(hi) < 0:
            break
        lo -= step; hi += step
    else:
        raise SystemExit(f"arm_B: no bracket found for c={c}")
    if f(lo)*f(hi) > 0:
        raise SystemExit(f"arm_B: no bracket found for c={c}")
    for _ in range(iters):
        mid = 0.5*(lo + hi)
        if f(lo)*f(mid) <= 0:
            hi = mid
        else:
            lo = mid
        if hi - lo < tol:
            break
    b = 0.5*(lo + hi)
    return (C - b - 2*c, b, c)

ARM_A = {"A1": arm_A(-0.080), "A2": arm_A(-0.040),
         "A3": arm_A(+0.020), "A4": arm_A(+0.040)}
ARM_B = {"B1": arm_B(-0.100), "B2": arm_B(-0.050),
         "B3": arm_B(+0.030), "B4": arm_B(+0.060)}
ANCHOR = {"anchor": (A_ANCHOR, B_ANCHOR, 0.0)}
ALL = {**ANCHOR, **ARM_A, **ARM_B}

def g(p, abc):
    a, b, c = abc
    return (np.sin(p) + a*(np.sin(3*p) - 3*np.sin(p))
            + b*(np.sin(5*p) - 5*np.sin(p)) + c*(np.sin(7*p) - 7*np.sin(p)))

def gp(p, abc):
    a, b, c = abc
    return (np.cos(p) + a*(3*np.cos(3*p) - 3*np.cos(p))
            + b*(5*np.cos(5*p) - 5*np.cos(p)) + c*(7*np.cos(7*p) - 7*np.cos(p)))

def descriptors(abc):
    a, b, c = abc
    a1 = 1 - 3*a - 5*b - 7*c
    H = (a*a + b*b + c*c)/(a1*a1 + a*a + b*b + c*c)
    c3 = -1/6 - 4*a - 20*b - 56*c
    return a1, H, c3

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
        raise SystemExit(f"GUARD FAIL {name}: max|g|={mx} at {am}")
    inner = v[(phi > 1e-9) & (phi < np.pi - 1e-9)]
    if int(np.sum(inner[:-1]*inner[1:] < 0)) != 0:
        raise SystemExit(f"GUARD FAIL {name}: extra zero in (0,pi)")
    _, H, c3 = descriptors(abc)
    if name.startswith("A") and abs(c3 - C3_ANCHOR) > 1e-10:
        raise SystemExit(f"GUARD FAIL {name}: Arm-A c3={c3} != anchor {C3_ANCHOR}")
    if name.startswith("B") and abs(H - H0) > 1e-6:
        raise SystemExit(f"GUARD FAIL {name}: Arm-B H_high={H} != H0 {H0}")

def block(abc, kappas):
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
    lam = (acc/LYAP).reshape(m, N_IC)
    ch = (lam > EPS) & np.all((Q > EPS).reshape(4, m, N_IC), axis=0)
    return ch.sum(axis=1), lam

def run_one(name, outdir):
    abc = ALL[name]
    guards(name, abc)
    a1, H, c3 = descriptors(abc)
    ks = survey_grid()
    rows = []
    for i in range(0, len(ks), BLOCK):
        chunk = ks[i:i+BLOCK]
        n, lam = block(abc, chunk)
        for j, k in enumerate(chunk):
            rows.append({"name": name, "a3": abc[0], "a5": abc[1], "a7": abc[2],
                         "H_high": f"{H:.9f}", "c3": f"{c3:.9f}",
                         "kappa": k, "n_chaos": int(n[j]),
                         "fracture": int(n[j]) >= CF_MIN,
                         "lam_max": f"{float(lam[j].max()):.8f}"})
        print(f"    [{name}] {min(i+BLOCK, len(ks))}/{len(ks)} cells", flush=True)
    path = os.path.join(outdir, f"ortho_{name}.csv")
    with open(path, "w", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w_.writeheader(); w_.writerows(rows)
    npos = sum(1 for r in rows if r["fracture"])
    print(f"[ortho] {name}: H_high={H:.6f} c3={c3:+.6f} positives={npos}/{len(rows)} -> {path}")

def mask_of(name, outdir):
    p = os.path.join(outdir, f"ortho_{name}.csv")
    if not os.path.exists(p):
        return None
    rows = list(csv.DictReader(open(p)))
    rows.sort(key=lambda r: float(r["kappa"]))
    return np.array([1 if r["fracture"] == "True" else 0 for r in rows], dtype=int)

def summary(outdir):
    Ba = mask_of("anchor", outdir)
    if Ba is None:
        raise SystemExit("summary: anchor run missing")
    out = []
    for arm, names in (("A", ["A1", "A2", "A3", "A4"]),
                       ("B", ["B1", "B2", "B3", "B4"])):
        for nm in names:
            B = mask_of(nm, outdir)
            if B is None:
                print(f"  {nm}: MISSING"); continue
            D = int(np.sum(Ba != B))/len(Ba)
            _, H, c3 = descriptors(ALL[nm])
            out.append({"arm": arm, "name": nm, "H_high": f"{H:.9f}",
                        "c3": f"{c3:.9f}", "n_cells_diff": int(np.sum(Ba != B)),
                        "D_mask": f"{D:.8f}", "positives": int(B.sum())})
    p = os.path.join(outdir, "ortho_mask_summary.csv")
    with open(p, "w", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w_.writeheader(); w_.writerows(out)
    print(f"\nanchor positives = {int(Ba.sum())}/{len(Ba)}")
    print(f"{'arm':>4} {'name':>6} {'H_high':>10} {'c3':>10} {'cells diff':>11} {'D_mask':>10}")
    for r in out:
        print(f"{r['arm']:>4} {r['name']:>6} {float(r['H_high']):10.6f} "
              f"{float(r['c3']):+10.5f} {r['n_cells_diff']:11d} {float(r['D_mask']):10.6f}")
    A_change = any(r["arm"] == "A" and int(r["n_cells_diff"]) > 0 for r in out)
    B_change = any(r["arm"] == "B" and int(r["n_cells_diff"]) > 0 for r in out)
    print(f"\nPRIMARY (locked booleans):  A_change={A_change}   B_change={B_change}")
    if A_change and B_change:
        v = "Both scalars insufficient alone -> waveform geometry is higher-dimensional"
    elif A_change:
        v = "c3 insufficient alone; H_high not falsified in this scope"
    elif B_change:
        v = "H_high insufficient alone; c3 not falsified in this scope"
    else:
        v = "Neither falsified -> both may proxy a deeper common structure"
    print(f"VERDICT [NUM-in-scope]: {v}")
    print(f"  -> {p}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", choices=list(ALL))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--outdir", default="out_ortho")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    if a.summary:
        summary(a.outdir); return
    if a.all:
        for nm in ALL:
            run_one(nm, a.outdir)
        summary(a.outdir); return
    if a.run:
        run_one(a.run, a.outdir); return
    raise SystemExit("give --run <name>, --all, or --summary")

if __name__ == "__main__":
    main()
