#!/usr/bin/env python3
"""
rtg_mm1_comparison_check.py -- local comparison of RTG's primitive dyad map T at P1 with the reduced MM-1 dyad.
Analytic note: records/coil/COIL_RTG_MM1_COMPARISON_NOTE.md. NOT a campaign, NOT a preregistered run; a
deterministic verification of derived formulas. The script prints only; it writes no file.
Reproduce the committed output with:
    python3 evidence/coil/code/rtg_mm1_comparison_check.py > evidence/coil/outputs/rtg_mm1_comparison_check.txt

Maps (sources: rtg-corpus dyad-v6.4.24 DYAD-DEF-PRIMITIVE-MAP and RECOG v0.3.27 section 6.10 K_p family;
COIL MM-1, reduced dyad in the normalisation g'(0) = 1):
  RTG  T(rho, eta)   = (rho - sin eta, eta + (e^rho - 1) - sin eta)                   fixed point P1 = (0, 0)
  K_p  T_p(rho, eta) = (rho - sin eta, eta + K (e^rho - 1) - K sin eta), K = 2 - 2 cos(2 pi/p);  T_6 = T
  MM-1 F(phi, w)     = (phi + w, (1 - a) w - a kappa g(phi)), g odd, g(phi) = phi + g3 phi^3/6 + o(phi^3) (g odd, C^3)

Checks:
  L1  DT(P1) and DF(0) have equal trace and determinant only at (a, kappa) = (1, 1)            [exact]
  L2  at kappa = 1 the MM-1 multiplier is e^{i theta}, cos theta = 1 - a/2 (S2); a = 1 gives theta = pi/3   [exact]
  L3  the K_p linear part has the trace and determinant of the MM-1 block at kappa = 1, a = K                [exact]
  N1  one-step cubic normal-form coefficient c1 of T at P1 (Kuznetsov's formula for maps, frame of the
      eigenvector with eta-component 1): 6 conj(lambda) c1 = 3 mu6^W, mu6^W = -1/2 - i 2 sqrt(3)/3
      (Dyadic frame rule DYAD-ALG-KP-FRAME-SCALE: mu6^Z = 3 mu6^W)                                   [exact]
  N2  K_p family, p = 5, 6, 7, 8, 12, 16, 20, 36: Re of the Z-frame coefficient = -p sin^2(pi/p) and arg = RECOG's values
      (-120.96, -113.41, -108.33 deg at p = 5, 6, 7)                                                [numeric]
  N3  MM-1 at kappa = 1, any a in (0, 4): conj(lambda) c1 = (i g3 / 2) tan(theta/2) e^{-i theta}
      (frame q = (1, lambda - 1)); exact at p = 6 with symbolic g3, numeric at random (theta, g3)   [exact + numeric]
  N4  frame-independent shear/healing ratio Im/Re of the cubic coefficient:
      RTG at P1: 4 sqrt(3)/3 = 2.3094 (Dyadic's exported value); MM-1 at its 1:6 point: cot(pi/3) = 1/sqrt(3)  [exact]
  N5  (supporting) normal-form coefficients of iterates: conj(lambda^n) c1(F^n) = n conj(lambda) c1(F) up to a positive frame factor
      (MM-1 n = 2; RTG T^7), so Im/Re is the same for every admissible iterate                      [numeric]
  N6  cot(theta) = +-4 sqrt(3)/3 has no solution with theta a rational multiple of pi (Niven)            [exact]
  P1  rotation-equivariant cubic monomials z^i zb^j (i + j = 3): only z^2 zb for the angles pi/3 (T) and theta (MM-1),
      theta not in {pi/2, pi}                                                                       [exact]
  P2  parabolic germs T^6, F^6 (a = 1, kappa = 1, sine) and F^3 (a = 3, kappa = 1, sine), composed raw: no quadratic
      part; cubic part in the eigen-coordinate is n conj(lambda) c1 |z|^2 z only (c1 from N1 / N3)  [numeric]
  P3  a real-linear L z = alpha z + beta zb with L(mu |z|^2 z) = nu |Lz|^2 Lz, nu != 0, forces alpha beta = 0:
      the z^3 and zb^3 coefficients are -nu alpha^2 conj(beta) and -nu conj(alpha) beta^2           [exact]
  G1  the reduced sine dyad is a global diffeomorphism iff a kappa < |1 - a| (the map w -> (1 - a) w - a kappa sin(phi' - w)
      must be strictly monotone with nonzero derivative); example a = 3/2, kappa = 1/10: det < 0 everywhere, diffeomorphism
"""
import cmath, math, random, sys
import sympy as sp

