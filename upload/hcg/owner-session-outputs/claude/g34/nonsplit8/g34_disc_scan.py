"""Claude: discriminant classes [det h] of H^1_par for G34 data (Lemma 7.2 cup form, engine generic_engine.py).
(a) 20-reflection tuples at hand (W5, W6, W7, NEW01-04, BLOCK-01, ESCAPE): expect [1] on every component if the
    discriminant is determined by the local classes.
(b) 19-point data obtained from W5's paired tuple by merging one adjacent pair of distinct reflections (s_i, s_j)
    into the rank-2 element g = s_i s_j (order 2: bireflection; order 3: rotation). These are Severn v1 Rem 6.3's
    'two further class data' with budget N-3 = 16. Question: is [det h] nonsplit for either rank-2 class?"""
import sys, json
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
from fractions import Fraction as Fr
theta=(Fr(1),Fr(2))
def Kc(p): return (Fr(p[0]),Fr(p[1]))
def refl(v):
    n=len(v); f=mul((Fr(-2),Fr(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
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
def hsig(M):
    M=[r[:] for r in M]; nn=len(M); pos=ng=0; idx=list(range(nn))
    assert all(M[i][j]==conj(M[j][i]) for i in range(nn) for j in range(nn))
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
def norm_class(q):
    if q<0: return 'NEG'
    odd=set()
    for n_ in (q.numerator,q.denominator):
        p=2
        while n_>1:
            e=0
            while n_%p==0: n_//=p; e+=1
            if e%2 and p%3==2: odd.add(p)
            p+=1
    return '[1]' if not odd else '['+'*'.join(map(str,sorted(odd)))+']'
def analyse(gs,label):
    LS=Local(gs); H=LS.comp; dH=len(H)
    G=[[LS.S(x,y) for y in H] for x in H]; hh=[[mul(theta,x) for x in r] for r in G]
    d=det(hh); assert d[1]==0
    print(f"{label}: dim={dH} det_K h={d[0]} class={norm_class(d[0])} sig={hsig(hh)}")
    return norm_class(d[0])
def mpow(M,k):
    R=eye(len(M))
    for _ in range(k): R=mm(R,M)
    return R
def order(M):
    return next(k for k in range(1,100) if mpow(M,k)==eye(len(M)))
# ---- (a) 20-reflection tuples
srcs={'W5':'/home/claude/g34/roots_alt_5.json','W6':'/home/claude/g34/roots_W6.json','W7':'/home/claude/g34/roots_W7.json',
      'NEW01':'/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT/NEW01_roots.json',
      'NEW02':'/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT/NEW02_roots.json',
      'NEW03':'/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT/NEW03_roots.json',
      'NEW04':'/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT/NEW04_roots.json',
      'BLOCK-01':'/home/claude/g34/h4sel/g34block/G34_BLOCK_01_roots.json',
      'ESCAPE':'/home/claude/g34/h4sel/braidescape/final_roots_generating.json'}
def load_roots(p):
    d=json.load(open(p))
    if isinstance(d,dict):
        for k in ('generating_reflection_roots','roots','root_vectors','final_roots'):
            if k in d: d=d[k]; break
        else: d=next(v for v in d.values() if isinstance(v,list) and len(v)==10)
    return [[Kc(c) for c in v] for v in d]
W5=None
for lab,p in srcs.items():
    try: V=load_roots(p)
    except Exception as e: print(lab,'skip',e); continue
    S_=[refl(v) for v in V]; gs=[]
    for s in S_: gs+=[s,s]
    if lab=='W5': W5=S_
    analyse(gs,f"(a) {lab} 20 reflections")
# ---- (b) merged 19-tuples from W5
print('--- (b) W5 paired tuple with one adjacent distinct pair merged into g = s_i s_j')
for i in range(9):
    g=mm(W5[i],W5[i+1]); o=order(g); rk=rank(msub(eye(6),g))
    gs=[]
    for k in range(10):
        if k==i: gs+=[W5[k],g]        # (s_i, s_i s_{i+1})
        elif k==i+1: gs+=[W5[k]]      # then s_{i+1}
        else: gs+=[W5[k],W5[k]]
    assert len(gs)==19
    analyse(gs,f"merge (s{i+1},s{i+2}) -> g order {o} rank(1-g)={rk}")
