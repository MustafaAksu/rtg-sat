"""Claude: independent check of ChatGPT's W(A2) reality counterexample, embedded as the A2 plane of K^3 with the
standard form (Gram [[2,-1],[-1,2]] on v1=(1,-1,0), v2=(0,1,-1); the trivial line (1,1,1) adds nothing to H_par).
Checks: dim H, S nondegenerate, ALL interval-curve operators (pair-aligned and mixed) in the fixed marking and after
random pure braids: Q-rank <= 3 = d(d+1)/2 < d^2 = 4; S takes rational values on rational cocycles."""
import sys,random,itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
exec(open('/home/claude/g34/h4sel/braidescape/replay_braid.py').read().split("def act")[1].split("gF,_,lab=")[0].join(["def act",""]))
q=lambda a:(F(a),F(0))
v1=[q(1),q(-1),q(0)]; v2=[q(0),q(1),q(-1)]; v3=[q(1),q(0),q(-1)]
R=[v1,v2,v3,v1]; n=3
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
g0=[]
for v in R: s=refl(v); g0+=[s,s]
def all_ops(gs):
    LS=Local(gs); H=LS.comp; dH=len(H)
    Bm=[list(c) for c in zip(*(H+LS.B1))]
    def toH(c): return solve(Bm,c)[:dH]
    rows=[]; NP=len(gs)
    for u in range(NP):
        for v in range(u+2,NP):
            if u==0 and v==NP-1: continue
            C=eye(n)
            for p in range(u,v): C=mm(C,gs[p])
            d=next(k for k in range(1,50) if functools_pow(C,k)==eye(n))
            cols=[toH(LS.coords(LS.twist_cocycle(LS.values(x),u,v-1,d))) for x in H]
            N=msub([[cols[j][i] for j in range(dH)] for i in range(dH)],eye(dH))
            rows.append([qq for r in N for x in r for qq in (x[0],x[1])])
    G=[[LS.S(x,y) for y in H] for x in H]
    return dH,rank(G),rows,G,LS
def functools_pow(M,k):
    P=eye(len(M))
    for _ in range(k): P=mm(P,M)
    return P
def qrank(rows):
    M=[list(r) for r in rows if any(x!=0 for x in r)]; rk=0
    if not M: return 0
    for c in range(len(M[0])):
        p=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[x-f*y for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk
dH,rS,rows,G,LS=all_ops(g0)
print('dim H =',dH,'; S rank =',rS,'; S entries all rational (b=0) in this rational basis:',all(x[1]==0 for r in G for x in r))
print('all 18 interval-curve operators (pair-aligned + mixed), fixed marking: Q-rank =',qrank(rows),'(d^2 = 4)')
random.seed(24)
mx=0
for trial in range(15):
    w=[]
    for _ in range(6):
        i=random.randrange(1,7); w+=[i,i] if random.random()<.5 else [-i,-i]   # sigma_i^2 is pure
    w2=[]
    for _ in range(3):
        i=random.randrange(1,8); w2+=[i,i]
    g,_,lab=act(g0,None,list(range(8)),w+w2)
    assert lab==list(range(8))
    _,_,rows2,_,_=all_ops(g); r=qrank(rows2); mx=max(mx,r)
print('max Q-rank over all interval curves after 15 random pure braids:',mx)
