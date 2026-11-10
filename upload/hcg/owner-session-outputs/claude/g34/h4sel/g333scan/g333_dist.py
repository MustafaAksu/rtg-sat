"""Claude: rank distribution over ALL A3-valid nodes of the single generating component (exhaustive)."""
exec(open('g333_orbit_scan.py').read().split("results=[]")[0]+"\n")
from collections import Counter
big=max(comps.values(),key=len)
hist=Counter(); na3=0; gen=0
for x in big:
    t=dec(x)
    if not A3(t): hist['A3-fail']+=1; continue
    hist[best_rank(t)[0]]+=1
print('component size',len(big),'; distribution of best pair-tree rank over its nodes:',dict(hist))
nongen=sum(len(m) for m in comps.values() if m is not big)
print('tuples outside it (non-generating):',nongen,'; total',N)
