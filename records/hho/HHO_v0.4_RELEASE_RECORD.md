# HHO v0.4 — release record

**Status:** **ADOPTED by the PI on 14 Nov 2026 as a register edition** (§8). Publication tag: `hho-v0.4`, created by the PI on the merge commit of the pull request that carries this record (PR #69).

**Release:** fourth repository edition of the HHO study. It supersedes `hho-v0.3` as the governing edition.

**Prepared by:** the Claude HHO owner session, on the recommendation of both owner sessions (Claude, 13 Nov 2026; ChatGPT, relayed by the PI on 14 Nov 2026) that the session results on `main` be fixed in a register edition before the work on (D) starts. **Review:** the ChatGPT HHO owner session. **Adoption:** PI Mustafa Aksu. The draft was prepared without a PI instruction; the PI's adoption decision is recorded in §8.

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
| `evidence/hho/posdefect/` | ten session-native files and `SHA256SUMS` | **new since `hho-v0.3`** (merged with PR #56, #58, #59, #60) |
| `records/hho/HHO_POSDEFECT_FIRST_READING.md` | session record of 12 Nov 2026 | **placed unchanged** by this release (SHA-256 `18aa8f7a24c9866674d7db6ea0064499885ac282ed5ebdf860bd0befd48bf3a6`); it was sent to the PI and is cited by hash in `HHO_POSDEFECT_PROJECTOR_AND_S_LENGTH_CHATGPT.md`. §3 of that note is superseded by HHO-LEM-SECTOR. It adds no row. **Custody:** it is a record written by the Claude owner session and placed by its author on a `claude/*` branch, as the P1 note was (PR #45, first commit); it is not a file arriving from outside, so the `upload/<topic>` intake of `CONVENTIONS.md` is not used. Its byte identity with the copy the PI received was verified by the co-owner (review `5906870449`). |
| `records/hho/HHO_NEG_GLUE_FORMAL_CHATGPT.md` | session record of 14 Nov 2026 (ChatGPT) | **new**, received through PR #70 and merged into the release branch (SHA-256 `64179e01b21c23ed9ec35a2f2050808b7e277a8ddb661af045d902ff72c22dfc`); source of part (b) of `HHO-NEG-GLUE-FORMAL`. It adds no row. |

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
| `HHO-NEG-GLUE-FORMAL` | character and Brauer tree do not determine the gluing of a formal self-dual lattice | `[NEG]` | CHECKED |

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

## 5. Review corrections applied

| Correction | Where | Source |
|---|---|---|
| Typing of the S-length statement (which module, which constituent) | `HHO_POSDEFECT_CLAUDE_REVIEW.md` §3 | ChatGPT, `HHO_POSDEFECT_PROJECTOR_AND_S_LENGTH_CHATGPT.md` §5 |
| B2-1 Tate twist; B2-2 the factor ±2(ϑ/δ)q; B2-3 the open source obligation | `HHO_B2_COMPARISON_CLAUDE.md` | ChatGPT review `5875862532` |
| FG-1 two lemmas with proofs; FG-2 explicit models in F₂₀ and C₆ | `HHO_POSDEFECT_FULL_GLUING_MECHANISM_CLAUDE.md` | ChatGPT review `5888334794` |
| R1: the parity is a congruence, ε_p ≡ ℓ_S(A_χ) (mod 2) | `hho/HHO_GATES.md`, table of local tools | ChatGPT review `5906870449` of this record |
| R2: the negative control (b) cites a file; custody of the first-reading note stated | register B.7; §2 of this record | same review; PR #70 |
| Editorial: χ ≠ χ̄ in the projector row; the second formulation of the sector lemma scoped; "branch count" limited to the two worked blocks | register B.7; `hho/HHO_SUPPORT_RESULTS.md` §6.5 | same review |

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

**Status: ADOPTED (2026-11-14).** SHA-256 of the bytes in the publication commit (§9).

| File | Role | SHA-256 |
|---|---|---|
| `hho/HHO_CHARTER.md` | charter (governance text; no scientific claim) | `be77ab1536775212c59d17f42741dfb04180c5321361f41e95442533c6177bc1` |
| `hho/HHO_CLAIM_REGISTER.md` | claim register (adopted as a register; no row ACCEPTED) | `ee3a6d280fbcea0b184c8c8c625880f5515a4f88d59de5b2eac2050887495c19` |
| `hho/HHO_GATES.md` | live summary: gates, bounds, calibration objects | `2131c9c180fee1c01a5adf85458eb160dda54b6096acf8fb8cb922e2888ec52c` |
| `hho/HHO_SUPPORT_RESULTS.md` | live summary: support results, bridges, positive-defect primes | `59ffec8f095dfa0c79ed1a48c74623f0211c30cfaca7059cc71db7d1d5d6cf85` |
| `records/hho/HHO_SOURCE_MANIFEST.md` | source manifest | `955f3910d85c06ec57085d1eccce9b30ccf301c750808778d2e445c92fc29c78` |
| `evidence/hho/SHA256SUMS` | index of the 54 placed evidence files (unchanged since `hho-v0.2`) | `e042d035534ca134ffed143eba41d97895dbe3de83ec5e6fec91db9ca77a5ae6` |
| `evidence/hho/b1/SHA256SUMS` | index of the three B1 files (unchanged since `hho-v0.3`) | `340c812af34e3b47ed37f47b6eeb6e4024e2f90dbde7d1876fe9d777a87d8fac` |
| `evidence/hho/posdefect/SHA256SUMS` | index of the ten positive-defect scripts and outputs | `705de5115a7157ed55ab9276ce03dbace93eec1f3010edfaa29a41ea239bb3af` |
| `evidence/hho/README.md` | guide to the evidence folder | `9fed0f76ef2d75b8cfda28fe2ac5e96169ad71ad40b04b346b698dbf761139fa` |
| `upload/hho/SHA256SUMS` | index of the 57 uploaded source files (unchanged since `hho-v0.1`) | `50417fca3c82ad7a487d0c986047ecb002d86aa5f5cbffe087672df33d60b410` |
| `records/hho/HHO_B2_COMPARISON_CLAUDE.md` | session record: bridge B2 | `0423165f76216b3b1ca88661151f19a2a61c7146e95265975b60d75277475d26` |
| `records/hho/HHO_POSDEFECT_PROJECTOR_AND_S_LENGTH_CHATGPT.md` | session record: projector lemma | `a16c553103d74df21fe88810a0492ba1a72c063d936bb29ee632942b84117ec9` |
| `records/hho/HHO_C6_P2_INTEGRAL_MODEL_CHATGPT.md` | session record: formal C₆ model | `628947ebdc6dd1db41e93b775866717d8416716f72d8c6a58a152d1ea996f721` |
| `records/hho/HHO_POSDEFECT_CLAUDE_REVIEW.md` | session record: review, sector lemma, three C₆ lattices | `12857b21ac9129be41f143fcd0ba597e396e42e3cc34402b1d9fe1d63a88b0c6` |
| `records/hho/HHO_POSDEFECT_F20_PILOT_CLAUDE.md` | session record: C₃ × F₂₀ pilot | `7d96d8300c2e59382485ca5cb187dad6597eebbb9a6800be47800db370ebf3bb` |
| `records/hho/HHO_POSDEFECT_FULL_GLUING_MECHANISM_CLAUDE.md` | session record: structure of the cover lattice | `a6a3253ef1a2b6c62060c754430ea5dc5cc34be7a869ec8b30af96f07e10bb42` |
| `records/hho/HHO_NEG_GLUE_FORMAL_CHATGPT.md` | session record: formal negative control | `64179e01b21c23ed9ec35a2f2050808b7e277a8ddb661af045d902ff72c22dfc` |
| `records/hho/HHO_POSDEFECT_FIRST_READING.md` | session record: first reading (placed unchanged) | `18aa8f7a24c9866674d7db6ea0064499885ac282ed5ebdf860bd0befd48bf3a6` |
| `pipes/HHO/20261112-HCG-v0.5-release.md` | received notice, dispositioned | `d5afdda29af360d85f86b69afc3c16709914cd4ffd8ce64d61c248b3bea31ebb` |

`REGISTRY.md`: only the single line of the `hho` study is hashed, with its line feed, because other studies change the same file: `53804a5a9bcaf12795d02086c006fb7fe3476a741822c42359fd314fd83611c0`.

- The evidence files are adopted as **evidence as it stands**, not as claims. `evidence/hho/posdefect/` holds ten scripts and outputs and their index.
- The eight session records are listed because the new rows cite them. They are not adopted as claims; the register rows carry the grade and the state.
- HCG material that is pending at the pin stays pending for HHO.
- The SHA-256 of this record is stated in the tag message, not here.

## 8. Checks and decisions

**Checks run for this edition.**

| Check | Result | By |
|---|---|---|
| Every claim row of `hho-v0.3` outside Part D is present unchanged (37 rows) | pass | Claude (script); ChatGPT (review `5906870449`) |
| New RIDs: exactly twelve (ten claim rows, two open items); none deleted | pass | Claude (script); ChatGPT |
| Every RID used in the two live summaries and in this record exists in the register | pass | Claude (script) |
| `sha256sum -c` for the three evidence indexes | pass | Claude |
| Byte identity of the first-reading note and of the HCG pipe answer as received | pass | ChatGPT (review `5906870449`) |
| Computations | none for this edition | — |

**Proof review, kept apart from the checks.** The new rows rest on session records reviewed in PR #56, #58, #59, #60, #64, #66 and #70. For this edition the co-owner checked the changed claims against those records in a targeted way and re-ran no code. **The 54 frozen files were not replayed.**

**Decisions.**

| Decision | By | Entry |
|---|---|---|
| Pilot on C₃ × F₂₀ | PI, 12 Nov 2026 | "pilot için onay veriyorum" |
| Merge of PR #64 and PR #66 as session records | PI | merge commits `ebe32ef`, `31f5913` |
| Co-owner review of this record | ChatGPT HHO owner session | PR #69, review `5906870449` at `3c9f92a`: ACCEPT WITH TWO SCOPED, PRE-ADOPTION CHANGES (R1, R2), both applied at `c57d757` (§5). Its answers: the four conditional grades stay; the second formulation of the sector lemma stays in the same row; the pin stays at `hcg-v0.2`. |
| Adoption of `hho-v0.4` with the scope of §§1–6, including the pin at `hcg-v0.2` | PI, 14 Nov 2026, 23:27 +03:00 | "hh0-v0.4 ü benimsiyorum" — I adopt hho-v0.4 (the PI's message has "hh0"; it answers the request for a decision on `hho-v0.4`). The scope put to the PI before the decision: register edition only; no row ACCEPTED; pin at `hcg-v0.2`. |
| Publication | PI | the PI merges PR #69 with a merge commit and creates the annotated tag |

## 9. Publication step (applied on 14 Nov 2026)

The sequence is: PI adoption decision → **one** publication commit → PI merge → annotated tag.

The publication commit contains all of the following and nothing else:

1. Status lines of the five live files: `hho/HHO_CHARTER.md`, `hho/HHO_CLAIM_REGISTER.md`, `hho/HHO_GATES.md`, `hho/HHO_SUPPORT_RESULTS.md` and `records/hho/HHO_SOURCE_MANIFEST.md`. In the charter, §3 is brought up to date: the governing edition is `hho-v0.4`, and one bullet describes this edition. No other text changes in these files.
2. `REGISTRY.md`, `hho` row: the governing edition is `hho-v0.4` with this record.
3. This record: "DRAFT" removed; §7–§9 completed.

Before the commit, `main` at `e45574b` was merged into the release branch. That merge touched no file of §7.

The hashes of §7 are those of the files in the publication commit itself. This record cannot contain its own hash; the tag message states it.

## 10. Pipe items handled with this release

| Item | Action |
|---|---|
| `pipes/HHO/20261112-HCG-v0.5-release.md` | dispositioned: accept. The notice is taken into §4.1; the pin stays at `hcg-v0.2`. |
