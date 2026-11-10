"""Claude: closure of every branch at d = 50, 51, 52 (stdlib only).

Inputs: inherited CHECKED lemmas (A', B, C, E, F, S, period bound, 3 x b, symplectic type, tensor-induced d >= 256),
this round's CHECKED-by-two items (Lemma B', Lemma T, 2 x 24, nonsplit => d >= 50) and Claude PROPOSED items:
  K-imprimitive corollary (ChatGPT): Lemma E + bound L  =>  K-defined imprimitive needs d >= 2L (L = 46: 92; L = 50: 100).
  2 x b, W = S_{b+1}: budget + Riemann-Hurwitz (+ determinant parity) -- two_by_b_rh_claude.py (b = 25, 26).
  4 x 13: Lemma T equality forces actives = (pseudoreflection on A) (x) scalar, inactives = I (x) pseudoreflection;
          W_B = S_14 (or monomial/decomposable, excluded); Riemann-Hurwitz on the 14-sheeted cover: 15 < 26.
"""
import json, sys
from pathlib import Path
def E(k, r): return 2*r + 2*k*k - 21*k + 8
def R(q, r): return r - (r + 1)//q
def bprime(r):
    e = 2*r - 26
    finer = [(2*kp, r//kp) for kp in range(2, r) if r % kp == 0 and r//kp >= 6]
    return 2*(R(3, r) - 1) > e and R(3, r) + R(2, r) > e and 17 > e/2 and all(E(k, rr) < 0 for k, rr in finer)
def lemmaT_min(a, b): return min(b*max(a, t) + max(19 - t, 0)*max(a, 2) for t in range(3, 40))

L_checked = 50
KIMP = 2*L_checked
cand = json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv) > 1 else {}

# 4 x 13 bookkeeping
a, b, tot = 4, 13, 2*52 + 8
sols = [(t, N, D) for t in range(3, 20) for N in range(19, 40) for D in range(max(a, t), 4*t + 1)
        if b*D + a*(N - t) <= tot]
assert sols == [(4, 19, 4)], sols                       # t = 4 actives, each codim 1 (D = 4), 15 inactives
# active: dim ker = 52 - 13 = 39 = 3*m_{alpha^-1}(B) + m_{beta^-1}(B) with m <= 13  =>  B_g scalar
assert [(x, y) for x in range(14) for y in range(14) if 3*x + y == 39 and x + y <= 13] == [(13, 0)]
# inactive: c = 4 * rank  = 4 => rank 1 on B; S_14 std: mu std(w) pseudoreflection iff mu = 1 and w a transposition
assert 15*1 + 4*0 < 2*14 - 2
print(f'(4x13) forced: t = 4, N = 19, actives (pseudoreflection on A) x scalar on B, 15 inactives I x pseudoreflection;')
print(f'       W_B = S_14: Riemann-Hurwitz on 14 sheets needs Sum ind >= 26, available 15*1 + 4*0 = 15  -> excluded')

opens = {}
for d in (50, 51, 52):
    bud = 2*d + 8; issues = []
    print(f'=== d = {d}, Sum c = {bud} ===')
    print(f'  K-defined imprimitive: needs d >= {KIMP} (Lemma E + nonsplit => d >= {L_checked})  -> excluded')
    for k in range(2, d + 1):
        if d % k: continue
        r = d//k
        if r < 6: continue
        if k == 2: st = 'excluded (Lemma B\', non-K-defined)' if bprime(r) else 'OPEN'
        else: st = f'excluded (A\', E_k = {E(k, r)})' if E(k, r) < 0 else 'OPEN'
        print(f'  imprimitive (k,r)=({k},{r}): {st}')
        if st == 'OPEN': issues.append(f'({k},{r})')
    print(f'  block size < 6: period bound; isotypic scalar kernel: r <= {d//10} < 6')
    for a in range(2, d + 1):
        if d % a or a*a > d: continue
        b = d//a
        if a == 3 and 14 <= b <= 18: st = 'excluded (3 x b lemma)'
        elif 3*b + 16*max(a, 2) > bud: st = 'excluded (budget)'
        elif lemmaT_min(a, b) > bud: st = f'excluded (Lemma T {lemmaT_min(a, b)} > {bud})'
        elif (a, b) == (2, 25): st = 'excluded (W-structure + Riemann-Hurwitz, two_by_b_rh)'
        elif (a, b) == (2, 26): st = 'excluded (W-structure + Riemann-Hurwitz + det parity, two_by_b_rh)'
        elif (a, b) == (4, 13): st = 'excluded (Lemma T equality + Riemann-Hurwitz, above)'
        else: st = 'OPEN'
        print(f'  factorwise {a} x {b}: {st}')
        if st == 'OPEN': issues.append(f'{a}x{b}')
    print('  tensor-induced: d < 256;  symplectic type: never;  A_{d+1} natural: Lemma F')
    def ppow(n):
        if n < 2: return False
        p = next(p for p in range(2, n + 1) if n % p == 0)
        while n % p == 0: n //= p
        return n == 1
    gen = sorted((q, f) for q in range(2, 4*d) if ppow(q) for f, deg in
                 (('q', q), ('q+1', q + 1), ('q-1', q - 1), ('(q+1)/2', (q + 1)/2 if q % 2 else -1),
                  ('(q-1)/2', (q - 1)/2 if q % 2 else -1)) if deg == d)
    print(f'  generic SL2(q) degree solutions: {gen}')
    thrSD = 2*((bud - 2*((d + 1)//2))//17); thrK = 2*(bud//19)
    rows = cand.get(str(d))
    if rows is None:
        issues.append('primitive screen missing')
    else:
        for nm, fld, mc in rows:
            thr = thrSD if fld == 'Q' else thrK
            assert mc > thr, (d, nm, mc, thr)
            print(f'    {nm:34s} field {fld}: min c = {mc} > {thr}  -> excluded (Lemma C)')
    opens[d] = issues
    print(f'  OPEN: {issues if issues else "none"}')
print('RESULT:', 'every branch closes at d = 50, 51, 52' if all(not v for v in opens.values()) else opens)
