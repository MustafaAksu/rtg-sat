"""Claude: regenerate the 756 minimal vectors (orbit of a root under the 10 W5 reflections) and the 126 lines;
count fixed points of each reflection on vectors and lines (ChatGPT's 270/243 and 46/40); orders of s_1 s over all
other reflections (rank-2 classes available as 'one point in place of two reflections')."""
import json, sys
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
from fractions import Fraction as Fr
roots=[[(Fr(c[0]),Fr(c[1])) for c in x] for x in json.load(open('/home/claude/g34/roots_alt_5.json'))['generating_reflection_roots']]
def refl(v):
    f=mul((Fr(-2),Fr(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(6)] for i in range(6)]
S=[refl(v) for v in roots]
orb={tuple(roots[0]):roots[0]}; fr=[roots[0]]
while fr:
    nf=[]
    for x in fr:
        for s in S:
            y=mv(s,x); k=tuple(y)
            if k not in orb: orb[k]=y; nf.append(y)
    fr=nf
V=list(orb.values()); print('orbit of v1 under <s_1..s_10>:',len(V))
lines={}
for x in V:
    j=next(i for i,c in enumerate(x) if not isz(c)); f=inv(x[j]); lines[tuple(mul(f,c) for c in x)]=x
L=list(lines.values()); print('lines:',len(L))
for v in roots[:3]:
    fv=sum(1 for x in V if isz(h(x,v))); fl=sum(1 for x in L if isz(h(x,v)) or rank([x,v])==1)
    print(f'reflection: fixed vectors {fv} (2-cycles {(756-fv)//2}); fixed lines {fl} (2-cycles {(126-fl)//2})')
print('genus of 756-cover with 20 reflections: 2g-2 =',-2*756+20*243,'-> g =',(-2*756+20*243+2)//2)
print('genus of 126-cover: g =',(-2*126+20*40+2)//2)
def order(M):
    R=eye(6)
    for k in range(1,50):
        R=mm(R,M)
        if R==eye(6): return k
orders={}
for x in L:
    if rank([x,roots[0]])==1: continue
    o=order(mm(S[0],refl(x))); orders[o]=orders.get(o,0)+1
print('orders of s_1*s over the other 125 reflections:',orders)
