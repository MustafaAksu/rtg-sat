"""Claude: independent replay of the 868-letter pure braid G34-BLOCK-01 -> BRAID-ESCAPE-01 with generic_engine.
Artin convention: sigma_i:(g_i,g_{i+1})->(g_i g_{i+1} g_i^-1, g_i); sigma_i^-1:(g_i,g_{i+1})->(g_{i+1}, g_{i+1}^-1 g_i g_{i+1}).
Cocycle transport: u'(new g_i)=u(word), consistent with u(xy)=u(x)+rho(x)u(y). Checks: pure permutation; final matrix
tuple equals the paired reflections of final_roots; cup form preserved S_init(x,y)=S_fin(Tx,Ty); inverse word returns."""
import sys,json
sys.path.insert(0,'/home/claude/g34/h4sel/p2p3')
from generic_engine import *
C=json.load(open('cert.json')); W=C['braid_word_left_to_right']
def K(v): return [(F(a),F(b)) for a,b in v]
n=6
def refl(v):
    f=mul((F(-2),F(0)),inv(h(v,v)))
    return [[add(ONE if i==j else Z, mul(f,mul(v[i],conj(v[j])))) for j in range(n)] for i in range(n)]
def tuple_from(roots):
    t=[]
    for v in roots: s=refl(K(v)); t+=[s,s]
    return t
g0=tuple_from(C['original_roots']); gT=tuple_from(C['final_roots'])
print('original roots file hash pinned in cert:',C['source_roots_sha256'][:16])
def act(g,vals,lab,word):
    g=list(g); vals=[list(v) for v in vals] if vals is not None else None; lab=list(lab)
    for s in word:
        i=abs(s)-1; x,y=g[i],g[i+1]
        if s>0:
            g[i],g[i+1]=mm(mm(x,y),adj(x)),x
            if vals is not None:
                cx,cy=vals[i],vals[i+1]
                # u(x y x^-1) = cx + x cy - (x y x^-1) cx
                vals[i],vals[i+1]=vadd(vadd(cx,mv(x,cy)),vsc(neg(ONE),mv(g[i],cx))),cx
            lab[i],lab[i+1]=lab[i+1],lab[i]
        else:
            g[i],g[i+1]=y,mm(mm(adj(y),x),y)
            if vals is not None:
                cx,cy=vals[i],vals[i+1]
                # u(y^-1 x y) = -y^-1 cy + y^-1 cx + y^-1 x cy
                yi=adj(y)
                vals[i],vals[i+1]=cy,vadd(vadd(vsc(neg(ONE),mv(yi,cy)),mv(yi,cx)),mv(mm(yi,x),cy))
            lab[i],lab[i+1]=lab[i+1],lab[i]
    return g,vals,lab
gF,_,lab=act(g0,None,list(range(20)),W)
print('word length:',len(W),'; permutation identity:',lab==list(range(20)))
print('final tuple equals paired reflections of final_roots:',gF==gT)
inv_w=[-s for s in reversed(W)]
gB,_,_=act(gF,None,list(range(20)),inv_w)
print('inverse word returns original tuple:',gB==g0)
# cocycle transport and cup preservation
L0=Local(g0); LF=Local(gF)
H0b=L0.comp
imgs=[]
for x in H0b+L0.B1:
    _,v2,_=act(g0,L0.values(x),list(range(20)),W)
    imgs.append(LF.coords(v2))
# image cocycles are cocycles for gF? check closure via LF.values roundtrip
ok_cocycle=all(LF.values(c)==act(g0,L0.values(x),list(range(20)),W)[1] for c,x in zip(imgs,H0b+L0.B1))
print('transported values are parabolic cochains for final tuple:',ok_cocycle)
Sinit=[[L0.S(x,y) for y in H0b] for x in H0b]
Sfin=[[LF.S(a,b) for b in imgs[:8]] for a in imgs[:8]]
print('cup preserved S_init = S_fin(transported):',Sinit==Sfin)
print('transported coboundaries are coboundaries in final:',all(rank(LF.B1+[c])==rank(LF.B1) for c in imgs[8:]))
print('transported H basis independent mod B1:',rank(LF.B1+imgs[:8])==rank(LF.B1)+8)
# A3 deletion ranks for final paired roots
R=[K(v) for v in C['final_roots']]
print('final root K-rank:',rank(R),'; deletion ranks:',[rank([R[j] for j in range(10) if j!=i]) for i in range(10)])
json.dump({'final_roots':C['final_roots']},open('final_roots_generating.json','w'))
