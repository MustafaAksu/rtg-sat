"""Claude: independent replay of Severn's 90-move word (T8BW/braid.txt) from the original gate tuple
(tuples/g34_tuples.g, record with datum [[7,20]]) to the paired tuple (D/tuple_pairs_D3.json), with Claude's own GAP-text
parser (no GAP / no Severn code executed) and Claude's act() (convention sigma_i:(g_i,g_{i+1})->(g_i g_{i+1} g_i^-1, g_i),
left to right). Also chains on to W5 via P and the 618-letter word (Δ22)."""
import sys,json,re
from fractions import Fraction as Fr
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
exec(open('/home/claude/g34/h4sel/braidescape/replay_braid.py').read().split("def act")[1].split("gF,_,lab=")[0].join(["def act",""]))
ROOT='/home/claude/severn_zenodo/certs/certificates/g34-d3/'
txt=open(ROOT+'tuples/g34_tuples.g').read()
recs=txt.split('rec(')[1:]
rec=[r for r in recs if re.search(r'datum\s*:=\s*\[\s*\[\s*7\s*,\s*20\s*\]\s*\]',r)]
assert len(rec)==1, len(rec)
tup_txt=rec[0].split('tup')[1]
W_=(Fr(0),Fr(1)); W2=(Fr(-1),Fr(-1))
def parse_entry(s):
    s=s.replace(' ','').replace('\n','')
    if not re.fullmatch(r"[0-9E()^*/+\-]+",s): raise ValueError(s)
    terms=re.findall(r'[+\-]?[^+\-]+',s)
    tot=(Fr(0),Fr(0))
    for t in terms:
        sign=-1 if t.startswith('-') else 1; t=t.lstrip('+-')
        unit=(Fr(1),Fr(0))
        if t.endswith('E(3)^2'): unit=W2; t=t[:-6]
        elif t.endswith('E(3)'): unit=W_; t=t[:-4]
        t=t.rstrip('*')
        c=Fr(t) if t else Fr(1)
        tot=(tot[0]+sign*c*unit[0], tot[1]+sign*c*unit[1])
    return tot
# extract matrices: sequence of [ [ ... ], ... ] at depth 3
depth=0; buf=''; mats=[]; cur=[]; row=[]
for ch in tup_txt:
    if ch=='[':
        depth+=1
        if depth==3: buf=''
        continue
    if ch==']':
        if depth==3: row=[parse_entry(x) for x in buf.split(',')]; cur.append(row)
        elif depth==2: mats.append(cur); cur=[]
        elif depth==1: break
        depth-=1; continue
    if depth==3: buf+=ch
assert len(mats)==20 and all(len(m)==6 and all(len(r)==6 for r in m) for m in mats), (len(mats))
I6=eye(6)
P_=I6
for m in mats: P_=mm(P_,m)
print('original tuple: 20 matrices; reflections:',all(mm(m,m)==I6 and rank(msub(I6,m))==1 for m in mats),'; product one:',P_==I6)
word=json.loads(open(ROOT+'T8BW/braid.txt').read())
print('braid word length:',len(word),'; positive generators only:',all(x>0 for x in word))
gF,_,lab=act(mats,None,list(range(20)),word)
paired=[[[ (Fr(a),Fr(b)) for a,b in r] for r in m] for m in json.load(open(ROOT+'D/tuple_pairs_D3.json'))]
print('original --90 moves--> paired tuple, exact entry-by-entry match:',sum(1 for a,b in zip(gF,paired) if a==b),'/ 20')
print('strand permutation of the 90-move word identity?',lab==list(range(20)),' (permutation:',lab,')')
# chain to W5 via P and Δ22 word
S=json.load(open('/home/claude/g34/h4sel/severnlink/severn_to_w5.json'))
P=[[ (Fr(a),Fr(b)) for a,b in r] for r in S['P']]
Pi=[r[6:] for r in rref([P[i]+[ONE if i==j else Z for j in range(6)] for i in range(6)])[0]]
T=[mm(mm(P,m),Pi) for m in gF]
gW,_,lab2=act(T,None,list(range(20)),S['word'])
exec(open('/home/claude/g34/h4sel/w5links/build_links.py').read().split("B='/home/claude")[0].split("def link")[0])
W5=[[ (Fr(a),Fr(b)) for a,b in v] for v in json.load(open('/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/W5_BASELINE_ROOTS.json'))['generating_reflection_roots']]
gT=[]
for v in W5: s=refl(v); gT+=[s,s]
print('chain original --90--> paired --P, 618--> W5 exact:',gW==gT)
