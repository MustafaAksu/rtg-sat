"""H4 obstruction analysis (session exploratory). For a roots file + interval decomposition:
N_j, I, beta_j on V/I, Q-rank of the beta_j in Herm_4(K) (=16-dim over Q), and the annihilating
Hermitian forms Y with tr(beta_j Y)=0 for all j (the obstruction directions). Uses g34_gateB unchanged."""
import os, sys, json
os.environ['ROOTS_JSON']=sys.argv[1]
sys.argv=[sys.argv[0]]+sys.argv[1:]
import sympy as sp
import g34_gateB as B
from fractions import Fraction as Fr
BAL=[(2*i-1,2*i) for i in range(1,11)]+[(1,4),(5,8),(9,12),(13,16),(1,8),(9,16),(1,16)]
COMB=[(2*i-1,2*i) for i in range(1,11)]+[(1,2*k) for k in range(2,9)]
w=sp.Rational(-1,2)+sp.sqrt(3)*sp.I/2
def toC(x): return sp.Rational(x[0].numerator,x[0].denominator)+sp.Rational(x[1].numerator,x[1].denominator)*w
def analyse(curves):
    Ns=[]
    for a,b in curves:
        k,C=B.return_power(a-1,b-1); T=B.T_matrix(a-1,b-1,k); Ns.append(B.mlog_unipotent(T))
    imgs=[[N[i][j] for i in range(8)] for N in Ns for j in range(8)]
    imgs=[c for c in imgs if any(not B.iszero(x) for x in c)]
    Ir,_=B.rref(imgs); Ib=[v for v in Ir if any(not B.iszero(x) for x in v)]
    compl=[]; cur=list(Ib)
    for e in B.eye(8):
        if B.rank(cur+[e])>B.rank(cur): cur.append(e); compl.append(e)
    def Sv(x,y):
        s=B.Z0
        for i in range(8):
            for j in range(8): s=B.add(s,B.mul(B.mul(x[i],B.Sg[i][j]),B.conj(y[j])))
        return s
    betas=[[[Sv(x,B.matvec(N,y)) for y in compl] for x in compl] for N in Ns]
    return Ns,Ib,compl,betas
def hcoords(Bm):
    c=[]
    for i in range(4): c.append(Bm[i][i][0])           # rational diagonal (b=0)
    for i in range(4):
        for j in range(i+1,4): c+= [Bm[i][j][0],Bm[i][j][1]]
    return c
out={}
for name,curves in (('balanced',BAL),('comb',COMB)):
    Ns,Ib,compl,betas=analyse(curves)
    C=sp.Matrix([[sp.Rational(str(v)) for v in hcoords(b)] for b in betas]).T   # 16 x 17
    rk=C.rank()
    # obstruction: Hermitian Y (16 params) with Re-trace tr(beta_j Y)=0
    ys=sp.symbols('y0:16', real=True); Y=[[None]*4 for _ in range(4)]
    for i in range(4): Y[i][i]=ys[i]
    idx=4
    for i in range(4):
        for j in range(i+1,4):
            Y[i][j]=ys[idx]+ys[idx+1]*w; Y[j][i]=sp.conjugate(Y[i][j]); idx+=2
    eqs=[]
    for b in betas:
        M=sp.Matrix(4,4,lambda i,j: toC(b[i][j]))
        t=sp.expand(sum(M[i,j]*Y[j][i] for i in range(4) for j in range(4)))
        eqs.append(sp.nsimplify(sp.simplify(t)))
    A,_=sp.linear_eq_to_matrix(eqs,ys); nul=A.nullspace()
    Ysig=[]
    for v in nul:
        Ym=sp.Matrix(4,4,lambda i,j: sp.simplify(Y[i][j].subs(dict(zip(ys,v)))))
        ev=[sp.re(sp.N(e,30)) for e in Ym.eigenvals(multiple=True)]
        Ysig.append(dict(rank=Ym.rank(),pos=sum(1 for e in ev if e>1e-20),neg=sum(1 for e in ev if e<-1e-20)))
    # which single curves lie outside the span of the others (needed curves)
    need=[curves[j] for j in range(len(curves)) if C[:, [k for k in range(len(curves)) if k!=j]].rank()<rk]
    out[name]=dict(rank=rk,obstruction_dim=16-rk,Y_signatures=Ysig,curves_needed_for_rank=need,
                   I_basis=[[str(x) for x in v] for v in Ib])
    print(name,'rank',rk,'obstruction dim',16-rk,'Y:',Ysig,'necessary curves:',need)
Ib_b=out['balanced']['I_basis']; Ib_c=out['comb']['I_basis']
print('I(balanced)==I(comb):',Ib_b==Ib_c)
out['same_I']=Ib_b==Ib_c
json.dump(out,open(sys.argv[2],'w'),indent=1)
