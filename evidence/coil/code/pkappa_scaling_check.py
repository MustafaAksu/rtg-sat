#!/usr/bin/env python3
"""
pkappa_scaling_check.py -- check of the small-a (Lienard) reduction of MM-1 on the tri0 cluster orbit.
Analytic note: records/coil/COIL_PKAPPA_SCALING_NOTE.md. NOT a campaign, NOT a preregistered run; a
deterministic verification of derived formulas, in the manner of tri0_reduction_check.py.

Derived statements checked (kappa = K/K*, a = gamma dt; in-cluster map q+ = q + r, r+ = (1-a) r - a kappa sin q;
transverse linearisation d+ = d + s, s+ = (1-a) s - (a kappa/3)(2 + cos q) d):
  C1  limit-cycle amplitude A(kappa):  int_{-A}^{A} (1 - kappa cos x) sqrt(2 kappa (cos x - cos A)) dx = 0
  C2  the amplitude reaches pi (separatrix) at kappa = 3
  C3  transverse exponent per step  lam_perp = a * Lam(kappa),
      Lam(kappa) = (1/2) [ (kappa/3)(2 + <cos q>) - 1 ],  <cos q> the time average over the pendulum orbit
      q'' = -kappa sin q of amplitude A(kappa)
C3 is compared with the LOCKED transverse block exponents of RUN-MM1-ICID v1.0
(evidence/coil/outputs/icid_results/icid_cell*_tri0_*.csv, column lam_perp_block, cluster ICs), which this
script only reads. C1-C2 are compared with direct iteration of the in-cluster map.
Writes ../outputs/pkappa_scaling_check.txt. Requires numpy, scipy.
"""
import csv, glob, math, os, sys
import numpy, scipy
from scipy import integrate, optimize

def bal(A, k):
    return integrate.quad(lambda x: (1 - k*math.cos(x))*math.sqrt(max(0.0, 2*k*(math.cos(x) - math.cos(A)))), -A, A, limit=200)[0]
def A_of(k):
    return optimize.brentq(lambda A: bal(A, k), 1e-3, math.pi - 1e-9)
def Lam(k):
    A = A_of(k); e = 1e-9
    den = lambda u: math.sqrt(2*k*(math.cos(A*math.sin(u)) - math.cos(A)))     # x = A sin u
    T = integrate.quad(lambda u: A*math.cos(u)/den(u), -math.pi/2 + e, math.pi/2 - e, limit=400)[0]
    C = integrate.quad(lambda u: math.cos(A*math.sin(u))*A*math.cos(u)/den(u), -math.pi/2 + e, math.pi/2 - e, limit=400)[0]
    return 0.5*((k/3)*(2 + C/T) - 1), C/T
def amp_map(a, k, N):
    q, r, mx = 1e-3, 0.0, 0.0
    for n in range(N):
        q, r = q + r, (1 - a)*r - a*k*math.sin(q)
        if abs(q) > math.pi: return None
        if n > N//2: mx = max(mx, abs(q))
    return mx
def lam_map(a, k, N):
    q, r, d, s, L, cnt = 1e-3, 0.0, 1.0, 0.0, 0.0, 0
    for n in range(N):
        g = (a*k/3)*(math.cos(q) + 2)
        d, s = d + s, (1 - a)*s - g*d
        q, r = q + r, (1 - a)*r - a*k*math.sin(q)
        if n % 50 == 0:
            nr = math.hypot(d, s)
            if n >= N//2: L += math.log(nr); cnt += 50
            d /= nr; s /= nr
    return L/cnt

here = os.path.dirname(os.path.abspath(__file__)); out = []
P = lambda *x: out.append(" ".join(str(v) for v in x))
P("pkappa_scaling_check  python", sys.version.split()[0], "numpy", numpy.__version__, "scipy", scipy.__version__)
P("\nC1  amplitude: predicted A(kappa) | map, a = 0.1, 0.03, 0.01, 0.003 (N = 400/a)")
worst1 = 0.0
for k in (1.2, 1.5, 2.0, 2.5, 2.9):
    A = A_of(k); row = [amp_map(a, k, int(400/a)) for a in (0.1, 0.03, 0.01, 0.003)]
    worst1 = max(worst1, max(abs(v - A)/A for v in row))
    P("  kappa %.2f  A_pred %.6f | %s" % (k, A, "  ".join("%.6f" % v for v in row)))
P("  largest relative deviation: %.2e" % worst1)
P("\nC2  balance integral at the separatrix, A = pi: zero at kappa = 3 (closed form 8 sqrt(kappa) (1 - kappa/3))")
for k in (2.9, 3.0, 3.1):
    P("  kappa %.1f  integral %.6f  closed form %.6f" % (k, bal(math.pi - 1e-9, k), 8*math.sqrt(k)*(1 - k/3)))
P("  first kappa on a 0.01 grid at which the map orbit from q = 1e-3 leaves |q| <= pi (N = 600/a):")
for a in (0.156, 0.1, 0.03, 0.01, 0.003):
    k = 2.90
    while amp_map(a, k, int(600/a)) is not None and k < 3.6: k = round(k + 0.01, 2)
    P("  a %.3f  kappa %.2f" % (a, k))
P("\nC3a transverse exponent, map against formula: kappa | Lam(kappa) | lam_perp/a at a = 0.156, 0.1, 0.03, 0.01 (N = 3000/a)")
for k in (1.2, 1.5, 2.0, 2.5, 2.8):
    L, mc = Lam(k)
    P("  kappa %.2f  <cos q> %+.4f  Lam %.4f | %s" % (k, mc, L, "  ".join("%.4f" % (lam_map(a, k, int(3000/a))/a) for a in (0.156, 0.1, 0.03, 0.01))))
P("\nC3b transverse exponent, LOCKED ICID data against formula (cluster ICs; lam_perp_block per step)")
PAIR = {'A': 0.03, 'B': 0.100, 'C': 0.156}; worst3 = 0.0; n3 = 0
for f in sorted(glob.glob(os.path.join(here, "..", "outputs", "icid_results", "icid_cell*_tri0_*.csv"))):
    R = [r for r in csv.DictReader(open(f)) if r['cluster'] == '1' and r['lam_perp_block'] not in ('', 'nan')]
    if not R: continue
    v = [float(r['lam_perp_block']) for r in R]; pair = R[0]['pair']; k = float(R[0]['kappa']); a = PAIR[pair]
    p = a*Lam(k)[0]; dev = max(abs(x - p)/p for x in v); worst3 = max(worst3, dev); n3 += len(v)
    P("  cell %2s  %s  kappa %.3f  n=%d  measured %.6e .. %.6e | a*Lam %.6e | max rel dev %.2e" % (R[0]['cell'], pair, k, len(v), min(v), max(v), p, dev))
P("  values compared: %d; largest relative deviation: %.2e" % (n3, worst3))
ok = worst1 < 5e-3 and worst3 < 3e-2 and n3 == 60
P("\nRESULT:", "PASS" if ok else "FAIL", "(C1 within 0.5%, C3b within 3% on 60 locked values)")
open(os.path.join(here, "..", "outputs", "pkappa_scaling_check.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out)); sys.exit(0 if ok else 1)
