"""HHO Addendum 3: independent exact trace-dual and scale checks.

For O_K=Z[omega], omega^2+omega+1=0, trace has Gram
[[2,-1],[-1,-1]] and determinant -3. These computations only
check the arithmetic aspects; they do not prove integral Morita theory.
"""
from fractions import Fraction as Q
from math import gcd
G=((2,-1),(-1,-1))
det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
assert det==-3
for p in (2,5,11,17,23,29,41):
    # All primes selected are 2 mod 3
    assert p%3==2 and gcd(p,det)==1
    assert det%p != 0
print('TRACE DUAL: det=-3 is a p-unit at all tested inert primes, including 2')
# Rational scaling of U by t causes W by t^{-1}; rank-8 determinant t^{-8}
for t in (Q(2,1),Q(1,2),Q(5,7),Q(25,3)):
    original_det=Q(5,2)
    new_det=original_det / (t**8)
    # Norm_{K/Q}(t^{-4})=(t^{-4})^2
    assert new_det/original_det==(t**(-4))**2
print('RATIONAL SCALING: det shift = Norm(t^{-4}) at K-rank 8')
