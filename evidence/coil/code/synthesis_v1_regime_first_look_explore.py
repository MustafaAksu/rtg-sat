#!/usr/bin/env python3
"""
synthesis_v1_regime_first_look_explore.py -- [EXPLORE] regime first look at the finite-memory map of
"Relational Time Geometry: Thermodynamic Floors, Geometric Noise, and Spectral Impedance in
Memory-Dependent Stability", v1.0 (doi:10.5281/zenodo.18078442), eqs. (2)-(3).

NOT a preregistered campaign, NOT a reproduction of the paper's code (not available), NOT a COIL
result. Deterministic, no RNG. Writes ../outputs/synthesis_v1_regime_first_look_explore.json.
Model contract: records/coil/COIL_SYNTHESIS_V1_SOURCE_PACKAGE.md section 2 (unprojected natural update;
exit = first n+1 with x outside [0, 1]).

For every cell (alpha, M, x0, r):
  exit      first exit step, or null if none in N steps
  amp, mean max-min and mean of x over the last TAIL steps (only if no exit)
  xbar      the larger root of  x = x0 + S (f_r(x) - x),  S = sum_j w_j = M^alpha / Gamma(1+alpha)
            (stationary state of the windowed rule for n >= M)
  c         f_r'(xbar) - 1
  rho, ang  modulus and argument of the largest root of  lambda^M - c sum_j w_j lambda^(M-1-j)
            (linearisation of the windowed rule at xbar)
and for every (alpha, M, x0) the crossing r_s: rho(r_s) = 1, by bisection on [1.2, 3.2].
Float64, numpy.dot summation; a 30-digit recomputation of the exit step on a subset is in "mp_check".
"""
import json, math, os, sys
import numpy as np
import mpmath as mp

N, TAIL = 20000, 4000
ALPHAS, MS, X0S = (0.98, 0.90, 0.80), (10, 30, 100), (0.1, 0.4, 0.7)
RS = [round(1.2 + 0.05*i, 2) for i in range(41)]

def W(al, M):
    j = np.arange(M, dtype=float); return ((j+1)**al - j**al)/math.gamma(1+al)
def run(al, r, x0, M):
    w = W(al, M); dx = np.zeros(N+1); x = x0; xs = np.empty(N)
    for n in range(N):
        dx[n] = r*x*(1-x) - x; m = min(n+1, M)
        x = x0 + float(np.dot(w[:m], dx[n-m+1:n+1][::-1])); xs[n] = x
        if not (0.0 <= x <= 1.0): return n+1, None, None
    t = xs[-TAIL:]; return None, float(t.max()-t.min()), float(t.mean())
def lin(al, r, x0, M):
    S = M**al/math.gamma(1+al); a = S*r; b = 1 - S*(r-1)
    xb = (-b + math.sqrt(b*b + 4*a*x0))/(2*a); c = r*(1-2*xb) - 1
    lam = np.roots(np.concatenate(([1.0], -c*W(al, M)))); k = int(np.argmax(abs(lam)))
    return xb, c, float(abs(lam[k])), float(abs(np.angle(lam[k])))
def crossing(al, x0, M):
    lo, hi = 1.2, 3.2
    if not (lin(al, lo, x0, M)[2] < 1 < lin(al, hi, x0, M)[2]): return None
    for _ in range(40):
        mid = 0.5*(lo+hi)
        if lin(al, mid, x0, M)[2] < 1: lo = mid
        else: hi = mid
    r = 0.5*(lo+hi); xb, c, rho, ang = lin(al, r, x0, M)
    return {"r_s": round(r, 6), "xbar": round(xb, 6), "c": round(c, 6), "angle": round(ang, 6)}
def exit_mp(al, r, x0, M, nmax):
    mp.mp.dps = 30; al_ = mp.mpf(al); r_ = mp.mpf(r); x0_ = mp.mpf(x0)
    w = [((j+1)**al_ - mp.mpf(j)**al_)/mp.gamma(1+al_) for j in range(M)]; dx = []; x = x0_
    for n in range(nmax):
        dx.append(r_*x*(1-x) - x); m = min(n+1, M)
        x = x0_ + mp.fsum(w[j]*dx[n-j] for j in range(m))
        if not (0 <= x <= 1): return n+1
    return None

OUT = {"label": "[EXPLORE]", "source": "doi:10.5281/zenodo.18078442 v1.0, eqs. (2)-(3)", "N": N, "TAIL": TAIL,
       "python": sys.version.split()[0], "numpy": np.__version__, "mpmath": mp.__version__, "cells": [], "crossings": []}
for al in ALPHAS:
    for M in MS:
        for x0 in X0S:
            OUT["crossings"].append({"alpha": al, "M": M, "x0": x0, **(crossing(al, x0, M) or {"r_s": None})})
            for r in RS:
                e, amp, mean = run(al, r, x0, M); xb, c, rho, ang = lin(al, r, x0, M)
                OUT["cells"].append({"alpha": al, "M": M, "x0": x0, "r": r, "exit": e, "amp": amp, "mean": mean,
                                     "xbar": round(xb, 9), "c": round(c, 9), "rho": round(rho, 9), "ang": round(ang, 9)})
chk = []
for al, r, x0, M in (("0.8", "2.5", "0.4", 10), ("0.8", "2.6", "0.1", 10), ("0.8", "2.7", "0.1", 10),
                     ("0.98", "2.2", "0.1", 10), ("0.98", "2.1", "0.4", 10), ("0.98", "1.6", "0.7", 10)):
    f = next(x["exit"] for x in OUT["cells"] if (x["alpha"], x["r"], x["x0"], x["M"]) == (float(al), float(r), float(x0), M))
    chk.append({"alpha": al, "r": r, "x0": x0, "M": M, "float64": f, "mp30_within_3000": exit_mp(al, r, x0, M, 3000)})
OUT["mp_check"] = chk
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "..", "outputs", "synthesis_v1_regime_first_look_explore.json"), "w") as fo:
    json.dump(OUT, fo, indent=1, sort_keys=True)

def cls(x):
    if x["exit"] is not None: return "X"
    return "s" if x["amp"] < 1e-6 else "o"
for al in ALPHAS:
    for M in MS:
        for x0 in X0S:
            row = [x for x in OUT["cells"] if (x["alpha"], x["M"], x["x0"]) == (al, M, x0)]
            cr = next(x for x in OUT["crossings"] if (x["alpha"], x["M"], x["x0"]) == (al, M, x0))
            print(f"a={al} M={M:3d} x0={x0}  r_s={cr['r_s']}  ang={cr.get('angle')}  " + "".join(cls(x) for x in row))
print("mp_check", chk)
