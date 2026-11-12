"""Integral cup lattice H^1(C, Z) of a cyclic C6-cover of P^1, with its deck action,
computed as integral parabolic cohomology of the regular local system Z[C6]
(Dettweiler-Wewers cocycle model and Thm 2.5 over the ring Z), and the one-sector
gluing length at p = 2.            Claude, 12 Nov 2026.  Exact; standard library only.

Usage:  python3 -I jacobian_lattice_c6_claude.py
Self-checks per datum: product one; H_g/E_g torsion-free of rank 2g (Riemann-Hurwitz);
Gram alternating with determinant 1; deck action of order 6 preserving the Gram;
character multiplicities equal Chevalley-Weil.
"""
from fractions import Fraction as Fr
from math import gcd
import importlib.util, os, sys, io, contextlib

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sec", os.path.join(here, "posdefect_c6_sector_check_claude.py"))
sec = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(sec)   # its own asserts run again

def row_reduce(A):
    """Integer row echelon form with transform: returns (H, U), U unimodular, U*A = H."""
    m = len(A); n = len(A[0]) if A else 0
    H = [r[:] for r in A]; U = [[int(i == j) for j in range(m)] for i in range(m)]
    r = 0
    for c in range(n):
        while True:
            nz = [i for i in range(r, m) if H[i][c] != 0]
            if len(nz) <= 1: break
            p = min(nz, key=lambda i: abs(H[i][c]))
            for i in nz:
                if i == p: continue
                q = H[i][c] // H[p][c]
                H[i] = [a - q*b for a, b in zip(H[i], H[p])]; U[i] = [a - q*b for a, b in zip(U[i], U[p])]
        nz = [i for i in range(r, m) if H[i][c] != 0]
        if nz:
            p = nz[0]; H[r], H[p] = H[p], H[r]; U[r], U[p] = U[p], U[r]; r += 1
            if r == m: break
    return H, U, r
