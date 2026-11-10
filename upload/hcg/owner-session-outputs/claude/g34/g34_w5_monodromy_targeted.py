"""Targeted search for monodromy elements beta^-1 * sigma_i^2 * beta (Picard-Lefschetz type) at adjacent EQUAL reflections
of tuple' = beta(tuple), keeping those whose image is NOT inside the common 4-dim subspace I0 found before.
Then: S invariance and dimension of invariant sesquilinear forms."""
import os, json, random, hashlib, flint
os.environ['ROOTS_JSON']='roots_alt_5.json'
import g34_gateB as B
src=open('g34_w5_monodromy_forms.py').read()
exec(src[src.index("refl=B.refl"):src.index("# sanity")])
# I0 from the balanced decomposition monodromies
I0=[]
for (a,b) in [(2*i-1,2*i) for i in range(1,11)]:
    T=B.T_matrix(a-1,b-1,1); D=B.matsub(T,B.eye(8)); I0+=[[D[i][j] for i in range(8)] for j in range(8)]
R0,_=B.rref(I0); I0=[v for v in R0 if any(not B.iszero(x) for x in v)]
print("dim I0 (pair transvections):",len(I0))
def same_line(v,w): return B.rank([v,w])==1
rng=random.Random(2027); found=[]; tried=0
while len(found)<8 and tried<600:
    tried+=1
    beta=[(rng.randrange(19),rng.random()<0.5) for _ in range(rng.randint(3,30))]
    roots=tuple_after(beta)
    for i in range(19):
        if same_line(roots[i],roots[i+1]):
            word=beta+[(i,False),(i,False)]+[(j,not inv) for j,inv in reversed(beta)]
            T=T_of(word); D=B.matsub(T,B.eye(8))
            cols=[[D[p][q] for p in range(8)] for q in range(8)]
            if B.rank(I0+cols)>len(I0): found.append((word,T)); print("new vanishing direction found after",tried,"braids",flush=True)
            break
Ts=[T for _,T in found]
for (a,b) in [(2*i-1,2*i) for i in range(1,11)]: Ts.append(B.T_matrix(a-1,b-1,1))
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
print("braids tried:",tried," new elements:",len(found)," non-commuting pairs:",noncomm," S invariant:",Sinv," dim_Q invariant forms:",dimQ)
json.dump({"tried":tried,"new_elements":len(found),"noncommuting_pairs":noncomm,"S_invariant":Sinv,"invariant_form_dim_Q":dimQ,
  "words":[w for w,_ in found],"script_sha256":hashlib.sha256(open(__file__,'rb').read()).hexdigest()},open('g34_w5_monodromy_targeted.json','w'),indent=0)
