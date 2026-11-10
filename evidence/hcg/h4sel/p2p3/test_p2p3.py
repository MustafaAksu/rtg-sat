"""Claude's independent falsification tests of ChatGPT's P2 (inverse unitary pairs) and P3 (finite-order
boundary projector) formulas, using generic_engine.py only (no g34_gateB / edgeform_predict / ChatGPT code).
Twist convention phi(g_k)=c g_k c^-1 (a<=k<=b), T: u -> u o phi^power  (same as the session certificates)."""
import sys, json, random, itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
random.seed(20261023)
LOG=[]
def say(*a):
    s=' '.join(str(x) for x in a); print(s); LOG.append(s)
def Kc(p): return (F(p[0]),F(p[1]))
def scal(c,M): return [[mul(c,x) for x in r] for r in M]
def outer(v,w): return [[mul(a,conj(b)) for b in w] for a in v]
def creflect(v,zeta):  # x -> x + (zeta-1) h(x,v)/h(v,v) v
    n=len(v); hv=h(v,v); f=mul(sub(zeta,ONE),inv(hv))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
def is_unitary(M): return mm(adj(M),M)==eye(len(M))
def order(M,cap=500):
    P=M; 
    for k in range(1,cap+1):
        if P==eye(len(M)): return k
        P=mm(P,M)
    return None
def proj_fix(C,k):
    n=len(C); P=[[Z]*n for _ in range(n)]; Cj=eye(n)
    for j in range(k): P=[[add(a,b) for a,b in zip(r,s)] for r,s in zip(P,Cj)]; Cj=mm(Cj,C)
    return scal((F(1,k),F(0)),P)
def basisH(LS):  # list of cocycle coordinate vectors representing H^1_par basis
    return LS.comp
FAIL=[0]
def chk(name,cond):
    if not cond: FAIL[0]+=1; say('  FAIL',name)
    return cond
def check_S_wellposed(LS):
    ok=all(isz(LS.S(b,z)) and isz(LS.S(z,b)) for b in LS.B1 for z in LS.Z1)
    H=LS.comp; G=[[LS.S(x,y) for y in H] for x in H]
    return ok, rank(G), len(H), G
# ---------------------------------------------------------------- P2
def p2_case(label, rs, controls=True):
    n=len(rs[0]); m=len(rs)
    gs=[]
    for r in rs: gs+= [r, adj(r)]
    LS=Local(gs)
    ok,rk,dimH,G=check_S_wellposed(LS)
    D=sum(len(colspace(msub(r,eye(n)))) for r in rs); d=D-n
    say(f'[P2:{label}] n={n} m={m} orders={[order(r) for r in rs]} dimW={[len(colspace(msub(r,eye(n)))) for r in rs]} d={d} dimH={dimH} S well-posed={ok} rank S={rk}')
    chk('dimH=2d',dimH==2*d); chk('S coboundary-null',ok); chk('S nondegenerate',rk==dimH)
    H=LS.comp; vals=[LS.values(x) for x in H]
    def tau(v,i): return vadd(v[2*i], mv(rs[i],v[2*i+1]))
    # tau surjective onto L_gen: rank of tau image (as vectors in (+)K^n) = d
    timg=[sum([tau(v,i) for i in range(m)],[]) for v in vals]; chk('rank tau = d', rank(timg)==d)
    ntest=0; nctl=[0,0,0]
    for a in range(m):
        for b in range(a,m):
            if (a,b)==(0,m-1): continue
            ka,kb=2*a,2*b+1
            # twist (power 1, rho(c)=1) vs formula
            for j,v in enumerate(vals):
                tw=LS.twist_cocycle(v,ka,kb,1); Nv=[sub_vec for sub_vec in [ [sub(p,q) for p,q in zip(x,y)] for x,y in zip(tw,v)]]
                uc=[Z]*n
                for i in range(a,b+1): uc=vadd(uc,tau(v,i))
                pred=[mv(msub(eye(n),gs[k]),uc) if ka<=k<=kb else [Z]*n for k in range(LS.r)]
                chk(f'N_e formula e=[{ka+1},{kb+1}] x{j}', Nv==pred)
                vals_N=Nv
                Ny=LS.coords(vals_N)
                for i_,x in enumerate(H):
                    lhs=LS.S(x,Ny)
                    fx=[Z]*n; fy=[Z]*n
                    for i in range(a,b+1): fx=vadd(fx,tau(vals[i_],i)); fy=vadd(fy,tau(v,i))
                    rhs=neg(h(fx,fy)); ntest+=1
                    chk(f'S(x,N_e y) e=[{ka+1},{kb+1}]', lhs==rhs)
                    if controls and not isz(rhs):
                        if lhs!=neg(rhs): nctl[0]+=1           # sign control (+h) must fail
                        # wrong inverse in tau: t_i = c_{2i-1} + r_i^{-1} c_{2i}
                        fx2=[Z]*n; fy2=[Z]*n
                        for i in range(a,b+1):
                            fx2=vadd(fx2,vadd(vals[i_][2*i],mv(adj(rs[i]),vals[i_][2*i+1]))); fy2=vadd(fy2,vadd(v[2*i],mv(adj(rs[i]),v[2*i+1])))
                        if lhs!=neg(h(fx2,fy2)): nctl[1]+=1
                        nctl[2]+=1
    say(f'   identity tests={ntest}; nonzero cases={nctl[2]}: +h control rejected {nctl[0]}, wrong-inverse control rejected {nctl[1]}')
    # aggregate: im(sum of pair N) = ker tau
    return LS
