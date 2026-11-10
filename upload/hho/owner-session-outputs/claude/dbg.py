exec(open('f20_faithful.py').read().split('random.seed(5)')[0])
t=[(2, (4, 1)), (1, (1, 2)), (0, (3, 2)), (0, (2, 1)), (0, (4, 4))]
P=(1,0)
for k,f in t: P=comp(P,f)
print('F20 product',P,'k sum',sum(k for k,f in t)%3)
gs=[sc(c3[k],perm(f)) for k,f in t]
M=eye(5)
for g in gs: M=mm(M,g)
print('matrix product is I:',M==eye(5))
print('cpsi',[cpsi(k,f) for k,f in t],'ranks total',[rank(msub(g,eye(5))) for g in gs])
LS=Local(gs); print('total dim',len(LS.comp),'Z1',len(LS.Z1),'B1 rank',rank(LS.B1))
L1=Local([[[c3[k]]] for k,f in t]); print('rank1 dim',len(L1.comp))
# invariants of perm(f) common to all
