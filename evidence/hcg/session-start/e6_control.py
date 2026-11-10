"""H3 negative control (Claude, PROPOSED): on E^6 (E = C/Z[zeta6]) compare the rational (3,3)
Hodge space of H^6 with the span of triple products of 36 explicit divisors; also count A*-fixed
dimension (M-1). Reuses only the generic exterior-algebra helpers of h1_h2_exact_checks.py."""
import itertools, flint, io, contextlib
src = open('h1_h2_exact_checks.py').read()
helpers = src.split('# ================================================================ exterior algebra (exact, integer)')[1].split('# ================================================================ H2a')[0]
exec(helpers)
vol4=(0,1,2,3)
L_D3=[[1,0],[0,1],[1,0],[0,1]]; L_D4=[[1,0],[0,1],[1,-1],[1,0]]
def pd(L):
    import sympy as sp
    bas=basis(4,2)
    rhs=[pullback({b:1},L).get((0,1),0) for b in bas]
    P=sp.Matrix([[wedge({bi:1},{bj:1}).get(vol4,0) for bj in bas] for bi in bas])
    sol=P.T.solve(sp.Matrix(rhs)); return {bas[i]:int(sol[i]) for i in range(6) if sol[i]!=0}
Dl, Ga = pd(L_D3), pd(L_D4)
def relabel(alpha,m):
    out={}
    for I,c in alpha.items():
        seq=[m[i] for i in I]; k=tuple(sorted(seq)); out[k]=out.get(k,0)+perm_sign(seq)*c
    return {k:c for k,c in out.items() if c}
N=6
divs=[{(2*i,2*i+1):1} for i in range(N)]
for i,j in itertools.combinations(range(N),2):
    m={0:2*i,1:2*i+1,2:2*j,3:2*j+1}; divs+= [relabel(Dl,m), relabel(Ga,m)]
print("divisors:",len(divs))
DU,bas=DU_matrix(N,6)
hodge=len(bas)-DU.rank()
rows=[]
for c in itertools.combinations_with_replacement(range(len(divs)),3):
    w={():1}
    for t in c:
        w=wedge(w,divs[t])
        if not w: break
    if w: rows.append(vec(w,bas))
rk=flint.fmpz_mat(rows).rank()
print("E^6 H^6: dim (3,3) rational Hodge =",hodge," rank of divisor triple products =",rk)
