"""Dump an exact, machine-readable certificate for tuple #5 + balanced decomposition (for independent re-checking)."""
import os, json, hashlib
os.environ['ROOTS_JSON']='roots_alt_5.json'
import g34_gateB as B
ser=lambda x:[str(x[0]),str(x[1])]
curves=[(2*i-1,2*i) for i in range(1,11)]+[(1,4),(5,8),(9,12),(13,16),(1,8),(9,16),(1,16)]
Ns=[]
for a,b in curves:
    k,C=B.return_power(a-1,b-1); T=B.T_matrix(a-1,b-1,k)
    Ns.append(dict(curve=[a,b],k=k,T=[[ser(x) for x in row] for row in T],N=[[ser(x) for x in row] for row in B.mlog_unipotent(T)]))
cert=dict(field="Q(w), w^2+w+1=0; entry [p,q] means p+q*w",
  roots=json.load(open('roots_alt_5.json'))['generating_reflection_roots'],
  tuple="(s1,s1,...,s10,s10), s_i = reflection in roots[i-1]: x -> x - 2 h(x,v)/h(v,v) v, h(x,y)=sum x_k conj(y_k)",
  cocycle_convention="u(g_i)=a_i v_i; closure sum_i Q_i u(g_i)=0, Q_i=s_1...s_(i-1); coboundary u(g)=(rho(g)-1)w",
  H1par_basis_cocycles=[[ser(x) for x in z] for z in B.comp],
  coordinates="T and N act on coordinate vectors w.r.t. H1par_basis_cocycles modulo coboundaries (columns = images)",
  S_gram=[[ser(x) for x in row] for row in B.Sg], S_convention="S(u,u')=sum_k hW(u(P_{k-1}),P_{k-1}u'(g_k)) - sum_k hW(alpha_k,u'(g_k)), alpha_k=-(a_k/2)v_k; S_gram[i][j]=S(basis_i,basis_j), linear in first slot",
  twist_convention="phi(g_i)=c g_i c^-1 for a<=i<=b, c=g_a...g_b; T: u -> u o phi^k (k exact return power)",
  curves=Ns)
json.dump(cert,open('g34_cert_tuple5_balanced.json','w'),indent=0)
print(hashlib.sha256(open('g34_cert_tuple5_balanced.json','rb').read()).hexdigest())
