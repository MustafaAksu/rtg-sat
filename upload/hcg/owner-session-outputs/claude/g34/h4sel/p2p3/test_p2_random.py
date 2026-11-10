"""Supplement: P2 identity and wrong-inverse control on RANDOM cocycles (random K-combinations of all of Z^1,
coboundaries included), since the complement basis has c_{2i}=0 on most pairs and makes that control vacuous."""
import sys,random; sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
random.seed(777)
def creflect(v,zeta):
    n=len(v); hv=h(v,v); f=mul(sub(zeta,ONE),inv(hv))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
def rr(n):
    while True:
        v=[(F(random.randint(-1,1)),F(random.randint(-1,1))) for _ in range(n)]
        if any(not isz(x) for x in v): return v
def rk(): return (F(random.randint(-3,3)),F(random.randint(-3,3)))
out=[]; fails=0
for label,zeta in [('order3',(F(0),F(1))),('order6',(F(0),F(-1)))]:
    rs=[creflect(rr(3),zeta) for _ in range(5)]; gs=[]
    for r in rs: gs+=[r,adj(r)]
    LS=Local(gs); n=3
    def rand_cocycle():
        z=[Z]*LS.N
        for b in LS.Z1: z=vadd(z,vsc(rk(),b))
        return z
    tests=0; rej=0; nz=0
    for trial in range(12):
        x=rand_cocycle(); y=rand_cocycle(); vx=LS.values(x); vy=LS.values(y)
        for a in range(5):
            for b in range(a,5):
                if (a,b)==(0,4): continue
                tw=LS.twist_cocycle(vy,2*a,2*b+1,1); Ny=LS.coords([[sub(p,q) for p,q in zip(s,t)] for s,t in zip(tw,vy)])
                lhs=LS.S(x,Ny)
                fx=[Z]*n; fy=[Z]*n; gx=[Z]*n; gy=[Z]*n
                for i in range(a,b+1):
                    fx=vadd(fx,vadd(vx[2*i],mv(rs[i],vx[2*i+1]))); fy=vadd(fy,vadd(vy[2*i],mv(rs[i],vy[2*i+1])))
                    gx=vadd(gx,vadd(vx[2*i],mv(adj(rs[i]),vx[2*i+1]))); gy=vadd(gy,vadd(vy[2*i],mv(adj(rs[i]),vy[2*i+1])))
                tests+=1
                if lhs!=neg(h(fx,fy)): fails+=1
                if not isz(lhs):
                    nz+=1
                    if lhs!=neg(h(gx,gy)): rej+=1
    s=f'[P2-random:{label}] identity tests={tests} failures so far={fails}; nonzero={nz}; wrong-inverse control rejected {rej}/{nz}'
    print(s); out.append(s)
out.append(f'TOTAL FAILURES: {fails}'); print(out[-1])
open('test_p2_random_out.txt','w').write('\n'.join(out)+'\n')
