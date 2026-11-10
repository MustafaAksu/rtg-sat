"""Claude: BLOCK-ESCAPE-01 -> W5 by inverse(868-letter cert word) followed by Claude's BLOCK01->W5 word."""
exec(open('build_links.py').read().split("out={}")[0])
C=json.load(open('/home/claude/g34/h4sel/braidescape/cert.json'))
L=json.load(open('claude_w5_links.json'))['BLOCK01']['word']
w=[-x for x in reversed(C['braid_word_left_to_right'])]+L
gE=[]
for v in C['final_roots']: s=refl(K(v)); gE+=[s,s]
gF,_,lab=act(gE,None,list(range(20)),w)
print('ESCAPE -> W5: letters',len(w),'(unreduced); endpoint',gF==gT,'; pure',lab==list(range(20)))
