import os, json
os.environ['ROOTS_JSON']='roots_alt_5.json'
import g34_gateB as B
exec(open('g34_w5_invariant_forms_full2.py').read().split("def inv_dim")[0].split("import g34_gateB as B")[1])
imgs=[]
for T in Ts:
    D=B.matsub(T,B.eye(8)); imgs+=[[D[i][j] for i in range(8)] for j in range(8)]
Ir,_=B.rref(imgs); Ib=[v for v in Ir if any(not B.iszero(x) for x in v)]
print("dim_K of sum of images of (T-1) over",len(Ts),"monodromies:",len(Ib))
comm=all(B.iszeromat(B.matsub(B.matmul(X,Y),B.matmul(Y,X))) for X in Ts for Y in Ts)
print("all monodromies commute:",comm)
