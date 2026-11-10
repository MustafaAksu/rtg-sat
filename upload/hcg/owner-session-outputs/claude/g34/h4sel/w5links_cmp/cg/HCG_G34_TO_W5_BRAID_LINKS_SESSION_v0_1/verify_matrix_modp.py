#!/usr/bin/env python3
"""Second implementation: Hurwitz braid on 6x6 reflection matrices over F_p[w].
Independent of the exact root conjugation formula in the certificate generator.
For corroboration only; exact replay is the primary proof.
"""
from pathlib import Path
import json,numpy as np
ROOT=Path(__file__).resolve().parent
P=10007
Q=pow(3,-1,P)

def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%P)
def conj(x):return ((x[0]-x[1])%P,(-x[1])%P)
def smat(v):
    R=np.zeros((6,6,2),dtype=np.int64)
    for i in range(6):
        for j in range(6):
            t=mul(v[i],conj(v[j]))
            R[i,j,0]=((1 if i==j else 0)-Q*t[0])%P
            R[i,j,1]=(-Q*t[1])%P
    return R

def mm(A,B):
    a=A[:,:,0];b=A[:,:,1];c=B[:,:,0];d=B[:,:,1]
    z=np.empty((6,6,2),dtype=np.int64)
    z[:,:,0]=(a@c-b@d)%P
    z[:,:,1]=(a@d+b@c-b@d)%P
    return z

def artin_mats(R,word):
    a=list(R)
    for c in word:
        k=abs(c)-1;x,y=a[k],a[k+1]
        a[k:k+2]=[mm(mm(x,y),x),x] if c>0 else [y,mm(mm(y,x),y)]
    return a

def roots(j):return [tuple((int(a),int(b)) for a,b in r) for r in j]

def matrix_run(tag):
    s=json.loads((ROOT/f'{tag}_TO_W5_PURE_BRAID_CERT.json').read_text())
    rr=roots(s['source_roots']);tt=roots(s['target_roots'])
    source=[smat(x) for r in rr for x in (r,r)]
    dest=[smat(x) for r in tt for x in (r,r)]
    got=artin_mats(source,s['braid_word_1_based_left_to_right'])
    assert all(np.array_equal(x,y) for x,y in zip(got,dest)),tag
    print('matrix_modp PASS',tag,'letters',s['braid_word_length'],flush=True)

if __name__=='__main__':
    for tag in ['NEW01','NEW02','NEW03','NEW04','BLOCK']:matrix_run(tag)
    b=json.loads((ROOT/'BLOCK_ESCAPE_TO_W5_PURE_BRAID_CERT.json').read_text())
    source=[smat(r) for root in roots(b['source_roots']) for r in (root,root)]
    dest=[smat(r) for root in roots(b['target_roots']) for r in (root,root)]
    got=artin_mats(source,b['braid_word_1_based_left_to_right'])
    assert all(np.array_equal(x,y) for x,y in zip(got,dest))
    print('matrix_modp PASS BLOCK_ESCAPE -> W5 letters',b['braid_word_length'])
    print('ALL SIX MODULAR MATRIX TESTS PASS')
