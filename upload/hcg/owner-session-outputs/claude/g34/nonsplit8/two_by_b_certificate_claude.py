"""Claude: finite certificate scan for factorwise 2 (x) b in the W = S_{b+1} branch, b = 24..B (stdlib only).

Uniform reduction (ChatGPT framework note section 4; re-derived): exactly t = 3 actives; every inactive has A' = I
(mu != 1 would cost >= b - 1 > budget), so an inactive with permutation w costs exactly 2 ind(w); s = N - 3 >= 16.
Active i: A'(g_i) nonscalar with eigenvalues (x^-1, y^-1); cost c = 2b - (mult_x + mult_y) on std(w_i).
Gates applied to every candidate (c_1, c_2, c_3; inactive total):
  budget   : Sum c = 4b + 8 exactly, inactive part even and >= 2*16;
  RH       : Sum_all ind = 2b + 2g' (>= 2b and EVEN), w transitive (contains S_{b+1});
  dihedral : two actives with pair {1,-1} (order-2 reflections) generate A'(Gamma) as a dihedral group -> real character
             -> chi_V real -> field Q != K;  (subsumes the all-three determinant parity)
  euler    : dim H^1_par(P^1, A') = sum rank(1 - A'_i) - 4 >= 0 for the irreducible rank-2 A' with three singular
             points, so the three actives cannot all have eigenvalue 1 (all reflections).
Type of an active option, most permissive available: 'gen' (1 not an A'-eigenvalue), 'refl' (A' has eigenvalue 1,
not the pair {1,-1}), 'pm' (pair {1,-1}).  Eigenvalues not occurring in std(w) are free and chosen permissively.
"""
from fractions import Fraction
from collections import Counter, defaultdict
import sys, time

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

ORDER = {'gen': 0, 'refl': 1, 'pm': 2}          # permissiveness: lower is better
ZERO, HALF = Fraction(0), Fraction(1, 2)

def active_options(b, min_inside):
    """(cost, type) -> [max even index, max odd index] over cycle types of S_{b+1}."""
    n = b + 1
    tab = defaultdict(lambda: [-1, -1])
    for lam in partitions(n):
        ev = Counter()
        for l in lam:
            for j in range(l): ev[Fraction(j, l)] += 1
        ev[ZERO] -= 1
        ev = {k: v for k, v in ev.items() if v > 0}
        ind = n - len(lam)
        items = sorted(ev.items(), key=lambda kv: -kv[1])
        opts = {}
        def put(inside, typ):
            if inside < min_inside: return
            if inside not in opts or ORDER[typ] < ORDER[opts[inside]]: opts[inside] = typ
        for i, (x, mx) in enumerate(items):
            if mx + (items[0][1] if i else (items[1][1] if len(items) > 1 else 0)) < min_inside and mx < min_inside:
                break
            # x plus a free non-eigenvalue y: 'gen' unless x = 1 (then 'refl', or 'pm' only)
            put(mx, 'refl' if x == ZERO else 'gen')
            for y, my in items[i + 1:]:
                if mx + my < min_inside: break
                pr = {x, y}
                typ = 'pm' if pr == {ZERO, HALF} else ('refl' if ZERO in pr else 'gen')
                put(mx + my, typ)
        for inside, typ in opts.items():
            c = 2*b - inside
            slot = tab[(c, typ)]
            slot[ind % 2] = max(slot[ind % 2], ind)
    return tab

def scan(b):
    total = 4*b + 8
    cmax = total - 32 - 2*b                      # other two actives >= b each, inactives >= 32
    tab = active_options(b, 2*b - cmax)
    keys = sorted(tab)
    surv = []
    for i1 in range(len(keys)):
        for i2 in range(i1, len(keys)):
            for i3 in range(i2, len(keys)):
                ks = (keys[i1], keys[i2], keys[i3])
                csum = sum(k[0] for k in ks)
                if csum > total - 32 or (total - csum) % 2: continue
                types = [k[1] for k in ks]
                if sum(t == 'pm' for t in types) >= 2: continue                 # dihedral
                if all(t in ('pm', 'refl') for t in types): continue            # Euler characteristic
                I_in = (total - csum)//2
                need = 2*b - I_in
                ok = False
                for p1 in (0, 1):
                    for p2 in (0, 1):
                        for p3 in (0, 1):
                            m = [tab[ks[0]][p1], tab[ks[1]][p2], tab[ks[2]][p3]]
                            if min(m) < 0: continue
                            if sum(m) >= need and (sum(m) + I_in) % 2 == 0: ok = True
                if ok: surv.append((tuple(k[0] for k in ks), tuple(types), I_in))
    return surv

if __name__ == '__main__':
    B = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    first_open = None
    for b in range(24, B + 1):
        t0 = time.time()
        s = scan(b)
        print(f'b = {b:2d} (d = {2*b}): surviving active-cost/type patterns: {len(s)}'
              + (f'   e.g. {s[:3]}' if s else '') + f'   [{time.time() - t0:.1f}s]', flush=True)
        if s and first_open is None: first_open = b
    print('RESULT: S_{b+1} branch of 2 x b closed by budget + RH(parity) + dihedral + Euler for every b in 24..'
          + (str(B) if first_open is None else f'{first_open - 1}; first surviving pattern at b = {first_open}'))
