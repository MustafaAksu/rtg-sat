# HCG — charter

**Study:** Hodge Conjecture study (RTG Complex Geometry and Hodge Realization). **Key:** `hcg`. **Tags:** `hcg-v<version>`. **Inbox:** `pipes/HCG/`.

**Owners:** the Claude and ChatGPT sessions of the HCG conversation. **PI:** Mustafa Aksu, who decides adoption.

**Status of this file:** adopted by the PI on 10 Nov 2026 as the governance document of `hcg-v0.2` (`records/hcg/HCG_v0.2_RELEASE_RECORD.md`); updated for `hcg-v0.3` and `hcg-v0.4` in the edition table, the content table, the pending list and the RTG pins only (`records/hcg/HCG_v0.3_RELEASE_RECORD.md` §6, `records/hcg/HCG_v0.4_RELEASE_RECORD.md` §6). It carries no scientific claim. **Governing edition:** `hcg-v0.4`.

## 0. Scope guard

> HCG makes no claim that the Hodge conjecture or Severn's claim is proved or refuted.

This sentence applies to every HCG document and to every publication-facing text written by the HCG owners or the PI about HCG. HCG does not govern third-party texts.
- B. Severn's results (`hexagon:2610.00386`, `hexagon:2610.00387`) are **CLAIMED**.
- Checking one link of Severn's argument, or rebuilding one certificate, is not a verification of the whole claim.

HCG is a satellite study (`rtg-sat/REGISTRY.md`). It is not an RTG stream, and nothing in it is an RTG result.

## 1. What HCG studies

HCG asks whether a mathematically precise choice of complex structure, lattice, polarization or Weil-type signature, suggested by RTG's Eisenstein arithmetic, leads to useful geometric constructions. Its work so far:

| Line | Content |
|---|---|
| H1, H2 | The Eisenstein elliptic curve E = ℂ/ℤ[ζ₆], its powers, and their integral Hodge rings. A calibration on known cases. |
| NF, R6, R7 | Normal-form and centralizer checks of the imported dyadic map. |
| H3 | An audit of Severn's claim on Weil classes for ℚ(√−3) sixfolds: proof obligations PO-1–PO-6, the G₃₄ datum and its boundary witnesses W5–W7, and the links to Severn's deposited data. |
| H4 | The selection theory for the boundary condition (H4): edge forms, rank obstructions, braid escapes. |
| H3, since `hcg-v0.3` | The third-family round 2, the Severn v2 successor audit (Theorem A/B chain), and the boundary-rank and dimension-budget bounds (Δ24–Δ26). |
| H3, since `hcg-v0.4` | Two results of Δ27: the local determinant formula for genus-zero parabolic cup forms and the induced period bound (ledger §6.24). |
| Pending | The rest of Δ27 (nonsplit Weil eightfolds), the HHO opening, and the all-powers question (Δ28, Δ29). |

The study's statements, grades and open items are in the study ledger, not in this charter.

## 2. Documents and layout

| What | Where |
|---|---|
| Study ledger (the claims, their grades and review states, safeguards, open items, imports, retired claims) | `hcg/HCG_STUDY_LEDGER.md` |
| This charter | `hcg/HCG_CHARTER.md` |
| Source manifest, source dictionary, pre-intake source inventory, release records, reviews | `records/hcg/` |
| Scripts, certificates, outputs, frozen historical files | `evidence/hcg/` |
| Original files as uploaded | `upload/hcg/` (unchanged; see its `README.md` and `SHA256SUMS`) |

**Layout:** session ledger (`REGISTRY.md`). The ledger is one file with a fixed name. Earlier editions and the pending-delta logs are frozen files; they are not live text.

**The ledger carries the claim register.** A separate claim-register file is not kept.
- Load-bearing claims carry an `HCG-…` RID in §6 of the ledger.
- Open items carry their `HCG-OPEN-…` RIDs in §2.
- Retired and rejected claims are in Appendix B.
- A few interpretive `[HEUR]` blocks in §6 have no RID. They are commentary, not registered claims.

