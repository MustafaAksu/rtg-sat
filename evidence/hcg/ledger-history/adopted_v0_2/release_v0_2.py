#!/usr/bin/env python3
"""Metadata-only release of HCG v0.2: DRAFT r2 -> ADOPTED.
Changes only: status line, revision/release-source line, supersedes line,
Appendix A adoption entry, footer. Every edit is assertion-gated, and a
structural check confirms that no other line changed."""
import hashlib, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r2.md')
OUT = os.path.join(HERE, 'HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md')
SRC_SHA = 'c8d595aefefc2fe488d24c6d9db258a702df1b51a4a151bcb29a6723c1752b2c'
sha = lambda b: hashlib.sha256(b).hexdigest()

raw = open(SRC, 'rb').read(); assert sha(raw) == SRC_SHA, 'r2 hash mismatch'
src = raw.decode('utf-8'); doc = src

def sub_line(prefix, new):
    global doc
    ls = doc.split('\n'); hits = [i for i, l in enumerate(ls) if l.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits)); ls[hits[0]] = new; doc = '\n'.join(ls)

sub_line('**Document status:** DRAFT — v0.2 candidate',
 '**Document status:** ADOPTED (scoped) — PI decision, 26 October 2026, 22:44 +03:00 ("Evet v0.2 yi ben de benimsiyorum(PI:Mustafa)"), following ChatGPT\'s adoption assessment "ACCEPT SCOPED". Adopted as the scoped scientific-record consolidation of the HCG session. Adoption does **not** set any individual claim\'s review state to ACCEPTED, does not establish any external claim (Severn Thm 6.2 stays CLAIMED), and is not an RTG adoption. Release record: `HCG_HODGE_SESSION_DSN_v0_2_RELEASE_RECORD.md`.')
sub_line('**Revision:** DRAFT r2 (26 Oct 2026).',
 '**Release source:** DRAFT r2 (`HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r2.md`, SHA-256 c8d595aefefc2fe488d24c6d9db258a702df1b51a4a151bcb29a6723c1752b2c; preserved unchanged), released by `release_v0_2.py` (labels and metadata only). r2 implements ChatGPT QA R01–R07; DRAFT r1 (SHA-256 c15815efeefcdaafa97f3f98688661c27ff43263543fe1198b2c4eec8a33ab61) is preserved unchanged.')
sub_line('**Supersedes (on adoption):**',
 '**Supersedes:** HCG_HODGE_SESSION_DSN_v0.1 (adopted 22 Oct 2026; preserved unchanged, SHA-256 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7). From this release, v0.2 is the governing record of the session.')
A = '### v0.2 DRAFT r2 — 26 October 2026 — DRAFT\n'
assert doc.count(A) == 1
doc = doc.replace(A, '''### v0.2 — adopted 26 October 2026 (scoped)

- **Owner decision [governance]:** PI adoption, 26 Oct 2026, 22:44 +03:00 ("Evet v0.2 yi ben de benimsiyorum(PI:Mustafa)"), of DRAFT r2 (c8d595ae…c1752b2c). Basis: ChatGPT r2 QA (`HCG_V02_DRAFT_R2_CHATGPT_QA_v0_1.md`, f41117eb…22ba572ffa; PASS / ACCEPT SCOPED FOR DRAFT QA) and ChatGPT's adoption assessment (ACCEPT SCOPED). Scope: the session's scientific-record consolidation. Severn Thm 6.2 stays CLAIMED; PO-1–PO-4 stay INTERNAL CHECKED with Priority B pending; PO-5 and the W5 application of PO-6 stay THIRD-FAMILY CHECKED; OPEN 8 and the general [19, Lemma 6.2] stay OPEN. No RTG transfer. The distribution guard stays in force.
- **Release edits [editorial]:** document status, release-source line, supersedes line, this entry, footer. No scientific text, grade, RID or OPEN status changed.
- **Chain:** r1 (c15815ef…a33ab61) → r2 (c8d595ae…c1752b2c) → this file. Builds of r1 and r2 reproduced byte-exactly by ChatGPT.

''' + A)
sub_line('*END OF DOCUMENT', '*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.2 · ADOPTED (scoped) 26 Oct 2026 · INTERNAL (withhold from the third-family auditor until round 2 is complete) · not RTG-adopted; PI-adopted as a scoped session-record consolidation only.*')

# Structural checks: only the gated lines differ; RIDs, OPEN headings and tags preserved
import difflib
a, b = src.split('\n'), doc.split('\n')
changed = [l for l in difflib.unified_diff(a, b, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
removed = [l for l in changed if l.startswith('-') and l != '-']
assert len(removed) == 4, removed   # status, revision, supersedes, footer
# Exact reverse check: drop the inserted Appendix A block and restore the 4 lines -> must equal r2
i = doc.index('### v0.2 — adopted 26 October 2026 (scoped)\n'); j = doc.index(A)
back = (doc[:i] + doc[j:]).split('\n')
for k, l in enumerate(back):
    for r in removed:
        pass
newl = [l for l in changed if l.startswith('+') and l != '+']
ra = {n[1:]: r[1:] for n, r in zip([x for x in newl if not x.startswith('+### v0.2 — adopted') and not x.startswith('+- **')], removed)}
back = [ra.get(l, l) for l in back]
assert '\n'.join(back) == src, 'reverse check failed: release changed more than metadata'
rid = lambda t: sorted(set(re.findall(r'HCG-[A-Z0-9][A-Z0-9-]*', t)))
assert rid(src) == rid(doc), 'RID set changed'
openh = lambda t: re.findall(r'^\*\*OPEN \d+ — .*', t, re.M)
assert openh(src) == openh(doc), 'OPEN headings changed'
tags = lambda t: re.findall(r'provenance: [A-Z][A-Z -]+', t)
assert tags(src) == tags(doc), 'provenance grades changed'
open(OUT, 'w', encoding='utf-8').write(doc)
assert sha(open(SRC, 'rb').read()) == SRC_SHA
print('OK', OUT, sha(doc.encode()), len(b), 'lines;', len(changed), 'diff lines;', len(rid(doc)), 'RIDs;', len(openh(doc)), 'OPEN')
