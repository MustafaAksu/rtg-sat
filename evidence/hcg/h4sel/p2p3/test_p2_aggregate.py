"""P2 aggregate claim: im(sum_i N_{pair i}) = ker(tau), dim d (positivity of sum_i h(t_i,t_i) on L_gen)."""
import sys,random,itertools; sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
random.seed(4242)
def creflect(v,zeta):
    n=len(v); hv=h(v,v); f=mul(sub(zeta,ONE),inv(hv))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
def rr(n):
    while True:
        v=[(F(random.randint(-1,1)),F(random.randint(-1,1))) for _ in range(n)]
        if any(not isz(x) for x in v): return v
W=(F(0),F(1)); MW=(F(0),F(-1))
R4=[[Z,neg(ONE),Z],[ONE,Z,Z],[Z,Z,ONE]]
P=[[Z,Z,ONE],[ONE,Z,Z],[Z,ONE,Z]]
cases={'order3':[creflect(rr(3),W) for _ in range(5)],
       'mixed-rank2':[R4,mm(mm(P,R4),adj(P)),mm(creflect(rr(3),W),creflect(rr(3),W)),mm(creflect(rr(3),MW),creflect(rr(3),W)),creflect(rr(3),W)]}
out=[]
for lab,rs in cases.items():
    gs=[]
    for r in rs: gs+=[r,adj(r)]
    LS=Local(gs); n=3; m=len(rs)
    D=sum(len(colspace(msub(r,eye(n)))) for r in rs); d=D-n
    imgs=[]
    for x in LS.comp:
        v=LS.values(x); tot=[Z]*LS.N
        for i in range(m):
            tw=LS.twist_cocycle(v,2*i,2*i+1,1)
            tot=vadd(tot,LS.coords([[sub(p,q) for p,q in zip(s,t)] for s,t in zip(tw,v)]))
        imgs.append(tot)
    # rank modulo coboundaries
    r_im=rank(LS.B1+imgs)-rank(LS.B1)
    # tau of images = 0
    tz=all(isz(c) for y in imgs for i in range(m) for c in vadd(LS.values(y)[2*i],mv(rs[i],LS.values(y)[2*i+1])))
    s=f'[P2-aggregate:{lab}] d={d} rank im(sum N_pair) mod B^1 = {r_im}; tau(im)=0: {tz}; claim holds: {r_im==d and tz}'
    print(s); out.append(s)
open('test_p2_aggregate_out.txt','w').write('\n'.join(out)+'\n')
