import sys, io, contextlib, itertools, importlib.util, json, time
from fractions import Fraction as Fr
sys.path.insert(0,'.')
spec=importlib.util.spec_from_file_location('cdc','cyclic_disc_claude.py'); mod=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
def m(a,ex): return -2+sum(1 for e in ex if (a*e)%6)
def h10(ex): return -1+sum(Fr((-e)%6,6) for e in ex)
rows=[]; t=time.time()
for ex in itertools.combinations_with_replacement([1,2,3,4,5],10):
    if sum(ex)%6: continue
    if h10(ex)!=4: continue      # signature (4,4) for chi1 (dim 8 automatic: all e nonzero, r=10)
    with contextlib.redirect_stdout(io.StringIO()):
        d=mod.family(6,list(ex),'s')
    rows.append((list(ex),m(4,ex),str(d),mod.norm_class(d)))
print('cases',len(rows),'time',round(time.time()-t,1))
from collections import Counter
print('m4=0 cases:',[(r[0],r[3]) for r in rows if r[1]==0])
print('class counts by m4:'); c=Counter((r[1],r[3]) for r in rows)
for k in sorted(c): print(' ',k,c[k])
json.dump(rows,open('c6_sweep_r10.json','w'))
