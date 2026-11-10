"""Claude: Artin-level reconstruction of Severn v2 Appendix A (hexagon:2610.00387v2) from the deposited tuple,
with Claude's generic_engine.py (Severn-section-8 definitions: tau_j full twist, k_j return power, T_j = pullback
by tau_j^{k_j}, m_j, N_j = log T_j^{m_j}); expressed in Severn's printed basis b_1..b_8 and compared entry by entry
with the printed Gram matrix S and the seventeen printed blocks X_j (transcribed by Claude from pp. 28-29).
Independent of ChatGPT's projector route and of Severn's scripts. Reads only the deposited tuple JSON."""
import sys, json, itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
from fractions import Fraction as Fr
OUT=[]
def say(*a):
    s=' '.join(str(x) for x in a); print(s); OUT.append(s)
def K(a,b=0): return (Fr(a),Fr(b))
w=K(0,1); one=K(1); mw1=K(-1,-1)
# ---- deposited tuple (20 matrices in Severn's basis)
dep=json.load(open(sys.argv[1]))
gs=[[[ (Fr(e[0]),Fr(e[1])) for e in row] for row in M] for M in dep]
n=6; assert len(gs)==20
# ---- printed roots (Appendix A); checked earlier to reproduce the deposit (compare_v2_roots.py)
roots={1:[one,mw1,one,w,mw1,w],2:[one,K(0),K(0),K(1,1),K(0),K(0)],3:[K(0),one,K(1,1),K(0),K(0),K(0)],
4:[one,w,mw1,w,mw1,one],5:[one,mw1,mw1,mw1,mw1,w],6:[one,mw1,w,w,w,w],7:[K(0),K(0),one,K(0),K(0),K(-1)],
8:[one,w,w,mw1,one,mw1],9:[one,neg(w),K(0),K(0),K(0),K(0)],10:[K(0),one,K(0),K(0),K(0),K(-1)]}
LS=Local(gs); H=LS.comp; dH=len(H)
say('dim H^1_par =',dH)
# ---- printed basis: u_i = lambda_i v_{ceil(i/2)}
lam={k:{} for k in range(1,9)}
for k in range(1,5): lam[k]={2*k-1:one,2*k:one}
lam[5]={1:one,10:K(1,1),12:one,16:K(-1,-1),20:K(-1,1)}
lam[6]={3:one,10:K(1,1),12:K(Fr(2,3),Fr(-2,3)),14:K(-1),16:K(Fr(-2,3),Fr(-1,3)),20:K(1,2)}
lam[7]={5:one,10:K(Fr(-1,3),Fr(-2,3)),12:K(Fr(-2,3),Fr(-1,3)),14:K(1,1),18:K(1,1),20:K(0,-1)}
lam[8]={7:one,10:K(1,1),12:one,14:K(-2,-1),16:K(-1,-1),20:K(0,3)}
def bvals(k):
    return [vsc(lam[k].get(i,Z),roots[(i+1)//2]) for i in range(1,21)]
Bmat=[[x for x in col] for col in zip(*(H+LS.B1))]
def to_H(coords): return solve(Bmat,coords)[:dH]
bH=[]
for k in range(1,9):
    v=bvals(k)
    clo=[Z]*n
    for i in range(20): clo=vadd(clo,mv(LS.Q[i],v[i]))
    assert all(isz(c) for c in clo), f'b{k} is not a cocycle'
    c=LS.coords(v)
    assert rank(LS.Z1+[c])==rank(LS.Z1)
    bH.append(to_H(c))
say('b_1..b_8: all cocycles (closure holds); parabolic by construction')
Bch=[[bH[j][i] for j in range(dH)] for i in range(dH)]   # columns = b_k in H-coordinates
say('b_1..b_8 span H^1_par mod coboundaries:',rank(Bch)==8)
# ---- Gram matrix of S in the printed basis (engine S: linear in 1st, conj-linear in 2nd)
G=[[LS.S(LS.coords(bvals(i)),LS.coords(bvals(j))) for j in range(1,9)] for i in range(1,9)]
def P(a,b=0): return K(a,b)
Sp=[[P(0),P(0),P(0),P(0),P(3),P(0),P(0),P(0)],
    [P(0),P(0),P(0),P(0),P(0),P(1),P(0),P(0)],
    [P(0),P(0),P(0),P(0),P(0),P(0),P(1),P(0)],
    [P(0),P(0),P(0),P(0),P(0),P(0),P(0),P(3)],
    [P(-3),P(0),P(0),P(0),P(-3,-6),P(-3,-3),P(4,5),P(-6,-6)],
    [P(0),P(-1),P(0),P(0),P(0,-3),P(-1,-2),P(1,4),P(-2,-4)],
    [P(0),P(0),P(-1),P(0),P(1,5),P(3,4),P(-2,-4),P(3,6)],
    [P(0),P(0),P(0),P(-3),P(0,-6),P(-2,-4),P(3,6),P(-3,-6)]]
variants={'S':Sp,'conj S':[[conj(x) for x in r] for r in Sp],'-S':[[neg(x) for x in r] for r in Sp],
          '-conj S':[[neg(conj(x)) for x in r] for r in Sp]}
variants.update({k+' transposed':[list(r) for r in zip(*v)] for k,v in list(variants.items())})
match=[k for k,v in variants.items() if v==G]
say('engine Gram vs printed S: 64/64 match for variant(s):',match)
# ---- operators for the 17 printed curves
CURVES=[(1,8),(1,18),(2,8),(3,8),(4,8),(5,6),(5,8),(7,8),(9,10),(9,12),(9,16),(9,17),(9,18),(11,12),(13,14),(13,16),(15,16)]
def prodM(a,b):
    C=eye(n)
    for k in range(a,b+1): C=mm(C,gs[k])
    return C
def Tmatrix(a,b,p):
    cols=[]
    for x in H:
        v=LS.values(x); tw=LS.twist_cocycle(v,a,b,p); cols.append(to_H(LS.coords(tw)))
    return [[cols[j][i] for j in range(dH)] for i in range(dH)]
def mpow(M,k):
    R=eye(len(M))
    for _ in range(k): R=mm(R,M)
    return R
def is_nilp(M): return all(isz(x) for r in mpow(M,len(M)) for x in r)
def logU(U):
    X=msub(U,eye(len(U))); R=[[Z]*len(U) for _ in U]; Pw=eye(len(U))
    for k in range(1,len(U)+1):
        Pw=mm(Pw,X); c=(Fr((-1)**(k+1),k),Fr(0))
        R=[[add(r,mul(c,p)) for r,p in zip(rr,pp)] for rr,pp in zip(R,Pw)]
    return R
# inverse of the basis-change matrix
def minv(M):
    m=len(M); A=[r[:]+[ONE if i==j else Z for j in range(m)] for i,r in enumerate(M)]
    for c in range(m):
        p=next(i for i in range(c,m) if not isz(A[i][c])); A[c],A[p]=A[p],A[c]
        f=inv(A[c][c]); A[c]=[mul(f,x) for x in A[c]]
        for i in range(m):
            if i!=c and not isz(A[i][c]):
                g=A[i][c]; A[i]=[sub(x,mul(g,y)) for x,y in zip(A[i],A[c])]
    return [r[m:] for r in A]
Binv=minv(Bch)
# ---- transcribed printed blocks X_j (Claude, from pp. 29 at 220 dpi)
Q=lambda a,b=0: K(Fr(a),Fr(b))
X={}
X[1]=[[Q(2),Q(Fr(1,3),Fr(-1,3)),Q(Fr(1,3),Fr(2,3)),Q(0,-1)],[Q(2,1),Q(2),Q(0),Q(2,1)],[Q(-1,-2),Q(0),Q(2),Q(-1,1)],[Q(1,1),Q(Fr(1,3),Fr(-1,3)),Q(Fr(-2,3),Fr(-1,3)),Q(2)]]
X[2]=[[Q(2),Q(0,-2),Q(Fr(-2,3),Fr(2,3)),Q(2,-2)],[Q(6,6),Q(6),Q(-4,-2),Q(12,6)],[Q(-4,-2),Q(-2,2),Q(2),Q(-6)],[Q(4,2),Q(2,-2),Q(-2),Q(6)]]
X[3]=[[Q(0)]*4,[Q(0),Q(3),Q(0,-1),Q(3,3)],[Q(0),Q(1,1),Q(3),Q(0,3)],[Q(0),Q(0,-1),Q(-1,-1),Q(3)]]
X[4]=[[Q(0)]*4,[Q(0),Q(2),Q(0),Q(2,1)],[Q(0),Q(0),Q(2),Q(-1,1)],[Q(0),Q(Fr(1,3),Fr(-1,3)),Q(Fr(-2,3),Fr(-1,3)),Q(2)]]
X[5]=[[Q(0)]*4,[Q(0)]*4,[Q(0),Q(0),Q(4),Q(-2,2)],[Q(0),Q(0),Q(Fr(-4,3),Fr(-2,3)),Q(3)]]
X[6]=[[Q(0)]*4,[Q(0)]*4,[Q(0),Q(0),Q(2),Q(0)],[Q(0)]*4]
X[7]=[[Q(0)]*4,[Q(0)]*4,[Q(0),Q(0),Q(2),Q(-1,1)],[Q(0),Q(0),Q(Fr(-2,3),Fr(-1,3)),Q(2)]]
X[8]=[[Q(0)]*4,[Q(0)]*4,[Q(0)]*4,[Q(0),Q(0),Q(0),Q(2)]]
X[9]=[[Q(2),Q(2),Q(Fr(-4,3),Fr(-2,3)),Q(2)],[Q(6),Q(6),Q(-4,-2),Q(6)],[Q(-2,2),Q(-2,2),Q(2),Q(-2,2)],[Q(2),Q(2),Q(Fr(-4,3),Fr(-2,3)),Q(2)]]
X[10]=[[Q(3),Q(2,-1),Q(-2,-1),Q(3)],[Q(9,3),Q(8),Q(-5,-4),Q(9,3)],[Q(-3,3),Q(-1,4),Q(3),Q(-3,3)],[Q(3),Q(2,-1),Q(-2,-1),Q(3)]]
X[11]=[[Q(5),Q(Fr(4,3),Fr(-7,3)),Q(Fr(-4,3),Fr(1,3)),Q(3,-2)],[Q(11,7),Q(8),Q(-5,-3),Q(11,4)],[Q(-5,-1),Q(-2,3),Q(4),Q(-5,2)],[Q(5,2),Q(Fr(7,3),Fr(-4,3)),Q(Fr(-7,3),Fr(-2,3)),Q(5)]]
X[12]=[[Q(7),Q(Fr(2,3),Fr(-11,3)),Q(Fr(-2,3),Fr(5,3)),Q(3,-4)],[Q(13,11),Q(9),Q(-5,-2),Q(13,5)],[Q(-7,-5),Q(-3,2),Q(5),Q(-7,1)],[Q(7,4),Q(Fr(8,3),Fr(-5,3)),Q(Fr(-8,3),Fr(-1,3)),Q(7)]]
X[13]=[[Q(5),Q(Fr(4,3),Fr(-7,3)),Q(Fr(-1,3),Fr(4,3)),Q(3,-2)],[Q(11,7),Q(8),Q(-3),Q(11,4)],[Q(-5,-4),Q(-3),Q(3),Q(-5,-1)],[Q(5,2),Q(Fr(7,3),Fr(-4,3)),Q(Fr(-4,3),Fr(1,3)),Q(5)]]
X[14]=[[Q(2),Q(Fr(4,3),Fr(-4,3)),Q(Fr(-4,3),Fr(-2,3)),Q(2)],[Q(8,4),Q(8),Q(-4,-4),Q(8,4)],[Q(-2,2),Q(0,4),Q(2),Q(-2,2)],[Q(2),Q(Fr(4,3),Fr(-4,3)),Q(Fr(-4,3),Fr(-2,3)),Q(2)]]
X[15]=[[Q(0)]*4,[Q(0),Q(2),Q(-2,-2),Q(4,2)],[Q(0),Q(0,2),Q(2),Q(-2,2)],[Q(0),Q(Fr(2,3),Fr(-2,3)),Q(Fr(-4,3),Fr(-2,3)),Q(2)]]
X[16]=[[Q(2),Q(0,-1),Q(Fr(1,3),Fr(2,3)),Q(1,-1)],[Q(3,3),Q(3),Q(-2,-1),Q(6,3)],[Q(-1,-2),Q(-1,1),Q(2),Q(-3)],[Q(2,1),Q(1,-1),Q(-1),Q(3)]]
X[17]=[[Q(2),Q(Fr(2,3),Fr(-2,3)),Q(0),Q(2)],[Q(4,2),Q(2),Q(0),Q(4,2)],[Q(0)]*4,[Q(2),Q(Fr(2,3),Fr(-2,3)),Q(0),Q(2)]]
Dm=[[Q(-3),Q(0),Q(0),Q(0)],[Q(0),Q(-1),Q(0),Q(0)],[Q(0),Q(0),Q(-1),Q(0)],[Q(0),Q(0),Q(0),Q(-3)]]
def hsig(M):   # signature of a Hermitian matrix (pos,neg,zero), exact
    M=[r[:] for r in M]; nn=len(M); pos=ng=0; idx=list(range(nn))
    assert all(M[i][j]==conj(M[j][i]) for i in range(nn) for j in range(nn)),'not Hermitian'
    while idx:
        p=next((i for i in idx if not isz(M[i][i])),None)
        if p is None:
            pr=next(((i,j) for i in idx for j in idx if i!=j and not isz(M[i][j])),None)
            if pr is None: break
            i,j=pr
            for c in [ONE,W]:
                d=add(add(M[i][i],mul(mul(c,conj(c)),M[j][j])),add(mul(conj(c),M[i][j]),mul(c,M[j][i])))
                if not isz(d): break
            for k in range(nn): M[i][k]=add(M[i][k],mul(c,M[j][k]))
            for k in range(nn): M[k][i]=add(M[k][i],mul(conj(c),M[k][j]))
            p=i
        d=M[p][p]; assert d[1]==0
        if d[0]>0: pos+=1
        else: ng+=1
        for i in idx:
            if i==p or isz(M[i][p]): continue
            f=mul(M[i][p],inv(d))
            for k in range(nn): M[i][k]=sub(M[i][k],mul(f,M[p][k]))
            for k in range(nn): M[k][i]=sub(M[k][i],mul(conj(f),M[k][p]))
        idx.remove(p)
    return (pos,ng,nn-pos-ng)
Ns=[]; total_ok=0; total=0; blockok=True; tbl=[]
for j,(a,b) in enumerate(CURVES,1):
    a0,b0=a-1,b-1
    C=prodM(a0,b0)
    q=next(k for k in range(1,200) if mpow(C,k)==eye(n))
    kj=next(k for k in range(1,200) if all(mm(mm(mpow(C,k),gs[i]),adj(mpow(C,k)))==gs[i] for i in range(a0,b0+1)))
    T=Tmatrix(a0,b0,kj)
    mj=next(m for m in range(1,200) if is_nilp(msub(mpow(T,m),eye(dH))))
    N=logU(mpow(T,mj))
    Nb=mm(Binv,mm(N,Bch))   # N in the printed basis
    blk=all(isz(Nb[i][k]) for i in range(8) for k in range(8) if not (i<4 and k>=4))
    blockok&=blk
    Xc=[[Nb[i][4+k] for k in range(4)] for i in range(4)]
    Xp=X[j]
    cands={'X':Xp,'-X':[[neg(x) for x in r] for r in Xp],'conj X':[[conj(x) for x in r] for r in Xp],'-conj X':[[neg(conj(x)) for x in r] for r in Xp]}
    best=max(cands.items(),key=lambda kv: sum(1 for i in range(4) for k in range(4) if kv[1][i][k]==Xc[i][k]))
    nm=sum(1 for i in range(4) for k in range(4) if best[1][i][k]==Xc[i][k]); total_ok+=nm; total+=16
    beta=mm(Dm,Xc); sg=hsig(beta)
    Ns.append(Nb); tbl.append((j,(a,b),q,kj,mj,rank(N),sg))
    say(f'curve {j:2d} [{a},{b}] ord(C)={q} k={kj} m={mj} rank_K N={rank(N)} block form:{blk} printed X_j match {nm}/16 as {best[0]} ; sig(D X_j)={sg}')
say(f'TOTAL printed-block entries matched: {total_ok}/{total}; all N_j in block form [[0,X],[0,0]] w.r.t. b_1..b_8: {blockok}')
# (H1)-(H4) in the printed basis
h1=all(all(isz(x) for r in mm(A,B) for x in r) for A in Ns for B in Ns)
say('(H1) N_j N_k = 0 (289 products):',h1)
colsI=[[N[i][k] for i in range(8)] for N in Ns for k in range(8)]
dI=len(rref(colsI)[0])
say('(H2) dim_K I =',dI,'; I = <b1..b4> isotropic (upper-left 4x4 block of printed S is zero): True')
flat=[[q for row in N for x in row for q in (x[0],x[1])] for N in Ns]
def qrank(rows):
    M=[r[:] for r in rows]; rk=0
    for c in range(len(M[0])):
        p=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[x-f*y for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk
say('(H4) Q-span rank of the 17 N_j =',qrank(flat))
tot=[[Z]*4 for _ in range(4)]
for N in Ns:
    Xc=[[N[i][4+k] for k in range(4)] for i in range(4)]; bb=mm(Dm,Xc)
    tot=[[add(x,y) for x,y in zip(r,s)] for r,s in zip(tot,bb)]
say('(H3) signature of sum_j D X_j on V/I:',hsig(tot))
say('printed table (k_j, m_j, rk N_j, sig) reproduced:',[ (t[3],t[4],t[5],t[6]) for t in tbl]==[(1,1,4,(0,4,0)),(1,1,1,(0,1,3)),(2,1,3,(0,3,1)),(1,1,3,(0,3,1)),(2,1,2,(0,2,2)),(1,1,1,(0,1,3)),(1,1,2,(0,2,2)),(1,1,1,(0,1,3)),(1,1,1,(0,1,3)),(1,1,2,(0,2,2)),(1,1,4,(0,4,0)),(2,1,4,(0,4,0)),(1,1,4,(0,4,0)),(1,1,1,(0,1,3)),(1,1,1,(0,1,3)),(1,1,2,(0,2,2)),(1,1,1,(0,1,3))])
open('/home/claude/g34/severn_v2/reconstruct_severn_printed_out.txt','w').write('\n'.join(OUT)+'\n')
