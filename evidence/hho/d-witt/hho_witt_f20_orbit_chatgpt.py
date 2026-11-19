"""Independent exact F20 Witt graph replay, with no matrix or source-engine imports.

Group elements (k,a,b) act on 5 affine points by x -> a*x+b (mod 5)
with a in (Z/5)^* and scalar twist omega**k (k mod 3). The coefficient
representation is omega**k tensor (permutation_5 minus trivial_1).

For H <= C3 x F20, dim V^H is calculated by two distinct identities:
(1) orbit/stabilizer with scalar-twist compatibility;
(2) exact character average (1/|H|) sum_{h in H} omega**k
    (number_of_fixed_affine_points(h)-1).
Each dimensional value must agree; no Q(omega) matrix operations used.

Default run (rtg-sat repo root): checks SHA-256 of BOTH the tuple output
and the a4_direct.py convention source without importing the latter.
--skip-code-hash-local permits using the byte-exact output copied locally
when the historical source code is accessible only by GitHub connector.
"""
from __future__ import annotations
import argparse
import ast
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import re

OUT_FILE = 'evidence/hho/outputs/a4_direct_out.txt'
CODE_FILE = 'evidence/hho/code/a4_direct.py'
EXPECTED = {
    OUT_FILE: '8d54d6622be6cef8a5568df5bee2285f780834d446c23bd3c1eae0b9b9ba6f89',
    CODE_FILE: 'cd548934c63af78e688d0697cd23da05fe602d09de3df9bb4a0d28d03616bc9d',
}
IDENTITY = (0, 1, 0)
OMEGAS = ((1,0), (0,1), (-1,-1))


def group_product(p,q):
    k,a,b=p; l,c,d=q
    return ((k+l)%3, a*c%5, (a*d+b)%5)


def group_inverse(p):
    k,a,b=p
    a_inv=next(x for x in range(1,5) if x*a%5==1)
    return ((-k)%3, a_inv, (-a_inv*b)%5)


@lru_cache(None)
def generated(generators):
    steps=tuple(generators)+tuple(group_inverse(g) for g in generators)
    seen={IDENTITY}; queue=[IDENTITY]
    for g in queue:
        for h in steps:
            u=group_product(h,g)
            if u not in seen:
                seen.add(u);queue.append(u)
    assert len(queue)<=60
    return tuple(sorted(queue))


def action(h,x):
    return (h[1]*x+h[2])%5


@lru_cache(None)
def fixed_dimension(generators):
    H=generated(tuple(generators))
    # Identity 1: twisted orbit-stabilizer count on permutation five-space.
    used=set(); permitted_orbits=0
    for x in range(5):
        if x in used:continue
        orbit={action(h,x) for h in H}
        used.update(orbit)
        if all(h[0]==0 for h in H if action(h,x)==x):
            permitted_orbits+=1
    triv_component = int(all(h[0]==0 for h in H))
    orbit_dim=permitted_orbits-triv_component

    # Identity 2: character/Burnside average; exact Z[omega] arithmetic.
    numerator_a=0; numerator_b=0
    for h in H:
        fixed_points=sum(action(h,x)==x for x in range(5))
        coef=fixed_points-1
        wa,wb=OMEGAS[h[0]]
        numerator_a+=wa*coef
        numerator_b+=wb*coef
    assert numerator_b==0 and numerator_a%len(H)==0
    character_dim=numerator_a//len(H)
    assert orbit_dim==character_dim, (generators, orbit_dim, character_dim)
    assert 0<=orbit_dim<=4
    return orbit_dim


def product(gs):
    answer=IDENTITY
    for g in gs: answer=group_product(answer,g)
    return answer


def binary_bracketings(a,b):
    """Exhaustive noncrossing brackets of leaves a..b, not Claude's DP."""
    if a==b:
        yield a
        return
    for k in range(a,b):
        for L in binary_bracketings(a,k):
            for R in binary_bracketings(k+1,b):
                yield (L,R)


def evaluate_tree(branch,gs):
    """Directly count each internal edge (except last root) and each vertex."""
    def visit(node):
        if isinstance(node,int):return gs[node],0,0,False
        left,le,lv,li=visit(node[0]);right,re,rv,ri=visit(node[1])
        edge_count=le+re+(fixed_dimension((left,)) if li else 0)+(fixed_dimension((right,)) if ri else 0)
        vertex_count=lv+rv+fixed_dimension((left,right))
        return group_product(left,right),edge_count,vertex_count,True
    P,edges,vertices,is_nonleaf=visit(branch)
    return edges-vertices, edges, vertices


