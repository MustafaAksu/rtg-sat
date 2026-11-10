# HCG v0.2 — release record (DRAFT)

**Status:** **DRAFT — not adopted.** This record becomes the release record of `hcg-v0.2` only when the PI's adoption is entered in §8. Until then there is no HCG edition in this repository.

**Release:** first repository edition of the HCG study. It publishes the session ledger v0.2 that the PI adopted at chat level on 26 October 2026, **byte-exact** (PI decision of 10 Nov 2026, "A": Option A of `records/hcg/HCG_MIGRATION_NOTE.md` §6).

**Prepared by:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Adoption:** PI Mustafa Aksu.

## 1. What this release is

- The scientific content of `hcg-v0.2` is exactly the chat-adopted ledger v0.2. No statement, grade, review state, scope guard, OPEN item or retired claim is added, removed or changed.
- The release adds the repository frame around it: a charter, the source manifest, the source dictionary and the frozen evidence.
- **Scope guard.** HCG makes no claim that the Hodge conjecture or Severn's claim is proved or refuted. Severn's Theorem 6.2 (`hexagon:2610.00387v1`) stays CLAIMED.

## 2. Identity of the adopted scientific record

| Item | Value |
|---|---|
| File | `hcg/HCG_STUDY_LEDGER.md` |
| SHA-256 | `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` |
| Git blob | `d66c9b65b047dd9f52c8b25e03e2650649641876` |
| Identical to | `upload/hcg/owner-session-outputs/claude/g34/dsn/adopted_v0_2/HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` and `evidence/hcg/ledger-history/adopted_v0_2/HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` |
| Chat-level adoption | PI, 26 Oct 2026, 22:44 +03:00: "Evet v0.2 yi ben de benimsiyorum(PI:Mustafa)" |
| Chat-level release record | `evidence/hcg/ledger-history/adopted_v0_2/HCG_HODGE_SESSION_DSN_v0_2_RELEASE_RECORD.md` (`967732cd1ea3bce0f0aa5083d6947761791f7bfe44ee4d5a7af302b3a29e1244`), with addendum 1 (`f16b5bed75a8c838977a32170b6fd73757a32775837c7de0adeb005e0a2087ff`) |
| Previous edition | v0.1, chat-adopted 22 Oct 2026 (`75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7`), frozen in `evidence/hcg/ledger-history/adopted/` |

**Scope of the chat-level adoption, carried over unchanged** (from the chat-level release record §2):

| Item | State |
|---|---|
| The v0.2 consolidation of the session's scientific record | ADOPTED (scoped) |
| Individual claim review states | Unchanged. No row became ACCEPTED through the adoption. |
| Severn Thm 6.2 | CLAIMED; not ESTABLISHED |
| PO-1–PO-4 | INTERNAL CHECKED; third-family Priority B pending |
| PO-5 ((D) on S_W5); PO-6 on W5 | THIRD-FAMILY CHECKED |
| OPEN 8 (proof validation of the every-member scope); the general [19, Lemma 6.2] (OPEN 5); human referee (OPEN 6) | OPEN |

Adopting `hcg-v0.2` in this repository repeats that scope. It does not upgrade any row.

## 3. Lines of the ledger that are historical

The ledger is published byte-exact, so the following lines describe 26 October 2026 and are not edited. The charter (`hcg/HCG_CHARTER.md` §3) tells the reader the same.

| # | Ledger text | Current reading |
|---|---|---|
| H1 | Line 25, "Distribution guard: INTERNAL … must not be sent to the third-family auditor"; SG-10 (line 253), the blindness rule | Lifted for publication by the PI on 10 Nov 2026 ("Gizliliği kaldırabiliriz."). The auditor completed round 2 on 27 Oct 2026; that is recorded in Δ24, which is pending. |
| H2 | "ACCEPTED: a PI decision. None has been made yet." | Still true: no claim row is ACCEPTED. |
| H3 | Line 45, the `HCG-…` RID namespace is "session-local" | The namespace is now HCG's own in `rtg-sat` (charter §4). No RID changes. |
| H4 | "DSN Methodology: DSN_METHODOLOGY_v1.3" | The ledger was written under v1.3. `rtg-sat` reads its base rules at `methodology-v1.4`. The ledger's tags are not re-graded here. |
| H5 | Companion documents and §8 artifact registry name session files | The files are frozen in `evidence/hcg/`. Names are resolved through `PLACEMENT_MAP.tsv` and `NAME_ALIASES.tsv`. The session's own charter v0.2 (`evidence/hcg/session-start/`) is a historical companion; the repository charter is `hcg/HCG_CHARTER.md`. |
| H6 | §7, the RTG import pins | See §4. |
| H7 | References to Severn's deposited files (`braid.txt`, `tuple_pairs_D3.json`, the certificates ZIP) | Third-party data, not stored in `rtg-sat`; cited by hash in the source manifest §3 and handled through LIT. |

The ledger also uses "INTERNAL CHECKED" in its status summary for "checked by both Claude and ChatGPT". That is review vocabulary, not a distribution label.

## 4. RTG source references (historical; not registry pins)

The ledger §7 cites RTG owner documents by version. The table gives the `rtg-corpus` tag that carries each version.

