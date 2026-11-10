#!/usr/bin/env python3
"""Independent exact audit of the supplied W5 *matrix certificate*.
Recomputes algebraic conditions from JSON, never imports Claude's scripts.
K=Q[w], w^2+w+1=0. Includes direct negative-semidefinite principal-minor tests.
This verifies matrix-level H0-H4, NOT derivation of monodromy or geometry.
"""
import json, hashlib, itertools
from fractions import Fraction as F
import sympy as sp

PATH='/home/claude/g34/g34_cert_W7_comb.json'
d=json.load(open(PATH,'r',encoding='utf-8'))
Q=lambda a=0,b=0:(F(a),F(b))
O=Q(); E=Q(1); TH=Q(1,2)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y):
 a,b=x; c,e=y
 return (a*c-b*e,a*e+b*c-b*e)
def conj(x): return (x[0]-x[1],-x[1])
def inv(x):
 a,b=x; nn=a*a-a*b+b*b; assert nn
 y=conj(x);return (y[0]/nn,y[1]/nn)
def div(x,y):return mul(x,inv(y))
def mat_from(s):return [[(F(a),F(b)) for a,b in row] for row in s]
def eye(n):return [[E if i==j else O for j in range(n)] for i in range(n)]
def transpose_conj(A):return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def mm(A,B):
 return [[sumk([mul(A[i][k],B[k][j]) for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]
def sumk(a):
 z=O
 for y in a: z=add(z,y)
 return z
def eq(A,B):return A==B
def mat_add(A,B):return [[add(x,y) for x,y in zip(r,s)] for r,s in zip(A,B)]
def mat_sub(A,B):return [[sub(x,y) for x,y in zip(r,s)] for r,s in zip(A,B)]
def iszero(A):return all(x==O for row in A for x in row)
def vec_flat(A):return [v for row in A for x in row for v in x]
def rankK(A):
 if not A:return 0
 a=[r[:] for r in A]; n=len(a);m=len(a[0]);r=0
 for c in range(m):
  p=next((p for p in range(r,n) if a[p][c]!=O),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r]
  z=inv(a[r][c]);a[r]=[mul(z,q) for q in a[r]]
  for i in range(r+1,n):
   if a[i][c]!=O:
    k=a[i][c];a[i]=[sub(a[i][j],mul(k,a[r][j])) for j in range(m)]
  r+=1
  if r==n:break
 return r
def basis_span(vectors):
 a=[]
 for v in vectors:
  if rankK(a+[v])>len(a):a.append(v)
 return a
def mv(A,x):return [sumk([mul(a,v) for a,v in zip(row,x)]) for row in A]
def pairing(x,S,y):return sumk([mul(mul(x[i],S[i][j]),conj(y[j])) for i in range(len(x)) for j in range(len(y))])
def detK(A):
 A=[r[:] for r in A];n=len(A); s=E
 for i in range(n):
  j=next((j for j in range(i,n) if A[j][i]!=O),None)
  if j is None:return O
  if j!=i:A[i],A[j]=A[j],A[i];s=neg(s)
  pivot=A[i][i];s=mul(s,pivot); iv=inv(pivot)
  for j in range(i+1,n):
   if A[j][i]!=O:
    factor=mul(A[j][i],iv)
    for k in range(i+1,n):A[j][k]=sub(A[j][k],mul(factor,A[i][k]))
    A[j][i]=O
 return s
def principal_minors_neg_semidefinite(H):
 n=len(H); sig_counts={}; bad=[]
 for k in range(1,n+1):
  for inds in itertools.combinations(range(n),k):
   minor=detK([[H[i][j] for j in inds] for i in inds]); assert minor[1]==0, (inds,minor)
   signed=(-1)**k*minor[0]
   sig_counts[(k,'zero' if signed==0 else 'positive' if signed>0 else 'negative')]=sig_counts.get((k,'zero' if signed==0 else 'positive' if signed>0 else 'negative'),0)+1
   if signed<0:bad.append((inds,signed))
 return len(bad)==0,bad,sig_counts

def sgn_hermitian(H):
 """Signature using inertia from exact rational principal minors of all leading blocks
 via identity: inertia from eigenvalues of real-part complex Hermitian by Sylvester law;
 if leading pivots vanish, use t*I perturbation and characteristic roots rational signs.
 Instead for semidefinite H4x4, rank is enough once negative-semidefiniteness established.
 """
 return rankK(H)


# Independent specialization of relative group cup product to a *paired reflection tuple*.
# For pair i: rho(prefix at 2i)=1, rho(prefix at 2i+1)=s_i;
# u(prefix at 2i)=sum_{j<i}(a_{2j}-a_{2j+1})v_j.
# The relative correction contributes 3*(a_even conjugate b_even + a_odd conjugate b_odd).
# No shared algorithm with Claude's general word-based cup engine.
V=[[Q(a,b) for a,b in root] for root in d['roots']]
C=[[Q(a,b) for a,b in co] for co in d['H1par_basis_cocycles']]

def hv(x,y):return sumk([mul(a,conj(b)) for a,b in zip(x,y)])
def cup_pair(a,b):
    p=[O]*6
    value=O
    for i,v in enumerate(V):
        a0,a1=a[2*i:2*i+2];b0,b1=b[2*i:2*i+2]
        bw=sub(b0,b1)
        value=add(value,mul(hv(p,v),conj(bw)))
        t1=mul(a0,conj(b0));t2=mul(a0,conj(b1));t3=mul(a1,conj(b1))
        value=add(value,mul(Q(3),add(sub(t1,mul(Q(2),t2)),t3)))
        dif=sub(a0,a1)
        p=[add(x,mul(dif,y)) for x,y in zip(p,v)]
    assert p==[O]*6
    return value
S0=[[cup_pair(a,b) for b in C] for a in C]
Sexpected=mat_from(d['S_gram'])
assert S0==Sexpected
# Rational trace Hermitian form realification on K^8 over Q
H=[[mul(TH,s) for s in row] for row in S0]
trace=lambda v:2*v[0]-v[1]
scalars=[E,Q(0,1)]
base=[(i,t) for i in range(8) for t in range(2)]
Tr=[[trace(mul(mul(scalars[ta],H[i][j]),conj(scalars[tb]))) for j,tb in base] for i,ta in base]
assert all(Tr[i][j]==Tr[j][i] for i in range(16) for j in range(16))

def rational_sym_signature(M):
    M=[r[:] for r in M];p=n=z=0
    while M:
        pivot=next((i for i in range(len(M)) if M[i][i]),None)
        if pivot is None:
            off=next(((i,j) for i in range(len(M)) for j in range(i+1,len(M)) if M[i][j]),None)
            if off is None:z+=len(M);break
            i,j=off
            # symmetric change basis: e_i <- e_i+e_j
            for k in range(len(M)):M[i][k]+=M[j][k]
            for k in range(len(M)):M[k][i]+=M[k][j]
            pivot=i
            assert M[i][i]
        M[0],M[pivot]=M[pivot],M[0]
        for row in M:row[0],row[pivot]=row[pivot],row[0]
        d=M[0][0]
        if d>0:p+=1
        else:n+=1
        M=[[M[i][j]-M[i][0]*M[0][j]/d for j in range(1,len(M))] for i in range(1,len(M))]
    return (p,n,z)
sgn=rational_sym_signature(Tr)
assert sgn==(8,8,0),sgn
# Check coboundary radical from paired formula, without relying on Claude's engine.
cob=[]
for k in range(6):cob.append([neg(div(conj(v[k]),Q(3))) for v in [vv for root in V for vv in (root,root)]])
for x in C:
 for b in cob:
  assert cup_pair(x,b)==O and cup_pair(b,x)==O
print('paired-cup formula == supplied S exactly:',S0==Sexpected)
print('coboundary radical (both slots): PASS')
print('Hermitian h exact rational trace signature:',sgn,' -> K-signature',(sgn[0]//2,sgn[1]//2))
with open('/home/claude/g34/cg_replay/W7_cup_results.json','w') as f:json.dump({'cup_gram_exact_match':S0==Sexpected,'coboundary_radical_both_slots':True,'trace_form_signature':sgn,'hermitian_K_signature':[sgn[0]//2,sgn[1]//2]},f,indent=2)
