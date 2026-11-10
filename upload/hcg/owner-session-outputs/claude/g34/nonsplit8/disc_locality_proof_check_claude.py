"""Claude: independent exact check of ChatGPT's local determinant formula proof
(HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md, eqs (1)-(5), Sec. 3.5 sign, Sec. 5 rank-2 census).
Uses Claude's own field arithmetic / cocycle engine (generic_engine.py, 66f2c253...) and a GENERAL coefficient
form H0 (not only the identity), so that the (det H0)^2 and N(det P / det H0) terms of (4)-(5) are exercised.
Nothing here imports ChatGPT's code.

Checks per case:
 (1)  det B = prod_i a_i / b_i          (B = extended triangular form on E = (+) E_i)
 (2)  B + B^*  =  Gram of h0(Cx, Cy)      (matrix identity on all of E)
 (3)  B(Dv, y) = -h0(v, Cy),  B(x, Dv) = h0(Cx, v)   for all basis vectors
 rad  rank(B|_Z) = dim Z - d   (radical of B on the closed cochains is exactly D(V))
 (4)  adapted-basis matrix has the block shape [[0,0,-H0],[0,S,A],[H0,B',T]] and det B_ad = det S (det H0)^2
 (5)  det B_ad = N(det P) det B ;  det S / prod(a_i/b_i) = N(det P / det H0)
 3.5  prod_i b_i rational;  [det(theta S)] = [(-1)^n prod a_i b_i]
 S    for H0 = I the middle block equals generic_engine's cup form S on the same representatives (Lemma 7.2 form)
"""
import sys, json, random
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import add, sub, neg, mul, conj, inv, isz, Z, ONE, W, eye, mm, mv, msub, adj, vadd, vsc, rref, nullspace, rank, colspace, solve, Local
from fractions import Fraction as Fr
theta=(Fr(1),Fr(2))                     # 1+2w = sqrt(-3), conj(theta) = -theta
def Kc(p): return (Fr(p[0]),Fr(p[1]))
def inner(x,y,H):                       # h0(x,y) = x^t H conj(y), linear in the first argument
    s=Z
    for i,a in enumerate(x):
        if isz(a): continue
        for j,b in enumerate(y):
            if isz(b) or isz(H[i][j]): continue
            s=add(s,mul(mul(a,H[i][j]),conj(b)))
    return s
def det(M):
    M=[r[:] for r in M]; n=len(M); d=ONE
    for c in range(n):
        p=next((i for i in range(c,n) if not isz(M[i][c])),None)
        if p is None: return Z
        if p!=c: M[c],M[p]=M[p],M[c]; d=neg(d)
        d=mul(d,M[c][c]); f=inv(M[c][c])
        for i in range(c+1,n):
            if not isz(M[i][c]):
                g=mul(M[i][c],f); M[i]=[sub(x,mul(g,y)) for x,y in zip(M[i],M[c])]
    return d
def trans(A): return [list(r) for r in zip(*A)]
def madj(A): return [[conj(x) for x in r] for r in trans(A)]
def madd(A,B): return [[add(x,y) for x,y in zip(r,s)] for r,s in zip(A,B)]
def N(x): return mul(x,conj(x))[0]
def norm_class(q):
    sg='-' if q<0 else ''; q=abs(q); odd=set()
    for n_ in (q.numerator,q.denominator):
        p=2
        while n_>1:
            e=0
            while n_%p==0: n_//=p; e+=1
            if e%2 and p%3==2: odd.add(p)
            p+=1
    return '['+sg+('1' if not odd else '*'.join(map(str,sorted(odd))))+']'
def is_unitary(g,H):
    return mm(mm(trans(g),H),[[conj(x) for x in r] for r in g])==H

