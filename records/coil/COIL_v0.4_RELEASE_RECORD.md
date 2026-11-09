# COIL v0.4 — release record (DRAFT, maintenance)

**Status:** **ADOPTED** by PI Mustafa Aksu on 2026-11-09 ("benimsiyorum", COIL owner session, after co-owner review `5826058891` ACCEPT WITH MINOR CHANGES and its application); publication tag `coil-v0.4`. Successor of `coil-v0.3` (`records/coil/COIL_v0.3_RELEASE_RECORD.md`). Triggered by the SAT advisory `pipes/COIL/20261109-SAT-maintenance-advisory.md` (disposition: accept with change).
**Scope:** maintenance of live documents only — guard naming, metadata, interfaces. No frozen file, translation, adopted release record or earlier tag is changed. No scientific claim, grade, negative result, retraction or OPEN item changes.

## 1. Changes of meaning

| # | Where | v0.3 said | v0.4 says | Reason |
|---|---|---|---|---|
| V1 | charter §0.2 (new guard), §0.3 pin row, §4, §9.0 firewall row, §10/§4-H criterion text; RMT §1 boundary and §4-H; RM-01 header, bridge burden, separation note; RM-02 wall; MM-1 header and §6; IDEALOG header; carrier audit header and §8; ringdiag record header; index §10; glossary; `REGISTRY.md` transfer rule | the MM-1/RM-01 separation was named "SG-PROG-1" (RTG's guard) | **SG-COIL-1** defined once in charter §0.2 (wording agreed with the co-owner review of 9 Nov 2026) and cited for the MM-1/RM-01 boundary everywhere; SG-PROG-1 and SG-PROG-4 (`programme-v1.4` §§3.2, 8) cited only where RTG-side material is bound by them (charter §0.3; RM-01 bridge-theorem criterion; RM-02 .c discrete-branch firewall; RMT RTG-counterpart criterion) | scope correction: SG-PROG-1 governs transfer across RTG's own discrete/continuous branches; using it as the name of COIL's separation rule was a borrowing of authority. **The "no named bridge" result is unchanged**; "no such bridge has been adopted" is recorded as current state, separate from the rule. **Scope clarification (PR #13 review `5826058891`):** SG-COIL-1 names the MM-1/RM-01 boundary; the same discipline applies separately to the MM-1/recovered-ringdiag route (carrier audit, ringdiag record) and the MM-1/RCSJ route (IDEALOG) — distinct source/target objects, none identified with RM-01 by the rule. Stated in charter §0.2 so that the citations in those documents do not read as an identification of ringdiag or RCSJ with RM-01 |
| V2 | charter header line 3; §0.1 `[DRAFT]` row | "none yet"; "[DRAFT] = document status" | governing edition `coil-v0.3`; `[DRAFT]` = document **class**, not release/adoption status | stale metadata; no grade change |
| V3 | charter §0.3 (new paragraph) | — | interfaces: COIL is not an admitted LIT consumer and claims no LIT-backed validation; transfer to RTG only via `rtg-corpus/pipes/<STREAM>/` with owner scope, evidence and source tag; filing ≠ adopted use; `pipes/COIL/` read at each owner pass and before each release | advisory item 4 |

## 2. Unchanged (advisory item 3, confirmed)

Carrier-audit v3.0 → v3.1 withdrawal; OPEN-QUOTIENT-EQUILIBRIUM parked; compendium not a self-contained rerun contract; Casebook F2 T = {54, 108} validation `[OPEN]`; two historical sources not available; all grades and labels.

## 3. Deferred to the PI

PR #9 (co-owner review tools auditing the pre-correction PR #10 candidates): merge as a historical review record with the limit note, or close. Owners' recommendation: merge with the note. Not part of this release.

## 3b. Publication step (applied)

Governing-edition fields in `coil/COIL_CHARTER.md` (header) and `REGISTRY.md` moved to `coil-v0.4`; the pipe item's state moved to `closed` (item 5 deferred to the PI's PR #9 decision, recorded in the disposition line); hashes of every changed file recomputed after this step (§6).

## 4. RTG pins

Unchanged: `dyad-v6.4.23`, `legacy-v0.7`, `programme-v1.4` (now also cited for SG-PROG-4 §8), `methodology-v1.4`.

## 5. Checks

- No frozen file, translation, `evidence/`, `upload/` or adopted release record touched (diff limited to `coil/*.md`, `coil/records/*.md`, `REGISTRY.md`, the pipe item and this record).
- Every remaining `SG-PROG-1` occurrence in `coil/` refers to RTG-side material (listed in V1).
- No hash, approval or file content invented.

## 6. Adoption manifest

**Status: ADOPTED (2026-11-09).** Files changed in this release, SHA-256 of their bytes at the **content commit** `5d0de2a568dfb4ccc773cfa701fcadac56a025a4` (this manifest-only commit follows it). Files not listed are inherited unchanged from `coil-v0.3`. If any file changes after this, hashes are recomputed after the change and before the tag.

| file | SHA-256 at content commit |
|---|---|
| `coil/COIL_CHARTER.md` | `160c9f314b1d9fe634770509a13dfafa781ec4d567db7461dbc161c5f7a440e5` |
| `coil/COIL_INDEX.md` | `126b4bed5d9dc3abd0353a6affd1c797a459c3478d25e992e796befa5e1298d8` |
| `coil/COIL_GLOSSARY.md` | `38a28248b75bc43fa3e03db9f071798d09242cc9d1f6376c7ffc747ab9ef21f6` |
| `coil/COIL_RMT.md` | `c04f0b9e89d62201be82b6a9f42f97b434e231ed5ef0bd5253a195ed08df48ea` |
| `coil/records/RM-01.md` | `c38736197230f0b456bb348f832b621b382663221bd3d3ee9194304aebb657c2` |
| `coil/records/RM-02.md` | `81eab406db499c12c28dcca5597b635ad9b774c075927669019a1198bd164fbb` |
| `coil/MM-1.md` | `f7f5f974eb4d282f4b316d14a8ed12a7a61d80435b111cb4c54525676314164a` |
| `coil/IDEALOG_COIL_RCSJ.md` | `b7e8003f0811197f86397f0895b8b3b265fa37ed97f5cbff92de350dc91490ce` |
| `coil/AUDIT_CARRIER_COMPLETENESS.md` | `dd395e4aab7e53af9998ff8f59fbe6336286d34d61974832330cbe3f1a9fcd6e` |
| `coil/RINGDIAG_UPDATE_RULE.md` | `a464a8e75c0deb692151dacbbd4bae1e0a5a8a1c4d10f1ae69e92f91a8815a0b` |
| `REGISTRY.md` | `c43a2770e6356f655a1631c2d89b67285390821fb4845c0432997fb06979d65c` |
| `pipes/COIL/20261109-SAT-maintenance-advisory.md` | `55ec0db9b3d9979fcb28ff4fe980955f666bf95681fad004d02c92146016c8ed` |

**Adoption scope (PI, 2026-11-09):** all files listed above as they stand at the content commit, plus everything inherited unchanged from `coil-v0.3`; tag `coil-v0.4`; no exclusions. What is adopted is the recorded current state of the study — its grades, assumptions, negative results, retractions and OPEN items as written; not a physical validation, a cross-layer equivalence or a transfer to RTG. PR #9 is outside this release.
