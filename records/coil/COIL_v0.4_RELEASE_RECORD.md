# COIL v0.4 — release record (DRAFT, maintenance)

**Status:** DRAFT — not adopted. Successor of `coil-v0.3` (`records/coil/COIL_v0.3_RELEASE_RECORD.md`). Becomes the adoption record of tag `coil-v0.4` when the PI adopts it. Triggered by the SAT advisory `pipes/COIL/20261109-SAT-maintenance-advisory.md` (disposition: accept with change).
**Scope:** maintenance of live documents only — guard naming, metadata, interfaces. No frozen file, translation, adopted release record or earlier tag is changed. No scientific claim, grade, negative result, retraction or OPEN item changes.

## 1. Changes of meaning

| # | Where | v0.3 said | v0.4 says | Reason |
|---|---|---|---|---|
| V1 | charter §0.2 (new guard), §0.3 pin row, §4, §9.0 firewall row, §10/§4-H criterion text; RMT §1 boundary and §4-H; RM-01 header, bridge burden, separation note; RM-02 wall; MM-1 header and §6; IDEALOG header; carrier audit header and §8; ringdiag record header; index §10; glossary; `REGISTRY.md` transfer rule | the MM-1/RM-01 separation was named "SG-PROG-1" (RTG's guard) | **SG-COIL-1** defined once in charter §0.2 (wording agreed with the co-owner review of 9 Nov 2026) and cited for the MM-1/RM-01 boundary everywhere; SG-PROG-1 and SG-PROG-4 (`programme-v1.4` §§3.2, 8) cited only where RTG-side material is bound by them (charter §0.3; RM-01 bridge-theorem criterion; RM-02 .c discrete-branch firewall; RMT RTG-counterpart criterion) | scope correction: SG-PROG-1 governs transfer across RTG's own discrete/continuous branches; using it as the name of COIL's separation rule was a borrowing of authority. **The "no named bridge" result is unchanged**; "no such bridge has been adopted" is recorded as current state, separate from the rule |
| V2 | charter header line 3; §0.1 `[DRAFT]` row | "none yet"; "[DRAFT] = document status" | governing edition `coil-v0.3`; `[DRAFT]` = document **class**, not release/adoption status | stale metadata; no grade change |
| V3 | charter §0.3 (new paragraph) | — | interfaces: COIL is not an admitted LIT consumer and claims no LIT-backed validation; transfer to RTG only via `rtg-corpus/pipes/<STREAM>/` with owner scope, evidence and source tag; filing ≠ adopted use; `pipes/COIL/` read at each owner pass and before each release | advisory item 4 |

## 2. Unchanged (advisory item 3, confirmed)

Carrier-audit v3.0 → v3.1 withdrawal; OPEN-QUOTIENT-EQUILIBRIUM parked; compendium not a self-contained rerun contract; Casebook F2 T = {54, 108} validation `[OPEN]`; two historical sources not available; all grades and labels.

## 3. Deferred to the PI

PR #9 (co-owner review tools auditing the pre-correction PR #10 candidates): merge as a historical review record with the limit note, or close. Owners' recommendation: merge with the note. Not part of this release.

## 4. RTG pins

Unchanged: `dyad-v6.4.23`, `legacy-v0.7`, `programme-v1.4` (now also cited for SG-PROG-4 §8), `methodology-v1.4`.

## 5. Checks

- No frozen file, translation, `evidence/`, `upload/` or adopted release record touched (diff limited to `coil/*.md`, `coil/records/*.md`, `REGISTRY.md`, the pipe item and this record).
- Every remaining `SG-PROG-1` occurrence in `coil/` refers to RTG-side material (listed in V1).
- No hash, approval or file content invented.

## 6. Candidate adoption manifest

Added in a manifest-only commit after the content commit, as in v0.1–v0.3 §6: *(pending)*.