def check(gs,H,label,engine_compare=False):
    d=len(H); r=len(gs)
    assert all(is_unitary(g,H) for g in gs), 'not H-unitary'
    P=eye(d)
    for g in gs: P=mm(P,g)
    assert P==eye(d), 'product != 1'
    Q=[eye(d)]
    for g in gs[:-1]: Q.append(mm(Q[-1],g))
    Qinv=[]
    for q in Q:                           # q^{-1} = H^{-1} q^* H  (H-unitary); use exact solve instead
        Qinv.append(trans([solve(q,e) for e in eye(d)]))
    Eb=[colspace(msub(eye(d),g)) for g in gs]        # basis of E_i = im(1-g_i)
    c=[len(e) for e in Eb]; R=sum(c); assert R%2==0
    n2=R-2*d; assert n2%2==0; n=n2//2
    # local data
    a=[]; b=[]
    for g,E in zip(gs,Eb):
        if not E: a.append(ONE); b.append(ONE); continue
        Gram=[[inner(x,y,H) for y in E] for x in E]; a.append(det(Gram))
        A=trans(E); M1=msub(eye(d),g)
        ME=trans([solve(A,mv(M1,x)) for x in E])     # matrix of (1-g)|E in basis E (columns = images)
        b.append(det(ME))
    prod_ab=ONE; prod_a_over_b=ONE; prod_b=ONE
    for ai,bi in zip(a,b):
        prod_ab=mul(prod_ab,mul(ai,bi)); prod_a_over_b=mul(prod_a_over_b,mul(ai,inv(bi))); prod_b=mul(prod_b,bi)
    assert all(ai[1]==0 and ai[0]>0 for ai in a), 'a_i not rational positive'
    assert prod_b[1]==0, 'prod b_i not rational'                       # Sec. 3.5
    # cochain space E, closure C (d x R), coboundary D (R-vectors), B (R x R)
    labels=[(i,j) for i in range(r) for j in range(c[i])]
    cols=[mv(Q[i],Eb[i][j]) for (i,j) in labels]                      # C(e_a) in V
    Cm=trans(cols)                                                     # d x R
    assert rank(Cm)==d, 'C not surjective (common fixed vector?)'
    def Dvec(v):
        out=[]
        for g,E in zip(gs,Eb):
            if E: out+=solve(trans(E),mv(msub(g,eye(d)),v))
        return out
    Dm=[Dvec(e) for e in eye(d)]                                       # d rows of length R
    assert rank(Dm)==d
    assert all(isz(x) for row in mm(Cm,trans(Dm)) for x in row), 'CD != 0'
    # preimages A_i inside E_i
    Apre=[]
    for g,E in zip(gs,Eb):
        if not E: Apre.append([]); continue
        A=trans(E); M1=msub(eye(d),g)
        ME=trans([solve(A,mv(M1,x)) for x in E])
        MEinv=trans([solve(ME,e) for e in eye(len(E))])
        Apre.append([ [Z]*d for _ in E ])
        for j in range(len(E)):
            coef=[MEinv[t][j] for t in range(len(E))]
            v=[Z]*d
            for t,x in enumerate(E): v=vadd(v,vsc(coef[t],x))
            Apre[-1][j]=v
            assert mv(M1,v)==E[j]
    B=[[Z]*R for _ in range(R)]
    for p,(i,ia) in enumerate(labels):
        for q,(j,jb) in enumerate(labels):
            if i==j: B[p][q]=inner(Apre[i][ia],Eb[j][jb],H)
            elif i<j: B[p][q]=inner(mv(Qinv[j],cols[p]),Eb[j][jb],H)   # h0(Q_j^{-1} Q_i x_i, y_j)
    # (1)
    dB=det(B); assert dB==prod_a_over_b, '(1) fails'
    # (2)
    CHC=[[inner(cols[p],cols[q],H) for q in range(R)] for p in range(R)]
    assert madd(B,madj(B))==CHC, '(2) fails'
    # (3)
    def Bf(x,y):
        s=Z
        for p in range(R):
            if isz(x[p]): continue
            for q in range(R):
                if isz(y[q]) or isz(B[p][q]): continue
                s=add(s,mul(mul(x[p],B[p][q]),conj(y[q])))
        return s
    for k,v in enumerate(eye(d)):
        for q in range(R):
            y=[Z]*R; y[q]=ONE
            assert Bf(Dm[k],y)==neg(inner(v,cols[q],H)), '(3a) fails'
            assert Bf(y,Dm[k])==inner(cols[q],v,H), '(3b) fails'
    # radical on Z
    Zb=nullspace(Cm,R); assert len(Zb)==R-d
    BZ=[[Bf(x,y) for y in Zb] for x in Zb]
    assert rank(BZ)==len(Zb)-d, 'rad(B|Z) has wrong dimension'
    # adapted basis
    cur=[row[:] for row in Dm]; QH=[]
    for z in Zb:
        if rank(cur+[z])>rank(cur): cur.append(z); QH.append(z)
    assert len(QH)==n2
    U=[solve(Cm,e) for e in eye(d)]
    X=Dm+QH+U; assert rank(X)==R
    BA=[[Bf(x,y) for y in X] for x in X]
    S=[[BA[d+i][d+j] for j in range(n2)] for i in range(n2)]
    negH=[[neg(x) for x in row] for row in H]
    for i in range(d):
        assert BA[i][:d]==[Z]*d and BA[i][d:d+n2]==[Z]*n2 and BA[i][d+n2:]==negH[i], '(4) top block row'
        assert BA[d+n2+i][:d]==H[i], '(4) bottom-left block'
    for i in range(n2): assert BA[d+i][:d]==[Z]*d, '(4) middle-left block'
    assert madd(S,madj(S))==[[Z]*n2 for _ in range(n2)], 'S not skew-Hermitian'
    dS=det(S); dH=det(H); assert dH[1]==0
    dBA=det(BA)
    assert dBA==mul(dS,mul(dH,dH)), '(4) determinant'
    dX=det(X)
    assert dBA==mul((N(dX),Fr(0)),dB), '(5a) N(det P) det B'
    lhs=mul(dS,inv(prod_a_over_b)); rhs=(N(mul(dX,inv(dH))),Fr(0))
    assert lhs==rhs, '(5b)'
    # 3.5 : class statement
    th=ONE
    for _ in range(n2): th=mul(th,theta)
    dh=mul(th,dS); assert dh[1]==0
    pred=mul(((-1)**n*1,Fr(0)) if True else ONE, prod_ab); pred=mul((Fr((-1)**n),Fr(0)),prod_ab); assert pred[1]==0
    cl=norm_class(dh[0]); clp=norm_class(pred[0]); assert cl==clp, 'class mismatch'
    ratio=dh[0]/pred[0]; assert norm_class(ratio)=='[1]'
    # engine comparison (H = I only): middle block == generic_engine S on the same representatives
    eng=''
    if engine_compare:
        LS=Local(gs)
        # generic_engine coordinates are wrt its own Wb bases; convert our QH (coords wrt Eb) to values and back
        def vals(coord):
            out=[]; p=0
            for i in range(r):
                v=[Z]*d
                for j in range(c[i]): v=vadd(v,vsc(coord[p+j],Eb[i][j]))
                out.append(v); p+=c[i]
            return out
        reps=[LS.coords(vals(z)) for z in QH]
        Seng=[[LS.S(x,y) for y in reps] for x in reps]
        assert Seng==S, 'engine S != B|_Z'
        eng=' engineS=match'
    print(f"{label}: d={d} N={r} R={R} dimH={n2} n={n} det(thetaS)={dh[0]} class={cl} "
          f"prod(a_i b_i)={prod_ab[0]} (-1)^n*prod={pred[0]} pred_class={clp} ratio={ratio} prod_b={prod_b[0]} "
          f"detH0={dH[0]} ALL(1)-(5)+3.5 PASS{eng}")
    return cl

