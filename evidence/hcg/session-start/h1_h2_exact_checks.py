#!/usr/bin/env python3
"""
H1/H2 exact checks — Hodge & Complex Geometry standalone session.
Primary derivation: Claude. Independent verifier: ChatGPT (blind; must not reuse this script).

Self-contained: no RTG files are read. RTG inputs are hard-coded below with provenance
(see charter v0.2 §1). All arithmetic is exact (SymPy symbolics, python-flint integer
matrices, Python Fractions, and an exact Q(zeta3) field class). The only floating-point
step is an optional numerical cross-check of j(E)=0 (H1-09), which is labelled as such.

Usage (Windows/PowerShell, env "RTG"):
    pip install sympy mpmath python-flint
    python h1_h2_exact_checks.py            # prints PASS/FAIL lines, writes h1_h2_results.json
Exit code 0 iff every check passes.
"""
import json, sys, hashlib, itertools
from fractions import Fraction
import sympy as sp
import flint

RESULTS = []
def check(cid, desc, ok, detail=""):
    RESULTS.append({"id": cid, "desc": desc, "pass": bool(ok), "detail": str(detail)})
    print(f"[{'PASS' if ok else 'FAIL'}] {cid}: {desc}" + (f"  -> {detail}" if detail else ""))

# ---------------------------------------------------------------- RTG imports (R1-R4)
A  = sp.Matrix([[1, -1], [1, 0]])                                  # R1
B  = sp.Matrix([[1, sp.Rational(-1, 2)], [sp.Rational(-1, 2), 1]])  # R2
I2 = sp.eye(2)
s3 = sp.sqrt(3)
J  = (2*A - I2) / s3                                               # R3
MU_OWNER  = sp.Rational(-1, 2) - 2*sp.I*s3/3                       # R4 (six-step cubic)
A05_OWNER = sp.Rational(-49, 8640) - sp.I*307*s3/25920             # R4 (six-step z̄^5)

# ================================================================ H1
print("\n=== H1: Eisenstein elliptic realization ===")
check("H1-01", "A^2 - A + I = 0", (A*A - A + I2) == sp.zeros(2))
check("H1-02", "A^3 = -I and A^6 = I", A**3 == -I2 and A**6 == I2)
check("H1-03", "A^T B A = B", sp.simplify(A.T*B*A - B) == sp.zeros(2))
check("H1-04", "J_Q^2 = -I and J_Q^T B J_Q = B",
      sp.simplify(J*J + I2) == sp.zeros(2) and sp.simplify(J.T*B*J - B) == sp.zeros(2))
check("H1-05", "A = I/2 + (sqrt3/2) J_Q, and J_Q commutes with A",
      sp.simplify(A - (I2/2 + s3/2*J)) == sp.zeros(2) and sp.simplify(A*J - J*A) == sp.zeros(2))

z3 = sp.Rational(-1, 2) + sp.I*s3/2      # zeta_3
z6 = sp.Rational(1, 2) + sp.I*s3/2       # zeta_6
x, y = sp.symbols("x y", real=True)
v = sp.Matrix([x, y])
phi = lambda w: sp.expand(w[0] + z3*w[1])
check("H1-06", "In z = x + zeta3*y: A acts as *zeta6 and J_Q as *i",
      sp.simplify(phi(A*v) - z6*phi(v)) == 0 and sp.simplify(phi(J*v) - sp.I*phi(v)) == 0)

# Lattice Z^2 <-> Lambda = Z + Z*zeta3; A in GL2(Z) preserves it.
check("H1-07", "A integral with det 1 (A in SL2(Z)), so Lambda = Z[zeta6] is A-stable",
      all(e.is_integer for e in A) and A.det() == 1)

# End: integral centralizer of A in M2(Z) equals Z[A] = Z*I + Z*A  (≅ Z[zeta6])
a_, b_, c_, d_ = sp.symbols("a b c d", integer=True)
X = sp.Matrix([[a_, b_], [c_, d_]])
sol = sp.solve(list(X*A - A*X), [a_, b_, c_, d_], dict=True)[0]
Xs = X.subs(sol)
p_, q_ = sp.symbols("p q")
# express Xs = p I + q A  with p,q integer combos of the free params
pq = sp.solve(list(Xs - (p_*I2 + q_*A)), [p_, q_], dict=True)
ok_end = len(pq) == 1 and all(sp.Poly(val, *[s for s in (a_, b_, c_, d_) if s in val.free_symbols]).is_linear
                              if val.free_symbols else val.is_integer for val in pq[0].values())
