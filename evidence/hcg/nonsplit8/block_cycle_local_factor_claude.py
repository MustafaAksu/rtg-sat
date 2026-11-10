"""Claude: local-factor identity behind the Shapiro discriminant compatibility (Lemma E, PROPOSED).
For g acting on V_1 (+) ... (+) V_l (each = K^r with the same Hermitian Gram H) by
    g(x_1,...,x_l) = (P x_l, x_1, ..., x_{l-1}),   P H-unitary,
test   [a(g) b(g)] = [ a(P) b(P) * det(H)^(l-1) ]   in Q^*/N(K^*)
(a = det of h on E = im(1-g), b = det((1-g)|E); a(P)b(P) := 1 if P = 1).
With the locality theorem this gives: [prod over downstairs a b] = [prod over upstairs a b] * [det H]^(sum ind),
and sum ind = 2(k-1) + 2*gamma is even, so sigma = Ind tau and the tau-datum on Y have the same class.
Exact arithmetic (generic_engine 66f2c253...). Random unitary P built from random order-2 and order-3 K-reflections."""
import sys, random
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import add, sub, neg, mul, conj, inv, isz, Z, ONE, W, eye, mm, mv, msub, colspace, solve
from fractions import Fraction as Fr
def trans(A): return [list(r) for r in zip(*A)]
def inner(x,y,H):
    s=Z
    for i,a in enumerate(x):
        if isz(a): continue
        for j,b in enumerate(y):
            if not isz(b) and not isz(H[i][j]): s=add(s,mul(mul(a,H[i][j]),conj(b)))
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
def ab(g,H):
    n=len(g); E=colspace(msub(eye(n),g))
    if not E: return ONE
    a=det([[inner(x,y,H) for y in E] for x in E])
    ME=trans([solve(trans(E),mv(msub(eye(n),g),x)) for x in E])
    return mul(a,det(ME))
def kref(v,H,zeta):   # x -> x - (1-zeta) h(x,v)/h(v,v) v : H-unitary reflection with eigenvalue zeta on v
    n=len(v); q=inner(v,v,H); Hv=mv(H,[conj(x) for x in v]); f=mul(sub(ONE,zeta),inv(q))
    return [[sub(ONE if i==j else Z, mul(f,mul(v[i],Hv[j]))) for j in range(n)] for i in range(n)]
OM2=mul(W,W)
random.seed(20261029)  # H now has non-norm determinants in general
def rk(): return (Fr(random.randint(-2,2)),Fr(random.randint(-2,2)))
results={}; fails=0; total=0
for trial in range(60):
    r=random.choice([1,2,3]); l=random.choice([2,3,4])
    while True:
        T=[[rk() for _ in range(r)] for _ in range(r)]
        if not isz(det(T)): break
    Dg=[[(Fr(random.choice([1,2,3,5,6,10])),Fr(0)) if i==j else Z for j in range(r)] for i in range(r)]
    H=mm(mm(trans(T),Dg),[[conj(x) for x in row] for row in T])   # det H = N(det T) * det(Dg): NOT always a norm
    P=eye(r)
    for _ in range(random.randint(0,3)):
        v=[rk() for _ in range(r)]
        if all(isz(x) for x in v): continue
        P=mm(P,kref(v,H,random.choice([neg(ONE),W,OM2])))
    n=r*l; g=[[Z]*n for _ in range(n)]
    for i in range(1,l):                       # block i-1 -> block i identity
        for t in range(r): g[i*r+t][(i-1)*r+t]=ONE
    for s in range(r):                         # block l-1 -> block 0 by P
        for t in range(r): g[s][(l-1)*r+t]=P[s][t]
    Hl=[[H[i%r][j%r] if i//r==j//r else Z for j in range(n)] for i in range(n)]
    assert mm(mm(trans(g),Hl),[[conj(x) for x in row] for row in g])==Hl
    lhs=ab(g,Hl); rhs=ab(P,H); dH=det(H)
    naive=mul(lhs,inv(rhs)); results.setdefault(('naive',l),set()).add((norm_class(naive[0]) if naive[1]==0 else 'nonrational', norm_class(dH[0])))
    for _ in range(l-1): rhs=mul(rhs,dH)
    ratio=mul(lhs,inv(rhs))
    total+=1
    if ratio[1]!=0:
        print(f'r={r} l={l}: ratio not rational {ratio}'); fails+=1; continue
    c=norm_class(ratio[0]); key=(r,l)
    results.setdefault(key,set()).add((c,norm_class(dH[0])))
    if c!='[1]': fails+=1; print(f'FAIL r={r} l={l} ratio={ratio[0]} class={c} detH={dH[0]}')
for k in sorted(results,key=str):
    lab='WITHOUT det(H)^(l-1) factor' if k[0]=='naive' else f'r={k[0]}'
    print(f'{lab} l={k[1]}: (class, [det H]) observed {sorted(results[k])}')
print(f'{total} cases, {fails} failures')
