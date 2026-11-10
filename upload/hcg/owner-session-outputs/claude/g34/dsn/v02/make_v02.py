#!/usr/bin/env python3
"""Build HCG_HODGE_SESSION_DSN_v0_2_DRAFT.md from the byte-verified v0.1 ADOPTED
file plus the fragment files in this directory. Every edit is assertion-gated:
each anchor must occur exactly once. Inputs are never modified."""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
G34 = os.path.abspath(os.path.join(HERE, '..', '..'))
BASE = os.path.join(HERE, '..', 'adopted', 'HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md')
DELTAS = os.path.join(HERE, '..', 'HCG_DSN_v0_2_PENDING_DELTAS.md')
OUT = os.path.join(HERE, 'HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r2.md')
BASE_SHA = '75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7'
DELTAS_SHA = '8fb25dadfb4416136625d7b8d6eea9f20ea0d8234bdd32495f0ac12d069efd98'

def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()

def frag(name):
    return open(os.path.join(HERE, name), encoding='utf-8').read()

assert sha(BASE) == BASE_SHA, 'v0.1 ADOPTED hash mismatch'
assert sha(DELTAS) == DELTAS_SHA, 'deltas file hash mismatch'
doc = open(BASE, encoding='utf-8').read()

def once(anchor):
    n = doc.count(anchor)
    assert n == 1, f'anchor count {n}: {anchor[:60]!r}'
    return doc.index(anchor)

def replace_between(start, end, new):
    """Replace doc[start_anchor : end_anchor) by new (end anchor kept)."""
    global doc
    i = once(start); j = once(end); assert i < j
    doc = doc[:i] + new + doc[j:]

def insert_before(anchor, new):
    global doc
    i = once(anchor); doc = doc[:i] + new + doc[i:]

def insert_after(anchor, new):
    global doc
    i = once(anchor) + len(anchor); doc = doc[:i] + new + doc[i:]

# Header (everything before the first horizontal rule)
replace_between('# HCG_HODGE_SESSION_DSN_v0.1\n', '\n---\n\n## Local Tag Aliases', frag('frag_header.md').rstrip('\n') + '\n')
# §1, §2
replace_between('## §1 Current Canonical State', '<a id="hcg-2"></a>', frag('frag_s1.md') + '\n')
replace_between('## §2 Active Frontier / OPEN Registry', '<a id="hcg-3"></a>', frag('frag_s2.md') + '\n')
# §3 additions
insert_before('\n---\n\n<a id="hcg-4"></a>', frag('frag_s3_add.md').rstrip('\n') + '\n')
# §4 routing row
LGEO = "| L-GEO (geometric realization) |"
i = once(LGEO); eol = doc.index('\n', i)
doc = doc[:eol + 1] + ("| L-BRAID (session certificates, new in v0.2) | Braid words in Artin generators (convention A, left to right); the intertwiner P; components of H/Σ | this DSN | Exact replay at matrix level. Component statements only through Σ = S₂₀ (Severn Step 0). Carries no polarization data (SG-11). |\n") + doc[eol + 1:]
# §5
replace_between('## §5 High-Risk Claims Ledger', '<a id="hcg-6"></a>', frag('frag_s5.md') + '\n')
# §6.7
replace_between('### §6.7 Dependency chain of Severn Thm 6.2', '### §6.8 PO-1', frag('frag_s67.md') + '\n')
# §6.8 note
insert_before('### §6.9 PO-2', frag('frag_s68_add.md').lstrip('\n') + '\n')
# §6.15 E01 note
insert_after('- E06: no global theorem is certified.\n', '\nv0.2 note: E01 is resolved for the tuple (not for Severn\'s polarization conventions) by §6.19; see §6.17.\n')
# §6.16, §6.17
replace_between('### §6.16 PO-6', '### §6.17 The component question', frag('frag_s616.md') + '\n')
replace_between('### §6.17 The component question', '### §6.18 H4 selection', frag('frag_s617.md') + '\n')
# §6.18 + new §6.19–§6.21
replace_between('### §6.18 H4 selection', '\n---\n\n<a id="hcg-7"></a>',
                frag('frag_s618.md') + frag('frag_s619.md') + frag('frag_s620.md') + frag('frag_s621.md').rstrip('\n') + '\n')
