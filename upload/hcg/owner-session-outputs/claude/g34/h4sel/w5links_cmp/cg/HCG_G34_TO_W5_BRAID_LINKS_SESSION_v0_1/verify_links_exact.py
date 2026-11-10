#!/usr/bin/env python3
"""Portable exact replay using Q(w) arithmetic and elementary Artin actions.
Neither a predictor nor a parabolic-monodromy engine is used.
"""
from pathlib import Path
import json,hashlib,sys
D=Path(__file__).resolve().parent

def fieldmul(q,r):
    return (q[0]*r[0]-q[1]*r[1],q[0]*r[1]+q[1]*r[0]-q[1]*r[1])
def fieldconj(q):return (q[0]-q[1],-q[1])
def fieldsub(q,r):return(q[0]-r[0],q[1]-r[1])
UNITS=((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1))
def line(v):return min(tuple(fieldmul(e,x) for x in v) for e in UNITS)
def involution(v,x):
    dot=(0,0)
    for a,b in zip(x,v):
        c=fieldmul(a,fieldconj(b));dot=(dot[0]+c[0],dot[1]+c[1])
    assert dot[0]%3==0 and dot[1]%3==0
    u=(dot[0]//3,dot[1]//3)
    return tuple(fieldsub(a,fieldmul(u,b)) for a,b in zip(x,v))
def artin(pairs,word):
    v=list(pairs)
    for c in word:
        ix=abs(c)-1
        assert 0<=ix<19
        a,b=v[ix:ix+2]
        if c>0:
            v[ix:ix+2]=[involution(a,b),a]
        else:
            v[ix:ix+2]=[b,involution(b,a)]
    return v
def braid_perm(word):
    q=list(range(20))
    for c in word:
        ix=abs(c)-1;q[ix],q[ix+1]=q[ix+1],q[ix]
    return q

def decode(x):return tuple((int(a),int(b)) for a,b in x)
def run():
    for tag in ['NEW01','NEW02','NEW03','NEW04','BLOCK']:
        path=D/f'{tag}_TO_W5_PURE_BRAID_CERT.json';s=json.loads(path.read_text())
        initial=[decode(u) for u in s['source_roots']]
        target=[decode(u) for u in s['target_roots']]
        # Check source file identity without treating metadata as authority.
        src=json.loads((D/'source_inputs'/f'{tag}_roots.json').read_text())
        source_roots=[decode(u) for u in src['generating_reflection_roots']]
        assert source_roots==initial,('source mismatch',tag)
        baseline=json.loads((D/'source_inputs'/'W5_roots.json').read_text())
        assert [decode(u) for u in baseline['generating_reflection_roots']]==target
        tuple20=[r for x in initial for r in (x,x)]
        total=[]
        for k,op in enumerate(s['operations']):
            w=op['word'];a=op['target_pair_1based']-1;b=op['source_pair_1based']-1
            assert a!=b
            before=[line(tuple20[i*2]) for i in range(10)]
            assert all(line(tuple20[2*i])==line(tuple20[2*i+1]) for i in range(10))
            tuple20=artin(tuple20,w);total+=w
            after=[line(tuple20[i*2]) for i in range(10)]
            assert all(line(tuple20[2*i])==line(tuple20[2*i+1]) for i in range(10))
            assert all(after[i]==before[i] for i in range(10) if i!=a),(tag,k)
        final=[r for i in range(10) for r in (target[i],target[i])]
        assert [line(v) for v in tuple20]==[line(v) for v in final],tag
        assert braid_perm(s['braid_word_1_based_left_to_right'])==list(range(20)),tag
        assert braid_perm(total)==list(range(20)),tag
        assert [line(v) for v in artin([r for x in initial for r in (x,x)],s['braid_word_1_based_left_to_right'])]==[line(v) for v in final]
        assert [line(v) for v in artin(tuple20,[-q for q in reversed(s['braid_word_1_based_left_to_right'])])]==[line(v) for x in initial for v in (x,x)]
        print(f'PASS {tag} -> W5 ops={len(s["operations"])} letters={len(s["braid_word_1_based_left_to_right"])} 20/20 endpoint & inverse & pure')
    e=json.loads((D/'BLOCK_ESCAPE_TO_W5_PURE_BRAID_CERT.json').read_text())
    pre=json.loads((D/'source_inputs/HCG_G34_BLOCK_BRAID_ESCAPE_01_CERTIFICATE_v0_1.json').read_text())
    block=json.loads((D/'BLOCK_TO_W5_PURE_BRAID_CERT.json').read_text())
    start=[decode(u) for u in e['source_roots']]
    goal=[decode(u) for u in e['target_roots']]
    assert [line(decode(u)) for u in pre['final_roots']]==[line(u) for u in start]
    assert [line(decode(u)) for u in pre['original_roots']]==[line(decode(u)) for u in block['source_roots']]
    word=e['braid_word_1_based_left_to_right']
    assert braid_perm(word)==list(range(20))
    out=artin([u for r in start for u in (r,r)],word)
    assert [line(u) for u in out]==[line(u) for r in goal for u in (r,r)]
    assert [line(u) for u in artin(out,[-q for q in reversed(word)])]==[line(u) for r in start for u in (r,r)]
    print('PASS BLOCK_ESCAPE -> W5 length=',len(word),'endpoint, inverse, pure')
    print('ALL SIX LINKS: EXACT REPLAY PASS')
if __name__=='__main__':run()
