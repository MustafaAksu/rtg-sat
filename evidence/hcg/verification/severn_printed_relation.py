"""Exact Q-linear relation among the 17 printed 4x4 blocks X_1..X_17 of Severn's Appendix A (v2),
as transcribed in evidence/hcg/severn-v2/reconstruct_severn_printed.py (the 17 lines 'X[j]=...').
Each entry a+b*omega is taken as two rational coordinates, so each block is a vector in Q^32.
Usage (repository root): python3 evidence/hcg/verification/severn_printed_relation.py
Needs sympy. It checks the transcription only; it does not read Severn's PDF or deposit.
"""
from fractions import Fraction as Fr
import sympy as sp

SRC = 'evidence/hcg/severn-v2/reconstruct_severn_printed.py'


def Q(a, b=0):
    return (Fr(a), Fr(b))


X = {}
lines = [l for l in open(SRC, encoding='utf-8').read().split('\n') if l.startswith('X[') and '=[[' in l]
assert len(lines) == 17
for l in lines:
    exec(l)
assert sorted(X) == list(range(1, 18))
M = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for r in X[j] for e in r for c in e] for j in range(1, 18)])
assert M.shape == (17, 32)
ns = M.T.nullspace()
v = ns[0] * sp.ilcm(*[x.q for x in ns[0]])
print('rank over Q:', M.rank())
print('dimension of the relation space:', len(ns))
print('primitive relation (coefficients of X_1..X_17):', list(v))
assert M.rank() == 16 and len(ns) == 1
assert list(v) == [0, 0, 0, 0, 2, 0, -4, 1] + [0] * 9
assert all(x == 0 for x in (2 * M[4, :] - 4 * M[6, :] + M[7, :]))
# the relation wrongly stated in DRAFT r1 (copied from the W5 tree) fails here:
print('X_17 - X_9 - X_10 == 0 ?', all(x == 0 for x in (M[16, :] - M[8, :] - M[9, :])))