def P(*x):
    print(" ".join(str(v) for v in x), flush=True)

ok_all = True
def check(name, cond):
    global ok_all
    ok_all = ok_all and bool(cond)
    P("  %-4s %s" % (name, "ok" if cond else "FAIL"))

P("rtg_mm1_comparison_check  python %s sympy %s" % (sys.version.split()[0], sp.__version__))

# ---------------------------------------------------------------- L1, L2
P("\nL. Linear parts")
a, k = sp.symbols('a kappa', real=True)
DT = sp.Matrix([[1, -1], [1, 0]])
DF = sp.Matrix([[1, 1], [-a*k, 1 - a]])
P("  DT(P1) =", DT.tolist(), " trace", DT.trace(), " det", DT.det(), " eigenvalues", list(DT.eigenvals().keys()))
P("  DF(0)  =", DF.tolist(), " trace", sp.simplify(DF.trace()), " det", sp.expand(DF.det()))
sol = sp.solve([sp.Eq(DF.trace(), DT.trace()), sp.Eq(DF.det(), DT.det())], [a, k], dict=True)
P("  equal trace and determinant:", sol)
check("L1", sol == [{a: 1, k: 1}])
D1 = DF.subs(k, 1)
cos_th = sp.simplify(D1.trace()/2)
disc = sp.factor(sp.expand(D1.trace()**2 - 4*D1.det()))
P("  kappa = 1: det =", sp.simplify(D1.det()), "; trace^2 - 4 det =", disc, "(< 0 for 0 < a < 4, so the multipliers are e^{+-i theta});",
  "cos theta = trace/2 =", cos_th)
check("L2", sp.simplify(D1.det()) == 1 and sp.simplify(cos_th - (1 - a/2)) == 0 and cos_th.subs(a, 1) == sp.Rational(1, 2))
Kp = sp.symbols('K', positive=True)
DTp = sp.Matrix([[1, -1], [Kp, 1 - Kp]])
P("  K_p family: DT_p(P1) =", DTp.tolist(), " trace", DTp.trace(), " det", sp.expand(DTp.det()),
  "= trace and det of DF(0) at kappa = 1, a = K")
check("L3", sp.simplify(DTp.trace() - D1.trace().subs(a, Kp)) == 0 and sp.simplify(DTp.det() - D1.det()) == 0)
P("  rotation per step at the spark (kappa = 1) for the locked pairs: " + ", ".join(
    "a = %.3f: 2 pi / %.2f" % (av, 2*math.pi/math.acos(1 - av/2)) for av in (0.03, 0.10, 0.156)))

