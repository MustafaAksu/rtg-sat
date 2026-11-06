#!/usr/bin/env python3
"""
rank_certificate.py — PREREG-MM1-RANK v1.0 gate.

R-G1  tangent directions satisfy the amplitude constraint exactly (da+db+2dc = 0)
       and are orthonormal
R-G2  all 12 perturbed points + anchor pass the family guards
       (g'(0)=1, max|g|=A0 at pi/2, no zero in (0,pi))
R-G3  observable is PRE-THRESHOLD: block() returns raw lambda / quarters and applies
       no comparison to the 1e-3 criterion anywhere
R-G4  grid: 751 cells on [0.5, 8], step 0.01
R-G5  kernel equivalence: rank block() reproduces the ORTHO/TONGUESET classification
       when the locked threshold is applied post hoc (anchor, three kappas)

Exit 0 iff all pass.
"""
import sys, math, inspect
import numpy as np
import rank_experiment as R

def main() -> int:
    ok = []
    def chk(n, c):
        ok.append(bool(c)); print(f"[{'PASS' if c else 'FAIL'}] {n}")

    # R-G1
    cu = R.U[0] + R.U[1] + 2*R.U[2]
    cv = R.V[0] + R.V[1] + 2*R.V[2]
    orth = abs(float(R.U @ R.V)) < 1e-15
    norm = abs(np.linalg.norm(R.U)-1) < 1e-12 and abs(np.linalg.norm(R.V)-1) < 1e-12
    chk(f"R-G1 tangent constraint (u:{cu:.1e}, v:{cv:.1e}), orthonormal", 
        abs(cu) < 1e-15 and abs(cv) < 1e-15 and orth and norm)

    # R-G2
    pts = R.points()
    phi = np.linspace(0, np.pi, 400001)
    g2 = True
    print(f"{'point':>12} {'g0':>9} {'max|g|-A0':>12} {'argmax/pi':>10} {'zeros':>6}")
    for nm, abc in pts.items():
        d = float(R.gp(np.array([0.0]), abc)[0])
        v = R.g(phi, abc)
        mx = float(np.abs(v).max()); am = float(phi[int(np.argmax(np.abs(v)))])
        inner = v[(phi > 1e-9) & (phi < np.pi - 1e-9)]
        nz = int(np.sum(inner[:-1]*inner[1:] < 0))
        good = (abs(d-1) < 1e-12 and abs(mx-R.A0) < 1e-9
                and abs(am-np.pi/2) < 1e-4 and nz == 0)
        g2 &= good
        print(f"{nm:>12} {d:9.6f} {mx-R.A0:12.2e} {am/np.pi:10.4f} {nz:6d}")
    chk(f"R-G2 guards for anchor + 12 perturbed points", g2)

    # R-G3 — observable must be pre-threshold.
    # NB: a naive "1e-3 in src" test is wrong — the guard constant 1e-300 contains it.
    # Match the threshold token only when not followed by another digit.
    import re
    src = inspect.getsource(R.block)
    has_thresh_const = bool(re.search(r"1e-3(?!\d)", src))
    has_eps = "EPS" in src
    returns_raw = "return (acc/LYAP)" in src and "chaos" not in src
    chk("R-G3 block() is pre-threshold (no 1e-3 token, no EPS, returns raw lambda)",
        (not has_thresh_const) and (not has_eps) and returns_raw)

    # R-G4
    grid = R.survey_grid()
    chk(f"R-G4 grid = {len(grid)} cells on [{grid[0]}, {grid[-1]}] step {R.D_SURVEY}",
        len(grid) == 751 and abs(grid[0]-0.5) < 1e-12 and abs(grid[-1]-8.0) < 1e-12)

    # R-G5 — post-hoc thresholding reproduces the ORTHO classification at the anchor
    try:
        import ortho_experiment as O
        ks = [2.90, 3.10, 6.63]
        lam, Q = R.block(R.ANCHOR, ks)
        chaos = (lam > 1e-3) & np.all(Q > 1e-3, axis=0)
        mine = chaos.sum(axis=1)
        n_ref, _ = O.block(tuple(R.ANCHOR), ks)
        same = all(int(mine[i]) == int(n_ref[i]) for i in range(len(ks)))
        for i, k in enumerate(ks):
            print(f"    kappa={k}: rank-kernel n={int(mine[i])}  ORTHO n={int(n_ref[i])}")
        chk("R-G5 post-hoc threshold reproduces ORTHO classification", same)
    except ImportError:
        chk("R-G5 ortho_experiment.py NOT FOUND (place it beside this script)", False)

    good = all(ok)
    print("\nCERTIFICATE:", "PASS" if good else "FAIL")
    return 0 if good else 1

if __name__ == "__main__":
    sys.exit(main())
