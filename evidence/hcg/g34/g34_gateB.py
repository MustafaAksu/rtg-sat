#!/usr/bin/env python3
"""G34-B/C (Claude): exact parabolic cohomology of the reflection local system of G34 on P^1 minus 20 points,
cup form, Dehn-twist monodromy and Severn's (H0)-(H4) for OUR OWN paired tuple and OUR OWN pants
decomposition. No Severn code/tuple/certificate is used; only definitions.

Model (derived independently, see report §2):
  pi = <g_1..g_r | g_1...g_r = 1>, rho(g_i) = s_i (reflections, unitary for h_W(x,y) = sum x_k conj(y_k)).
  Parabolic cocycle u: u(g_i) = a_i v_i  (im(s_i - 1) = K v_i), closure sum_i Q_i u(g_i) = 0, Q_i = s_1...s_{i-1}.
  Coboundary: u(g) = (rho(g)-1) w.
  Relative lift alpha_i with u(g_i) = (s_i - 1) alpha_i:  alpha_i = -(a_i/2) v_i.
  Cup form (relative fundamental class Z = sum_k [P_{k-1} | g_k], dZ = sum_k [g_k]):
     S(u,u') = sum_k h_W(u(P_{k-1}), P_{k-1} u'(g_k)) - sum_k h_W(alpha_k, u'(g_k)).
  Well-definedness on H^1_par is checked numerically below.
Dehn twist along a curve enclosing consecutive points a..b: phi(g_i) = c g_i c^-1 (a<=i<=b), c = g_a...g_b;
T_j = (u -> u o phi^k) with k the exact return power (rho o phi^k = rho)."""
import json, hashlib, itertools, sys
from fractions import Fraction as Fr

# ---------------- exact Q(w), w^2 = -1 - w ; element (a,b) = a + b w
def K(a,b=0): return (Fr(a),Fr(b))
Z0=K(0); ONE=K(1); W=K(0,1); THETA=K(1,2)   # theta = sqrt(-3)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): a,b=x; c,d=y; return (a*c-b*d, a*d+b*c-b*d)
def conj(x): a,b=x; return (a-b,-b)
def nrm(x): a,b=x; return a*a-a*b+b*b
def inv(x): n=nrm(x); c=conj(x); return (c[0]/n,c[1]/n)
def div(x,y): return mul(x,inv(y))
def iszero(x): return x[0]==0 and x[1]==0
def is_rational(x): return x[1]==0
# vectors / matrices
def vadd(u,v): return [add(a,b) for a,b in zip(u,v)]
def vsub(u,v): return [sub(a,b) for a,b in zip(u,v)]
def vscale(c,u): return [mul(c,a) for a in u]
def hW(x,y):
    s=Z0
    for a,b in zip(x,y): s=add(s,mul(a,conj(b)))
    return s
def matvec(M,x): return [ (lambda row: __import__('functools').reduce(add,[mul(m,v) for m,v in zip(row,x)],Z0))(row) for row in M]
def matmul(A,B):
    n,m,p=len(A),len(B),len(B[0])
    return [[__import__('functools').reduce(add,[mul(A[i][k],B[k][j]) for k in range(m)],Z0) for j in range(p)] for i in range(n)]
def eye(n): return [[ONE if i==j else Z0 for j in range(n)] for i in range(n)]
def matsub(A,B): return [[sub(a,b) for a,b in zip(r,s)] for r,s in zip(A,B)]
def matadd(A,B): return [[add(a,b) for a,b in zip(r,s)] for r,s in zip(A,B)]
def matscale(c,A): return [[mul(c,a) for a in r] for r in A]
def iszeromat(A): return all(iszero(a) for r in A for a in r)

def rref(M):
    """returns (R, pivots) reduced row echelon over K"""
    R=[list(r) for r in M]; piv=[]; row=0
    ncol=len(R[0]) if R else 0
    for col in range(ncol):
        p=next((i for i in range(row,len(R)) if not iszero(R[i][col])),None)
        if p is None: continue
        R[row],R[p]=R[p],R[row]
        iv=inv(R[row][col]); R[row]=[mul(iv,a) for a in R[row]]
        for i in range(len(R)):
            if i!=row and not iszero(R[i][col]):
                f=R[i][col]; R[i]=[sub(a,mul(f,b)) for a,b in zip(R[i],R[row])]
        piv.append(col); row+=1
        if row==len(R): break
    return R,piv
