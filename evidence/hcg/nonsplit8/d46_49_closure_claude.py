"""Claude: closure of every branch at d = 46, 47, 48, 49 (stdlib only).

Inherited CHECKED inputs as in d44_45_closure_claude.py, plus three Claude PROPOSED lemmas of this round:
  Lemma B' (two_block_quadratic_claude.py): S_{r+1} two-block branch closed for 13 <= r <= 29 (blocks not K-defined).
  Lemma T  (common eigenvector): factorwise A (x) B, a = dim A.  For the active elements (A_g not scalar) let m_g be the
           largest eigenspace dimension of A_g and D = sum (a - m_g).  If D <= a - 1 the largest eigenspaces meet in a
           nonzero v, Cv is invariant under the projective A-image (inactive elements are scalar on A), so V is reducible.
           Hence D >= a.  Costs: active c >= b (a - m_g), inactive c >= max(a, 2); t >= 3 actives (noncyclic image).
           Lower bound: min_{t >= 3} [ b * max(a, t) + max(19 - t, 0) * max(a, 2) ]  <=  2ab + 8 is necessary.
  Lemma 2x24: the budget-tight factorwise 2 (x) 24 at d = 48 (see report section 5); cycle-type facts checked below.
"""
def E(k, r): return 2*r + 2*k*k - 21*k + 8
def R(q, r): return r - (r + 1)//q
def is_prime_power(n):
    if n < 2: return False
    for p in range(2, n + 1):
        if n % p == 0:
            while n % p == 0: n //= p
            return n == 1
def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

def lemmaT_min(a, b):
    return min(b*max(a, t) + max(19 - t, 0)*max(a, 2) for t in range(3, 40))
def old_min(a, b): return 3*b + 16*max(a, 2)

