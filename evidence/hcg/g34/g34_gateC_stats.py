import random, json
from collections import Counter
import g34_gateC_search as S
rng=random.Random(7); seen=set(); fails=Counter(); qs=Counter(); n=0
def failcode(res):
    for h in ('H0','H1','H2','H3','H4'):
        if not res.get(h): return h
    return 'PASS'
for t in range(1500):
    res=S.evaluate(S.random_tree(1,20,rng))
    if res is None: continue
    key=tuple(res['curves'])
    if key in seen: continue
    seen.add(key); n+=1; fails[failcode(res)]+=1
    if res.get('H0') and res.get('H1') and res.get('H2') and res.get('H3'): qs[res['qspan']]+=1
print("distinct:",n," first failing hypothesis:",dict(fails)," Q-span among H0-H3 passing:",dict(qs))
sev=[(1,8),(1,18),(2,8),(3,8),(4,8),(5,6),(5,8),(7,8),(9,10),(9,12),(9,16),(9,17),(9,18),(11,12),(13,14),(13,16),(15,16)]
# evaluate this interval pattern on OUR tuple by building its tree
def tree_from_curves(curves):
    # nodes from laminar family plus root and leaves
    fam=set(curves)|{(1,20)}
    # add complements needed: build recursively by finding maximal sub-intervals
    def build(lo,hi):
        if lo==hi: return []
        kids=[c for c in fam if lo<=c[0] and c[1]<=hi and c!=(lo,hi)]
        maxk=[c for c in kids if not any(d!=c and d[0]<=c[0] and c[1]<=d[1] for d in kids)]
        # fill gaps with singletons
        pts=sorted(maxk); parts=[]; cur=lo
        for a,b in pts:
            parts+= [(x,x) for x in range(cur,a)]; parts.append((a,b)); cur=b+1
        parts+=[(x,x) for x in range(cur,hi+1)]
        # binarize left to right
        nodes=[]; left=parts[0]
        for p in parts[1:]:
            new=(left[0],p[1]); nodes.append((new[0],new[1],left,p)); left=new
        for a,b in parts:
            if a<b: nodes+=build(a,b)
        # last node equals (lo,hi)
        return nodes
    return build(1,20)
res=S.evaluate(tree_from_curves(sev))
print("Severn-shaped decomposition on OUR tuple:", {k:res.get(k) for k in ('H0','H1','H2','H3','H4','dimI','qspan')} if res else res)
