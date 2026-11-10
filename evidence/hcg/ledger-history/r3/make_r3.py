"""HCG DSN v0.1 DRAFT r3 (final acceptance candidate) from byte-verified r2: source-dependency wording for Lemma 5.2 (ChatGPT r2 QA)."""
import hashlib
SRC='/home/claude/g34/dsn/r2/HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r2.md'
DST='/home/claude/g34/dsn/r3/HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r3.md'
EXP='959f6a036f8cacf530de427a3e26a9f7f2cb7fc6974e72071b183e961aa519dc'
b=open(SRC,'rb').read(); assert hashlib.sha256(b).hexdigest()==EXP
t=b.decode(); E=[]
def R(old,new):
    assert t.count(old)==1,(old,t.count(old)); E.append((old,new))
R('# HCG_HODGE_SESSION_DSN_v0.1 — DRAFT r2\n','# HCG_HODGE_SESSION_DSN_v0.1 — DRAFT r3 (final acceptance candidate)\n')
R('**Document status:** DRAFT r2. Not PI-adopted.','**Document status:** DRAFT r3 (final acceptance candidate). Not PI-adopted.')
R('**Revision base:** DRAFT v0.1','**Revision base:** DRAFT r2 (`HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r2.md`, SHA-256 959f6a036f8cacf530de427a3e26a9f7f2cb7fc6974e72071b183e961aa519dc; preserved unchanged), itself built from DRAFT v0.1')
R('[assuming: Severn [386] Lemma 5.2 = [19, Lemma 6.2] (hexagon:2610.00246v2), not yet reviewed]',
  '[assuming: Severn [386] Lemma 5.2 (cocycle formula), whose proof [386] does not repeat but takes from [19, Lemma 6.2] (hexagon:2610.00246v2); that source proof not yet reviewed]')
R("Open dependency: Severn's Lemma 5.2 is his [19, Lemma 6.2] (hexagon:2610.00246v2), which is not yet reviewed (OPEN 5).",
  "Open dependency: Severn [386] Lemma 5.2 relies, for its proof, on [19, Lemma 6.2] (hexagon:2610.00246v2): \"This is [19, Lemma 6.2]; as a companion paper we rely on it and do not repeat its derivation\" ([386] §5). That source proof is not yet reviewed (OPEN 5).")
R('with the unreviewed Lemma 5.2 / [19, Lemma 6.2] as an explicit `[assuming:]`.',
  'with the unreviewed Lemma 5.2 (resting on [19, Lemma 6.2]) as an explicit `[assuming:]`.')
R('### v0.1 DRAFT r2 — 22 October 2026 — DRAFT\n',
'''### v0.1 DRAFT r3 — 22 October 2026 — DRAFT (final acceptance candidate)

- **Basis [governance]:** ChatGPT QA of r2. It reproduced r2 byte-exactly from v0.1 with `make_r2.py` and found F01–F09 correctly addressed. It recommended one source-dependency wording change before acceptance. r2 is preserved unchanged (959f6a03…a519dc); r3 was built from the byte-verified r2 by `make_r3.py`.
- **§6.16, §2 OPEN 5 context, Appendix A F01 bullet [evidence/provenance]:** Replaced the identity "Severn [386] Lemma 5.2 = [19, Lemma 6.2]" with the actual relation. [386] Lemma 5.2 is stated in [386], and its proof is taken from [19, Lemma 6.2] (quoted). No scientific content, grade or RID changed.
- The r2 Appendix A entry below keeps its original wording for provenance.

### v0.1 DRAFT r2 — 22 October 2026 — DRAFT
''')
R('*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.1 DRAFT r2 ·','*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.1 DRAFT r3 (final acceptance candidate) ·')
for o,n in E: t=t.replace(o,n)
open(DST,'w').write(t); print(len(E),'edits', hashlib.sha256(t.encode()).hexdigest())
