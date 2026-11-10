"""Claude's generic exact engine (independent of g34_gateB and of ChatGPT code) for parabolic cohomology of a
local system on P^1 minus r points with unitary monodromy (g_1..g_r), g_1...g_r = 1, over K=Q(w), w^2+w+1=0.
Left cocycles u(xy)=u(x)+rho(x)u(y); parabolic: u(g_k) in im(g_k - 1); cup form = Severn [19, Lemma 6.2] /
session formula S(a,b)=sum_k h(Q_k^{-1}F_k^a + alpha_k^a, c_k^b), (1-g_k)alpha_k = c_k."""
from fractions import Fraction as F
import itertools, random
Z=(F(0),F(0)); ONE=(F(1),F(0)); W=(F(0),F(1))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): a,b=x;c,e=y; return (a*c-b*e,a*e+b*c-b*e)
def conj(x): return (x[0]-x[1],-x[1])
def inv(x): n=x[0]*x[0]-x[0]*x[1]+x[1]*x[1]; c=conj(x); return (c[0]/n,c[1]/n)
def isz(x): return x[0]==0 and x[1]==0
def h(x,y):
    s=Z
    for a,b in zip(x,y): s=add(s,mul(a,conj(b)))
    return s
def mv(M,x): return [ (lambda r: __import__('functools').reduce(add,[mul(a,b) for a,b in zip(r,x)],Z))(r) for r in M]
def mm(A,B): return [[ __import__('functools').reduce(add,[mul(A[i][k],B[k][j]) for k in range(len(B))],Z) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n): return [[ONE if i==j else Z for j in range(n)] for i in range(n)]
def msub(A,B): return [[sub(a,b) for a,b in zip(r,s)] for r,s in zip(A,B)]
def adj(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def vadd(u,v): return [add(a,b) for a,b in zip(u,v)]
def vsc(c,u): return [mul(c,a) for a in u]
def rref(M):
    M=[r[:] for r in M]; piv=[]; r=0
    ncol=len(M[0]) if M else 0
    for c in range(ncol):
        p=next((i for i in range(r,len(M)) if not isz(M[i][c])),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; iv=inv(M[r][c]); M[r]=[mul(iv,x) for x in M[r]]
        for i in range(len(M)):
            if i!=r and not isz(M[i][c]):
                f=M[i][c]; M[i]=[sub(a,mul(f,b)) for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
    return M[:r],piv
def nullspace(M,n):
    R,piv=rref(M) if M else ([],[])
    free=[c for c in range(n) if c not in piv]; out=[]
    for fc in free:
        v=[Z]*n; v[fc]=ONE
        for i,pc in enumerate(piv): v[pc]=neg(R[i][fc])
        out.append(v)
    return out
def rank(M): return len(rref(M)[1]) if M else 0
def colspace(M):  # basis of column space
    cols=[[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
    R,piv=rref(cols); return [r for r in R]
def solve(A,b):   # one solution x of A x = b (A square or not), exact
    n=len(A[0]); aug=[A[i]+[b[i]] for i in range(len(A))]
    R,piv=rref(aug); assert n not in piv, 'inconsistent'
    x=[Z]*n
    for i,pc in enumerate(piv): x[pc]=R[i][n]
    return x
class Local:
    def __init__(self,gs):
        self.g=gs; self.r=len(gs); self.n=len(gs[0])
        P=eye(self.n)
        for g in gs: P=mm(P,g)
        assert P==eye(self.n), 'product != 1'
        self.Q=[eye(self.n)]
        for g in gs[:-1]: self.Q.append(mm(self.Q[-1],g))
        self.Wb=[colspace(msub(g,eye(self.n))) for g in gs]      # basis of im(g-1)
        # cochain coordinates: concat of coefficients wrt Wb[k]
        self.dims=[len(w) for w in self.Wb]; self.N=sum(self.dims)
        cl=[]   # closure: sum_k Q_k c_k = 0
        cols=[]
        for k in range(self.r):
            for w in self.Wb[k]: cols.append(mv(self.Q[k],w))
        cl=[[cols[j][i] for j in range(self.N)] for i in range(self.n)]
        self.Z1=nullspace(cl,self.N)
        self.B1=[self.coords([mv(msub(g,eye(self.n)),e) for g in gs]) for e in eye(self.n)]
        # complement of B1 in Z1
        cur=[b for b in self.B1]; self.comp=[]
        for z in self.Z1:
            if rank(cur+[z])>rank(cur): cur.append(z); self.comp.append(z)
    def values(self,coord):  # coordinate vector -> list of c_k in K^n
        out=[]; p=0
        for k in range(self.r):
            v=[Z]*self.n
            for j,w in enumerate(self.Wb[k]): v=vadd(v,vsc(coord[p+j],w))
            out.append(v); p+=self.dims[k]
        return out
    def coords(self,vals):
        out=[]
        for k in range(self.r):
            if self.dims[k]==0: continue
            A=[[self.Wb[k][j][i] for j in range(self.dims[k])] for i in range(self.n)]
            out+=solve(A,vals[k])
        return out
    def uword(self,vals,word):   # word: list of (index, +1/-1); returns (u(word), rho(word))
        u=[Z]*self.n; R=eye(self.n)
        for (k,e) in word:
            g=self.g[k]
            if e==1: val=vals[k]; gm=g
            else:
                gi=adj(g); val=vsc(neg(ONE),mv(gi,vals[k])); gm=gi   # u(g^-1) = -g^{-1}u(g)
            u=vadd(u,mv(R,val)); R=mm(R,gm)
        return u,R
    def S(self,x,y):  # x,y cochain coordinates (cocycles)
        cx=self.values(x); cy=self.values(y); s=Z; Fk=[Z]*self.n
        for k in range(self.r):
            Qi=adj(self.Q[k]); G=mv(Qi,Fk)
            al=solve(msub(eye(self.n),self.g[k]),cx[k])
            s=add(s,h(vadd(G,al),cy[k]))
            Fk=vadd(Fk,mv(self.Q[k],cx[k]))
        return s
    def twist_cocycle(self,vals,a,b,power):   # u -> u o phi^power, phi(g_k)=c g_k c^-1 for a<=k<=b (0-based)
        c=[(k,1) for k in range(a,b+1)]
        cw=c*power; ciw=[(k,-1) for k in reversed(range(a,b+1))]*power
        out=[]
        for k in range(self.r):
            if a<=k<=b: out.append(self.uword(vals,cw+[(k,1)]+ciw)[0])
            else: out.append(vals[k])
        return out
