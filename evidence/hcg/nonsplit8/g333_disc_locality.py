"""Claude: is the discriminant class [det h] of H^1_par a function of the local conjugacy classes only?
Test in G(3,3,3) (order 54, 3-dim reflection rep over K=Q(w)): random product-one generating tuples of N order-2
reflections (N = 8 -> dim H_par = 2; N = 10 -> dim 4), record the multiset of local conjugacy classes (in G(3,3,3))
and the class of det h. If two tuples with the same local class multiset have different [det h], locality fails."""
import sys, json, random, itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
from fractions import Fraction as Fr
random.seed(20261029)
theta=(Fr(1),Fr(2)); w=W
def kp(k):
    r=ONE
    for _ in range(k%3): r=mul(r,w)
    return r
n=3
# G(3,3,3) reflections of order 2: x_i <-> z^k x_j, x_j <-> z^{-k} x_i
refls=[]
for i,j in itertools.combinations(range(3),2):
    for k in range(3):
        M=[[Z]*3 for _ in range(3)]
        for t in range(3):
            if t not in (i,j): M[t][t]=ONE
        M[i][j]=kp(k); M[j][i]=kp(-k)
        refls.append(M)
assert len(refls)==9
import sys as _s
if len(_s.argv)>1 and _s.argv[1]=='G313':
    for i in range(3):
        for k in (1,2):
            M=[[ONE if a==b else Z for b in range(3)] for a in range(3)]; M[i][i]=kp(k); refls.append(M)
    print('using G(3,1,3): reflections =',len(refls))
# group closure
def key(M): return tuple(tuple(x) for r in M for x in r)
G={key(eye(3)):eye(3)}; frontier=[eye(3)]
while frontier:
    nf=[]
    for A in frontier:
        for s in refls:
            B=mm(A,s); k=key(B)
            if k not in G: G[k]=B; nf.append(B)
    frontier=nf
print('|G(3,3,3)| =',len(G))
# conjugacy classes of the 9 reflections inside G
Glist=list(G.values())
def cls(M):
    return frozenset(key(mm(mm(g,M),adj(g))) for g in Glist)   # g unitary: g^{-1} = g^*
classes={}
for s in refls:
    c=cls(s); classes.setdefault(c,len(classes))
print('reflection conjugacy classes in G(3,3,3):',len(classes))
rcls=[classes[cls(s)] for s in refls]
def det(M):
    M=[r[:] for r in M]; m=len(M); d=ONE
    for c in range(m):
        p=next((i for i in range(c,m) if not isz(M[i][c])),None)
        if p is None: return Z
        if p!=c: M[c],M[p]=M[p],M[c]; d=neg(d)
        d=mul(d,M[c][c]); f=inv(M[c][c])
        for i in range(c+1,m):
            if not isz(M[i][c]):
                g=mul(M[i][c],f); M[i]=[sub(x,mul(g,y)) for x,y in zip(M[i],M[c])]
    return d
def norm_class(q):
    sg='-' if q<0 else ''
    q=abs(q); odd=set()
    for n_ in (q.numerator,q.denominator):
        p=2
        while n_>1:
            e=0
            while n_%p==0: n_//=p; e+=1
            if e%2 and p%3==2: odd.add(p)
            p+=1
    return '['+sg+('1' if not odd else '*'.join(map(str,sorted(odd))))+']'
def generates(gs):
    S={key(eye(3))}; fr=[eye(3)]
    while fr:
        nf=[]
        for A in fr:
            for s in gs:
                B=mm(A,s); k=key(B)
                if k not in S: S.add(k); nf.append(B)
        fr=nf
    return len(S)==len(G)
results={}
for N in (8,10):
    tried=0; got=0
    while got<80 and tried<60000:
        tried+=1
        idx=[random.randrange(len(refls)) for _ in range(N-1)]
        P=eye(3)
        for i in idx: P=mm(P,refls[i])
        Pinv=adj(P)
        last=next((j for j,s in enumerate(refls) if s==Pinv),None)
        if last is None: continue
        idx.append(last); gs=[refls[i] for i in idx]
        if not generates(gs): continue
        got+=1
        LS=Local(gs); H=LS.comp; dH=len(H)
        Gm=[[LS.S(x,y) for y in H] for x in H]; hh=[[mul(theta,x) for x in r] for r in Gm]
        d=det(hh); assert d[1]==0
        local=tuple(sorted(rcls[i] for i in idx))
        results.setdefault((N,local,dH),set()).add(norm_class(d[0]))
for (N,local,dH),cl in sorted(results.items()):
    print(f"N={N} dim={dH} local classes {local}: det classes {sorted(cl)}")
