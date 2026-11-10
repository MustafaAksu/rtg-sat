"""Claude: independent checks of two claims in ChatGPT's HCG_OBSTRUCTION_FRAMEWORK_CHATGPT_INDEPENDENT_REVIEW_v0_1 (stdlib).
(1) Closed form D_min(a, t) = max(t, a + ceil(a/(t-1))) for  min sum(delta)  s.t.  sum - max >= a,
    t terms, 1 <= delta_i <= a - 1 (largest eigenspace of a nonscalar A-part has dim >= 1)  -- vs brute force.
(2) b = 26 (S_27 on std, dim 26): every pair {x, y} (x != y; possibly a non-eigenvalue) with
    m_x + m_y >= 52 - 28 = 24 for a permutation of index J >= 9 is {1, -1}; and the index maxima at
    active costs 26, 27, 28 are 13, 2, 14 -- exhaustive over all cycle types.
(3) The two multiplicity bounds used: m_1 = b - J, and for zeta of order q > 1: m_zeta <= floor((b+1)/q), m_zeta <= J/(q-1).
"""
from itertools import combinations_with_replacement
from fractions import Fraction
from collections import Counter
from math import ceil

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

# (1)
bad = []
for a in range(2, 13):
    for t in range(3, 20):
        best = min((sum(d) for d in combinations_with_replacement(range(1, a), t) if sum(d) - max(d) >= a), default=None)
        if best != max(t, a + ceil(a/(t - 1))): bad.append((a, t, best))
print(f'(1) D_min closed form vs brute force, 2 <= a <= 12, 3 <= t <= 19: {"agree" if not bad else bad}')

# (2) + (3)
b = 26; n = b + 1
ZERO, HALF = Fraction(0), Fraction(1, 2)
idxmax = {}
viol = []; bound_viol = []
for lam in partitions(n):
    ev = Counter()
    for l in lam:
        for j in range(l): ev[Fraction(j, l)] += 1
    ev[ZERO] -= 1
    ev = {k: v for k, v in ev.items() if v > 0}
    J = n - len(lam)
    # (3) bounds
    if ev.get(ZERO, 0) != b - J: bound_viol.append(('m1', lam))
    for z, m in ev.items():
        if z == 0: continue
        q = z.denominator
        if m > (b + 1)//q or m*(q - 1) > J: bound_viol.append(('mz', lam, z))
    keys = list(ev)
    pairs = [(x, y, ev[x] + ev[y]) for i, x in enumerate(keys) for y in keys[i + 1:]]
    pairs += [(x, None, ev[x]) for x in keys]                 # partner not an eigenvalue
    for x, y, inside in pairs:
        c = 2*b - inside
        idxmax[c] = max(idxmax.get(c, -1), J)
        if J >= 9 and inside >= 24 and {x, y} != {ZERO, HALF}:
            viol.append((lam, x, y, inside, J))
print(f'(2) S_27: pairs with m_x + m_y >= 24 at index J >= 9 other than {{1,-1}}: {len(viol)}')
print(f'    index maxima at active costs 26, 27, 28: {idxmax.get(26)}, {idxmax.get(27)}, {idxmax.get(28)}')
print(f'(3) multiplicity bounds m_1 = b - J, m_z <= floor((b+1)/q), m_z <= J/(q-1): violations {len(bound_viol)}')
assert not bad and not viol and not bound_viol and (idxmax[26], idxmax[27], idxmax[28]) == (13, 2, 14)
print('ALL PASS')
