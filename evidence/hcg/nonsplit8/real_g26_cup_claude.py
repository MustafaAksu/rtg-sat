"""Claude: direct parabolic cup-form discriminant for the exported real-data tuples in the order-1296 G26-type group.
Uses check() from disc_locality_proof_check_claude.py (Claude's exact engine, generic_engine 66f2c253...): it builds the
cochain complex, the cup form S on H^1_par, computes det(theta S) directly and asserts agreement with the locality
prediction [(-1)^n prod a_i b_i].  Every local monodromy in these tuples is conjugate to its inverse in the group, so
(L) holds by PO-4 (Severn [387] Thm 3.1, CHECKED as recorded in HCG v0.2 section 6.11).
Usage: python3 -I real_g26_cup_claude.py gap/real_g26_examples.json
"""
import sys, json, os, io, contextlib
from fractions import Fraction as Fr
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, 'engine'))             # bundle copy of generic_engine.py (66f2c253...)
src = open(os.path.join(here, 'disc_locality_proof_check_claude.py')).read()
ns = {'__name__': 'disc_locality_lib'}
exec(src.split('\nroots=')[0], ns)               # definitions only (engine import, check(), helpers)
check = ns['check']; eye = ns['eye']
data = json.load(open(sys.argv[1]))
def dec(m): return [[(Fr(x[0]), Fr(x[1])) for x in row] for row in m]
H = eye(3)
summary = []
for k, e in enumerate(data):
    gs = [dec(m) for m in e['mats']]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cl = check(gs, H, f'ex{k}')
    line = buf.getvalue().strip()
    summary.append((k, e['N'], sum(e['c']), e['n'], e['cls'], cl))
    print(f"ex{k}: N={e['N']} sum c={sum(e['c'])} dim H1_par={2*e['n']} n={e['n']}  GAP local-product class {e['cls']}  "
          f"direct det(theta S) class {cl}")
n4 = [s for s in summary if s[3] == 4 and s[5] != '[1]']
print('direct cup-form computation agrees with locality on all', len(summary), 'examples (check() asserts it)')
print('nonsplit examples with n = 4 (dim H1_par = 8):', [(s[0], s[5]) for s in n4])
