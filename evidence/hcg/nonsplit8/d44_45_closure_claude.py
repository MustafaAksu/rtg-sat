"""Claude: arithmetic closure of every branch at d = 44, 45 (and where it first fails, d = 46).  stdlib only.
Inherited (CHECKED) inputs, used as stated:
  * Sum c_j = 2d + 8 over N >= 19 effective branches; noncentral effective c >= 3 (Theorem R + GT12 Cor 1.6 / centre in mu_6),
    A_{d+1}-standard excluded for every d by Lemma F.
  * C-imprimitive (Lemma A'): Galois-stable system of shape (k, r), r >= 6, gamma = 0; K-imprimitive needs d >= 50.
      k >= 3: need E_k(r) = 2r + 2k^2 - 21k + 8 >= 0.
      k = 2: two-block lemma, E <= 2r - 26; scalar psi costs >= 2(T_r - 1), T_r = r - floor((r+1)/2)  (Lemma B: strict >);
             reflection branch needs 17 > E/2; finer W_R systems (2k', r/k') need E_{2k'}(r/k') < 0.
      isotypic kernel: scalar => k >= 10 => r <= d/10 < 6; else factorwise tensor.
  * Factorwise tensor a x b (a <= b): need 2ab + 8 >= 3b + 16 max(a, 2); the 3 x b lemma kills 14 <= b <= 18.
  * Tensor-induced needs d >= 256.  Symplectic type impossible for every d.
  * Almost quasisimple socle L (irreducible), character field of chi|L inside K:
      self-dual (rational): Lemma S needs 2 ceil(d/2) + 51 <= 2d + 8; then c_min <= floor((2d+8-2ceil(d/2))/17),
      non-self-dual (field K): c_min <= floor((2d+8)/19);  Lemma C needs a noncentral h in L with c(h) <= 2 c_min.
"""
def E(k, r): return 2*r + 2*k*k - 21*k + 8
def T(r): return r - (r + 1)//2
def ceil2(d): return (d + 1)//2

# min moving rank over noncentral classes, from gap/d44_45_screen_out.txt (CTblLib 1.3.7 + generic SL2 tables)
CAND = {
    44: [('A11', 'Q', 14), ('U5(2)', 'Q', 16), ('M11', 'Q', 20), ('L2(43)', 'Q', 22), ('SL2(43)', 'Q', 30)],
    45: [('A11', 'Q', 16), ('M11', 'Q', 24), ('M12', 'Q', 20), ('U4(2)', 'K', 24)],
}
open_items = {}
for d in (44, 45, 46):
    bud = 2*d + 8
    issues = []
    print(f'=== d = {d}, Sum c = {bud} ===')
    # imprimitive
    for k in range(2, d + 1):
        if d % k: continue
        r = d//k
        if r < 6: continue
        if k >= 3:
            ok = E(k, r) < 0
            print(f'  imprimitive (k,r)=({k},{r}): E_k = {E(k, r)} -> {"excluded" if ok else "OPEN"}')
            if not ok: issues.append(f'imprimitive ({k},{r})')
        else:
            e = 2*r - 26; cost = 2*(T(r) - 1)
            finer = [(2*kp, r//kp, E(2*kp, r//kp)) for kp in range(2, r) if r % kp == 0 and r//kp >= 6]
            okB = cost > e; okR = 17 > e/2; okF = all(f[2] < 0 for f in finer)
            print(f'  two-block r={r}: E<={e}, scalar-psi cost>={cost} (Lemma B {"holds" if okB else "FAILS"}), '
                  f'reflection branch {"closes" if okR else "OPEN"}, finer {finer} {"closed" if okF else "OPEN"}')
            if not (okB and okR and okF): issues.append(f'two-block r={r}' + ('' if okB else ' (Lemma B equality/failure)'))
    print(f'  isotypic scalar kernel: r <= {d//10} < 6 -> excluded')
    # factorwise tensor
    for a in range(2, d + 1):
        if d % a or a*a > d: continue
        b = d//a
        need = 3*b + 16*max(a, 2)
        passes = bud >= need
        killed = (a == 3 and 14 <= b <= 18)
        st = 'excluded (budget)' if not passes else ('excluded (3 x b lemma)' if killed else 'OPEN')
        print(f'  factorwise tensor {a} x {b}: {bud} vs {need} -> {st}')
        if st == 'OPEN': issues.append(f'tensor {a}x{b}')
    print(f'  tensor-induced: d < 256 -> excluded;  K-imprimitive: d < 50 -> {"excluded" if d < 50 else "OPEN"}')
    # Lemma S / Lemma C
    sd_min = 2*ceil2(d) + 51
    sd_ok = sd_min <= bud
    cmin_sd = (bud - 2*ceil2(d))//17
    cmin_k = bud//19
    print(f'  Lemma S: {sd_min} <= {bud}? {sd_ok}; self-dual Lemma C threshold 2*{cmin_sd} = {2*cmin_sd}; '
          f'field-K threshold 2*{cmin_k} = {2*cmin_k}')
    for (nm, fld, mc) in CAND.get(d, []):
        thr = 2*cmin_sd if fld == 'Q' else 2*cmin_k
        assert mc > thr, (d, nm)
        print(f'    {nm:8s} field {fld}: min c = {mc} > {thr} -> excluded by Lemma C')
    if d not in CAND: issues.append('almost-quasisimple candidates not screened')
    print(f'  A_{d+1} natural: Lemma F.  OPEN items: {issues if issues else "none"}')
    open_items[d] = issues
assert open_items[44] == [] and open_items[45] == []
print('RESULT: every branch closes at d = 44 and d = 45; first open items at d = 46:', open_items[46])
