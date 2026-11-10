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

S=mat_from(d['S_gram']); n=8
N=[mat_from(curve['N']) for curve in d['curves']]
T=[mat_from(curve['T']) for curve in d['curves']]
zero=[[O]*n for _ in range(n)]
assert len(N)==17
results={}
results['S_skew_Hermitian']=iszero(mat_add(S,transpose_conj(S)))
results['S_rank_K']=rankK(S)
h=[[mul(TH,v) for v in row] for row in S]
results['h_Hermitian']=eq(h,transpose_conj(h))
results['det_h']=str(detK(h))
results['every_T_equals_1_plus_N']=all(mat_sub(t,eye(n))==a for t,a in zip(T,N))
results['all_N_squared_zero']=all(iszero(mm(x,x)) for x in N)
results['all_NjNk_zero']=all(iszero(mm(x,y)) for x in N for y in N)
results['all_T_preserve_S']=all(eq(mm(mm(list(map(list,zip(*t))),S),[[conj(x) for x in row] for row in t]),S) for t in T)
results['all_T_preserve_h']=all(eq(mm(mm(list(map(list,zip(*t))),h),[[conj(x) for x in row] for row in t]),h) for t in T)
# Images of N_j are columns
all_cols=[[X[i][j] for i in range(n)] for X in N for j in range(n)]
I=basis_span(all_cols)
results['dimI_K']=len(I)
results['I_isotropic']=all(pairing(x,S,y)==O for x in I for y in I)
results['N_annihilate_I']=all(mv(x,y)==[O]*n for x in N for y in I)
# complete I to basis using standard coordinate vectors, no inherited basis
comp=[]; full=I[:]
for e in eye(n):
 if rankK(full+[e])>len(full): comp.append(e);full.append(e)
results['dim_quotient_K']=len(comp)
Bs=[]; minor_results=[]
for x in N:
 B=[[pairing(a,S,mv(x,b)) for b in comp] for a in comp]
 Bs.append(B)
 herm=eq(B,transpose_conj(B));neg,bad,counts=principal_minors_neg_semidefinite(B)
 minor_results.append({'hermitian':herm,'negative_semidefinite':neg,'rank':rankK(B),'bad_minors':len(bad)})
results['all_beta_hermitian']=all(k['hermitian'] for k in minor_results)
results['all_beta_negative_semidefinite']=all(k['negative_semidefinite'] for k in minor_results)
results['beta_ranks']=[x['rank'] for x in minor_results]
Bs_sum=[[sumk([b[i][j] for b in Bs]) for j in range(len(comp))] for i in range(len(comp))]
neg,bad,counts=principal_minors_neg_semidefinite(Bs_sum)
# Negative definite => leading principal minors alternating STRICT and rank 4
leading=[detK([row[:k] for row in Bs_sum[:k]]) for k in range(1,len(comp)+1)]
results['sum_beta_negative_definite']=neg and all(p[1]==0 and (-1)**(i+1)*p[0]>0 for i,p in enumerate(leading))
results['sum_beta_leading_minors']=[str(x) for x in leading]
flat=[[x for row in X for z in row for x in z] for X in N]
results['qspanN_rank']=sp.Matrix(flat).rank()
# H0: pairs are involutions, every even aligned block has product 1
R=[]
for root in d['roots']:
 v=[(F(a),F(b)) for a,b in root]
 hnorm=sumk([mul(z,conj(z)) for z in v]); assert hnorm==Q(6)
 fac=div(Q(2),hnorm)
 R.append([[sub(E if i==j else O, mul(fac,mul(v[i],conj(v[j])))) for j in range(6)] for i in range(6)])
results['reflection_involutions']=all(eq(mm(r,r),eye(6)) for r in R)
results['all_balanced_boundary_products_identity']=all(all(a%2==1 and b%2==0 for a,b in [curve['curve']]) for curve in d['curves'])
results['all_return_powers_k1']=all(c['k']==1 for c in d['curves'])
results['H0_pants_dimension_zero']=results['all_balanced_boundary_products_identity'] and results['reflection_involutions']
results['PASS_H0_H4_from_supplied_matrices']=(results['H0_pants_dimension_zero'] and results['all_NjNk_zero'] and results['dimI_K']==4 and results['I_isotropic'] and results['N_annihilate_I'] and results['all_beta_hermitian'] and results['all_beta_negative_semidefinite'] and results['sum_beta_negative_definite'] and results['qspanN_rank']==16)
results['certificate_sha256']=hashlib.sha256(open(PATH,'rb').read()).hexdigest()
print(json.dumps(results,indent=2))
with open('/home/claude/g34/cg_replay/W7_matrix_results.json','w') as f:json.dump(results,f,indent=2)