check("H1-08", "Integral centralizer of A in M2(Z) is Z[A] (CM by Z[zeta6], rank 2)",
      ok_end, f"general commuting X = {Xs.tolist()} = {pq[0]}")

# j-invariant: symbolic argument + numerical cross-check (float, labelled)
try:
    import mpmath
    mpmath.mp.dps = 50
    Jk = mpmath.kleinj(mpmath.mpc(-0.5, mpmath.sqrt(3)/2))   # Klein J = j/1728
    check("H1-09", "j(E) = 0 [numerical cross-check; exact reason: zeta6*Lambda = Lambda forces g2 = 0]",
          abs(Jk) < mpmath.mpf(10)**-40, f"|kleinJ(zeta3)| = {mpmath.nstr(abs(Jk), 5)}")
except Exception as e:
    check("H1-09", "j(E)=0 numerical cross-check", False, repr(e))

# Polarization: omega_B(u,w) = B(J u, w) = u^T (J^T B) w ;  omega_0 = (2/sqrt3) omega_B
WB = sp.simplify(J.T*B)
W0 = sp.simplify(2/s3*WB)
check("H1-10", "omega_B = (sqrt3/2) dx^dy and omega_0 = dx^dy (integral on Z^2, value 1 on (e1,e2))",
      sp.simplify(WB - s3/2*sp.Matrix([[0, 1], [-1, 0]])) == sp.zeros(2)
      and W0 == sp.Matrix([[0, 1], [-1, 0]]))
Hsym = sp.simplify(W0*J)   # omega_0(u, J w) = u^T W0 J w
check("H1-11", "Riemann conditions: omega_0(Ju,Jw)=omega_0(u,w); omega_0(u,Jw) symmetric positive definite",
      sp.simplify(J.T*W0*J - W0) == sp.zeros(2) and Hsym == Hsym.T
      and all(ev > 0 for ev in Hsym.eigenvals()),
      f"omega_0(u,Jw) matrix = {Hsym.tolist()} = (2/sqrt3) B")

# ================================================================ exterior algebra (exact, integer)
def perm_sign(seq):
    s = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s

def wedge(a, b):
    out = {}
    for I, ca in a.items():
        for K, cb in b.items():
            if set(I) & set(K):
                continue
            seq = I + K
            key = tuple(sorted(seq))
            out[key] = out.get(key, 0) + perm_sign(seq)*ca*cb
    return {k: c for k, c in out.items() if c != 0}

def one_form(coeffs):                  # coeffs: list over coordinate indices
    return {(k,): c for k, c in enumerate(coeffs) if c != 0}

def pullback(alpha, L):
    """L: target_dim x source_dim integer matrix (target = L*source). Pull back form alpha."""
    out = {}
    for I, c in alpha.items():
        term = {(): 1}
        for i in I:
            term = wedge(term, one_form([L[i][k] for k in range(len(L[0]))]))
        for k2, c2 in term.items():
            out[k2] = out.get(k2, 0) + c*c2
    return {k: c for k, c in out.items() if c != 0}

def derivation(alpha, M):
    """Derivation of Λ induced by dx_i -> sum_k M[i][k] dx_k (pullback by the linear map M)."""
    out = {}
    n = len(M)
    for I, c in alpha.items():
        for pos, i in enumerate(I):
            for k in range(n):
                m = M[i][k]
                if m == 0:
                    continue
                new = list(I); new[pos] = k
                if len(set(new)) < len(new):
                    continue
                key = tuple(sorted(new))
                out[key] = out.get(key, 0) + perm_sign(new)*c*m
    return {k: c for k, c in out.items() if c != 0}

def basis(n, d):
    return list(itertools.combinations(range(n), d))

