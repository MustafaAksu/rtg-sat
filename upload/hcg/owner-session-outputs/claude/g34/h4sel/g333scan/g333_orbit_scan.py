"""Claude: exhaustive G(3,3,3), m=6 paired-tuple scan under adjacent pure pair-conjugations (both orientations).
Nodes: all 9^6 line-tuples. Graph components via union-find (A3-failing nodes kept as bridges). Generation is constant
on components (moves preserve the generated group) -> keep components generating the full order-54 group.
On A3-valid nodes, best rank over the 14 pair-containing trees (EDGEFLUX forms, mod p); early stop at 9; components
without 9 are exhaustively evaluated."""
import sys, itertools, time
src=open('/home/claude/g34/h4sel/toybraid/toy_braid_bfs.py').read().split("print('start best pair-tree rank:'")[0]
exec(src)
NL=len(rep); assert NL==9
N=NL**6
def enc(t):
    x=0
    for a in t: x=x*NL+a
    return x
def dec(x):
    t=[]
    for _ in range(6): t.append(x%NL); x//=NL
    return tuple(reversed(t))
par=list(range(N))
def find(a):
    while par[a]!=a: par[a]=par[par[a]]; a=par[a]
    return a
def union(a,b):
    ra,rb=find(a),find(b)
    if ra!=rb: par[ra]=rb
t0=time.time()
for x in range(N):
    s=dec(x)
    for i in range(5):
        a,b=s[i],s[i+1]
        for new in ((ACT[a][b],b),(a,ACT[b][a])):
            union(x,enc(s[:i]+new+s[i+2:]))
comps={}
for x in range(N): comps.setdefault(find(x),[]).append(x)
print('components (all tuples):',len(comps),' time',round(time.time()-t0,1),'s')
# group order per set of distinct lines (cache)
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
RM=[refl(v) for v in rep]
key=lambda M: tuple(x for r in M for y in r for x in y)
gcache={}
def gorder(lineset):
    if lineset in gcache: return gcache[lineset]
    seen={key(eye(n))}; fr=[eye(n)]
    while fr:
        nw=[]
        for M in fr:
            for l in lineset:
                P=mm(M,RM[l]); k=key(P)
                if k not in seen: seen.add(k); nw.append(P)
        fr=nw
    gcache[lineset]=len(seen); return len(seen)
def a3(t): return all(rank([rep[t[j]] for j in range(6) if j!=i])==3 for i in range(6))
a3cache={}
def A3(t):
    k=tuple(sorted(t))  # deletion ranks depend on multiset of lines only? depends on which deleted -> multiset suffices
    if k not in a3cache: a3cache[k]=a3(t)
    return a3cache[k]
results=[]
for root,mem in comps.items():
    s0=dec(mem[0]); go=gorder(frozenset(s0))
    if go!=54: results.append((len(mem),go,None,None,None)); continue
    best=0; witness=None; na3=0
    for x in mem:
        t=dec(x)
        if not A3(t): continue
        na3+=1
        br,bt,_=best_rank(t)
        if br>best: best,witness=br,(t,bt)
        if br==9: break
    results.append((len(mem),go,na3,best,witness))
full=[r for r in results if r[1]==54]
print('components generating G(3,3,3):',len(full),'; sizes:',sorted(r[0] for r in full))
print('components with rank-9 witness:',sum(1 for r in full if r[3]==9))
neg=[r for r in full if r[3]!=9]
print('NEGATIVE candidates (no rank-9 on any A3 node, exhaustive):',len(neg))
for r in neg: print('  size',r[0],'A3 nodes',r[2],'max rank',r[3],'example',r[4])
for r in full[:5]: print('  witness example: size',r[0],'tuple',r[4][0],'tree',r[4][1])
import json
json.dump([{'size':r[0],'order':r[1],'a3_nodes_scanned':r[2],'best':r[3],'witness':None if r[4] is None else [list(r[4][0]),[list(e) for e in r[4][1]]]} for r in results],open('g333_orbit_scan.json','w'))