## 3. Editions

| Edition | Adoption | Identity |
|---|---|---|
| Session ledger v0.1 | PI, chat level, 22 Oct 2026 | SHA-256 `75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7` |
| Session ledger v0.2 | PI, chat level, 26 Oct 2026 (scoped) | SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` |
| `hcg-v0.2` (first repository edition) | PI, 10 Nov 2026; release record `records/hcg/HCG_v0.2_RELEASE_RECORD.md`; published by the annotated tag | the ledger at that tag is byte-identical to the chat-adopted v0.2 (PI decision 1 of 10 Nov 2026, recorded in `upload/hcg/README.md`); frozen copy in `evidence/hcg/ledger-history/adopted_v0_2/` |
| `hcg-v0.3` | PI, 11 Nov 2026 (scoped); release record `records/hcg/HCG_v0.3_RELEASE_RECORD.md`; published by the annotated tag | the ledger at that tag, SHA-256 `fc03e8376eb56c14abeae77c7f20c2fa70723977572744af8a0c4a38dcec814d`: v0.2 with Δ24–Δ26 and the RTG import review |
| `hcg-v0.4` | PI, 11 Nov 2026 (scoped); release record `records/hcg/HCG_v0.4_RELEASE_RECORD.md`; published by the annotated tag | `hcg/HCG_STUDY_LEDGER.md`, SHA-256 `51487f925e34f01e0d233d1ff909e29357d3eadbf1b839f79f73e8fe84022949`: v0.3 with two results of Δ27 (§6.24) |

**What an adoption covers.** The v0.2 and v0.3 adoptions each adopted the consolidated record as the governing record. Neither made any claim `ACCEPTED`: every claim keeps its own review state.

**Pending, not part of `hcg-v0.4`:** Δ27 except its two results in ledger §6.24, Δ28 and Δ29, in `HCG_DSN_v0_3_PENDING_DELTAS.md` (frozen original in `upload/hcg/`). They enter a later edition only through review and a PI decision.

**Reading the v0.2 ledger (tag `hcg-v0.2`).** That ledger is kept byte-exact, so some of its lines are historical; v0.3 updated them:
- its "INTERNAL" distribution line and safeguard SG-10 (the blindness rule) describe the state of 26 Oct 2026; the PI lifted that guard for publication on 10 Nov 2026;
- its file paths and its "session-local" wording refer to the session's storage;
- its RTG pins are historical citations (§5).

A release record lists these points. The ledger text itself is changed only in a later edition.

## 4. Grades and review states

HCG keeps two separate axes. Both are defined in the ledger's header and are restated here.

**Evidence grades (claim tags).** The DSN Methodology tags as used in the ledger: `[THM]`, `[ALG]`, `[DEF]`, `[COR]`, `[RESULT]`, `[HEUR]`, `[HYP]`, `[OPEN]`, and for retired claims `[RETRACTED]`, `[REFUTED]`, `[FAIL]`, `[SUPERSEDED]`. The ledger adds three local aliases:

| Alias | Meaning |
|---|---|
| `[MATH]` | a classical published theorem used as input; not a session result |
| `[EXT-CLAIM]` | a theorem asserted in an unrefereed external manuscript, recorded at the audit grade the session reached |
| `[ALG cert]` | an exact finite computation on one named certificate; no generalisation implied |

An imported theorem from an unrefereed source keeps that scope in its tag line.

**Review states (`[provenance: …]`).**

| State | Meaning |
|---|---|
| `PROPOSED` | one AI has derived the claim |
| `CHECKED` | an independent check by a second AI is recorded |
| `THIRD-FAMILY CHECKED` | a reviewer outside the Claude and OpenAI model families has independently checked the claim |
| `ACCEPTED` | a PI decision |

A review state is not a proof grade and does not upgrade a claim tag. Agreement among AIs is not human refereeing. The third-family auditor is a reviewer, not an owner.

**Negative results** — refutations, retractions, failed routes and counterexamples — are kept with the same care as positive ones and are never dropped.

**RIDs.** `HCG-<KIND>-<NAME>`. The namespace is HCG's own; it is not an RTG namespace. Historical aliases stay as written. A withdrawn RID is not reused.

## 5. Interfaces

**RTG (one way in).** HCG imports a small set of mathematical facts from RTG (ledger §7: the matrices A and B, J_Q, the normal-form coefficients, the smooth embedding, the attractor statement, the programme boundary). RTG grades travel unchanged, and an import is mathematical reuse only (ledger SG-1, SG-2).
- The v0.2 ledger cites DYAD v6.4.18/19, GENESIS v2.8.9, Programme v1.2 and OFN v0.10.
- The corresponding `rtg-corpus` tags are `dyad-v6.4.19`, `gen-v2.8.9`, `programme-v1.2` and `ofn-v0.10`. There is no tag for DYAD v6.4.18.
- A targeted check on 10 Nov 2026 found the cited RIDs and the J_Q statement at those tags, and the DSN file at `dyad-v6.4.19` has the SHA-256 recorded in the HCG charter of 21 Oct 2026 (`40c9e63f…`).
- The grades at each RID have not been re-read, and `rtg-corpus` has moved on since. For `hcg-v0.2` the pins were therefore not set (PI decision 6 of 10 Nov 2026).
- **Since `hcg-v0.3` the pins are `dyad-v6.4.23`, `gen-v2.10` and `programme-v1.4`** (approved by the PI on 11 Nov 2026), after the review in `records/hcg/HCG_RTG_IMPORT_AUDIT_20261110.md`. There is no OFN pin. `hcg-v0.4` keeps these pins unchanged (PI, 11 Nov 2026). A later RTG edition is consumed only by a new HCG decision.

**RTG (back).** Nothing in HCG is an RTG result. A finding goes to RTG only as a pipe item in `rtg-corpus`, with the PI's disclosure check (`CONVENTIONS.md` §4).

**HHO.** The Hurwitz–Hodge Obstruction study was opened inside the HCG conversation on 3 Nov 2026 and is a separate study with its own owners.
- HHO-track files made in the HCG conversation are kept here as dated source evidence. Their scientific custody is with HHO.
- HHO uses HCG inputs as received, hash-pinned files until an `hcg-v*` tag exists, and re-pins by its own decision afterwards.
- An HHO result enters HCG only with all three of: an explicit disposition by the HCG owners, PI adoption, and an HCG release that records the import. Shared storage transfers nothing.

**Symbol warning.** "(H)" in the HHO opening note and "(H0)–(H4)" in the HCG ledger are different objects. See `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md`.

**LIT and third-party sources.** Third-party texts and data are not stored in `rtg-sat`. They are cited by identifier and version, with the SHA-256 of a held copy, and are handled through LIT and its methodology (PI decision 3 of 10 Nov 2026). No LIT-backed validation is claimed until a LIT report of use exists.

## 6. Working rules

- Original files are never rewritten. Corrections are dated additions, and a new edition is a new release.
- Each owner session pushes only to its own prefix (`claude/hcg-*`, `chatgpt/hcg-*`). The PI merges. Tags are created by the PI or under `CONVENTIONS.md` §2.1.
- A release needs: the owners' files, the other owner's review, a release record with the SHA-256 of every adopted file, and the PI's adoption.
- No hash, approval, RID or file content is invented. A source that is not held is written "not available".
- Before any novelty claim, a bounded prior-art check is requested through LIT. The edge-flux theorem's novelty is already limited by the prior art of Alexeev–Donagi–Farkas–Izadi–Ortega (ledger §6.18 and Δ7); that limit stays.
