"""Generic toy of the SAME cocycle/braid model over Q, to test whether paired tuples produce abelian monodromy.
Case A: S3 = W(A2) reflection rep (2-dim, over Q), paired tuple (s1,s1,s2,s2,s3,s3) (+ extra pair) .
Case B: Z/2 (d=1, g=-1), 6 points (hyperelliptic genus 2): known non-abelian (Sp4)."""
import random, itertools, sys
from fractions import Fraction as F
import sympy as sp
def run(gens_roots, form, tuple_idx, trials=40, seed=1):
    d=len(form); r=len(tuple_idx)
    Fm=sp.Matrix(form)
    def refl(v):
        v=sp.Matrix(v); return sp.eye(d)-2*v*(v.T*Fm)/((v.T*Fm*v)[0])
    R=[refl(v) for v in gens_roots]
    G=[R[t] for t in tuple_idx]; V=[sp.Matrix(gens_roots[t]) for t in tuple_idx]
    P=sp.eye(d)
    for g in G: P=P*g
    assert P==sp.eye(d)
    Q=[sp.eye(d)]
    for i in range(1,r): Q.append(Q[-1]*G[i-1])
    a=sp.symbols(f'a0:{r}')
    clos=sum((Q[i]*V[i]*a[i] for i in range(r)),sp.zeros(d,1))
    Cl=sp.Matrix([[sp.diff(clos[k],a[i]) for i in range(r)] for k in range(d)])
    Z=Cl.nullspace()
    Bm=[]
    for k in range(d):
        w=sp.zeros(d,1); w[k]=1
        Bm.append([ ((G[i]-sp.eye(d))*w).dot(V[i])/V[i].dot(V[i]) if True else 0 for i in range(r)])
    # coordinates of (g-1)w along v_i: (g-1)w is a multiple of v_i
    Bm=[]
    for k in range(d):
        w=sp.zeros(d,1); w[k]=1; row=[]
        for i in range(r):
            x=(G[i]-sp.eye(d))*w; j=next(t for t in range(d) if V[i][t]!=0); row.append(x[j]/V[i][j])
        Bm.append(row)
    Bmat=sp.Matrix(Bm); rkB=Bmat.rank()
    Zm=sp.Matrix.hstack(*Z).T
    comp=[]; cur=Bmat
    for z in Z:
        t=sp.Matrix.vstack(cur,z.T)
        if t.rank()>cur.rank(): cur=t; comp.append(z)
    dim=len(comp)
    basis=sp.Matrix.hstack(*(comp+[sp.Matrix(b) for b in Bm]))
    def coords(avec):
        sol=basis.gauss_jordan_solve(sp.Matrix(avec))[0]
        sol=sol.subs({s:0 for s in sol.free_symbols})
        return list(sol[:dim])
    def move(roots,U,i,inv):
        gi=refl(roots[i]); gj=refl(roots[i+1]); u0,u1=U[i],U[i+1]
        if not inv:
            nv=gi*roots[i+1]; gn=refl(nv); U[i]=u0+gi*u1-gn*u0; U[i+1]=u0; roots[i],roots[i+1]=nv,roots[i]
        else:
            nv=gj*roots[i]; U[i]=u1; U[i+1]=gj*(u0+gi*u1-u1); roots[i],roots[i+1]=roots[i+1],nv
    def T_of(word):
        cols=[]
        for z in comp:
            roots=[sp.Matrix(v) for v in V]; U=[V[i]*z[i] for i in range(r)]
            for i,inv in word: move(roots,U,i,inv)
            for t in range(r): assert refl(roots[t])==G[t]
            av=[]
            for t in range(r):
                j=next(q for q in range(d) if V[t][q]!=0); av.append(U[t][j]/V[t][j])
            cols.append(coords(av))
        return sp.Matrix(cols).T
    def ret_k(roots,a,b):
        C=sp.eye(d)
        for j in range(a,b+1): C=C*refl(roots[j])
        Ck=sp.eye(d)
        for k in range(1,60):
            Ck=Ck*C
            if all(Ck*refl(roots[i])==refl(roots[i])*Ck for i in range(a,b+1)): return k
    rng=random.Random(seed); Ts=[]
    for _ in range(trials):
        beta=[(rng.randrange(r-1),rng.random()<0.5) for _ in range(rng.randint(0,12))]
        roots=[sp.Matrix(v) for v in V]; U=[sp.zeros(d,1)]*r
        for i,inv in beta: move(roots,U,i,inv)
        L=2; a_=rng.randrange(r-1); b_=a_+1
        k=ret_k(roots,a_,b_)
        if k is None: continue
        word=beta+[(i,False) for i in range(a_,b_)]*((b_-a_+1)*k)+[(i,not inv) for i,inv in reversed(beta)]
        T=T_of(word)
        if T!=sp.eye(dim): Ts.append(T)
    nc=sum(1 for X in Ts for Y in Ts if X*Y!=Y*X)
    return dim,rkB,len(Ts),nc
# Case B: hyperelliptic genus 2: d=1, g=-1, 6 points
print("Z/2, 6 pts (dim H1, rank B, #T, noncommuting pairs):",run([[1]],[[1]],[0]*6,trials=30))
# Case A: S3 reflection rep on {x1+x2+x3=0} coordinates; form = [[2,-1],[-1,2]]; roots of A2: a1=(1,0), a2=(0,1), a1+a2
A2=[[2,-1],[-1,2]]
print("S3 paired (s1,s1,s2,s2,s3,s3,s1,s1):",run([[1,0],[0,1],[1,1]],A2,[0,0,1,1,2,2,0,0],trials=40))
