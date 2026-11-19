#!/usr/bin/env python3
"""
rtg_mm1_global_check.py -- global half of the RTG/MM-1 comparison (saddle, symmetry, band area, invertibility).
Analytic note: records/coil/COIL_RTG_MM1_GLOBAL_NOTE.md. NOT a campaign, NOT a preregistered run; no orbit is
iterated. Deterministic verification of derived formulas. The script prints only; it writes no file.
Reproduce the committed output with:
    python3 evidence/coil/code/rtg_mm1_global_check.py > evidence/coil/outputs/rtg_mm1_global_check.txt

Maps: RTG T(rho, eta) = (rho - sin eta, eta + (e^rho - 1) - sin eta) (dyad-v6.4.24 DYAD-DEF-PRIMITIVE-MAP);
reduced MM-1 dyad F(phi, w) = (phi + w, (1 - a) w - a kappa g(phi)), g odd, 2 pi-periodic, g'(0) = 1.

Checks:
  S1  saddles. RTG P2 = (0, pi): trace 3, det 1, multipliers phi^{+-2} (phi the golden ratio). MM-1 (pi, 0) with
      c = -g'(pi) > 0: trace 2 - a, det 1 - a(1 + kappa c), p(1) = -a kappa c < 0 (one multiplier > 1); saddle iff
      p(-1) = 4 - 2a - a kappa c > 0; det != 1 for a, kappa, c > 0
  S2  MM-1 mirror: M(phi, w) = (2 pi - phi, -w) satisfies F o M = M o F for odd 2 pi-periodic g; M fixes (pi, 0),
      DM = -I swaps the two branches of the unstable eigendirection; det DF(M x) = det DF(x), so Crit(F^m) is M-invariant
  S3  RTG has no such mirror: T o N - N o T != 0 for N(rho, eta) = (-rho, 2 pi - eta); the discrepancy is the
      even part of e^rho - 1
  B1  band area: (1/2 pi) int det DT d eta = 1 for every rho; (1/2 pi) int det DF d phi = 1 - a for every w
  S4  iterate clocks: at a = kappa = c = 1 the MM-1 saddle is a saddle and DF(pi, 0)^2 has trace 3, det 1 (= DT(P2))
  I1  invertibility bounds of the reduced sine dyad for the locked pairs A, B, C (diffeomorphism iff a kappa < |1 - a|);
      RTG critical curve C0 = {rho >= ln 2, cos eta = -1/(e^rho - 1)}: none on rho < ln 2
  I2  reduced R1 dyad g_q = arcsin(q sin phi)/q, q = 0.99 (normalised g'(0) = 1): |g_q'| <= 1, hence
      det DF >= 1 - a - a kappa = 0.88 > 0 for a = 0.03, kappa <= 3 (locked DYAD range; fracture recorded at kappa = 2.30)
"""
import math, sys
import sympy as sp

def P(*x):
    print(" ".join(str(v) for v in x), flush=True)

ok_all = True
def check(name, cond):
    global ok_all
    ok_all = ok_all and bool(cond)
    P("  %-3s %s" % (name, "ok" if cond else "FAIL"))

P("rtg_mm1_global_check  python %s sympy %s" % (sys.version.split()[0], sp.__version__))
rho, eta, phi, w = sp.symbols('rho eta phi w', real=True)
a, k = sp.symbols('a kappa', positive=True)
T = sp.Matrix([rho - sp.sin(eta), eta + sp.exp(rho) - 1 - sp.sin(eta)])
DT = T.jacobian([rho, eta])

