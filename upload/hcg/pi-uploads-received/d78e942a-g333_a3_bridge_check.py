#!/usr/bin/env python3
"""Exact witness: A3 is not invariant under adjacent pure pair-conjugation in G(3,3,3).

Roots are e_i - omega**(-a) e_j with 0-based i,j; omega**2+omega+1=0.
All computations are integer arithmetic in Z[omega] and monomial matrices over mu_3.
"""
from itertools import combinations, permutations, product

P0 = (0, 1, 2)
IDENTITY = (P0, (0, 0, 0))


def mmul(a, b):
    p, x = a
    q, y = b
    return (tuple(q[p[i]] for i in range(3)),
            tuple((x[i] + y[p[i]]) % 3 for i in range(3)))


def root_reflection(i, j, a):
    p = list(P0)
    p[i], p[j] = p[j], p[i]
    ph = [0, 0, 0]
    ph[i], ph[j] = a, (-a) % 3
    return (tuple(p), tuple(ph))


def eadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def emul(x, y):
    a, b = x
    c, d = y
    return (a*c - b*d, a*d + b*c - b*d)


def eneg(x):
    return (-x[0], -x[1])


def epow(n):
    return ((1, 0), (0, 1), (-1, -1))[n % 3]


def root(i, j, a):
    v = [(0, 0)] * 3
    v[i], v[j] = (1, 0), eneg(epow(-a))
    return v


def det3(A):
    answer = (0, 0)
    for p, sign in [((0, 1, 2), 1), ((0, 2, 1), -1),
                    ((1, 0, 2), -1), ((1, 2, 0), 1),
                    ((2, 0, 1), 1), ((2, 1, 0), -1)]:
        value = emul(emul(A[0][p[0]], A[1][p[1]]), A[2][p[2]])
        answer = eadd(answer, value if sign == 1 else eneg(value))
    return answer


def rank3(vectors):
    return any(det3(triple) != (0, 0) for triple in combinations(vectors, 3))


def deletion_test(labels):
    return [rank3([root(*labels[j]) for j in range(6) if j != k])
            for k in range(6)]


def generated_order(labels):
    generators = [root_reflection(*item) for item in labels]
    seen, frontier = {IDENTITY}, [IDENTITY]
    while frontier:
        g = frontier.pop()
        for s in generators:
            t = mmul(g, s)
            if t not in seen:
                seen.add(t)
                frontier.append(t)
    return len(seen)


def main():
    # Adjacent pairs 4 and 5; one pure four-strand move conjugates pair 4 by 5.
    original = [(0, 2, 0), (0, 2, 0), (0, 2, 1),
                (0, 2, 1), (0, 1, 2), (0, 2, 0)]
    successor = [(0, 2, 0), (0, 2, 0), (0, 2, 1),
                 (1, 2, 2), (0, 1, 2), (0, 2, 0)]

    s = root_reflection(*original[3])
    t = root_reflection(*original[4])
    assert mmul(mmul(t, s), t) == root_reflection(*successor[3])
    assert original[:3] == successor[:3] and original[4:] == successor[4:]

    G = {(p, x) for p in permutations(P0)
         for x in product(range(3), repeat=3) if sum(x) % 3 == 0}
    assert len(G) == 54
    refl = {root_reflection(i, j, a)
            for i, j in [(0, 1), (0, 2), (1, 2)] for a in range(3)}
    conj = {mmul(mmul(g, s), monomial_inverse(g)) for g in G}
    assert conj == refl

    before = deletion_test(original)
    after = deletion_test(successor)
    assert before == [True, True, True, True, False, True], before
    assert after == [True] * 6, after
    assert generated_order(original) == generated_order(successor) == 54

    print('FULL GROUP ORDER before/after: 54 / 54')
    print('ONE PAIR MOVE (pair 4 conjugated by pair 5): PASS')
    print('A3 deletion rank3 flags before:', before)
    print('A3 deletion rank3 flags after: ', after)
    print('NINE reflection lines form one G-conjugacy class: PASS')
    print('FIX-FIRST-ROOT upper-bound candidate tuples:', 9**5)
    print('ALL EXACT CHECKS PASS')


def monomial_inverse(a):
    p, x = a
    pi = tuple(p.index(j) for j in P0)
    return (pi, tuple((-x[pi[j]]) % 3 for j in P0))


if __name__ == '__main__':
    main()
