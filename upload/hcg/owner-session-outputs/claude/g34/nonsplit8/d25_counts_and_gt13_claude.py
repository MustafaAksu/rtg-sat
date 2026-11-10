"""Claude: (a) recount the d=25 local profiles distinguishing the rank-4 spectrum (ChatGPT: 6548);
(b) GT12 Thm 1.3 screen arithmetic: Delta(g) = 25 - |Tr g| >= 8 - 4 sqrt 2 for g and all its nonidentity powers
    (ChatGPT: 3 rank-3 and 24 rank-4 types survive; 92 age profiles, 210 spectrum profiles).
Reuses the exact spectra of d25_terminal_sieve_claude.py (imported by path as data, recomputed here)."""
import cmath, math, runpy, io, contextlib
from fractions import Fraction as F
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    ns=runpy.run_path('/home/claude/g34/nonsplit8/d25_terminal_sieve_claude.py')
res=ns['res']; M=ns['M']; age=ns['age']; order=ns['order']
d=25
def tr(ms): return (d-len(ms))+sum(cmath.exp(2j*math.pi*e/M) for e in ms)
thr=17+4*math.sqrt(2)                       # Delta >= 8-4 sqrt2  <=>  |Tr| <= 17+4 sqrt2
def gt13_ok(ms):
    n=order(ms); gaps=[]
    for k in range(1,n):
        p=[(k*e)%M for e in ms]
        if all(x==0 for x in p): continue
        p=[x for x in p if x]
        gaps.append(thr-abs(tr(p)))
    return min(gaps)>=0, min(gaps)
r3=[ms for ms in res[3]]; r4=[ms for ms in res[4]]
for ms in r3:
    t=tr(ms); print('rank3',ms,'|Tr|^2 =',round(abs(t)**2,6),'GT1.3 ok/gap',gt13_ok(ms))
s3=[ms for ms in r3 if gt13_ok(ms)[0]]; s4=[ms for ms in r4 if gt13_ok(ms)[0]]
print('GT1.3 survivors: rank3',len(s3),' rank4',len(s4),' min |gap| over all tested powers',
      round(min(abs(gt13_ok(ms)[1]) for ms in r3+r4),4))
def count(r3l,r4l,by_age):
    a3=[age(ms) for ms in r3l]
    if by_age: items=[(b,1) for b in sorted({age(ms) for ms in r4l})]
    else:
        from collections import Counter
        items=list(Counter(age(ms) for ms in r4l).items())
    tot=0
    def rec(i,left,acc):
        nonlocal tot
        if i==len(a3)-1:
            s=acc+left*a3[i]
            for b,mult in items:
                if s+b==29: tot+=mult
            return
        for n in range(left+1): rec(i+1,left-n,acc+n*a3[i])
    rec(0,18,F(0)); return tot
print('profiles (age-level, spectrum-level): terminal',count(r3,r4,True),count(r3,r4,False),
      '; after GT1.3',count(s3,s4,True),count(s3,s4,False))
