"""Claude: independent check of ChatGPT's G(3,3,3) mixed real/non-real example: group order, real W(A2) subgroup,
character field (trace of central element), A3, and the paired tree via actual twists (reconstruct script)."""
import sys,json
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
from sympy.combinatorics import Permutation, PermutationGroup
q=lambda a,b=0:(F(a),F(b)); W_=(F(0),F(1))
R=[[q(1),q(-1),q(0)],[q(0),q(1),q(-1)],[q(1),q(0),q(-1)],[q(1),q(0),neg(W_)],[q(1),neg(W_),q(0)],[q(0),q(1),neg(W_)]]
n=3
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
S=[refl(v) for v in R]
def closure(gens):
    key=lambda M: tuple(x for r in M for y in r for x in y)
    seen={key(eye(n)):eye(n)}; fr=[eye(n)]
    while fr:
        nw=[]
        for M in fr:
            for g in gens:
                P=mm(M,g); k=key(P)
                if k not in seen: seen[k]=P; nw.append(P)
        fr=nw
    return list(seen.values())
G2=closure(S[:2]); G=closure(S)
print('order <s1,s2> =',len(G2),'; all matrices rational:',all(x[1]==0 for M in G2 for r in M for x in r))
print('order <s1..s4> =',len(closure(S[:4])),'; full group order =',len(G))
wI=[[W_ if i==j else Z for j in range(n)] for i in range(n)]
print('omega*I in group:',wI in G,'; trace =',add(add(W_,W_),W_))
print('A3 deletion ranks:',[rank([R[j] for j in range(6) if j!=i]) for i in range(6)])
json.dump({'final_roots':[[ [str(x[0]),str(x[1])] for x in v] for v in R]},open('g333_roots.json','w'))
