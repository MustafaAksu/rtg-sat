"""Positive defect, C6 at p = 2 -- independent exact check (Claude), 12 Nov 2026.

Rebuilds the formal Z[C6]-lattice M0 of PR #56 from its description (not from the
printed matrices), compares with the printed G0 and T0, and checks:
  (a) the paired gluing group A = L^#/L over Z (Smith form);
  (b) the SECTOR statement: for the idempotent e_chi of one character,
      over R = Z[omega] localised at 2,
          Hermitian dual of L_chi  =  e_chi M_R ,   L_chi := M_R cap e_chi V,
      and  length_R(e_chi M_R / L_chi) = v_2(det H | L_chi);
  (c) 2 * (e_chi M_R) is contained in L_chi  (exponent t = v_2(6/1) = 1);
  (d) the same for M = M0 + 7 perfect rank-two summands (multiplicity 8).
No code of ChatGPT's script is imported.  Standard library only.
"""
from fractions import Fraction as Fr

class E:                                   # a + b*omega, omega^2 = -1 - omega
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0): s.a, s.b = Fr(a), Fr(b)
    @staticmethod
    def c(z): return z if isinstance(z, E) else E(z)
    def __add__(s, t): t = E.c(t); return E(s.a + t.a, s.b + t.b)
    __radd__ = __add__
    def __neg__(s): return E(-s.a, -s.b)
    def __sub__(s, t): return s + (-E.c(t))
    def __mul__(s, t):
        t = E.c(t); return E(s.a*t.a - s.b*t.b, s.a*t.b + s.b*t.a - s.b*t.b)
    __rmul__ = __mul__
    def conj(s): return E(s.a - s.b, -s.b)
    def nrm(s): return s.a*s.a - s.a*s.b + s.b*s.b
    def inv(s): c = s.conj(); n = s.nrm(); return E(c.a/n, c.b/n)
    def tr(s): return 2*s.a - s.b
    def __eq__(s, t): t = E.c(t); return s.a == t.a and s.b == t.b
    def iszero(s): return s.a == 0 and s.b == 0
    def __repr__(s): return f"({s.a}+{s.b}w)"

def v2q(q):
    q = Fr(q); assert q != 0; n, d, v = q.numerator, q.denominator, 0
    while n % 2 == 0: n //= 2; v += 1
    while d % 2 == 0: d //= 2; v -= 1
    return v
def v2(z):                                 # 2 is inert: v(a + b w) = min(v(a), v(b))
    z = E.c(z); assert not z.iszero()
    return min(v2q(x) for x in (z.a, z.b) if x != 0)

W = E(0, 1); ONE = E(1); ZERO = E(0)
ZETA = ONE + W                             # primitive 6th root of unity, = -omega^2
DELTA = E(1, 2)                            # sqrt(-3) = 2 omega + 1
assert DELTA*DELTA == E(-3) and ZETA*ZETA*ZETA == E(-1)
E0 = lambda x, y: (DELTA.inv()*x*y.conj()).tr()

# ---- M0 from its description --------------------------------------------------
half = Fr(1, 2)
basis = [(E(half), E(half)), (W*E(half), W*E(half)), (ONE, ZERO), (W, ZERO)]   # f_1, f_w, h_1, h_w
form = lambda u, v: 2*E0(u[0], v[0]) - 2*E0(u[1], v[1])
act = lambda u: (ZETA*u[0], W*W*u[1])
def coords(u):                             # (a,b) = x1 f_1 + x2 f_w + x3 h_1 + x4 h_w, x_i rational
    b = u[1]; x1, x2 = 2*b.a, 2*b.b
    r = u[0] - b
    return [x1, x2, r.a, r.b]
G0 = [[form(u, v) for v in basis] for u in basis]
T0 = [[None]*4 for _ in range(4)]
for j, u in enumerate(basis):
    cj = coords(act(u))
    assert all(x.denominator == 1 for x in cj), "action not integral"
    for i in range(4): T0[i][j] = cj[i]
G0_printed = [[0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, -2], [1, 0, 2, 0]]
T0_printed = [[-1, 1, 0, 0], [-1, 0, 0, 0], [1, -1, 1, -1], [1, 0, 1, 0]]
assert G0 == G0_printed, "Gram differs from PR #56"
assert T0 == T0_printed, "action differs from PR #56"
print("M0 rebuilt from its description: Gram and action equal the printed G0, T0")