# ---------------------------------------------------------------- S1
P("\nS. Saddles")
DT2 = DT.subs({rho: 0, eta: sp.pi})
ev = sorted(DT2.eigenvals().keys(), key=lambda e: float(e))
gold = (1 + sp.sqrt(5))/2
P("  RTG DT(P2) =", DT2.tolist(), " trace", DT2.trace(), " det", DT2.det(), " multipliers", ev)
okS1 = DT2.trace() == 3 and DT2.det() == 1 and sp.simplify(ev[1] - gold**2) == 0 and sp.simplify(ev[0] - gold**-2) == 0
c = sp.symbols('c', positive=True)   # c = -g'(pi) > 0 (sine and the triangle family: c = 1)
DFpi = sp.Matrix([[1, 1], [a*k*c, 1 - a]])
lam = sp.symbols('lam')
pch = sp.expand((DFpi - lam*sp.eye(2)).det())
P("  MM-1 DF(pi, 0) =", DFpi.tolist(), " (c = -g'(pi) > 0)  trace", DFpi.trace(), " det", sp.expand(DFpi.det()))
P("  characteristic polynomial p(lam) =", pch, "; p(1) =", sp.simplify(pch.subs(lam, 1)), "; p(-1) =", sp.expand(pch.subs(lam, -1)))
okS1 = okS1 and sp.simplify(pch.subs(lam, 1) + a*k*c) == 0 and sp.simplify(pch.subs(lam, -1) - (4 - 2*a - a*k*c)) == 0
okS1 = okS1 and sp.solve(sp.Eq(DFpi.det(), 1), k) == []   # det = 1 impossible for a, kappa > 0
for av, lab in ((0.03, "A"), (0.10, "B"), (0.156, "C")):
    P("  pair %s a = %.3f, sine (c = 1): saddle at (pi, 0) iff kappa < (4 - 2a)/a = %.2f" % (lab, av, (4 - 2*av)/av))
check("S1", okS1)
D1 = DFpi.subs({a: 1, k: 1, c: 1})
D1sq = D1*D1
P("  a = kappa = c = 1: DF(pi, 0) =", D1.tolist(), "; p(-1) =", 4 - 2 - 1, "> 0 (saddle); DF(pi, 0)^2 =", D1sq.tolist(),
  " trace", D1sq.trace(), " det", D1sq.det())
check("S4", D1sq.trace() == 3 and D1sq.det() == 1 and (4 - 2 - 1) > 0)

# ---------------------------------------------------------------- S2
P("\nM. Mirror symmetry of MM-1 and its absence in RTG")
g = sp.Function('g')
F = lambda u, v: sp.Matrix([u + v, (1 - a)*v - a*k*g(u)])
M = lambda u, v: sp.Matrix([2*sp.pi - u, -v])
lhs = F(*M(phi, w)); rhs = M(*F(phi, w))
d = sp.simplify(lhs - rhs)
P("  F(M x) - M(F x) =", d.T.tolist(), " ; vanishes iff g(2 pi - phi) = -g(phi)")
gs = lambda u: sp.sin(u)
dsin = sp.simplify(sp.Matrix([phi + w, (1 - a)*w - a*k*gs(phi)]).subs({phi: 2*sp.pi - phi, w: -w}, simultaneous=True) - M(phi + w, (1 - a)*w - a*k*gs(phi)))
P("  with g = sin:", dsin.T.tolist())
DFs = sp.Matrix([[1, 1], [-a*k*sp.cos(phi), 1 - a]])
okS2 = d[0] == 0 and sp.simplify(d[1] + a*k*(g(phi) + g(2*sp.pi - phi))) == 0
okS2 = okS2 and dsin == sp.zeros(2, 1)
okS2 = okS2 and sp.simplify(DFs.det().subs(phi, 2*sp.pi - phi) - DFs.det()) == 0
P("  M(pi, 0) = (pi, 0); DM = -I maps the unstable eigenvector v to -v (swaps the two branches);",
  "det DF(M x) - det DF(x) =", sp.simplify(DFs.det().subs(phi, 2*sp.pi - phi) - DFs.det()))
check("S2", okS2)

