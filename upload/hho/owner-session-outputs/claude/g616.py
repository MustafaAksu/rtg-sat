# HHO: (D)-budget regime d=6. Imprimitive reflection group G(6,1,6) over K=Q(omega), standard unitary form.
# Budget: dim H1_par = sum c_j - 2d = 8 with d=6 and N_eff >= 19 forces (near-)reflection tuples.
# Local factors (locality): diag(-1) reflection a/b = 1/2 (odd v2); diag(zeta6^{+-1}) unit; diag(omega^{+-1}) 3-only;
# transposition-type e_i - zeta^a e_j (norm 2, b=2) -> 1. Prediction: class [2^{n(-1)}] when signature (4,4).
import sys, io, contextlib, importlib.util, itertools, random
sys.path.insert(0,'.')
from generic_engine import *
spec=importlib.util.spec_from_file_location('cdc','cyclic_disc_claude.py'); mod=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
n=6; z6=(F(1),F(1)); mu=[mod.kpow(z6,e) for e in range(6)]
def D(i,e):   # diagonal reflection: coordinate i multiplied by zeta6^e
    M=eye(n); M[i][i]=mu[e]; return M
def T(i,j,a): # transposition-type involution
    M=eye(n); M[i][i]=Z; M[j][j]=Z; M[i][j]=mu[a%6]; M[j][i]=mu[(-a)%6]; return M
def prod(gs):
    P=eye(n)
    for g in gs: P=mm(P,g)
    return P
def closure_size(gs,limit=50000):
    key=lambda M: tuple(tuple(x for x in r) for r in M)
    seen={key(eye(n))}; fr=[eye(n)]
    while fr and len(seen)<limit:
        M=fr.pop()
        for g in gs:
            X=mm(M,g); k=key(X)
            if k not in seen: seen.add(k); fr.append(X)
    return len(seen)
def run(label,gs):
    assert prod(gs)==eye(n), 'product != 1'
    cs=[rank(msub(g,eye(n))) for g in gs]
    LS=Local(gs); H=LS.comp
    G=[[LS.S(x,y) for y in H] for x in H]; h=[[mul(mod.theta,x) for x in r] for r in G]
    d=mod.det(h); assert d[1]==0
    print(f"{label}: N={len(gs)} sum c={sum(cs)} dim={len(H)} det={d[0]} sig={mod.hsig(h)} class={mod.norm_class(d[0])}",flush=True)
    return d[0]
random.seed(616)
# chain of twisted transposition pairs connecting all 6 coordinates (generates G(6,6,6)-part together with twists)
def pairs(spec): return [m for (i,j,a) in spec for m in (T(i,j,a),T(i,j,a))]
base=[(0,1,1),(1,2,0),(2,3,2),(3,4,0),(4,5,1),(0,5,3),(1,3,1),(2,4,5)]   # 8 pairs = 16 reflections
assert len(pairs(base))==16
cases={
 'P1 n(-1)=1: d(-1),d(z),d(w^2),d(w^2) + 8 pairs   predict [2]': [D(0,3),D(0,1),D(0,4),D(0,4)]+pairs(base),
 'P2 n(-1)=1: d(-1),d(w),d(w),d(z^-1) + 8 pairs    predict [2]': [D(3,3),D(3,2),D(3,2),D(3,5)]+pairs(base),
 'P3 n(-1)=3: 3 d(-1), d(z),d(w^2),d(w^2) + 7 pairs predict [2]': [D(0,3),D(1,3),D(1,3),D(0,1),D(0,4),D(0,4)]+pairs(base[:7]),
 'Q0 n(-1)=0: d(z),d(z^-1),d(z),d(z^-1) + 8 pairs  predict [1]': [D(0,1),D(0,5),D(2,1),D(2,5)]+pairs(base),
 'Q2 n(-1)=2: d(-1),d(-1),d(z),d(z^-1) + 8 pairs   predict [1]': [D(0,3),D(0,3),D(4,1),D(4,5)]+pairs(base),
}
for lab,gs in cases.items():
    print(lab,'| group order (capped 50000):',closure_size(gs))
    run(lab,gs)