# ---------------------------------------------------------------- normal-form machinery
z, zb = sp.symbols('z zb')
def c1_coeff(F, A, lam, exact):
    """one-step cubic normal-form coefficient c1 of a planar map x -> A x + h.o.t. with multipliers lam, conj(lam),
    |lam| = 1, lam^k != 1 for k = 1..4 (Kuznetsov, Elements of Applied Bifurcation Theory, NS normal form).
    Frame: right eigenvector q = (A12, lam - A11), left eigenvector p with p^H q = 1."""
    a11, a12, a21, a22 = A
    conj = sp.conjugate if exact else (lambda u: complex(u).conjugate())
    q = [a12, lam - a11]
    p = [a21, conj(lam) - a11]
    s = conj(p[0])*q[0] + conj(p[1])*q[1]
    p = [p[0]/conj(s), p[1]/conj(s)]
    x0 = q[0]*z + conj(q[0])*zb
    x1 = q[1]*z + conj(q[1])*zb
    Fx = F(x0, x1)
    g = sp.expand(conj(p[0])*Fx[0] + conj(p[1])*Fx[1])
    Pz = sp.Poly(g, z, zb)
    def co(i, j):
        v = Pz.coeff_monomial(z**i * zb**j) * math.factorial(i) * math.factorial(j)
        return sp.nsimplify(sp.simplify(v)) if exact else complex(v)
    g20, g11, g02, g21 = co(2, 0), co(1, 1), co(0, 2), co(2, 1)
    lb = conj(lam)
    c1 = g20*g11*(1 - 2*lam)/(2*(lam**2 - lam)) + g11*conj(g11)/(1 - lb) + g02*conj(g02)/(2*(lam**2 - lb)) + g21/2
    return sp.simplify(c1) if exact else c1

def rtg_map(K):
    # cubic Taylor jet of T_p at P1 (higher orders do not enter c1)
    return lambda r, e: [r - (e - e**3/6), e + K*(r + r**2/2 + r**3/6) - K*(e - e**3/6)]
def mm1_map(av, g3):
    return lambda f, w: [f + w, (1 - av)*w - av*(f + g3*f**3/6)]

# ---------------------------------------------------------------- N1
P("\nN. Cubic normal-form coefficients")
lam6 = sp.Rational(1, 2) + sp.I*sp.sqrt(3)/2
c1T = c1_coeff(rtg_map(1), (1, -1, 1, 0), lam6, exact=True)
v6 = sp.simplify(sp.expand(6*sp.conjugate(lam6)*c1T))
mu6W = -sp.Rational(1, 2) - sp.I*2*sp.sqrt(3)/3
P("  RTG at P1: 6 conj(lambda) c1 =", v6, "; 3 mu6^W =", sp.expand(3*mu6W), "; arg = %.3f deg" % math.degrees(cmath.phase(complex(v6))))
check("N1", sp.simplify(v6 - 3*mu6W) == 0)

# ---------------------------------------------------------------- N2
P("  K_p family (RECOG v0.3.27 section 6.10), frame factor K between this frame and RECOG's Z-frame:")
P("    p     K          Re(Z-frame)    -p sin^2(pi/p)   arg (deg)")
okN2 = True
rec_arg = {5: -120.96, 6: -113.41, 7: -108.33}
rows = []
for p in (5, 6, 7, 8, 12, 16, 20, 36):
    t = 2*math.pi/p; lam = cmath.exp(1j*t); K = 2 - 2*math.cos(t)
    m = p*lam.conjugate()*c1_coeff(rtg_map(K), (1.0, -1.0, K, 1 - K), lam, exact=False)
    mZ = m/K
    target = -p*math.sin(math.pi/p)**2
    arg = math.degrees(cmath.phase(m))
    okN2 = okN2 and abs(mZ.real - target) < 1e-10 and (p not in rec_arg or abs(arg - rec_arg[p]) < 0.005)
    rows.append((p, arg))
    P("    %-4d  %.6f   %+.10f  %+.10f   %9.3f" % (p, K, mZ.real, target, arg))
check("N2", okN2)

