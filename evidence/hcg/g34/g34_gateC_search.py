#!/usr/bin/env python3
"""G34-C search (Claude): precompute T_j, N_j for every interval curve [a,b] (2<=len<=18) on OUR paired tuple,
then test (H0)-(H4) on random interval pants decompositions (random full binary trees on 20 ordered leaves).
Uses only g34_gateB.py (our engine). A failure for any decomposition is non-decisive (Severn Remark 4.3)."""
import pickle, random, json, hashlib, sys, os
import g34_gateB as B
import flint

r=20
cache='g34_intervals.pkl'
if os.path.exists(cache):
    data=pickle.load(open(cache,'rb'))
else:
    data={}
    for L in range(2,19):
        for a in range(1,r-L+2):
            b=a+L-1
            k,C=B.return_power(a-1,b-1,kmax=400)
            if k is None: data[(a,b)]=None; continue
            T=B.T_matrix(a-1,b-1,k)
            P=B.eye(8); m=None
            for mm in range(1,241):
                P=B.matmul(P,T)
                if B.nilpotent(B.matsub(P,B.eye(8))): m=mm; break
            N=B.mlog_unipotent(P) if m else None
            data[(a,b)]=dict(k=k,m=m,N=N,cs=B.c_sigma(C),C=C)
        print("intervals of length",L,"done",flush=True)
    pickle.dump(data,open(cache,'wb'))

def Sv(x,y):
    s=B.Z0
    for i in range(8):
        for j in range(8): s=B.add(s,B.mul(B.mul(x[i],B.Sg[i][j]),B.conj(y[j])))
    return s
def gens_fixed_dim(mats):
    rows=[]
    for M in mats: rows+=B.matsub(M,B.eye(6))
    return 6-B.rank(rows)
def prod_interval(a,b):
    C=B.eye(6)
    for j in range(a-1,b): C=B.matmul(C,B.G[j])
    return C

def random_tree(lo,hi,rng):
    """full binary tree on leaves lo..hi; returns list of internal nodes as (lo,hi,(l1,h1),(l2,h2))"""
    if lo==hi: return []
    m=rng.randint(lo,hi-1)
    return [(lo,hi,(lo,m),(m+1,hi))]+random_tree(lo,m,rng)+random_tree(m+1,hi,rng)

def evaluate(nodes):
    curves=set()
    for lo,hi,_,_ in nodes:
        if (lo,hi)==(1,r): continue
        L=hi-lo+1
        if L<2 or L>18: continue
        c=(lo,hi)
        comp=None
        if lo==1: comp=(hi+1,r)
        if hi==r: comp=(1,lo-1)
        if comp and comp in curves: continue
        curves.add(c)
    curves=sorted(curves)
    if len(curves)!=17: return None
    # H0 over pants = internal nodes except the root
    H0=True
    for lo,hi,c1,c2 in nodes:
        if (lo,hi)==(1,r): continue
        mats=[prod_interval(*c1),prod_interval(*c2),prod_interval(lo,hi)]
        val=sum(B.c_sigma(M) for M in mats)-12+2*gens_fixed_dim(mats)
        if val!=0: H0=False; break
    if any(data[c] is None or data[c]['N'] is None for c in curves): return dict(curves=curves,H0=H0,ok=False,why="no return/unipotent")
    Ns=[data[c]['N'] for c in curves]
    H1=all(B.iszeromat(B.matmul(X,Y)) for X in Ns for Y in Ns)
    if not H1: return dict(curves=curves,H0=H0,H1=False,ok=False)
    imgs=[]
    for N in Ns:
        imgs+=[[N[i][j] for i in range(8)] for j in range(8)]
    Ir,_=B.rref(imgs); Ib=[v for v in Ir if any(not B.iszero(x) for x in v)]
    iso=all(B.iszero(Sv(x,y)) for x in Ib for y in Ib)
    kill=all(all(B.iszero(t) for t in B.matvec(N,x)) for N in Ns for x in Ib)
    H2=len(Ib)==4 and iso and kill
    flat=flint.fmpq_mat([[flint.fmpq(c.numerator,c.denominator) for row in N for x in row for c in x] for N in Ns])
    qd=flat.rank(); H4=(qd==16)
    res=dict(curves=curves,H0=H0,H1=H1,H2=H2,dimI=len(Ib),qspan=qd,H4=H4)
    if H2:
        compl=[]; cur=list(Ib)
        for e in B.eye(8):
            if B.rank(cur+[e])>B.rank(cur): cur.append(e); compl.append(e)
        sigs=[]; Bsum=[[B.Z0]*4 for _ in range(4)]
        for N in Ns:
            Bj=[[Sv(x,B.matvec(N,y)) for y in compl] for x in compl]
            sigs.append(B.herm_signature(Bj)[0]); Bsum=B.matadd(Bsum,Bj)
        ss=B.herm_signature(Bsum)[0]
        semi=all(s[0]==0 for s in sigs) or all(s[1]==0 for s in sigs)
        H3=semi and ss[2]==0 and (ss[0]==0 or ss[1]==0)
        res.update(H3=H3,sigs=[list(s) for s in sigs],sumsig=list(ss))
    else: res['H3']=False
    res['ok']=all(res.get(h) for h in ('H0','H1','H2','H3','H4'))
    return res

if __name__=='__main__':
    ntrials=int(sys.argv[1]) if len(sys.argv)>1 else 300
    rng=random.Random(2026)
    summary={'trials':0,'pass':[],'best_qspan':0}
    seen=set()
    for t in range(ntrials):
        nodes=random_tree(1,r,rng)
        res=evaluate(nodes)
        if res is None: continue
        key=tuple(res['curves'])
        if key in seen: continue
        seen.add(key); summary['trials']+=1
        summary['best_qspan']=max(summary['best_qspan'],res.get('qspan',0))
        if res['ok']:
            summary['pass'].append(res); print("PASS",res['curves'],flush=True)
            if len(summary['pass'])>=3: break
    print("distinct decompositions tested:",summary['trials']," passing:",len(summary['pass'])," best Q-span:",summary['best_qspan'])
    # interval statistics
    stats={str(c):dict(k=v['k'],m=v['m'],rkN=(B.rank(v['N']) if v and v['N'] else None),cs=v['cs']) for c,v in data.items() if v}
    json.dump(dict(script_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),
                   engine_sha256=hashlib.sha256(open('g34_gateB.py','rb').read()).hexdigest(),
                   summary=summary,interval_stats=stats),open('g34_gateC_search.json','w'),indent=1,default=str)
