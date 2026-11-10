"""Claude: per-tree test for W(A2): every laminar interval tree (all 132 triangulations of the 8-gon, mixed curves
allowed), in the fixed marking and after 15 random pure braids; claim: tree Q-rank <= 3 = d(d+1)/2."""
exec(open('a2_real_check.py').read().split("dH,rS,rows,G,LS=all_ops(g0)")[0])
def ops_by_diag(gs):
    LS=Local(gs); H=LS.comp; dH=len(H); Bm=[list(c) for c in zip(*(H+LS.B1))]
    def toH(c): return solve(Bm,c)[:dH]
    D={}; NP=len(gs)
    for u in range(NP):
        for v in range(u+2,NP):
            if u==0 and v==NP-1: continue
            C=eye(n)
            for p in range(u,v): C=mm(C,gs[p])
            d=next(k for k in range(1,50) if functools_pow(C,k)==eye(n))
            cols=[toH(LS.coords(LS.twist_cocycle(LS.values(x),u,v-1,d))) for x in H]
            N=msub([[cols[j][i] for j in range(dH)] for i in range(dH)],eye(dH))
            D[(u,v)]=[qq for r in N for x in r for qq in (x[0],x[1])]
    return D
def trees(i,k):
    if k-i<2: return [[]]
    out=[]
    for j in range(i+1,k):
        for L in trees(i,j):
            for Rr in trees(j,k): out.append(L+Rr+([(i,j)] if j-i>=2 else [])+([(j,k)] if k-j>=2 else []))
    return out
T=trees(0,7); print('trees:',len(T))
def maxrank(gs):
    D=ops_by_diag(gs); return max(qrank([D[d] for d in t]) for t in T)
print('fixed marking: max tree rank =',maxrank(g0))
random.seed(24); mx=0
for trial in range(15):
    w=[]
    for _ in range(9):
        i=random.randrange(1,8); w+=[i,i] if random.random()<.5 else [-i,-i]
    g,_,lab=act(g0,None,list(range(8)),w); assert lab==list(range(8))
    mx=max(mx,maxrank(g))
print('max tree rank over 15 random pure-braid markings:',mx,'(bound 3 < d^2 = 4)')