def vec(alpha, bas):
    return [alpha.get(b, 0) for b in bas]

def block_diag(blocks):
    n = sum(len(b) for b in blocks)
    M = [[0]*n for _ in range(n)]
    o = 0
    for b in blocks:
        for i in range(len(b)):
            for k in range(len(b)):
                M[o+i][o+k] = b[i][k]
        o += len(b)
    return M

# Hodge (k,k) condition on a torus with complex structure J (per factor J_Q):
# a real m-form is of pure type (k,k) iff it is killed by the derivation D_J.
# D_J = D_U / sqrt3 with U = 2A - I integral, so ker D_J = ker D_U (exact integer test).
U2 = [[1, -2], [2, -1]]                # 2A - I
A2 = [[1, -1], [1, 0]]

def DU_matrix(nfac, m):
    n = 2*nfac
    U = block_diag([U2]*nfac)
    bas = basis(n, m)
    cols = [vec(derivation({b: 1}, U), bas) for b in bas]
    return flint.fmpz_mat([list(r) for r in zip(*cols)]), bas   # rows = output coords

def snf_diag(rows):
    M = flint.fmpz_mat(rows)
    S = M.snf()
    r = min(S.nrows(), S.ncols())
    return [int(S[i, i]) for i in range(r)]

# ================================================================ H2a: E x E
print("\n=== H2a: integral Neron-Severi basis of E x E ===")
n2 = 4
vol4 = (0, 1, 2, 3)

def pair(a, b, top):
    return wedge(a, b).get(top, 0)

def poincare_dual_of_curve(L, n=4):
    """Curve parametrized by E -> E^2 via integral linear L (4x2). Return class eta in Λ^2 Z^4
    with  ∫_X eta ∧ alpha = ∫_curve alpha  for all alpha in Λ^2."""
    bas = basis(n, 2)
    rhs = [pullback({b: 1}, L).get((0, 1), 0) for b in bas]        # ∫_curve dx_b
    P = sp.Matrix([[pair({bi: 1}, {bj: 1}, vol4) for bj in bas] for bi in bas])  # P[i][j]=<e_i,e_j>
    sol = P.T.solve(sp.Matrix(rhs))                                 # sum_i eta_i P[i][j] = rhs_j
    assert all(s.is_integer for s in sol)
    return {bas[i]: int(sol[i]) for i in range(len(bas)) if sol[i] != 0}

L_D1 = [[0, 0], [0, 0], [1, 0], [0, 1]]           # {O} x E
L_D2 = [[1, 0], [0, 1], [0, 0], [0, 0]]           # E x {O}
L_D3 = [[1, 0], [0, 1], [1, 0], [0, 1]]           # diagonal
L_D4 = [[1, 0], [0, 1], [1, -1], [1, 0]]          # graph of a (matrix A)
D = [poincare_dual_of_curve(L) for L in (L_D1, L_D2, L_D3, L_D4)]
names = ["D1={O}xE", "D2=Ex{O}", "D3=Delta", "D4=Gamma_A"]
for nm, d in zip(names, D):
    print(f"   class[{nm}] = {d}")

Mint = [[pair(D[i], D[j], vol4) for j in range(4)] for i in range(4)]
check("H2-01", "Intersection matrix of D1..D4 equals [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]",
      Mint == [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], Mint)
check("H2-02", "det M = -3", sp.Matrix(Mint).det() == -3, sp.Matrix(Mint).det())

DU2, bas2 = DU_matrix(2, 2)
check("H2-03", "dim_Q (H^{1,1} ∩ H^2(Q)) on E^2 = rank ker D_U on Λ^2 Q^4 = 4",
      6 - DU2.rank() == 4, f"rank D_U = {DU2.rank()}")
check("H2-04", "Each [D_i] is of type (1,1) (killed by D_U)",
      all(derivation(d, block_diag([U2, U2])) == {} for d in D))
Dmat = [vec(d, bas2) for d in D]
inv = snf_diag(Dmat)
check("H2-05", "Z-span of [D1..D4] is saturated in Λ^2 Z^4 (all SNF invariants = 1)",
      inv == [1, 1, 1, 1], f"SNF invariants {inv}")
