"""Claude: Lemma T' (Euler characteristic / Katz counting) for factorwise A (x) B, a = dim A (stdlib only).

Normalise lifts of the A-parts: inactive (A-scalar) branches -> I, actives -> scalar multiples chosen freely, except one
active that absorbs the product scalar.  This is a genuine rank-a local system on P^1 minus the t active points; it is
irreducible because the projective A-image is.  For such a system  dim H^1_par = sum_s rank(1 - A_s) - 2a >= 0.
Choosing optimal scalars (largest eigenspace -> eigenvalue 1) on all actives but the one with the largest
delta_i = a - m_i:   sum_i delta_i - max_i delta_i >= a      (Lemma T had only sum_i delta_i >= a).
Costs: active c >= b*delta_i, inactive c >= max(a, 2) (and >= 2), N >= 19, t >= 3, Sum c = 2ab + 8.
Special cases: a = 3, t = 3, all delta = 1 gives 2 < 3: the three-pseudoreflection lemma; for the std factor of
S_{b+1} the same count is Riemann-Hurwitz (rank(1 - std w) = ind w).
"""
from itertools import combinations_with_replacement

def min_cost_exact(a, b, prime=True):
    # exhaustive over t in 3..19 and delta_i in [1, a-1] (largest eigenspace of a nonscalar A-part has dim >= 1)
    best = None
    for t in range(3, 20):
        for deltas in combinations_with_replacement(range(1, a), t):
            D = sum(deltas)
            if (D - max(deltas) >= a) if prime else (D >= a):
                cost = b*D + max(19 - t, 0)*max(a, 2)
                if best is None or cost < best[0]: best = (cost, t, deltas)
    return best

print(' a | Lemma T: min b (d)  | Lemma T\': min b (d)  | witness (t, deltas) at the T\' minimum')
rows = {}
for a in range(2, 11):
    def first_b(prime):
        for b in range(a, 400):
            c = min_cost_exact(a, b, prime)
            if c and c[0] <= 2*a*b + 8: return b, c
    bT, _ = first_b(False); bP, wP = first_b(True)
    rows[a] = (bT, bP)
    print(f'{a:2d} | {bT:4d} ({a*bT:4d})          | {bP:4d} ({a*bP:4d})           | t = {wP[1]}, deltas = {wP[2]}')
surv = sorted((a*b, a, b) for a in range(2, 12) for b in range(a, 60) if a*b <= 100
              and min_cost_exact(a, b, True)[0] <= 2*a*b + 8 and not (a == 3 and 14 <= b <= 18))
print('factorwise shapes with d <= 100 surviving Lemma T\' (and the 3 x b lemma):')
print('  ', [(d, f'{a}x{b}') for d, a, b in surv])
assert rows[3][1] == 19 and rows[4][1] == 16
assert min_cost_exact(4, 13, True)[0] > 2*4*13 + 8         # 4 x 13 excluded without Riemann-Hurwitz
assert min_cost_exact(3, 14, True)[0] > 2*3*14 + 8         # reproduces the three-pseudoreflection exclusion at 3 x 14
print('checks: 4 x 13, 4 x 14, 4 x 15 excluded by T\' directly; 3 x 14..18 reproduced; ALL PASS')
