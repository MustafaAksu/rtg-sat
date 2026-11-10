"""Cross-check of crossing-interval twists by elementary Artin moves (sigma_i: (g_i,g_{i+1}) -> (g_i g_{i+1} g_i^-1, g_i)),
independent of the closed c g c^-1 formula; then test commutation of twists along CROSSING curves."""
import os
os.environ['ROOTS_JSON']='roots_alt_5.json'
import g34_gateB as B
def refl(v): return B.refl(v)
def braid_T(word):
    """word: list of 0-based i (sigma_i), applied left to right; tuple must return. Returns 8x8 matrix."""
    cols=[]
    for z in B.comp:
        roots=[list(v) for v in B.V]; U=B.u_gen(z)
        for i in word:
            gi=refl(roots[i]); gj=refl(roots[i+1])
            newv=B.matvec(gi,roots[i+1])                     # root of g_i g_{i+1} g_i^-1
            gnew=refl(newv)
            u0,u1=U[i],U[i+1]
            U[i]=B.vsub(B.vadd(u0,B.matvec(gi,u1)),B.matvec(gnew,u0)); U[i+1]=u0
            roots[i],roots[i+1]=newv,roots[i]
        for t in range(20): assert B.iszeromat(B.matsub(refl(roots[t]),B.G[t])), "tuple did not return"
        a=[]
        for t in range(20):
            v=B.V[t]; j=next(q for q in range(6) if not B.iszero(v[q])); c=B.div(U[t][j],v[j])
            assert all(B.iszero(x) for x in B.vsub(U[t],B.vscale(c,v))); a.append(c)
        cols.append(B.coords(a))
    return [[cols[j][r] for j in range(8)] for r in range(8)]
def full_twist_word(a,b,k):   # 0-based inclusive interval, (sigma_a...sigma_{b-1})^{(b-a+1)k}
    return ([i for i in range(a,b)])*((b-a+1)*k)
for (a1,b1) in [(1,2),(2,3),(3,4),(2,5),(1,3)]:
    k,C=B.return_power(a1-1,b1-1)
    Tf=B.T_matrix(a1-1,b1-1,k); Tb=braid_T(full_twist_word(a1-1,b1-1,k))
    print(f"[{a1},{b1}] k={k}: closed formula == elementary braids:",B.iszeromat(B.matsub(Tf,Tb)), " T==I:",B.iszeromat(B.matsub(Tf,B.eye(8))))
T12=B.T_matrix(0,1,1); k,_=B.return_power(1,2); T23=B.T_matrix(1,2,k)
print("T[1,2] and T[2,3] commute:",B.iszeromat(B.matsub(B.matmul(T12,T23),B.matmul(T23,T12))))
