exec(open('/home/claude/g34/h4sel/toy/toy_mixed.py').read().split("hist={}; best=[]")[0])
zero={dg for dg in diags if all(x==0 for x in flat[dg])}
print('zero operators:',len(zero),sorted((u+1,v) for u,v in zero))
# classify cut by line content: count of each line inside interval [u+1,v]
def content(dg):
    u,v=dg; pos=range(u+1,v+1); return tuple(sum(1 for p in pos if (p-1)//4==L) for L in range(3))
from collections import Counter
nz=Counter(); joint=Counter()
for t in T:
    k=sum(1 for d in t if d not in zero)
    r=qrank([flat[d] for d in t]); joint[(k,r)]+=1
print('(#nonzero ops in tree, rank) counts:',sorted(joint.items()))
print('rank-1 ops?', Counter(rank(OPS[d][0]) for d in diags if d not in zero))
for d in sorted(diags):
    if d in zero: continue
    print((d[0]+1,d[1]),'content',content(d),'ordC',OPS[d][1],'rankK',rank(OPS[d][0]))
