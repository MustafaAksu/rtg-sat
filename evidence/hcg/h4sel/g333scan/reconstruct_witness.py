"""Claude's independent reconstruction of NEW01-MIXED-01 with generic_engine.py (no ChatGPT code; the ChatGPT
certificate is read ONLY in the final comparison block). Severn hexagon:2610.00387v1 §4 definitions:
 tau_j full Artin twist g_i -> c g_i c^-1 (a<=i<=b); k_j least power with tau_j^k(g)=g (matrix tuple equality);
 T_j = pullback u -> u o phi^{k_j} on H^1_par; m_j order of semisimple part of T_j; N_j = log T_j^{m_j}.
 (H0) per pants: sum_i rank(1-P_i) - 2d + 2 dim Fix<P1,P2,P3> = 0;  (H1)-(H4) as in Prop 4.2."""
import sys, json, itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
OUT=[]
def say(*a):
    s=' '.join(str(x) for x in a); print(s); OUT.append(s)
NAME=sys.argv[1]; CURVES=[tuple(x) for x in json.loads(sys.argv[2])]
ROOTS='/home/claude/g34/h4sel/g333scan/g333_witness_roots.json'
assert len(CURVES)==9
def Kc(p): return (F(p[0]),F(p[1]))
V=[[Kc(c) for c in v] for v in json.load(open(ROOTS))['final_roots']]
n=3
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
S_=[refl(v) for v in V]
gs=[]
for s in S_: gs+=[s,s]
LS=Local(gs); H=LS.comp; dH=len(H)
say('dim H^1_par =',dH,'; |Z1|=',len(LS.Z1),'; |B1|=',len(LS.B1))
# ---- laminar check + pants
iv=[(a-1,b-1) for a,b in CURVES]
lam=all((b1<a2 or b2<a1) or (a1<=a2 and b2<=b1) or (a2<=a1 and b1<=b2) for (a1,b1),(a2,b2) in itertools.combinations(iv,2))
say('9 curves, laminar:',lam,', all proper (not whole sphere):',all(not(a==0 and b==11) for a,b in iv))
def prodM(a,b):
    C=eye(n)
    for k in range(a,b+1): C=mm(C,gs[k])
    return C
# pants: regions = each interval e minus its maximal sub-intervals, plus the root region
def children(e):
    a,b=e; inside=[f for f in iv if f!=e and a<=f[0] and f[1]<=b]
    maxi=[f for f in inside if not any(g!=f and g[0]<=f[0] and f[1]<=g[1] for g in inside)]
    covered=set(k for f in maxi for k in range(f[0],f[1]+1))
    pts=[(k,k) for k in range(a,b+1) if k not in covered]
    return sorted(maxi+pts)
roots_=[f for f in iv if not any(g!=f and g[0]<=f[0] and f[1]<=g[1] for g in iv)]
covered=set(k for f in roots_ for k in range(f[0],f[1]+1))
rootregion=sorted(roots_+[(k,k) for k in range(12) if k not in covered])
pants=[(e,children(e)) for e in iv]+[(None,rootregion)]
h0ok=True
for outer,ch in pants:
    bnd=[prodM(a,b) for a,b in ch]
    if outer is not None: bnd.append(adj(prodM(*outer)))
    if len(bnd)!=3: say('  pants not trivalent!',outer,ch); h0ok=False; continue
    cs=[rank(msub(eye(n),P)) for P in bnd]
    fixdim=n-rank(msub(eye(n),bnd[0])+msub(eye(n),bnd[1])+msub(eye(n),bnd[2]))
    defect=sum(cs)-2*n+2*fixdim
    if defect!=0: h0ok=False
    say(f'  pants outer={None if outer is None else (outer[0]+1,outer[1]+1)} children={[(a+1,b+1) for a,b in ch]} c={cs} dimFix={fixdim} defect={defect}')
say('number of pants =',len(pants),'; (H0) all defects zero:',h0ok)
# ---- operators
Bmat=[[x for x in col] for col in zip(*(H+LS.B1))]  # columns: comp then B1
def to_H(coords):
    sol=solve(Bmat,coords); return sol[:dH]
def Tmatrix(a,b,p):
    cols=[]
    for x in H:
        v=LS.values(x); tw=LS.twist_cocycle(v,a,b,p); cols.append(to_H(LS.coords(tw)))
    return [[cols[j][i] for j in range(dH)] for i in range(dH)]   # column j = image of basis j
def mpow(M,k):
    R=eye(len(M))
    for _ in range(k): R=mm(R,M)
    return R
def is_nilp(M):
    return all(isz(x) for r in mpow(M,len(M)) for x in r)
def logU(U):
    X=msub(U,eye(len(U))); R=[[Z]*len(U) for _ in U]; P=eye(len(U))
    for k in range(1,len(U)+1):
        P=mm(P,X); c=(F((-1)**(k+1),k),F(0))
        R=[[add(r,mul(c,p)) for r,p in zip(rr,pp)] for rr,pp in zip(R,P)]
    return R
G=[[LS.S(x,y) for y in H] for x in H]
say('S Gram rank =',rank(G))
recs=[]
for (a,b) in iv:
    C=prodM(a,b)
    ordC=next(k for k in range(1,200) if mpow(C,k)==eye(n))
    kj=next(k for k in range(1,200) if all(mm(mm(mpow(C,k),gs[i]),adj(mpow(C,k)))==gs[i] for i in range(a,b+1)))
    T=Tmatrix(a,b,kj)
    mj=next(m for m in range(1,200) if is_nilp(msub(mpow(T,m),eye(dH))))
    N=logU(mpow(T,mj))
    That=Tmatrix(a,b,ordC); Nhat=msub(That,eye(dH))
    scale=F(ordC,kj*mj)
    rel=all(Nhat[i][j]==mul((scale,F(0)),N[i][j]) for i in range(dH) for j in range(dH))
    nil2=all(isz(x) for r in mm(N,N) for x in r)
    recs.append(dict(e=(a+1,b+1),ordC=ordC,k=kj,m=mj,N=N,rkK=rank(N),hat_rel=rel,N2=nil2))
    say(f'curve [{a+1},{b+1}] ord(C)={ordC} k={kj} m={mj} rank_K N={rank(N)} N^2=0:{nil2} Nhat=(ordC/(k m))N:{rel}')
