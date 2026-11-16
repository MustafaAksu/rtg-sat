"""Exact combinatorial graph-W0 extrema over ALL labelled trivalent trees.

SESSION mathematical calibration, not a Hodge/period-map engine.
Assumes a connected cyclic C6 cover of P1, nonzero branch exponents,
rank-one character chi1(t)=zeta6, and the admissible-cover graph model.

For a tree T, the chi1-part of H1 of the dual graph has dimension
  d(T) = # internal edges with zero monodromy product
       - # trivalent vertices with all three adjacent monodromies trivial.
This is Euler characteristic of G-invariant graph cochains; the missing
+dim V^G is zero for the nontrivial chi1 character.

Root the unrooted tree at one distinguished branch leaf. Binary partitions
of the remaining leaf set enumerate every trivalent leaf-labelled tree.
Dynamic programming over subsets computes the exact minimum and maximum
without enumerating 2,027,025 trees explicitly. State permutation/root
invariance and internal witness checks are independent controls.
"""
from functools import lru_cache


def graph_bounds(exponents):
    if len(exponents) < 4 or any(not isinstance(x, int) or x % 6 == 0 for x in exponents):
        raise ValueError("At least 4 nonzero branch exponents modulo 6")
    if sum(exponents) % 6:
        raise ValueError("Product one required")

    rest = exponents[1:]
    n = len(rest)
    allmask = (1 << n) - 1
    sums = [0] * (allmask + 1)
    for mask in range(1, allmask + 1):
        low = mask & -mask
        sums[mask] = (sums[mask ^ low] + rest[low.bit_length()-1]) % 6

    @lru_cache(maxsize=None)
    def rec(mask):
        if mask.bit_count() == 1:
            return (0, 0, None, None)
        best_min = 10**9
        best_max = -10**9
        min_pair = max_pair = None
        first = mask & -mask
        part = (mask - 1) & mask
        while part:
            if part & first:  # eliminate double counting of {A, B}
                other = mask ^ part
                a = rec(part)
                b = rec(other)
                # Edges to non-leaf subtrees A/B, then vertex H_v correction.
                contribution = (int(part.bit_count() > 1 and sums[part] == 0)
                                + int(other.bit_count() > 1 and sums[other] == 0)
                                - int(sums[part] == 0 and sums[other] == 0))
                mn = a[0] + b[0] + contribution
                mx = a[1] + b[1] + contribution
                if mn < best_min:
                    best_min, min_pair = mn, (part, other)
                if mx > best_max:
                    best_max, max_pair = mx, (part, other)
            part = (part - 1) & mask
        return best_min, best_max, min_pair, max_pair

    lo, hi, _, _ = rec(allmask)

    def verify_witness(mask, maximum=True):
        if mask.bit_count() == 1:
            return 0, 0, 0
        pair = rec(mask)[3 if maximum else 2]
        x, y = pair
        sx = verify_witness(x, maximum)
        sy = verify_witness(y, maximum)
        edge_count = sx[1] + sy[1]
        vertex_count = sx[2] + sy[2]
        if x.bit_count() > 1 and sums[x] == 0:
            edge_count += 1
        if y.bit_count() > 1 and sums[y] == 0:
            edge_count += 1
        if sums[x] == 0 and sums[y] == 0:
            vertex_count += 1
        score = edge_count - vertex_count
        assert score == rec(mask)[1 if maximum else 0]
        return score, edge_count, vertex_count

    witness_lo = verify_witness(allmask, False)
    witness_hi = verify_witness(allmask, True)
    return lo, hi, witness_lo, witness_hi


def count_trees(leaves):
    answer = 1
    for x in range(2 * leaves - 5, 0, -2):
        answer *= x
    return answer


CASES = {
    "C6 separator [2]": [2]*5 + [3] + [4]*3 + [5],
    "C6 leaf A [1]": [3]*8 + [1, 5],
    "C6 leaf B [1]": [3]*8 + [2, 4],
}

if __name__ == "__main__":
    assert count_trees(10) == 2027025
    for name, exponents in CASES.items():
        lo, hi, wlo, whi = graph_bounds(exponents)
        assert lo == 0
        expected = 3 if "separator" in name else 4
        assert hi == expected
        # The distinguished root leaf is arbitrary. Test all 10 roots.
        for j in range(len(exponents)):
            rotated = exponents[j:] + exponents[:j]
            assert graph_bounds(rotated)[:2] == (lo, hi)
        assert wlo[0] == lo and whi[0] == hi
        print(f"{name}: all {count_trees(10)} labelled trivalent trees; "
              f"W0 min/max = {lo}/{hi}; maximal witness edges={whi[1]}, "
              f"vertices={whi[2]}; all 10 roots PASS")
    # Strict rejected-input control.
    try:
        graph_bounds([1, 1, 1, 1])
    except ValueError:
        print("negative control: product-one violation rejected")
    else:
        raise AssertionError("missing product-one rejection")
    print("ALL PASS — graph Euler/W0 calculation; not a (D) dominance test")