N = lambda r, e: sp.Matrix([-r, 2*sp.pi - e])
dT = sp.simplify(T.subs({rho: -rho, eta: 2*sp.pi - eta}, simultaneous=True) - N(*T))
P("  RTG: T(N x) - N(T x) =", dT.T.tolist(), "for N(rho, eta) = (-rho, 2 pi - eta)")
check("S3", sp.simplify(dT[0]) == 0 and sp.simplify(dT[1] - (sp.exp(-rho) + sp.exp(rho) - 2)) == 0)
P("  (the discrepancy e^rho + e^-rho - 2 = 2 (cosh rho - 1) is the even part of e^rho - 1 and vanishes only on rho = 0)")

# ---------------------------------------------------------------- B1
P("\nB. Band area (signed, degree-weighted image area of a full band)")
bT = sp.simplify(sp.integrate(DT.det(), (eta, 0, 2*sp.pi))/(2*sp.pi))
bF = sp.simplify(sp.integrate(DFs.det(), (phi, 0, 2*sp.pi))/(2*sp.pi))
P("  RTG: det DT =", sp.simplify(DT.det()), "; mean over eta =", bT, "for every rho")
P("  MM-1 (sine): det DF =", sp.expand(DFs.det()), "; mean over phi =", bF, "for every w (and every odd 2 pi-periodic g:",
  "the mean of g' over a period is 0)")
check("B1", bT == 1 and sp.simplify(bF - (1 - a)) == 0)

# ---------------------------------------------------------------- I1
P("\nI. Invertibility where the escape mechanisms act")
okI = True
for av, lab in ((0.03, "A"), (0.10, "B"), (0.156, "C")):
    lim = abs(1 - av)/av
    P("  pair %s a = %.3f: reduced sine dyad a diffeomorphism iff kappa < %.4f" % (lab, av, lim))
Amin = sp.solve(sp.Eq(sp.exp(rho) - 1, 1), rho)[0]
P("  RTG: det DT = 0 needs |e^rho - 1| >= 1 with e^rho - 1 > 0 at cos eta < 0, i.e. rho >= ln 2 =", Amin,
  "; for rho < 0, 0 < det DT < 2 (RECOG, negative half-plane)")
okI = okI and Amin == sp.log(2)
P("  RECOG-THM-P2-C0-FIRST box: 2.03334 < rho_* < 2.03342 > ln 2 = %.5f (consistency only)" % math.log(2))
check("I1", okI)
q = sp.Rational(99, 100)
gq_p = sp.diff(sp.asin(q*sp.sin(phi))/q, phi)
s2 = sp.symbols('s2', nonnegative=True)
ratio2 = (1 - s2)/(1 - q**2*s2)          # (g_q')^2 with s2 = sin^2 phi
okI2 = sp.simplify(sp.diff(ratio2, s2)) .subs(s2, sp.Rational(1, 2)) < 0 and ratio2.subs(s2, 0) == 1
mx = max(abs(float(gq_p.subs(phi, 2*math.pi*i/20000))) for i in range(20000))
bound = 1 - 0.03 - 0.03*3
P("  R1: g_q'(phi) =", sp.simplify(gq_p), "; (g_q')^2 = (1 - s)/(1 - q^2 s), s = sin^2 phi, decreasing in s, = 1 at s = 0; max |g_q'| on a grid = %.12f" % mx)
P("  a = 0.03, kappa <= 3: det DF = 1 - a + a kappa g_q' >= 1 - a - a kappa = %.2f > 0 -> diffeomorphism on the locked DYAD range" % bound)
okI2 = okI2 and mx <= 1 + 1e-12 and bound > 0 and sp.simplify(sp.diff(ratio2, s2)*(1 - q**2*s2)**2 + (1 - q**2)) == 0
check("I2", okI2)

P("\nRESULT: %s (S1-S4, B1, I1-I2)" % ("PASS" if ok_all else "FAIL"))
sys.exit(0 if ok_all else 1)
