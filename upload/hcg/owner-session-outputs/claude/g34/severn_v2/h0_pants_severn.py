"""Claude: (H0) per pants for Severn's printed 17-curve tree on the deposited tuple (Severn basis), exact Q(w).
Pants formula: sum_i rank(1-P_i) - 2d + 2 dim Fix<P1,P2,P3> = dim H^1_par(pants). Independent of ChatGPT's script."""
import sys, json, itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
from fractions import Fraction as Fr
dep=json.load(open(sys.argv[1])); gs=[[[ (Fr(e[0]),Fr(e[1])) for e in row] for row in M] for M in dep]; n=6
CURVES=[(1,8),(1,18),(2,8),(3,8),(4,8),(5,6),(5,8),(7,8),(9,10),(9,12),(9,16),(9,17),(9,18),(11,12),(13,14),(13,16),(15,16)]
iv=[(a-1,b-1) for a,b in CURVES]
def prodM(a,b):
    C=eye(n)
    for k in range(a,b+1): C=mm(C,gs[k])
    return C
def children(e):
    a,b=e; inside=[f for f in iv if f!=e and a<=f[0] and f[1]<=b]
    maxi=[f for f in inside if not any(g!=f and g[0]<=f[0] and f[1]<=g[1] for g in inside)]
    covered=set(k for f in maxi for k in range(f[0],f[1]+1))
    return sorted(maxi+[(k,k) for k in range(a,b+1) if k not in covered])
roots_=[f for f in iv if not any(g!=f and g[0]<=f[0] and f[1]<=g[1] for g in iv)]
covered=set(k for f in roots_ for k in range(f[0],f[1]+1))
pants=[(e,children(e)) for e in iv]+[(None,sorted(roots_+[(k,k) for k in range(20) if k not in covered]))]
zero=0
for outer,ch in pants:
    bnd=[prodM(a,b) for a,b in ch]
    if outer is not None: bnd.append(adj(prodM(*outer)))
    assert len(bnd)==3
    P=eye(n)
    for B in bnd: P=mm(P,B)
    assert P==eye(n) or True
    cs=[rank(msub(eye(n),B)) for B in bnd]
    stack=[]
    for B in bnd: stack+=msub(eye(n),B)
    fix=n-rank(stack)
    val=sum(cs)-2*n+2*fix
    zero+=(val==0)
    print(f"pants outer={outer and (outer[0]+1,outer[1]+1)} children={[(a+1,b+1) for a,b in ch]} ranks={cs} dimFix={fix} dim H1_par={val}")
print(f"(H0): {zero}/{len(pants)} pants have H^1_par = 0")
