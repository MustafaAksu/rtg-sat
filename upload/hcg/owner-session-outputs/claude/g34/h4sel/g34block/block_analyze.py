"""Claude: G34-BLOCK-01 analysis on the pickled operators: label decomposition (E_L,F_L,X_LL'), E/F exclusion,
and flip-walk search for the maximal tree rank (exact re-check)."""
import sys,json,pickle,random,math,itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
exec(open('block_ops.py').read().split("diags=[(u,v)")[0])
D=pickle.load(open('block_ops.pkl','rb')); flat=D['flat']; H0=D['H0']; diags=D['diags']
OPS={k:([[ (F(a),F(b)) for a,b in r] for r in N],d) for k,(N,d) in D['OPS'].items()}
def qrank(rows):
    M=[list(r) for r in rows if any(x!=0 for x in r)]; rk=0
    if not M: return 0
    for c in range(len(M[0])):
        p=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[x-f*y for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk
def beta(N): return [[__import__('functools').reduce(add,[mul(G[i][k],conj(N[k][l])) for k in range(dH)],Z) for l in range(dH)] for i in range(dH)]
lines=[P10[0],P10[2],P10[4],P10[6]]  # 4-blocks: positions 1-4,5-8,9-12,13-16
def coeffs(x):
    vals=LS.values(x); out=[]
    for i in range(16):
        v=lines[i//4]; out.append(mul(h(vals[i],v),inv(h(v,v))))
    return out
A=[coeffs(x) for x in H]
e=[[sub(a[4*L],a[4*L+1]) for a in A] for L in range(4)]
f=[[sub(a[4*L+1],a[4*L+2]) for a in A] for L in range(4)]
print('e_L,f_L independent on H:',rank(e+f)==8)
def outer(p,q,c=ONE): return [[mul(c,mul(p[i],conj(q[j]))) for j in range(dH)] for i in range(dH)]
def madd(X,Y): return [[add(a,b) for a,b in zip(r,s)] for r,s in zip(X,Y)]
def fl(M): return [q for r in M for x in r for q in (x[0],x[1])]
names=[];pred=[]
for L in range(4): pred.append(outer(e[L],e[L])); names.append(f'E{L+1}')
for L in range(4): pred.append(outer(f[L],f[L])); names.append(f'F{L+1}')
for L,M in itertools.combinations(range(4),2):
    c_=h(lines[L],lines[M])
    if not isz(c_): pred.append(madd(outer(e[L],e[M],c_),outer(e[M],e[L],conj(c_)))); names.append(f'X{L+1}{M+1}')
print('cross pairs with h != 0:',[n_ for n_ in names if n_[0]=='X'])
Pv=[fl(M) for M in pred]; Bv={d:fl(beta(OPS[d][0])) for d in diags}
print('rank predicted:',qrank(Pv),'; rank predicted + all 170 forms:',qrank(Pv+list(Bv.values())))
USES={}
base=qrank(Pv)
for d in diags:
    b=Bv[d]
    USES[d]=set() if all(x==0 for x in b) else {k for k in range(len(Pv)) if qrank([Pv[j] for j in range(len(Pv)) if j!=k]+[b])>qrank([Pv[j] for j in range(len(Pv)) if j!=k])}
# E/F exclusion: any two cuts, one using E_L and one using F_L, must cross
def crosses(d1,d2):
    (a,b),(c_,dd)=d1,d2
    return (a<c_<b<dd) or (c_<a<dd<b)
bad=0
for L in range(4):
    Es=[d for d in diags if L in USES[d]]; Fs=[d for d in diags if L+4 in USES[d]]
    bad+=sum(1 for x in Es for y in Fs if not crosses(x,y))
print('E/F non-crossing pairs (must be 0):',bad)
# flip-walk search for maximal rank
P_=2**61-1
FM={d:[(x.numerator*pow(x.denominator,-1,P_))%P_ for x in flat[d]] for d in diags}
def rmod(rows):
    M=[r[:] for r in rows]; rk=0
    for col in range(len(M[0])):
        p=next((i for i in range(rk,len(M)) if M[i][col]),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]; iv=pow(M[rk][col],-1,P_)
        for i in range(len(M)):
            if i!=rk and M[i][col]:
                f_=M[i][col]*iv%P_; M[i]=[(x-f_*y)%P_ for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk
def tris(T):
    Ds=set(T)|{(i,i+1) for i in range(19)}|{(0,19)}
    adj={i:set() for i in range(20)}
    for a,b in Ds: adj[a].add(b); adj[b].add(a)
    return {tuple(sorted((a,b,c_))) for a,b in Ds for c_ in adj[a]&adj[b]}
def flips(T):
    S_=set(T); tr=tris(T); res=[]
    for dg in T:
        ap=[t for t in tr if dg[0] in t and dg[1] in t]
        oth=[[x for x in t if x not in dg][0] for t in ap]
        if len(oth)!=2: continue
        nd=tuple(sorted(oth))
        if nd not in S_: res.append((dg,nd))
    return res
def fan(): return [(0,v) for v in range(2,19)]
random.seed(2026102318); best=0; bestT=None
for restart in range(40):
    T=fan()
    for _ in range(60): o,nw=random.choice(flips(T)); T=[x for x in T if x!=o]+[nw]
    r=rmod([FM[x] for x in T]); temp=1.0
    for step in range(800):
        o,nw=random.choice(flips(T)); T2=[x for x in T if x!=o]+[nw]; r2=rmod([FM[x] for x in T2])
        if r2>=r or random.random()<math.exp((r2-r)/temp): T,r=T2,r2
        temp=max(0.05,temp*0.995)
        if r>best: best=r; bestT=sorted(T)
print('max mod-p tree rank found over 40 annealing restarts:',best)
print('best tree intervals:',[(u+1,v) for u,v in bestT],'; exact rank',qrank([flat[x] for x in bestT]),'; labels',sorted(names[k] for k in set().union(*[USES[x] for x in bestT])))
