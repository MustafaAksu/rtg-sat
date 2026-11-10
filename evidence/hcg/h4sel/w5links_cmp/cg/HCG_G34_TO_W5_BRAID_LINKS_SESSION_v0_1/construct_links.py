#!/usr/bin/env python3
"""Research-session exact paired-braid path builder; requires hcg_connect_probe.py.
The source-root normalization is the declared Q(omega) embedding, h(v,v)=6.
All braid words are independently replayed as elementary Hurwitz moves.
"""
import json, hashlib, pathlib
from construct_helper import allroots, canon, refl, path_to
OUT=pathlib.Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True)

def permuted_pair_swap(p):
    return [2*p+2,2*p+1,2*p+3,2*p+2]

def conjugate_word(i,j):
    prefix=[]
    if j>i:
        for p in range(j-1,i,-1):prefix+=permuted_pair_swap(p)
        c=[2*i+2,2*i+1,2*i+1,2*i+2]
    else:
        for p in range(j,i-1):prefix+=permuted_pair_swap(p)
        p=i-1
        c=[-(2*p+2),-(2*p+3),-(2*p+3),-(2*p+2)]
    return prefix+c+[-x for x in reversed(prefix)]

def braid_on_20(vectors,word):
    v=list(vectors)
    for q in word:
        i=abs(q)-1
        assert 0<=i<19
        a,b=v[i:i+2]
        v[i:i+2]=[refl(a,b),a] if q>0 else [b,refl(b,a)]
    return v

def permutation(word):
    p=list(range(20))
    for q in word:
        i=abs(q)-1;p[i],p[i+1]=p[i+1],p[i]
    return p

def encode(rs):return [[[int(a),int(b)] for a,b in v] for v in rs]

def run(tag):
    target=list(allroots['W5']);roots=list(allroots[tag]);original=roots[:]
    assert len(roots)==10 and len(target)==10
    operations=[];whole=[]
    for i in range(10):
        js=path_to(roots,target,i)
        assert js is not None,(tag,i)
        for j in js:
            before=roots[i];roots[i]=refl(roots[j],roots[i]);w=conjugate_word(i,j)
            # Check the elementary word acts as advertised in current state
            # Fully independent running endpoint check occurs after completing each operation below.
            operations.append({'target_pair_1based':i+1,'source_pair_1based':j+1,'word':w})
            whole.extend(w)
    assert all(canon(x)==canon(y) for x,y in zip(roots,target))
    old20=[u for r in original for u in (r,r)]
    cur=old20[:]
    for k,op in enumerate(operations):
        c=braid_on_20(cur,op['word'])
        i=op['target_pair_1based']-1;j=op['source_pair_1based']-1
        assert all(canon(c[2*a])==canon(c[2*a+1]) for a in range(10)),(tag,k,'pair')
        assert all(canon(c[2*a])==canon(cur[2*a]) for a in range(10) if a!=i),(tag,k,'other moved')
        assert canon(c[2*i])==canon(refl(cur[2*j],cur[2*i])),(tag,k,'bad conjugation')
        cur=c
    assert all(canon(cur[2*i])==canon(target[i]) for i in range(10))
    assert permutation(whole)==list(range(20)),(tag,'non-pure')
    assert [canon(v) for v in braid_on_20(cur,[-q for q in reversed(whole)])]==[canon(v) for v in old20]
    # reduced word by adjacent cancellation, replay independently
    red=[]
    for q in whole:
        if red and red[-1]==-q:red.pop()
        else:red.append(q)
    assert [canon(v) for v in braid_on_20(old20,red)]==[canon(v) for v in cur]
    assert permutation(red)==list(range(20))
    result={
       'tag':tag,'target':'W5','scope':'fixed G34 six-dimensional Q(omega) root chart; equality of root reflections up to Eisenstein units',
       'source_roots':encode(original),'target_roots':encode(target),
       'operations':operations,'operation_count':len(operations),
       'braid_word_1_based_left_to_right':red,'unreduced_word_length':len(whole),'braid_word_length':len(red),
       'pure_braid':True,'endpoint_exact_projective':True,'inverse_exact_projective':True,
       'each_local_word_exact':True,'field':'Q(omega), omega^2+omega+1=0',
    }
    raw=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    dest=OUT/f'{tag}_TO_W5_PURE_BRAID_CERT.json'
    dest.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(tag,'local_ops',len(operations),'unreduced',len(whole),'reduced',len(red),'sha256',hashlib.sha256(dest.read_bytes()).hexdigest()[:14],flush=True)
    return result

if __name__=='__main__':
    results=[run(n) for n in ['NEW01','NEW02','NEW03','NEW04','BLOCK']]
    sums={'source':str(pathlib.Path(__file__).name),'comparisons':len(results),'all_pass':True,
          'items':[{'tag':x['tag'],'local_ops':x['operation_count'],'word_len':x['braid_word_length']} for x in results]}
    (OUT/'SUMMARY.json').write_text(json.dumps(sums,indent=2)+'\n')
