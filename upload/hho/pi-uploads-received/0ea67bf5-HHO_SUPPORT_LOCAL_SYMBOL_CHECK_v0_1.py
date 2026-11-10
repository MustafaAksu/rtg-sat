"""HHO session control: norms in Q(sqrt(-3)); p-adic inert-support parity.
For D>0, an inert prime p=2 (mod 3) gives Hilbert sign (-1)^v_p(D).
The sign at the ramified prime 3 is then determined by reciprocity.
This tests arithmetic classes, NOT geometric Jacobian/projector realizations.
"""
from fractions import Fraction
from math import isqrt

def factor(n):
    n=abs(int(n))
    ans={}
    k=2
    while k*k<=n:
        while n%k==0:
            ans[k]=ans.get(k,0)+1
            n//=k
        k=3 if k==2 else k+2
    if n>1: ans[n]=ans.get(n,0)+1
    return ans

def certificate(v):
    d=Fraction(v)
    assert d>0
    exps=factor(d.numerator)
    for p,e in factor(d.denominator).items():exps[p]=exps.get(p,0)-e
    inert=sorted(p for p,e in exps.items() if p%3==2 and e%2)
    minus=inert+([3] if len(inert)%2 else [])
    return {'D':str(d),'inert_odd_valuations':inert,'negative_local_Hilbert_places':minus,'is_norm':not inert}

if __name__=='__main__':
    inputs=[1,Fraction(1,2),Fraction(3,2),2,3,5,10]
    rows=[certificate(x) for x in inputs]
    assert rows[0]['is_norm'] and rows[1]['negative_local_Hilbert_places']==[2,3]
    assert rows[-1]['negative_local_Hilbert_places']==[2,5]
    for x in rows:print(x)
    print('EXACT PARITY/NORM TEST PASS')
