# HCG v0.6 — release record

**Status:** **ADOPTED** by PI Mustafa Aksu on 16 November 2026, 09:36 +03:00 (§8). Publication tag: `hcg-v0.6`, created by the PI on the merge commit of the pull request that carries this record (PR #72).

**Release:** fifth repository edition of the HCG study. It is the ledger of `hcg-v0.5` with two line-by-line reviews of Severn v2 recorded as §6.26, two OPEN items closed in their scopes, one new OPEN item and one scope guard. Nothing else of v0.5 changes.

**Prepared by:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Adoption:** PI Mustafa Aksu.

## 1. What this release is

- **Scoped adoption.** The consolidated record is adopted as the governing record. No individual claim becomes ACCEPTED; every claim keeps its own review state.
- **Scope guard.** HCG makes no claim that the Hodge conjecture or Severn's claim is proved or refuted. Severn's Theorem 6.2 (`hexagon:2610.00387v1`) and Theorems A, B, C of `hexagon:2610.00387v2` stay CLAIMED.
- **What the new section says.** (a) The every-member scope of Severn's Theorem 6.2 and the compensation step are correct as written in v2, given the premises they cite. (b) If the Weil classes of a Weil-type abelian variety A are algebraic and Hg(A) = SU_H, every Hodge class on every power of A is algebraic (v2 Theorem 11.2); hence Theorem C follows from Theorem B under that condition. (c) A scope table of what the chain would give for the Hodge conjecture **if** Theorems A and B hold.
- **What it does not say.** It does not establish Theorems A, B or C, conditions (L) and (D), or the discriminant of the component. It does not say that the Hodge conjecture holds for the special members of these families, nor for abelian sixfolds in general. v2 §12 (type III) is not reviewed.
- **AI review is not refereeing.** Each review was made by the Claude session and repeated against the same PDF by the ChatGPT session. No third model family and no human has read v2 (PI standing decision, §8). The standard results cited by the reviewed sections were not re-read.

## 2. Changes from `hcg-v0.5`

| Item | v0.5 | v0.6 |
|---|---|---|
| OPEN 8 `HCG-OPEN-PO1-PREMISE` | PARTIAL | CLOSED in its scope (PI decision of 13 Nov 2026) |
| OPEN 10 `HCG-OPEN-SEVERN-V2-C` | ACTIVE (v2 §11 and §12) | CLOSED in its scope: v2 §11 only (PI, with this adoption) |
| OPEN 12 `HCG-OPEN-SEVERN-V2-TYPE3` | — | new, ACTIVE: v2 §12; blocked on Abdulali's paper (through LIT) |
| §6.26 (a): gates A–D (v2 Lemma 6.1, Thm 6.2 with Cor. 4.7, Lemma 2.2, Lemma 10.1 / Prop. 10.2) | — | CHECKED (two AIs), line by line against v2 |
| §6.26 (b): `HCG-THM-SEVERN-V2-L111` (v2 Lemma 11.1), `HCG-THM-SEVERN-V2-T112` (v2 Theorem 11.2) | — | new; `[THM]` with `[import:]` and `[assuming:]`; CHECKED (two AIs) |
| §6.26 (c): scope table | — | new; a scope statement, not a result |
| SG-14 | — | new guard: "Weil classes algebraic" is not "the Hodge conjecture"; the passage needs Hg(A) = SU_H or dimension ≤ 5 |

Also changed: §1.6 (index); in §5 the PO-1 and Severn v2 rows and two new rows; the PO-1 row of the §6.7 matrix; one sentence each in §6.8, §6.20, §6.22; notes in §6.8 and §6.10; one limit in §6.21; import lines in §7 (Kraft–Procesi, van Geemen, Voisin: not re-read; Abdulali: not held); artefact lines in §8; the PI row and corrections D-27, D-28 in §9; the status summary; Appendix A.

Three RID labels are new: `HCG-THM-SEVERN-V2-L111`, `HCG-THM-SEVERN-V2-T112`, `HCG-OPEN-SEVERN-V2-TYPE3` (and the artefact RIDs `HCG-ART-V06-REVIEW`, `HCG-ART-V2-EX122`).

Every other statement, grade, review state and scope guard of `hcg-v0.5`, and OPEN 1–7, 9, 11, are unchanged.

## 3. Identity of the adopted scientific record

| Item | Value |
|---|---|
| File | `hcg/HCG_STUDY_LEDGER.md` |
| SHA-256 | `b1e928f5ae555d688a18bb1046be7626796f2a07935b6ff81a0fc934036b14cb` |
| Adopted text | DRAFT r2, SHA-256 `05e2de260d535a10424a536f341f0517aa4d04bc1dca547b83c3506c12b7e513`, at commit `ed0b732632390372afb58d48a269b1240d59c895` of PR #72 |
| Build | `evidence/hcg/verification/make_v06_draft.py`: 37 assertion-gated edits (30 string anchors, 7 line-prefix anchors) of the ledger at tag `hcg-v0.5` (SHA-256 `650c301f8465536705c852113fa7c2e2288d8c3e3cae99fa92a9c466e47bf383`) |
| Release transform | `evidence/hcg/verification/release_v06.py`: rebuilds DRAFT r2, checks its hash, applies 15 edits of labels and metadata only |
| Previous edition | `hcg-v0.5` (`records/hcg/HCG_v0.5_RELEASE_RECORD.md`) |

**What the release transform changes.** Title, date, status, build line, "draft" and "proposed" in headings and labels, the three places where the closure of OPEN 10 for v2 §11 was written as taking effect with the adoption (now dated 16 Nov 2026), the PI role line, the version-history heading with the adoption entry, and the footer. No statement, grade, review state, scope guard or OPEN item otherwise differs from DRAFT r2.

## 4. RTG inputs (unchanged)

**`dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4`** in `rtg-corpus`; no OFN pin. Kept as in v0.3–v0.5 (§8). The new section uses no RTG input. Nothing in HCG is an RTG result.

## 5. Not part of this release

- **v2 §12** (type III; Corollary 12.1 through Abdulali's theorem): OPEN 12. Only its first three steps and the arithmetic of Example 12.2 were read.
- **The premises of the chain:** (L) and the supply of cycles (PO-2, PO-4), (D) on S_W5 (PO-5), the discriminant and the polarization comparison (PO-6; HHO's bridge B2). OPEN 6 (human referee).
- **The standard results** cited by the reviewed sections (relative Hilbert schemes and flat classes; the moduli space and its universal family; Landherr; the first fundamental theorem for SL_n; the Hodge group of the very general member): not re-read by anyone.
- **The rest of Δ27, Δ28 and Δ29:** pending in `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`.
- **HHO.** No HHO claim is an HCG result. HHO's pin of HCG does not change with this release; HHO re-pins only by its own decision.
- Third-party texts, which are not stored in this repository. No text of Severn's is copied; statements are cited by number.

## 6. Other files changed by this release

| File | Change |
|---|---|
| `hcg/HCG_CHARTER.md` | Status line; the edition table (row for `hcg-v0.6`); the content table (row for §6.26); the pending list; the sentences on adoptions and on the RTG pins. No rule of the charter changes. |
| `REGISTRY.md` | `hcg` row: governing edition `hcg-v0.6`; RTG inputs unchanged. |
| `evidence/hcg/README.md` | The column header names the current edition. |
| `evidence/hcg/verification/` | New: `make_v06_draft.py`, `release_v06.py`. `severn_v2_example_12_2_check.py` and its output are already on `main` (PR #67). |
| The three review records in `records/hcg/` | Already on `main` (PRs #61, #67, merged as proposal records). They are the review basis and are not changed here. |

No frozen source file in `evidence/hcg/` or `upload/hcg/` is changed.

## 7. Checks

| Check | Result | By |
|---|---|---|
| Builder: every anchor unique in v0.5; untouched text byte-identical | 37/37 | Claude (script); ChatGPT (independent re-application, PR #72) |
| DRAFT r1 (`0f88e86d…5bdc7374e`) | ACCEPT WITH CHANGE: two current-state sentences (OPEN 8 summary; §5 "Theorem C audited") | ChatGPT (PR #72 review `5906916164`) |
| DRAFT r2 (`05e2de26…12b7e513`): both corrections, one further current-state sentence (§6.8 v0.2 note), OPEN 10's old criterion marked | ACCEPT SCOPED; byte-identical rebuild; builder hash checked | ChatGPT (PR #72 review `5906989472`) |
| Release transform reproduces DRAFT r2 and changes labels and metadata only | pass | Claude |
| OPEN 8 line review, revision 3 (`56d9053f…60cada57`): gates A–D | PASS, two sessions against the v2 PDF | Claude; ChatGPT (PR #61) |
| Hodge scope note, revision 2 (`088abefd…1a7baf715`) | ACCEPT SCOPED, one wording correction (D-28) | ChatGPT (PR #61) |
| OPEN 10 review, revision 2 (`8b23528d…db6a3e38`): Lemma 11.1 L1–L9, Theorem 11.2 T1–T7, Theorem C deduction | PASS, two sessions against the v2 PDF; two wording corrections (D-27) | Claude; ChatGPT (PR #67) |
| Example 12.2 arithmetic (`severn_v2_example_12_2_check.py`) | exact; classes [−5], [−11] | Claude (script) |
| New proofs or computation campaigns for this release | **none** | — |

## 8. Decisions

| Decision | By | Entry |
|---|---|---|
| Review ceiling: CHECKED (two AIs); no third-family reading for now | PI, 11 Nov 2026, 18:18 +03:00 (standing) | "“CHECKED kalsın, üçüncü denetçi şimdilik yok” aksi PI tarafından bildirilene kadar geçerli." |
| OPEN 8 closed in its scope | PI, 13 Nov 2026 (recorded on PR #61, comment `6848035948`) | "PR61 i birleştirelim OPEN8 i artık kapayalım." |
| Co-owner reviews of DRAFT r1 and r2 | ChatGPT HCG owner session | PR #72 reviews `5906916164` (ACCEPT WITH CHANGE), `5906989472` (ACCEPT SCOPED) |
| Adoption of v0.6 with the scope of §§1–5, including the closure of OPEN 10 for v2 §11 and OPEN 12 | PI, 16 Nov 2026, 09:36 +03:00 | "benimsiyorum." — in reply to: adoption of DRAFT r2 (SHA-256 `05e2de26…12b7e513`) as `hcg-v0.6`, scoped; the adoption covers the split of OPEN 10; no claim ACCEPTED |
| RTG pins and publication | PI, standing practice (12 Nov 2026, 14:58 +03:00: "Kendimizi tekrar ediyoruz. Aşağıdaki kararları defaten ilettim.") | `dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4` unchanged, no OFN pin; the PI creates the annotated tag `hcg-v0.6` and the owner session supplies the command |

Order: decision → release record → merge → tag (`CONVENTIONS.md` §2).

## 9. Adoption manifest

(Added in the manifest-only commit that follows the content commit.)