def refl(v,H):
    d=len(v); q=inner(v,v,H); f=mul((Fr(-2),Fr(0)),inv(q))
    Hv=mv(H,[conj(x) for x in v])            # row vector of h0(., v) coefficients: h0(x,v)= sum x_i (H conj v)_i
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],Hv[j]))) for j in range(d)] for i in range(d)]

roots=[[Kc(x) for x in v] for v in json.load(open('/home/claude/g34/roots_alt_5.json'))['generating_reflection_roots']]
I6=eye(6)
s=[refl(v,I6) for v in roots]
# (i) W5 paired 20-tuple, H0 = I
gs=[g for x in s for g in (x,x)]
check(gs,I6,'W5 (20 reflections, H0=I)',engine_compare=True)
# (ii) W5 merges 1-2 (rotation, order 3) and the first order-2 merge, H0 = I
def merged(i):
    out=[]
    for j,g in enumerate(s):
        if j==i: out+=[g,mm(g,s[j+1])]
        elif j==i+1: out.append(g)
        else: out+=[g,g]
    return out
for i in range(9):
    g=mm(s[i],s[i+1]); M=g; o=1
    while M!=I6: M=mm(M,g); o+=1
    E=colspace(msub(I6,g)); Gram=[[inner(x,y,I6) for y in E] for x in E]
    ME=trans([solve(trans(E),mv(msub(I6,g),x)) for x in E])
    check(merged(i),I6,f'W5 merge ({i+1},{i+2}) order {o}: rank-2 local a={det(Gram)[0]} b={det(ME)}',engine_compare=True)