def rand_root(n,lo=-1,hi=1):
    while True:
        v=[(F(random.randint(lo,hi)),F(random.randint(lo,hi))) for _ in range(n)]
        if not all(isz(x) for x in v): return v
W6=( F(0),F(1)); MW=(F(0),F(-1))  # w, -w (primitive 6th root: -w has order 6)
say('=== P2: inverse unitary pairs ===')
# (a) order-3 reflections, n=3, m=5
rs=[creflect(rand_root(3),W6) for _ in range(5)]; p2_case('order3-refl',rs)
# (b) order-6 reflections (eigenvalue -w), n=3, m=5
rs=[creflect(rand_root(3),MW) for _ in range(5)]; p2_case('order6-refl',rs)
# (c) mixed: order-4 rotation blocks (dim W=2), products of two order-3 reflections (dim W=2, possibly infinite order)
R4=[[Z,neg(ONE),Z],[ONE,Z,Z],[Z,Z,ONE]]
def conjP(M,P): return mm(mm(P,M),adj(P))
perms=[ [[ONE if j==p[i] else Z for j in range(3)] for i in range(3)] for p in itertools.permutations(range(3))]
rs=[R4, conjP(R4,perms[3]), mm(creflect(rand_root(3),W6),creflect(rand_root(3),W6)), mm(creflect(rand_root(3),MW),creflect(rand_root(3),W6)), creflect(rand_root(3),W6)]
p2_case('mixed-rank2',rs)
# (d) order-2 G34 W5 roots (regression to EDGEFLUX constant -1)
W5=json.load(open('/home/claude/g34/roots_alt_5.json'))['generating_reflection_roots']
rs=[creflect([Kc(c) for c in v],neg(ONE)) for v in W5]
p2_case('G34-W5-order2',rs,controls=True)
# ---------------------------------------------------------------- P3
say('=== P3: finite-order boundary projector ===')
def p3_case(label, gs, intervals):
    LS=Local(gs); n=LS.n
    ok,rk,dimH,G=check_S_wellposed(LS)
    say(f'[P3:{label}] n={n} r={LS.r} dimH={dimH} S well-posed={ok} rank S={rk}')
    chk('S coboundary-null',ok)
    H=LS.comp; vals=[LS.values(x) for x in H]
    stats=[]
    for (a,b) in intervals:
        C=eye(n)
        for k in range(a,b+1): C=mm(C,gs[k])
        k_=order(C); P=proj_fix(C,k_); fixdim=rank(P) if any(not isz(x) for r in P for x in r) else 0
        ucs=[LS.uword(v,[(i,1) for i in range(a,b+1)])[0] for v in vals]
        good=0; tot=0; c_k2=0; c_np=0; c_nz=0; n2=0; ncz=0; Nzero=True
        Nys=[]
        for j,v in enumerate(vals):
            tw=LS.twist_cocycle(v,a,b,k_); Nv=[[sub(p,q) for p,q in zip(x,y)] for x,y in zip(tw,v)]
            wy=scal((F(k_),F(0)),[[x] for x in mv(P,ucs[j])]); wy=[r[0] for r in wy]
            pred=[mv(msub(eye(n),gs[i]),wy) if a<=i<=b else [Z]*n for i in range(LS.r)]
            chk(f'N formula [{a+1},{b+1}]',Nv==pred)
            if any(not isz(x) for vv in Nv for x in vv): Nzero=False
            Ny=LS.coords(Nv); Nys.append(Ny)
            # (Ny)(c)=0
            if all(isz(x) for x in LS.uword(Nv,[(i,1) for i in range(a,b+1)])[0]): ncz+=1
            # N^2 = 0
            tw2=LS.twist_cocycle(Nv,a,b,k_); 
            if all(isz(sub(p,q)) for x,y in zip(tw2,Nv) for p,q in zip(x,y)): n2+=1
            for i_,x in enumerate(H):
                lhs=LS.S(x,Ny); px=mv(P,ucs[i_]); py=mv(P,ucs[j])
                rhs=mul((F(-k_),F(0)),h(px,py)); tot+=1
                if chk(f'S formula [{a+1},{b+1}] k={k_}',lhs==rhs): good+=1
                if not isz(rhs):
                    c_nz+=1
                    if k_>1 and lhs!=mul((F(-k_*k_),F(0)),h(px,py)): c_k2+=1
                    if lhs!=mul((F(-k_),F(0)),h(ucs[i_],ucs[j])): c_np+=1
        stats.append((a+1,b+1,k_,fixdim,good,tot,c_nz,c_k2,c_np,n2,ncz,Nzero))
        chk('Fix(C)=0 => N=0', fixdim>0 or Nzero)
        say(f'   e=[{a+1},{b+1}] k={k_} dimFix={fixdim} S-identity {good}/{tot}; nonzero={c_nz}: k^2-control rejected {c_k2}, no-projector control rejected {c_np}; N^2=0 {n2}/{len(vals)}; (Ny)(c)=0 {ncz}/{len(vals)}; N==0:{Nzero}')
    return stats