def rank(M): return len(rref(M)[1]) if M else 0
def nullspace(M,ncol):
    if not M: return [[ONE if i==j else Z0 for i in range(ncol)] for j in range(ncol)]
    R,piv=rref(M); free=[c for c in range(ncol) if c not in piv]; basis=[]
    for f in free:
        v=[Z0]*ncol; v[f]=ONE
        for r,pc in enumerate(piv): v[pc]=neg(R[r][f])
        basis.append(v)
    return basis

# ---------------- the group data (our own G34-A output)
import os
dat=json.load(open(os.environ.get('ROOTS_JSON','g34_gateA.json')))
roots=[[K(a,b) for a,b in v] for v in dat['generating_reflection_roots']]
def refl(v):  # s_v = I - (2/h(v,v)) v v^*
    hv=hW(v,v); c=div(K(2),hv)
    return [[sub(ONE if i==j else Z0, mul(c,mul(v[i],conj(v[j])))) for j in range(6)] for i in range(6)]
S_ref=[refl(v) for v in roots]
for M,v in zip(S_ref,roots):
    assert iszeromat(matsub(matmul(M,M),eye(6)))
    assert all(iszero(a) for a in vadd(matvec(M,v),v))
r=20
tup=[i//2 for i in range(r)]            # paired tuple (s1,s1,...,s10,s10): index of reflection
G=[S_ref[t] for t in tup]; V=[roots[t] for t in tup]
Q=[eye(6)]
for i in range(1,r): Q.append(matmul(Q[-1],G[i-1]))
assert iszeromat(matsub(matmul(Q[-1],G[-1]),eye(6))), "tuple product must be 1"
log=[]
def say(*a):
    s=" ".join(str(x) for x in a); print(s); log.append(s)

# ---------------- cocycles: coordinate a in K^20, u(g_i) = a_i v_i
def u_gen(a): return [vscale(a[i],V[i]) for i in range(r)]
closure=[[ mul(row_i, a) for a in [ONE] ] for row_i in []]
Cl=[]   # 6 x 20 matrix: sum_i Q_i v_i a_i = 0
QV=[matvec(Q[i],V[i]) for i in range(r)]
Cl=[[QV[i][k] for i in range(r)] for k in range(6)]
Bmat=[]  # coboundary: a_i = coefficient of (s_i - 1) w along v_i = -2 h(w,v_i)/h(v_i,v_i)
for k in range(6):
    w=[Z0]*6; w[k]=ONE
    Bmat.append([ div(neg(mul(K(2),hW(w,V[i]))), hW(V[i],V[i])) for i in range(r)])
rk_cl=rank(Cl); rk_cb=rank(Bmat)
Zbasis=nullspace(Cl,r)
say("closure rank =",rk_cl," coboundary rank =",rk_cb," dim Z_par =",len(Zbasis)," dim H1_par =",len(Zbasis)-rk_cb)
assert all(all(iszero(x) for x in matvec(Cl,b)) for b in Bmat)   # coboundaries are cocycles

# quotient coordinates: choose complement of B inside Z
Brows,_=rref(Bmat); Brows=[b for b in Brows if any(not iszero(x) for x in b)]
comp=[]; cur=list(Brows)
for z in Zbasis:
    if rank(cur+[z])>rank(cur): cur.append(z); comp.append(z)
assert len(comp)==8
def coords(a):
    """write cocycle a = sum c_j comp_j + (coboundary); return c (8)"""
    basis=comp+Brows  # 14 vectors in K^20
    M=[[basis[j][i] for j in range(len(basis))]+[a[i]] for i in range(r)]
    R,piv=rref(M); assert len(basis) not in piv, "not in Z_par"
    c=[Z0]*len(basis)
    for row,pc in enumerate(piv): c[pc]=R[row][-1]
    return c[:8]

# ---------------- cup form
def u_of_prefix(ug,k):   # u(P_k) = sum_{j<k} Q_j u(g_j), P_k = g_1...g_k
    s=[Z0]*6
    for j in range(k): s=vadd(s,matvec(Q[j],ug[j]))
    return s
def Sform(a,b):
    ua,ub=u_gen(a),u_gen(b); tot=Z0
    for k in range(r):
        tot=add(tot,hW(u_of_prefix(ua,k), matvec(Q[k],ub[k])))
        alpha=vscale(neg(div(a[k],K(2))),V[k])
        tot=sub(tot,hW(alpha,ub[k]))
    return tot
# well-definedness: S(coboundary, z) = 0 = S(z, coboundary) for all z in Z
wd=all(iszero(Sform(b,z)) and iszero(Sform(z,b)) for b in Bmat for z in Zbasis)
say("S vanishes on coboundaries (both slots):",wd)
Sg=[[Sform(x,y) for y in comp] for x in comp]
skew=all(iszero(add(Sg[i][j],conj(Sg[j][i]))) for i in range(8) for j in range(8))
say("S skew-Hermitian on H1_par:",skew,"  nondegenerate:",rank(Sg)==8)
Hg=[[mul(THETA,x) for x in row] for row in Sg]        # h = theta S
herm=all(iszero(sub(Hg[i][j],conj(Hg[j][i]))) for i in range(8) for j in range(8))

def herm_signature(H):
    """congruence diagonalization of a Hermitian K-matrix; returns (pos,neg,zero), diag list, det"""
    H=[list(r) for r in H]; n=len(H); diag=[]
    idxs=list(range(n))
    while idxs:
        p=next((i for i in idxs if not iszero(H[i][i])),None)
        if p is None:
            pair=next(((i,j) for i in idxs for j in idxs if i<j and not iszero(H[i][j])),None)
            if pair is None: diag+= [Fr(0)]*len(idxs); break
            i,j=pair
            for t in (ONE,THETA):           # e_i <- e_i + t e_j makes diagonal nonzero for some t
                hii=add(add(H[i][i],mul(H[i][j],conj(t))),add(mul(t,H[j][i]),mul(mul(t,conj(t)),H[j][j])))
                if not iszero(hii): break
            # row/col operation
            H[i]=[add(H[i][k],mul(t,H[j][k])) for k in range(n)]
            for k in range(n): H[k][i]=add(H[k][i],mul(H[k][j],conj(t)))
            p=i
        d=H[p][p]; assert is_rational(d); diag.append(d[0])
        for k in idxs:
            if k==p or iszero(H[k][p]): continue
            f=div(H[k][p],d)
            H[k]=[sub(H[k][m],mul(f,H[p][m])) for m in range(n)]
            for m in range(n): H[m][k]=sub(H[m][k],mul(H[m][p],conj(f)))
        idxs.remove(p)
    pos=sum(1 for x in diag if x>0); negc=sum(1 for x in diag if x<0); z=sum(1 for x in diag if x==0)
    det=Fr(1)
    for x in diag: det*=x
    return (pos,negc,z),diag,det
sig,diag,det=herm_signature(Hg)
say("h = theta*S Hermitian:",herm," signature (pos,neg,zero) =",sig," det(h) =",det)

def is_norm_QK(q):
    """q in Q_{>0}: norm from Q(sqrt-3) iff every prime = 2 mod 3 has even valuation"""
    if q<=0: return False
    from sympy import factorint
    for p,e in list(factorint(q.numerator).items())+list(factorint(q.denominator).items()):
        if p%3==2 and e%2: return False
    return True
say("discriminant class: det(h) =",det," -> split [1] (norm, n=4 even):",is_norm_QK(det))

# ---------------- Dehn twists
def word_u(ug,word):
    """u(word) and rho(word) for a word = list of (index, +-1) in the generators"""
    u=[Z0]*6; R=eye(6)
    for i,e in word:
        if e==1: ui=ug[i]; Ri=G[i]
        else: Ri=G[i]; ui=vscale(K(-1),matvec(Ri,ug[i]))  # s_i^-1 = s_i; u(g^-1) = -g^-1 u(g)
        u=vadd(u,matvec(R,ui)); R=matmul(R,Ri)
    return u,R
def twist_word(a_,b_,i,k):
    c=[(j,1) for j in range(a_,b_+1)]; cinv=[(j,-1) for j in range(b_,a_-1,-1)]
    return c*k+[(i,1)]+cinv*k
def return_power(a_,b_,kmax=60):
    C=eye(6)
    for j in range(a_,b_+1): C=matmul(C,G[j])
    Ck=eye(6)
    for k in range(1,kmax+1):
        Ck=matmul(Ck,C); Cki=None
        # C^k g_i C^-k = g_i  <=> C^k commutes with g_i
        if all(iszeromat(matsub(matmul(Ck,G[i]),matmul(G[i],Ck))) for i in range(a_,b_+1)): return k,C
    return None,C
def T_matrix(a_,b_,k):
    C=eye(6)
    for j in range(a_,b_+1): C=matmul(C,G[j])
    Ck=matpow(C,k)
    cols=[]
    for z in comp:
        ug=u_gen(z)
        uc=[Z0]*6; R=eye(6)
        for j in range(a_,b_+1): uc=vadd(uc,matvec(R,ug[j])); R=matmul(R,G[j])
        uck=[Z0]*6; Ct=eye(6)
        for t in range(k): uck=vadd(uck,matvec(Ct,uc)); Ct=matmul(Ct,C)
        new=[]
        for i in range(r):
            if a_<=i<=b_:
                # C^k g_i C^-k = g_i (exact return), so last term is g_i u(c^k)
                ui=vsub(vadd(uck,matvec(Ck,ug[i])),matvec(G[i],uck))
            else: ui=ug[i]
            vi=V[i]; j=next(t for t in range(6) if not iszero(vi[t]))
            ai=div(ui[j],vi[j]); assert all(iszero(x) for x in vsub(ui,vscale(ai,vi))), "not parabolic"
            new.append(ai)
        cols.append(coords(new))
    return [[cols[j][i] for j in range(8)] for i in range(8)]
def matpow(A,m):
    R=eye(len(A))
    for _ in range(m): R=matmul(R,A)
    return R
def nilpotent(A):
    return iszeromat(matpow(A,len(A)))
def mlog_unipotent(U):
    X=matsub(U,eye(len(U))); L=[[Z0]*len(U) for _ in U]; P=eye(len(U))
    for k in range(1,len(U)+1):
        P=matmul(P,X)
        L=matadd(L,matscale(K(Fr((-1)**(k+1),k)),P))
    return L

def run_decomposition(curves,label):
    say(f"\n--- decomposition {label}: {len(curves)} curves (1-based intervals)")
    Ns=[]; rows=[]
    for (a1,b1) in curves:
        a_,b_=a1-1,b1-1
        k,C=return_power(a_,b_)
        T=T_matrix(a_,b_,k)
        m=next(m for m in range(1,13) if nilpotent(matsub(matpow(T,m),eye(8))))
        N=mlog_unipotent(matpow(T,m))
        Ns.append(N); rows.append((a1,b1,k,m,rank(N)))
    # H1
    H1=all(iszeromat(matmul(A,B)) for A in Ns for B in Ns)
    # H2
    imgs=[]
    for N in Ns:
        cols=[[N[i][j] for i in range(8)] for j in range(8)]
        imgs+= [c for c in cols if any(not iszero(x) for x in c)]
    Ir,_=rref(imgs) if imgs else ([],[])
    Ibasis=[v for v in Ir if any(not iszero(x) for x in v)]
    dimI=len(Ibasis)
    def Sv(x,y):  # S on coordinate vectors
        s=Z0
        for i in range(8):
            for j in range(8): s=add(s,mul(mul(x[i],Sg[i][j]),conj(y[j])))
        return s
    iso=all(iszero(Sv(x,y)) for x in Ibasis for y in Ibasis)
    killI=all(all(iszero(t) for t in matvec(N,x)) for N in Ns for x in Ibasis)
    H2=(dimI==4) and iso and killI
    # H3: beta_j(x,y) = S(x, N_j y) on V/I
    compl=[]; cur=list(Ibasis)
    for e in eye(8):
        if rank(cur+[e])>rank(cur): cur.append(e); compl.append(e)
    E8=eye(8)
    descend=all(iszero(Sv(x,matvec(N,y))) and iszero(Sv(y,matvec(N,x))) for N in Ns for x in Ibasis for y in E8)
    sigs=[]; herm_ok=True; Bsum=[[Z0]*len(compl) for _ in compl]
    for N in Ns:
        Bj=[[Sv(x,matvec(N,y)) for y in compl] for x in compl]
        herm_ok&=all(iszero(sub(Bj[i][j],conj(Bj[j][i]))) for i in range(len(compl)) for j in range(len(compl)))
        sigs.append(herm_signature(Bj)[0]); Bsum=matadd(Bsum,Bj)
    ssum=herm_signature(Bsum)[0]
    semidef_pos=all(s[1]==0 for s in sigs); semidef_neg=all(s[0]==0 for s in sigs)
    definite=(ssum[2]==0) and (ssum[0]==0 or ssum[1]==0)
    H3=herm_ok and descend and (semidef_pos or semidef_neg) and definite and \
       ((semidef_pos and ssum[1]==0) or (semidef_neg and ssum[0]==0))
    # H4: Q-span of the N_j (flatten K entries to Q pairs)
    import flint
    flat=flint.fmpq_mat([[flint.fmpq(c.numerator,c.denominator) for row in N for x in row for c in x] for N in Ns])
    qdim=flat.rank()
    H4=(qdim==16)
    for (a1,b1,k,m,rN),s in zip(rows,sigs):
        say(f"   [{a1:2d},{b1:2d}] k={k} m={m} rkK(N)={rN} sig(beta)={s}")
    say(f"   H1={H1}  dimK(I)={dimI} isotropic={iso} N(I)=0:{killI} -> H2={H2}")
    say(f"   beta Hermitian={herm_ok} descends={descend} sum-signature={ssum} -> H3={H3}")
    say(f"   dimQ span(N_j)={qdim} -> H4={H4}")
    return dict(label=label,curves=curves,rows=rows,H1=H1,H2=H2,H3=H3,H4=H4,dimI=dimI,qspan=qdim,
                sigs=[list(s) for s in sigs],sumsig=list(ssum))

# (H0) for interval pants decompositions: pants = (two children, parent)
def boundary_product(a1,b1):
    C=eye(6)
    for j in range(a1-1,b1): C=matmul(C,G[j])
    return C
def c_sigma(M): return rank(matsub(M,eye(6)))
def fixed_dim_group(mats):
    rows=[]
    for M in mats: rows+=matsub(M,eye(6))
    return 6-rank(rows) if rows else 6
if __name__=='__main__':
    results=[]
    comb=[(2*i-1,2*i) for i in range(1,11)]+[(1,2*k) for k in range(2,9)]
    results.append(run_decomposition(comb,"comb: pairs + [1,4],[1,6],...,[1,16]"))
    balanced=[(2*i-1,2*i) for i in range(1,11)]+[(1,4),(5,8),(9,12),(13,16),(1,8),(9,16),(1,16)]
    results.append(run_decomposition(balanced,"balanced: pairs + [1,4],[5,8],[9,12],[13,16],[1,8],[9,16],[1,16]"))
    # H0 for the comb (pants listed explicitly as boundary intervals; outer = complement)
    def H0_check(pants):
        ok=True
        for P in pants:
            mats=[boundary_product(a,b) for a,b in P]
            val=sum(c_sigma(M) for M in mats)-12+2*fixed_dim_group(mats)
            ok&=(val==0)
        return ok
    say("\n(H0) all pants contributions vanish for both decompositions: boundary products of every curve are 1 "
        "(paired tuple), so each pants with three trivial boundaries gives 0-12+12=0, and each pair-pants (s,s,1) gives 1+1+0-12+2*5=0:",
        H0_check([[(2*i-1,2*i-1),(2*i,2*i),(2*i-1,2*i)] for i in range(1,11)]) and
        all(c_sigma(boundary_product(a,b))==0 for a,b in comb+balanced))
    out={"script_sha256":hashlib.sha256(open(__file__,'rb').read()).hexdigest(),
         "tuple":"paired (s1,s1,...,s10,s10) from g34_gateA.json (Claude's own roots)",
         "dim_H1par":len(comp),"closure_rank":rk_cl,"coboundary_rank":rk_cb,
         "S_well_defined":wd,"S_skew_hermitian":skew,"h_signature":list(sig),"det_h":str(det),
         "split_class":is_norm_QK(det),"decompositions":results,"log":log}
    json.dump(out,open("g34_gateB.json","w"),indent=1,default=str)
