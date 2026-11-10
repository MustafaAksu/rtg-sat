import json,collections,sys,pathlib
B=pathlib.Path(__file__).resolve().parent
allroots={}
for tag in ['W5','NEW01','NEW02','NEW03','NEW04','BLOCK']:
    j=json.loads((B/'source_inputs'/f'{tag}_roots.json').read_text())
    allroots[tag]=[tuple(map(tuple,v)) for v in j['generating_reflection_roots']]

def mul(x,y):
 a,b=x;c,d=y;return (a*c-b*d,a*d+b*c-b*d)
def conj(x):a,b=x;return(a-b,-b)
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def refl(s,x):
 a=b=0
 for v,u in zip(s,x):
  r,t=mul(u,conj(v));a+=r;b+=t
 assert a%3==0 and b%3==0,(a,b)
 f=(a//3,b//3)
 return tuple(sub(y,mul(f,v)) for v,y in zip(s,x))
U=((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1))
def canon(v):return min(tuple(mul(u,x) for x in v) for u in U)

def path_to(roots,target,i):
 start=canon(roots[i]);goal=canon(target[i]);
 if start==goal:return []
 qs=collections.deque([start]);pa={start:None}
 while qs:
  v=qs.popleft()
  for j,s in enumerate(roots):
   if j==i:continue
   w=canon(refl(s,v))
   if w in pa:continue
   pa[w]=(v,j)
   if w==goal:
    path=[]
    while pa[w] is not None:
     w,jj=pa[w];path.append(jj)
    return path[::-1]
   qs.append(w)
 return None

def run(name,target):
 roots=list(allroots[name]);tar=list(allroots[target]); assert len(roots)==len(tar)==10
 lens=[]
 for i in range(10):
  path=path_to(roots,tar,i)
  if path is None:return False,i,lens,roots
  for j in path:roots[i]=refl(roots[j],roots[i])
  assert canon(roots[i])==canon(tar[i]),i
  lens.append(len(path))
 return True,len(lens),lens,roots
if __name__=='__main__':
 for nm in ['NEW01','NEW02','NEW03','NEW04','BLOCK']:
  print(nm,run(nm,'W5')[:3],flush=True)
