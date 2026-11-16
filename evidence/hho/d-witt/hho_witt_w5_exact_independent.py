"""Independent exact Q(omega) Witt-tree check for the PR #78 W5 marking.

Only the 10 source certificate root vectors are embedded; no HCG / Claude
numerical engine is imported. Rational arithmetic is exact using Fraction.
The input root list was inspected at HCG hcg-v0.5, reference:
  evidence/hcg/g34/g34_cert_tuple5_balanced.json
This is a graph-Euler check, NOT a dominance or Hodge-theoretic proof.
"""
from fractions import Fraction as F
from functools import lru_cache

ROOTS = [
 [(1,0),(0,1),(1,0),(1,0),(-1,-1),(1,0)],
 [(1,0),(1,0),(0,1),(1,0),(-1,-1),(1,0)],
 [(1,0),(1,0),(-1,-1),(-1,-1),(-1,-1),(1,0)],
 [(1,0),(0,1),(-1,-1),(1,0),(1,0),(1,0)],
 [(1,0),(-1,-1),(-1,-1),(0,1),(-1,-1),(-1,-1)],
 [(0,0),(1,2),(0,0),(2,1),(0,0),(0,0)],
 [(1,0),(0,1),(0,1),(1,0),(1,0),(0,1)],
 [(0,0),(1,2),(-1,1),(0,0),(0,0),(0,0)],
 [(1,0),(0,1),(-1,-1),(-1,-1),(1,0),(0,1)],
 [(1,0),(1,0),(1,0),(-1,-1),(0,1),(1,0)],
]
CERT=[(1,2),(3,4),(5,6),(7,8),(9,10),
      (11,12),(13,14),(15,16),(17,18),(19,20),
      (1,4),(5,8),(9,12),(13,16),(1,8),(9,16),(1,16)]

Z=(F(0),F(0)); O=(F(1),F(0))
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x): return (x[0]-x[1], -x[1])
def inv(x):
    a,b=x; den=a*a-a*b+b*b
    return ( (a-b)/den, (-b)/den )
def ident(): return [[O if i==j else Z for j in range(6)] for i in range(6)]
def mm(A,B):
    ret=[[Z]*6 for _ in range(6)]
    for i in range(6):
        for k in range(6):
            if A[i][k]==Z: continue
            for j in range(6):
                if B[k][j]!=Z: ret[i][j]=add(ret[i][j],mul(A[i][k],B[k][j]))
    return ret

def rank(rows):
    a=[r[:] for r in rows]; piv=0
    for col in range(6):
        idx=next((i for i in range(piv,len(a)) if a[i][col]!=Z),None)
        if idx is None:continue
        a[piv],a[idx]=a[idx],a[piv]
        recip=inv(a[piv][col]);a[piv]=[mul(v,recip) for v in a[piv]]
        for i in range(piv+1,len(a)):
            if a[i][col]!=Z:
                fac=a[i][col]
                for j in range(col,6): a[i][j]=sub(a[i][j],mul(fac,a[piv][j]))
        piv+=1
        if piv==6:break
    return piv

def reflect(v):
    v=[tuple(map(F,x)) for x in v]
    h=Z
    for x in v:h=add(h,mul(x,conj(x)))
    assert h==(F(6),F(0)),h
    c=(F(1,3),F(0))
    return [[sub((O if i==j else Z),mul(c,mul(v[i],conj(v[j]))))
             for j in range(6)] for i in range(6)]

G=[a for v in ROOTS for a in (reflect(v), reflect(v))]
I=ident(); P=I
for g in G:P=mm(P,g)
assert P==I, 'product one not satisfied'

@lru_cache(None)
def product(i,j):
    if i==j:return G[i]
    return mm(product(i,j-1),G[j])

@lru_cache(None)
def inv_dim(i,j):
    a=product(i,j)
    return 6-rank([[sub(a[r][c],I[r][c]) for c in range(6)] for r in range(6)])

@lru_cache(None)
def common_dim(i,k,j):
    a=product(i,k);b=product(k+1,j)
    rows=[[sub(t[r][c],I[r][c]) for c in range(6)]
          for t in (a,b) for r in range(6)]
    return 6-rank(rows)

@lru_cache(None)
def ext(i,j):
    if i==j:return (0,0)
    vals=[]
    for k in range(i,j):
        x,y=ext(i,k),ext(k+1,j)
        c=(inv_dim(i,k) if k>i else 0)+(inv_dim(k+1,j) if j>k+1 else 0)-common_dim(i,k,j)
        vals.append((x[0]+y[0]+c,x[1]+y[1]+c))
    return min(v[0] for v in vals),max(v[1] for v in vals)

nodes=[(0,a-2) if b==20 else (a-1,b-1) for a,b in CERT]+[(0,18)]
assert len(set(nodes))==18
edges=0;verts=0
for i,j in nodes:
    kids=[];k=i
    while k<=j:
        best=k
        for a,b in nodes:
            if a==k and (a,b)!=(i,j) and best<b<=j:best=b
        kids.append((k,best));k=best+1
    assert len(kids)==2, (i,j,kids)
    verts+=common_dim(kids[0][0],kids[0][1],kids[1][1])
    if (i,j)!=(0,18):edges+=inv_dim(i,j)
assert edges-verts==4
assert ext(0,18)==(4,4)
print('W5 EXACT Q(omega) PASS: product-one, roots norm 6, 20 reflections')
print(f'certificate graph sums: edges={edges}, vertices={verts}, w={edges-verts}')
print(f'Catalan(18)=477638700 planar rooted trees: DP minimum/maximum={ext(0,18)}')
print(f'exact invariant dimensions computed: intervals={inv_dim.cache_info().currsize}, vertices={common_dim.cache_info().currsize}')
print('This is graph W0 only; NOT period rank (D)')
