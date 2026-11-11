# Claude independent check of the C3 x F20 counterexample with the HCG engine (generic_engine.py unchanged).
import sys, io, contextlib, importlib.util
sys.path.insert(0,'.')
from generic_engine import *
spec=importlib.util.spec_from_file_location('cdc','cyclic_disc_claude.py'); mod=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
w=W; w2=mul(W,W)
# F20 acting on F5 by x -> a*x+b ; u: x->x+1, a: x->2x  (a u a^-1 = u^2)
def perm(f):
    M=[[Z]*5 for _ in range(5)]
    for x in range(5): M[f(x)][x]=ONE
    return M
U=perm(lambda x:(x+1)%5); Ui=perm(lambda x:(x-1)%5)
A=perm(lambda x:(2*x)%5); Ai=perm(lambda x:(3*x)%5)
I5=eye(5)
assert mm(mm(A,U),Ai)==mm(U,U)
def sc(c,M): return [[mul(c,x) for x in r] for r in M]
c3=[ONE,w,w2]
tup=[(1,I5)]*5+[(2,I5)]*4+[(2,A),(0,Ai),(0,U),(0,Ui)]
# rank-1 chi = omega (x) 1
chi=[[[c3[k]]] for k,_ in tup]
LS=Local(chi); H=LS.comp
G=[[LS.S(x,y) for y in H] for x in H]; h=[[mul(mod.theta,x) for x in r] for r in G]
d=mod.det(h)
print('chi: dim',len(H),'det',d[0],'sig',mod.hsig(h),'class',mod.norm_class(d[0]))
# 5-dim permutation local system omega^k (x) perm = psi (+) chi  -> dim = m(psi)+m(chi)
P=[sc(c3[k],M) for k,M in tup]
LP=Local(P)
print('omega(x)perm5: dim H1_par =',len(LP.comp),' => m(psi) =',len(LP.comp)-len(H))
# chi-effective-branch moving-rank sum for psi
def rk(M): return rank(msub(M,eye(len(M))))
cpsi=[rk(sc(c3[k],M))-(0 if k==0 else 1) for k,M in tup]   # psi rank = perm rank minus chi-part rank
print('c_psi per branch',cpsi,'sum',sum(cpsi),'sum over chi-effective',sum(c for c,(k,_) in zip(cpsi,tup) if k))
