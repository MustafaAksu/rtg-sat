"""Independent (Claude) check of ChatGPT's rank-obstruction claims. For fixed roots (10 pairs, fixed cyclic order):
 - rho_all_cyclic: Q-rank of the 45 cyclic-interval cut forms (10 pairs + 35 decagon diagonals)
 - rho_all_subsets: Q-rank of all 511 subset forms (up to complement)
 - all 1430 decagon triangulations (planar pair-containing trees): rank distribution.
Edge forms B_A(t,t') = h(F_A t, F_A t') on L = ker(t -> sum t_i v_i), via edgeform_predict primitives."""
import json, sys, itertools
from fractions import Fraction as F
from functools import reduce
from collections import Counter
sys.path.insert(0,'/home/claude/g34/h4sel/edgeform')
import edgeform_predict as P
import flint
def forms(V,L,subsets):
    out={}
    for S in subsets:
        X=[[reduce(P.add,[P.mul(t[i],V[i][k]) for i in S],P.Z) for k in range(len(V[0]))] for t in L]
        B=[[P.h(X[p],X[q]) for q in range(len(L))] for p in range(len(L))]
        c=[B[p][p][0] for p in range(len(L))]
        for p in range(len(L)):
            for q in range(p+1,len(L)): c+=[B[p][q][0],B[p][q][1]]
        out[S]=[flint.fmpq(x.numerator,x.denominator) for x in c]
    return out
def rank(rows): return flint.fmpq_mat(rows).rank() if rows else 0
def triangulations(lo,hi):   # polygon vertices lo..hi (hi>lo+1): list of diagonal sets (pairs (a,b), not sides)
    if hi-lo<2: return [frozenset()]
    res=[]
    for k in range(lo+1,hi):
        for A in triangulations(lo,k):
            for B in triangulations(k,hi):
                d=set(A)|set(B)
                if k-lo>1: d.add((lo,k))
                if hi-k>1: d.add((k,hi))
                res.append(frozenset(d))
    return res
def canon(S,m):  # subset up to complement
    S=frozenset(S); C=frozenset(range(m))-S
    return min(tuple(sorted(S)),tuple(sorted(C)))
def run(roots):
    V=[[(F(str(a)),F(str(b))) for a,b in v] for v in roots]; m=len(V); n=len(V[0])
    L=P.nullspace([[V[i][k] for i in range(m)] for k in range(n)],m)
    # decagon vertices 0..m-1; side (j,j+1 mod m) <-> pair j ; diagonal (a,b) a<b <-> pairs {a..b-1}
    cyc=set()
    for a in range(m):
        for b in range(a+1,m+1):
            S=frozenset(range(a,b))
            if 0<len(S)<m: cyc.add(canon(S,m))
    allsub=set(canon(S,m) for r in range(1,m) for S in itertools.combinations(range(m),r))
    Fm=forms(V,L,allsub)
    pair=[canon({i},m) for i in range(m)]
    res=dict(m=m,n=n,dimL=len(L),rank_pairs=rank([Fm[p] for p in pair]),
             n_cyclic=len(cyc),rho_all_cyclic=rank([Fm[s] for s in cyc]),
             n_subsets=len(allsub),rho_all_subsets=rank([Fm[s] for s in allsub]))
    T=triangulations(0,m-1)   # triangulations of polygon with vertices 0..m-1  (m-gon)
    dist=Counter()
    for tri in T:
        curves=[canon(set(range(a,b)),m) for a,b in tri]
        dist[rank([Fm[p] for p in pair]+[Fm[c] for c in curves])]+=1
    res.update(n_trees=len(T),tree_rank_distribution=dict(sorted(dist.items())))
    return res
if __name__=='__main__':
    for f in sys.argv[1:]:
        r=run(json.load(open(f))['generating_reflection_roots']); print(f.split('/')[-1],json.dumps(r))
