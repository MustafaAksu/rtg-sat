# HHO test: faithful, all-effective, nonabelian K-valued coefficient rep psi = omega^k (x) rho4 on G = C3 x F20.
# Branches of type (1,u) have pure 5-power eigenvalues -> tame-unimodular lemma does not apply -> possible 5-support.
# psi-part computed as (omega^k (x) perm5) minus (omega^k (x) 1); cup form is an orthogonal sum, so
# class(psi) = class(total) * class(rank-one part)  (classes multiplicative; det of empty form = 1).
import sys, io, contextlib, importlib.util, random, itertools
sys.path.insert(0,'.')
from generic_engine import *
spec=importlib.util.spec_from_file_location('cdc','cyclic_disc_claude.py'); mod=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
from fractions import Fraction as Fr
c3=[ONE,W,mul(W,W)]
F20=[(al,be) for al in (1,2,3,4) for be in range(5)]           # x -> al*x+be
def comp(f,g): return ((f[0]*g[0])%5,(f[0]*g[1]+f[1])%5)       # f o g
def inv(f):
    ai=pow(f[0],-1,5); return (ai,(-ai*f[1])%5)
def perm(f):
    M=[[Z]*5 for _ in range(5)]
    for x in range(5): M[(f[0]*x+f[1])%5][x]=ONE
    return M
def sc(c,M): return [[mul(c,x) for x in r] for r in M]
def cpsi(k,f):
    M=sc(c3[k],perm(f)); r=rank(msub(M,eye(5))); return r-(0 if k==0 else 1)
def gen_F20(fs):
    S={(1,0)}; frontier=[(1,0)]
    while frontier:
        x=frontier.pop(); 
        for f in fs:
            y=comp(f,x)
            if y not in S: S.add(y); frontier.append(y)
    return len(S)==20
def disc(gs):
    LS=Local(gs); H=LS.comp
    if not H: return 0,Fr(1),(0,0,0)   # r2: empty form has dim 0 (r1 bug: returned 1)
    G=[[LS.S(x,y) for y in H] for x in H]; h=[[mul(mod.theta,x) for x in r] for r in G]
    d=mod.det(h); return len(H),d[0],mod.hsig(h)
random.seed(5)
els=[(k,f) for k in range(3) for f in F20 if not (k==0 and f==(1,0))]
seen=set(); out=[]; tries=0
while len(out)<40 and tries<400000:
    tries+=1
    r=random.randint(4,6)
    t=[random.choice(els) for _ in range(r-1)]
    # last element closes the product (left-to-right product = identity)
    P=(1,0); ks=0
    for k,f in t: P=comp(P,f); ks+=k
    last=(( -ks)%3, inv(P))
    if last==(0,(1,0)): continue
    t.append(last)
    if sum(cpsi(k,f) for k,f in t)!=16: continue
    if not gen_F20([f for k,f in t]) or all(k==0 for k,f in t): continue
    key=tuple(sorted(t))
    if key in seen: continue
    seen.add(key)
    tot=disc([sc(c3[k],perm(f)) for k,f in t]); one=disc([[[c3[k]]] for k,f in t])
    dim=tot[0]-one[0]; d=tot[1]/one[1]
    sig=(tot[2][0]-one[2][0],tot[2][1]-one[2][1])
    n5pure=sum(1 for k,f in t if k==0 and f[0]==1)   # untwisted translations: eigenvalues pure 5-power
    out.append((t,dim,sig,str(d),mod.norm_class(d),n5pure))
    print(t,'dim',dim,'sig',sig,'det',d,'class',mod.norm_class(d),'#untwisted-5-elements',n5pure,flush=True)
from collections import Counter
print('SUMMARY', Counter((o[1],o[2],o[4],o[5]%2) for o in out))
