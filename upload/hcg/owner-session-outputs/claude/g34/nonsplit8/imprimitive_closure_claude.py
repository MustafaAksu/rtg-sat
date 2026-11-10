"""Claude: arithmetic for the corrected k-block lemma (A') and the two-block scalar lemma (B), d <= 42 (stdlib only).
A' route: from any C-system with kernel Lambda, either V|Lambda is isotypic (scalar Lambda, or factorwise tensor via Clifford),
or the Lambda-isotypic decomposition X is a Galois-stable system; K-primitivity makes Galois transitive on X,
so block-preserving effective elements move >= k blocks' worth: c >= k.  Budget: E_k = 2r + 2k^2 - 21k + 8 >= 0 needed.
Field-free inputs: any C-system with r >= 2 has gamma = 0 and r >= 6 (r = 1: monomial, excluded)."""
def E(k,r): return 2*r+2*k*k-21*k+8
def T(r): return r-(r+1)//2
print('(1) every Galois-stable system shape (k>=2, r>=6, kr<=42):')
bad=[]
for d in range(26,43):
    for k in range(2,d+1):
        if d%k: continue
        r=d//k
        if r<6: continue
        e=E(k,r)
        if k>=3 and e>=0: bad.append((d,k,r,e))
        if k>=3: print(f'   d={d} (k,r)=({k},{r}) E_k={e}')
assert not bad, bad
print('   all k>=3 shapes with d<=42 have E_k<0')
print('(2) two-block (k=2) lemma, r=13..22: E=2r-26, scalar cost 2(T_r-1), finer systems (2k\',r/k\') with r/k\'>=6:')
for r in range(13,23):
    e=2*r-26; cost=2*(T(r)-1)
    finer=[(2*kp,r//kp,E(2*kp,r//kp)) for kp in range(2,r) if r%kp==0 and r//kp>=6]
    ok_scalar=e<cost; ok_finer=all(x[2]<0 for x in finer); ok_refl=17>e//2
    print(f'   r={r:2d} d={2*r:2d} E<={e:2d} scalar-cost>={cost:2d} scalar-trivial={ok_scalar} finer={finer} '
          f'finer-excluded={ok_finer} reflection-present={ok_refl}')
    assert ok_scalar and ok_finer and ok_refl
print('(3) isotypic case: scalar Lambda needs >=18 block-moving branches, J=2(k-1)>=18 => k>=10 => r<=d/10:',
      'max r for d<=42 =',42//10, '(< 6, excluded)')
print('(4) factorwise tensor shapes a<=b, ab<=42, passing 2ab+8 >= 3b+16*max(a,2):',
      [(a,b) for a in range(2,7) for b in range(a,22) if a*b<=42 and 2*a*b+8>=3*b+16*max(a,2)])
print('ALL PASS')
