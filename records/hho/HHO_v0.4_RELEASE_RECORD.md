# HHO v0.4 — release record

**Status:** **DRAFT.** Not adopted. It becomes the record of `hho-v0.4` only after the co-owner's review, the PI's adoption decision and the publication commit (§9).

**Release:** fourth repository edition of the HHO study. If adopted, it supersedes `hho-v0.3` as the governing edition.

**Prepared by:** the Claude HHO owner session, on the recommendation of both owner sessions (Claude, 13 Nov 2026; ChatGPT, relayed by the PI on 14 Nov 2026) that the session results on `main` be fixed in a register edition before the work on (D) starts. **Review:** the ChatGPT HHO owner session. **Adoption:** PI Mustafa Aksu. *No PI decision to prepare or to adopt this edition is recorded yet; this draft commits the PI to nothing.*

## 1. What this release is

`hho-v0.4` is a **register edition**. It records, as register rows, results that are already on `main` as reviewed session records: the conditional bridge B2 to Severn's polarized factor, and the description of the parity at inert primes of positive defect by the sector module of the integral cup lattice.

- **No claim row becomes ACCEPTED.** No row that existed in `hho-v0.3` is regraded or promoted (checked by script, §8).
- Ten claim rows and two open items are added (§3). No new computation was run for this edition.
- The pin of HCG stays at `hcg-v0.2` (§4.1).

**Scope guard.** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist, and no statement about the Hodge conjecture. Severn's results stay CLAIMED. A failed gate excludes a datum or a class of data and nothing more. The rows of B.7 describe a parity; they do not obstruct it, and they say nothing about (D).

## 2. Files of this edition