# ---------------------------------------------------------------- N3
P("  MM-1 at kappa = 1 (spark point), frame q = (1, lambda - 1):")
g3 = sp.symbols('g3', real=True)
c1M6 = c1_coeff(mm1_map(1, g3), (1, 1, -1, 0), lam6, exact=True)
lhs6 = sp.simplify(sp.expand(sp.conjugate(lam6)*c1M6))
rhs6 = sp.simplify(sp.expand(sp.I*g3/2*sp.tan(sp.pi/6)*sp.exp(-sp.I*sp.pi/3)))
P("    a = 1 (theta = pi/3): conj(lambda) c1 =", sp.simplify(sp.expand_complex(lhs6)), " ; formula:", sp.simplify(sp.expand_complex(rhs6)))
okN3 = sp.simplify(sp.expand_complex(lhs6 - rhs6)) == 0
random.seed(20261118)
worst = 0.0
for _ in range(40):
    t = random.uniform(0.05, 3.0); gv = random.uniform(-3, 3); av = 2 - 2*math.cos(t); lam = cmath.exp(1j*t)
    if any(abs(lam**j - 1) < 1e-3 for j in (1, 2, 3, 4)):
        continue
    num = lam.conjugate()*c1_coeff(mm1_map(av, gv), (1.0, 1.0, -av, 1 - av), lam, exact=False)
    form = 1j*gv/2*math.tan(t/2)*cmath.exp(-1j*t)
    worst = max(worst, abs(num - form))
P("    random (theta, g3), 40 draws: max |numeric - formula| = %.2e" % worst)
check("N3", okN3 and worst < 1e-11)
P("    sine (g3 = -1) along the same rotations as the K_p table:")
P("    p     a          arg MM-1 (deg)   arg RTG K_p (deg)")
for p, argR in rows:
    t = 2*math.pi/p
    vM = 1j*(-1)/2*math.tan(t/2)*cmath.exp(-1j*t)
    P("    %-4d  %.6f   %9.3f        %9.3f" % (p, 2 - 2*math.cos(t), math.degrees(cmath.phase(vM)), argR))

# ---------------------------------------------------------------- N4
P("\n  Shear/healing ratio Im/Re of the cubic coefficient (frame-independent):")
rT = sp.simplify(sp.im(v6)/sp.re(v6))
rM = sp.simplify(sp.im(lhs6)/sp.re(lhs6))
P("    RTG at P1:", rT, "= %.6f   (Dyadic exports 4 sqrt(3)/3)" % float(rT))
P("    MM-1 at a = 1, kappa = 1, any odd g with g3 != 0:", rM, "= %.6f" % float(rM))
check("N4", sp.simplify(rT - 4*sp.sqrt(3)/3) == 0 and sp.simplify(rM - 1/sp.sqrt(3)) == 0)

# ---------------------------------------------------------------- N5, N6
P("\n  Iterates (cubic jets composed and truncated):")
X, Y = sp.symbols('X Y')
def trunc3(e):
    e = sp.expand(e)
    return sum(t for t in sp.Add.make_args(e) if sp.Poly(t, X, Y).total_degree() <= 3)
def iterate(Fmap, n):
    cur = [X, Y]
    for _ in range(n):
        cur = [trunc3(c) for c in Fmap(cur[0], cur[1])]
        cur = [sp.expand(c) for c in cur]
    return lambda u, v: [c.subs({X: u, Y: v}, simultaneous=True) for c in cur]
def lin(Fn):
    e = Fn(X, Y)
    return tuple(float(sp.diff(c, var).subs({X: 0, Y: 0})) for c in e for var in (X, Y))
okN5 = True
t = 0.7; av = 2 - 2*math.cos(t); lam = cmath.exp(1j*t)
F1 = mm1_map(av, -1.0); F2 = iterate(F1, 2)
c_1 = c1_coeff(F1, (1.0, 1.0, -av, 1 - av), lam, exact=False)
c_2 = c1_coeff(F2, lin(F2), lam**2, exact=False)
r = (lam**2).conjugate()*c_2 / (2*lam.conjugate()*c_1)
P("    MM-1 (theta = 0.7, sine): conj(lambda^2) c1(F^2) / (2 conj(lambda) c1(F)) = %.12f%+.12fi" % (r.real, r.imag))
okN5 = okN5 and abs(r.imag) < 1e-10 and r.real > 0
T1 = rtg_map(1.0); T7 = iterate(T1, 7)
c_7 = c1_coeff(T7, lin(T7), complex(lam6), exact=False)
c_T = complex(c1T)
r7 = (complex(lam6)**7).conjugate()*c_7 / (7*complex(lam6).conjugate()*c_T)
P("    RTG T^7 (multiplier e^{i pi/3}): conj(lambda^7) c1(T^7) / (7 conj(lambda) c1(T)) = %.12f%+.12fi" % (r7.real, r7.imag))
okN5 = okN5 and abs(r7.imag) < 1e-10 and r7.real > 0
check("N5", okN5)
P("    (a positive real ratio is the frame factor |s|^2 of a different eigenvector scaling: arguments, hence Im/Re, agree)")
P("  Rotation angle at which the MM-1 ratio cot(theta) would equal +-4 sqrt(3)/3: tan^2(theta) = 3/16, cos(2 theta) = (1 - 3/16)/(1 + 3/16) =",
  sp.Rational(13, 19), "; Niven: cos of a rational multiple of pi is rational only in {0, +-1/2, +-1}")
