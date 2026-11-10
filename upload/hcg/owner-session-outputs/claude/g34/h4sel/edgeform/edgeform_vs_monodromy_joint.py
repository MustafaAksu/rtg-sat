"""Compare edge-form prediction with actual monodromy logarithms for one tuple over many decompositions.
argv: roots_json  n_random  seed.  Decompositions: comb, balanced, + n_random random full binary bracketings of the
10 pairs (17 curves: 10 pairs + 7 non-root internal intervals, one of the two root children dropped)."""
import os, sys, json, random
os.environ['ROOTS_JSON']=sys.argv[1]
sys.path.insert(0,'/home/claude/g34'); sys.path.insert(0,'/home/claude/g34/h4sel/edgeform')
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import g34_gateB as B
import edgeform_predict as P
import flint
def qrank(rows): return flint.fmpq_mat([[flint.fmpq(x.numerator,x.denominator) for x in r] for r in rows]).rank()
roots=json.load(open(sys.argv[1]))['generating_reflection_roots']
def random_tree(rng):
    def build(lo,hi):   # pairs lo..hi-1 -> list of intervals (pair indices)
        if hi-lo==1: return [(lo,hi)]
        m=rng.randint(lo+1,hi-1); return build(lo,m)+build(m,hi)+[(lo,hi)]
    m=rng.randint(1,9); iv=build(0,m)+build(m,10)        # root children (0,m),(m,10): keep (0,m) only
    iv=[x for x in iv if x!=(m,10)] if m<9 else [x for x in iv if x!=(m,10)]
    if m==9: pass
    cur=[(2*a+1,2*b) for a,b in iv]
    cur=list(dict.fromkeys(cur))
    # if m==1 the kept child (0,1) is a pair curve already: drop the other child (1,10) [done]; need 17 curves
    return cur
def actual(curves):
    rows=[]
    for a,b in curves:
        k,C=B.return_power(a-1,b-1); assert k==1
        T=B.T_matrix(a-1,b-1,k); N=B.mlog_unipotent(T)
        rows.append([c for row in N for x in row for c in x])
    return rows
rng=random.Random(int(sys.argv[3]))
decs=[('comb',P.COMB),('balanced',P.BAL)]
seen=set()
while len(decs)<2+int(sys.argv[2]):
    c=random_tree(rng); key=tuple(sorted(c))
    if len(c)!=17 or key in seen: continue
    seen.add(key); decs.append(('rand',c))
agree=0; out=[]; joint=[]
for name,cv in decs:
    dL,pr,_=P.predict(roots,cv)
    act=actual(cv); ar=qrank(act)
    bet=P.beta_rows(roots,cv); br=qrank(bet); jr=qrank([a+b for a,b in zip(act,bet)])
    joint.append(jr==ar==br)
    # joint test: does a common linear relation structure hold? rank of [N | beta] rows
    _,_,_=P.predict(roots,cv)
    agree+= (pr==ar); out.append((name,pr,ar))
print('JOINT relations identical:',sum(joint),'/',len(joint)); print(sys.argv[1],'cases',len(decs),'agree',agree, 'mismatches',[o for o in out if o[1]!=o[2]], 'ranks',[(o[0][0],o[2]) for o in out])
