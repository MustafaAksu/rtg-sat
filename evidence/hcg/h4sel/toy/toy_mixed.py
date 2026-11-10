"""Claude: independent check of ChatGPT's toy mixed-tree obstruction (generic_engine only).
Tuple (s1,s1,...,s6,s6) for toy roots (v1=v2, v3=v4, v5=v6 -> 3 distinct lines, each 4 consecutive points).
Operators Nhat_e = T_e^{ord C} - 1 from actual twists, all 54 proper cuts; H0 per triangle; all 16796 trees."""
import sys, json, itertools
from functools import lru_cache
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
def Kc(p): return (F(p[0]),F(p[1]))
V=[[Kc(c) for c in v] for v in json.load(open('/home/claude/g34/h4sel/rankobs/toy_cg_roots.json'))['generating_reflection_roots']]
n=3; NP=12
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
S_=[refl(v) for v in V]; gs=[]
for s in S_: gs+=[s,s]
LS=Local(gs); H=LS.comp; dH=len(H)
print('dim H =',dH,' S rank =',rank([[LS.S(x,y) for y in H] for x in H]))
Bmat=[list(c) for c in zip(*(H+LS.B1))]
def to_H(coords): return solve(Bmat,coords)[:dH]
def prod(a,b):
    M=eye(n)
    for p in range(a,b+1): M=mm(M,gs[p-1])
    return M
def order(M):
    P=M
    for k in range(1,100):
        if P==eye(n): return k
        P=mm(P,M)
def Nhat(a,b):
    d=order(prod(a,b)); cols=[]
    for x in H:
        v=LS.values(x); tw=LS.twist_cocycle(v,a-1,b-1,d)
        img=to_H(LS.coords(tw)); cols.append([sub(img[i],x_) for i,x_ in enumerate([ONE if i==j else Z for i in range(dH)])] if False else None)
        cols[-1]=img
    T=[[cols[j][i] for j in range(dH)] for i in range(dH)]
    N=msub(T,eye(dH))
    assert all(isz(x) for r in mm(N,N) for x in r)
    return N,d
diags=[(u,v) for u in range(NP) for v in range(u+2,NP) if not (u==0 and v==NP-1)]
OPS={}
for (u,v) in diags: OPS[(u,v)]=Nhat(u+1,v)
print('cuts:',len(diags),' ord(C) values:',sorted(set(d for _,d in OPS.values())))
flat={k:[q for row in N for x in row for q in (x[0],x[1])] for k,(N,d) in OPS.items()}
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
print('Q-span of all 54 cut operators:',qrank(list(flat.values())))
# joint image dim
cols=[[N[i][j] for i in range(dH)] for (N,d) in OPS.values() for j in range(dH)]
print('dim_K of joint image of all 54:',rank(cols))
def c(M): return rank(msub(eye(n),M))
H0={}
for i,j,k in itertools.combinations(range(NP),3):
    A=prod(i+1,j); B=prod(j+1,k)
    fix=n-rank(msub(eye(n),A)+msub(eye(n),B))
    H0[(i,j,k)]=(c(A)+c(B)+c(mm(A,B))-2*n+2*fix)==0
print('H0-valid triangles:',sum(H0.values()),'of',len(H0))
def trees(i,k):
    if k-i<2: return [[]]
    out=[]
    for j in range(i+1,k):
        if not H0[(i,j,k)]: continue
        for L in trees(i,j):
            for R in trees(j,k):
                out.append(L+R+([(i,j)] if j-i>=2 else [])+([(j,k)] if k-j>=2 else []))
    return out
T=trees(0,NP-1)
print('H0-valid trees:',len(T))
hist={}; best=[]
for t in T:
    assert len(t)==9
    r=qrank([flat[d] for d in t]); hist[r]=hist.get(r,0)+1
    if r>=6 and len(best)<3: best.append(t)
print('exact Q-rank histogram:',dict(sorted(hist.items())))
print('example max-rank trees (intervals):',[[(u+1,v) for u,v in t] for t in best])
json.dump({'hist':hist},open('/home/claude/g34/h4sel/toy/toy_mixed_hist.json','w'))