def mmul(A, B): return [[sum((E.c(A[i][k])*E.c(B[k][j]) for k in range(len(B))), ZERO) for j in range(len(B[0]))] for i in range(len(A))]
def ident(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
def det(A):
    A = [[E.c(x) for x in r] for r in A]; n = len(A); d = ONE
    for c in range(n):
        p = next((i for i in range(c, n) if not A[i][c].iszero()), None)
        if p is None: return ZERO
        if p != c: A[c], A[p] = A[p], A[c]; d = -d
        d = d*A[c][c]; iv = A[c][c].inv()
        for i in range(c + 1, n):
            f = A[i][c]*iv
            A[i] = [x - f*y for x, y in zip(A[i], A[c])]
    return d
def minv(A):
    n = len(A); A = [[E.c(x) for x in r] + ident(n)[i] for i, r in enumerate(A)]
    for c in range(n):
        p = next(i for i in range(c, n) if not A[i][c].iszero()); A[c], A[p] = A[p], A[c]
        iv = A[c][c].inv(); A[c] = [x*iv for x in A[c]]
        for i in range(n):
            if i != c and not A[i][c].iszero():
                f = A[i][c]; A[i] = [x - f*y for x, y in zip(A[i], A[c])]
    return [r[n:] for r in A]

def lattice_basis(cols):
    """R-basis (R = Z[w] localised at 2) of the lattice spanned by the columns `cols`
    (vectors over K): column reduction with pivots of minimal valuation."""
    cols = [c[:] for c in cols]; n = len(cols[0]); out = []; row = 0
    while row < n and cols:
        live = [c for c in cols if not c[row].iszero()]
        if not live: row += 1; continue
        p = min(live, key=lambda c: v2(c[row])); iv = p[row].inv(); new = []
        for c in cols:
            if c is p: continue
            f = c[row]*iv                  # integral, since p has minimal valuation
            c2 = [x - f*y for x, y in zip(c, p)]
            if any(not x.iszero() for x in c2): new.append(c2)
        out.append(p); cols = new; row += 1
    return out
def saturate(cols):
    """R-basis of (K-span of cols) cap R^n, with the rows where it is an identity block:
    reduced echelon form over K with pivots of minimal valuation (hence unit pivots)."""
    cols = [c[:] for c in cols if any(not x.iszero() for x in c)]; out = []; rows = []
    while cols:
        c = cols[0]
        m = min(v2(x) for x in c if not x.iszero())
        r = next(i for i, x in enumerate(c) if not x.iszero() and v2(x) == m)
        iv = c[r].inv(); c = [x*iv for x in c]          # now integral with a unit at row r
        red = lambda d: [x - d[r]*y for x, y in zip(d, c)]
        out = [red(d) for d in out]
        cols = [d for d in (red(d) for d in cols[1:]) if any(not x.iszero() for x in d)]
        out.append(c); rows.append(r)
    for j, c in enumerate(out):
        assert all(x.iszero() or v2(x) >= 0 for x in c), "saturation basis not integral"
        assert all(c[rows[i]] == (ONE if i == j else ZERO) for i in range(len(out)))
    return out, rows

def sector(T, G, k, label):
    n = len(T); Tk = ident(n); e = [[ZERO]*n for _ in range(n)]
    zi = ONE; zinv = ZETA.inv()
    for j in range(6):                     # e = (1/6) sum_j zeta^{-jk} T^j
        ch = ONE
        for _ in range((j*k) % 6): ch = ch*zinv
        e = [[e[a][b] + ch*Tk[a][b]*E(Fr(1, 6)) for b in range(n)] for a in range(n)]
        Tk = mmul(Tk, T)
    assert mmul(e, e) == e, "not idempotent"
    cols = [[e[i][j] for i in range(n)] for j in range(n)]
    eM = lattice_basis(cols)               # e M_R
    r = len(eM)
    L, rows = saturate(cols)         # L_chi = M_R cap e V
    assert len(L) == r
    def coord(v):                          # v in the span: its coordinates are its entries at the pivot rows
        x = [v[i] for i in rows]
        assert all(sum((x[j]*L[j][i] for j in range(r)), ZERO) == v[i] for i in range(n))
        return x
    D = [coord(v) for v in eM]             # D[a] = coordinates of the a-th generator
    Dm = [[D[a][b] for a in range(r)] for b in range(r)]
    length = -v2(det(Dm))
    # 2 e M inside L
    assert all(x.iszero() or v2(2*x) >= 0 for row in D for x in row), "2 eM not in L"
    # Hermitian form on L_chi: H(x,y) = x^T G conj(y); here the pairing of the chi-part with its conjugate
    Gk = [[E.c(x) for x in row] for row in G]
    def H(x, y): return sum((x[i]*Gk[i][j]*y[j].conj() for i in range(n) for j in range(n)), ZERO)
    HL = [[H(L[a], L[b]) for b in range(r)] for a in range(r)]
    vdet = v2(det(HL))
    # dual test: eM = L^#  <=>  the matrix H(L_a, eM_b) is in GL_r(R)
    P = [[H(L[a], eM[b]) for b in range(r)] for a in range(r)]
    assert all(x.iszero() or v2(x) >= 0 for row in P for x in row), "eM not in the dual"
    assert v2(det(P)) == 0, "eM is not the whole dual"
    print(f"{label}: sector rank {r}; e M_R = Hermitian dual of L_chi: yes; "
          f"length(e M_R / L_chi) = {length}; v_2(det H|L_chi) = {vdet}; 2 e M_R in L_chi: yes")
    assert length == vdet
    return r, length

r1, l1 = sector(T0, G0, 1, "M0, character zeta6      ")
r4, l4 = sector(T0, G0, 4, "M0, character zeta6^4=w^2")
assert (r1, l1, r4, l4) == (1, 1, 1, 1)

# ---- paired gluing over Z: L = M cap (chi1 + chi5 part) is spanned by h_1, h_w ----
GL = [[G0[i][j] for j in (2, 3)] for i in (2, 3)]
assert GL == [[0, -2], [2, 0]]
print("M0, paired over Z: Gram of L = [[0,-2],[2,0]]; A = L^#/L = (Z/2)^2, 2A = 0, order 4")

# ---- M = M0 + 7 perfect summands (R, E0, zeta6) -------------------------------
TK = [[1, -1], [1, 0]]; J = [[0, -1], [1, 0]]
bK = [ONE, W]
assert [[E0(x, y) for y in bK] for x in bK] == J
n = 18
T = [[0]*n for _ in range(n)]; G = [[0]*n for _ in range(n)]
for i in range(4):
    for j in range(4): T[i][j] = T0[i][j]; G[i][j] = G0[i][j]
for s in range(7):
    o = 4 + 2*s
    for i in range(2):
        for j in range(2): T[o+i][o+j] = TK[i][j]; G[o+i][o+j] = J[i][j]
assert det(G) == ONE
r, l = sector(T, G, 1, "M (rank 18), character zeta6")
assert (r, l) == (8, 1)
print("ALL PASS")
