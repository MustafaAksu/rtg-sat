"""Claude: exact checks for ChatGPT's reciprocal-locality corollary and the inert-prime norm criterion.
Local factor (locality theorem, CHECKED): a(g) = det(h0 | E_g) (rational), b(g) = det((1-g)|E_g) (in K), E_g = im(1-g).
Claim: for h0-unitary g, E_{g^-1} = E_g, [a(g^-1)] = [a(g)], b(g^-1) = conj(b(g)); hence a(g)b(g) * a(g')b(g') is a norm
whenever g' = u g^-1 u^-1 with u a K-linear h0-isometry.  Over C alone the a-factor is NOT controlled (control 3).
Exact arithmetic in K = Q(omega) via generic_engine (66f2c253...)."""
import sys, random, os
sys.path.insert(0, '/home/claude/g34/h4sel/p2p3')                                         # Claude workspace
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'engine'))   # bundle copy (same hash)
from generic_engine import add, sub, neg, mul, conj, inv, isz, Z, ONE, W, eye, mm, mv, msub, colspace, solve
from fractions import Fraction as Fr

def trans(A): return [list(r) for r in zip(*A)]
def inner(x, y, H):
    s = Z
    for i, a in enumerate(x):
        if isz(a): continue
        for j, b in enumerate(y):
            if not isz(b) and not isz(H[i][j]): s = add(s, mul(mul(a, H[i][j]), conj(b)))
    return s
def det(M):
    M = [r[:] for r in M]; n = len(M); d = ONE
    for c in range(n):
        p = next((i for i in range(c, n) if not isz(M[i][c])), None)
        if p is None: return Z
        if p != c: M[c], M[p] = M[p], M[c]; d = neg(d)
        d = mul(d, M[c][c]); f = inv(M[c][c])
        for i in range(c + 1, n):
            if not isz(M[i][c]):
                g = mul(M[i][c], f); M[i] = [sub(x, mul(g, y)) for x, y in zip(M[i], M[c])]
    return d
def norm_class(q):
    if q == 0: return '[0]'
    sg = '-' if q < 0 else ''; q = abs(q); odd = set()
    for n_ in (q.numerator, q.denominator):
        p = 2
        while n_ > 1:
            e = 0
            while n_ % p == 0: n_ //= p; e += 1
            if e % 2 and p % 3 == 2: odd.add(p)
            p += 1
    return '[' + sg + ('1' if not odd else '*'.join(map(str, sorted(odd)))) + ']'
def a_b(g, H):
    n = len(g); E = colspace(msub(eye(n), g))
    if not E: return ONE, ONE
    a = det([[inner(x, y, H) for y in E] for x in E])
    ME = trans([solve(trans(E), mv(msub(eye(n), g), x)) for x in E])
    return a, det(ME)
def kref(v, H, zeta):
    n = len(v); q = inner(v, v, H); Hv = mv(H, [conj(x) for x in v]); f = mul(sub(ONE, zeta), inv(q))
    return [[sub(ONE if i == j else Z, mul(f, mul(v[i], Hv[j]))) for j in range(n)] for i in range(n)]
def ctrans(A): return [[conj(x) for x in r] for r in trans(A)]
def ginv(g, H):                       # H-unitary inverse: g^-1 = H^-1-conjugated adjoint; compute by solving
    n = len(g); return trans([solve(g, [ONE if i == j else Z for i in range(n)]) for j in range(n)])
def is_unitary(g, H): return mm(mm(trans(g), H), [[conj(x) for x in r] for r in g]) == H

random.seed(20261102)
OM2 = mul(W, W)
def rk(): return (Fr(random.randint(-2, 2)), Fr(random.randint(-2, 2)))
def rand_unitary(H, r, m):
    P = eye(r)
    for _ in range(m):
        v = [rk() for _ in range(r)]
        if all(isz(x) for x in v): continue
        P = mm(P, kref(v, H, random.choice([neg(ONE), W, OM2])))
    return P

fails = 0; t1 = t2 = 0; b_ok = a_ok = 0
for trial in range(40):
    r = random.choice([2, 3])
    H = [[(Fr(random.choice([1, 2, 3, 5, 6, 10])), Fr(0)) if i == j else Z for j in range(r)] for i in range(r)]
    g = rand_unitary(H, r, random.randint(1, 2))
    assert is_unitary(g, H)
    gi = ginv(g, H); assert mm(g, gi) == eye(r)
    a1, b1 = a_b(g, H); a2, b2 = a_b(gi, H)
    if a1 == ONE and b1 == ONE: continue                       # g = 1
    t1 += 1
    # (1) b(g^-1) = conj(b(g)) exactly; [a(g^-1)] = [a(g)]; pair product is a norm
    if b2 == conj(b1): b_ok += 1
    else: fails += 1; print('b mismatch', r)
    assert a1[1] == 0 and a2[1] == 0                            # Gram determinants are rational
    if norm_class(a1[0] * a2[0]) == '[1]': a_ok += 1
    else: fails += 1; print('a class mismatch', r, a1, a2)
    pair = mul(mul(a1, b1), mul(a2, b2))
    assert pair[1] == 0 and norm_class(pair[0]) == '[1]', pair
    # (2) K-isometric conjugate of g^-1
    u = rand_unitary(H, r, 1); ui = ginv(u, H)
    gp = mm(mm(u, gi), ui); assert is_unitary(gp, H)
    a3, b3 = a_b(gp, H)
    pair2 = mul(mul(a1, b1), mul(a3, b3))
    assert pair2[1] == 0
    if norm_class(pair2[0]) == '[1]': t2 += 1
    else: fails += 1; print('isometric-conjugate pair not a norm', r)
print(f'(1) {t1} random K-unitary g (r = 2..3, diagonal h0 with non-norm entries): b(g^-1) = conj b(g) in {b_ok}/{t1}, '
      f'[a(g)a(g^-1)] = [1] in {a_ok}/{t1}; pair products all norms')
print(f'(2) g\' = u g^-1 u^-1, u random K-isometry: pair product a norm in {t2}/{t1}')
# (3) control: C-conjugate but not K-isometric -- two order-2 reflections with root lengths 1 and 2
H = [[(Fr(1), Fr(0)), Z], [Z, (Fr(2), Fr(0))]]
s1 = kref([ONE, Z], H, neg(ONE)); s2 = kref([Z, ONE], H, neg(ONE))
A1, B1 = a_b(s1, H); A2, B2 = a_b(s2, H)
prod = mul(mul(A1, B1), mul(A2, B2))
print(f'(3) control: s1, s2 order-2 reflections (C-conjugate, both self-inverse), root norms 1 and 2: '
      f'a*b = {A1[0]*B1[0]}, {A2[0]*B2[0]}; product class {norm_class(prod[0])} (not [1])')
assert norm_class(prod[0]) == '[2]'
# (4) inert-prime criterion: positive integer D is a norm from K = Q(omega) iff v_p(D) even for all p = 2 mod 3
N = 3000
reps = set()
x = 0
while x*x <= 4*N:
    for y in range(-2*int(N**0.5) - 2, 2*int(N**0.5) + 3):
        v = x*x - x*y + y*y
        if 0 < v <= N: reps.add(v)
    x += 1
bad = [D for D in range(1, N + 1) if (D in reps) != (norm_class(Fr(D)) == '[1]')]
print(f'(4) D = 1..{N}: integral representability x^2 - xy + y^2 = D agrees with the inert-prime parity criterion: {not bad}')
assert not bad and fails == 0
print('ALL PASS')