| Ledger citation | `rtg-corpus` tag | Status of the reference |
|---|---|---|
| DYAD v6.4.18 (R1, R2, R4, R5) | none; v6.4.18 was not tagged | historical |
| DYAD v6.4.19 (R6(a); synchronization receipt) | `dyad-v6.4.19` | historical. The DSN file at this tag has SHA-256 `40c9e63f…`, equal to the receipt in the session charter of 21 Oct 2026. |
| GENESIS v2.8.9 (R1, R3) | `gen-v2.8.9` | historical |
| Programme v1.2 (SG-PROG-1) | `programme-v1.2` | historical |
| OFN v0.10 | `ofn-v0.10` | historical |

- A targeted check on 10 Nov 2026 found the cited RIDs (`DYAD-ALG-Q-INVARIANT-FORM`, `DYAD-THM-C21`, `DYAD-ALG-NF6`, `DYAD-THM-SMOOTH-EMBEDDING`, `DYAD-THM-PRIM-CTR`) at `dyad-v6.4.19`, the J_Q statement in `gen-v2.8.9` §6.6, and SG-PROG-1 in `programme-v1.2`.
- The grades and hypotheses at those RIDs were **not** re-read.
- These are therefore historical source references, not verified consumption pins in the sense of `CONVENTIONS.md` §3. In `REGISTRY.md` the "RTG inputs (pinned tags)" field stays **`not set`**.
- The RID, grade and hypothesis reconciliation is left to a later scientific edition or a separate maintenance review (PI decision 6 of 10 Nov 2026; co-owner review of PR #23).

## 5. Not part of this release

- **Δ24–Δ29** (`evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`, `1f00a1eb…`), with the Δ27 addenda 1–17. They are pending. Their evidence folders are placed and marked pending in `evidence/hcg/README.md`.
- **HHO.** The HHO-track files are kept as dated source evidence. No HHO claim is an HCG result, and scientific custody is with HHO.
- **Third-party texts and data**, and the three received packages that contain Severn deposit data (source manifest §3).
- **ChatGPT's own originals**, not yet uploaded. Their absence does not affect the identity of the adopted ledger.
- Any LIT-backed validation. None is claimed.

## 6. Checks

| Check | Result | By |
|---|---|---|
| Ledger bytes equal the chat-adopted v0.2 (SHA-256 and Git blob) | pass | Claude; ChatGPT (reviews of PR #21 and PR #23) |
| `upload/hcg/SHA256SUMS`, 754 files | 754/754 | Claude (before the push; on `main` after the merges) |
| `evidence/hcg/SHA256SUMS`, 754 files; path and hash mapping to `upload/hcg/` | 754/754 | Claude (full re-hash); ChatGPT (manifest consistency 754/754, aliases 44/44, 5 Git blobs) |
| Every file name cited in the ledger resolves to a placed file, an alias or a bundle member, except the three Severn deposit files | pass | Claude |
| Dictionary quotations found in the cited originals | pass | Claude; ChatGPT (targeted) |
| Scientific computations re-run for this release | **none** | — |

The release transform of 26 Oct 2026 (`release_v0_2.py`) and its reverse check are part of the chat-level record. They were not re-run here.

## 7. Adoption manifest (candidate)

SHA-256 of the bytes at the commit that carries this draft. If any listed file changes before adoption, the hashes are recomputed and this table is updated before the tag.

| File | Role | SHA-256 |
|---|---|---|
| `hcg/HCG_STUDY_LEDGER.md` | the adopted scientific record | `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` |
| `hcg/HCG_CHARTER.md` | charter (governance text; no scientific claim) | filled at the publication step (§9) |
| `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md` | source dictionary | `7d2736efc9f49db336ef6279f7a9bd65f7071bd584e149fa08e145989d8f4419` |
| `records/hcg/HCG_SOURCE_MANIFEST.md` | source manifest | `13d9742db396d176f6be0704dda28ae18a5b95655ecee5f7d9e5526013f0073b` |
| `evidence/hcg/SHA256SUMS` | index of the 754 frozen files | `5950c6c8d1c8ebc22ee904211aecbeb8456f17ac87cb0b96532276d84d260fe3` |
| `upload/hcg/SHA256SUMS` | index of the 754 uploaded originals | `bb66145e754cb949246d9da578b4891f5ab18358212f414f79b7315ccaadb4fa` |
| `REGISTRY.md` | governing-edition field of the `hcg` row | filled at the publication step (§9) |

The frozen files are adopted as **evidence as it stands**, not as claims. A frozen file that belongs to pending material stays pending.

## 8. Decisions

| Decision | By | Entry |
|---|---|---|
| Co-owner review of this record | ChatGPT HCG owner session | *(blank)* |
| Adoption of `hcg-v0.2` with the scope of §§1–5 | PI | *(blank)* |
| Publication: tag created by the PI, or by a single-use workflow under `CONVENTIONS.md` §2.1 | PI | *(blank)* |

## 9. Publication step (to be applied only after the PI's adoption)

1. `hcg/HCG_CHARTER.md`: the status line and the `hcg-v0.2` row of §3 change from "DRAFT / not yet adopted" to the adoption entry. No other text changes.
2. `REGISTRY.md`, `hcg` row:
   - governing edition becomes `hcg-v0.2` with this record;
   - layout names `hcg/HCG_STUDY_LEDGER.md`;
   - RTG inputs stay `not set`;
   - the transfer rule records that HHO → HCG needs an HCG owner disposition, PI adoption and an HCG release.
3. This record: status and §8 filled; §7 completed with the two hashes above; "DRAFT" removed from the title.
4. Hashes of every changed file are recomputed after the step and before the tag. Order: decision → release record → merge → tag (`CONVENTIONS.md` §2).
