"""Claude: finite checks accompanying the review of HCG_D15_D24_EXCLUSION_PROPOSED_v0_1.md (standard library only).
(1) Reflection-free imprimitive budget: for k>=2, r>=6, gamma=0, N>=19, every effective c_j>=2, block-moving entries
    c_j >= r*ind, sum ind = 2(k-1): minimum possible sum c_j (optimized over t and over N>=19) vs 2kr+8.
    Expect: feasible iff r+2k >= 17; least d = 26.
(2) Tensor-induced groups V = A^{(x)m}, Gamma <= GL(A)^{(x)m}:S_m (not covered explicitly by 'tensor decomposable'):
    exact minimum of rank(1-g) over noncentral g, for (a,m) with a^m in [15,25]: (2,4)=16, (4,2)=16, (5,2)=25.
    g = (A_1 (x) ... (x) A_m) P_pi. Up to conjugation by GL(A)^{(x)m} only one twist per cycle of pi matters and it is
    diagonalizable, so g acts on the tensor basis as a weighted permutation; fixed dim = #orbits with weight product 1.
    Twists: one diagonal twist per cycle (others identity); exhaustive over mu_6 x mu_6 for a = 2, representative
    twists for a = 4, 5 (the analytic necklace bound in the report covers all twists); plus the analytic base-element bound rank >= d/a (A_i nonscalar).
(3) Age identity sanity: sum_j age(g_j) = d + p for signature (p,q) on data with known signature."""
from fractions import Fraction as F
from itertools import product, permutations
import math
# (1)
print('(1) reflection-free imprimitive budget, gamma = 0')
least=None; mismatch=0
for k in range(2,13):
    for r in range(6,40):
        J=2*(k-1); avail=2*k*r+8
        best=min(r*J+2*(N-t) for t in range(1,J+1) for N in range(max(19,t),60))
        feasible = best<=avail
        if feasible != (r+2*k>=17): mismatch+=1
        if feasible and (least is None or k*r<least): least=k*r
print('   mismatches with r+2k>=17:',mismatch,'; least feasible d =',least)
assert mismatch==0 and least==26
# (2)
print('(2) tensor-induced minimum moving rank of noncentral elements')
mu=[F(i,12) for i in range(12)]          # exponents of exp(2 pi i x)
mu6=[F(i,6) for i in range(6)]
def cycles(p):
    seen=set(); out=[]
    for i in range(len(p)):
        if i in seen: continue
        c=[]; j=i
        while j not in seen: seen.add(j); c.append(j); j=p[j]
        out.append(c)
    return out
def fixed_dim(a,m,pi,tw):            # tw: dict factor-index -> tuple of a exponents (diagonal twist on that factor)
    idx=list(product(range(a),repeat=m)); pos={x:i for i,x in enumerate(idx)}
    # g(e_{i_1..i_m}) = w * e_{j} with j_{pi(s)} = i_s ; weight = product over twisted factors s of tw[s][i_s]
    img=[]; wt=[]
    for x in idx:
        y=[None]*m
        for s in range(m): y[pi[s]]=x[s]
        w=sum((tw[s][x[s]] for s in tw),F(0))%1
        img.append(pos[tuple(y)]); wt.append(w)
    seen=[False]*len(idx); fd=0
    for i in range(len(idx)):
        if seen[i]: continue
        j=i; tot=F(0)
        while not seen[j]: seen[j]=True; tot+=wt[j]; j=img[j]
        if tot%1==0: fd+=1
    return fd
TW={4:[(0,0,0,0),(0,0,0,6),(0,0,6,6),(0,4,8,0),(0,0,0,4),(0,3,6,9),(0,0,4,4),(6,6,6,6)],
    5:[(0,0,0,0,0),(0,0,0,0,6),(0,0,0,4,8),(0,3,6,9,0),(0,0,0,6,6),(0,0,4,4,8)]}
for a,m in [(2,4),(4,2),(5,2)]:
    d=a**m; worst=d
    for pi in permutations(range(m)):
        if list(pi)==list(range(m)): continue
        cyc=cycles(list(pi)); reps=[c[0] for c in cyc]
        if a==2: opts=list(product(mu6,repeat=2))                      # exhaustive over mu_6 x mu_6
        else:    opts=[tuple(F(i,12) for i in v) for v in TW[a]]         # representative twists
        choices=[opts for _ in reps]
        for combo in product(*choices):
            tw={s:combo[i] for i,s in enumerate(reps)}
            fd=fixed_dim(a,m,list(pi),tw)
            worst=min(worst,d-fd)
    base=d//a
    print(f'   a={a} m={m} d={d}: min rank(1-g) over factor-permuting g tested = {worst}; base elements (nonscalar) >= d/a = {base}')
    assert worst>=3 and base>=3
# (3)
print('(3) age identity sum age(g_j) = d + p  (signature (p,q))')
cases=[('W5: 20 reflections of order 2, d=6, sig (4,4)',6,[F(1,2)]*20,4),
       ('C6 control exponents (2^5,3,4^3,5), d=1, sig (4,4)',1,[F(k,6) for k in [2]*5+[3]+[4]*3+[5]],4),
       ('C3 control (1^5,2^5), d=1, sig (4,4)',1,[F(k,3) for k in [1]*5+[2]*5],4),
       ('odd-n control (w,w,w^2,w^2), d=1, sig (1,1)',1,[F(1,3),F(1,3),F(2,3),F(2,3)],1)]
for lab,d,ages,p in cases:
    s=sum(ages); print(f'   {lab}: sum age = {s} ; d+p = {d+p}'); assert s==d+p
# (4) general tensor budgets (PROPOSED remarks in the report)
print('(4) general tensor budgets, N >= 19, sum c_j = 2d+8, reflection-free')
# factorwise V = A (x) B, 2 <= a <= b: >=3 entries nontrivial in PGL(A) with c >= b; every other noncentral entry c >= a (and >= 2)
tdmin=None
for a in range(2,40):
    for b in range(a,400):
        d=a*b; need=3*b+max(a,2)*(19-3)
        if need<=2*d+8:
            if tdmin is None or d<tdmin[0]: tdmin=(d,a,b)
            break
print('   least d admitting a factorwise tensor decomposition:',tdmin)
assert tdmin==(42,3,14)
# tensor-induced A^{(x)m}: >=2 factor-permuting entries with c >= a^(m-1)(a-1)/2, others noncentral c >= min(a^(m-1), perm bound)
tid=None
for a in range(2,40):
    for m in range(2,6):
        d=a**m; perm=a**(m-1)*(a-1)/2; base=a**(m-1); low=min(perm,base)
        need=2*perm+17*max(low,2)
        if need<=2*d+8 and (tid is None or d<tid[0]): tid=(d,a,m)
print('   least d admitting a tensor-induced structure:',tid)
assert tid[0]>=256
print('ALL PASS')
