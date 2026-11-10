"""Claude: provenance + per-tuple check. (a) uncached best rank per A3-valid tuple of the generating component (as in
g333_dist.py); (b) independently, best rank of the canonical representative under simultaneous conjugation by the
line-permutation action of G(3,3,3). Compare per tuple; write the per-tuple table (tuple code -> rank) with a hash."""
exec(open('g333_orbit_scan.py').read().split("results=[]")[0])
import hashlib
from collections import Counter
gens=[tuple(ACT[i][j] for i in range(NL)) for j in range(NL)]
perms={tuple(range(NL))}; fr=list(perms)
while fr:
    nw=[]
    for pp in fr:
        for g in gens:
            q=tuple(g[pp[i]] for i in range(NL))
            if q not in perms: perms.add(q); nw.append(q)
    fr=nw
perms=list(perms); print('line permutation group size:',len(perms),flush=True)
big=max(comps.values(),key=len)
canon_cache={}; mism=0; hist=Counter(); rows=[]
for x in sorted(big):
    t=dec(x)
    if not A3(t): hist['A3-fail']+=1; rows.append(f'{x} F'); continue
    r_unc=best_rank(t)[0]
    c=min(tuple(pp[a] for a in t) for pp in perms)
    if c not in canon_cache:
        cache.pop(c,None)          # force fresh evaluation of the canonical rep
        canon_cache[c]=best_rank(c)[0]
    if canon_cache[c]!=r_unc: mism+=1
    hist[r_unc]+=1; rows.append(f'{x} {r_unc}')
tab='\n'.join(rows)+'\n'
open('g333_pertuple_table.txt','w').write(tab)
print('component size',len(big),'; histogram',dict(sorted(hist.items(),key=str)))
print('conjugation classes',len(canon_cache),'; per-tuple mismatches (uncached vs canonical-class):',mism)
print('per-tuple table sha256:',hashlib.sha256(tab.encode()).hexdigest())
