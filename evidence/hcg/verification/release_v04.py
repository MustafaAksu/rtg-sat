"""Release transform for the HCG study ledger v0.4 (run from the repository root).

Input : DRAFT r2, rebuilt in memory from the ledger at tag hcg-v0.3 with the edits of make_v04_draft.py
        (SHA-256 of DRAFT r2 is checked; it is the text reviewed in PR #40 at head e95f92c).
Output: hcg/HCG_STUDY_LEDGER.md, the adopted v0.4.
Labels and metadata only: title, date, status, build line, the words "draft"/"proposed" in headings and labels,
the PI role line, the version-history heading and the footer. No statement, grade, review state, scope guard or
OPEN item is changed. Each anchor must occur exactly once.
Usage: python3 evidence/hcg/verification/release_v04.py
"""
import hashlib
import importlib.util
import subprocess

DRAFT_SHA = 'a23aef682216df98b578d5ca4744465fa8ec9538b8edde68f8dd0ec9070a39ad'
DST = 'hcg/HCG_STUDY_LEDGER.md'

spec = importlib.util.spec_from_file_location('mk', 'evidence/hcg/verification/make_v04_draft.py')
mk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mk)

src = subprocess.check_output(['git', 'show', mk.SRC_REF]).decode('utf-8')
assert hashlib.sha256(src.encode('utf-8')).hexdigest() == mk.SRC_SHA
draft = mk.build(src)
assert hashlib.sha256(draft.encode('utf-8')).hexdigest() == DRAFT_SHA, 'DRAFT r2 not reproduced'

R = [
('# HCG study ledger v0.4 — DRAFT r2\n', '# HCG study ledger v0.4\n'),
('**Date:** 11 November 2026 (draft)\n', '**Date:** 11 November 2026\n'),
('''**Document status:** **DRAFT r2 — not adopted.** The governing edition is `hcg-v0.3`. This draft adds two results of Δ27 (§6.24) and changes nothing else of v0.3. It becomes an edition only through co-owner review, a release record and a PI decision. Adoption would **not** set any individual claim's review state to ACCEPTED and would not establish any external claim (Severn's Theorem 6.2 stays CLAIMED).''',
 '''**Document status:** ADOPTED (scoped) — PI decision, 11 November 2026 ("1- İncelenen DRAFT r2'nin `hcg-v0.4` olarak scoped kabulü uygun"; recorded on PR #40), following the ChatGPT co-owner review "ACCEPT SCOPED" of DRAFT r2. It adds two results of Δ27 (§6.24) and changes nothing else of v0.3. Adoption does **not** set any individual claim's review state to ACCEPTED and does not establish any external claim (Severn's Theorem 6.2 stays CLAIMED). Release record: `records/hcg/HCG_v0.4_RELEASE_RECORD.md`. The edition is published by the annotated tag `hcg-v0.4`.'''),
('''Text that the script does not touch is the v0.3 text, byte for byte.''',
 '''Text that the script does not touch is the v0.3 text, byte for byte. Released from DRAFT r2 (SHA-256 a23aef682216df98b578d5ca4744465fa8ec9538b8edde68f8dd0ec9070a39ad) by `evidence/hcg/verification/release_v04.py` (labels and metadata only).'''),
('**Supersedes (on adoption only):** `hcg-v0.3`.', '**Supersedes:** `hcg-v0.3`.'),
('The claim tags are not re-graded in this draft.', 'The claim tags are not re-graded in this edition.'),
('- **New in this draft (Δ27, two results only).**', '- **New in this edition (Δ27, two results only).**'),
('### §1.4 New in v0.4 (proposed)', '### §1.4 New in v0.4'),
('| Item | v0.3 state | v0.4 state (proposed) | Record |', '| Item | v0.3 state | v0.4 state | Record |'),
('Decided on 11 Nov 2026 that no third-family reading of the two results of §6.24 is requested for now and that they stay CHECKED (two AIs). No claim row is ACCEPTED.',
 'Decided on 11 Nov 2026 that no third-family reading of the two results of §6.24 is requested for now and that they stay CHECKED (two AIs). Adopted v0.4 (scoped), with the RTG pins unchanged (11 Nov 2026). No claim row is ACCEPTED.'),
('### v0.4 DRAFT r2 — 11 November 2026 — DRAFT (not adopted)\n',
 '''### v0.4 — 11 November 2026 — ADOPTED (scoped)

- **Owner decision [governance]:** PI adoption, 11 Nov 2026, of DRAFT r2 (a23aef68…070a39ad): "1- İncelenen DRAFT r2'nin `hcg-v0.4` olarak scoped kabulü uygun"; the RTG pins are kept and there is no OFN pin (decision 2 of the same record). Recorded on PR #40. Basis: ChatGPT co-owner reviews of PR #40 (r1: three corrections; r2: ACCEPT SCOPED). Release record: `records/hcg/HCG_v0.4_RELEASE_RECORD.md`.
- **Release transform [governance]:** `release_v04.py`, labels and metadata only. The entries below are the DRAFT r2 record.
'''),
('*END OF DOCUMENT — HCG study ledger v0.4 · DRAFT r2 · 11 Nov 2026 · not adopted; `hcg-v0.3` governs · not an RTG document.*',
 '*END OF DOCUMENT — HCG study ledger v0.4 · ADOPTED (scoped) 11 Nov 2026 · no claim row is ACCEPTED · not an RTG document.*'),
]
out = draft
for old, new in R:
    assert draft.count(old) == 1 and out.count(old) == 1, old[:60]
    out = out.replace(old, new)
open(DST, 'w', encoding='utf-8').write(out)
print('label edits:', len(R))
print('lines:', out.count('\n'))
print('v0.4 SHA-256:', hashlib.sha256(out.encode('utf-8')).hexdigest())