print("   => H2-03+H2-04+H2-05: span_Z[D_i] = (H^{1,1} ∩ H^2(Z)) = NS(E^2) by Lefschetz (1,1):"
      " a direct proof of index 1, not using the classical discriminant value.")
C3 = {k: D[2].get(k, 0) - D[0].get(k, 0) - D[1].get(k, 0) for k in set(D[0]) | set(D[1]) | set(D[2])}
C4 = {k: D[3].get(k, 0) - D[0].get(k, 0) - D[1].get(k, 0) for k in set(D[0]) | set(D[1]) | set(D[3])}
C3 = {k: c for k, c in C3.items() if c}; C4 = {k: c for k, c in C4.items() if c}
G = [[pair(a, b, vol4) for b in (C3, C4)] for a in (C3, C4)]
orth = all(pair(c, d, vol4) == 0 for c in (C3, C4) for d in (D[0], D[1]))
check("H2-06", "C3=D3-D1-D2, C4=D4-D1-D2 orthogonal to <D1,D2> with Gram [[-2,-1],[-1,-2]] (A_2(-1))",
      orth and G == [[-2, -1], [-1, -2]], G)

# ================================================================ H2b: E^4
print("\n=== H2b: Hodge ring of E^4 and divisor-product spans ===")
n8 = 8
def relabel(alpha, idx_map):
    out = {}
    for I, c in alpha.items():
        seq = [idx_map[i] for i in I]
        key = tuple(sorted(seq))
        out[key] = out.get(key, 0) + perm_sign(seq)*c
    return {k: c for k, c in out.items() if c}

divs, dnames = [], []
for i in range(4):                                         # pr_i^*[pt] = fibre class
    divs.append({(2*i, 2*i+1): 1}); dnames.append(f"F{i}")
for i, j in itertools.combinations(range(4), 2):          # pr_ij^* of diagonal and Gamma_A
    m = {0: 2*i, 1: 2*i+1, 2: 2*j, 3: 2*j+1}
    divs.append(relabel(D[2], m)); dnames.append(f"Delta{i}{j}")
    divs.append(relabel(D[3], m)); dnames.append(f"GammaA{i}{j}")
U8 = block_diag([U2]*4)
check("H2-07", "All 16 explicit divisors on E^4 are of type (1,1)",
      all(derivation(d, U8) == {} for d in divs))

hodge_dims, prod_ranks, sat = [], [], []
products = {0: [{(): 1}], 1: divs}
for k in range(2, 5):
    pk = []
    for combo in itertools.combinations_with_replacement(range(16), k):
        w = {(): 1}
        for t in combo:
            w = wedge(w, divs[t])
            if not w:
                break
        if w:
            pk.append(w)
    products[k] = pk
for k in range(0, 5):
    m = 2*k
    if m == 0:
        hodge_dims.append(1); prod_ranks.append(1); sat.append([1]); continue
    DU, bas = DU_matrix(4, m)
    hd = len(bas) - DU.rank()
    rows = [vec(w, bas) for w in products[k]]
    rk = flint.fmpz_mat(rows).rank()
    hodge_dims.append(hd); prod_ranks.append(rk)
    inv = [d for d in snf_diag(rows) if d != 0]
    sat.append(inv)
check("H2-08", "dim_Q Hodge classes in H^{2k}(E^4,Q), k=0..4, equals (1,16,36,16,1)",
      hodge_dims == [1, 16, 36, 16, 1], hodge_dims)
check("H2-09", "Q-span of products of the 16 explicit divisors equals the full Hodge space in each degree",
      prod_ranks == hodge_dims, f"ranks {prod_ranks}")
idx = [int(sp.prod(s)) for s in sat]
print(f"   integral index [ (H^{{k,k}} ∩ H^{{2k}}(Z)) : Z-span of divisor products ], k=0..4: {idx}")
print(f"   (nontrivial SNF invariants per k: {[[d for d in s if d != 1] for s in sat]})")
check("H2-10", "[informational] k=1: 16 explicit divisors are a Z-basis of NS(E^4) (index 1)", idx[1] == 1, idx[1])

