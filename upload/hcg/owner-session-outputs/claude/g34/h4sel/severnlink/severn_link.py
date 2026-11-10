"""Claude: link Severn's deposited paired tuple (Zenodo 10.5281/zenodo.23422649, certificates/g34-d3/D/tuple_pairs_D3.json,
sha256 0021185d...) to the session W5 chart. Steps: (1) sanity of Severn's matrices (order 2, rank-one, product one,
paired); (2) find a linear intertwiner P (GL6(K)) with P r P^-1 in our 126-reflection set for all Severn reflections,
via backtracking on pairwise product orders + linear solve; also try the Galois-conjugate chart; (3) pure pair-conjugation
braid from P(Severn)P^-1 to W5 with build_links machinery; verify at matrix level."""
import sys,json,itertools
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
exec(open('/home/claude/g34/h4sel/w5links/build_links.py').read().split("B='/home/claude")[0])
SEV='/home/claude/severn_zenodo/certs/certificates/g34-d3/D/tuple_pairs_D3.json'
def Kq(s): return F(s)
raw=json.load(open(SEV))
M=[[[ (Kq(a),Kq(b)) for a,b in row] for row in m] for m in raw]
I6=eye(6)
print('Severn: 20 matrices; all order 2:',all(mm(m,m)==I6 for m in M),'; all rank(1-m)=1:',all(rank(msub(I6,m))==1 for m in M))
P_=I6
for m in M: P_=mm(P_,m)
print('product one:',P_==I6,'; paired:',all(M[2*i]==M[2*i+1] for i in range(10)))
SR=[M[2*i] for i in range(10)]
# our reflection set (126) from W5 roots
B='/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/'
W5=load(B+'W5_BASELINE_ROOTS.json')
roots={key(v):v for v in W5}; fr=list(W5)
while fr:
    nw=[]
    for v in fr:
        for w in list(roots.values())[:]:
            u=sref(v,w); k=key(u)
            if k not in roots: roots[k]=u; nw.append(u)
    fr=nw
OUR=[refl(v) for v in roots.values()]
print('our reflections:',len(OUR))
def order(Mx,cap=40):
    Q=Mx
    for k in range(1,cap+1):
        if Q==I6: return k
        Q=mm(Q,Mx)
SO=[[order(mm(a,b)) for b in SR] for a in SR]
OO=[[None]*len(OUR) for _ in OUR]
def oo(i,j):
    if OO[i][j] is None: OO[i][j]=order(mm(OUR[i],OUR[j]))
    return OO[i][j]
# choose Severn basis subset: greedy independent roots (images of 1-r)
def rootof(r): return colspace(msub(I6,r))[0]
base=[]
for i in range(10):
    if rank([rootof(SR[j]) for j in base+[i]])>len(base): base.append(i)
    if len(base)==6: break
print('Severn independent subset:',base)
def solveP(assign):   # P r_i = o_i P for i in assign keys
    rows=[]
    for i,j in assign.items():
        A=SR[i]; Bm=OUR[j]
        # unknown P (36 entries, row-major). (P A)_{rc}=sum_k P_rk A_kc ; (B P)_{rc}=sum_k B_rk P_kc
        for r in range(6):
            for c in range(6):
                row=[Z]*36
                for k in range(6):
                    row[r*6+k]=add(row[r*6+k],A[k][c]); row[k*6+c]=sub(row[k*6+c],Bm[r][k])
                rows.append(row)
    ns=nullspace(rows,36)
    return ns
found=None
def bt(idx,assign):
    global found
    if found: return
    if idx==len(base):
        ns=solveP(assign)
        if len(ns)==1:
            P=[ns[0][r*6:(r+1)*6] for r in range(6)]
            if rank(P)==6: found=(dict(assign),P)
        return
    i=base[idx]
    for j in range(len(OUR)):
        if j in assign.values(): continue
        if all(oo(j,assign[k])==SO[i][k] for k in assign):
            assign[i]=j
            if len(solveP(assign))>=1: bt(idx+1,assign)
            del assign[i]
            if found: return
bt(0,{})
print('intertwiner found:',found is not None)
if found:
    assign,P=found
    Pi=[r[6:] for r in rref([P[i]+[ONE if i==j else Z for j in range(6)] for i in range(6)])[0]]
    T=[mm(mm(P,r),Pi) for r in SR]
    inset=[any(t==o for o in OUR) for t in T]
    print('all 10 conjugated Severn reflections lie in our reflection set:',all(inset))
    # roots of conjugated tuple
    TR=[colspace(msub(I6,t))[0] for t in T]
    assert all(refl(v)==t for v,t in zip(TR,T))
    moves,fail=link(TR,W5)
    if moves is None: print('pair-conjugation link FAILED at coordinate',fail)
    else:
        word=[]
        for i,j in moves: word+=conjword(i,j)
        word=freereduce(word)
        g0=[]
        for t in T: g0+=[t,t]
        gT=[]
        for v in W5: s=refl(v); gT+=[s,s]
        gF,_,lab=act(g0,None,list(range(20)),word)
        gB,_,_=act(gF,None,list(range(20)),[-x for x in reversed(word)])
        print(f'Severn(paired, conjugated by P) -> W5: pair moves {len(moves)}, letters {len(word)}; endpoint {gF==gT}; pure {lab==list(range(20))}; inverse {gB==g0}')
        json.dump({'P':[[ [str(x[0]),str(x[1])] for x in r] for r in P],'word':word,'pair_moves':moves},open('severn_to_w5.json','w'))
