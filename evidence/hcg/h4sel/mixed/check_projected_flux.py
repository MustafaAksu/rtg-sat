"""ChatGPT §5 lemma, explicit form, on NEW01-MIXED-01 (Claude engine): S(x,Nhat y) = -d h(P F_J tau x, P F_J tau y),
P = orthogonal projector onto Fix(C_e), J(e) = complete pairs in e, d = ord(C_e); here Nhat=N (d=k, m=1)."""
import sys,json; sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
def Kc(p): return (F(p[0]),F(p[1]))
V=[[Kc(c) for c in v] for v in json.load(open('/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT/NEW01_roots.json'))['generating_reflection_roots']]
n=6
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
S_=[refl(v) for v in V]; gs=[]
for s in S_: gs+=[s,s]
LS=Local(gs); H=LS.comp; dH=len(H)
G=[[LS.S(x,y) for y in H] for x in H]
recs=json.load(open('claude_new01_mixed_records.json'))['records']
vals=[LS.values(x) for x in H]
def tau(v): return [vadd(v[2*i],mv(S_[i],v[2*i+1])) for i in range(10)]
ok_all=True
for r in recs:
    a,b=r['e']; a-=1; b-=1; d=r['ordC']
    N=[[(F(x[0]),F(x[1])) for x in row] for row in r['N']]
    C=eye(n)
    for k in range(a,b+1): C=mm(C,gs[k])
    P=[[Z]*n for _ in range(n)]; Cj=eye(n)
    for j in range(d): P=[[add(p,c) for p,c in zip(rp,rc)] for rp,rc in zip(P,Cj)]; Cj=mm(Cj,C)
    P=[[mul((F(1,d),F(0)),x) for x in row] for row in P]
    J=[i for i in range(10) if a<=2*i and 2*i+1<=b]
    flux=[]
    for v in vals:
        t=tau(v); f=[Z]*n
        for i in J: f=vadd(f,t[i])
        flux.append(mv(P,f))
    ok=all(__import__('functools').reduce(add,[mul(G[i][k],conj(N[k][l])) for k in range(dH)],Z)==mul((F(-d),F(0)),h(flux[i],flux[l])) for i in range(dH) for l in range(dH))
    ok_all&=ok
    print(f"[{a+1},{b+1}] d={d} complete pairs J={[i+1 for i in J]} endpoints partial={'yes' if (a%2==1 or b%2==0) else 'no'}: projected-flux formula {ok}")
print('ALL 17 curves:',ok_all)
