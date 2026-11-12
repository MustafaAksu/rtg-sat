"""C3 x F20, sigma = omega (x) rho4, p = 5: the sector module A_chi = e_chi M_R / L_chi
of the integral cup lattice M = H^1(C, Z_5), computed modulo 5.      Claude, 12 Nov 2026.

Method.  t = v_5(|G|/chi(1)) = v_5(15) = 1, so 5 e_chi lies in R[G] (R = Z_5[omega]) and
    A_chi = e_chi M_R / (M_R cap e_chi V)  ~=  image of (5 e_chi) on M/5M (x) F_25
(x = e m  |->  5 e m mod 5; its kernel is {e m in M_R} = L_chi).  So A_chi is an
F_25[G]-module and only H^1(C, F_5) with its deck action is needed.
H^1(C, F_5) is the parabolic cohomology of the regular local system F_5[G]
(Dettweiler-Wewers cocycle model; cup form by their Thm 2.5 with the permutation pairing).

Per tuple the script asserts: product one; the tuple generates G; dim Z - rank E_g = 2g
(Riemann-Hurwitz); the cup Gram on H^1(C, F_5) is alternating and nonsingular.
Output: dim_F25 A_chi and the multiplicities of the four simple constituents, read off
from the eigenvalues of c: x -> 2x (C5 acts trivially on A_chi, C3 by a scalar).

Usage: python3 -I f20_sector_mod5_claude.py <path to a4_direct_out.txt>
Standard library only.  No HCG engine, no earlier HHO script is imported.
"""
import sys, ast
P = 5
# ---------------- group C3 x F20 ----------------
F20 = [(a, b) for a in (1, 2, 3, 4) for b in range(5)]                 # x -> a x + b
def fcomp(f, g): return ((f[0]*g[0]) % 5, (f[0]*g[1] + f[1]) % 5)      # f o g
G = [(k, f) for k in range(3) for f in F20]
IDX = {g: i for i, g in enumerate(G)}
def gmul(x, y): return ((x[0] + y[0]) % 3, fcomp(x[1], y[1]))
ID = (0, (1, 0)); n = len(G)
def gpow_order(g):
    x, o = g, 1
    while x != ID: x = gmul(x, g); o += 1
    return o
RIGHT = {g: [IDX[gmul(x, g)] for x in G] for g in G}                   # x -> x g
LEFT = {g: [IDX[gmul(g, x)] for x in G] for g in G}                    # x -> g x
def act(v, perm):                                                       # (v.g)[x g] = v[x]
    out = [0]*n
    for i, j in enumerate(perm): out[j] = v[i]
    return out