# ================================================================ R7 support: normal form of T
print("\n=== R7 support: Poincaré-Dulac normal form of T through degree 5 (exact, Q(zeta3)) ===")
class K:
    """Exact element a + b*w of Q(zeta3), w = zeta3, w^2 = -1 - w."""
    __slots__ = ("a", "b")
    def __init__(self, a, b=0): self.a, self.b = Fraction(a), Fraction(b)
    def __add__(s, o): o = o if isinstance(o, K) else K(o); return K(s.a+o.a, s.b+o.b)
    __radd__ = __add__
    def __neg__(s): return K(-s.a, -s.b)
    def __sub__(s, o): return s + (-(o if isinstance(o, K) else K(o)))
    def __rsub__(s, o): return K(o) - s
    def __mul__(s, o):
        o = o if isinstance(o, K) else K(o)
        return K(s.a*o.a - s.b*o.b, s.a*o.b + s.b*o.a - s.b*o.b)
    __rmul__ = __mul__
    def conj(s): return K(s.a - s.b, -s.b)
    def norm(s): return s.a*s.a - s.a*s.b + s.b*s.b
    def inv(s): n = s.norm(); c = s.conj(); return K(c.a/n, c.b/n)
    def __truediv__(s, o): o = o if isinstance(o, K) else K(o); return s*o.inv()
    def iszero(s): return s.a == 0 and s.b == 0
    def __eq__(s, o): o = o if isinstance(o, K) else K(o); return s.a == o.a and s.b == o.b
    def sym(s): return sp.nsimplify(s.a) + sp.nsimplify(s.b)*z3
    def __repr__(s): return f"({s.a})+({s.b})w"

W3 = K(0, 1); OMEGA = K(1, 1)          # zeta3, zeta6 = 1 + zeta3
ISQ3 = K(1, 2)                          # i*sqrt3 = 1 + 2 zeta3
DEG = 5

def padd(P, Q):
    R = dict(P)
    for k, c in Q.items():
        R[k] = R.get(k, K(0)) + c
    return {k: c for k, c in R.items() if not c.iszero()}
def pscale(P, s): return {k: c*s for k, c in P.items() if not (c*s).iszero()}
def pmul(P, Q):
    R = {}
    for (a1, b1), c1 in P.items():
        for (a2, b2), c2 in Q.items():
            if a1+b1+a2+b2 > DEG: continue
            k = (a1+a2, b1+b2); R[k] = R.get(k, K(0)) + c1*c2
    return {k: c for k, c in R.items() if not c.iszero()}
def pconj(P): return {(b, a): c.conj() for (a, b), c in P.items()}
def compose(P, Q):
    """P(Q, conj Q), truncated at DEG."""
    Qb = pconj(Q)
    maxd = max(a+b for a, b in P) if P else 0
    powQ = [{(0, 0): K(1)}]; powQb = [{(0, 0): K(1)}]
    for _ in range(maxd):
        powQ.append(pmul(powQ[-1], Q)); powQb.append(pmul(powQb[-1], Qb))
    R = {}
    for (a, b), c in P.items():
        R = padd(R, pscale(pmul(powQ[a], powQb[b]), c))
    return R
def Kpow(x, n):
    r = K(1)
    for _ in range(n): r = r*x
    return r
def rotfac(a, b):  # (omega z)^a (conj(omega z))^b = omega^{a-b} z^a zb^b
    return Kpow(OMEGA, (a - b) % 6)

