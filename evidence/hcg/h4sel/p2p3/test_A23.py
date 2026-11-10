"""ChatGPT note §A, Corollaries A2 and A3, exact check on W5 and NEW01 roots (Claude, generic engine arithmetic)."""
import sys,json; sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
def Kc(p): return (F(p[0]),F(p[1]))
out=[]
for lab,path,key in [('W5','/home/claude/g34/roots_alt_5.json','generating_reflection_roots'),
                     ('NEW01','/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT/NEW01_roots.json',None)]:
    J=json.load(open(path))
    if key is None: key=[k for k in J if isinstance(J[k],list)][0]
    V=[[Kc(c) for c in v] for v in J[key]]; m=len(V); n=len(V[0])
    A=[[V[i][r] for i in range(m)] for r in range(n)]
    Lb=nullspace(A,m); d=len(Lb)
    def Bform(e):
        Fv=[ [ __import__('functools').reduce(add,[mul(t[i],V[i][r]) for i in e],Z) for r in range(n)] for t in Lb]
        return [[h(Fv[p],Fv[q]) for q in range(d)] for p in range(d)]
    def C(i,j):
        zi=[[mul(t[i],x) for x in V[i]] for t in Lb]; zj=[[mul(t[j],x) for x in V[j]] for t in Lb]
        return [[add(h(zi[p],zj[q]),h(zj[p],zi[q])) for q in range(d)] for p in range(d)]
    def madd(*Ms): 
        R=[[Z]*d for _ in range(d)]
        for c,M in Ms: R=[[add(a,mul(c,b)) for a,b in zip(r,s)] for r,s in zip(R,M)]
        return R
    one=ONE; mone=neg(ONE); two=(F(2),F(0))
    a2=all(madd((two,Bform([i])),*[(one,C(i,j)) for j in range(m) if j!=i])==[[Z]*d for _ in range(d)] for i in range(m))
    def BI(i,j): return Bform(list(range(i,j+1))) if i<=j else [[Z]*d for _ in range(d)]
    a3=all(C(i,j)==madd((one,BI(i,j)),(mone,BI(i+1,j)),(mone,BI(i,j-1)),(one,BI(i+1,j-1))) for i in range(m) for j in range(i+1,m))
    # cut formula (P1) on all 2^(m-1)-1 proper subsets containing index 0 sampled: all subsets of size <=3
    import itertools
    cut=all(Bform(list(e))==madd(*[((F(-1,2),F(0)),C(i,j)) for i in e for j in range(m) if j not in e]) for k in (1,2,3) for e in itertools.combinations(range(m),k))
    s=f'[A:{lab}] m={m} d={d}: A2 holds {a2}; A3 holds for all {m*(m-1)//2} pairs {a3}; cut formula on all subsets of size<=3 {cut}'
    print(s); out.append(s)
open('test_A23_out.txt','w').write('\n'.join(out)+'\n')