# (a) G34 W5 paired tuple, NON-pair-aligned intervals (reflection order 2, k>1)
gsW5=[]
for r in rs: gsW5+=[r,r]
ints=[(1,2),(1,4),(3,6),(1,2+3),(5,10),(7,8),(1,6)]   # 0-based (a,b): positions 2-3, 2-5, 4-7, ...
p3_case('G34-W5 odd intervals',gsW5,ints)
# (b) random monomial tuples in G(6,1,4): entries mu_6 in Q(w), various orders incl 4,6,12
MU6=[ONE,(F(1),F(1)),W6,neg(ONE),MW,(F(-1),F(-1))]  # 1, -w^2=1+w, w, -1, -w, w^2=-1-w
def rand_mono(n):
    p=list(range(n)); random.shuffle(p)
    return [[random.choice(MU6) if j==p[i] else Z for j in range(n)] for i in range(n)]
gs=[rand_mono(4) for _ in range(5)]
P=eye(4)
for g in gs: P=mm(P,g)
gs.append(adj(P))
assert all(is_unitary(g) for g in gs)
p3_case('G(6,1,4) random',gs,[(0,1),(1,2),(0,2),(1,3),(2,4),(0,3),(3,4)])
# (c) reflection tuple in G(3,1,3) with product 1 found by search (order-3 diagonal and order-2 transposition-type reflections)
def refl_list(n):
    L=[]
    for i in range(n):
        for z in [W6,(F(-1),F(-1))]:
            M=eye(n); M[i][i]=z; L.append(M)
    for i in range(n):
        for j in range(i+1,n):
            for z in [ONE,W6,(F(-1),F(-1))]:
                v=[Z]*n; v[i]=ONE; v[j]=neg(z); L.append(creflect(v,neg(ONE)))
    return L
RL=refl_list(3)
found=None
for trial in range(20000):
    t=[random.choice(RL) for _ in range(7)]
    P=eye(3)
    for g in t: P=mm(P,g)
    last=adj(P)
    if last in RL and len(colspace(msub(last,eye(3))))==1:
        found=t+[last]; break
say('reflection tuple found:',found is not None)
if found:
    p3_case('G(3,1,3) reflection tuple r=8',found,[(0,1),(1,2),(0,2),(2,4),(1,4),(3,6),(0,4)])
say('TOTAL FAILURES:',FAIL[0])
open('/home/claude/g34/h4sel/p2p3/test_p2p3_out.txt','w').write('\n'.join(LOG)+'\n')
