"""Independent exact Witt graph replay for HCG W6/W7 source certificates.

The arithmetic uses Fraction pairs in Q(omega), omega^2+omega+1=0.
Monodromy is constructed from the JSON root vectors, not from an HCG
calculation engine or an earlier Witt checker. Tree extrema are found
by a bottom-up interval-bracketing recurrence, with separately evaluated
certificate trees and witness decompositions.

Default: run from rtg-sat repository root and verify ORIGINAL full-file
SHA-256. The optional --extracted-fixture root is solely for reproducible
local tests where GitHub source files cannot be downloaded into the runner;
its root vectors and interval curves must be checked separately against
verified GitHub source bytes. Fixture-mode output is explicitly marked.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

SOURCE = {
    'W6': ('evidence/hcg/g34/g34_cert_W6_comb.json',
           'ae9048784171da49d7d39e13154addd9d1de291478f7af73aadbe44c1f42aedc'),
    'W7': ('evidence/hcg/g34/g34_cert_W7_comb.json',
           '45097b3042f30dcb746a1c0522c2375af9215957796c85f205c5b1e3c87f10ed'),
}
N = 6
ZERO = (Fraction(0), Fraction(0))
UNIT = (Fraction(1), Fraction(0))


def z(a=0, b=0):
    return (Fraction(a), Fraction(b))


def plus(x, y):
    return x[0]+y[0], x[1]+y[1]


def minus(x, y):
    return x[0]-y[0], x[1]-y[1]


def times(x, y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]-x[1]*y[1]


def conj(x):
    return x[0]-x[1], -x[1]


def reciprocal(x):
    a, b = x
    norm = a*a-a*b+b*b
    assert norm
    return (a-b)/norm, -b/norm


def eye():
    return tuple(tuple(UNIT if i == j else ZERO for j in range(N)) for i in range(N))

I = eye()


def matmul(A, B):
    rows = []
    for row in A:
        sums = []
        for j in range(N):
            s = ZERO
            for k in range(N):
                if row[k] != ZERO and B[k][j] != ZERO:
                    s = plus(s, times(row[k], B[k][j]))
            sums.append(s)
        rows.append(tuple(sums))
    return tuple(rows)


def dimension_fixed(*operators):
    """Exact rank of the stacked matrices (operator - identity)."""
    A = []
    for M in operators:
        for i in range(N):
            A.append([minus(M[i][j], I[i][j]) for j in range(N)])
    rank = 0
    for j in range(N):
        pivot = next((i for i in range(rank, len(A)) if A[i][j] != ZERO), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        p = reciprocal(A[rank][j])
        A[rank] = [times(p, q) for q in A[rank]]
        for i in range(rank+1, len(A)):
            if A[i][j] != ZERO:
                c = A[i][j]
                A[i] = [minus(A[i][k], times(c, A[rank][k])) for k in range(N)]
        rank += 1
    return N-rank


def reflection(vector):
    v = [z(*x) for x in vector]
    norm = ZERO
    for q in v:
        norm = plus(norm, times(q, conj(q)))
    assert norm == z(6), f'root norm {norm} not six'
    return tuple(tuple(minus(I[i][j], times(z(Fraction(1,3)), times(v[i], conj(v[j]))))
                       for j in range(N)) for i in range(N))


def run_case(name, data):
    roots = data['roots']
    curves = [c['curve'] if isinstance(c, dict) else c for c in data['curves']]
    assert len(roots) == 10 and len(curves) == 17
    gens = [reflection(v) for v in roots]
    for s in gens:
        assert matmul(s, s) == I
    mon = [m for s in gens for m in (s, s)]
    P = I
    for g in mon:
        P = matmul(P, g)
    assert P == I and dimension_fixed(*gens) == 0  # product one and V^G = 0

    @lru_cache(maxsize=None)
    def interval(i, j):
        return mon[i] if i == j else matmul(interval(i, j-1), mon[j])

    @lru_cache(maxsize=None)
    def edge(i, j):
        return dimension_fixed(interval(i, j))

    @lru_cache(maxsize=None)
    def vertex(i, k, j):
        return dimension_fixed(interval(i, k), interval(k+1, j))

    # Bottom-up DP. Every binary bracketing (Catalan 18) corresponds to one
    # noncrossing trivalent tree rooted at the 20th marked leaf.
    top = len(mon)-2
    state = {}
    for i in range(top+1):
        state[i, i] = (0, 0, None, None)
    for length in range(2, top+2):
        for i in range(top-length+2):
            j = i+length-1
            lo, hi = 10**8, -10**8
            low_split = high_split = None
            for k in range(i, j):
                left, right = state[i, k], state[k+1, j]
                w_here = (edge(i,k) if i<k else 0) + (edge(k+1,j) if k+1<j else 0) - vertex(i,k,j)
                cand_lo = left[0] + right[0] + w_here
                cand_hi = left[1] + right[1] + w_here
                if cand_lo < lo: lo, low_split = cand_lo, k
                if cand_hi > hi: hi, high_split = cand_hi, k
            state[i,j] = (lo,hi,low_split,high_split)

    def direct_witness(i,j,maximum):
        if i==j: return 0,0
        k = state[i,j][3 if maximum else 2]
        a,b = direct_witness(i,k,maximum)
        c,d = direct_witness(k+1,j,maximum)
        e = a+c+(edge(i,k) if k>i else 0)+(edge(k+1,j) if k+1<j else 0)
        v = b+d+vertex(i,k,j)
        return e,v

    # Certificate: 17 base intervals, complemented when they contain root leaf 20;
    # plus one extra root-internal vertex. Count the 17 internal edges exactly once.
    nodes = [((0, a-2) if b == 20 else (a-1,b-1)) for a,b in curves] + [(0,top)]
    assert len(set(nodes)) == 18
    cert_edge, cert_vertex = 0, 0
    for i,j in nodes:
        assert i < j
        kids, start = [], i
        while start <= j:
            candidates=[b for a,b in nodes if a==start and b<=j and (a,b)!=(i,j)]
            end=max(candidates,default=start)
            kids.append((start,end))
            start=end+1
        assert len(kids)==2, (i,j,kids)
        cert_vertex += vertex(kids[0][0],kids[0][1],kids[1][1])
        if (i,j)!=(0,top): cert_edge += edge(i,j)
    cert = cert_edge-cert_vertex
    mn,mx,*_=state[0,top]
    emin,vmin=direct_witness(0,top,False)
    emax,vmax=direct_witness(0,top,True)
    assert (mn,mx)==(emin-vmin,emax-vmax)
    assert (mn,mx,cert)==(4,4,4), (name,mn,mx,cert)
    return dict(name=name, certificate=cert, certificate_edge=cert_edge,
                certificate_vertex=cert_vertex, min=mn,max=mx,
                min_witness=(emin,vmin),max_witness=(emax,vmax),
                interval_products=interval.cache_info().currsize,
                common_fixed_subspaces=vertex.cache_info().currsize)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--extracted-fixture',help='local extracted roots/curves only; NOT original full-file SHA-256')
    args=ap.parse_args()
    root=Path(args.extracted_fixture) if args.extracted_fixture else Path('.')
    if args.extracted_fixture:
        print('MODE: extracted source fixtures; full source SHA-256 independently verified on GitHub, not in this local fixture run')
    else:
        print('MODE: original repository source files; enforcing source SHA-256')
    for name,(path,expected_sha) in SOURCE.items():
        payload=(root/path).read_bytes()
        if not args.extracted_fixture:
            assert sha256(payload).hexdigest()==expected_sha, f'{name} source SHA-256 mismatch'
            print(f'{name} input SHA-256 PASS: {expected_sha}')
        datum=json.loads(payload)
        ans=run_case(name,datum)
        print(f"{name}: source roots=10, N=20, product-one=PASS, V^G=0: PASS, "
              f"certificate edges={ans['certificate_edge']}, vertices={ans['certificate_vertex']}, "
              f"w={ans['certificate']}; planar C18=477638700 min/max={ans['min']}/{ans['max']}; "
              f"direct witnesses min={ans['min_witness']}, max={ans['max_witness']}: PASS")
    print('ALL PASS: exact Q(omega) arithmetic, new bottom-up interval DP; graph W0 only, NOT (D)')

if __name__=='__main__': main()
