"""Claude: determinant-aware refinement of two_by_b_certificate_claude.py (stdlib only, standalone).

Adds the gate  det A'(g_1) det A'(g_2) det A'(g_3) = 1  (inactive A' = I; product one).  For an active option with
eigenvalue pair {x, y} of std(w) (A' eigenvalues x^-1, y^-1): det = (xy)^-1, recorded exactly as an angle in Q/Z
when both x and y are eigenvalues of std(w); if a pair member is a free non-eigenvalue the det is recorded as 'free'.
All (type, det) options are kept (no permissive collapsing), so the gate is exact for determined options.
Other gates as before: budget, RH (>= 2b, even), dihedral (two {1,-1} actives), Euler (all three with eigenvalue 1).
Usage: python3 -I two_by_b_det_claude.py b_min b_max
"""
from fractions import Fraction
from collections import Counter, defaultdict
import sys, time

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

ZERO, HALF = Fraction(0), Fraction(1, 2)
def frac1(q): return q - (q.numerator // q.denominator)

def options(b, min_inside):
    n = b + 1
    tab = defaultdict(lambda: [-1, -1])          # (c, type, det) -> [max even ind, max odd ind]
    for lam in partitions(n):
        ev = Counter()
        for l in lam:
            for j in range(l): ev[Fraction(j, l)] += 1
        ev[ZERO] -= 1
        ev = {k: v for k, v in ev.items() if v > 0}
        ind = n - len(lam)
        items = sorted(ev.items(), key=lambda kv: -kv[1])
        found = set()
        for i, (x, mx) in enumerate(items):
            nxt = items[i + 1][1] if i + 1 < len(items) else 0
            if mx < min_inside and mx + nxt < min_inside:
                break                            # sorted: no later x yields a new option
            if mx >= min_inside:                 # x + a free non-eigenvalue y
                if x == ZERO:
                    found.add((mx, 'refl', 'free'))
                    if HALF not in ev: found.add((mx, 'pm', HALF))
                else:
                    found.add((mx, 'gen', 'free'))
                    if ZERO not in ev and x == HALF: found.add((mx, 'pm', HALF))
            for y, my in items[i + 1:]:
                if mx + my < min_inside: break
                pr = {x, y}
                typ = 'pm' if pr == {ZERO, HALF} else ('refl' if ZERO in pr else 'gen')
                found.add((mx + my, typ, frac1(-(x + y))))
        for inside, typ, det in found:
            slot = tab[(2*b - inside, typ, det)]
            slot[ind % 2] = max(slot[ind % 2], ind)
    return tab

def scan(b):
    total = 4*b + 8
    cmax = total - 32 - 2*b
    tab = options(b, 2*b - cmax)
    keys = sorted(tab, key=lambda k: (k[0], k[1], str(k[2])))
    surv = []
    for i1 in range(len(keys)):
        for i2 in range(i1, len(keys)):
            c12 = keys[i1][0] + keys[i2][0]
            for i3 in range(i2, len(keys)):
                ks = (keys[i1], keys[i2], keys[i3])
                csum = c12 + ks[2][0]
                if csum > total - 32 or (total - csum) % 2: continue
                types = [k[1] for k in ks]
                if sum(t == 'pm' for t in types) >= 2: continue
                if all(t in ('pm', 'refl') for t in types): continue
                dets = [k[2] for k in ks]
                pass
                I_in = (total - csum)//2
                need = 2*b - I_in
                ok = False
                for p1 in (0, 1):
                    for p2 in (0, 1):
                        for p3 in (0, 1):
                            m = [tab[ks[0]][p1], tab[ks[1]][p2], tab[ks[2]][p3]]
                            if min(m) >= 0 and sum(m) >= need and (sum(m) + I_in) % 2 == 0: ok = True
                if ok: surv.append((tuple(k[0] for k in ks), tuple(types), tuple(str(d) for d in dets), I_in))
    return surv

if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for b in range(lo, hi + 1):
        t0 = time.time(); s = scan(b)
        print(f'b = {b} (d = {2*b}): surviving patterns with the determinant gate: {len(s)}'
              + (f'  e.g. {s[:4]}' if s else '') + f'  [{time.time() - t0:.1f}s]', flush=True)
