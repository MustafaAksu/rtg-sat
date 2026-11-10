import json,sys,flint
from fractions import Fraction as F
d=json.load(open(sys.argv[1]))
K=lambda p:(F(p[0]),F(p[1]))
def mul(x,y): a,b=x;c,e=y; return (a*c-b*e,a*e+b*c-b*e)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def conj(x): return (x[0]-x[1],-x[1])
Z=(F(0),F(0))
S=[[K(x) for x in r] for r in d['S_gram']]; N=[[[K(x) for x in r] for r in c['N']] for c in d['curves']]
def mm(A,B): return [[ (lambda i,j: __import__('functools').reduce(add,[mul(A[i][k],B[k][j]) for k in range(8)],Z))(i,j) for j in range(8)] for i in range(8)]
H1=all(all(x==Z for r in mm(a,b) for x in r) for a in N for b in N)
flat=flint.fmpq_mat([[flint.fmpq(c.numerator,c.denominator) for r in X for x in r for c in x] for X in N])
print(sys.argv[1],"curves",len(N),"H1",H1,"Q-span",flat.rank())