# ---------------- F_25 = F_5[w], w^2 + w + 1 = 0; element a + b w coded as a + 5 b ----------------
def enc(a, b): return (a % 5) + 5*(b % 5)
ADD = [[enc(x % 5 + y % 5, x//5 + y//5) for y in range(25)] for x in range(25)]
def _mul(x, y):
    a, b, c, d = x % 5, x//5, y % 5, y//5
    return enc(a*c - b*d, a*d + b*c - b*d)
MUL = [[_mul(x, y) for y in range(25)] for x in range(25)]
NEG = [enc(-(x % 5), -(x//5)) for x in range(25)]
INV = [0]*25
for x in range(1, 25):
    INV[x] = next(y for y in range(1, 25) if MUL[x][y] == 1)
W = enc(0, 1); W2 = MUL[W][W]
assert ADD[ADD[W2][W]][1] == 0

def rank25(vecs, basis=None):
    """Echelon basis (dict pivot -> vector) over F_25, extending `basis`."""
    basis = dict(basis) if basis else {}
    for v in vecs:
        v = v[:]
        for p in sorted(basis):
            if v[p]:
                f = v[p]; b = basis[p]
                v = [ADD[x][NEG[MUL[f][y]]] if y else x for x, y in zip(v, b)]
        p = next((i for i, x in enumerate(v) if x), None)
        if p is None: continue
        iv = INV[v[p]]; v = [MUL[iv][x] if x else 0 for x in v]
        basis[p] = v
    return basis
def kernel5(rows, ncols):
    """Basis of {x in F_5^ncols : rows . x = 0}."""
    M = [r[:] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        t = next((i for i in range(r, len(M)) if M[i][c] % 5), None)
        if t is None: continue
        M[r], M[t] = M[t], M[r]
        iv = pow(M[r][c], -1, 5); M[r] = [(x*iv) % 5 for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % 5:
                f = M[i][c]; M[i] = [(x - f*y) % 5 for x, y in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == len(M): break
    free = [c for c in range(ncols) if c not in piv]; out = []
    for c in free:
        v = [0]*ncols; v[c] = 1
        for j, p in enumerate(piv): v[p] = (-M[j][c]) % 5
        out.append(v)
    return out
def det_nonzero5(M):
    M = [[x % 5 for x in r] for r in M]; m = len(M)
    for c in range(m):
        t = next((i for i in range(c, m) if M[i][c]), None)
        if t is None: return False
        M[c], M[t] = M[t], M[c]; iv = pow(M[c][c], -1, 5)
        for i in range(c + 1, m):
            if M[i][c]:
                f = (M[i][c]*iv) % 5; M[i] = [(x - f*y) % 5 for x, y in zip(M[i], M[c])]
    return True

def rho4(f): return 4 if f == (1, 0) else (-1 if f[0] == 1 else 0)
CGEN = (0, (2, 0))                                                      # c : x -> 2x, of order 4

def analyse(tup):
    N = len(tup); gs = [tuple((k, tuple(f))) for k, f in tup]
    prod = ID
    for g in gs: prod = gmul(prod, g)
    assert prod == ID, "product is not one"
    S = {ID}; fr = [ID]
    while fr:
        x = fr.pop()
        for g in gs:
            y = gmul(x, g)
            if y not in S: S.add(y); fr.append(y)
    assert len(S) == n, "tuple does not generate G"
    suffix = [None]*N; s = ID
    for i in range(N - 1, -1, -1): suffix[i] = s; s = gmul(gs[i], s)
    # cycles of right multiplication by g_i
    cycles = []
    for g in gs:
        seen = [False]*n; cs = []
        for x in range(n):
            if seen[x]: continue
            c = [x]; seen[x] = True; y = RIGHT[g][x]
            while y != x: c.append(y); seen[y] = True; y = RIGHT[g][y]
            cs.append(c)
        cycles.append(cs)
    tot = N*n
    rows = []
    for i in range(N):                      # v_i in Im(g_i - 1): zero sum on every cycle
        for c in cycles[i]:
            r = [0]*tot
            for x in c: r[i*n + x] = 1
            rows.append(r)
    for y in range(n):                      # relation (2): sum_i v_i . (g_{i+1} ... g_N) = 0, coordinate y
        r = [0]*tot
        for i in range(N):
            perm = RIGHT[suffix[i]]
            for x in range(n):
                if perm[x] == y: r[i*n + x] = 1
        rows.append(r)
    Z = kernel5(rows, tot)
    def blocks(z): return [z[i*n:(i + 1)*n] for i in range(N)]
    Eg = []
    for a in range(n):
        u = [0]*n; u[a] = 1; z = []
        for i in range(N):
            ug = act(u, RIGHT[gs[i]]); z += [(x - y) % 5 for x, y in zip(ug, u)]
        Eg.append(z)
    EB = rank25(Eg); rE = len(EB)
    two_g = 2 - 2*n + sum(n - n//gpow_order(g) for g in gs)
    ZB = rank25(Z)
    assert len(ZB) == len(Z) and len(rank25(Z, EB)) == len(Z), "E_g not inside Z"
    assert len(Z) - rE == two_g, (len(Z), rE, two_g)
    # complement of E_g in Z: vectors of Z that enlarge the echelon basis
    comp = []; B = dict(EB)
    for z in Z:
        B2 = rank25([z], B)
        if len(B2) > len(B): comp.append(z); B = B2
    assert len(comp) == two_g
    # cup form (Thm 2.5), to validate the model: alternating and nonsingular mod 5
    def primitive(i, v):                    # u with u.g_i - u = v
        u = [0]*n
        for c in cycles[i]:
            for j in range(1, len(c)): u[c[j]] = (u[c[j-1]] - v[c[j]]) % 5
        chk = [(x - y) % 5 for x, y in zip(act(u, RIGHT[gs[i]]), u)]
        assert chk == [x % 5 for x in v]
        return u
    pre = []
    for z in comp:
        v = blocks(z); vp = [primitive(i, v[i]) for i in range(N)]
        # left factors: for each i, the vector  v_i + sum_{j<i} v_j g_{j+1}..g_{i-1}(g_i - 1)
        left = []
        for i in range(N):
            acc = v[i][:]
            for j in range(i):
                w = v[j]
                for m in range(j + 1, i): w = act(w, RIGHT[gs[m]])
                w2 = act(w, RIGHT[gs[i]])
                acc = [(a + b - c) % 5 for a, b, c in zip(acc, w2, w)]
            left.append(acc)
        pre.append((left, vp))
    Gm = [[sum(sum(a*b for a, b in zip(pre[x][0][i], pre[y][1][i])) for i in range(N)) % 5
           for y in range(two_g)] for x in range(two_g)]
    assert all((Gm[a][b] + Gm[b][a]) % 5 == 0 for a in range(two_g) for b in range(two_g)), "Gram not alternating mod 5"
    assert det_nonzero5(Gm), "Gram singular mod 5"
    # the operator 5 e_chi = (1/3) sum_g chi(g^-1) g  ==  2 sum_g chi(g^-1) g  (mod 5)
    def deck(z, g): return sum((act(b, LEFT[g]) for b in blocks(z)), [])
    def theta(z, kk):                       # chi = omega^kk (x) rho4
        out = [0]*tot
        for g in G:
            r = rho4(g[1])
            if r == 0: continue
            ginv = next(h for h in G if gmul(g, h) == ID)
            coef = MUL[enc(2*r, 0)][[1, W, W2][(kk*ginv[0]) % 3]]     # 2 * chi(g^-1)
            img = deck(z, g)
            out = [ADD[o][MUL[coef][x]] if x else o for o, x in zip(out, img)]
        return out
    res = {}
    for kk in (1, 2):
        imgs = [theta(z, kk) for z in comp]
        VA = rank25(imgs, EB); dimA = len(VA) - rE
        mult = {}
        for lam in (1, 2, 3, 4):
            sh = [[ADD[x][NEG[MUL[lam][y]]] for x, y in zip(deck(v, CGEN), v)] for v in imgs]
            mult[lam] = dimA - (len(rank25(sh, EB)) - rE)
        assert sum(mult.values()) == dimA, (mult, dimA)
        # C5 acts trivially on A_chi
        tau = (0, (1, 1))
        assert all(len(rank25([[ADD[x][NEG[y]] for x, y in zip(deck(v, tau), v)]], EB)) == rE for v in imgs)
        res[kk] = (dimA, tuple(mult[l] for l in (1, 2, 3, 4)))
    return two_g, res

if __name__ == "__main__":
    lines = [l for l in open(sys.argv[1]) if l.startswith("[")]
    print("# tuple | 2g | t | recorded sig, class | chi=w(x)rho4: dim A, (n_1,n_2,n_3,n_4) | chi=w^2(x)rho4: dim A, (n_1..n_4)")
    for l in lines:
        tup = ast.literal_eval(l[:l.index("] dim") + 1])
        sig = l[l.index("sig") + 4:l.index("class")].strip(); cls = l[l.index("class") + 6:l.index("t=#")].strip()
        t = sum(1 for k, f in tup if k != 0)
        two_g, res = analyse(tup)
        print(f"{tup} | {two_g} | {t} | {sig} {cls} | {res[1][0]} {res[1][1]} | {res[2][0]} {res[2][1]}", flush=True)
    print("DONE: all per-tuple assertions passed")
