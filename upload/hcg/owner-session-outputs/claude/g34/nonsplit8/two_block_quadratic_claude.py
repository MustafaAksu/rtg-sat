"""Claude: two-block lemma, S_{r+1}-standard branch -- 'quadratic' version of Lemma B (Lemma B').  stdlib only.

Setting (CHECKED inputs): V = Ind_Lambda^Gamma(tau_1), U_1, U_2 swapped, blocks not K-defined (d < 50), Y = P^1,
Galois equal rank on the two lifts of a block-preserving point, excess E = p_1 + p_2 + 2 sum_j (rho_j - 1) <= 2r - 26,
W_R(tau_1) = S_{r+1} acting by std, tau_1 = std(w) * psi with psi : Lambda -> C^x (Lemma B: normalizer = W x C^x).

Lemma B' : if psi takes only the values +-1 on the meridians of Y, then psi(Lambda) <= {+-1}, chi_{tau_1} is rational,
the induced character is rational, contradicting the character field K.  So only values of order q >= 3 need excluding.
A meridian value lambda of order q forces rank(1 - lambda*w | std) = r - #{cycles of w of length divisible by q}
>= R_q(r) := r - floor((r+1)/q).  (Checked below by exhaustive enumeration of cycle types.)
Cheapest configurations containing a value of order >= 3 (values multiply to 1, so >= 2 nontrivial points):
  (a) at a lift of a preserving point: Galois equal rank => both lifts rank >= R_3, cost 2(R_3 - 1) (inverse value can sit
      on the other lift at no extra cost);
  (b) at a swap point: cost R_3, plus a second nontrivial point: another swap (>= R_2) or a preserving point (2(R_2 - 1)).
Lemma B' holds when both minima exceed E_max = 2r - 26.
Other branches: reflection presence needs 17 > E/2; finer W_R systems (2k', r/k') with r/k' >= 6 need E_{2k'}(r/k') < 0;
r/k' < 6 is excluded by the field-free period bound; G(m,p,r)/diagonal => monomial; exceptional rank <= 8.
"""
def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

def E(k, r): return 2*r + 2*k*k - 21*k + 8
def R(q, r): return r - (r + 1)//q

# (1) exhaustive check of the rank formula over all cycle types of S_{r+1}, r <= 30
for r in range(2, 31):
    parts = list(partitions(r + 1))
    for q in range(2, r + 2):
        m = min(r - sum(1 for p in lam if p % q == 0) for lam in parts)
        assert m == R(q, r), (r, q, m, R(q, r))
print('(1) min_w rank(1 - lambda w | std) = r - floor((r+1)/q) for ord(lambda) = q: verified over all cycle types, r = 2..30')

# (2) range of Lemma B' and of the whole two-block lemma
print('(2)  r   d  E_max  R2  R3 | old B: 2(R2-1)>E | B\'(a): 2(R3-1)>E  B\'(b): R3+R2>E | refl 17>E/2 | finer systems')
closed = []
for r in range(13, 35):
    e = 2*r - 26; r2 = R(2, r); r3 = R(3, r)
    oldB = 2*(r2 - 1) > e
    a = 2*(r3 - 1) > e
    b = r3 + min(r2, 2*(r2 - 1)) > e
    refl = 17 > e/2
    finer = [(2*kp, r//kp, E(2*kp, r//kp)) for kp in range(2, r) if r % kp == 0 and r//kp >= 6]
    fin_ok = all(f[2] < 0 for f in finer)
    allok = a and b and refl and fin_ok
    if allok: closed.append(r)
    print(f'   {r:2d} {2*r:3d}  {e:3d}   {r2:2d}  {r3:2d} | {str(oldB):5s}           | {str(a):5s}             {str(b):5s}          | {str(refl):5s}       | {finer} {"ok" if fin_ok else "OPEN"}')
print('    two-block (non-K-defined) datum excluded for r in', closed[0], '..', closed[-1], ':', closed == list(range(13, closed[-1] + 1)))
print('    caveat: for d = 2r >= 50 the K-defined (K-imprimitive) two-block case is a separate, still-open branch')

# (3) ChatGPT's r = 23 equality case as a special case
r = 23; e = 2*r - 26
assert R(2, r) == 11 and 2*(R(2, r) - 1) == e == 20       # old Lemma B: equality, not strict
assert R(3, r) == 15 and 2*(R(3, r) - 1) == 28 > e         # order >= 3 at a preserving point: 28 > 20
assert R(3, r) + R(2, r) == 26 > e                          # order >= 3 at a swap point: 26 > 20
assert all(R(q, r) >= 15 for q in range(3, 25))
print('(3) r = 23: values of order >= 3 cost >= min(28, 26) > E = 20; order-2 values give a rational character. CLOSED.')
r = 24; e = 2*r - 26
assert 2*(R(2, r) - 1) == e == 22 and 2*(R(3, r) - 1) == 30 > e and R(3, r) + R(2, r) == 28 > e
print('    r = 24 (d = 48): old Lemma B is again an equality (22 = 22); Lemma B\' closes it (30, 28 > 22).')
print('ALL PASS')
