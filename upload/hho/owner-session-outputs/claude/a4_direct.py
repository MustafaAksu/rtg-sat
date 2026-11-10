# Claude: independent DIRECT parabolic Gram computation for psi = omega^k (x) rho4 with the actual A4 coefficient form.
# generic_engine.Local is reused for the cocycle space; only the cup form is re-implemented with a general
# invariant Gram H0 (S(x,y) = sum_k h0(Q_k^{-1} F_k + alpha_k, c_k)), using true inverses Q_k^{-1}.
import sys, io, contextlib, importlib.util, ast
sys.path.insert(0,'.')
from generic_engine import *
spec=importlib.util.spec_from_file_location('cdc','cyclic_disc_claude.py'); mod=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
c3=[ONE,W,mul(W,W)]
def minv(M):
    n=len(M); R,piv=rref([r+e for r,e in zip(M,eye(n))]); assert piv==list(range(n)); return [r[n:] for r in R]
def hH(H0,x,y): return h(mv(H0,x),y) if False else __import__('functools').reduce(add,[mul(mul(x[i],H0[i][j]),conj(y[j])) for i in range(len(x)) for j in range(len(y))],Z)
class LocalH0(Local):
    def __init__(self,gs,H0):
        self.H0=H0; super().__init__(gs)
    def S(self,x,y):
        cx=self.values(x); cy=self.values(y); s=Z; Fk=[Z]*self.n
        for k in range(self.r):
            G=mv(minv(self.Q[k]),Fk)
            al=solve(msub(eye(self.n),self.g[k]),cx[k])
            s=add(s,hH(self.H0,vadd(G,al),cy[k]))
            Fk=vadd(Fk,mv(self.Q[k],cx[k]))
        return s
# rho4 in basis f_i = e_i - e_4 (points 0..4, point 4 as base), Gram I+J (det 5)
def rho4(f):
    al,be=f; img=lambda x:(al*x+be)%5
    def vec(a,b):   # e_a - e_b in basis f_0..f_3
        v=[Z]*4
        if a!=4: v[a]=add(v[a],ONE)
        if b!=4: v[b]=sub(v[b],ONE)
        return v
    cols=[vec(img(i),img(4)) for i in range(4)]
    return [[cols[j][i] for j in range(4)] for i in range(4)]
H0=[[(F(2),F(0)) if i==j else ONE for j in range(4)] for i in range(4)]
def sc(c,M): return [[mul(c,x) for x in r] for r in M]
def unitary(M): return mm(mm(adj(M),H0),M)==H0   # adj = conj transpose; h0(Mx,My)=h0(x,y)
def run(t):
    gs=[sc(c3[k],rho4(f)) for k,f in t]
    assert all(unitary(g) for g in gs)
    P=eye(4)
    for g in gs: P=mm(P,g)
    assert P==eye(4)
    LS=LocalH0(gs,H0); Hb=LS.comp
    Gm=[[LS.S(x,y) for y in Hb] for x in Hb]; hm=[[mul(mod.theta,x) for x in r] for r in Gm]
    d=mod.det(hm); assert d[1]==0
    tcount=sum(1 for k,f in t if k)
    return len(Hb),d[0],mod.hsig(hm),mod.norm_class(d[0]),tcount
rows=[]
for line in open(sys.argv[1]):
    if line.startswith('[('):
        t=ast.literal_eval(line.split(' dim')[0]); rows.append(t)
from collections import Counter
cnt=Counter()
for t in rows:
    dim,d,sig,cl,tc=run(t)
    print(t,'dim',dim,'det',d,'sig',sig,'class',cl,'t=#{k!=0}',tc,'t odd' if tc%2 else '')
    cnt[(sig,cl,tc%2)]+=1
print('SUMMARY',dict(cnt))
