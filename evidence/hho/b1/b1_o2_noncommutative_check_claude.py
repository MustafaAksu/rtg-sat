"""B1 / O2 -- independent exact check (Claude), 12 Nov 2026.

Compares, on unitary product-one tuples in rank 2 and 3 over K = Q(omega):
  (a) the triangular form B of the HCG locality proof (left action, linear-first);
  (b) Dettweiler-Wewers Thm 2.5, implemented literally in right-action terms
      with an explicit dual space of row vectors;
  (c) Dettweiler-Wewers eq. (21), sum <w*_i - w*_{i-1}, u_i - w_{i-1}>.
Also checks: DW relation (2) for the converted cocycle and for the dual cocycle,
B = 0 against coboundaries, B skew-Hermitian on Z, rad(B|Z) = D(V) by rank.
Tuples are noncommutative and the Hermitian form is not the identity.
No HCG or ChatGPT code is imported.  Standard library only.
"""
from fractions import Fraction as Fr
import itertools, random, sys

class E:                                   # a + b*omega, omega^2 = -1 - omega
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0): s.a, s.b = Fr(a), Fr(b)
    @staticmethod
    def c(z): return z if isinstance(z, E) else E(z)
    def __add__(s, t): t = E.c(t); return E(s.a + t.a, s.b + t.b)
    __radd__ = __add__
    def __neg__(s): return E(-s.a, -s.b)
    def __sub__(s, t): return s + (-E.c(t))
    def __rsub__(s, t): return E.c(t) - s
    def __mul__(s, t):
        t = E.c(t)
        return E(s.a*t.a - s.b*t.b, s.a*t.b + s.b*t.a - s.b*t.b)
    __rmul__ = __mul__
    def conj(s): return E(s.a - s.b, -s.b)
    def nrm(s): return s.a*s.a - s.a*s.b + s.b*s.b
    def inv(s): c = s.conj(); n = s.nrm(); return E(c.a/n, c.b/n)
    def __eq__(s, t): t = E.c(t); return s.a == t.a and s.b == t.b
    def __hash__(s): return hash((s.a, s.b))
    def iszero(s): return s.a == 0 and s.b == 0
    def __repr__(s): return f"({s.a}+{s.b}w)"

W = E(0, 1); ZERO = E(0); ONE = E(1)

