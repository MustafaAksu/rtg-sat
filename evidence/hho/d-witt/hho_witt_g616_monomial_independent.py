"""Independent G(6,1,6) Witt-graph check for five recorded cases.

Representation: monomial permutations with sixth-root phase exponents.
Fixed dimensions are connected-component counts in a phase-labelled graph;
no matrices over Q(omega), no HCG/HHO code imports.
Source of the ordered cases:
  evidence/hho/code/g616.py (adopted HHO hho-v0.4)
This is only the graph-Euler w(T), not the period rank (D).
"""
from functools import lru_cache

DIM = 6
IDENT = (tuple(range(DIM)), (0,) * DIM)
PAIRS = [(0,1,1),(1,2,0),(2,3,2),(3,4,0),
         (4,5,1),(0,5,3),(1,3,1),(2,4,5)]

def diagonal(i, exponent):
    phases = list(IDENT[1]); phases[i] = exponent % 6
    return (IDENT[0], tuple(phases))

def transposition(i, j, phase):
    perm = list(range(DIM)); perm[i], perm[j] = perm[j], perm[i]
    phases = [0] * DIM
    phases[i], phases[j] = (-phase) % 6, phase % 6
    return tuple(perm), tuple(phases)

def paired(spec):
    return [g for i,j,a in spec for g in
            (transposition(i,j,a), transposition(i,j,a))]

def multiply(a,b):
    pa,za=a; pb,zb=b
    return (tuple(pa[pb[j]] for j in range(DIM)),
            tuple((zb[j]+za[pb[j]]) % 6 for j in range(DIM)))

def product(gs):
    r=IDENT
    for g in gs:r=multiply(r,g)
    return r

def fixed_dimension(*group_generators):
    """Common invariant space via graph of x_perm(j) = zeta6**phase x_j."""
    edges=[[] for _ in range(DIM)]
    for perm,phase in group_generators:
        for i in range(DIM):
            j=perm[i]
            edges[i].append((j,phase[i]))
            edges[j].append((i,(-phase[i])%6))
    exp=[None]*DIM
    dim=0
    for root in range(DIM):
        if exp[root] is not None:continue
        exp[root]=0; frontier=[root]; consistent=True
        for u in frontier:
            for v,ph in edges[u]:
                want=(exp[u]+ph)%6
                if exp[v] is None:
                    exp[v]=want; frontier.append(v)
                elif exp[v]!=want:
                    consistent=False
        if consistent:dim+=1
    return dim

def get_cases():
    return {
        'P1':[diagonal(0,3),diagonal(0,1),diagonal(0,4),diagonal(0,4)]+paired(PAIRS),
        'P2':[diagonal(3,3),diagonal(3,2),diagonal(3,2),diagonal(3,5)]+paired(PAIRS),
        'P3':[diagonal(0,3),diagonal(1,3),diagonal(1,3),diagonal(0,1),
              diagonal(0,4),diagonal(0,4)]+paired(PAIRS[:7]),
        'Q0':[diagonal(0,1),diagonal(0,5),diagonal(2,1),diagonal(2,5)]+paired(PAIRS),
        'Q2':[diagonal(0,3),diagonal(0,3),diagonal(4,1),diagonal(4,5)]+paired(PAIRS),
    }

def tree_bounds(gs):
    N=len(gs)
    assert N==20 and product(gs)==IDENT
    assert fixed_dimension(*gs)==0

    @lru_cache(maxsize=None)
    def arc(i,j):
        if i==j:return gs[i]
        return multiply(arc(i,j-1),gs[j])

    @lru_cache(maxsize=None)
    def node(i,j):
        if i==j:return (0,0,None,None)
        min_v=1000; max_v=-1000; min_k=max_k=None
        for k in range(i,j):
            low= node(i,k); high=node(k+1,j)
            left=arc(i,k);right=arc(k+1,j)
            contribution=((fixed_dimension(left) if k>i else 0)
                          +(fixed_dimension(right) if j>k+1 else 0)
                          -fixed_dimension(left,right))
            cand_min=low[0]+high[0]+contribution
            cand_max=low[1]+high[1]+contribution
            if cand_min<min_v: min_v,min_k=cand_min,k
            if cand_max>max_v: max_v,max_k=cand_max,k
        return (min_v,max_v,min_k,max_k)

    def direct_witness(i,j,maximum):
        if i==j:return 0,0,0
        k=node(i,j)[3 if maximum else 2]
        l=direct_witness(i,k,maximum); r=direct_witness(k+1,j,maximum)
        edge=l[1]+r[1]
        if k>i:edge+=fixed_dimension(arc(i,k))
        if j>k+1:edge+=fixed_dimension(arc(k+1,j))
        vert=l[2]+r[2]+fixed_dimension(arc(i,k),arc(k+1,j))
        return edge-vert,edge,vert

    low,high,*_=node(0,N-2)
    lo=direct_witness(0,N-2,False);hi=direct_witness(0,N-2,True)
    assert low==lo[0] and high==hi[0]
    return low,high,lo,hi

if __name__=='__main__':
    expect={'P1':3,'P2':3,'P3':3,'Q0':4,'Q2':4}
    for name, gs in get_cases().items():
        lo,hi,lw,hw=tree_bounds(gs)
        assert (lo,hi)==(expect[name],expect[name])
        print(f'{name}: N=20, all Catalan(18)=477638700 planar trees; '
              f'w min/max={lo}/{hi}; maximal witness edges={hw[1]}, '
              f'vertices={hw[2]} PASS')
    print('ALL PASS: independent weighted-monomial invariant-graph method; not (D)')
