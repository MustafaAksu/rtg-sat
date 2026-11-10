"""H4 edge-form predictor (HCG-HYP-EDGEFORM). For a paired tuple (s1,s1,...,s10,s10) with roots v_1..v_10 and an
interval pants decomposition containing the 10 pair curves (so every curve encloses whole pairs; all k_j=1):
  L = {t in K^10 : sum t_i v_i = 0}            (sigma-part of H_1 of the dual graph; dim_K 4 if roots span K^6)
  beta_e(t,t') = h( sum_{i in sub(e)} t_i v_i , sum_{i in sub(e)} t'_i v_i )   restricted to L
Predicted H4 rank = dim_Q span{beta_e} in Herm(L) (<= 16). Uses only roots + curve list; no monodromy, no cocycles."""
import json, sys
from fractions import Fraction as F
Z=(F(0),F(0)); ONE=(F(1),F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): a,b=x;c,e=y; return (a*c-b*e,a*e+b*c-b*e)
def conj(x): return (x[0]-x[1],-x[1])
def inv(x): n=x[0]*x[0]-x[0]*x[1]+x[1]*x[1]; c=conj(x); return (c[0]/n,c[1]/n)
def isz(x): return x[0]==0 and x[1]==0
def h(x,y):
    s=Z
    for a,b in zip(x,y): s=add(s,mul(a,conj(b)))
    return s
def nullspace(M,n):            # right nullspace over K of rows M (each length n)
    M=[r[:] for r in M]; piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,len(M)) if not isz(M[i][c])),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; iv=inv(M[r][c]); M[r]=[mul(iv,x) for x in M[r]]
        for i in range(len(M)):
            if i!=r and not isz(M[i][c]):
                f=M[i][c]; M[i]=[sub(a,mul(f,b)) for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]; basis=[]
    for fc in free:
        v=[Z]*n; v[fc]=ONE
        for i,pc in enumerate(piv): v[pc]=sub(Z,M[i][fc])
        basis.append(v)
    return basis
def qrank(rows):
    import flint
    return flint.fmpq_mat([[flint.fmpq(x.numerator,x.denominator) for x in r] for r in rows]).rank() if rows else 0
def predict(roots, curves):
    V=[[ (F(str(a)),F(str(b))) for a,b in v] for v in roots]
    L=nullspace([[V[i][k] for i in range(10)] for k in range(6)],10)
    rows=[]; ranks=[]
    for (a,b) in curves:
        assert a%2==1 and b%2==0, 'curve must enclose whole pairs'
        S=list(range((a-1)//2,b//2))
        X=[[ (lambda t: [ (lambda k: __import__('functools').reduce(add,[mul(t[i],V[i][k]) for i in S],Z))(k) for k in range(6)])(t) ] for t in L]
        X=[x[0] for x in X]
        B=[[h(X[p],X[q]) for q in range(len(L))] for p in range(len(L))]
        coords=[B[p][p][0] for p in range(len(L))]
        for p in range(len(L)):
            for q in range(p+1,len(L)): coords+= [B[p][q][0],B[p][q][1]]
        rows.append(coords)
        ranks.append(len(L)-len(nullspace(B,len(L))))
    return len(L), qrank(rows), ranks
def beta_rows(roots,curves):
    V=[[ (F(str(a)),F(str(b))) for a,b in v] for v in roots]
    L=nullspace([[V[i][k] for i in range(10)] for k in range(6)],10); rows=[]
    for (a,b) in curves:
        S=list(range((a-1)//2,b//2))
        X=[[__import__('functools').reduce(add,[mul(t[i],V[i][k]) for i in S],Z) for k in range(6)] for t in L]
        B=[[h(X[p],X[q]) for q in range(len(L))] for p in range(len(L))]
        c=[B[p][p][0] for p in range(len(L))]
        for p in range(len(L)):
            for q in range(p+1,len(L)): c+=[B[p][q][0],B[p][q][1]]
        rows.append(c)
    return rows
COMB=[(2*i-1,2*i) for i in range(1,11)]+[(1,2*k) for k in range(2,9)]
BAL=[(2*i-1,2*i) for i in range(1,11)]+[(1,4),(5,8),(9,12),(13,16),(1,8),(9,16),(1,16)]
if __name__=='__main__':
    roots=json.load(open(sys.argv[1]))['generating_reflection_roots']
    for name,cv in (('comb',COMB),('balanced',BAL)):
        dL,r,rk=predict(roots,cv); print(f'{sys.argv[1]} {name}: dimK L={dL} predicted Q-rank={r} per-curve K-ranks={rk}')
