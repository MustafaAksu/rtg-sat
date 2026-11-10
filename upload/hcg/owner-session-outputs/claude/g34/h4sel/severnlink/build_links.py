"""Claude: independent construction (own algorithm) of pure braids from NEW01..04 and G34-BLOCK-01 to the W5 baseline.
Pair-level moves: conj(i by j) via pair-swap transport + local pure move + inverse transport. Per coordinate BFS
over conjugations by the other current roots. Every word is verified at matrix level with replay_braid.act()."""
import sys,json
from collections import deque
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
exec(open('/home/claude/g34/h4sel/braidescape/replay_braid.py').read().split("def act")[1].split("gF,_,lab=")[0].join(["def act",""]))
n=6
def K(v): return [(F(a),F(b)) for a,b in v]
def load(p): return [K(v) for v in json.load(open(p))['generating_reflection_roots']]
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
def sref(v,w): return vadd(v,vsc(mul((F(-2),F(0)),mul(h(v,w),inv(h(w,w)))),w))
def key(v):
    i=next(k for k in range(n) if not isz(v[k])); c=inv(v[i]); return tuple(x for y in vsc(c,v) for x in y)
def swapword(k):   # adjacent pairs k,k+1 (0-based): (s,s,t,t)->(t,t,s,s)
    return [2*k+2,2*k+1,2*k+3,2*k+2]
def conjword(i,j):  # pair i := s_j s_i s_j, others unchanged
    W=[]
    if j>i:
        for k in range(j-1,i,-1): W+=swapword(k)      # bring pair j to position i+1
        loc=[2*i+2,2*i+1,2*i+1,2*i+2]
    else:
        for k in range(j,i-1): W+=swapword(k)          # bring pair j to position i-1 (pair j moves right)
        loc=[-(2*(i-1)+2),-(2*(i-1)+3),-(2*(i-1)+3),-(2*(i-1)+2)]
    return W+loc+[-x for x in reversed(W)]
def link(src,tgt):
    cur=[v[:] for v in src]; moves=[]
    for i in range(10):
        goal=key(tgt[i])
        if key(cur[i])==goal: continue
        # BFS over conjugations of root i by other current roots
        start=cur[i]; prev={key(start):None}; vec={key(start):start}; dq=deque([start]); found=None
        while dq and found is None:
            v=dq.popleft()
            for j in range(10):
                if j==i: continue
                w=sref(v,cur[j]); kw=key(w)
                if kw not in prev:
                    prev[kw]=(key(v),j); vec[kw]=w; dq.append(w)
                    if kw==goal: found=kw; break
        if found is None: return None,i
        path=[]; k=found
        while prev[k] is not None: pk,j=prev[k]; path.append(j); k=pk
        for j in reversed(path):
            cur[i]=sref(cur[i],cur[j]); moves.append((i,j))
    return moves,None
def freereduce(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return out
B='/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/'
W5=load(B+'W5_BASELINE_ROOTS.json')
srcs={'NEW01':B+'BLIND_INPUT/NEW01_roots.json','NEW02':B+'BLIND_INPUT/NEW02_roots.json','NEW03':B+'BLIND_INPUT/NEW03_roots.json','NEW04':B+'BLIND_INPUT/NEW04_roots.json','BLOCK01':'/home/claude/g34/h4sel/g34block/G34_BLOCK_01_roots.json'}
gT=[]
for v in W5: s=refl(v); gT+=[s,s]
out={}
for name,p in srcs.items():
    S=load(p); moves,fail=link(S,W5)
    if moves is None: print(name,'FAILED at coordinate',fail); continue
    word=[]
    for i,j in moves: word+=conjword(i,j)
    word=freereduce(word)
    g0=[]
    for v in S: s=refl(v); g0+=[s,s]
    gF,_,lab=act(g0,None,list(range(20)),word)
    gB,_,_=act(gF,None,list(range(20)),[-x for x in reversed(word)])
    ok=(gF==gT, lab==list(range(20)), gB==g0)
    print(f'{name} -> W5: pair conjugations {len(moves)}, reduced letters {len(word)}; endpoint {ok[0]}, pure {ok[1]}, inverse {ok[2]}',flush=True)
    out[name]={'pair_moves':moves,'word':word,'checks':ok}
json.dump(out,open('claude_w5_links.json','w'))