def all_tree_values(gs):
    if len(gs)==5:
        trees=list(binary_bracketings(0,3))
        assert len(trees)==5
        return [evaluate_tree(t,gs) for t in trees]
    assert len(gs)==4
    # A: {1,2}|{3,4}; B: {2,3}|{1,4}.
    A=evaluate_tree(((0,1),2),gs)
    B=evaluate_tree((0,(1,2)),gs)
    # C: {1,3}|{2,4}. One braid sends (g1,g2) to
    # (g1*g2*g1^{-1},g1) using 0-based indices 1,2.
    g0,g1,g2,g3=gs
    braided=(g0,group_product(group_product(g1,g2),group_inverse(g1)),g1,g3)
    assert product(braided)==IDENTITY
    C=evaluate_tree(((0,1),2),braided)
    return [A,B,C]


def read_rows(text):
    rows=[]
    for line_num,line in enumerate(text.splitlines(),1):
        if not line.startswith('[('):continue
        prefix=line.split(' dim',1)[0]
        t=ast.literal_eval(prefix)
        assert all(isinstance(e,tuple) and len(e)==2 for e in t)
        sig=re.search(r'\bsig \(([^)]+)\) class (\[\d+\]|negative)',line)
        assert sig, (line_num,line)
        cls=sig.group(2)
        rows.append((line_num, tuple((int(k),int(f[0]),int(f[1])) for k,f in t),sig.group(1),cls))
    return rows


def main():
    arg=argparse.ArgumentParser()
    arg.add_argument('--skip-code-hash-local',action='store_true',help='only for a local runner lacking source code; never for final repo replay')
    args=arg.parse_args()
    for path,wanted in EXPECTED.items():
        if args.skip_code_hash_local and path==CODE_FILE:
            print('SOURCE CODE: NOT AVAILABLE LOCALLY; convention/hash verified separately on GitHub')
            continue
        payload=Path(path).read_bytes()
        assert sha256(payload).hexdigest()==wanted, f'{path}: SHA-256 mismatch'
        print(f'SOURCE SHA-256 PASS: {path}: {wanted}')

    data=read_rows(Path(OUT_FILE).read_text())
    assert len(data)==40
    split=Counter(); non=[]; n_ok=0
    all_sig=Counter()
    for line,gs,sig,cls in data:
        assert product(gs)==IDENTITY, line
        assert len(generated(gs))==60, line
        assert fixed_dimension(gs)==0, line
        n_ok+=1
        if sig!='4, 4, 0':continue
        values=all_tree_values(gs)
        nums=[v[0] for v in values]
        assert all(0<=w<=4 for w in nums)
        all_sig[(len(gs),cls)]+=1
        if cls=='[5]':
            assert len(gs)==4 and nums==[0,0,0]
            non.append((line,nums))
        elif cls=='[1]':
            split[(len(gs),max(nums))]+=1
        else:
            raise AssertionError(('unexpected class',line,cls))
    expected={(4,0):4,(4,1):6,(4,2):5,(4,4):1,
              (5,1):3,(5,2):3,(5,3):3,(5,4):2}
    assert dict(split)==expected, (split,expected)
    assert len(non)==3 and [x[0] for x in non]==[9,29,32]
    assert sum(split.values())==27
    assert all_sig=={(4,'[5]'):3,(4,'[1]'):16,(5,'[1]'):11}
    print('F20 all 40 source tuples: product-one PASS; generated group order=60 PASS; V^G=0 PASS')
    print('F20 subgroup invariants: independent orbit/stabilizer and character-average identities agree')
    for line,nums in non:
        print(f'F20 nonsplit [5] source line {line}: three distinct N=4 topologies w={nums}: PASS')
    print('F20 split [1], signature (4,4,0), 27 tuples: counts (N,maxw) = '+repr(dict(sorted(split.items()))))
    print('ALL PASS: exact finite-group combinatorics; original class/signature labels not recalculated; graph W0 only, NOT (D)')

if __name__=='__main__':main()
