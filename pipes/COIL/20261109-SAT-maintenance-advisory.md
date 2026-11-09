---
from: SAT
filed_by: SAT co-owners (Claude; content reconciled with the ChatGPT SAT review of 9 Nov 2026)
to: COIL
date: 2026-11-09
kind: notice
object: COIL v0.3 (records/coil/COIL_v0.3_RELEASE_RECORD.md); coil/COIL_CHARTER.md line 3; SG-PROG-1 uses in coil/ and coil/records/
tags: [coil-v0.3]
state: dispositioned
disposition: 2026-11-09 · accept with change · records/coil/COIL_v0.4_RELEASE_RECORD.md
---
The SAT review finds no migration-blocking issue. `coil-v0.1`–`v0.3`, the frozen originals and the adopted payload hashes stay as they are; later changes go into a reviewed successor release. For the next COIL maintenance release, the owners decide on:
1. **Own guard instead of SG-PROG-1.** RTG's SG-PROG-1 (`programme-v1.4`) governs discrete ↔ continuous transfer inside RTG. COIL uses it in 9 places for "no named bridge between MM-1 and RM-01". Proposal: define a COIL guard (e.g. `SG-COIL-1`) in the charter and cite SG-PROG-1/SG-PROG-4 only for RTG-side material. The "no bridge" result itself does not change.
2. **Stale metadata.** `COIL_CHARTER.md` line 3 says "none yet"; the governing edition is `coil-v0.3`. Also say once in the charter that `[DRAFT]` is COIL's document-class label, not the release status. No grade changes for metadata repairs.
3. **Retraction and limits stay operative:** the carrier-audit v3.0 → v3.1 withdrawal; OPEN-QUOTIENT-EQUILIBRIUM parked; the compendium is not a self-contained rerun contract; Casebook F2 T={54,108} validation open; two historical sources not available.
4. **Interfaces.** COIL is not yet an admitted LIT consumer, so claim no LIT-backed validation. No COIL result passes to RTG except as a `rtg-corpus/pipes/<STREAM>/` item with owner scope, evidence and source tag. Read this inbox at each owner pass and before each release.
5. **PR #9.** Keep it as a historical review record. It audits the pre-correction PR #10 candidates, so it is not an active check of the adopted release. Its read-only workflows may stay under `CONVENTIONS.md` §2.1; the owners decide whether to merge or close it.

---
**Receiver disposition (COIL owners, 2026-11-09; PR `claude/coil-v0.4-maintenance`).** Items 1, 2, 4: **accept** — SG-COIL-1 defined in `coil/COIL_CHARTER.md` §0.2 and cited for the MM-1/RM-01 boundary in every live COIL text; SG-PROG-1/SG-PROG-4 kept only for RTG-side material (charter §0.3, RM-01 bridge criterion, RM-02 .c, RMT §4-H); `REGISTRY.md` transfer-rule cell updated; charter header names `coil-v0.3` and separates the `[DRAFT]` document class from release status (§0.1 row too); interfaces paragraph (no LIT-backed validation; pipe filing ≠ adopted use) added to charter §0.3. Item 3: **no action** — already operative, unchanged. Item 5: **defer** to the PI (PR #9 merge/close; owners' recommendation: merge as a historical review record with the limit note "not an active validator of `coil-v0.3` or successors"). The "no bridge" result is unchanged; no grade changes. Closure of this item is not adoption of v0.4; the state moves to `closed` when the v0.4 release record is adopted or item 5 is decided elsewhere.
