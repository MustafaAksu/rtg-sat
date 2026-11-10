"""Claude: P1 test — can pure braids rescue the toy (target 9)? State space: paired tuples (r1,r1,...,r6,r6) reached
from the toy by adjacent pure pair-conjugations  (s,s,t,t)->(tst,tst,t,t) [word s2,s1,s1,s2 at that pair] and
(s,s,t,t)->(s,s,sts,sts) [word s2^-1,s3^-1,s3^-1,s2^-1]. For each reachable line-tuple, rank over all 14 pair-containing
planar trees via the EDGEFLUX edge forms h(F_e,F_e) on L=ker(t->sum t_i v_i) (mod p, p=1 mod 3); hits re-checked exactly."""
import sys,json,itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
V0=[[(F(a),F(b)) for a,b in v] for v in json.load(open('/home/claude/g34/h4sel/rankobs/toy_cg_roots.json'))['generating_reflection_roots']]
n=3
def rvec(v,w):  # s_w(v)
    return vadd(v,vsc(mul((F(-2),F(0)),mul(h(v,w),inv(h(w,w)))),w))
# enumerate line orbit
def canon(v):
    i=next(k for k in range(n) if not isz(v[k])); c=inv(v[i]); return tuple(x for y in vsc(c,v) for x in y)
lines={}; rep=[]
def lid(v):
    k=canon(v)
    if k not in lines: lines[k]=len(rep); rep.append(v)
    return lines[k]
fr=[lid(v) for v in V0]
changed=True
while changed:
    changed=False
    for i in range(len(rep)):
        for j in range(len(rep)):
            k=canon(rvec(rep[i],rep[j]))
            if k not in lines: lid(rvec(rep[i],rep[j])); changed=True
NL=len(rep); print('root lines in orbit:',NL)
ACT=[[lines[canon(rvec(rep[i],rep[j]))] for j in range(NL)] for i in range(NL)]  # ACT[i][j]= line of s_j(v_i)
start=tuple(lid(v) for v in V0); print('start line tuple:',start)
# mod-p arithmetic: p=1 mod 3, omega root of x^2+x+1
p=1000003
while True:
    if p%3==1 and all(p%q for q in range(2,int(p**.5)+1)): break
    p+=1
w=next(x for x in range(2,p) if (x*x+x+1)%p==0)
def tomod(k): return (k[0].numerator*pow(k[0].denominator,-1,p)+k[1].numerator*pow(k[1].denominator,-1,p)*w)%p
wbar=(-1-w)%p
def cj_mod_pair(k): return (k[0].numerator*pow(k[0].denominator,-1,p)+k[1].numerator*pow(k[1].denominator,-1,p)*wbar)%p
REPM=[[tomod(x) for x in v] for v in rep]; REPC=[[cj_mod_pair(x) for x in v] for v in rep]
def nullsp(M,ncol):
    M=[r[:] for r in M]; piv=[]; r=0
    for c in range(ncol):
        q=next((i for i in range(r,len(M)) if M[i][c]),None)
        if q is None: continue
        M[r],M[q]=M[q],M[r]; iv=pow(M[r][c],-1,p); M[r]=[x*iv%p for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]: f=M[i][c]; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
    out=[]
    for fc in [c for c in range(ncol) if c not in piv]:
        v=[0]*ncol; v[fc]=1
        for i,pc in enumerate(piv): v[pc]=(-M[i][fc])%p
        out.append(v)
    return out
def rankp(rows):
    M=[r[:] for r in rows]; rk=0
    for c in range(len(M[0]) if M else 0):
        q=next((i for i in range(rk,len(M)) if M[i][c]),None)
        if q is None: continue
        M[rk],M[q]=M[q],M[rk]; iv=pow(M[rk][c],-1,p)
        for i in range(len(M)):
            if i!=rk and M[i][c]: f=M[i][c]*iv%p; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
