"""Claude: certify the toy braid escape with actual operators. Expand pair moves to a pure Artin word on 12 strands,
act on the actual toy tuple (matrix level) + transport cocycles, check purity/cup preservation, then rebuild the target
pair-containing tree (6 pair curves + 3 internal) with generic_engine and check H0-H4 (target 9)."""
import sys,json,itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
D=json.load(open('toy_braid_found.json'))
word=[]
for i,kind in D['path']:
    word+= [2*i+2,2*i+1,2*i+1,2*i+2] if kind==0 else [-(2*i+2),-(2*i+3),-(2*i+3),-(2*i+2)]
print('Artin word (left to right):',word)
V0=[[(F(a),F(b)) for a,b in v] for v in json.load(open('/home/claude/g34/h4sel/rankobs/toy_cg_roots.json'))['generating_reflection_roots']]
n=3
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
g0=[]
for v in V0: s=refl(v); g0+=[s,s]
exec(open('/home/claude/g34/h4sel/braidescape/replay_braid.py').read().split("def act")[1].split("gF,_,lab=")[0].join(["def act",""]))
gF,_,lab=act(g0,None,list(range(12)),word)
print('pure:',lab==list(range(12)),'; final tuple paired:',all(gF[2*i]==gF[2*i+1] for i in range(6)))
REP=[[ (F(a),F(b)) for a,b in v] for v in D['rep']]
print('final reflections match predicted lines:',all(gF[2*i]==refl(REP[D['final_lines'][i]]) for i in range(6)))
gB,_,_=act(gF,None,list(range(12)),[-s for s in reversed(word)]); print('inverse returns:',gB==g0)
L0=Local(g0); LF=Local(gF)
imgs=[LF.coords(act(g0,L0.values(x),list(range(12)),word)[1]) for x in L0.comp+L0.B1]
print('transported are cocycles:',all(rank(LF.Z1+[c])==rank(LF.Z1) for c in imgs))
print('cup preserved:',[[L0.S(x,y) for y in L0.comp] for x in L0.comp]==[[LF.S(a,b) for b in imgs[:6]] for a in imgs[:6]])
# target tree curves (1-based positions): pair curves + internal pair-interval curves
curves=[[2*i+1,2*i+2] for i in range(6)]+[[2*u+1,2*v] for (u,v) in D['tree']]
print('target curves:',curves)
json.dump({'final_roots':[[ [str(x[0]),str(x[1])] for x in REP[l]] for l in D['final_lines']],'word':word,'curves':curves},open('toy_final.json','w'))
