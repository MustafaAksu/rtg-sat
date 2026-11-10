"""Exact check of the identity  S(x, N_e y) = - h( F_e(tau x), F_e(tau y) )  on certificates, where
tau(u)_i = a_{2i-1} - a_{2i}  (u(g_k) = a_k v_{pair(k)}),  F_e(t) = sum_{i in P(e)} t_i v_i.
Also checks: tau(N_e u) = 0 for all e (so N_e N_f = 0), dim ker tau = 4, image of tau = L."""
import json, sys
from fractions import Fraction as F
d=json.load(open(sys.argv[1]))
K=lambda p:(F(str(p[0])),F(str(p[1])))
Z=(F(0),F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): a,b=x;c,e=y; return (a*c-b*e,a*e+b*c-b*e)
def conj(x): return (x[0]-x[1],-x[1])
def neg(x): return (-x[0],-x[1])
def h(x,y):
    s=Z
    for a,b in zip(x,y): s=add(s,mul(a,conj(b)))
    return s
roots=[[K(p) for p in v] for v in d['roots']]
basis=[[K(p) for p in c] for c in d['H1par_basis_cocycles']]     # 8 cocycles, each 20 scalars a_k
S=[[K(p) for p in r] for r in d['S_gram']]
def tau(coords):   # coords: 8 K-coefficients in the basis -> tau in K^10
    a=[Z]*20
    for c,b in zip(coords,basis):
        a=[add(x,mul(c,y)) for x,y in zip(a,b)]
    return [sub(a[2*i],a[2*i+1]) for i in range(10)]
def Fe(t,P):
    v=[Z]*6
    for i in P: v=[add(x,mul(t[i],y)) for x,y in zip(v,roots[i])]
    return v
def Sform(x,y):   # S(x,y)=x^T S conj(y), linear in first
    s=Z
    for i in range(8):
        for j in range(8): s=add(s,mul(mul(x[i],S[i][j]),conj(y[j])))
    return s
E=[[1 if i==j else 0 for j in range(8)] for i in range(8)]
E=[[(F(v),F(0)) for v in r] for r in E]
ok_id=True; ok_tauN=True
for cv in d['curves']:
    a,b=cv['curve']; P=list(range((a-1)//2,b//2))
    N=[[K(p) for p in r] for r in cv['N']]
    Ny=[[ (lambda col: col)([N[i][j] for i in range(8)]) ] for j in range(8)]   # N e_j = column j
    cols=[[N[i][j] for i in range(8)] for j in range(8)]
    for j in range(8):
        ok_tauN &= all(x==Z for x in tau(cols[j]))
        for i in range(8):
            lhs=Sform(E[i],cols[j])
            rhs=neg(h(Fe(tau(E[i]),P),Fe(tau(E[j]),P)))
            ok_id &= (lhs==rhs)
# rank of tau
import flint
rows=[]
for i in range(8):
    t=tau(E[i]); rows.append([c for x in t for c in x])
rk=flint.fmpq_mat([[flint.fmpq(x.numerator,x.denominator) for x in r] for r in rows]).rank()
# tau image inside L
inL=all(all(x==Z for x in Fe(tau(E[i]),range(10))) for i in range(8))
print(sys.argv[1],'| identity S(x,N_e y) = -h(F_e tau x, F_e tau y) for all 17 curves, 64 entries each:',ok_id,
      '| tau(N_e u)=0:',ok_tauN,'| Q-rank of the 8 basis images (diagnostic):',rk,'| image in L:',inL)
sys.path.insert(0,'/home/claude/g34/h4sel/edgeform')
import edgeform_predict as P
M=[tau(E[i]) for i in range(8)]
print('   K-rank of tau =',10-len(P.nullspace(M,10)),'(dim_K L = 4 => surjective onto L)')
Lb=P.nullspace([[roots[i][k] for i in range(10)] for k in range(6)],10)
print('   (A3) every coordinate t_i nonzero on L:', all(any(t[i]!=Z for t in Lb) for i in range(10)))