| File | Role | Change since `hho-v0.3` |
|---|---|---|
| `hho/HHO_CHARTER.md` | governance text | status line and §3 only (publication commit) |
| `hho/HHO_CLAIM_REGISTER.md` | the register | new sections B.6 (one row) and B.7 (nine rows); four evidence abbreviations; two new open items and the notes of two open items in Part D |
| `hho/HHO_GATES.md` | live summary | three rows in the table of local tools |
| `hho/HHO_SUPPORT_RESULTS.md` | live summary | §3.3 rewritten for bridge B2; new §6 on positive-defect primes; the list of open items is now §7 |
| `records/hho/HHO_SOURCE_MANIFEST.md` | source manifest | new §3.3: the HCG pipe answer used as an input |
| `evidence/hho/posdefect/` | eleven session-native files and `SHA256SUMS` | **new since `hho-v0.3`** (merged with PR #56, #58, #59, #60) |
| `records/hho/HHO_POSDEFECT_FIRST_READING.md` | session record of 12 Nov 2026 | **placed unchanged** by this release (SHA-256 `18aa8f7a24c9866674d7db6ea0064499885ac282ed5ebdf860bd0befd48bf3a6`); it was sent to the PI and is cited by hash in `HHO_POSDEFECT_PROJECTOR_AND_S_LENGTH_CHATGPT.md`. §3 of that note is superseded by HHO-LEM-SECTOR. It adds no row. |

Session records on `main` that the new rows cite (not adopted as claims): `HHO_B2_COMPARISON_CLAUDE.md`; `HHO_POSDEFECT_PROJECTOR_AND_S_LENGTH_CHATGPT.md`; `HHO_C6_P2_INTEGRAL_MODEL_CHATGPT.md`; `HHO_POSDEFECT_CLAUDE_REVIEW.md`; `HHO_POSDEFECT_F20_PILOT_CLAUDE.md`; `HHO_POSDEFECT_FULL_GLUING_MECHANISM_CLAUDE.md`.

## 3. Changes of scientific content since `hho-v0.3`

**B.6 — bridge B2 (one row).**

| RID | Statement, in short | Grade | State |
|---|---|---|---|
| `HHO-LEM-B2` | If Severn's A_σ and its polarization are defined as HCG reads them, its Hermitian form is a rational multiple of h_W; in rank 8 the classes agree and the support bound applies to A_σ. | `[THM-cond: HCG's reading of Severn's Def. 3.2, Lemma 3.3 and Prop. 7.1 Step 1]` | CHECKED for the algebra; source not verified by HHO |

**B.7 — positive-defect primes (nine rows).**

| RID | Statement, in short | Grade | State |
|---|---|---|---|
| `HHO-LEM-GLUE-PROJECTOR` | L^# = eM; A ≅ M/(L ⊕ L′); p^t·A = 0 for t = v_p(\|G\|/χ(1)) | `[THM]` | CHECKED |
| `HHO-LEM-SECTOR` | the Hermitian dual of the χ-sector lattice is e_χM_R; for an absolutely irreducible reduction, ℓ_S(A_χ) = v_p(det h_W) | `[THM]` | CHECKED |
| `HHO-THM-COVER-BLOCK` | for a G-cover and a block without the trivial module, H¹(C, 𝒪)_B ≅ Ω(Q_B) ⊕ projective | `[THM-cond: Gysin sequence … as a sequence of 𝒪[G]-modules]` | CHECKED |
| `HHO-THM-FG-F20` | C₃ × F₂₀ at 5: A_χ ≅ ⊕ S_μ^{m(ω ⊗ λ_μ)} for every cover | same | CHECKED |
| `HHO-THM-FG-C6` | C₆ at 2: ℓ(A_{χ₁}) = m(χ₄) for every cover | same | CHECKED |
| `HHO-COR-PROJ-EVEN` | irreducible reduction, block without the trivial module, no local monodromy of order divisible by p ⇒ v_p(det h_W) even in rank 8 | same, for the Jacobian-induced class | CHECKED |
| `HHO-NUM-C6-JAC` | integral cup lattices of three C₆ covers: sector length 7, 0, 0 | `[NUM]` | CHECKED (two implementations) |
| `HHO-NUM-F20-SECTOR` | 42 C₃ × F₂₀ tuples: n_μ equal to the Chevalley–Weil multiplicities; n₁ = t − 2 | `[NUM]` | CHECKED (two implementations; the second is not in the repository) |
| `HHO-NEG-GLUE-FORMAL` | character and Brauer tree do not determine the gluing of a formal self-dual lattice | `[NEG]` | (a) CHECKED; (b) argument checked, no file |

**New open items.** `HHO-OPEN-PARITY-CONSTITUENT` (which constituent of A_χ carries the parity when the reduction is reducible) and `HHO-OPEN-INTCW-REF` (a literature reference for the structure statement).

**Open items restated (notes only).** `HHO-OPEN-SUPPORT-TRANSFER`: the algebra is recorded as `HHO-LEM-B2`; what stays open is one source check with three named parts. `HHO-OPEN-POSDEFECT-GLUE`: settled for the two worked blocks and for the projective case with irreducible reduction; open elsewhere.

**Provenance and limits.**
- B2: comparison by Claude, checked by ChatGPT (PR #64). HCG's answer is one session's reading of unrefereed texts; **the HHO sessions have not read Severn's texts.**
- Projector lemma and the formal C₆ model: ChatGPT; reviewed and rebuilt by Claude (PR #56, #58). Sector lemma, the three C₆ lattices, the F₂₀ pilot and the structure statement: Claude; checked by ChatGPT, with an independent modulo-2 computation in the repository (PR #59) and an independent 𝔽₂₅ computation that is **not** in the repository (PR #60, #66).
- The recorded parabolic-cup classes that the `[NUM]` rows are compared with were **not recomputed**.
- All covers computed have at most ten branch points and cannot satisfy (D).
- No novelty is claimed for `HHO-THM-COVER-BLOCK`; the literature was not read.
- No third-family check and no human refereeing exists for any new row.

## 4. Received inputs

### 4.1 HCG — the pin stays at `hcg-v0.2`

HCG published `hcg-v0.5` on 12 Nov 2026 (notice `pipes/HHO/20261112-HCG-v0.5-release.md`). Its ledger records Lemma E, Lemma F, Theorem R and the d ≤ 14 corollary of Δ27 as CHECKED by two AIs, under new RID labels. **HHO does not re-pin in this release.**

- No new row of this edition depends on a result that changed state between `hcg-v0.2` and `hcg-v0.5`.
- A re-pin needs the comparison of the later ledger with HHO's uses of (L), (D), (H0)–(H4), W5 and the Δ27 statements of Part A, and a mapping of "Lemma E", "Lemma F" and "Theorem R" to HCG's new labels. Neither has been made. It is a natural task for the edition that starts the work on (D).
- Until then the HHO texts keep describing the Δ27 material as pending at the pin.

### 4.2 HCG — the answer on Severn's polarized factor

`pipes/HHO/20261112-HCG-answer-severn-polarized-factor.md` was dispositioned on 12 Nov 2026 (accept, as an HCG input; PR #64). It is the input of `HHO-LEM-B2` and is listed in the manifest §3.3 with the hash of the file as received.

### 4.3 RTG

None.

### 4.4 Third-party sources

None added.

## 5. Review corrections applied before this draft

| Correction | Where | Source |
|---|---|---|
| Typing of the S-length statement (which module, which constituent) | `HHO_POSDEFECT_CLAUDE_REVIEW.md` §3 | ChatGPT, `HHO_POSDEFECT_PROJECTOR_AND_S_LENGTH_CHATGPT.md` §5 |
| B2-1 Tate twist; B2-2 the factor ±2(ϑ/δ)q; B2-3 the open source obligation | `HHO_B2_COMPARISON_CLAUDE.md` | ChatGPT review `5875862532` |
| FG-1 two lemmas with proofs; FG-2 explicit models in F₂₀ and C₆ | `HHO_POSDEFECT_FULL_GLUING_MECHANISM_CLAUDE.md` | ChatGPT review `5888334794` |

## 6. Not part of this release

- **Any ACCEPTED claim, and any regrading or promotion of a row that existed in `hho-v0.3`.** In particular the grade of `HHO-THM-SUPPORT` for Severn's factor is unchanged; `HHO-LEM-B2` is a separate row.
- **A re-pin of HCG** (§4.1).
- **The source check of Severn's definitions** (`HHO-OPEN-SUPPORT-TRANSFER`).
- **Part III of the mechanism record** (which constituent carries the parity): heuristic, recorded as an open item only.
- **A literature reference** for the structure statement.
- **Anything about (D).** The observation of the first-reading note that the G(6,1,6) tuples P1–P3 satisfy every item of (H) except (D) is in a placed session record and is not a register row.
- **ChatGPT's independent 𝔽₂₅ script.** If it is placed later, the review state of `HHO-NUM-F20-SECTOR` does not change; its evidence column does.
- **Any import or transfer to HCG or RTG.**

## 7. Adoption manifest

**Status: DRAFT.** The SHA-256 values are filled in by the publication commit (§9) for: the four live files of `hho/`; `records/hho/HHO_SOURCE_MANIFEST.md`; the three evidence indexes (`evidence/hho/SHA256SUMS`, unchanged; `evidence/hho/b1/SHA256SUMS`, unchanged; `evidence/hho/posdefect/SHA256SUMS`); `upload/hho/SHA256SUMS` (unchanged); the seven session records cited by the new rows; the `hho` row of `REGISTRY.md`; the dispositioned notice.

## 8. Checks and decisions

**Checks run for this draft.**

| Check | Result | By |
|---|---|---|
| Every claim row of `hho-v0.3` outside Part D is present unchanged (37 rows) | pass | Claude (script) |
| New RIDs: exactly twelve (ten claim rows, two open items) | pass | Claude (script) |
| Every RID used in the two live summaries exists in the register | pass | Claude (script) |
| `sha256sum -c` for the three evidence indexes | pass | Claude |
| Computations | none for this edition | — |

**Decisions.**

| Decision | By | Entry |
|---|---|---|
| Pilot on C₃ × F₂₀ | PI, 12 Nov 2026 | "pilot için onay veriyorum" |
| Merge of PR #64 and PR #66 as session records | PI | merge commits `ebe32ef`, `31f5913` |
| Co-owner review of this record | ChatGPT HHO owner session | pending |
| Adoption of `hho-v0.4` | PI | pending |

## 9. Publication step (not yet applied)

After the PI's adoption decision, one publication commit: status lines of the five live files and charter §3; the `hho` row of `REGISTRY.md`; this record with "DRAFT" removed and §7–§8 completed. Then the PI merges with a merge commit and creates the annotated tag `hho-v0.4`, whose message states the SHA-256 of this record.

## 10. Pipe items handled with this release

| Item | Action |
|---|---|
| `pipes/HHO/20261112-HCG-v0.5-release.md` | dispositioned: accept. The notice is taken into §4.1; the pin stays at `hcg-v0.2`. |
