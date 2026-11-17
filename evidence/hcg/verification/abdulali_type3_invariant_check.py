"""HCG check for the OPEN 12 review: invariant counts behind Abdulali's Theorem 4.1 (type III, m = 3).

Model (no third-party text used): V_C = U (x) C^2 with U = C^6 carrying SO(6) (the group G_1(C)), and
D (x) C = M_2(C) acting on the factor C^2. K = Q(sqrt(-3)) sits in D = (-3,-1)_Q by
u -> diag(s, -s), v -> [[0,-1],[1,0]], s^2 = -3; its eigenlines in C^2 are e_sigma = (1,0), e_sigmabar = (0,1).
For a in C^2 (one factor) or C^{2k} (A^k), det(U (x) a) = (u_1 (x) a) ^ ... ^ (u_6 (x) a) in wedge^6.
The Weil classes of K on A, complexified, are spanned by det(U (x) e_sigma), det(U (x) e_sigmabar).

All arithmetic is exact in F_p, p = 1000003 (p = 1 mod 3, so s = sqrt(-3) exists). A rank over F_p is a
lower bound for the rank over Q(sqrt(-3)) of the same integral vectors; a kernel dimension over F_p is an
upper bound for the kernel over characteristic 0. Each claim below uses the bound in the safe direction.
Usage: python3 evidence/hcg/verification/abdulali_type3_invariant_check.py
"""
import itertools
import random
import numpy as np

P = 1000003
S = next(x for x in range(2, P) if (x * x + 3) % P == 0)
N = 6
random.seed(20261117)


def rank_mod_p(rows):
    M = np.array(rows, dtype=np.int64) % P
    r = 0
    nrows, ncols = M.shape
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if M[i, c]:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), P - 2, P)
        M[r] = (M[r] * inv) % P
        col = M[:, c].copy()
        col[r] = 0
        nz = np.nonzero(col)[0]
        if len(nz):
            M[nz] = (M[nz] - np.outer(col[nz], M[r])) % P
        r += 1
        if r == nrows:
            break
    return r


def perm_sign(seq):
    seq = list(seq)
    sgn = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                sgn = -sgn
    return sgn


def det_vector(a, p_dim):
    """coefficients of det(U (x) a) on the basis of wedge^6(U (x) C^p), as a dict subset -> coeff."""
    out = {}
    for js in itertools.product(range(p_dim), repeat=N):
        idx = [i * p_dim + js[i] for i in range(N)]
        coeff = 1
        for i in range(N):
            coeff = coeff * a[js[i]] % P
        if coeff == 0:
            continue
        key = tuple(sorted(idx))
        out[key] = (out.get(key, 0) + perm_sign(idx) * coeff) % P
    return out


def wedge(f, g):
    out = {}
    for k1, c1 in f.items():
        for k2, c2 in g.items():
            if set(k1) & set(k2):
                continue
            seq = list(k1) + list(k2)
            key = tuple(sorted(seq))
            out[key] = (out.get(key, 0) + perm_sign(seq) * c1 * c2) % P
    return out


def act(gen_a, gen_b, form, p_dim):
    """derivation by X = E_ab - E_ba on U, extended to wedge powers of U (x) C^p."""
    out = {}
    for key, c in form.items():
        for pos, idx in enumerate(key):
            i, j = divmod(idx, p_dim)
            if i == gen_b:
                new, sg = gen_a * p_dim + j, 1
            elif i == gen_a:
                new, sg = gen_b * p_dim + j, -1
            else:
                continue
            seq = list(key)
            seq[pos] = new
            if len(set(seq)) < len(seq):
                continue
            k2 = tuple(sorted(seq))
            out[k2] = (out.get(k2, 0) + sg * perm_sign(seq) * c) % P
    return out


def to_rows(forms, basis):
    return [[f.get(b, 0) for b in basis] for f in forms]


def quaternion_matrix(x, y, z, w):
    # d = x + y u + z v + w uv in M_2(F_p), u = diag(s,-s), v = [[0,-1],[1,0]], uv = [[0,-s],[-s,0]]
    return [[(x + y * S) % P, (-z - w * S) % P], [(z - w * S) % P, (x - y * S) % P]]


