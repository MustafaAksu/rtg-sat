"""Exact check of the computations in Example 12.2 of Severn, hexagon:2610.00387v2 (section 12).

Quaternion algebra D = (a,b)_Q with a = -3, b = -1, basis 1,u,v,uv, K = Q(u). For a pure quaternion
t = alpha*u + beta*v + gamma*uv it checks: the reduced norm 3alpha^2 + beta^2 + 3gamma^2; the Gram matrix of the
K-component of conj(x)*t*y in the basis 1,v of D = K + vK; its determinant -b*nrd(t); and the two products of
reduced norms 45 and 396. It checks arithmetic only: not the polarization conditions, not Corollary 12.1.
Standard library only. Usage: python3 evidence/hcg/verification/severn_v2_example_12_2_check.py
"""
from fractions import Fraction as F
a, b = F(-3), F(-1)
def mul(x, y):  # basis 1,u,v,uv ; u^2=a, v^2=b, vu=-uv
    x0,x1,x2,x3 = x; y0,y1,y2,y3 = y
    return (x0*y0 + a*x1*y1 + b*x2*y2 - a*b*x3*y3,
            x0*y1 + x1*y0 - b*x2*y3 + b*x3*y2,
            x0*y2 + x2*y0 + a*x1*y3 - a*x3*y1,
            x0*y3 + x3*y0 + x1*y2 - x2*y1)
def conj(x): return (x[0], -x[1], -x[2], -x[3])
def nrd(x): return mul(x, conj(x))[0]
one, u, v = (F(1),0,0,0), (0,F(1),0,0), (0,0,F(1),0)
uv = mul(u, v)
assert mul(u,u) == (a,0,0,0) and mul(v,v) == (b,0,0,0) and mul(v,u) == tuple(-c for c in uv)
def Kcomp(x):  # D = K + vK as right K-space: x = k1 + v*k2 ; v*(p+q u) = p v + q v u = p v - q uv
    return (x[0], x[1])            # k1 = x0 + x1 u
def kmul(p, q): return (p[0]*q[0] + a*p[1]*q[1], p[0]*q[1] + p[1]*q[0])
def gram(t):
    basis = [one, v]
    return [[Kcomp(mul(mul(conj(x), t), y)) for y in basis] for x in basis]
def det2(G):
    p = kmul(G[0][0], G[1][1]); q = kmul(G[0][1], G[1][0])
    return (p[0]-q[0], p[1]-q[1])
def lin(al, be, ga): return (F(0), F(al), F(be), F(ga))
for al, be, ga in [(1,2,3), (2,-1,5), (0,1,0), (1,0,2)]:
    t = lin(al, be, ga)
    assert nrd(t) == 3*al*al + be*be + 3*ga*ga
    G = gram(t)
    assert G[0][0] == (0, F(al)) and G[1][1] == (0, b*al)
    assert G[0][1] == (b*be, b*ga) and G[1][0] == (-b*be, b*ga)
    assert det2(G) == (-b*nrd(t), 0)
for forms, prod in [([(0,1,0),(1,0,0),(1,0,2)], 45), ([(1,4,1),(1,0,0),(1,0,1)], 396)]:
    P = 1
    for f in forms: P *= nrd(lin(*f))
    assert P == prod
print('Example 12.2: Gram matrices, determinant -b*nrd(t), nrd = 3a^2+b^2+3c^2, products 45 and 396: all confirmed')
