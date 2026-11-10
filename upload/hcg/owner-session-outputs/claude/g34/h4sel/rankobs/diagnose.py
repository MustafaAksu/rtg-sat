import json, sys
from fractions import Fraction as F
sys.path.insert(0,'/home/claude/g34/h4sel/edgeform'); import edgeform_predict as P
def div(x,y): return P.mul(x,P.inv(y))
for f in sys.argv[1:]:
    V=[[(F(str(a)),F(str(b))) for a,b in v] for v in json.load(open(f))['generating_reflection_roots']]
    m=len(V); L=P.nullspace([[V[i][k] for i in range(m)] for k in range(6)],m)
    col=[[t[i] for t in L] for i in range(m)]          # coordinate functional t_i as vector over L basis
    classes=[]                                          # parallel classes: t_i = lambda t_j
    for i in range(m):
        for c in classes:
            j=c[0]; a=col[i]; b=col[j]
            k=next(p for p in range(len(b)) if not P.isz(b[p])); lam=div(a[k],b[k])
            if all(P.sub(a[p],P.mul(lam,b[p]))==P.Z for p in range(len(a))):
                c.append(i); break
        else: classes.append([i])
    orth=[(i+1,j+1) for i in range(m) for j in range(i+1,m) if P.h(V[i],V[j])==P.Z]
    print(f.split('/')[-1],'parallel classes of coordinate functionals (1-based pairs):',[[x+1 for x in c] for c in classes if len(c)>1],'| #classes',len(classes),'| orthogonal root pairs:',orth)
