"""Claude: independent checks for ChatGPT's HCG_REFLECTIONFREE_NEXT_SCREEN_PROPOSED_v0_1.md (no engine import).
(1) Ten-type sieve: all pairs (lam, mu) of roots of unity != 1 such that (x-lam)(x-mu) has coefficients in K=Q(w)
    and no power of diag(lam,mu) is a rank-one (reflection) matrix. Exact Galois criterion in Q(zeta_N), N=120
    (every root of unity of degree <= 2 over K has order dividing 120 since phi(m) <= 4).
    z in Q(zeta_N) lies in K iff fixed by every sigma_k: zeta -> zeta^k with gcd(k,N)=1 and k = 1 mod 3.
    Sums of two roots of unity: zeta^a + zeta^b = zeta^c + zeta^e  iff {a,b}={c,e} (mod N) or both sums vanish.
(2) Triple lemma (general scalars, not only mu_6): roots of unity l1 l2 l3 = 1, none equal to 1  =>  sum 1/ord <= 1.
    Checked exhaustively for orders dividing 360 (proof in the report).
(3) Type-A scalar budget: for every d in 6..400, t>=3 nonidentity scalars cost > 2d-11 (with the triple lemma),
    t>=4 cost > 2d-11; hence t = 2 and rank Per <= 3n = 12 (n = 4)."""
from math import gcd
from fractions import Fraction as F
N=120
ks=[k for k in range(1,N) if gcd(k,N)==1 and k%3==1]
def order(a): return N//gcd(a,N)
def sum_fixed(a,b,k):
    A=sorted([a%N,b%N]); B=sorted([(k*a)%N,(k*b)%N])
    if A==B: return True
    return ((a-b)%N==N//2) and ((k*a-k*b)%N==N//2)       # both sums are zero
def prod_fixed(a,b,k): return (k*(a+b))%N==(a+b)%N
types={}
for a in range(1,N):
    for b in range(a,N):
        if not all(sum_fixed(a,b,k) and prod_fixed(a,b,k) for k in ks): continue
        oa,ob=order(a),order(b)
        # reflection-free: no power m with exactly one of lam^m, mu^m equal to 1
        refl_power=any(((m*a)%N==0)!=((m*b)%N==0) for m in range(1,N+1))
        if refl_power: continue
        assert oa==ob
        types.setdefault(oa,[]).append((a,b))
total=sum(len(v) for v in types.values())
print('allowed orders and pairs (exponents of zeta_120):')
for o in sorted(types): print(f'  order {o}: {len(types[o])} pair(s) {types[o]}')
print('total types:',total)
assert sorted(types)==[2,3,4,6,12] and total==10
# (2) triple lemma
M=360; bad=0; cnt=0
for a in range(1,M):
    for b in range(a,M):
        c=(-a-b)%M
        if c==0 or c<b: continue
        cnt+=1
        s=F(gcd(a,M),M)+F(gcd(b,M),M)+F(gcd(c,M),M)     # 1/ord = gcd/M
        if s>1: bad+=1; print('VIOLATION',a,b,c,s)
print(f'triple lemma: {cnt} unordered product-one triples of nonidentity roots of unity of order | {M}: violations {bad}')
assert bad==0
# (3) budget
for d in range(6,401):
    A=d-(d+1)//3-1; B=d-(d+1)//2-1
    assert 2*A+2*B>2*d-11                      # t >= 4
    worst3=3*d-3-(d+1)                         # t = 3 with sum 1/q <= 1
    assert worst3>2*d-11
print('budget: t>=3 impossible for all d in 6..400 (analytic: 2A+2B >= (7d-17)/3, triple >= 2d-4)')
print('ALL PASS')