def two_block_closed(r):   # Lemma B' + reflection branch + finer systems (non-K-defined blocks)
    e = 2*r - 26
    ok = 2*(R(3, r) - 1) > e and R(3, r) + R(2, r) > e and 17 > e/2
    finer = [(2*kp, r//kp) for kp in range(2, r) if r % kp == 0 and r//kp >= 6]
    return ok and all(E(k, rr) < 0 for k, rr in finer)

# min moving rank over noncentral classes of the field-compatible candidates (gap/d46_48_screen_out.txt, d49_screen_out.txt)
CAND = {46: [('L2(47) discrete series, 3 rational chars', 'Q', 24)],
        47: [('L2(47) Steinberg', 'Q', 24)],
        48: [('A9', 'Q', 20), ('2.A8', 'Q', 24), ('2.S6(2)', 'Q', 24), ('3.U3(5) (6 chars)', 'K', 24)],
        49: [('L2(49) Steinberg', 'Q', 24)]}

print('(0) Lemma T vs the old factorwise budget: smallest b allowed for each a (b >= a)')
for a in range(2, 11):
    bo = next(b for b in range(a, 200) if old_min(a, b) <= 2*a*b + 8)
    bn = next(b for b in range(a, 200) if lemmaT_min(a, b) <= 2*a*b + 8)
    print(f'    a={a:2d}: old needs b>={bo:3d} (d>={a*bo:3d});  Lemma T needs b>={bn:3d} (d>={a*bn:3d})')
surv = sorted((a*b, a, b) for a in range(2, 31) for b in range(a, 31) if a*b <= 60 and lemmaT_min(a, b) <= 2*a*b + 8
              and not (a == 3 and 14 <= b <= 18))
print('    factorwise shapes with d <= 60 surviving Lemma T and the 3 x b lemma:', surv)

opens = {}
for d in (46, 47, 48, 49):
    bud = 2*d + 8; issues = []
    print(f'=== d = {d}, Sum c = {bud} ===')
    for k in range(2, d + 1):
        if d % k: continue
        r = d//k
        if r < 6:
            continue
        if k >= 3:
            st = 'excluded (A\', E_k = %d)' % E(k, r) if E(k, r) < 0 else 'OPEN'
        else:
            st = 'excluded (two-block, Lemma B\')' if (two_block_closed(r) and d < 50) else 'OPEN'
        print(f'  imprimitive (k,r)=({k},{r}): {st}')
        if st == 'OPEN': issues.append(f'imprimitive ({k},{r})')
    print(f'  block size r < 6: field-free period bound;  isotypic scalar kernel: r <= {d//10} < 6')
    for a in range(2, d + 1):
        if d % a or a*a > d: continue
        b = d//a
        if a == b:
            print(f'  {a} x {b}: square -- tensor-induced (d < 256) or factorwise:', end=' ')
        if a == 3 and 14 <= b <= 18: st = 'excluded (3 x b lemma, CHECKED)'
        elif old_min(a, b) > bud: st = f'excluded (budget {old_min(a, b)} > {bud})'
        elif lemmaT_min(a, b) > bud: st = f'excluded (Lemma T {lemmaT_min(a, b)} > {bud})'
        elif (a, b) == (2, 24): st = 'budget-tight (104 = 104): excluded by Lemma 2x24 (PROPOSED)'
        else: st = 'OPEN'
        print(f'  factorwise {a} x {b}: {st}')
        if st == 'OPEN': issues.append(f'tensor {a}x{b}')
    print(f'  K-imprimitive: {"excluded (d < 50)" if d < 50 else "OPEN"};  tensor-induced: d < 256')
    sols = sorted({(q, f) for q in range(2, 4*d) if is_prime_power(q) for f, deg in
                   (('q', q), ('q+1', q + 1), ('q-1', q - 1), ('(q+1)/2', (q + 1)/2 if q % 2 else -1),
                    ('(q-1)/2', (q - 1)/2 if q % 2 else -1)) if deg == d})
    print(f'  generic SL2(q) degree solutions: {sols};  A_{d+1} natural: Lemma F')
    thrSD = 2*((bud - 2*((d + 1)//2))//17); thrK = 2*(bud//19)
    for nm, fld, mc in CAND[d]:
        thr = thrSD if fld == 'Q' else thrK
        assert mc > thr
        print(f'    {nm:42s} field {fld}: min c = {mc} > {thr}: excluded (Lemma C)')
    opens[d] = issues
    print(f'  OPEN: {issues if issues else "none"}')

# Lemma 2x24 bookkeeping: N = 19, t = 3, active c = 24, inactive c = 2 forced
a, b, bud = 2, 24, 104
best = min((b*t + 2*(N - t), N, t) for t in range(3, 19) for N in range(19, 40))
assert best == (104, 19, 3)
assert all(not (b*t + 2*(N - t) <= bud) or (N, t) == (19, 3) for t in range(3, 19) for N in range(19, 40))
# cycle-type facts in S_25 acting on std (dim 24)
n = 25
two_or_less = []
for lam in partitions(n):
    ev = set()
    for l in lam:
        for j in range(l): ev.add(j/l)          # eigenvalue exp(2 pi i j/l) as a fraction
    cyc = len(lam)
    std_ev = set(ev) if cyc >= 2 else set(ev) - {0}
    if len(std_ev) <= 2: two_or_less.append(lam)
    # mu * std(w) is a pseudoreflection only for mu = 1 and w a transposition
    for q in range(1, n + 1):
        mult = (cyc - 1) if q == 1 else sum(1 for l in lam if l % q == 0)
        if 24 - mult == 1: assert q == 1 and sorted(lam) == [1]*23 + [2], (lam, q)
assert all(max(lam) <= 2 for lam in two_or_less)
print('(2x24) budget forces (N, t) = (19, 3), active c = 24, inactive c = 2; in S_25: std(w) has <= 2 eigenvalues iff w^2 = 1;')
print('       mu*std(w) is a pseudoreflection iff mu = 1 and w is a transposition.')
assert opens == {46: [], 47: [], 48: [], 49: []}
print('RESULT: every branch closes at d = 46, 47, 48, 49 (with Lemmas B\', T, 2x24 PROPOSED)')