# (iii) rank-one controls
z6=add(ONE,W)
def pw(x,k):
    v=ONE
    for _ in range(k): v=mul(v,x)
    return v
check([[[pw(z6,k)]] for k in [2]*5+[3]+[4]*3+[5]],[[ONE]],'C6 control (2^5,3,4^3,5)',engine_compare=True)
check([[[pw(W,k)]] for k in [1]*5+[2]*5],[[ONE]],'C3 control (1^5,2^5)',engine_compare=True)
check([[[W]],[[W]],[[conj(W)]],[[conj(W)]]],[[ONE]],'odd-n control (w,w,w^2,w^2)',engine_compare=True)
# (iv) GENERAL H0: transport W5 by a random rational T: g' = T^{-1} g T, H0' = T^t conj(T) (so det H0' = N(det T) != 1)
random.seed(7)
while True:
    T=[[(Fr(random.randint(-2,2)),Fr(random.randint(-1,1))) for _ in range(6)] for _ in range(6)]
    if not isz(det(T)): break
Tinv=trans([solve(T,e) for e in eye(6)])
Hp=mm(trans(T),[[conj(x) for x in r] for r in T])
gsp=[mm(mm(Tinv,g),T) for g in gs]
check(gsp,Hp,f'W5 transported (H0 = T^t conj T, det H0 = {det(Hp)[0]})')
# (v) a G(3,1,3) sample with the (0^4,2^6) multiset (class [-1]) -- rebuilt here from the reflection list
def kp(k):
    r=ONE
    for _ in range(k%3): r=mul(r,W)
    return r
refls=[]
for i,j in __import__('itertools').combinations(range(3),2):
    for k in range(3):
        M=[[Z]*3 for _ in range(3)]
        for t in range(3):
            if t not in (i,j): M[t][t]=ONE
        M[i][j]=kp(k); M[j][i]=kp(-k); refls.append(M)
for i in range(3):
    for k in (1,2):
        M=[[ONE if a==b else Z for b in range(3)] for a in range(3)]; M[i][i]=kp(k); refls.append(M)
I3=eye(3)
# random product-one G(3,1,3) tuples of 10 reflections (mixed classes); formula checked on each accepted sample
random.seed(20261029)
got=0; tries=0
while got<3 and tries<20000:
    tries+=1
    idx=[random.randrange(len(refls)) for _ in range(9)]
    P=I3
    for i in idx: P=mm(P,refls[i])
    Pinv=trans([solve(P,e) for e in I3])
    last=next((j for j,M in enumerate(refls) if M==Pinv),None)
    if last is None: continue
    idx.append(last); g=[refls[i] for i in idx]
    # need no common fixed vector: dim H^0 = 0  <=>  rank of stacked (1-g_i) = 3
    if rank([row for M in g for row in msub(I3,M)])<3: continue
    got+=1
    check(g,I3,f'G(3,1,3) sample idx={idx}',engine_compare=True)
print('DONE')
