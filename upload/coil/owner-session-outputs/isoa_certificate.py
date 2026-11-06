#!/usr/bin/env python3
"""
isoa_certificate.py — PREREG-MM1-WAVEFORM-ISOA v1.0 analytic certificate.

C1  h3'(0) = h5'(0) = 0                      (derivative-null bases)
C2  g_t'(0) = 1 for every locked t           (S1/S2 frozen, zero tolerance)
C3  g_t(pi/2) = A0 for every locked t        (iso-amplitude by construction)
C4  max|g_t| = A0 attained at pi/2           (iso-amplitude actually holds)
C5  g_t has no zero in (0, pi)               (well-structure confound absent)
C6  locked t set lies inside validity window [-0.749824, +0.023143]
C7  descriptor table reproduces the prereg values

Exit 0 iff all pass. Run BEFORE the experiment.
"""
import sys, math
import numpy as np

A0 = math.asin(0.9125)/0.9125
C  = (1.0 - A0)/4.0
T_LOCKED = [-0.300, -0.220, -0.140, -0.060, 0.000, 0.008]
T_WIN = (-0.749824, 0.023143)
TOL = 1e-9

def g(phi, t):
    a, b = C/2 + t, C/2 - t
    return np.sin(phi) + a*(np.sin(3*phi) - 3*np.sin(phi)) + b*(np.sin(5*phi) - 5*np.sin(phi))

def gp(phi, t):
    a, b = C/2 + t, C/2 - t
    return np.cos(phi) + a*(3*np.cos(3*phi) - 3*np.cos(phi)) + b*(5*np.cos(5*phi) - 5*np.cos(phi))

def coeffs(t):
    a, b = C/2 + t, C/2 - t
    return 1 - 3*a - 5*b, a, b            # a1, a3, a5

def main() -> int:
    ok = []
    def chk(name, cond):
        ok.append(bool(cond)); print(f"[{'PASS' if cond else 'FAIL'}] {name}")

    h3p = 3*math.cos(0) - 3*math.cos(0)
    h5p = 5*math.cos(0) - 5*math.cos(0)
    chk("C1 h3'(0)=h5'(0)=0", abs(h3p) < TOL and abs(h5p) < TOL)

    phi = np.linspace(0, np.pi, 400001)
    c2 = c3 = c4 = c5 = c6 = True
    for t in T_LOCKED:
        c2 &= abs(float(gp(np.array([0.0]), t)[0]) - 1.0) < TOL
        c3 &= abs(float(g(np.array([np.pi/2]), t)[0]) - A0) < TOL
        v = np.abs(g(phi, t))
        c4 &= (v.max() - A0 < TOL) and abs(phi[int(np.argmax(v))] - np.pi/2) < 1e-4
        inner = g(phi, t)[(phi > 1e-9) & (phi < np.pi - 1e-9)]
        c5 &= int(np.sum(inner[:-1]*inner[1:] < 0)) == 0
        c6 &= (T_WIN[0] <= t <= T_WIN[1])
    chk("C2 g_t'(0) = 1 for all locked t", c2)
    chk(f"C3 g_t(pi/2) = A0 = {A0:.10f}", c3)
    chk("C4 max|g_t| = A0 at pi/2 (iso-amplitude holds)", c4)
    chk("C5 no zero of g_t in (0,pi) (no extra fixed points)", c5)
    chk(f"C6 locked t set inside validity window {T_WIN}", c6)

    print(f"\n{'t':>8} {'a1':>9} {'a3':>9} {'a5':>9} {'c3':>8} {'H3':>8} {'H5':>8} {'H_high':>9}")
    c7 = True
    expect_c3 = {-0.300: -4.188, -0.220: -2.908, -0.140: -1.628,
                 -0.060: -0.348, 0.000: 0.612, 0.008: 0.740}
    h = 1e-4
    for t in T_LOCKED:
        a1, a3, a5 = coeffs(t)
        d3 = (g(np.array([2*h]), t)[0] - 2*g(np.array([h]), t)[0]
              + 2*g(np.array([-h]), t)[0] - g(np.array([-2*h]), t)[0])/(2*h**3)
        cc = d3/6
        H3, H5 = abs(a3/a1), abs(a5/a1)
        Hh = (a3**2 + a5**2)/(a1**2 + a3**2 + a5**2)
        c7 &= abs(cc - expect_c3[t]) < 5e-3
        print(f"{t:8.3f} {a1:9.5f} {a3:9.5f} {a5:9.5f} {cc:8.3f} {H3:8.4f} {H5:8.4f} {Hh:9.5f}")
    chk("C7 descriptor table matches prereg", c7)

    good = all(ok)
    print("\nCERTIFICATE:", "PASS" if good else "FAIL")
    return 0 if good else 1

if __name__ == "__main__":
    sys.exit(main())