# Hermitian form over F_p(omega) split: represent conj via the second embedding; a Hermitian matrix entry pair (B, Bconj) ->
# we use the Q-structure: entries a+b w with a,b determined from value and its conjugate: a+bw=x, a+b wbar=y -> b=(x-y)/(w-wbar)
dw=pow((w-wbar)%p,-1,p)
def form_vec(lines6,e,Lb,Lbc):
    # B(t,s)=sum_{i,j in e} t_i conj(s_j) h(v_i,v_j); value x via embedding1, y via embedding2 (conjugate)
    d=len(Lb); out=[]
    for a in range(d):
        for b_ in range(d):
            x=0; y=0
            for i in e:
                for j in e:
                    hij=sum(REPM[lines6[i]][k]*REPC[lines6[j]][k] for k in range(n))%p
                    hijc=sum(REPC[lines6[i]][k]*REPM[lines6[j]][k] for k in range(n))%p
                    x=(x+Lb[a][i]*Lbc[b_][j]*hij)%p; y=(y+Lbc[a][i]*Lb[b_][j]*hijc)%p
            bq=(x-y)*dw%p; aq=(x-bq*w)%p
            out+= [aq,bq]
    return out
# 14 trees of hexagon with pair-leaves 0..5: internal edges = pair-intervals of length 2..3 (laminar, cyclic, mod complement)
def hex_trees():
    diags=[(u,v) for u in range(6) for v in range(u+2,6) if not (u==0 and v==5)]
    def cross(d1,d2): (a,b),(c,d)=d1,d2; return a<c<b<d or c<a<d<b
    return [t for t in itertools.combinations(diags,3) if not any(cross(x,y) for x,y in itertools.combinations(t,2))]
TREES=hex_trees(); print('hexagon trees:',len(TREES))
cache={}
def best_rank(lines6):
    if lines6 in cache: return cache[lines6]
    A=[[REPM[lines6[i]][k] for i in range(6)] for k in range(n)]
    Lb=nullsp(A,6)
    Ac=[[REPC[lines6[i]][k] for i in range(6)] for k in range(n)]
    Lbc=nullsp(Ac,6)   # conjugate embedding basis (same rref procedure -> conjugate basis)
    single=[form_vec(lines6,[i],Lb,Lbc) for i in range(6)]
    br=0; bt=None
    for t in TREES:
        rows=single+[form_vec(lines6,list(range(u,v)),Lb,Lbc) for (u,v) in t]
        r=rankp(rows)
        if r>br: br,bt=r,t
    cache[lines6]=(br,bt,len(Lb)); return cache[lines6]
print('start best pair-tree rank:',best_rank(start))
# BFS
from collections import deque
prev={start:None}; dq=deque([start]); found=None
while dq:
    s=dq.popleft()
    br,bt,dL=best_rank(s)
    if br==9: found=s; break
    for i in range(5):
        a,b=s[i],s[i+1]
        for new in [(ACT[a][b],b),(a,ACT[b][a])]:
            t=s[:i]+new+s[i+2:]
            if t not in prev: prev[t]=(s,i,0 if new[1]==b else 1); dq.append(t)
print('states explored:',len(prev),' found rank 9:',found is not None)
if found:
    path=[]; s=found
    while prev[s] is not None: ps,i,kind=prev[s]; path.append((i,kind)); s=ps
    path.reverse()
    print('pair moves (pair index i, kind 0=left conj by right / 1=right conj by left):',path)
    print('final lines:',found,' tree (pair intervals):',best_rank(found)[1])
    json.dump({'start':start,'path':path,'final_lines':found,'tree':best_rank(found)[1],'rep':[[ [str(x[0]),str(x[1])] for x in v] for v in rep]},open('toy_braid_found.json','w'))
else:
    from collections import Counter
    print('max rank over reachable states:',max(best_rank(s)[0] for s in prev),' histogram:',Counter(best_rank(s)[0] for s in prev))
