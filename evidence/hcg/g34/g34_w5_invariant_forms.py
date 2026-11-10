"""Robustness of (H2)/(H3) to the cup-form derivation: dimension of the space of sesquilinear forms X on H1_par
invariant under all 17 W5 monodromies T_j (X(Tx,Ty)=X(x,y), i.e. T^t X conj(T) = X). If it is K*S (Q-dim 2), the true
intersection form equals lambda*S with lambda in K, and skew-Hermitian forces lambda in Q: (H2),(H3) hold up to one global sign."""
import json, hashlib, flint
from fractions import Fraction as F
d=json.load(open('g34_cert_tuple5_balanced.json'))
def K(p): return (F(p[0]),F(p[1]))
def mul(x,y): a,b=x; c,e=y; return (a*c-b*e,a*e+b*c-b*e)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def conj(x): return (x[0]-x[1],-x[1])
Ts=[[[K(x) for x in row] for row in c['T']] for c in d['curves']]
n=8; cols=[]
for i in range(n):
    for j in range(n):
        for unit in ((F(1),F(0)),(F(0),F(1))):
            col=[]
            for T in Ts:
                # (T^t X conj T)_{ab} - X_{ab} with X = unit*E_ij
                for a in range(n):
                    for b in range(n):
                        v=mul(mul(T[i][a],unit),conj(T[j][b]))
                        if a==i and b==j: v=(v[0]-unit[0],v[1]-unit[1])
                        col+=[v[0],v[1]]
            cols.append(col)
M=flint.fmpq_mat([[flint.fmpq(cols[c][r].numerator,cols[c][r].denominator) for c in range(len(cols))] for r in range(len(cols[0]))])
dimQ=len(cols)-M.rank()
print("dim_Q of T-invariant sesquilinear forms on H1_par:",dimQ," (2 => unique up to K-scalar)")
json.dump({"invariant_form_dim_Q":dimQ,"cert_sha256":hashlib.sha256(open('g34_cert_tuple5_balanced.json','rb').read()).hexdigest(),
           "script_sha256":hashlib.sha256(open(__file__,'rb').read()).hexdigest()},open('g34_w5_invariant_forms.json','w'),indent=1)
