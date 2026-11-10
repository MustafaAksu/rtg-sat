"""Claude: structural explanation of the toy bound 6. Block functionals on H: for block L (positions 4L+1..4L+4,
u(g_i)=a_i v_L), e_L=a_1-a_2 (=a_4-a_3 on cocycles), f_L=a_2-a_3. Predicted: every cut form beta_e lies in the
Q-span of E_L=|e_L|^2, F_L=|f_L|^2, X_LL'=c e_L(x)conj(e_L'(y)) + conj(c) e_L'(x)conj(e_L(y)), c=h(v_L,v_L').
Check: span(predicted)=9 and span(predicted + all 54 betas)=9; per cut, its exact decomposition type."""
exec(open('/home/claude/g34/h4sel/toy/toy_mixed.py').read().split("hist={}; best=[]")[0])
G=[[LS.S(x,y) for y in H] for x in H]
def beta(N): return [[__import__('functools').reduce(add,[mul(G[i][k],conj(N[k][l])) for k in range(dH)],Z) for l in range(dH)] for i in range(dH)]
Vl=[V[0],V[2],V[4]]
def coeffs(x):  # a_i with u(g_i)=a_i v_line
    vals=LS.values(x); out=[]
    for i,val in enumerate(vals):
        v=Vl[i//4]; out.append(mul(h(val,v),inv(h(v,v))))
    return out
A=[coeffs(x) for x in H]
# check closure consequence a1-a2 = a4-a3 per block
print('e_L = a4-a3 on all basis cocycles:',all(sub(a[4*L],a[4*L+1])==sub(a[4*L+3],a[4*L+2]) for a in A for L in range(3)))
e=[[sub(a[4*L],a[4*L+1]) for a in A] for L in range(3)]
f=[[sub(a[4*L+1],a[4*L+2]) for a in A] for L in range(3)]
def outer(p,q,c=ONE): return [[mul(c,mul(p[i],conj(q[j]))) for j in range(dH)] for i in range(dH)]
def madd(X,Y): return [[add(a,b) for a,b in zip(r,s)] for r,s in zip(X,Y)]
def fl(M): return [q for r in M for x in r for q in (x[0],x[1])]
pred=[outer(e[L],e[L]) for L in range(3)]+[outer(f[L],f[L]) for L in range(3)]
for L,M in [(0,1),(0,2),(1,2)]:
    c_=h(Vl[L],Vl[M]); pred.append(madd(outer(e[L],e[M],c_),outer(e[M],e[L],conj(c_))))
print('functionals e_a,e_b,e_c,f_a,f_b,f_c K-independent on H:',rank(e+f)==6)
P=[fl(M) for M in pred]; B=[fl(beta(OPS[d][0])) for d in diags]
print('rank predicted 9 forms:',qrank(P),'; rank predicted + 54 cut forms:',qrank(P+B))
# type of each nonzero cut: which predicted forms are needed
for d in diags:
    b=fl(beta(OPS[d][0]))
    if all(x==0 for x in b): continue
    need=[k for k in range(9) if qrank([P[j] for j in range(9) if j!=k]+[b])>qrank([P[j] for j in range(9) if j!=k])]
    names=['E_a','E_b','E_c','F_a','F_b','F_c','X_ab','X_ac','X_bc']
    print((d[0]+1,d[1]),'uses',[names[k] for k in need])