def main():
    # ---- one factor (A itself), degree 2: the Hodge classes of degree 2 (divisor classes, Lefschetz (1,1))
    b2 = list(itertools.combinations(range(2 * N), 2))
    rows2 = []
    for b in b2:
        img = {}
        for g in range(N - 1):
            for k, c in act(g, g + 1, {b: 1}, 2).items():
                img[(g, k)] = c
        rows2.append(img)
    k2 = sorted({k for img in rows2 for k in img})
    M2 = [[img.get(k, 0) for k in k2] for img in rows2]
    ker2_upper = len(b2) - rank_mod_p(M2)
    print('A, degree 2: so(6)-invariants (upper bound from F_p):', ker2_upper)
    assert ker2_upper == 1

    # ---- one factor (A itself): wedge^6 (U (x) C^2), dimension 924
    basis = list(itertools.combinations(range(2 * N), N))
    assert len(basis) == 924
    # invariants of so(6): kernel of the adjacent generators X_{i,i+1} (they generate so(6) as a Lie algebra)
    cols = []
    for b in basis:
        img = {}
        for g in range(N - 1):
            for k, c in act(g, g + 1, {b: 1}, 2).items():
                img[(g, k)] = c
        cols.append(img)
    keys = sorted({k for img in cols for k in img})
    kpos = {k: i for i, k in enumerate(keys)}
    A = np.zeros((len(keys), len(basis)), dtype=np.int64)
    for j, img in enumerate(cols):
        for k, c in img.items():
            A[kpos[k], j] = c
    rk = rank_mod_p(A.T.tolist())  # rank of the map
    ker_upper = len(basis) - rk
    print('A, degree 6: so(6)-invariants (upper bound from F_p):', ker_upper)

    # explicit invariants: omega^3 (O(6)-invariant) and det(U (x) a)
    omega = {}
    for i in range(N):
        omega[(2 * i, 2 * i + 1)] = 1
    om3 = wedge(wedge(omega, omega), omega)
    dets = [det_vector([random.randrange(P), random.randrange(P)], 2) for _ in range(10)]
    for f in [om3] + dets:
        for g in range(N - 1):
            assert not any(act(g, g + 1, f, 2).values()), 'not invariant'
    r_all = rank_mod_p(to_rows([om3] + dets, basis))
    r_det = rank_mod_p(to_rows(dets, basis))
    weil = [det_vector([1, 0], 2), det_vector([0, 1], 2)]
    r_ring = rank_mod_p(to_rows([om3] + weil, basis))
    # D-translates: d^* acts on C^2 by the transpose of d's matrix; e_sigma -> (column of d^T)
    trans = []
    for _ in range(10):
        d = quaternion_matrix(*[random.randrange(-5, 6) for _ in range(4)])
        for e in ([1, 0], [0, 1]):
            a = [(d[0][0] * e[0] + d[1][0] * e[1]) % P, (d[0][1] * e[0] + d[1][1] * e[1]) % P]
            trans.append(det_vector(a, 2))
    r_trans = rank_mod_p(to_rows(trans, basis))
    print('A, degree 6: rank of {omega^3, det(U(x)a)} =', r_all, '; det-type part =', r_det)
    print('A, degree 6: ring of divisors and W_K alone reaches', r_ring, 'dimensions')
    print('A, degree 6: D-translates of W_K span', r_trans, 'dimensions')
    assert ker_upper == 8 and r_all == 8 and r_det == 7 and r_ring == 3 and r_trans == 7

    # ---- A^2: det-type part of wedge^6 (U (x) C^4); coordinates: functions [6] -> [4] (sign fixed per index)
    def vec(a):
        out = []
        for js in itertools.product(range(4), repeat=N):
            c = 1
            for j in js:
                c = c * a[j] % P
            out.append(c)
        return out

    proj = [vec(a) for a in ([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])]
    per_factor = []
    for _ in range(10):
        d = quaternion_matrix(*[random.randrange(-5, 6) for _ in range(4)])
        for e in ([1, 0], [0, 1]):
            a = [(d[0][0] * e[0] + d[1][0] * e[1]) % P, (d[0][1] * e[0] + d[1][1] * e[1]) % P]
            per_factor.append(vec(a + [0, 0]))
            per_factor.append(vec([0, 0] + a))
    homs = []
    for _ in range(120):
        d1 = quaternion_matrix(*[random.randrange(-5, 6) for _ in range(4)])
        d2 = quaternion_matrix(*[random.randrange(-5, 6) for _ in range(4)])
        for e in ([1, 0], [0, 1]):
            a1 = [(d1[0][0] * e[0] + d1[1][0] * e[1]) % P, (d1[0][1] * e[0] + d1[1][1] * e[1]) % P]
            a2 = [(d2[0][0] * e[0] + d2[1][0] * e[1]) % P, (d2[0][1] * e[0] + d2[1][1] * e[1]) % P]
            homs.append(vec(a1 + a2))
    r_proj, r_pf, r_hom = rank_mod_p(proj), rank_mod_p(per_factor), rank_mod_p(homs)
    print('A^2, degree 6, det-type part (dimension of Sym^6 C^4 = 84):')
    print('  projection pull-backs of W_K:', r_proj, '; with D-translates on each factor:', r_pf,
          '; pull-backs along x -> d1 x1 + d2 x2:', r_hom)
    assert (r_proj, r_pf, r_hom) == (2 * 2, 14, 84)
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
