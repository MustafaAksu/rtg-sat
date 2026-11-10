"""Claude: independent census behind the rank-2 step (proof note Sec. 5).
From the 10 W5 roots alone: 756 minimal vectors, 126 reflection lines (norm-6 representatives, standard form);
for EVERY pair of distinct lines count the lines lying in the complex plane they span (claim: exactly 2 if the pair is
orthogonal, exactly 3 otherwise, i.e. the Gram-rank bound q <= 3 is attained only by the A2 configuration);
count two-line and three-line planes (ChatGPT: 2835 and 1680); and compute the local data (a,b) of g = s_v s_w in
the root basis for both types (ChatGPT: (36,4) and (27,3)).
Exact Eisenstein-integer arithmetic, no engine import."""
import json, itertools
roots=[[tuple(c) for c in v] for v in json.load(open('/home/claude/g34/roots_alt_5.json'))['generating_reflection_roots']]
# Z[w] arithmetic on pairs (a,b) = a + b w, w^2 = -1 - w
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): a,b=x;c,e=y; return (a*c-b*e,a*e+b*c-b*e)
def conj(x): return (x[0]-x[1],-x[1])
def Nm(x): return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def h(x,y):
    s=(0,0)
    for a,b in zip(x,y): s=add(s,mul(a,conj(b)))
    return s
assert all(h(v,v)==(6,0) for v in roots)
def refl(v):   # s(x) = x - 2 h(x,v)/h(v,v) v = x - (h(x,v)/3) v ; integrality: h(x,v) must be divisible by 3 in Z[w]
    def s(x):
        c=h(x,v); assert c[0]%3==0 and c[1]%3==0, 'non-integral reflection image'
        c=(c[0]//3,c[1]//3)
        return tuple(sub(a,mul(c,b)) for a,b in zip(x,v))
    return s
S=[refl(v) for v in roots]
orb={tuple(roots[0])}; fr=[tuple(roots[0])]
while fr:
    nf=[]
    for x in fr:
        for s in S:
            y=s(x)
            if y not in orb: orb.add(y); nf.append(y)
    fr=nf
V=list(orb); print('minimal vectors:',len(V))
units=[(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,1)]      # mu_6
lines={}
for x in V:
    key=min(tuple(mul(u,c) for c in x) for u in units); lines.setdefault(key,x)
L=list(lines.values()); print('lines:',len(L))
assert all(h(v,v)==(6,0) for v in L)
def gram_det3(a,b,c):
    G=[[h(x,y) for y in (a,b,c)] for x in (a,b,c)]
    d=(0,0)
    for p,sg in (((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)):
        t=mul(mul(G[0][p[0]],G[1][p[1]]),G[2][p[2]])
        d=add(d,t) if sg==1 else sub(d,t)
    return d
pairs=list(itertools.combinations(range(len(L)),2)); print('pairs:',len(pairs))
hist={}; types={}
for i,j in pairs:
    v,w=L[i],L[j]; n2=Nm(h(v,w)); assert n2 in (0,9), n2
    q=sum(1 for u in L if gram_det3(v,w,u)==(0,0))      # lines in the plane span(v,w) (incl. v,w)
    hist[(n2,q)]=hist.get((n2,q),0)+1
    types.setdefault(n2,(i,j))
print('(|h(v,w)|^2, lines in plane): pair counts =',hist)
two=hist.get((0,2),0); three=hist.get((9,3),0)
print('two-line planes =',two,' three-line planes =',three//3,' (each 3-line plane counted by 3 pairs)')
assert set(hist)=={(0,2),(9,3)}, 'a plane with a different line count exists'
# local data of g = s_v s_w in the root basis {v,w}
from fractions import Fraction as Fr
def K(x): return (Fr(x[0]),Fr(x[1]))
def kmul(x,y): a,b=x;c,e=y; return (a*c-b*e,a*e+b*c-b*e)
def kadd(x,y): return (x[0]+y[0],x[1]+y[1])
def ksub(x,y): return (x[0]-y[0],x[1]-y[1])
for n2,(i,j) in sorted(types.items()):
    v,w=L[i],L[j]; sv,sw=refl(v),refl(w)
    g=lambda x: sv(sw(x))
    # g on the plane in basis (v,w): g v = s_v(s_w v), g w = s_v(s_w w) = s_v(-w); express in basis by solving the Gram system
    G=[[K(h(x,y)) for y in (v,w)] for x in (v,w)]
    def coords(u):   # u = p v + q w  ->  (p,q) from h(u,v)=p h(v,v)+q h(w,v), h(u,w)=p h(v,w)+q h(w,w)
        r1,r2=K(h(u,v)),K(h(u,w)); a,b=G[0][0],G[1][0]; c,d=G[0][1],G[1][1]   # r1 = p a + q b ; r2 = p c + q d
        det=ksub(kmul(a,d),kmul(b,c)); inv=lambda x:(lambda n:( (x[0]-x[1])/n, -x[1]/n))(x[0]*x[0]-x[0]*x[1]+x[1]*x[1])
        p=kmul(ksub(kmul(r1,d),kmul(b,r2)),inv(det)); q=kmul(ksub(kmul(a,r2),kmul(r1,c)),inv(det))
        return p,q
    gv=coords(g(v)); gw=coords(g(w))
    M=[[gv[0],gw[0]],[gv[1],gw[1]]]                      # columns = images
    one_minus=[[ksub((Fr(1),Fr(0)) if r==c else (Fr(0),Fr(0)),M[r][c]) for c in range(2)] for r in range(2)]
    b=ksub(kmul(one_minus[0][0],one_minus[1][1]),kmul(one_minus[0][1],one_minus[1][0]))
    a=ksub(kmul(G[0][0],G[1][1]),kmul(G[0][1],G[1][0]))
    # order of g on the plane
    M2=[r[:] for r in M]; o=1
    def mm2(A,B): return [[kadd(kmul(A[r][0],B[0][c]),kmul(A[r][1],B[1][c])) for c in range(2)] for r in range(2)]
    while M2!=[[(Fr(1),Fr(0)),(Fr(0),Fr(0))],[(Fr(0),Fr(0)),(Fr(1),Fr(0))]]: M2=mm2(M2,M); o+=1
    print(f'type |h|^2={n2}: g=s_v s_w order {o}; root-basis a=det Gram={a[0]} (imag {a[1]}), b=det(1-g|E)={b}, a*b={a[0]*b[0]}')
print('CENSUS DONE')
