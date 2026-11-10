"""Independent principle for the cup form: monodromy of the Hurwitz family on H1_par at tuple #5, including
NON-commuting elements beta*twist*beta^-1 (beta random Artin words). Tests (a) S is invariant under every element,
(b) the Q-dimension of all invariant sesquilinear forms. dim 2 => the intersection form is a K-multiple of S,
and skew-Hermitian forces a rational multiple: (H2),(H3) are then convention-free up to one global sign."""
import os, json, random, hashlib, flint
os.environ['ROOTS_JSON']='roots_alt_5.json'
import g34_gateB as B
refl=B.refl
def move(roots,U,i,inverse=False):
    gi=refl(roots[i]); gj=refl(roots[i+1]); u0,u1=U[i],U[i+1]
    if not inverse:   # (g_i,g_{i+1}) -> (g_i g_{i+1} g_i^-1, g_i)
        newv=B.matvec(gi,roots[i+1]); gn=refl(newv)
        U[i]=B.vsub(B.vadd(u0,B.matvec(gi,u1)),B.matvec(gn,u0)); U[i+1]=u0
        roots[i],roots[i+1]=newv,roots[i]
    else:             # (g_i,g_{i+1}) -> (g_{i+1}, g_{i+1}^-1 g_i g_{i+1})
        newv=B.matvec(gj,roots[i])
        U[i]=u1; U[i+1]=B.matvec(gj,B.vsub(B.vadd(u0,B.matvec(gi,u1)),u1))
        roots[i],roots[i+1]=roots[i+1],newv
def tuple_after(word):
    roots=[list(v) for v in B.V]; U=[[B.Z0]*6 for _ in range(20)]
    for i,inv in word: move(roots,U,i,inv)
    return roots
def return_k(roots,a,b,kmax=400):
    C=B.eye(6)
    for j in range(a,b+1): C=B.matmul(C,refl(roots[j]))
    Ck=B.eye(6)
    for k in range(1,kmax+1):
        Ck=B.matmul(Ck,C)
        if all(B.iszeromat(B.matsub(B.matmul(Ck,refl(roots[i])),B.matmul(refl(roots[i]),Ck))) for i in range(a,b+1)): return k
    return None
def T_of(word):
    cols=[]
    for z in B.comp:
        roots=[list(v) for v in B.V]; U=B.u_gen(z)
        for i,inv in word: move(roots,U,i,inv)
        for t in range(20): assert B.iszeromat(B.matsub(refl(roots[t]),B.G[t])), "no return"
        a=[]
        for t in range(20):
            v=B.V[t]; j=next(q for q in range(6) if not B.iszero(v[q])); c=B.div(U[t][j],v[j])
            assert all(B.iszero(x) for x in B.vsub(U[t],B.vscale(c,v))); a.append(c)
        cols.append(B.coords(a))
    return [[cols[j][r] for j in range(8)] for r in range(8)]
# sanity: sigma then sigma^-1 = identity
assert B.iszeromat(B.matsub(T_of([(3,False),(3,True)]),B.eye(8)))
rng=random.Random(99); Ts=[]; words=[]
while len(Ts)<40:
    beta=[(rng.randrange(19),rng.random()<0.5) for _ in range(rng.randint(10,40))]
    roots=tuple_after(beta)
    L=rng.randint(2,4); a=rng.randrange(0,20-L+1); b=a+L-1
    k=return_k(roots,a,b)
    if k is None: continue
    tw=[(i,False) for i in range(a,b)]*((b-a+1)*k)
    word=beta+tw+[(i,not inv) for i,inv in reversed(beta)]
    T=T_of(word)
    if B.iszeromat(B.matsub(T,B.eye(8))): continue
    Ts.append(T); words.append(word)
Sinv=all(B.iszeromat(B.matsub(B.matmul(B.matmul([list(r) for r in zip(*T)],B.Sg),[[B.conj(x) for x in row] for row in T]),B.Sg)) for T in Ts)
noncomm=sum(1 for X in Ts for Y in Ts if not B.iszeromat(B.matsub(B.matmul(X,Y),B.matmul(Y,X))))
n=8; cols=[]
for i in range(n):
    for j in range(n):
        for unit in (B.ONE,B.W):
            col=[]
            for T in Ts:
                for p in range(n):
                    for q in range(n):
                        v=B.mul(B.mul(T[i][p],unit),B.conj(T[j][q]))
                        if p==i and q==j: v=B.sub(v,unit)
                        col+=[v[0],v[1]]
            cols.append(col)
M=flint.fmpq_mat([[flint.fmpq(cols[c][r].numerator,cols[c][r].denominator) for c in range(len(cols))] for r in range(len(cols[0]))])
dimQ=len(cols)-M.rank()
print("elements:",len(Ts)," non-commuting ordered pairs:",noncomm," S invariant under all:",Sinv," dim_Q invariant sesquilinear forms:",dimQ)
json.dump({"elements":len(Ts),"noncommuting_pairs":noncomm,"S_invariant":Sinv,"invariant_form_dim_Q":dimQ,"words":words,
           "script_sha256":hashlib.sha256(open(__file__,'rb').read()).hexdigest()},open('g34_w5_monodromy_forms_long.json','w'),indent=0)
