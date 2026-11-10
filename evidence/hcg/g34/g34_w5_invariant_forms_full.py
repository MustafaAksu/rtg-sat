"""As g34_w5_invariant_forms.py, but with monodromies of MANY interval twists on tuple #5 (lengths 2..6, all positions,
exact return powers), which generate a non-abelian subgroup of the monodromy of the Hurwitz component."""
import os, json, hashlib, flint
os.environ['ROOTS_JSON']='roots_alt_5.json'
import g34_gateB as B
Ts=[]; used=[]
for L in range(2,7):
    for a in range(1,20-L+2):
        b=a+L-1; k,C=B.return_power(a-1,b-1,kmax=400)
        if k is None: continue
        Ts.append(B.T_matrix(a-1,b-1,k)); used.append((a,b,k))
n=8; cols=[]
from fractions import Fraction as F
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
dimQ=len(cols)-M.rank()
# S itself must be invariant
inv_ok=all(B.iszeromat(B.matsub(B.matmul(B.matmul([list(r) for r in zip(*T)],B.Sg),[[B.conj(x) for x in row] for row in T]),B.Sg)) for T in Ts)
print("twists used:",len(Ts)," S invariant under all:",inv_ok," dim_Q invariant sesquilinear forms:",dimQ)
json.dump({"twists":used,"S_invariant":inv_ok,"invariant_form_dim_Q":dimQ,
           "script_sha256":hashlib.sha256(open(__file__,'rb').read()).hexdigest()},open('g34_w5_invariant_forms_full.json','w'),indent=1)
