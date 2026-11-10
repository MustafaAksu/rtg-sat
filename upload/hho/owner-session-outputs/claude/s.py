from fractions import Fraction
def factor(n):
    n=abs(int(n));a={};k=2
    while k*k<=n:
        while n%k==0:a[k]=a.get(k,0)+1;n//=k
        k=3 if k==2 else k+2
    if n>1:a[n]=a.get(n,0)+1
    return a
print(factor(39191040))
# independent Hilbert symbol (d,-3)_p via local norm test for p=3: d unit part square mod 3?
def hilb3(d):
    d=Fraction(d);e=0;n,m=d.numerator,d.denominator
    while n%3==0:n//=3;e+=1
    while m%3==0:m//=3;e-=1
    u=(n*m)%3  # unit part mod 3 (m^-1 ≡ m mod 3)
    s=1 if u==1 else -1          # (u,-3)_3 = (u/3)
    # (3,-3)_3 = (-1,-3)... (3,-3)=(3,-1)(3,3)=(3,-1)(3,-1)=1 ; so v_3 doesn't matter
    return s
for d in [1,Fraction(1,2),Fraction(3,2),2,3,5,10]:
    inert=[p for p,e in {**factor(Fraction(d).numerator),**{q:-f for q,f in factor(Fraction(d).denominator).items()}}.items() if p%3==2 and e%2]
    print(d,inert,'sign@3=',hilb3(d),'product ok:',(-1)**len(inert)*hilb3(d)==1)