def matmul(A, B): return [[sum(a*b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
def vecmat(v, M): return [sum(v[i]*M[i][j] for i in range(len(v))) for j in range(len(M[0]))]
def int_inverse(M):
    n = len(M); A = [[Fr(x) for x in r] + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(M)]
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c] != 0); A[c], A[p] = A[p], A[c]
        iv = 1/A[c][c]; A[c] = [x*iv for x in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]; A[i] = [x - f*y for x, y in zip(A[i], A[c])]
    out = [[x for x in r[n:]] for r in A]
    assert all(x.denominator == 1 for r in out for x in r)
    return [[int(x) for x in r] for r in out]
def det_int(M):
    n = len(M); A = [[Fr(x) for x in r] for r in M]; d = Fr(1)
    for c in range(n):
        p = next((i for i in range(c, n) if A[i][c] != 0), None)
        if p is None: return 0
        if p != c: A[c], A[p] = A[p], A[c]; d = -d
        d *= A[c][c]
        for i in range(c + 1, n):
            f = A[i][c]/A[c][c]; A[i] = [x - f*y for x, y in zip(A[i], A[c])]
    assert d.denominator == 1; return int(d)

n = 6
def perm(e):                               # right action of t^e on rows: basis vector b_a -> b_{a+e}
    return [[int((a + e) % n == b) for b in range(n)] for a in range(n)]
I6 = perm(0)

def lattice(exps, label):
    N = len(exps); assert sum(exps) % n == 0, "product is not one"
    g = [perm(e) for e in exps]
    gm1 = [[[g[i][a][b] - I6[a][b] for b in range(n)] for a in range(n)] for i in range(N)]
    # Z-basis of Im_i = Z^6 (g_i - 1), with one preimage per basis vector
    Bi, Pi = [], []
    for i in range(N):
        H, U, r = row_reduce(gm1[i]); Bi.append(H[:r]); Pi.append(U[:r])      # H[k] = U[k] (g_i - 1)
    dims = [len(b) for b in Bi]; off = [sum(dims[:i]) for i in range(N)]; tot = sum(dims)
    suffix = [None]*N; S = I6
    for i in range(N - 1, -1, -1): suffix[i] = S; S = matmul(g[i], S)          # g_{i+1} ... g_N
    assert S == I6
    rel = [vecmat(Bi[i][k], suffix[i]) for i in range(N) for k in range(dims[i])]   # tot x 6
    H, U, r = row_reduce(rel); Hg = U[r:]                                          # saturated kernel: coordinates
    k = len(Hg)
    # echelon form of Hg, to read coordinates
    HgE, UE, rk = row_reduce(Hg); assert rk == k
    piv = [next(j for j in range(tot) if row[j] != 0) for row in HgE]
    def coords_in_Hg(x):                   # x in the lattice spanned by HgE (coordinates w.r.t. HgE)
        x = x[:]; c = []
        for row, p in zip(HgE, piv):
            q, rem = divmod(x[p], row[p]); assert rem == 0
            c.append(q); x = [a - q*b for a, b in zip(x, row)]
        assert not any(x); return c
    def to_blocks(v_list):                 # tuple (v_i) with v_i in Im_i  ->  coordinate vector of length tot
        out = []
        for i in range(N):
            x = v_list[i][:]; Hrow = Bi[i]; c = []
            for row in Hrow:
                p = next(j for j in range(n) if row[j] != 0)
                q, rem = divmod(x[p], row[p]); assert rem == 0
                c.append(q); x = [a - q*b for a, b in zip(x, row)]
            assert not any(x); out += c
        return out
    def from_blocks(x):                    # -> (v_i), (v_i') with v_i'(g_i - 1) = v_i
        v, vp = [], []
        for i in range(N):
            c = x[off[i]:off[i] + dims[i]]
            v.append([sum(c[a]*Bi[i][a][j] for a in range(dims[i])) for j in range(n)])
            vp.append([sum(c[a]*Pi[i][a][j] for a in range(dims[i])) for j in range(n)])
        return v, vp
    # coboundaries
    Eg = [coords_in_Hg(to_blocks([vecmat([int(j == a) for j in range(n)], gm1[i]) for i in range(N)])) for a in range(n)]
    Ht, Ut, rc = row_reduce([list(c) for c in zip(*Eg)])        # Ut * Eg^T = Ht  =>  Eg * Ut^T = Ht^T
    Uc = [list(c) for c in zip(*Ut)]
    Lblk = [row[:rc] for row in matmul(Eg, Uc)]
    HL, _, r2 = row_reduce(Lblk)
    assert r2 == rc and all(abs(HL[i][i]) == 1 for i in range(rc)), "H_g/E_g has torsion"
    Uci = int_inverse(Uc)
    Wb = [vecmat(Uci[j], HgE) for j in range(rc, k)]            # basis of a complement, as block coordinates
    rank = k - rc
    genus2 = 2 - 2*n + sum(n - gcd(e, n) for e in exps)
    assert rank == genus2, (rank, genus2)
    def cup(x, y):                         # Thm 2.5 with <w, v> the dot product; dual class from x
        vs, _ = from_blocks(x); _, vp = from_blocks(y); tot_ = 0
        for i in range(N):
            tot_ += sum(a*b for a, b in zip(vs[i], vp[i]))
            w = None
            for j in range(i - 1, -1, -1):          # v_j* g_{j+1} ... g_{i-1} (g_i - 1)
                w0 = vs[j]
                for m in range(j + 1, i): w0 = vecmat(w0, g[m])
                w1 = vecmat(w0, gm1[i])
                tot_ += sum(a*b for a, b in zip(w1, vp[i]))
        return tot_
    G = [[cup(x, y) for y in Wb] for x in Wb]
    assert all(G[a][b] == -G[b][a] for a in range(rank) for b in range(rank)), "Gram not alternating"
    d = det_int(G); assert d == 1, f"Gram determinant {d}"
    # deck action: v_i -> v_i t ; coordinates in W
    P1 = perm(1)
    def wcoords(x):
        c = coords_in_Hg(x); y = vecmat(c, Uc); return y[rc:]
    T = [[0]*rank for _ in range(rank)]
    for j, x in enumerate(Wb):
        v, _ = from_blocks(x)
        img = wcoords(to_blocks([vecmat(vi, P1) for vi in v]))
        for i in range(rank): T[i][j] = img[i]
    Tp = [[int(i == j) for j in range(rank)] for i in range(rank)]
    for _ in range(6): Tp = matmul(Tp, T)
    assert Tp == [[int(i == j) for j in range(rank)] for i in range(rank)], "deck action not of order 6"
    Tt = [list(c) for c in zip(*T)]
    assert matmul(matmul(Tt, G), T) == G, "deck action does not preserve the Gram"
    print(f"{label}: exponents {tuple(exps)}: rank H^1 = {rank} = 2g, Gram alternating, det = 1, deck action of order 6 is an isometry")
    res = {}
    for kch in (1, 2, 3, 4, 5):
        cw = -2 + sum(1 for e in exps if (kch*e) % n != 0)
        if cw == 0: continue
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf): r, l = sec.sector(T, G, kch, f"chi_{kch}")
        assert r == cw, ("Chevalley-Weil", kch, r, cw)
        res[kch] = (r, l)
        print(f"   chi_{kch}: multiplicity {r} (= Chevalley-Weil); e M_R is the Hermitian dual of L_chi; "
              f"length(e M_R/L_chi) = v_2(det h_W) = {l}")
    return res

if __name__ == "__main__":
    out = {}
    out["separator"] = lattice([2, 2, 2, 2, 2, 3, 4, 4, 4, 5], "C6 separator")
    out["leaf A"] = lattice([3]*8 + [1, 5], "C6 (3^8,1,5)")
    out["leaf B"] = lattice([3]*8 + [2, 4], "C6 (3^8,2,4)")
    print("parity of v_2(det h_W) on chi_1:", {k: v[1][1] % 2 for k, v in out.items()})
    print("recorded parabolic-cup classes: separator [2] (odd), (3^8,1,5) [1] (even), (3^8,2,4) [1] (even)")
    assert out["separator"][1][1] % 2 == 1 and out["leaf A"][1][1] % 2 == 0 and out["leaf B"][1][1] % 2 == 0
    print("ALL PASS")