def mat(r, c, f): return [[E.c(f(i, j)) for j in range(c)] for i in range(r)]
def eye(n): return mat(n, n, lambda i, j: 1 if i == j else 0)
def mul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), ZERO) for j in range(len(B[0]))] for i in range(len(A))]
def add(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def ct(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def rref(A):
    A = [r[:] for r in A]; piv = []; r = 0
    for c in range(len(A[0]) if A else 0):
        p = next((i for i in range(r, len(A)) if not A[i][c].iszero()), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        iv = A[r][c].inv(); A[r] = [x*iv for x in A[r]]
        for i in range(len(A)):
            if i != r and not A[i][c].iszero():
                f = A[i][c]; A[i] = [x - f*y for x, y in zip(A[i], A[r])]
        piv.append(c); r += 1
    return A, piv
def rank(A): return len(rref(A)[1])
def inv(A):
    n = len(A); R, piv = rref([A[i] + eye(n)[i] for i in range(n)])
    assert piv[:n] == list(range(n)); return [row[n:] for row in R]
def nullspace(A):
    R, piv = rref(A); n = len(A[0]); out = []
    for f in [c for c in range(n) if c not in piv]:
        v = [ZERO]*n; v[f] = ONE
        for k, c in enumerate(piv): v[c] = -R[k][f]
        out.append(v)
    return out
def col(v): return [[x] for x in v]
def solve(A, b):                            # one solution of A z = b (b a column list)
    n = len(A[0]); R, piv = rref([A[i] + [b[i]] for i in range(len(A))])
    assert n not in piv, "inconsistent system"
    z = [ZERO]*n
    for k, c in enumerate(piv): z[c] = R[k][n]
    return z

def monomial(perm, phases):
    n = len(perm); return mat(n, n, lambda i, j: (W**0 if False else phases[j]) if perm[j] == i else 0)
def wpow(k):
    z = ONE
    for _ in range(k % 6): z = z*(-W*W)     # -omega^2 is a primitive 6th root of unity
    return z

def run(n, N, seed, P):
    rnd = random.Random(seed)
    Pi = inv(P)
    H = mul(ct(Pi), Pi)                     # h0(u,v) = v^* H u ; g' = P g P^-1 is unitary for it
    while True:
        gs = []
        for _ in range(N - 1):
            perm = list(range(n)); rnd.shuffle(perm)
            gs.append(mul(mul(P, monomial(perm, [wpow(rnd.randrange(6)) for _ in range(n)])), Pi))
        prod = eye(n)
        for g in gs: prod = mul(prod, g)
        gs.append(inv(prod))
        if all(not meq(g, eye(n)) for g in gs) and not meq(mul(gs[0], gs[1]), mul(gs[1], gs[0])): break
    ginv = [inv(g) for g in gs]
    for g in gs: assert meq(mul(mul(ct(g), H), g), H), "not unitary"
    h0 = lambda u, v: mul(mul(ct(col(v)), H), col(u))[0][0]
    Q = [eye(n)]
    for g in gs: Q.append(mul(Q[-1], g))
    assert meq(Q[N], eye(n))
    I = eye(n)
    Eb = []                                 # bases of E_i = im(1 - g_i), as columns
    for g in gs:
        M = sub(I, g); R, piv = rref(M)
        Eb.append([[M[r][c] for r in range(n)] for c in piv])
    # coordinates: x = (x_1..x_N), x_i = sum_k t_{i,k} Eb[i][k]
    idx = [(i, k) for i in range(N) for k in range(len(Eb[i]))]
    Cmat = [[ZERO]*len(idx) for _ in range(n)]
    for a, (i, k) in enumerate(idx):
        v = mul(Q[i], col(Eb[i][k]))
        for r in range(n): Cmat[r][a] = v[r][0]
    Zb = nullspace(Cmat)
    def unpack(t):
        x = [[ZERO]*n for _ in range(N)]
        for a, (i, k) in enumerate(idx):
            for r in range(n): x[i][r] = x[i][r] + t[a]*Eb[i][k][r]
        return x
    def A_(i, xi): return solve(sub(I, gs[i]), xi)       # some v with (1-g_i)v = x_i
    def apply(M, v): return [r[0] for r in mul(M, col(v))]
    def Bform(x, y):
        tot = ZERO
        for i in range(N):
            F = [ZERO]*n
            for j in range(i): F = [a + b for a, b in zip(F, apply(Q[j], x[j]))]
            u = [a + b for a, b in zip(apply(inv(Q[i]), F), A_(i, x[i]))]
            tot = tot + h0(u, y[i])
        return tot
    # --- DW side, literal: right action v.g := g^{-1} v on columns; V* = rows, w.g* := w g
    ract = lambda v, i: apply(ginv[i], v)
    def row_of(y): return mul(ct(col(y)), H)[0]          # f_y(v) = h0(v,y) = y^* H v
    rdual = lambda w, i: [sum((w[k]*gs[i][k][j] for k in range(n)), ZERO) for j in range(n)]
    pair = lambda w, v: sum((a*b for a, b in zip(w, v)), ZERO)
    def dw_data(x, y):
        v = [apply(ginv[i], x[i]) for i in range(N)]
        vs = [row_of(apply(ginv[i], y[i])) for i in range(N)]
        for i in range(N):                                # <w.g*, v.g> = <w, v>
            assert pair(rdual(vs[i], i), ract(v[i], i)) == pair(vs[i], v[i])
        for seq, act in ((v, ract), (vs, rdual)):         # relation (2)
            tot = [ZERO]*n
            for i in range(N):
                t = seq[i]
                for k in range(i + 1, N): t = act(t, k)
                tot = [a + b for a, b in zip(tot, t)]
            assert all(z.iszero() for z in tot), "relation (2) fails"
        vp = [solve(sub(ginv[i], I), v[i]) for i in range(N)]   # v'.(g_i - 1) = v_i
        return v, vs, vp
    def DW25(x, y):
        v, vs, vp = dw_data(x, y); tot = ZERO
        for i in range(N):
            tot = tot + pair(vs[i], vp[i])
            for j in range(i):
                w = vs[j]
                for k in range(j + 1, i): w = rdual(w, k)
                w = [a - b for a, b in zip(rdual(w, i), w)]
                tot = tot + pair(w, vp[i])
        return tot
    def DW21(x, y):
        v, vs, vp = dw_data(x, y)
        w = [v[0]]; ws = [vs[0]]
        for i in range(1, N):
            w.append([a + b for a, b in zip(v[i], ract(w[i-1], i))])
            ws.append([a + b for a, b in zip(vs[i], rdual(ws[i-1], i))])
        z = [ZERO]*n; tot = ZERO
        for i in range(N):
            wp = w[i-1] if i else z; wsp = ws[i-1] if i else z
            u = solve(sub(ginv[i], I), [a - b for a, b in zip(w[i], wp)])
            tot = tot + pair([a - b for a, b in zip(ws[i], wsp)], [a - b for a, b in zip(u, wp)])
        return tot
    xs = [unpack(t) for t in Zb]; m = len(xs); cnt = 0
    G = [[Bform(x, y) for y in xs] for x in xs]
    for a in range(m):
        for b in range(m):
            assert G[a][b] == DW25(xs[a], xs[b]), "B != DW Thm 2.5"
            assert G[a][b] == DW21(xs[a], xs[b]), "B != DW eq (21)"
            assert G[a][b] == -(G[b][a].conj()), "B not skew-Hermitian on Z"
            cnt += 1
    # coboundaries D(v) = ((g_i - 1) v)_i lie in Z and in the radical
    for r in range(n):
        e = [ONE if k == r else ZERO for k in range(n)]
        d = [apply(sub(gs[i], I), e) for i in range(N)]
        tot = [ZERO]*n
        for i in range(N): tot = [a + b for a, b in zip(tot, apply(Q[i], d[i]))]
        assert all(z.iszero() for z in tot)
        for y in xs: assert Bform(d, y).iszero() and Bform(y, d).iszero()
    fix = n - rank([sum((sub(g, I)[r] for g in [gg]), []) for gg in gs for r in range(n)])
    dimD = n - fix
    assert rank(G) == m - dimD, "rad(B|Z) != D(V)"
    return m, m - dimD, fix, cnt

if __name__ == "__main__":
    P2 = mat(2, 2, lambda i, j: [[1, 1], [0, 2]][i][j])
    P3 = mat(3, 3, lambda i, j: [[1, 1, 0], [0, 1, 2], [1, 0, 3]][i][j])
    total = 0
    for n, N, P in ((2, 4, P2), (2, 5, P2), (3, 4, P3), (3, 5, P3)):
        for seed in range(1, 6):
            m, par, fix, cnt = run(n, N, seed, P)
            total += cnt
            print(f"n={n} N={N} seed={seed}: dim Z={m}, dim H1_par={par}, fixed={fix}, entries checked={cnt}: PASS")
    print(f"ALL PASS: {total} entries; B = DW Thm 2.5 = DW eq (21) on Z; skew-Hermitian; rad = D(V)")
