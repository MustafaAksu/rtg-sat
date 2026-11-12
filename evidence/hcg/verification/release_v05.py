"""Release transform for the HCG study ledger v0.5 (run from the repository root).

Input : DRAFT r2, rebuilt in memory from the ledger at tag hcg-v0.4 with the edits of make_v05_draft.py
        (SHA-256 of DRAFT r2 is checked; it is the text of PR #53 at head 6d8b665).
Output: hcg/HCG_STUDY_LEDGER.md, the adopted v0.5.
Labels and metadata only: title, date, status, build line, the words "draft"/"proposed" in headings and labels,
the PI role line, the version-history heading and the footer. No statement, grade, review state, scope guard or
OPEN item is changed. Each anchor must occur exactly once.
Usage: python3 evidence/hcg/verification/release_v05.py
"""
import hashlib
import importlib.util
import subprocess

DRAFT_SHA = 'd85e7fac6a9bac1af881595d7c48cc3e76216a17c958d8c70a649a9c8d93beb4'
DST = 'hcg/HCG_STUDY_LEDGER.md'

spec = importlib.util.spec_from_file_location('mk', 'evidence/hcg/verification/make_v05_draft.py')
mk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mk)

src = subprocess.check_output(['git', 'show', mk.SRC_REF]).decode('utf-8')
assert hashlib.sha256(src.encode('utf-8')).hexdigest() == mk.SRC_SHA
draft = mk.build(src)
assert hashlib.sha256(draft.encode('utf-8')).hexdigest() == DRAFT_SHA, 'DRAFT r2 not reproduced'

R = [
('# HCG study ledger v0.5 — DRAFT r2\n', '# HCG study ledger v0.5\n'),
('**Date:** 12 November 2026 (draft)\n', '**Date:** 12 November 2026\n'),
('''**Document status:** **DRAFT r2 — not adopted.** The governing edition is `hcg-v0.4`. This draft adds seven results of Δ27 (§6.25: the d = 6 chain, the reduction to the inducing datum, and the reflection dichotomy with its corollary for d ≤ 14) and one OPEN item, and changes nothing else of v0.4. It becomes an edition only through co-owner review, a release record and a PI decision. Adoption would **not** set any individual claim's review state to ACCEPTED and would not establish any external claim (Severn's Theorem 6.2 stays CLAIMED).''',
 '''**Document status:** ADOPTED (scoped) — PI decision, 12 November 2026, 14:58 +03:00 ("1- Belirtildiği şekilde kabul ediyorum."), of DRAFT r2. It adds seven results of Δ27 (§6.25: the d = 6 chain, the reduction to the inducing datum, and the reflection dichotomy with its corollary for d ≤ 14) and one OPEN item, and changes nothing else of v0.4. Adoption does **not** set any individual claim's review state to ACCEPTED and does not establish any external claim (Severn's Theorem 6.2 stays CLAIMED). Release record: `records/hcg/HCG_v0.5_RELEASE_RECORD.md`. The edition is published by the annotated tag `hcg-v0.5`.'''),
('''Text that the script does not touch is the v0.4 text, byte for byte.''',
 '''Text that the script does not touch is the v0.4 text, byte for byte. Released from DRAFT r2 (SHA-256 d85e7fac6a9bac1af881595d7c48cc3e76216a17c958d8c70a649a9c8d93beb4) by `evidence/hcg/verification/release_v05.py` (labels and metadata only).'''),
('**Supersedes (on adoption only):** `hcg-v0.4`.', '**Supersedes:** `hcg-v0.4`.'),
('The claim tags are not re-graded in this draft.', 'The claim tags are not re-graded in this edition.'),
('- **New in this draft (Δ27, seven results).**', '- **New in this edition (Δ27, seven results).**'),
('### §1.5 New in v0.5 (proposed)', '### §1.5 New in v0.5'),
('| Item | v0.4 state | v0.5 state (proposed) | Record |', '| Item | v0.4 state | v0.5 state | Record |'),
('aksi PI tarafından bildirilene kadar geçerli." No claim row is ACCEPTED. |',
 'aksi PI tarafından bildirilene kadar geçerli." Adopted v0.5 (scoped), with the RTG pins unchanged (12 Nov 2026). No claim row is ACCEPTED. |'),
('### v0.5 DRAFT r2 — 12 November 2026 — DRAFT (not adopted)\n',
 '''### v0.5 — 12 November 2026 — ADOPTED (scoped)

- **Owner decision [governance]:** PI adoption, 12 Nov 2026, 14:58 +03:00, of DRAFT r2 (d85e7fac…8d93beb4): "1- Belirtildiği şekilde kabul ediyorum."; RTG pins kept, no OFN pin ("2- RTG pinleri belirtildiği gibi OFN yok"). Basis: ChatGPT co-owner reviews of the three acceptance matrices and of PR #53. Release record: `records/hcg/HCG_v0.5_RELEASE_RECORD.md`.
- **Release transform [governance]:** `release_v05.py`, labels and metadata only. The entries below are the DRAFT r2 record.
'''),
('*END OF DOCUMENT — HCG study ledger v0.5 · DRAFT r2 · 12 Nov 2026 · not adopted; `hcg-v0.4` governs · not an RTG document.*',
 '*END OF DOCUMENT — HCG study ledger v0.5 · ADOPTED (scoped) 12 Nov 2026 · no claim row is ACCEPTED · not an RTG document.*'),
]
out = draft
for old, new in R:
    assert draft.count(old) == 1 and out.count(old) == 1, old[:60]
    out = out.replace(old, new)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(out)
print('label edits:', len(R))
print('lines:', out.count('\n'))
print('v0.5 SHA-256:', hashlib.sha256(out.encode('utf-8')).hexdigest())