check("N6", sp.Rational(13, 19) not in (0, sp.Rational(1, 2), -sp.Rational(1, 2), 1, -1) and
      sp.simplify((1 - sp.Rational(3, 16))/(1 + sp.Rational(3, 16)) - sp.Rational(13, 19)) == 0)

# ---------------------------------------------------------------- P1-P3
P("\nP. Parabolic germs (six-step and iterate clocks)")
ok = True
for name, ang in (("T, angle pi/3", sp.pi/3), ("MM-1, a = 1", sp.pi/3), ("MM-1, a = 3 (theta = 2 pi/3)", 2*sp.pi/3), ("MM-1, a = 0.03", sp.acos(1 - sp.Rational(3, 200)))):
    eq = [(i, 3 - i) for i in range(4) if sp.simplify(sp.exp(sp.I*(i - (3 - i) - 1)*ang) - 1) == 0]
    P("  %-30s equivariant cubic monomials z^i zb^j: %s" % (name, eq))
    ok = ok and eq == [(2, 1)]
for name, ang in (("MM-1, a = 2 (theta = pi/2)", sp.pi/2),):
    eq = [(i, 3 - i) for i in range(4) if sp.simplify(sp.exp(sp.I*(i - (3 - i) - 1)*ang) - 1) == 0]
    P("  %-30s equivariant cubic monomials z^i zb^j: %s  (excluded case)" % (name, eq))
    ok = ok and (0, 3) in eq
check("P1", ok)

def jet_in_z(Fn, A, lam):
    a11, a12, a21, a22 = A
    q = [a12, lam - a11]; pv = [a21, lam.conjugate() - a11]
    s_ = pv[0].conjugate()*q[0] + pv[1].conjugate()*q[1]; pv = [pv[0]/s_.conjugate(), pv[1]/s_.conjugate()]
    x0 = q[0]*z + q[0].conjugate()*zb; x1 = q[1]*z + q[1].conjugate()*zb
    e = Fn(x0, x1)
    g = sp.expand(pv[0].conjugate()*e[0] + pv[1].conjugate()*e[1])
    Pz = sp.Poly(g, z, zb)
    return {(i, j): complex(Pz.coeff_monomial(z**i*zb**j)) for i in range(4) for j in range(4) if 1 < i + j <= 3}
okP2 = True
for name, Fmap, A, c1v in (("T^6 (RTG)", rtg_map(1.0), (1.0, -1.0, 1.0, 0.0), complex(c1T)),
                           ("F^6 (MM-1, a = 1, sine)", mm1_map(1.0, -1.0), (1.0, 1.0, -1.0, 0.0), complex(c1M6.subs(g3, -1)))):
    F6 = iterate(Fmap, 6)
    J = jet_in_z(F6, A, complex(lam6))
    expect = 6*complex(lam6).conjugate()*c1v
    others = max(abs(v) for kk, v in J.items() if kk != (2, 1))
    P("  %-26s z^2 zb coefficient %+.12f%+.12fi, expected 6 conj(lambda) c1 = %+.12f%+.12fi; largest other quadratic/cubic coefficient %.1e"
      % (name, J[(2, 1)].real, J[(2, 1)].imag, expect.real, expect.imag, others))
    okP2 = okP2 and abs(J[(2, 1)] - expect) < 1e-10 and others < 1e-10
