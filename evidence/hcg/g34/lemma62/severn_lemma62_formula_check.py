"""Evaluate Severn's Lemma 6.2 formula S(a,b)=sum_i h(Q_i^{-1}F_i^a + a_i, c_i^b) directly on the W5 certificate
(no session engine import) and compare with the certificate's S_gram. Also test independence of the choice of
preimage a_i (any a_i with (1-T_i)a_i = c_i) by adding random vectors of ker(1-T_i)."""
import json, sys, random
from fractions import Fraction as F
d=json.load(open(sys.argv[1]))
K=lambda p:(F(str(p[0])),F(str(p[1])))
def mul(x,y): a,b=x;c,e=y; return (a*c-b*e,a*e+b*c-b*e)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def conj(x): return (x[0]-x[1],-x[1])
def inv(x): n=x[0]*x[0]-x[0]*x[1]+x[1]*x[1]; c=conj(x); return (c[0]/n,c[1]/n)
Z=(F(0),F(0)); ONE=(F(1),F(0))
def h(x,y):
    s=Z
    for a,b in zip(x,y): s=add(s,mul(a,conj(b)))
    return s
def vadd(u,v): return [add(a,b) for a,b in zip(u,v)]
def vsc(c,u): return [mul(c,a) for a in u]
roots=[[K(p) for p in v] for v in d['roots']]
def refl_apply(v,x):  # x - 2h(x,v)/h(v,v) v
    c=mul((F(-2),F(0)),mul(h(x,v),inv(h(v,v)))); return vadd(x,vsc(c,v))
r=20; V=[roots[i//2] for i in range(r)]
def T(i,x): return refl_apply(V[i],x)          # reflections are self-inverse, unitary
def Q(i,x):   # Q_i = s_1...s_{i-1} applied to x: apply s_{i-1} first
    for j in range(i-1,-1,-1): x=T(j,x)
    return x
def Qinv(i,x):
    for j in range(0,i): x=T(j,x)
    return x
basis=[[K(p) for p in c] for c in d['H1par_basis_cocycles']]
def data(coc):
    c=[vsc(coc[i],V[i]) for i in range(r)]
    Fs=[]; acc=[Z]*6
    for i in range(r):
        Fs.append(acc); acc=vadd(acc,Q(i,c[i]))
    assert all(x==Z for x in acc), 'closure'
    return c,Fs
def S(ca,cb,rand=False):
    c,Fs=data(ca); c2,_=data(cb); s=Z
    for i in range(r):
        a=vsc((F(1,2),F(0)),c[i])          # (1-s_i)(c/2)=c since c in K v_i
        if rand:                             # add k in ker(1-s_i) = v_i-perp
            w=[(F(random.randint(-3,3)),F(random.randint(-3,3))) for _ in range(6)]
            p=mul(h(w,V[i]),inv(h(V[i],V[i]))); k=vadd(w,vsc(neg(p),V[i]))
            assert T(i,k)==k; a=vadd(a,k)
        s=add(s,h(vadd(Qinv(i,Fs[i]),a),c2[i]))
    return s
G=[[K(p) for p in row] for row in d['S_gram']]
M=[[S(basis[i],basis[j]) for j in range(8)] for i in range(8)]
Mr=[[S(basis[i],basis[j],True) for j in range(8)] for i in range(8)]
same=all(M[i][j]==G[i][j] for i in range(8) for j in range(8))
negs=all(M[i][j]==neg(G[i][j]) for i in range(8) for j in range(8))
conjs=all(M[i][j]==conj(G[i][j]) for i in range(8) for j in range(8))
print('Severn Lemma 6.2 formula vs certificate S_gram: equal',same,'| equals -S',negs,'| equals conj S',conjs)
print('independent of preimage choice (random ker(1-T_i) shifts):',Mr==M)
skew=all(M[i][j]==neg(conj(M[j][i])) for i in range(8) for j in range(8)); print('skew-Hermitian:',skew)