# z = rho + zeta3*eta ; eta = (z - zb)/(i sqrt3) ; rho = z - zeta3*eta
Z  = {(1, 0): K(1)}
ETA = pscale(padd(Z, pscale(pconj(Z), K(-1))), ISQ3.inv())
RHO = padd(Z, pscale(ETA, K(-1)*W3))
def series_sin(u):
    t = u; out = dict(u); fac = 1; p = u
    for n in (3, 5):
        p = pmul(pmul(p, u), u); fac = fac*(n-1)*n
        out = padd(out, pscale(p, K(Fraction((-1)**((n-1)//2), fac))))
    return out
def series_expm1(u):
    out = {}; p = {(0, 0): K(1)}; fac = 1
    for n in range(1, DEG+1):
        p = pmul(p, u); fac *= n
        out = padd(out, pscale(p, K(Fraction(1, fac))))
    return out
sinE = series_sin(ETA)
RHOp = padd(RHO, pscale(sinE, K(-1)))
ETAp = padd(padd(ETA, series_expm1(RHO)), pscale(sinE, K(-1)))
T = padd(RHOp, pscale(ETAp, W3))
check("NF-01", "Linear part of T in z = rho + zeta3*eta is multiplication by zeta6",
      T.get((1, 0), K(0)) == OMEGA and T.get((0, 1), K(0)).iszero())

def resonant(a, b): return (a - b - 1) % 6 == 0
TN = dict(T)
for d in range(2, DEG+1):
    h = {}
    for (a, b), c in TN.items():
        if a+b == d and not resonant(a, b):
            h[(a, b)] = c / (rotfac(a, b) - OMEGA)
    if not h: continue
    H = padd(Z, h)
    G = dict(Z)                                   # inverse of H: G = z - h(G), iterate
    for _ in range(DEG):
        G = padd(Z, pscale(compose(h, G), K(-1)))
    TN = compose(G, compose(TN, H))
nonres_left = [(k, c) for k, c in TN.items() if sum(k) >= 2 and not resonant(*k)]
check("NF-02", "Normal form T_NF through degree 5 has only resonant monomials (a-b ≡ 1 mod 6)",
      not nonres_left, nonres_left)
tau, tau32, tau05 = TN.get((2, 1), K(0)), TN.get((3, 2), K(0)), TN.get((0, 5), K(0))
print(f"   tau  (z^2 zb)  = {sp.nsimplify(sp.expand(tau.sym()))}")
print(f"   tau05 (zb^5)   = {sp.nsimplify(sp.expand(tau05.sym()))}")
check("NF-03", "tau != 0 and tau05 != 0 (cubic and z̄^5 resonant coefficients of T itself)",
      not tau.iszero() and not tau05.iszero())
F6 = dict(TN)
for _ in range(5):
    F6 = compose(TN, F6)
mu_c, a05_c = F6.get((2, 1), K(0)), F6.get((0, 5), K(0))
even = [k for k in F6 if sum(k) in (2, 4)]
check("NF-04", "F = T_NF^6 = z + (deg 3) + (deg 5): no even-degree terms through degree 5",
      F6.get((1, 0)) == K(1) and not even, even)
OMB = OMEGA.conj()
check("NF-05", "Iterate identities: mu = 6*conj(omega)*tau and a05 = 6*conj(omega)*tau05",
      mu_c == K(6)*OMB*tau and a05_c == K(6)*OMB*tau05)
mu_s, a05_s = sp.nsimplify(sp.expand(mu_c.sym())), sp.nsimplify(sp.expand(a05_c.sym()))
print(f"   mu  (computed) = {sp.simplify(mu_s)}   owner: {MU_OWNER}")
print(f"   a05 (computed) = {sp.simplify(a05_s)}   owner: {A05_OWNER}")
check("NF-06", "Computed mu equals owner value -1/2 - 2i*sqrt3/3 (chart z = rho + zeta3*eta)",
      sp.simplify(mu_s - MU_OWNER) == 0)
check("NF-07", "Computed a05 equals owner value -49/8640 - 307i*sqrt3/25920",
      sp.simplify(a05_s - A05_OWNER) == 0)

# ================================================================ summary
npass = sum(r["pass"] for r in RESULTS)
print(f"\n{npass}/{len(RESULTS)} checks passed.")
src = open(__file__, "rb").read()
json.dump({"script_sha256": hashlib.sha256(src).hexdigest(),
           "sympy": sp.__version__, "python_flint": flint.__version__,
           "hodge_dims_E4": hodge_dims, "divisor_product_ranks_E4": prod_ranks,
           "integral_index_E4": idx, "intersection_matrix_E2": Mint,
           "results": RESULTS}, open("h1_h2_results.json", "w"), indent=2)
sys.exit(0 if npass == len(RESULTS) else 1)
