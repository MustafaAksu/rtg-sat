# Test of defect-zero support theorem: G = C3 x S3, chi = zeta3 (x) std (degree 2, values in K).
# |G|/chi(1) = 9 -> no inert prime -> prediction: every (4,4) rank-8 datum has class [1].
import sys, io, contextlib, random, itertools
sys.path.insert(0,'.')
from generic_engine import *
import importlib.util
spec=importlib.util.spec_from_file_location('cdc','cyclic_disc_claude.py'); mod=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
w=W; w2=mul(W,W)
R3=[[w,Z],[Z,w2]]; T=[[Z,ONE],[ONE,Z]]
S3=[eye(2),R3,mm(R3,R3),T,mm(T,R3),mm(T,mm(R3,R3))]
names=['1','r','r2','t','tr','tr2']
def sc(c,M): return [[mul(c,x) for x in row] for row in M]
G=[(a,i,sc(mod.kpow(w,a),S3[i])) for a in range(3) for i in range(6)]
def rk(M): return rank(msub(M,eye(2)))
random.seed(20261104)
seen=set(); res=[]
tries=0
while len(res)<60 and tries<200000:
    tries+=1
    r=random.randint(6,12)
    tup=[random.choice(G) for _ in range(r-1)]
    P=eye(2)
    for g in tup: P=mm(P,g[2])
    last=next((g for g in G if mm(P,g[2])==eye(2)),None)
    if last is None: continue
    tup.append(last)
    if any(rk(g[2])==0 for g in tup): continue          # identity local monodromy = no branch point
    if sum(rk(g[2]) for g in tup)!=12: continue         # m(chi) = -4 + sum rank = 8
    if not any(g[1] in (3,4,5) for g in tup) or not any(g[1] in (1,2) for g in tup): continue  # irreducible image
    key=tuple(sorted((g[0],g[1]) for g in tup))
    if key in seen: continue
    seen.add(key)
    LS=Local([g[2] for g in tup]); H=LS.comp
    if len(H)!=8: continue
    Gm=[[LS.S(x,y) for y in H] for x in H]
    h=[[mul(mod.theta,x) for x in r_] for r_ in Gm]
    d=mod.det(h); sig=mod.hsig(h)
    res.append(([f"w^{g[0]}{names[g[1]]}" for g in tup],sig,str(d[0]),mod.norm_class(d[0])))
from collections import Counter
print('cases',len(res))
print(Counter((r[1],r[3]) for r in res))
for r in res:
    print(r)
