"""Claude: independent terminal sieve for moving-rank 3 and 4 elements, and the d = 25 local age budget (stdlib only).
Setting: finite-order g in GL_d(K), K = Q(sqrt-3), in a group with NO element of age <= 1 (no junior elements at all;
reflection-free). Eigenvalues != 1 of g: a multiset of roots of unity, stable under Gal(Kbar/K), of size c = rank(1-g).
Condition: for every k with g^k != 1: age(g^k) > 1  (this also covers inverses, g^{-1} = g^{ord-1}).
Representation: eigenvalue exp(2 pi i e/M), e in Z/M, M = 360 (all roots of unity of degree <= 4 over K have order | 360).
Gal(Q(zeta_M)/K) = {k in (Z/M)^x : k = 1 mod 3}. Multisets are unions of Galois orbits (with multiplicity).
(1) rank 3: expect ChatGPT's five spectra. (2) rank 4: list all surviving spectra.
(3) d = 25 pattern (3^18, 4): enumerate type counts with sum_j age(g_j) = d + 4 = 29 (balanced Chevalley-Weil, sig (4,4)).
    Note det(g) = exp(2 pi i age(g)), so the product-one determinant condition is implied by an integral age sum."""
from fractions import Fraction as F
from math import gcd
from itertools import combinations_with_replacement
M=360
G=[k for k in range(1,M) if gcd(k,M)==1 and k%3==1]
orbits=[]; seen=set()
for e in range(1,M):
    if e in seen: continue
    o=sorted({(k*e)%M for k in G}); seen.update(o); orbits.append(tuple(o))
def age(ms): return sum(F(e,M) for e in ms if e%M)
def order(ms):
    o=1
    for e in ms: o=o*(M//gcd(e,M))//gcd(o,M//gcd(e,M))
    return o
def spectra(c):
    small=[o for o in orbits if len(o)<=c]
    out=set()
    for r in range(1,c+1):
        for combo in combinations_with_replacement(range(len(small)),r):
            ms=[]
            for i in combo: ms+=list(small[i])
            if len(ms)==c: out.add(tuple(sorted(ms)))
    return sorted(out)
def terminal(ms):
    n=order(ms)
    for k in range(1,n):
        p=[(k*e)%M for e in ms]
        if all(x==0 for x in p): continue
        if age(p)<=1: return False
    return True
def show(ms):
    names={180:'-1',120:'w',240:'wb',60:'z6',300:'z6b',90:'i',270:'-i'}
    return '('+','.join(names.get(e,f'e^{F(e,M)}') for e in ms)+')'
res={}
for c in (3,4):
    cand=spectra(c); good=[ms for ms in cand if terminal(ms)]
    res[c]=good
    print(f'rank {c}: {len(cand)} K-Galois-stable spectra, {len(good)} terminal:')
    for ms in good: print(f'   {show(ms):34s} order {order(ms):3d}  age {age(ms)}  age(inv) {age([(-e)%M for e in ms])}')
assert len(res[3])==5
# (3) d=25 budget
a3=[age(ms) for ms in res[3]]; a4=sorted({age(ms) for ms in res[4]})
sols=[]
def rec(i,left,acc,counts):
    if i==len(a3)-1:
        counts=counts+[left]; tot=acc+left*a3[i]
        for b in a4:
            if tot+b==29: sols.append((tuple(counts),b))
        return
    for n in range(left+1): rec(i+1,left-n,acc+n*a3[i],counts+[n])
rec(0,18,F(0),[])
print(f'(3) d=25: rank-3 types {[str(x) for x in a3]}, rank-4 ages {[str(x) for x in a4]}')
print(f'   solutions (n per rank-3 type, rank-4 age) with sum age = 29: {len(sols)}')
from collections import Counter
print('   rank-4 ages used:',dict(Counter(str(b) for _,b in sols)))
print('   sample:',[(c,str(b)) for c,b in sols[:5]])
print('ALL PASS')
