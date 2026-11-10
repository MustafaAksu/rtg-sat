"""Claude: test the real-descent hypothesis for the toy bound 6 = d(d+1)/2 (d=3).
For each tree T: reduce beta_e = S(.,N_e .) to Q_T = H/I^perp (dim r), G0 = sum beta_e (definite), M_e = G0^{-1} beta_e.
If all beta_e are real-symmetric in one K-basis then every trace of a word in the M_e is rational. Test words up to
length 3. Also compute for the union of all 54 cuts (no common I, so instead use span test: Q-rank vs K-span)."""
exec(open('/home/claude/g34/h4sel/toy/toy_mixed.py').read().split("hist={}; best=[]")[0])
import random
G=[[LS.S(x,y) for y in H] for x in H]
def beta(N): return [[__import__('functools').reduce(add,[mul(G[i][k],conj(N[k][l])) for k in range(dH)],Z) for l in range(dH)] for i in range(dH)]
def minv(M):
    nn=len(M); A=[M[i][:]+[ONE if i==j else Z for j in range(nn)] for i in range(nn)]
    R,piv=rref(A); return [r[nn:] for r in R]
def tr(M): return __import__('functools').reduce(add,[M[i][i] for i in range(len(M))],Z)
def test_tree(t):
    Ns=[OPS[dg][0] for dg in t]
    colsI=[[N[i][j] for i in range(dH)] for N in Ns for j in range(dH)]
    Ib=rref(colsI)[0]; r=len(Ib)
    # complement of I^perp: I^perp = ker of x->S(x,I) ; choose Q_T coordinates via functionals y -> S(y, i) for i in Ib? use beta restricted
    # pick r vectors w_1..w_r with S-pairing to I nondegenerate: take basis vectors of H greedily
    cand=[[ONE if i==j else Z for i in range(dH)] for j in range(dH)]
    def Sv(x,y): return __import__('functools').reduce(add,[mul(mul(x[i],conj(y[j])),G[i][j]) for i in range(dH) for j in range(dH)],Z)
    W=[]
    for c in cand:
        Mtest=[[Sv(w,i_) for i_ in Ib] for w in W+[c]]
        if rank(Mtest)>len(W): W.append(c)
        if len(W)==r: break
    Bs=[]
    for N in Ns:
        b=beta(N); Bs.append([[__import__('functools').reduce(add,[mul(mul(w1[i],conj(w2[j])),b[i][j]) for i in range(dH) for j in range(dH)],Z) for w2 in W] for w1 in W])
    G0=Bs[0]
    for B in Bs[1:]: G0=[[add(a,b) for a,b in zip(x,y)] for x,y in zip(G0,B)]
    Gi=minv(G0); Ms=[mm(Gi,B) for B in Bs]
    nonreal=0; tot=0
    for L in (1,2,3):
        for word in itertools.product(range(len(Ms)),repeat=L):
            P=eye(r)
            for w in word: P=mm(P,Ms[w])
            t_=tr(P); tot+=1
            if t_[1]!=0: nonreal+=1
    return r,nonreal,tot
random.seed(1)
best=[t for t in T if qrank([flat[d] for d in t])==6][:5]
sample=best+random.sample(T,12)
for t in sample:
    rk=qrank([flat[d] for d in t]); r,nr,tot=test_tree(t)
    print(f'tree rank {rk}, dim I={r}: non-rational traces {nr}/{tot}')
