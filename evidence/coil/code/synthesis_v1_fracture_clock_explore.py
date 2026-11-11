#!/usr/bin/env python3
"""
synthesis_v1_fracture_clock_explore.py -- [EXPLORE] first look at the finite-memory map of
"Relational Time Geometry: Thermodynamic Floors, Geometric Noise, and Spectral Impedance in
Memory-Dependent Stability", v1.0 (doi:10.5281/zenodo.18078442), eqs. (2)-(3), section 3.2.

NOT a preregistered campaign, NOT a reproduction of the paper's code (not available) and NOT a
COIL result. Deterministic, no RNG. Writes ../outputs/synthesis_v1_fracture_clock_explore.json.

Model contract used here (the paper's eqs. 2-3; tau_exit as first exit of the natural update):
  dx_k      = r x_k (1 - x_k) - x_k
  w_j       = ((j+1)^alpha - j^alpha) / Gamma(1 + alpha),            j = 0 .. M-1
  x_{n+1}   = x_0 + sum_{j=0}^{min(n, M-1)} w_j dx_{n-j}
  tau_exit  = first n+1 with x_{n+1} outside [0, 1]   (before it, the paper's projected and the
              unprojected dynamics coincide, so the greedy projection plays no role here)
For comparison only: the web edition "Synthesis v7.3" uses b_j = Gamma(j+alpha)/(Gamma(alpha) j!).

Sections: S1 Figure-1 candidate (alpha 0.98, r 3.05); S2 r scan; S3 high-precision check;
S4 M = 1 control; S5 strong-memory precision sensitivity; S6 weight-family comparison.
"""
import json, math, os, sys
import numpy as np
import mpmath as mp

def w_v1(alpha, M):
    j = np.arange(M, dtype=float); return ((j+1)**alpha - j**alpha)/math.gamma(1+alpha)
def w_v73(alpha, M):
    b = np.empty(M); b[0] = 1.0
    for j in range(1, M): b[j] = b[j-1]*(j-1+alpha)/j
    return b
def tau(alpha, r, x0, M, wf=w_v1, nmax=None, order="fsum"):
    w = wf(alpha, M); nmax = nmax or 8*M+200
    dx = np.zeros(nmax+1); x = x0
    for n in range(nmax):
        dx[n] = r*x*(1-x)-x; m = min(n+1, M); seg = dx[n-m+1:n+1][::-1]
        if order == "fsum": s = math.fsum((w[:m]*seg).tolist())
        elif order == "dot": s = float(np.dot(w[:m], seg))
        else:
            s = 0.0
            for j in range(m): s += w[j]*seg[j]
        x = x0 + s
        if not (0.0 <= x <= 1.0): return n+1
    return None
def tau_mp(alpha, r, x0, M, dps, nmax=None, family="v1"):
    mp.mp.dps = dps; al = mp.mpf(alpha); r_ = mp.mpf(r); x0_ = mp.mpf(x0); nmax = nmax or 8*M+200
    if family == "v1": w = [((j+1)**al - mp.mpf(j)**al)/mp.gamma(1+al) for j in range(M)]
    else:
        w = [mp.mpf(1)]
        for j in range(1, M): w.append(w[-1]*(j-1+al)/j)
    dx = []; x = x0_
    for n in range(nmax):
        dx.append(r_*x*(1-x)-x); m = min(n+1, M)
        x = x0_ + mp.fsum(w[j]*dx[n-j] for j in range(m))
        if not (0 <= x <= 1): return n+1
    return None

OUT = {"label": "[EXPLORE]", "source": "doi:10.5281/zenodo.18078442 v1.0, eqs. (2)-(3)",
       "python": sys.version.split()[0], "numpy": np.__version__, "mpmath": mp.__version__}
X0 = (0.1, 0.4, 0.7)

# S1 -- Figure-1 candidate: alpha = 0.98, r = 3.05 (the figure states neither)
Ms = list(range(10, 250, 5)); s1 = {}
for x0 in X0:
    t = [tau(0.98, 3.05, x0, M) for M in Ms]
    k, c = np.polyfit(Ms, t, 1); res = [ti-(k*M+c) for ti, M in zip(t, Ms)]
    s1[str(x0)] = {"M": Ms, "tau": t, "fit_k": round(float(k), 4), "fit_c": round(float(c), 3),
                   "max_abs_residual": round(float(max(abs(x) for x in res)), 3),
                   "tau_minus_M_range": [min(a-b for a, b in zip(t, Ms)), max(a-b for a, b in zip(t, Ms))]}
OUT["S1_fig1_candidate_alpha0.98_r3.05"] = s1

# S2 -- r scan at alpha = 0.98
Msc = [20, 50, 100, 150, 200, 245]
OUT["S2_r_scan_alpha0.98"] = {"M": Msc, "rows": {str(r): {str(x0): [tau(0.98, r, x0, M) for M in Msc] for x0 in X0}
                              for r in (2.8, 3.05, 3.2, 3.45, 3.57, 3.7, 3.83, 3.9, 3.95, 4.0)}}

# S3 -- high precision (50 digits) against float64 on a subset
s3 = []
for r, x0 in ((3.05, 0.1), (3.05, 0.4), (3.05, 0.7), (2.8, 0.1), (2.8, 0.4)):
    for M in (20, 100, 245):
        a = tau(0.98, r, x0, M); b = tau_mp("0.98", str(r), str(x0), M, 50)
        s3.append({"r": r, "x0": x0, "M": M, "float64": a, "mp50": b, "agree": a == b})
OUT["S3_precision_alpha0.98"] = s3

# S4 -- M = 1: x_{n+1} = x0 + w_0 (f(x_n) - x_n), first-order in x_n for fixed x0
OUT["S4_M1_control"] = {str(r): {str(x0): tau(0.98, r, x0, 1, nmax=20000) for x0 in X0} for r in (2.8, 3.05, 3.57, 3.9)}

# S5 -- strong memory alpha = 0.8: float64 summation-order sensitivity vs 50 digits
s5 = []
for M in (50, 100, 200, 400):
    s5.append({"M": M, **{o: tau(0.8, 3.05, 0.2, M, order=o) for o in ("fsum", "dot", "loop")},
               "mp50": tau_mp("0.8", "3.05", "0.2", M, 50)})
OUT["S5_precision_alpha0.8_r3.05_x0_0.2"] = s5

# S6 -- the two weight families give different clocks at the same (alpha, r, x0)
OUT["S6_weight_families_alpha0.98_r3.05_x0_0.2"] = {
    "M": [100, 400], "v1_power_difference": [tau(0.98, 3.05, 0.2, M) for M in (100, 400)],
    "v7.3_gamma_ratio": [tau(0.98, 3.05, 0.2, M, wf=w_v73) for M in (100, 400)],
    "w0_v1": float(w_v1(0.98, 1)[0]), "w0_v7.3": 1.0}

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "..", "outputs", "synthesis_v1_fracture_clock_explore.json"), "w") as f:
    json.dump(OUT, f, indent=1, sort_keys=True)
for x0 in X0: print("S1", x0, {k: v for k, v in s1[str(x0)].items() if k not in ("M", "tau")})
print("S3 all agree:", all(x["agree"] for x in s3)); print("S4", OUT["S4_M1_control"]); print("S5", s5); print("S6", OUT["S6_weight_families_alpha0.98_r3.05_x0_0.2"])