Ns=[r['N'] for r in recs]
# H1
h1=all(all(isz(x) for r in mm(A,B) for x in r) for A in Ns for B in Ns)
say('(H1) all 81 products N_j N_k = 0:',h1)
# H2
colsI=[[N[i][j] for i in range(dH)] for N in Ns for j in range(dH)]
Ibasis=rref(colsI)[0]; dI=len(Ibasis)
def Svec(x,y):  # S on H-coordinates
    return __import__('functools').reduce(add,[mul(mul(x[i],conj(y[j])),G[i][j]) for i in range(dH) for j in range(dH)],Z)
iso=all(isz(Svec(x,y)) for x in Ibasis for y in Ibasis)
kill=all(all(isz(c) for c in mv(N,x)) for N in Ns for x in Ibasis)
say(f'(H2) dim_K I = {dI}; isotropic: {iso}; all N_j kill I: {kill}')
# beta_j(x,y)=S(x,N_j y): matrix beta[i][l] = sum_k G[i][k] conj(N[k][l])
def beta(N): return [[__import__('functools').reduce(add,[mul(G[i][k],conj(N[k][l])) for k in range(dH)],Z) for l in range(dH)] for i in range(dH)]
def herm_sig(M):
    M=[r[:] for r in M]; nn=len(M); pos=neg_=0; idx=list(range(nn))
    assert all(M[i][j]==conj(M[j][i]) for i in range(nn) for j in range(nn)),'not Hermitian'
    while idx:
        p=next((i for i in idx if not isz(M[i][i])),None)
        if p is None:
            pr=next(((i,j) for i in idx for j in idx if i!=j and not isz(M[i][j])),None)
            if pr is None: break
            i,j=pr
            for c in [ONE,(F(0),F(1))]:
                d=add(add(M[i][i],mul(mul(c,conj(c)),M[j][j])),add(mul(conj(c),M[i][j]),mul(c,M[j][i])))
                if not isz(d): break
            # row/col i += c * row/col j  (congruence by E = I + c e_i e_j^T style)
            for k in range(nn): M[i][k]=add(M[i][k],mul(c,M[j][k]))
            for k in range(nn): M[k][i]=add(M[k][i],mul(conj(c),M[k][j]))
            p=i
        d=M[p][p]; assert d[1]==0
        if d[0]>0: pos+=1
        else: neg_+=1
        for i in idx:
            if i==p or isz(M[i][p]): continue
            f=mul(M[i][p],inv(d))
            for k in range(nn): M[i][k]=sub(M[i][k],mul(f,M[p][k]))
            for k in range(nn): M[k][i]=sub(M[k][i],mul(conj(f),M[k][p]))
        idx.remove(p)
    return (pos,neg_,nn-pos-neg_)
sigs=[herm_sig(beta(N)) for N in Ns]
for r,sg in zip(recs,sigs): r['sig']=sg
semi=all(sg[0]==0 for sg in sigs) or all(sg[1]==0 for sg in sigs)
tot=beta(Ns[0])
for N in Ns[1:]: tot=[[add(a,b) for a,b in zip(r,s)] for r,s in zip(tot,beta(N))]
tsig=herm_sig(tot)
say('(H3) beta signatures (pos,neg,zero) on H:',[sg for sg in sigs])
say(f'(H3) common-sign semidefinite: {semi}; sum signature {tsig} -> definite on H/I: {tsig[2]==dI and (tsig[0]==0 or tsig[1]==0) and tsig[0]+tsig[1]==dH-dI}')
# H4
flat=[[q for row in N for x in row for q in (x[0],x[1])] for N in Ns]
from fractions import Fraction
def qrank(rows):
    M=[r[:] for r in rows]; rk=0; col=0; ncol=len(M[0])
    for c in range(ncol):
        p=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[x-f*y for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk
say('(H4) Q-span rank of the 9 N_j =',qrank(flat))
# relation N_[3,19] = 2 N_[1,2]
# Q-relations among N_j (left kernel)
rel=nullspace([[(F(flat[j][c]),F(0)) for j in range(9)] for c in range(len(flat[0]))],9)
say('Q-relation space dim =',len(rel),'; relations:',[[str(x[0]) for x in r_] for r_ in rel])
# P3 factorization through tau (ChatGPT §5 lemma): tau N_j = 0 and S(x,Nhat y) = -d h(P F_J tau x, P F_J tau y)
def tau_vals(v): return [vadd(v[2*i],mv(S_[i],v[2*i+1])) for i in range(6)]
tauN=True
for r in recs:
    for j in range(dH):
        col=[r['N'][i][j] for i in range(dH)]
        x=[Z]*LS.N
        for i in range(dH): x=vadd(x,vsc(col[i],H[i]))
        if not all(isz(c) for t in tau_vals(LS.values(x)) for c in t): tauN=False
say('tau N_j = 0 for all 9 curves:',tauN)
open(f'/home/claude/g34/h4sel/g333scan/reconstruct_{NAME}_out.txt','w').write('\n'.join(OUT)+'\n')
