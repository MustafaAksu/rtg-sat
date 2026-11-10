"""Invariant sesquilinear forms on H1_par for tuple #5 under (a) half-twists sigma_{2i-1} (they fix the paired tuple),
(b) interval Dehn twists of ALL lengths 2..18 with exact return powers. Elementary Artin action implemented directly:
sigma_i: (g_i,g_{i+1}) -> (g_i g_{i+1} g_i^-1, g_i);  u'(g_i)=u(g_i)+rho(g_i)u(g_{i+1})-rho(g_i g_{i+1} g_i^-1)u(g_i), u'(g_{i+1})=u(g_i)."""
import os, json, hashlib, flint
os.environ['ROOTS_JSON']='roots_alt_5.json'
import g34_gateB as B
def half_twist_T(i):   # i 0-based, acts on positions i,i+1; requires tuple fixed
    cols=[]
    for z in B.comp:
        ug=B.u_gen(z); new=list(ug)
        gi=B.G[i]; gj=B.G[i+1]; conjg=B.matmul(B.matmul(gi,gj),gi)   # g_i g_{i+1} g_i^-1 (g_i involution)
        assert B.iszeromat(B.matsub(conjg,B.G[i]))                    # tuple fixed for a pair (s,s)
        new[i]=B.vsub(B.vadd(ug[i],B.matvec(gi,ug[i+1])),B.matvec(conjg,ug[i])); new[i+1]=ug[i]
        a=[]
        for t in range(20):
            v=B.V[t]; j=next(q for q in range(6) if not B.iszero(v[q])); c=B.div(new[t][j],v[j])
            assert all(B.iszero(x) for x in B.vsub(new[t],B.vscale(c,v))); a.append(c)
        cols.append(B.coords(a))
    return [[cols[j][r] for j in range(8)] for r in range(8)]
Ts=[half_twist_T(2*i) for i in range(10)]; used=[('half',2*i+1,2*i+2) for i in range(10)]
for L in range(2,19):
    for a in range(1,20-L+2):
        b=a+L-1; k,C=B.return_power(a-1,b-1,kmax=400)
        if k is None: continue
        Ts.append(B.T_matrix(a-1,b-1,k)); used.append((a,b,k))
def inv_dim(Ts):
    n=8; cols=[]
    for i in range(n):
        for j in range(n):
            for unit in (B.ONE,B.W):
                col=[]
                for T in Ts:
                    for a in range(n):
                        for b in range(n):
                            v=B.mul(B.mul(T[i][a],unit),B.conj(T[j][b]))
                            if a==i and b==j: v=B.sub(v,unit)
                            col+=[v[0],v[1]]
                cols.append(col)
    M=flint.fmpq_mat([[flint.fmpq(cols[c][r].numerator,cols[c][r].denominator) for c in range(len(cols))] for r in range(len(cols[0]))])
    return len(cols)-M.rank()
Sinv=all(B.iszeromat(B.matsub(B.matmul(B.matmul([list(r) for r in zip(*T)],B.Sg),[[B.conj(x) for x in row] for row in T]),B.Sg)) for T in Ts)
d_half=inv_dim(Ts[:10]); d_all=inv_dim(Ts)
print("half-twists only: dimQ =",d_half,"| half + all interval twists (",len(Ts),"elements): dimQ =",d_all," S invariant under all:",Sinv)
json.dump({"elements":len(Ts),"S_invariant":Sinv,"dimQ_half_only":d_half,"dimQ_all":d_all,
           "script_sha256":hashlib.sha256(open(__file__,'rb').read()).hexdigest()},open('g34_w5_invariant_forms_full2.json','w'),indent=1)
