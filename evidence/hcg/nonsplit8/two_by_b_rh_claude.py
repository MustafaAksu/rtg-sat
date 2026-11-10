"""Claude: factorwise 2 (x) b, the W = S_{b+1} branch, by budget + Riemann-Hurwitz (stdlib only).

Setting (see report): V = A (x) B, dim A = 2, dim B = b, d = 2b, Sum c = 4b + 8 exactly (an identity, not a bound),
N >= 19 effective branches, t >= 3 A-active ones.  Active: c = 2b - dim ker >= b.  Inactive: c = 2 rank(1 - mu B_g), even.
In the W = S_{b+1} case g = A'(g) (x) std(w(g)) with w : Gamma -> S_{b+1} a homomorphism with transitive image, so the
(b+1)-sheeted cover gives  Sum_j ind(w(g_j)) = 2b + 2 g' >= 2b,  ind(w) = (b+1) - #cycles(w).
  active with cost c:   exists x != y (x = alpha^-1, y = beta^-1) with mult_x(std w) + mult_y(std w) = 2b - c;
  inactive with cost c: exists z with mult_z(std w) = b - c/2   (z = mu^-1; mult 0 allowed when z is not an eigenvalue).
For every cost distribution we bound Sum ind by the maximum index compatible with each cost; if the bound is < 2b
for every distribution, the S_{b+1} branch is impossible.
"""
from fractions import Fraction
from collections import Counter
import sys

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

def tables(b):
    n = b + 1
    act, inact = {}, {}            # cost -> max index
    for lam in partitions(n):
        ev = Counter()
        for l in lam:
            for j in range(l): ev[Fraction(j, l)] += 1
        ev[Fraction(0)] -= 1         # std = perm - trivial
        mults = [m for m in ev.values() if m > 0]
        ind = n - len(lam)
        # inside counts for a pair x != y: any two distinct eigenvalue classes, or one class + a non-eigenvalue, or none
        pair_vals = {0} | set(mults) | {mults[i] + mults[j] for i in range(len(mults)) for j in range(i + 1, len(mults))}
        for inside in pair_vals:
            c = 2*b - inside
            act[c] = max(act.get(c, -1), ind)
        for m in {0} | set(mults):
            c = 2*(b - m)
            if c > 0: inact[c] = max(inact.get(c, -1), ind)
    return act, inact

def analyse(b, verbose=True):
    total = 4*b + 8
    act, inact = tables(b)
    survivors = []
    # enumerate: t actives (costs >= b), s = N - t inactives (even costs >= 2), N >= 19, t >= 3
    def comps(k, lo, step, budget):            # multisets of k costs >= lo, nondecreasing, sum <= budget
        def rec(k, lo, budget):
            if k == 0: yield (); return
            c = lo
            while c*k <= budget:
                for rest in rec(k - 1, c, budget - c): yield (c,) + rest
                c += step
        yield from rec(k, lo, budget)
    count = 0
    for t in range(3, 20):
        for s in range(max(0, 19 - t), 60):
            if t*b + 2*s > total: break
            for a_costs in comps(t, b, 1, total - 2*s):
                rest = total - sum(a_costs)
                if rest < 2*s or rest % 2: continue
                for i_costs in comps(s, 2, 2, rest):
                    if sum(i_costs) != rest: continue
                    count += 1
                    if any(c not in act for c in a_costs) or any(c not in inact for c in i_costs):
                        continue                   # cost not realisable at all in the S_{b+1} model
                    bound = sum(act[c] for c in a_costs) + sum(inact[c] for c in i_costs)
                    if bound >= 2*b:
                        survivors.append((t, s, a_costs, Counter(i_costs), bound))
    if verbose:
        print(f'b = {b}: d = {2*b}, Sum c = {total}; distributions enumerated: {count}; RH needs Sum ind >= {2*b}')
        print(f'   max index by active cost  {dict(sorted((c, act[c]) for c in act if c <= b + 4))}')
        print(f'   max index by inactive cost {dict(sorted((c, inact[c]) for c in inact if c <= 8))}')
        print(f'   distributions surviving RH: {len(survivors)}', survivors[:6])
    return survivors

def parity_tables(b):
    """For each active cost: max index over options whose eigenvalue pair is {1,-1} (then det A' = -1) and over all other
    options ('free': det A' unconstrained here).  For each inactive cost: whether mu != 1 is possible (det A' = mu^2 free)."""
    n = b + 1
    pm, free, inact_mu_free = {}, {}, {}
    for lam in partitions(n):
        ev = Counter()
        for l in lam:
            for j in range(l): ev[Fraction(j, l)] += 1
        ev[Fraction(0)] -= 1
        ev = {k: v for k, v in ev.items() if v > 0}
        ind = n - len(lam)
        keys = list(ev)
        pairs = [(keys[i], keys[j]) for i in range(len(keys)) for j in range(i + 1, len(keys))]
        opts = [(ev[x] + ev[y], {x, y} == {Fraction(0), Fraction(1, 2)}) for x, y in pairs]
        opts += [(ev[x], False) for x in keys] + [(0, False)]          # pair containing a non-eigenvalue: det free
        for inside, is_pm in opts:
            c = 2*b - inside
            tab = pm if is_pm else free
            tab[c] = max(tab.get(c, -1), ind)
        for z, m in ev.items():
            if z != 0: inact_mu_free[2*(b - m)] = True
    return pm, free, inact_mu_free

def analyse_parity(b, survivors):
    pm, free, mu_free = parity_tables(b)
    left = []
    for (t, s, a_costs, i_costs, bound) in survivors:
        if any(mu_free.get(c, False) for c in i_costs):            # an inactive with mu != 1: no parity constraint
            left.append((a_costs, dict(i_costs), 'inactive mu free')); continue
        inact_ind = bound - sum(max(pm.get(c, -1), free.get(c, -1)) for c in a_costs)
        need = 2*b - inact_ind
        all_pm = sum(pm.get(c, -10**6) for c in a_costs)
        ok_all_pm = all_pm >= need and t % 2 == 0                    # all {1,-1}: det product (-1)^t must be 1
        ok_some_free = any(free.get(a_costs[i], -10**6) + sum(max(pm.get(c, -1), free.get(c, -1))
                           for j, c in enumerate(a_costs) if j != i) >= need for i in range(t))
        if ok_all_pm or ok_some_free: left.append((a_costs, dict(i_costs), 'parity does not decide'))
    print(f'   after the determinant-parity filter: {len(left)} left', left)
    return left

if __name__ == '__main__':
    out, par = {}, {}
    for b in (24, 25, 26):
        out[b] = analyse(b)
        par[b] = analyse_parity(b, out[b])
    assert out[25] == []
    assert par[24] == [] and par[26] == []
    print('RESULT: b = 25 (d = 50): no cost distribution is compatible with Riemann-Hurwitz -> S_26 branch of 2 x 25 impossible')
    print('        b = 24 (d = 48): RH leaves only (24,24,24)+2^16; determinant parity removes it (ChatGPT\'s proof)')
    print('        b = 26 (d = 52): RH leaves 3 distributions; determinant parity removes all -> S_27 branch of 2 x 26 impossible')
