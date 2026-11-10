"""Claude: G34-BLOCK-01 — all 170 cut operators Nhat=T^{ord C}-1 from actual twists (generic_engine), Q-rank,
H0 per triangle, cup form, and pickle of operators for the tree search."""
import sys,json,itertools,pickle
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
J=json.load(open('G34_BLOCK_01_roots.json'))
P10=[[ (F(a),F(b)) for a,b in v] for v in J['generating_reflection_roots']]
n=6
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
gs=[]
for v in P10: s=refl(v); gs+=[s,s]
P=eye(n)
for g in gs: P=mm(P,g)
print('product one:',P==eye(n),'; tuple length',len(gs))
LS=Local(gs); H=LS.comp; dH=len(H)
G=[[LS.S(x,y) for y in H] for x in H]
print('dim H =',dH,'; S rank =',rank(G))
Bmat=[list(c) for c in zip(*(H+LS.B1))]
def to_H(c): return solve(Bmat,c)[:dH]
def prod(a,b):
    M=eye(n)
    for p in range(a,b+1): M=mm(M,gs[p-1])
    return M
def order(M):
    Q=M
    for k in range(1,200):
        if Q==eye(n): return k
        Q=mm(Q,M)
diags=[(u,v) for u in range(20) for v in range(u+2,20) if not (u==0 and v==19)]
OPS={}
for (u,v) in diags:
    d=order(prod(u+1,v)); cols=[]
    for x in H:
        cols.append(to_H(LS.coords(LS.twist_cocycle(LS.values(x),u,v-1,d))))
    T=[[cols[j][i] for j in range(dH)] for i in range(dH)]
    N=msub(T,eye(dH)); assert all(isz(x) for r in mm(N,N) for x in r)
    OPS[(u,v)]=(N,d)
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
print('cuts:',len(diags),'; nonzero:',sum(1 for k in flat if any(x!=0 for x in flat[k])),'; Q-rank all:',qrank(list(flat.values())))
def c(M): return rank(msub(eye(n),M))
H0={}
for i,j,k in itertools.combinations(range(20),3):
    A=prod(i+1,j); B=prod(j+1,k); fix=n-rank(msub(eye(n),A)+msub(eye(n),B))
    H0[(i,j,k)]=(c(A)+c(B)+c(mm(A,B))-2*n+2*fix)==0
print('H0-valid triangles:',sum(H0.values()),'of',len(H0))
pickle.dump({'flat':flat,'H0':H0,'diags':diags,'OPS':{k:([[ (str(x[0]),str(x[1])) for x in r] for r in N],d) for k,(N,d) in OPS.items()}},open('block_ops.pkl','wb'))
