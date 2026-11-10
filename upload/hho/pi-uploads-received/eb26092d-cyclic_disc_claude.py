"""Claude: independent check of ChatGPT's cyclic-cover feasibility examples with generic_engine.py (Severn v2 Lemma 7.2
formula; rank-one local system with monodromies zeta_m^{a_i}). K = Q(w), w^2+w+1=0; zeta_6 = 1+w, zeta_3 = w.
Outputs: dim H^1_par, Gram of S, h = theta S, det_K h, signature, class in Q^x / N(K^x); plus the (L) supplier census
for G = C_m from Severn v2 Def 4.1 / Def 4.5 (abelian G: double cosets = G/(H'<g_i>))."""
import sys
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
from fractions import Fraction as Fr
from math import gcd
def Kc(a,b=0): return (Fr(a),Fr(b))
w=Kc(0,1); zeta6=Kc(1,1); theta=Kc(1,2)
def kpow(z,k):
    r=ONE
    for _ in range(k): r=mul(r,z)
    return r
def det(M):
    M=[r[:] for r in M]; n=len(M); d=ONE
    for c in range(n):
        p=next((i for i in range(c,n) if not isz(M[i][c])),None)
        if p is None: return Z
        if p!=c: M[c],M[p]=M[p],M[c]; d=neg(d)
        d=mul(d,M[c][c]); f=inv(M[c][c])
        for i in range(c+1,n):
            if not isz(M[i][c]):
                g=mul(M[i][c],f); M[i]=[sub(x,mul(g,y)) for x,y in zip(M[i],M[c])]
    return d
def hsig(M):
    M=[r[:] for r in M]; nn=len(M); pos=ng=0; idx=list(range(nn))
    assert all(M[i][j]==conj(M[j][i]) for i in range(nn) for j in range(nn)),'not Hermitian'
    while idx:
        p=next((i for i in idx if not isz(M[i][i])),None)
        if p is None:
            pr=next(((i,j) for i in idx for j in idx if i!=j and not isz(M[i][j])),None)
            if pr is None: break
            i,j=pr
            for c in [ONE,W]:
                d=add(add(M[i][i],mul(mul(c,conj(c)),M[j][j])),add(mul(conj(c),M[i][j]),mul(c,M[j][i])))
                if not isz(d): break
            for k in range(nn): M[i][k]=add(M[i][k],mul(c,M[j][k]))
            for k in range(nn): M[k][i]=add(M[k][i],mul(conj(c),M[k][j]))
            p=i
        d=M[p][p]; assert d[1]==0
        if d[0]>0: pos+=1
        else: ng+=1
        for i in idx:
            if i==p or isz(M[i][p]): continue
            f=mul(M[i][p],inv(d))
            for k in range(nn): M[i][k]=sub(M[i][k],mul(f,M[p][k]))
            for k in range(nn): M[k][i]=sub(M[k][i],mul(conj(f),M[k][p]))
        idx.remove(p)
    return (pos,ng,nn-pos-ng)
def norm_class(q):
    """class of a rational q in Q^x/N(K^x), K=Q(sqrt-3): norms = positive rationals whose primes p = 2 mod 3 have even exponent."""
    assert q!=0
    if q<0: return 'negative (not a norm)'
    num,den=q.numerator,q.denominator; odd=[]
    for n_ in (num,den):
        p=2
        while n_>1:
            e=0
            while n_%p==0: n_//=p; e+=1
            if e%2==1 and p%3==2: odd.append(p)
            p+=1
    return '[1]' if not odd else '['+'*'.join(str(p) for p in sorted(set(odd)))+']'
def family(m,exps,label):
    z=zeta6 if m==6 else (w if m==3 else None)
    gs=[[[kpow(z,a)]] for a in exps]
    assert sum(exps)%m==0
    LS=Local(gs); H=LS.comp; dH=len(H)
    G=[[LS.S(x,y) for y in H] for x in H]
    h=[[mul(theta,x) for x in r] for r in G]
    d=det(h); assert d[1]==0, d
    sig=hsig(h)
    print(f"{label}: m={m} exps={exps} dim H^1_par={dH} det_K h={d[0]} signature={sig} class={norm_class(d[0])}")
    return d[0]
# (L) census for G = C_m (abelian): suppliers (H', chi) with ord chi >= 3; q, s, alpha from local monodromies
def census(m,exps,label):
    print(f"--- (L) census for {label}")
    divisors=[k for k in range(1,m+1) if m%k==0]
    found=[]
    for hsize in divisors:                      # subgroup H' = <g^{m/hsize}> of order hsize
        step=m//hsize
        for o in [o for o in divisors if o>=3 and hsize%o==0]:   # character of H' of order o
            # chi: g^{step*j} -> zeta_o^{j * u}, take u=1 (other generators give Galois-conjugate data)
            # branch data of C/ker chi -> C/H'
            s=0; alphas=[]; ram_base=0
            for a in exps:
                # <g_i> = <g^a>; H'<g_i> has order lcm(hsize, m/gcd(a,m)) ; number of points over p_i = m / |H'<g_i>|
                og=m//gcd(a,m); hg=hsize*og//gcd(hsize,og); npts=m//hg
                # least l with g^{a l} in H' : a l = 0 mod step
                l=step//gcd(a,step)
                loc=(a*l)//step % hsize          # local monodromy g^{a l} = (g^{step})^{(a l)/step} in H'
                alpha=(loc*(hsize//o)) % o       # image under chi: exponent in Z/o
                if loc!=0: ram_base+=npts        # branch points of C -> C/H' over p_i ... (not needed)
                if alpha!=0: s+=npts; alphas+=[alpha]*npts
            # genus q of C/H': Riemann-Hurwitz for the H'-cover C/H' -> P^1 of degree m/hsize: 2q-2 = (m/hsize)(-2) + sum over p_i of (m/hsize - npts_base)
            deg=m//hsize
            br=0
            for a in exps:
                og=m//gcd(a,m); hg=hsize*og//gcd(hsize,og); npts_total=m//hg      # points of C/H' over p_i
                br+=deg-npts_total
            q=(deg*(-2)+br+2)//2
            hval=2*q-2+s
            # simple?
            from collections import Counter
            c=Counter(alphas); simple=all(c[a]==c[(-a)%o] for a in c) and all(c[a]%2==0 for a in c if (2*a)%o==0)
            ok=(hval>0 and hval%2==0 and simple)
            print(f"  H' order {hsize}, chi order {o}: q={q} s={s} h={hval} exps={dict(c)} simple={simple} admissible={ok}")
            if ok: found.append((hsize,o))
    print(f"  admissible suppliers: {found if found else 'NONE -> L = 0, (L) fails'}")
d6=family(6,[2,2,2,2,2,3,4,4,4,5],'C6 example')
census(6,[2,2,2,2,2,3,4,4,4,5],'C6 example')
d3=family(3,[1,1,1,1,1,2,2,2,2,2],'C3 control')
census(3,[1,1,1,1,1,2,2,2,2,2],'C3 control')