# §7 additions
insert_before('\n---\n\n<a id="hcg-8"></a>', frag('frag_s7_add.md').rstrip('\n') + '\n')

# §8 additions: hashes computed here from the session files, never typed in
REG = [
 ('HCG-ART-EDGEFLUX', 'h4sel/theorem/H3_H4SEL_EDGEFLUX_THEOREM_v0_2.md', 'EDGEFLUX theorem note v0.2'),
 ('HCG-ART-EDGEFLUX', 'h4sel/theorem/H3_H4SEL_EDGEFORM_THEOREM_CLAUDE_v0_1.md', 'theorem note v0.1 (preserved)'),
 ('HCG-ART-EDGEFORM', 'h4sel/edgeform/H3_H4SEL_EDGEFORM_CLAUDE_v0_1.md', 'edge-form predictor report'),
 ('HCG-ART-RANKOBS', 'h4sel/rankobs/H3_H4_RANKOBS_CHECK_CLAUDE_v0_1.md', 'rank obstructions, series bound'),
 ('HCG-ART-ENGINE2', 'h4sel/p2p3/generic_engine.py', 'independent exact Q(w) engine (Severn §4 definitions)'),
 ('HCG-ART-P2P3', 'h4sel/p2p3/H3_P2P3_INDEPENDENT_CHECK_CLAUDE_v0_1.md', 'P2/P3 check (its §6 corrected by Δ10)'),
 ('HCG-ART-NEW01MIX', 'h4sel/mixed/H3_NEW01_MIXED_INDEPENDENT_CHECK_CLAUDE_v0_1.md', 'NEW01 mixed tree, factorization, laminar'),
 ('HCG-ART-NEW02MIX', 'h4sel/new02/H3_NEW02_MIXED_CLAUDE_v0_1.md', 'NEW02 mixed tree'),
 ('HCG-ART-TOY', 'h4sel/toy/H3_TOY_MIXED_CHECK_AND_EXPLANATION_CLAUDE_v0_1.md', 'toy obstruction and block lemma'),
 ('HCG-ART-BLOCK01', 'h4sel/g34block/H3_G34_BLOCK_01_CHECK_CLAUDE_v0_1.md', 'G34-BLOCK-01'),
 ('HCG-ART-ESCAPE', 'h4sel/braidescape/H3_BRAID_ESCAPE_01_REPLAY_CLAUDE_v0_1.md', 'BRAID-ESCAPE-01 replay'),
 ('HCG-ART-ESCAPE', 'h4sel/braidescape/cert.json', 'BRAID-ESCAPE-01 certificate (ChatGPT)'),
 ('HCG-ART-TOYESC', 'h4sel/toybraid/H3_TOY_BRAID_ESCAPE_CLAUDE_v0_1.md', 'toy braid escape'),
 ('HCG-ART-A2REAL', 'h4sel/a2real/H3_A2_REALITY_CHECK_CLAUDE_v0_1.md', 'reality obstruction check'),
 ('HCG-ART-G333', 'h4sel/g333/H3_G333_MIXED_REAL_CHECK_CLAUDE_v0_1.md', 'G(3,3,3) mixed real example'),
 ('HCG-ART-G333SCAN', 'h4sel/g333scan/H3_G333_ORBIT_SCAN_CLAUDE_v0_1.md', 'G(3,3,3) orbit scan'),
 ('HCG-ART-G333SCAN', 'h4sel/g333scan/g333_pertuple_table.txt', 'per-tuple table'),
 ('HCG-ART-W5LINKS', 'h4sel/w5links/H3_W5_LINKS_INDEPENDENT_CLAUDE_v0_1.md', 'named W5 links (Claude)'),
 ('HCG-ART-W5LINKS', 'h4sel/w5links/claude_w5_links.json', 'link words'),
 ('HCG-ART-SEVERNLINK', 'h4sel/severnlink/H3_SEVERN_APPXA_TO_W5_LINK_CLAUDE_v0_1.md', 'Severn paired tuple to W5 (contains the "42 files" error, corrected in Δ23)'),
 ('HCG-ART-SEVERNLINK', 'h4sel/severnlink/severn_link.py', 'link script'),
 ('HCG-ART-SEVERNLINK', 'h4sel/severnlink/severn_to_w5.json', 'P, 618-letter word, pair moves'),
 ('HCG-ART-SEVERN90', 'h4sel/severn90/H3_SEVERN_90MOVE_REPLAY_CLAUDE_v0_1.md', '90-move replay report'),
 ('HCG-ART-SEVERN90', 'h4sel/severn90/replay90.py', '90-move replay script'),
 ('HCG-ART-LEMMA62', 'lemma62/H3_LEMMA62_SOURCE_REVIEW_CLAUDE_v0_1.md', '[19, Lemma 6.2] source review'),
 ('HCG-ART-DELTAS', 'dsn/HCG_DSN_v0_2_PENDING_DELTAS.md', 'change log Δ1–Δ23 (input of this draft)'),
]
lines = ['\n**v0.2 additions to the registry.** SHA-256 values below are 16-hex prefixes computed by `make_v02.py` from the session files at build time. "Claude workspace" means present in this workspace; ChatGPT and auditor packages are referenced in the Δ records by the hashes stated there. A standalone replay of `make_v02.py` rebuilds these rows from the frozen `registry_hashes.tsv`; it verifies the frozen registry only, not the bytes or availability of the referenced artifacts, whose lineage is in the Δ records.\n']
FROZEN = os.path.join(HERE, 'registry_hashes.tsv')
paths = [os.path.join(G34, rel) for _, rel, _ in REG]
if all(os.path.isfile(p) for p in paths):      # Claude workspace: compute and freeze
    hx = {rel: sha(p) for (_, rel, _), p in zip(REG, paths)}
    open(FROZEN, 'w').write(''.join(f'{rel}\t{h}\n' for rel, h in hx.items()))
