"""Claude: flip-walk (simulated annealing) over H0-valid triangulations maximizing mod-p Q-rank of projected forms.
Imports the precomputation of new02_mixed_search.py by exec with NS=0."""
import sys, random, math
NAME=sys.argv[1]; SEED=int(sys.argv[2]); STEPS=int(sys.argv[3])
sys.argv=['x',str(SEED),NAME,'0']
exec(open('/home/claude/g34/h4sel/new02/new02_mixed_search.py').read())
random.seed(SEED)
def tris(T):
    Ds=set(T)|{(i,i+1) for i in range(19)}|{(0,19)}
    adj={i:set() for i in range(20)}
    for a,b in Ds: adj[a].add(b); adj[b].add(a)
    out=[]
    for a,b in Ds:
        for c_ in adj[a]&adj[b]:
            t=tuple(sorted((a,b,c_)))
            out.append(t)
    return set(out)
def flips(T):
    S=set(T); tr=tris(T); res=[]
    for dg in T:
        a,b=dg
        apex=[t for t in tr if a in t and b in t]
        others=[ [x for x in t if x not in dg][0] for t in apex]
        if len(others)!=2: continue
        c1,c2=sorted(others); nd=(c1,c2)
        if nd in S: continue
        t1=tuple(sorted((c1,c2,a))); t2=tuple(sorted((c1,c2,b)))
        if H0[t1] and H0[t2]: res.append((dg,nd))
    return res
found=[]
for restart in range(200):
    T=sample(0,19); r=rmod([FMOD[x] for x in T]); temp=1.0
    for step in range(STEPS):
        fl=flips(T)
        if not fl: break
        old,new=random.choice(fl); T2=[x for x in T if x!=old]+[new]
        r2=rmod([FMOD[x] for x in T2])
        if r2>=r or random.random()<math.exp((r2-r)/temp):
            T,r=T2,r2
        temp=max(0.05,temp*0.995)
        if r==16: break
    if r==16:
        T=sorted(T); ex=qrank([FORM[x] for x in T])
        print(f'restart {restart}: HIT exact rank {ex}; intervals {[(u+1,v) for u,v in T]}; all triangles H0 {all(H0[t] for t in tris(T))}')
        found.append(T)
        if len(found)>=3: break
    else:
        print(f'restart {restart}: best rank reached {r}')
json.dump({'name':NAME,'seed':SEED,'hits':[[(u+1,v) for u,v in T] for T in found]},open(f'/home/claude/g34/h4sel/new02/{NAME}_flip_hits.json','w'))
