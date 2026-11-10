#!/usr/bin/env python3
"""Independent exact local-character and group check for HHO Addendum 11.

Uses pure rational linear algebra and cyclotomic Z[omega] arithmetic, not
HCG generic_engine / cyclic_disc / a4_direct; only reads their frozen output
for comparing the already reported examples. The mathematical use of this
independent implementation is conditional on the parabolic locality theorem.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import reduce
from math import gcd
import ast, json, hashlib
import sympy as sp

BASE=Path(__file__).parent
SOURCE=BASE/'replay'/'a4_direct_out.txt'

# Elements a+b*w, where w^2+w+1=0 and w is primitive cubic root.
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    a,b=x;c,d=y
    return a*c-b*d, a*d+b*c-b*d
def conj(x):return x[0]-x[1],-x[1]
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def inv(x):
    c,d=conj(x);n=norm(x)
    return c/n,d/n
def div(x,y):return mul(x,inv(y))
def powK(x,k):return reduce(mul,[x]*k,(Q(1),Q(0)))
ONE=(Q(1),Q(0));W=(Q(0),Q(1));ZERO=(Q(0),Q(0))

def affine_mult(x,y):
    a,b=x;c,d=y
    return a*c%5,(a*d+b)%5

def affine_inv(x):
    a,b=x;z=pow(a,-1,5)
    return z,(-z*b)%5

def gm(x,y):return (x[0]+y[0])%3,affine_mult(x[1],y[1])
def gi(x):return (-x[0])%3,affine_inv(x[1])
GID=(0,(1,0))

def closure(els):
    gens=set(els)|{gi(x) for x in els}
    seen={GID}; frontier=[GID]
    while frontier:
        g=frontier.pop()
        for h in gens:
            x=gm(g,h)
            if x not in seen:
                seen.add(x);frontier.append(x)
    return seen

H0=sp.eye(4)+sp.ones(4,4)
assert H0.det()==5

def rho(x):
    # Affine permutation representation of F20 on five letters;
    # A4 basis v_i=e_i-e_4, i=0..3.
    a,b=x
    v=[]
    for i in range(4):
        first=(a*i+b)%5; last=(4*a+b)%5
        col=[(int(j==first) if first!=4 else 0) -
             (int(j==last) if last!=4 else 0) for j in range(4)]
        v.append(col)
    M=sp.Matrix.hstack(*(sp.Matrix(c) for c in v))
    assert M.T*H0*M==H0
    return M

def frac_pair(a,b=0):return (Q(a),Q(b))

def local_factor(g):
    k,x=g
    M=rho(x)
    if k==0:
        A=sp.eye(4)-M
        basis=A.columnspace()
        if not basis:return ONE,0,0
        C=sp.Matrix.hstack(*basis)
        gram=C.T*H0*C
        a=gram.det()
        # representation of A restricted to im(A) in the chosen rational K-basis
        restricted=sp.Matrix.hstack(*(C.gauss_jordan_solve(A*b)[0] for b in basis))
        b=restricted.det()
        assert a>0 and b!=0
        return frac_pair(Q(a,b)),Q(a),Q(b)
    # For nontrivial cubic twist, F20 has no cubic eigenvalues, so full E.
    # det(I - w^k M) = 1 + c3*w^k + c2*w^(2k) + c1*w^(3k) + c0*w^(4k)
    poly=M.charpoly().all_coeffs()
    assert poly[0]==1 and len(poly)==5
    z=powK(W,k)
    denominator=ZERO
    for j, coeff in enumerate(poly):
        # 1, c3, c2, c1, c0
        denominator=plus(denominator,mul(frac_pair(coeff),powK(z,j)))
    assert denominator != ZERO
    return div(frac_pair(5),denominator),Q(5),denominator

def v_p(q,p):
    if isinstance(q,tuple):
        # Kp is unramified with uniformizer p. Kp valuation of a+b*w is
        # min(vp(a),vp(b)), including fractional coefficients/negative vp.
        vals=[v_p(x,p) for x in q if x]
        assert vals
        return min(vals)
    n,d=Q(q).as_integer_ratio();v=0
    while n%p==0 and n!=0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v

def inert_norm_class(q):
    a,b=q
    assert b==0,q
    if a<0:return 'negative (not a norm)'
    n,d=a.numerator,a.denominator
    from sympy import factorint
    odd=[]
    for p,e in factorint(n).items():
        if p%3==2 and e%2:odd.append(int(p))
    for p,e in factorint(d).items():
        if p%3==2 and e%2:
            if int(p) in odd:odd.remove(int(p))
            else:odd.append(int(p))
    return '[1]' if not odd else '['+'*'.join(str(p) for p in sorted(odd))+']'

raw=SOURCE.read_text().splitlines()
rows=[]
for line in raw:
    if not line.startswith('[('):continue
    tupletext=line.split(' dim ')[0]
    data=ast.literal_eval(tupletext)
    assert gm(reduce(gm,data,GID),GID)==GID
    assert all(g!=GID for g in data),data
    generated=closure(data)
    assert len(generated)==60
    ts=sum(k!=0 for k,_ in data)
    factors=[local_factor(g)[0] for g in data]
    prod=reduce(mul,factors,ONE)
    sig=tuple(map(int,__import__('re').search(r'sig \((\d+), (\d+), (\d+)\)',line).groups()))
    expected='[5]' if 'class [5]' in line else '[1]' if 'class [1]' in line else 'negative (not a norm)'
    computed=inert_norm_class(prod)
    assert computed==expected, (data,prod,expected,computed)
    assert v_p(prod[0],5)%2==ts%2
    rows.append(dict(tuple=data,t=ts,signature=sig,source_class=expected,computed_class=computed,
                     local_product=[str(prod[0]),str(prod[1])],group_order=len(generated)))
assert len(rows)==40
assert Counter((r['signature'],r['computed_class']) for r in rows)[((4,4,0),'[5]')]==3
assert Counter((r['signature'],r['computed_class']) for r in rows)[((4,4,0),'[1]')]==27

# Complete local-conjugacy census: all 60 group elements, k=1/2 and F20.
local_table=[]
for k in (0,1,2):
    for a in (1,2,3,4):
        for b in range(5):
            frac,gram,denom=local_factor((k,(a,b)))
            local_table.append(dict(k=k,a=a,b=b,
                                    vp5_delta=v_p(frac,5),
                                    vp2_delta=v_p(frac,2),
                                    vp11_delta=v_p(frac,11),
                                    vp5_gram=v_p(gram,5),
                                    vp5_denom=v_p(denom,5)))
assert all(z['vp5_delta']%2==int(z['k']!=0) for z in local_table)
assert all(z['vp2_delta']%2==0 and z['vp11_delta']%2==0 for z in local_table)
print('SOURCE_ROWS',len(rows),'C3xF20_GENERATION=60 EACH, PRODUCT_ONE EACH')
print('BALANCED',Counter(r['computed_class'] for r in rows if r['signature']==(4,4,0)))
print('ALL_60_LOCAL_ELEMENTS',Counter((z['k'],z['vp5_delta']) for z in local_table))
print('OTHER_INERT_P2_P11',Counter((z['k'],z['vp2_delta'],z['vp11_delta']) for z in local_table))
print('INDEPENDENT_LOCALITY_AND_GENERATION_PASS')
(BASE/'independent_locality_results.json').write_text(json.dumps({
 'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'cases':rows,'local_census':local_table,
 'status':'independent class calculation using rational group matrices and Q(omega) character arithmetic',
 'scope':'Numerical signature labels are imported from source; discriminant classes, tuple product/generation and local v5 computed independently; global class depends on parabolic locality theorem.'
},indent=2,default=str)+'\n')
