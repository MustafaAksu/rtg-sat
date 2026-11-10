"""Claude: NEW02 (1) independent recomputation of ChatGPT's projected-span prefilter (45 unprojected pair cuts vs
170 projected cuts); (2) H0 per triangle of the 20-gon; (3) search over H0-valid triangulations for Q-rank 16 of the
projected forms (laminar reduction: H0 + H4 suffice). Search uses mod-p ranks; any hit is re-verified exactly here
and must then be certified by operator reconstruction (separate script)."""
import sys, json, random, itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 20261023)
NAME=sys.argv[2] if len(sys.argv)>2 else 'NEW02'
def Kc(p): return (F(p[0]),F(p[1]))
V=[[Kc(c) for c in v] for v in json.load(open(f'/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT/{NAME}_roots.json'))['generating_reflection_roots']]
n=6; m=10
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
S_=[refl(v) for v in V]
g=[None]+[S_[(p-1)//2] for p in range(1,21)]       # g[1..20]
A=[[V[i][r] for i in range(m)] for r in range(n)]
Lb=nullspace(A,m); d=len(Lb)
print(NAME,'dim L =',d)
def prod(a,b):
    M=eye(n)
    for p in range(a,b+1): M=mm(M,g[p])
    return M
def order(M):
    P=M
    for k in range(1,100):
        if P==eye(n): return k
        P=mm(P,M)
def proj_fix(C,k):
    P=[[Z]*n for _ in range(n)]; Cj=eye(n)
    for j in range(k): P=[[add(a,b) for a,b in zip(r,s)] for r,s in zip(P,Cj)]; Cj=mm(Cj,C)
    return [[mul((F(1,k),F(0)),x) for x in r] for r in P]
def form(a,b,project=True):   # interval of positions a..b (1-based)
    C=prod(a,b); k=order(C); P=proj_fix(C,k) if project else eye(n)
    J=[i for i in range(m) if a<=2*i+1 and 2*i+2<=b]
    Fl=[]
    for t in Lb:
        f=[Z]*n
        for i in J: f=vadd(f,vsc(t[i],V[i]))
        Fl.append(mv(P,f))
    kk=(F(k),F(0)) if project else ONE
    M=[[mul(kk,h(Fl[p],Fl[q])) for q in range(d)] for p in range(d)]
    coords=[M[i][i][0] for i in range(d)]
    for i in range(d):
        for j in range(i+1,d): coords+= [M[i][j][0],M[i][j][1]]
    assert all(M[i][i][1]==0 for i in range(d))
    return coords
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
# diagonals (u,v) 0<=u<v<=19 non-adjacent, (u,v)!=(0,19) ; interval positions [u+1, v]
diags=[(u,v) for u in range(20) for v in range(u+2,20) if not (u==0 and v==19)]
FORM={dg:form(dg[0]+1,dg[1]) for dg in diags}
pairaligned=[(u,v) for (u,v) in diags if u%2==0 and v%2==0]
print('cuts:',len(diags),' pair-aligned:',len(pairaligned))
print('Q-rank unprojected pair-aligned cuts:',qrank([form(u+1,v,False) for (u,v) in pairaligned]))
print('Q-rank projected, all cuts:',qrank(list(FORM.values())))
# H0 per triangle (i<j<k vertices): A=prod(i+1..j), B=prod(j+1..k)
def c(M): return rank(msub(eye(n),M))
H0={}
for i,j,k in itertools.combinations(range(20),3):
    Am=prod(i+1,j); Bm=prod(j+1,k)
    fix=n-rank(msub(eye(n),Am)+msub(eye(n),Bm))
    H0[(i,j,k)]=(c(Am)+c(Bm)+c(mm(Am,Bm))-2*n+2*fix)==0
print('H0-valid triangles:',sum(H0.values()),'of',len(H0))
# count H0-valid triangulations by DP
from functools import lru_cache
@lru_cache(None)
def cnt(i,k):
    if k-i<2: return 1
    return sum(cnt(i,j)*cnt(j,k) for j in range(i+1,k) if H0[(i,j,k)])
print('H0-valid triangulations of the 20-gon:',cnt(0,19))
def sample(i,k):  # uniform random H0-valid triangulation of polygon i..k
    if k-i<2: return []
    ws=[(j,cnt(i,j)*cnt(j,k)) for j in range(i+1,k) if H0[(i,j,k)]]
    tot=sum(w for _,w in ws); r=random.randrange(tot)
    for j,w in ws:
        if r<w: break
        r-=w
    out=[]
    if j-i>=2: out.append((i,j))
    if k-j>=2: out.append((j,k))
    return out+sample(i,j)+sample(j,k)
P_=2**61-1
FMOD={dg:[ (x.numerator*pow(x.denominator,-1,P_))%P_ for x in FORM[dg]] for dg in diags}
def rmod(rows):
    M=[r[:] for r in rows]; rk=0
    for col in range(16):
        p=next((i for i in range(rk,len(M)) if M[i][col]),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]; iv=pow(M[rk][col],-1,P_)
        for i in range(len(M)):
            if i!=rk and M[i][col]:
                f=M[i][col]*iv%P_; M[i]=[(x-f*y)%P_ for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk
best=0; hist={}; hits=[]
NS=int(sys.argv[3]) if len(sys.argv)>3 else 20000
for s in range(NS):
    T=sample(0,19); assert len(T)==17
    r=rmod([FMOD[dg] for dg in T]); hist[r]=hist.get(r,0)+1
    if r==16 and len(hits)<5: hits.append(sorted(T))
print('rank histogram over',NS,'uniform H0-valid triangulations:',dict(sorted(hist.items())))
for T in hits:
    ex=qrank([FORM[dg] for dg in T])
    print('HIT intervals:',[(u+1,v) for u,v in T],' exact Q-rank',ex)
json.dump({'name':NAME,'hits':[[(u+1,v) for u,v in T] for T in hits],'hist':hist},open(f'/home/claude/g34/h4sel/new02/{NAME}_search.json','w'))