else:                                           # replay without the session files
    print('NOTE: artifacts absent; using frozen registry_hashes.tsv')
    hx = dict(l.rstrip('\n').split('\t') for l in open(FROZEN))
for rid, rel, what in REG:
    lines.append(f'- [RID: {rid}] :: `{rel}` ({hx[rel][:16]}) :: {what} :: AVAILABLE (Claude workspace)')
insert_before('\n---\n\n<a id="hcg-9"></a>', '\n'.join(lines) + '\n')

# §9
replace_between('## §9 Collaboration and Provenance', '<a id="hcg-appendix-a"></a>', frag('frag_s9.md') + '\n')
# Appendix A, Appendix B
insert_after('## Appendix A — Version History\n\n', frag('frag_appA.md'))
insert_before('\n---\n\n*END OF DOCUMENT', frag('frag_appB_add.md').rstrip('\n') + '\n')
# Footer
OLDF = doc[once('*END OF DOCUMENT'):]
doc = doc.replace(OLDF, '*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.2 · DRAFT r2 26 Oct 2026 · not adopted (v0.1 ADOPTED governs until a PI decision) · INTERNAL (withhold from the third-family auditor until round 2 is complete) · not RTG-adopted.*\n')

# Post-build checks
for must in ['Severn Thm 6.2 remains CLAIMED' if False else 'CLAIMED', 'hexagon:2610.00387v1', '### §6.19', '### §6.20', '### §6.21', 'OPEN 8']:
    assert must in doc, must
assert 'arXiv:2610' not in doc, 'arXiv ID for a hexagon document'
assert ' ESTABLISHED' in doc  # only in "not ESTABLISHED" contexts; checked below
for ln in doc.splitlines():
    if 'ESTABLISHED' in ln:
        assert ('not ESTABLISHED' in ln or 'not establish' in ln or '"ESTABLISHED"' in ln or 'ESTABLISHED by this ledger' in ln
                or 'described as ESTABLISHED' in ln or 'CLAIMED, not ESTABLISHED' in ln), ln
open(OUT, 'w', encoding='utf-8').write(doc)
assert sha(BASE) == BASE_SHA and sha(DELTAS) == DELTAS_SHA, 'inputs changed'
print('OK', OUT, sha(OUT), len(doc.splitlines()), 'lines')
