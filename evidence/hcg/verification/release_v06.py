"""Release transform for the HCG study ledger v0.6 (run from the repository root).

Input : DRAFT r2, rebuilt in memory from the ledger at tag hcg-v0.5 with the edits of make_v06_draft.py
        (SHA-256 of DRAFT r2 is checked; it is the text of PR #72 at head ed0b732).
Output: hcg/HCG_STUDY_LEDGER.md, the adopted v0.6.
Labels and metadata only: title, date, status, build line, the words "draft"/"proposed" in headings and labels,
the three places where the closure of OPEN 10 for v2 §11 was written as taking effect with the adoption (now
dated), the PI role line, the version-history heading and the footer. No statement, grade, review state, scope
guard or OPEN item is otherwise changed. Each anchor must occur exactly once.
Usage: python3 evidence/hcg/verification/release_v06.py
"""
import hashlib
import importlib.util
import subprocess

DRAFT_SHA = '05e2de260d535a10424a536f341f0517aa4d04bc1dca547b83c3506c12b7e513'
DST = 'hcg/HCG_STUDY_LEDGER.md'

spec = importlib.util.spec_from_file_location('mk', 'evidence/hcg/verification/make_v06_draft.py')
mk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mk)

src = subprocess.check_output(['git', 'show', mk.SRC_REF]).decode('utf-8')
assert hashlib.sha256(src.encode('utf-8')).hexdigest() == mk.SRC_SHA
draft = mk.build(src)
assert hashlib.sha256(draft.encode('utf-8')).hexdigest() == DRAFT_SHA, 'DRAFT r2 not reproduced'

R = [
('# HCG study ledger v0.6 — DRAFT r2\n', '# HCG study ledger v0.6\n'),
('**Date:** 14 November 2026 (draft)\n', '**Date:** 16 November 2026\n'),
('''**Document status:** **DRAFT r2 — not adopted.** The governing edition is `hcg-v0.5`. This draft records two line-by-line reviews of Severn's v2 against its source (§6.26: the every-member and compensation steps; the passage from Weil classes to all Hodge classes on powers), the PI's closure of OPEN 8 in its scope, a proposed split of OPEN 10, and one scope guard (SG-14). It changes nothing else of v0.5. It becomes an edition only through co-owner review, a release record and a PI decision. Adoption would **not** set any individual claim's review state to ACCEPTED and would not establish any external claim (Severn's theorems stay CLAIMED).''',
 '''**Document status:** ADOPTED (scoped) — PI decision, 16 November 2026, 09:36 +03:00 ("benimsiyorum."), of DRAFT r2. It records two line-by-line reviews of Severn's v2 against its source (§6.26: the every-member and compensation steps; the passage from Weil classes to all Hodge classes on powers), the PI's closure of OPEN 8 in its scope, the split of OPEN 10 (v2 §11 closed in its scope; v2 §12 now OPEN 12), and one scope guard (SG-14). It changes nothing else of v0.5. Adoption does **not** set any individual claim's review state to ACCEPTED and does not establish any external claim (Severn's theorems stay CLAIMED). Release record: `records/hcg/HCG_v0.6_RELEASE_RECORD.md`. The edition is published by the annotated tag `hcg-v0.6`.'''),
('''Text that the script does not touch is the v0.5 text, byte for byte.''',
 '''Text that the script does not touch is the v0.5 text, byte for byte. Released from DRAFT r2 (SHA-256 05e2de260d535a10424a536f341f0517aa4d04bc1dca547b83c3506c12b7e513) by `evidence/hcg/verification/release_v06.py` (labels and metadata only).'''),
('**Supersedes (on adoption only):** `hcg-v0.5`.', '**Supersedes:** `hcg-v0.5`.'),
('The claim tags are not re-graded in this draft.', 'The claim tags are not re-graded in this edition.'),
('- **New in this draft (v2 source reviews).**', '- **New in this edition (v2 source reviews).**'),
('### §1.6 New in v0.6 (proposed)', '### §1.6 New in v0.6'),
('| Item | v0.5 state | v0.6 state (proposed) | Record |', '| Item | v0.5 state | v0.6 state | Record |'),
('**CLOSED in its scope: v2 §11 only** (proposed; takes effect with the adoption of this edition) |',
 '**CLOSED in its scope: v2 §11 only** (PI, with the adoption of this edition, 16 Nov 2026) |'),
('(changed in v0.6; proposed in the draft and decided by the PI with the adoption of this edition)',
 '(changed in v0.6; decided by the PI with the adoption of this edition, 16 Nov 2026)'),
('OPEN 10 closed in its scope for v2 §11 (proposed; decided with the adoption of this edition).',
 'OPEN 10 closed in its scope for v2 §11 (PI, with the adoption of this edition, 16 Nov 2026).'),
('"PR61 i birleştirelim OPEN8 i artık kapayalım."). No claim row is ACCEPTED. |',
 '"PR61 i birleştirelim OPEN8 i artık kapayalım."). Adopted v0.6 (scoped), with the RTG pins unchanged, and with it closed OPEN 10 in its scope for v2 §11 (16 Nov 2026). No claim row is ACCEPTED. |'),
('### v0.6 DRAFT r2 — 14 November 2026 — DRAFT (not adopted)\n',
 '''### v0.6 — 16 November 2026 — ADOPTED (scoped)

- **Owner decision [governance]:** PI adoption, 16 Nov 2026, 09:36 +03:00, of DRAFT r2 (05e2de26…12b7e513): "benimsiyorum."; RTG pins kept, no OFN pin, as in v0.3–v0.5. Basis: ChatGPT co-owner reviews of the three review records (PRs #61, #67) and of PR #72 (r1: ACCEPT WITH CHANGE; r2: ACCEPT SCOPED). Release record: `records/hcg/HCG_v0.6_RELEASE_RECORD.md`.
- **Release transform [governance]:** `release_v06.py`, labels and metadata only. The entries below are the DRAFT r2 record.
'''),
('*END OF DOCUMENT — HCG study ledger v0.6 · DRAFT r2 · 14 Nov 2026 · not adopted; `hcg-v0.5` governs · not an RTG document.*',
 '*END OF DOCUMENT — HCG study ledger v0.6 · ADOPTED (scoped) 16 Nov 2026 · no claim row is ACCEPTED · not an RTG document.*'),
]
out = draft
for old, new in R:
    assert draft.count(old) == 1 and out.count(old) == 1, old[:60]
    out = out.replace(old, new)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(out)
print('label edits:', len(R))
print('lines:', out.count('\n'))
print('v0.6 SHA-256:', hashlib.sha256(out.encode('utf-8')).hexdigest())
