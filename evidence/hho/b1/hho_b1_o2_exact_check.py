"""Exact Q(omega) regression for DW06 Thm 2.5 versus HCG triangular cup B.
No other scientific engine is used; 9 entries only (not a general proof).
"""
from fractions import Fraction as F
from dataclasses import dataclass

@dataclass(frozen=True)
class K:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))
    @staticmethod
    def get(z):
        return z if isinstance(z, K) else K(z)
    def __add__(self, z):
        z = K.get(z)
        return K(self.a+z.a, self.b+z.b)
    __radd__ = __add__
    def __neg__(self): return K(-self.a, -self.b)
    def __sub__(self, z): return self + -K.get(z)
    def __rsub__(self, z): return K.get(z) - self
    def __mul__(self, z):
        z = K.get(z)
        return K(self.a*z.a-self.b*z.b, self.a*z.b+self.b*z.a-self.b*z.b)
    __rmul__ = __mul__
    def conj(self): return K(self.a-self.b, -self.b)
    def norm(self): return self.a*self.a-self.a*self.b+self.b*self.b
    def __truediv__(self, z):
        z = K.get(z)
        q = z.conj()
        return self * K(q.a/z.norm(), q.b/z.norm())
    def __rtruediv__(self, z): return K.get(z)/self
    def __pow__(self, n):
        if n < 0: return (K(1)/self)**(-n)
        s, q = K(1), self
        while n:
            if n & 1: s *= q
            q *= q
            n //= 2
        return s

w = K(0, 1)
g = [w, w**2, w, w**2]
q = [K(1)]
for z in g: q.append(q[-1]*z)
assert q[-1] == K(1)

def cycle(a,b,c):
    x = [K.get(a),K.get(b),K.get(c),K(0)]
    x[3] = -sum((q[i]*x[i] for i in range(3)),K(0))/q[3]
    assert sum((q[i]*x[i] for i in range(4)),K(0)) == K(0)
    return x

def h(x,y): return x*y.conj()

def triangular(x,y):
    value=K(0)
    for i in range(4):
        F_i=sum((q[j]*x[j] for j in range(i)),K(0))
        value+=h(F_i/q[i]+x[i]/(1-g[i]),y[i])
    return value

def DW(x,y):
    value=K(0)
    for i in range(4):
        A_i=x[i]/(1-g[i])
        value+=h(A_i,y[i]/g[i])
        for j in range(i):
            R=K(1)
            for k in range(j,i): R*=g[k]
            value+=h(A_i,(1/g[i]-1)*y[j]/R)
    return value

basis=[cycle(1,0,0),cycle(0,1,0),cycle(0,0,1)]
for x in basis:
    for y in basis:
        assert triangular(x,y)==DW(x,y)
print("O2 exact rank-one regression: 9/9 entries PASS")
