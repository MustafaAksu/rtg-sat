exec(open('/home/claude/g34/h4sel/toy/toy_explain.py').read().split("# type of each nonzero cut")[0])
names=['E_a','E_b','E_c','F_a','F_b','F_c','X_ab','X_ac','X_bc']
USES={}
for d in diags:
    b=fl(beta(OPS[d][0]))
    USES[d]=set() if all(x==0 for x in b) else {k for k in range(9) if qrank([P[j] for j in range(9) if j!=k]+[b])>qrank([P[j] for j in range(9) if j!=k])}
viol_EF=0; viol_bound=0; maxlab=0; eq=0
for t in T:
    lab=set().union(*[USES[d] for d in t]); maxlab=max(maxlab,len(lab))
    if any(L in lab and L+3 in lab for L in range(3)): viol_EF+=1
    r=qrank([flat[d] for d in t])
    if r>len(lab): viol_bound+=1
    if r==len(lab): eq+=1
print('trees using both E_L and F_L for some block:',viol_EF)
print('trees with rank > #labels:',viol_bound,'; trees with rank == #labels:',eq,'of',len(T),'; max #labels:',maxlab)