lam3 = cmath.exp(2j*math.pi/3)
F3 = iterate(mm1_map(3.0, -1.0), 3)
J = jet_in_z(F3, (1.0, 1.0, -3.0, -2.0), lam3)
expect = 3*(1j*(-1.0)/2*math.tan(math.pi/3)*cmath.exp(-2j*math.pi/3))
others = max(abs(v) for kk, v in J.items() if kk != (2, 1))
P("  %-26s z^2 zb coefficient %+.12f%+.12fi, expected 3 x N3 formula = %+.12f%+.12fi; largest other quadratic/cubic coefficient %.1e"
  % ("F^3 (MM-1, a = 3, sine)", J[(2, 1)].real, J[(2, 1)].imag, expect.real, expect.imag, others))
okP2 = okP2 and abs(J[(2, 1)] - expect) < 1e-10 and others < 1e-10
check("P2", okP2)

al, be, alc, bec, mu_, nu_ = sp.symbols('alpha beta alphac betac mu nu')
Lz = al*z + be*zb; Lzb = alc*zb + bec*z
lhs = al*(mu_*z**2*zb) + be*(sp.conjugate(mu_)*zb**2*z)
rhs = nu_*Lz*Lzb*Lz
diff_ = sp.Poly(sp.expand(lhs - rhs), z, zb)
c30, c03 = diff_.coeff_monomial(z**3), diff_.coeff_monomial(zb**3)
P("  L(mu |z|^2 z) - nu |Lz|^2 Lz:  z^3 coefficient", sp.factor(c30), "; zb^3 coefficient", sp.factor(c03))
check("P3", sp.simplify(c30 + nu_*al**2*bec) == 0 and sp.simplify(c03 + nu_*alc*be**2) == 0)

# ---------------------------------------------------------------- G1
P("\nG. Invertibility of the reduced sine dyad F(phi, w) = (phi + w, (1 - a) w - a kappa sin phi)")
P("  F^{-1}: phi = phi' - w, with w solving (1 - a) w - a kappa sin(phi' - w) = w'; the left side has derivative")
P("  (1 - a) + a kappa cos(phi' - w), ranging over [(1 - a) - a kappa, (1 - a) + a kappa]: sign-definite iff a kappa < |1 - a|.")
P("  det DF = 1 - a + a kappa cos(phi): the same interval. F is a global diffeomorphism iff a kappa < |1 - a|.")
okG = True
for av, lab in ((0.03, "A"), (0.10, "B"), (0.156, "C")):
    P("  pair %s a = %.3f: diffeomorphism iff kappa < (1 - a)/a = %.4f" % (lab, av, (1 - av)/av))
av, kv = 1.5, 0.1
dets = [1 - av + av*kv*math.cos(2*math.pi*i/1000) for i in range(1000)]
P("  example a = 3/2, kappa = 1/10: det DF in [%.3f, %.3f] (negative everywhere): orientation-reversing diffeomorphism" % (min(dets), max(dets)))
okG = okG and max(dets) < 0 and av*kv < abs(1 - av)
random.seed(7)
for _ in range(2000):
    av = random.uniform(0.01, 3.0); kv = random.uniform(0.01, 40.0)
    lo, hi = (1 - av) - av*kv, (1 - av) + av*kv
    okG = okG and ((lo > 0 or hi < 0) == (av*kv < abs(1 - av)))
P("  a = 1: det DF = kappa cos(phi); critical lines phi = +-pi/2 for every kappa > 0; not invertible")
check("G1", okG)

P("\nRESULT: %s (L1-L3, N1-N6, P1-P3, G1)" % ("PASS" if ok_all else "FAIL"))
sys.exit(0 if ok_all else 1)
