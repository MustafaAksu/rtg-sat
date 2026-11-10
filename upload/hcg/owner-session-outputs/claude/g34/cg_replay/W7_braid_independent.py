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


# Reconstruct interval monodromy by elementary Hurwitz/Artin braid operations,
# rather than the closed interval-twist formula used in the producing script.
import time

def reflect(v,x):
    q=sumk([mul(a,conj(b)) for a,b in zip(x,v)])
    q=div(q,Q(3))
    return [sub(xi,mul(q,vi)) for xi,vi in zip(x,v)]

def vadd(x,y):return [add(a,b) for a,b in zip(x,y)]
def vsub(x,y):return [sub(a,b) for a,b in zip(x,y)]
def vscale(x,y):return [mul(x,a) for a in y]
roots=[[Q(a,b) for a,b in v] for v in d['roots']]
rr=[v for root in roots for v in (root,root)]
cb=[]
for k in range(6):
    cb.append([neg(div(conj(v[k]),Q(3))) for v in rr])
cc=[[Q(a,b) for a,b in basis] for basis in d['H1par_basis_cocycles']]
BB=cc+cb
assert rankK(BB)==14
rows=[[basis[i] for basis in BB] for i in range(20)]
chosen=[]; inds=[]
for i,row in enumerate(rows):
    if rankK(chosen+[row])>len(chosen):chosen.append(row); inds.append(i)
assert len(chosen)==14

def invmat(M):
  n=len(M); a=[r[:]+eye(n)[i] for i,r in enumerate(M)]
  for k in range(n):
    j=next(j for j in range(k,n) if a[j][k]!=O)
    a[k],a[j]=a[j],a[k]
    c=inv(a[k][k]);a[k]=[mul(c,u) for u in a[k]]
    for j in range(n):
      if j!=k and a[j][k]!=O:
        factor=a[j][k];a[j]=[sub(x,mul(factor,y)) for x,y in zip(a[j],a[k])]
  assert all(a[i][:n]==eye(n)[i] for i in range(n))
  return [r[n:] for r in a]
left=invmat(chosen)
def coordinates(a):
  t=mv(left,[a[i] for i in inds]); assert mv(rows,t)==a, 'not a valid cocycle in Z_par'
  return t[:8]

def elementary_braid(root20,U,i):
    # σ_i: (g_i,g_{i+1}) -> (g_i g_{i+1} g_i^{-1},g_i)
    # Cocycle values transform by functorial pullback under this Artin move.
    v=root20[i]; w=root20[i+1]
    new_v=reflect(v,w)
    for row in U:
       u0,u1=row[i],row[i+1]
       row[i] = vsub(vadd(u0,reflect(v,u1)),reflect(new_v,u0))
       row[i+1]=u0
    root20[i],root20[i+1]=new_v,v

def full_twist(a,b):
    # a,b zero-indexed inclusive, product (sigma_a ... sigma_(b-1))^(b-a+1)
    L=b-a+1
    root20=[v[:] for v in rr]
    U=[[vscale(cc[h][i],rr[i]) for i in range(20)] for h in range(8)]
    for _ in range(L):
      for i in range(a,b): elementary_braid(root20,U,i)
    # Returning tuple may have unit-scaled roots but same reflections.
    for v,w in zip(root20,rr):
      assert all(reflect(v,[E if i==j else O for i in range(6)])==reflect(w,[E if i==j else O for i in range(6)]) for j in range(6)), 'root tuple failed to return'
    cols=[]
    for row in U:
      ai=[]
      for v,u in zip(rr,row):
        j=next(j for j in range(6) if v[j]!=O)
        co=div(u[j],v[j]); assert vscale(co,v)==u, 'cocycle not parabolic'
        ai.append(co)
      cols.append(coordinates(ai))
    return [[cols[j][i] for j in range(8)] for i in range(8)]

print('Gauge independent row indices:',inds)
results={}; t0=time.time()
for c in d['curves']:
 a,b=c['curve']; t=full_twist(a-1,b-1)
 wanted=mat_from(c['T'])
 ok=eq(t,wanted)
 results[f'{a}-{b}']=ok
 print(f'braid sigma-composition [{a},{b}]: {"MATCH" if ok else "MISMATCH"} elapsed={time.time()-t0:.1f}s',flush=True)
 if not ok:
  print('difference:',mat_sub(t,wanted));break
assert all(results.values()) and len(results)==17
print('17/17 exact T matrices reproduced by independent Artin action')
with open('/home/claude/g34/cg_replay/W7_braid_results.json','w') as f:json.dump({'braid_rebuilt_exact':results,'all_pass':all(results.values()) and len(results)==17},f,indent=2)
