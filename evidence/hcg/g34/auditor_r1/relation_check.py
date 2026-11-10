# Exact Q-nullspace of the 17 N_j for W5/W6/W7 certificates (checks auditor E02) and return exponents (E03)
import json, sys, sympy as sp
from fractions import Fraction as F
for f in sys.argv[1:]:
    d=json.load(open(f)); cs=d['curves']
    print(f,'k set =',sorted(set(c['k'] for c in cs)))
    A=sp.Matrix([[sp.Rational(str(F(v))) for r in c['N'] for x in r for v in x] for c in cs]).T
    ns=A.nullspace(); print('  nullity =',len(ns))
    for v in ns:
        m=min(abs(t) for t in v if t!=0); v=v/m
        print('  relation:',{str(tuple(cs[i]['curve'])):str(v[i]) for i in range(len(cs)) if v[i]!=0})
