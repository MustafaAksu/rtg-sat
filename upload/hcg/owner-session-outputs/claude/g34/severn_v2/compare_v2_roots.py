# Compare the roots printed in Severn v2 Appendix A with the deposited tuple_pairs_D3.json (v0.5 deposit).
# Exact arithmetic in Q(w), w^2+w+1=0, elements as (a,b) = a + b w with Fractions.
import json, sys
from fractions import Fraction as F
W=lambda a,b=0:(F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): # (a+bw)(c+dw) = ac + (ad+bc)w + bd w^2, w^2=-1-w
    a,b=x;c,d=y; return (a*c-b*d, a*d+b*c-b*d)
def conj(x): a,b=x; return (a-b,-b)
def neg(x): return (-x[0],-x[1])
def sc(x,y): return mul(conj(x),y)
one=W(1); w=W(0,1); mw1=W(-1,-1)  # -1-w
roots={1:[one,mw1,one,w,mw1,w],6:[one,mw1,w,w,w,w],2:[one,W(0),W(0),W(1,1),W(0),W(0)],7:[W(0),W(0),one,W(0),W(0),W(-1)],
3:[W(0),one,W(1,1),W(0),W(0),W(0)],8:[one,w,w,mw1,one,mw1],4:[one,w,mw1,w,mw1,one],9:[one,neg(w),W(0),W(0),W(0),W(0)],
5:[one,mw1,mw1,mw1,mw1,w],10:[W(0),one,W(0),W(0),W(0),W(-1)]}
def refl(v):
    nn=W(0)
    for x in v: nn=add(nn,sc(x,x))
    assert nn[1]==0
    M=[[W(1) if i==j else W(0) for j in range(6)] for i in range(6)]
    for i in range(6):
        for j in range(6):
            M[i][j]=add(M[i][j], neg(mul(W(2/nn[0]), mul(v[i],conj(v[j])))))
    return M
dep=json.load(open(sys.argv[1]))
def parse(M): return [[(F(e[0]),F(e[1])) for e in row] for row in M]
depM=[parse(M) for M in dep]
# paired tuple: entries 0,1 = s1; 2,3 = s2; ...
ok=True
for i in range(10):
    R=refl(roots[i+1])
    for k in (2*i,2*i+1):
        same = (R==depM[k]); okT=(R==[list(map(tuple,r)) for r in zip(*depM[k])])
        if not same:
            ok=False; print('pair',i+1,'entry',k,'matches:',same,'transpose:',okT)
print('v2 printed roots reproduce deposited tuple_pairs_D3.json exactly:',ok)
# sanity: involutions
for i in range(10):
    R=refl(roots[i+1]); sq=[[W(0)]*6 for _ in range(6)]
    for a in range(6):
        for b in range(6):
            s=W(0)
            for c in range(6): s=add(s,mul(R[a][c],R[c][b]))
            sq[a][b]=s
    assert sq==[[W(1) if a==b else W(0) for b in range(6)] for a in range(6)]
print('all ten printed reflections are involutions')
