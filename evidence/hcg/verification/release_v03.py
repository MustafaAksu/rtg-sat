"""Release transform for the HCG study ledger v0.3 (run from the repository root).

Input : DRAFT r2, rebuilt in memory from the adopted v0.2 text with the edits of make_v03_draft.py
        (SHA-256 of DRAFT r2 is checked; it is the text reviewed in PR #31, head 4c6912f).
Output: hcg/HCG_STUDY_LEDGER.md, the adopted v0.3.
Labels and metadata only: title, date, status, build line, the words "draft"/"proposed" in headings and
labels, the pin sentence, the PI role line, the version-history heading and the footer. No statement,
grade, review state, scope guard or OPEN item is changed. Each anchor must occur exactly once.
Usage: python3 evidence/hcg/verification/release_v03.py
"""
import hashlib
import importlib.util

DRAFT_SHA = '23929cceec6e1e9aa5cb4082522cfc04b943824c578cee3a17d23be355aeef2e'
DST = 'hcg/HCG_STUDY_LEDGER.md'

spec = importlib.util.spec_from_file_location('mk', 'evidence/hcg/verification/make_v03_draft.py')
mk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mk)

src = open(mk.SRC, encoding='utf-8').read()
assert hashlib.sha256(src.encode('utf-8')).hexdigest() == mk.SRC_SHA
draft = src
for kind, old, new in mk.EDITS:
    if old != new:
        assert draft.count(old) == 1
        draft = draft.replace(old, new)
assert hashlib.sha256(draft.encode('utf-8')).hexdigest() == DRAFT_SHA, 'DRAFT r2 not reproduced'

R = [
('# HCG study ledger v0.3 — DRAFT r2\n', '# HCG study ledger v0.3\n'),
('**Date:** 11 November 2026 (draft)\n', '**Date:** 11 November 2026\n'),
('''**Document status:** **DRAFT r2 — not adopted.** The governing edition is `hcg-v0.2`. This draft proposes the changes of Δ24–Δ26 and the RTG import review. It becomes an edition only through co-owner review, a release record and a PI decision. Adoption would **not** set any individual claim's review state to ACCEPTED and would not establish any external claim (Severn's Theorem 6.2 stays CLAIMED).''',
 '''**Document status:** ADOPTED (scoped) — PI decision, 11 November 2026, 08:54 +03:00 ("1 Kabul ettim"), following the ChatGPT co-owner review "ACCEPT SCOPED" of DRAFT r2 (PR #31). It carries the changes of Δ24–Δ26 and the RTG import review. Adoption does **not** set any individual claim's review state to ACCEPTED and does not establish any external claim (Severn's Theorem 6.2 stays CLAIMED). Release record: `records/hcg/HCG_v0.3_RELEASE_RECORD.md`. The edition is published by the annotated tag `hcg-v0.3`.'''),
('''Text that the script does not touch is the v0.2 text, byte for byte.''',
 '''Text that the script does not touch is the v0.2 text, byte for byte. Released from DRAFT r2 (SHA-256 23929cceec6e1e9aa5cb4082522cfc04b943824c578cee3a17d23be355aeef2e) by `evidence/hcg/verification/release_v03.py` (labels and metadata only).'''),
('**Supersedes (on adoption only):** `hcg-v0.2`.', '**Supersedes:** `hcg-v0.2`.'),
('The claim tags are not re-graded in this draft.', 'The claim tags are not re-graded in this edition.'),
('- **New in this draft (Δ25, Δ26).**', '- **New in this edition (Δ25, Δ26).**'),
('### §1.3 Changed or new in v0.3 (proposed; each row cites its change record)', '### §1.3 Changed or new in v0.3 (each row cites its change record)'),
('| Item | v0.2 state | v0.3 state (proposed) | Record |', '| Item | v0.2 state | v0.3 state | Record |'),
('Pins proposed for this edition (PI decision pending): `dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4` in `rtg-corpus`.',
 'Pins of this edition (approved by the PI on 11 Nov 2026: "2 Onaylıyorum"): `dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4` in `rtg-corpus`. There is no OFN pin.'),
('between the historical and the proposed tags', 'between the historical and the pinned tags'),
('| Import | Statement | Source at the proposed tag | Source grade and scope | Use in HCG |', '| Import | Statement | Source at the pinned tag | Source grade and scope | Use in HCG |'),
('only Δ24–Δ26 are inputs of this draft', 'only Δ24–Δ26 are inputs of this edition'),
(':: review basis of this draft', ':: review basis of this edition'),
('Decided on 10 Nov 2026 that OPEN 8 stays PARTIAL and that `HCG-OPEN-SEVERN-V2` is closed in its verified scope. No claim row is ACCEPTED.',
 'Decided on 10 Nov 2026 that OPEN 8 stays PARTIAL and that `HCG-OPEN-SEVERN-V2` is closed in its verified scope. Adopted v0.3 (scoped) and approved its RTG pins (11 Nov 2026). No claim row is ACCEPTED.'),
('### v0.3 DRAFT r2 — 11 November 2026 — DRAFT (not adopted)\n',
 '''### v0.3 — 11 November 2026 — ADOPTED (scoped)

- **Owner decision [governance]:** PI adoption, 11 Nov 2026, 08:54 +03:00 ("1 Kabul ettim"), of DRAFT r2 (23929cce…5aeef2e); RTG pins approved in the same message ("2 Onaylıyorum"). Basis: ChatGPT co-owner reviews of PR #31 (r1: CHANGES REQUIRED; r2: ACCEPT SCOPED). Release record: `records/hcg/HCG_v0.3_RELEASE_RECORD.md`.
- **Release transform [governance]:** `release_v03.py`, labels and metadata only. The entries below are the DRAFT r2 record.
'''),
('- **Review-state changes (proposed).**', '- **Review-state changes.**'),
('- **OPEN changes (proposed).**', '- **OPEN changes.**'),
('*END OF DOCUMENT — HCG study ledger v0.3 · DRAFT r2 · 11 Nov 2026 · not adopted; `hcg-v0.2` governs · not an RTG document.*',
 '*END OF DOCUMENT — HCG study ledger v0.3 · ADOPTED (scoped) 11 Nov 2026 · no claim row is ACCEPTED · not an RTG document.*'),
]
out = draft
for old, new in R:
    assert draft.count(old) == 1 and out.count(old) == 1, old[:60]
    out = out.replace(old, new)
open(DST, 'w', encoding='utf-8').write(out)
print('label edits:', len(R))
print('lines:', out.count('\n'))
print('v0.3 SHA-256:', hashlib.sha256(out.encode('utf-8')).hexdigest())
