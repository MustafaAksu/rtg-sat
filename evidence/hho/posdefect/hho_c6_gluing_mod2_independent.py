"""Independent C6 p=2 gluing-sector test using only F2 cochain ranks.

Does NOT use the Gram matrix, Hermitian determinant, Claude's Python code,
or the HCG engine. Verifies the sector-length result on three geometric covers.
All linear algebra uses Python integer bit vectors over F2.

Algebraic rationale: C6=<t>, R=Z2[omega], a=t^2, s=t^3.
The nontrivial C3 block idempotent modulo 2 is E=t^2+t^4.
The chi_1 idempotent on that R[C2] block is e_-=(1-s)/2.
For the saturated chi_1 lattice L, multiplication by 2 induces
    e_- M / L  ~= im(1-s : E(M/2M) -> E(M/2M)).
Thus length_R(A_chi_1) = (1/2) rank_F2((1-s)E | H^1(C,F2)).
The F2 rank is even because E(M/2M) is an F4-module.
"""
from math import gcd


def echelon(vectors):
    pivots = {}
    for value in vectors:
        x = value
        while x:
            k = x.bit_length() - 1
            if k in pivots:
                x ^= pivots[k]
            else:
                pivots[k] = x
                break
    return pivots


def kernel(rows, columns):
    mat = rows[:]
    pivots = []
    rank = 0
    for c in range(columns):
        target = next((j for j in range(rank, len(mat)) if mat[j] & (1 << c)), None)
        if target is None:
            continue
        mat[rank], mat[target] = mat[target], mat[rank]
        for j in range(len(mat)):
            if j != rank and mat[j] & (1 << c):
                mat[j] ^= mat[rank]
        pivots.append(c)
        rank += 1
        if rank == len(mat):
            break
    free = [c for c in range(columns) if c not in pivots]
    out = []
    for c in free:
        v = 1 << c
        for j, p in enumerate(pivots):
            if mat[j] & (1 << c):
                v |= 1 << p
        assert all((v & row).bit_count() % 2 == 0 for row in rows)
        out.append(v)
    return out


def cyclic_shift(v, exponent):
    k = exponent % 6
    return (((v << k) | (v >> (6 - k))) & 63) if k else v


def check_cover(exponents):
    assert sum(exponents) % 6 == 0
    assert gcd(6, *exponents) == 1
    N = len(exponents)
    blocks, dictionaries, offsets = [], [], []
    total = 0
    for e in exponents:
        # Integral regular-permutation monodromy has primitive image (t^e-1)Z^6.
        # Its reduction modulo 2 is the image of t^e-1 on F2^6.
        basis = list(echelon([cyclic_shift(1 << a, e) ^ (1 << a)
                              for a in range(6)]).values())
        dictionary = {0: 0}
        for j, element in enumerate(basis):
            dictionary.update({v ^ element: bits | (1 << j)
                               for v, bits in list(dictionary.items())})
        assert len(dictionary) == (1 << len(basis))
        offsets.append(total)
        total += len(basis)
        blocks.append(basis)
        dictionaries.append(dictionary)

    # Right-action DW cocycle closure: sum_i v_i t^(e_{i+1}+...+e_N)=0.
    closure_columns = [cyclic_shift(v, sum(exponents[i + 1:]))
                       for i in range(N) for v in blocks[i]]
    closure_rows = [sum(((col >> a) & 1) << j
                        for j, col in enumerate(closure_columns)) for a in range(6)]
    Z = kernel(closure_rows, total)

    def encode(vectors):
        return sum(dictionaries[i][v] << offsets[i] for i, v in enumerate(vectors))

    Eg = [encode([cyclic_shift(1 << a, e) ^ (1 << a) for e in exponents])
          for a in range(6)]
    assert all(all((row & e).bit_count() % 2 == 0 for row in closure_rows)
               for e in Eg)
    eg_rank = len(echelon(Eg))
    two_g = 2 - 12 + sum(6 - gcd(6, e) for e in exponents)
    assert len(Z) - eg_rank == two_g

    def deck(z, k):
        out = 0
        for i, basis in enumerate(blocks):
            bits = (z >> offsets[i]) & ((1 << len(basis)) - 1)
            local = 0
            for j, v in enumerate(basis):
                if bits & (1 << j):
                    local ^= v
            out |= dictionaries[i][cyclic_shift(local, k)] << offsets[i]
        return out

    for z in Z + Eg:
        assert deck(z, 6) == z
        assert all((row & deck(z, 1)).bit_count() % 2 == 0
                   for row in closure_rows)
    assert len(echelon(Eg + [deck(x, 1) for x in Eg])) == eg_rank

    # Mod 2: e_nontrivial_C3 = t^2+t^4; (1-s)=(1+t^3).
    # Product = t+t^2+t^4+t^5, all as F2-linear maps on cocycles.
    images = [deck(z, 1) ^ deck(z, 2) ^ deck(z, 4) ^ deck(z, 5)
              for z in Z]
    rank_paired = len(echelon(Eg + images)) - eg_rank
    assert rank_paired % 2 == 0  # naturally linear over F4
    sector_length = rank_paired // 2
    chi1 = -2 + sum(e % 6 != 0 for e in exponents)
    chi4 = -2 + sum((4 * e) % 6 != 0 for e in exponents)
    return two_g, chi1, chi4, rank_paired, sector_length


CASES = {
    "separator": [2]*5 + [3] + [4]*3 + [5],
    "leaf_A": [3]*8 + [1, 5],
    "leaf_B": [3]*8 + [2, 4],
}

if __name__ == "__main__":
    expected = {"separator": 7, "leaf_A": 0, "leaf_B": 0}
    for label, exps in CASES.items():
        two_g, chi1, chi4, r2, length = check_cover(exps)
        assert length == expected[label]
        print(f"{label}: 2g={two_g}, m(chi1)={chi1}, m(chi4)={chi4}; "
              f"rank_F2((1-s)e_C3)={r2}, length_R(A_chi1)={length} PASS")
    print("ALL PASS: 7, 0, 0; independent F2 cochain/representation test")
