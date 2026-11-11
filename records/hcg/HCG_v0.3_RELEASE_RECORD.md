# HCG v0.3 — release record

**Status:** **ADOPTED** by PI Mustafa Aksu on 11 November 2026, 08:54 +03:00 (§8). Publication tag: `hcg-v0.3`, created by the PI on the merge commit of the pull request that carries this record (PR #31).

**Release:** second repository edition of the HCG study. It is the ledger of `hcg-v0.2` with the changes of Δ24–Δ26 and the review of the RTG imports.

**Prepared by:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Adoption:** PI Mustafa Aksu.

## 1. What this release is

- **Scoped adoption.** The consolidated record is adopted as the governing record. No individual claim becomes ACCEPTED; every claim keeps its own review state.
- **Scope guard.** HCG makes no claim that the Hodge conjecture or Severn's claim is proved or refuted. Severn's Theorem 6.2 (`hexagon:2610.00387v1`) and Theorems A, B, C of `hexagon:2610.00387v2` stay CLAIMED.
- **AI review is not refereeing.** Every check in this edition was made by AI sessions (two families, and a third family for the auditor rounds). No human referee has reviewed the chain.

## 2. Changes from `hcg-v0.2`

The index is §1.3 of the ledger. In short:

| Item | State in `hcg-v0.3` |
|---|---|
| PO-1–PO-4 | THIRD-FAMILY CHECKED at theorem level, each under its conditions, **on the v1 and [386] texts** (auditor round 2). The auditor's summary stays beside it: "Public global statement: NOT VERIFIED as independently established theorem." |
| Severn v2 | Not read by the third family. v2 locations are cited through a two-AI crosswalk only (guard SG-13). |
| `HCG-ALG-E02` | CHECKED as a whole; the W5 sub-claim alone is THIRD-FAMILY CHECKED. |
| `HCG-EXT-PO6`, general statement | CHECKED (two AIs) as a proof-path review only. |
| OPEN 1, OPEN 3, OPEN 5 | CLOSED in their stated scopes. |
| OPEN 8 | **PARTIAL** (PI decision, 10 Nov 2026). |
| OPEN 9, `HCG-OPEN-SEVERN-V2` | CLOSED for the Theorem A/B chain only (PI decision, 10 Nov 2026). |
| OPEN 10, `HCG-OPEN-SEVERN-V2-C` | ACTIVE: v2 §11 (Theorem C) and §12 (type III) are not audited. |
| New entries | §6.22: `HCG-THM-SEVERN-V2-L44`, `HCG-THM-SEVERN-V2-L72`, `HCG-ALG-SEVERN-APPXA-REPRO`, `HCG-ALG-LAMINAR-H4-GATE`, the crosswalk. §6.23: `HCG-COR-BOUNDARY-WITT`, `HCG-ALG-DIM-BUDGET`. |
| RTG imports | Cited by tag, section, RID, grade and scope (§4). |

## 3. Identity of the adopted scientific record

| Item | Value |
|---|---|
| File | `hcg/HCG_STUDY_LEDGER.md` |
| SHA-256 | `fc03e8376eb56c14abeae77c7f20c2fa70723977572744af8a0c4a38dcec814d` |
| Reviewed text | DRAFT r2, SHA-256 `23929cceec6e1e9aa5cb4082522cfc04b943824c578cee3a17d23be355aeef2e`, at commit `4c6912f17a276dc1cd035b8dddc056558f6b132a` of PR #31 |
| Build | `evidence/hcg/verification/make_v03_draft.py`: 64 assertion-gated edits of the v0.2 text (SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`) |
| Release transform | `evidence/hcg/verification/release_v03.py`: rebuilds DRAFT r2, checks its hash, applies 19 edits of labels and metadata only |
| Previous edition | `hcg-v0.2` (`records/hcg/HCG_v0.2_RELEASE_RECORD.md`); frozen ledger in `evidence/hcg/ledger-history/adopted_v0_2/` |

**What the release transform changes.** Title, date, status, build line, "draft" and "proposed" in headings and labels, the pin sentence (from "proposed, PI decision pending" to the PI's approval), the PI role line, the version-history heading with the adoption entry, and the footer. No statement, grade, review state, scope guard or OPEN item differs from DRAFT r2.

## 4. RTG inputs (pinned)

Pins of this edition, approved by the PI: **`dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4`** in `rtg-corpus`. There is no OFN pin.

- Basis: `records/hcg/HCG_RTG_IMPORT_AUDIT_20261110.md` (revision 2). The audit compared one selected defining line per import between the historical tags and these tags and found each identical. It did not re-read proofs and did not trace dependencies.
- Exception to "found": the v0.2 ledger named "OFN v0.10" beside the Programme without a section, RID or statement. That is not an auditable import, and OFN is not an import of this edition.
- Only R6(a) (`DYAD-THM-PRIM-CTR`) is taken on RTG's grade, as a premise of `HCG-THM-R6B`. The other imports are recomputed, used as cross-checks, or used as context.
- The citations of v0.2 (DYAD v6.4.18/19, GENESIS v2.8.9, Programme v1.2) stay in the ledger as provenance.
- A later RTG edition is consumed only by a new HCG decision. Nothing in HCG is an RTG result.

## 5. Not part of this release

- **Δ27** (nonsplit eightfolds, with its addenda), **Δ28** (HHO opening) and **Δ29** (positive lane). They stay pending in `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`.
- **HHO.** No HHO claim is an HCG result; scientific custody is with HHO.
- **Third-party texts and data.** Severn's v2 and deposited files are not stored here. §6.22 of the ledger cannot be replayed from this repository alone, and the ledger says so. One ChatGPT bundle is held back because it contains deposit data; two ChatGPT packages were never received by the Claude session.
- **A reported prior preprint** for the boundary-rank conclusion. Its identity is not confirmed and it is not cited.
- Any LIT-backed validation. None is claimed.
- **ChatGPT's own originals**, not yet uploaded.

## 6. Other files changed by this release

| File | Change |
|---|---|
| `hcg/HCG_CHARTER.md` | Status line; the edition table (row for `hcg-v0.3`); the content table (Δ24–Δ26 moved out of "Pending"); the pending list (Δ27–Δ29); the RTG pin bullet. No rule of the charter changes. |
| `REGISTRY.md` | `hcg` row: governing edition `hcg-v0.3`; RTG inputs set to the pins of §4. |
| `evidence/hcg/README.md` | Two folder labels (`severn-v2/`, `research-next/`) from "pending" to "in `hcg-v0.3`". |
| `evidence/hcg/verification/` | New: `make_v03_draft.py`, `release_v03.py`, `severn_printed_relation.py` with its output. |

No frozen source file in `evidence/hcg/` or `upload/hcg/` is changed.

## 7. Checks

| Check | Result | By |
|---|---|---|
| Builder: every anchor occurs exactly once in v0.2; untouched text byte-identical | 64/64 | Claude (script); ChatGPT (independent reimplementation, byte-identical output) |
| DRAFT r2 hash | `23929cce…5aeef2e` | Claude; ChatGPT |
| Relation among Severn's printed blocks: rank 16, one relation 2X₅ − 4X₇ + X₈ = 0 | pass | ChatGPT (found the error of r1 and the relation); Claude (`severn_printed_relation.py`). The check reads the transcription in `reconstruct_severn_printed.py`, not Severn's PDF or deposit. |
| Δ24–Δ26 acceptance matrix, revision 3 (`30a80660…`) | ACCEPT | ChatGPT (PR #27) |
| RTG import audit, revision 2 (`f99d5439…`) | ACCEPT | ChatGPT (PR #29) |
| Release transform reproduces DRAFT r2 and changes labels and metadata only | pass | Claude |
| Scientific campaigns re-run for this release (84 suppliers, 272 blocks, auditor bundle) | **none** | — |

**Error corrected during review.** DRAFT r1 stated the relation X₁₇ = X₉ + X₁₀ for Severn's printed tree. That was the W5-tree relation copied to a different tree and indexing, and it is false there. It was found by the ChatGPT review and never entered an adopted edition.

## 8. Decisions

| Decision | By | Entry |
|---|---|---|
| OPEN 8 stays PARTIAL; `HCG-OPEN-SEVERN-V2` closed in its verified scope | PI, 10 Nov 2026, 18:04 +03:00 | "Karar 1 Partial kalsın Karar 2 kapatılabilir." |
| Co-owner review of DRAFT r1 | ChatGPT HCG owner session | PR #31 review `5848716444`: CHANGES REQUIRED (S1, E1, S2, E2 and two editorial points). All applied in commit `4c6912f`. |
| Co-owner review of DRAFT r2 | ChatGPT HCG owner session | PR #31 review `5854330360`: ACCEPT SCOPED. |
| Adoption of v0.3 with the scope of §§1–5 | PI, 11 Nov 2026, 08:54 +03:00 | "1 Kabul ettim" — in reply to: adoption of DRAFT r2 (SHA-256 `23929cce…5aeef2e`) as v0.3, scoped. |
| RTG pins | PI, same message | "2 Onaylıyorum" — in reply to: `dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4`, no OFN pin. |
| Publication | PI, same message | "3 Tagi atarım sorun yok" — the PI creates the annotated tag `hcg-v0.3`; the owner session supplies the command. |

Order: decision → release record → merge → tag (`CONVENTIONS.md` §2).
