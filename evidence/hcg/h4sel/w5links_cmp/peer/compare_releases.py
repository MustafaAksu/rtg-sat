#!/usr/bin/env python3
"""Exact equality audit of sealed HCG braid-word archives; no network or scientific-engine dependencies."""
import hashlib,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
OLD=ROOT/'HCG_G34_W5_BRAID_LINKS_SESSION_v0_1.zip'
NEW=ROOT/'H3_W5_LINKS_CLAUDE_v0_1.zip'
OLD_SHA='00b93b575fbddd9a041fb695d6ca8c76d9d98a044e876f8431448cdbf3a6eec6'
NEW_SHA='d3a366119fbe563063d4c97e801432d3887289a5860402d7d26bb0c49e67bdec'
assert hashlib.sha256(OLD.read_bytes()).hexdigest()==OLD_SHA
assert hashlib.sha256(NEW.read_bytes()).hexdigest()==NEW_SHA
p='HCG_G34_TO_W5_BRAID_LINKS_SESSION_v0_1/'
with zipfile.ZipFile(OLD) as z1,zipfile.ZipFile(NEW) as z2:
    claude=json.loads(z2.read('claude_w5_links.json'))
    report=[]
    for name in ('NEW01','NEW02','NEW03','NEW04','BLOCK01'):
        old=('BLOCK' if name=='BLOCK01' else name)
        chat=json.loads(z1.read(p+old+'_TO_W5_PURE_BRAID_CERT.json'))
        other=claude[name]
        assert other['word']==chat['braid_word_1_based_left_to_right'],name
        assert [tuple(q) for q in other['pair_moves']]==[(q['target_pair_1based']-1,q['source_pair_1based']-1) for q in chat['operations']],name
        assert other['checks']==[True,True,True]
        assert chat['pure_braid'] and chat['endpoint_exact_projective'] and chat['inverse_exact_projective']
        new_src=('G34_BLOCK_01_roots.json' if name=='BLOCK01' else name+'_roots.json')
        assert z2.read(new_src)==z1.read(p+'source_inputs/'+old+'_roots.json'),name
        s=hashlib.sha256(json.dumps(other['word'],separators=(',',':')).encode()).hexdigest()
        report.append({'link':name+' -> W5','pair_moves':len(other['pair_moves']),'letters':len(other['word']),'word_sha256_normalized':s,'source_sha256':hashlib.sha256(z2.read(new_src)).hexdigest()})
        print('EXACT MATCH',name,len(other['pair_moves']),len(other['word']))
    assert z2.read('W5_BASELINE_ROOTS.json')==z1.read(p+'source_inputs/W5_roots.json')
    pre=json.loads(z1.read(p+'source_inputs/HCG_G34_BLOCK_BRAID_ESCAPE_01_CERTIFICATE_v0_1.json'))
    esc=json.loads(z1.read(p+'BLOCK_ESCAPE_TO_W5_PURE_BRAID_CERT.json'))
    combined=[-q for q in reversed(pre['braid_word_left_to_right'])]+claude['BLOCK01']['word']
    assert combined==esc['braid_word_1_based_left_to_right']
    assert len(combined)==1748 and esc['pure_braid'] and esc['endpoint_exact_projective'] and esc['inverse_exact_projective']
    report.append({'link':'BLOCK-ESCAPE -> W5','pair_moves':None,'letters':1748,'word_sha256_normalized':hashlib.sha256(json.dumps(combined,separators=(',',':')).encode()).hexdigest()})
    print('EXACT MATCH ESCAPE 1748')
    (ROOT/'word_match_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print('ALL SIX ARCHIVAL WORD MATCHES PASS')
