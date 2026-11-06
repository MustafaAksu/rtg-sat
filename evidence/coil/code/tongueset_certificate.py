#!/usr/bin/env python3
"""
tongueset_certificate.py — PREREG-MM1-WAVEFORM-TONGUESET v1.0 gate.

G1  iso-A family guards hold for all six locked t   (g'(0)=1, max|g|=A0 at pi/2, no zero in (0,pi))
G2  block-vectorized computation is BIT-IDENTICAL to the per-cell computation
    (same n_chaos and same lambda vector, exact equality)
G3  locked grids are consistent: survey [0.5,8] step 0.01 -> 751 cells; refine step 0.0025

Exit 0 iff all pass. Must pass before any run.
"""
import sys, math
import numpy as np
import tongueset_experiment as E

def main() -> int:
    ok = []
    def chk(n, c):
        ok.append(bool(c)); print(f"[{'PASS' if c else 'FAIL'}] {n}")

    # G1 — family guards
    phi = np.linspace(0, np.pi, 400001)
    g1 = True
    for t in E.T_LOCKED:
        d = float(E.gp(np.array([0.0]), t)[0])
        v = E.g(phi, t)
        amax = float(np.abs(v).max())
        argm = float(phi[int(np.argmax(np.abs(v)))])
        inner = v[(phi > 1e-9) & (phi < np.pi - 1e-9)]
        nz = int(np.sum(inner[:-1]*inner[1:] < 0))
        g1 &= (abs(d - 1.0) < 1e-9) and (abs(amax - E.A0) < 1e-9) \
              and (abs(argm - np.pi/2) < 1e-4) and (nz == 0)
    chk(f"G1 iso-A guards for all six t (A0={E.A0:.10f})", g1)

    # G2 — exact equivalence of blocked vs per-cell
    t_test = -0.300
    ks = [3.05, 3.10, 3.15]
    nb, lamb = E.block(t_test, ks)
    g2 = True
    for i, k in enumerate(ks):
        nc, lamc = E.block(t_test, [k])           # width-1 block == per-cell path
        g2 &= (int(nb[i]) == int(nc[0])) and np.array_equal(lamb[i], lamc[0])
        print(f"    kappa={k}: blocked n={int(nb[i])}  single n={int(nc[0])}  "
              f"max|dlam|={np.max(np.abs(lamb[i]-lamc[0])):.3e}")
    chk("G2 blocked == per-cell, bit-identical", g2)

    # G2b — equivalence against the parent ISOA implementation (independent kernel)
    try:
        import isoa_experiment as P
        g2b = True
        for k in ks:
            n_ref, lmax_ref, lmed_ref = P.cell(t_test, k)
            nb1, lam1 = E.block(t_test, [k])
            same_n = int(nb1[0]) == int(n_ref)
            same_max = float(lam1[0].max()) == float(lmax_ref)
            same_med = float(np.median(lam1[0])) == float(lmed_ref)
            g2b &= same_n and same_max and same_med
            print(f"    kappa={k}: n {int(nb1[0])}=={n_ref}  "
                  f"lam_max {'==' if same_max else '!='}  median {'==' if same_med else '!='}")
        chk("G2b legacy ISOA reference-equivalence (exact)", g2b)
    except ImportError:
        chk("G2b legacy ISOA reference-equivalence — isoa_experiment.py NOT FOUND "
            "(place it beside this script to certify)", False)

    # G3 — grid arithmetic
    survey = E.survey_grid()
    g3 = (len(survey) == 751 and abs(survey[0] - 0.5) < 1e-12
          and abs(survey[-1] - 8.0) < 1e-12
          and abs(E.D_FINE - 0.0025) < 1e-15)
    chk(f"G3 survey grid = {len(survey)} cells on [0.5,8], refine step {E.D_FINE}", g3)

    good = all(ok)
    print("\nCERTIFICATE:", "PASS" if good else "FAIL")
    return 0 if good else 1

if __name__ == "__main__":
    sys.exit(main())
