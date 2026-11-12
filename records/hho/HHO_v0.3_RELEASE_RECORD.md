# HHO v0.3 — release record

**Status:** **ADOPTED by the PI on 12 Nov 2026 as a register edition** (§8). Publication tag: `hho-v0.3`, created by the PI on the merge commit of the pull request that carries this record (PR #55).

**Release:** third repository edition of the HHO study. It supersedes `hho-v0.2` as the governing edition.

**Prepared by:** the Claude HHO owner session, on the PI's decision of 12 Nov 2026 that the B1 results enter the claim register with `hho-v0.3`. **Review:** the ChatGPT HHO owner session. **Adoption:** PI Mustafa Aksu.

## 1. What this release is

`hho-v0.3` is a **register edition**. It records the first results of the study's work on P1: the bridge B1 between the parabolic-cup form and the Jacobian-induced multiplicity form, and the necessary condition that follows from it.

- **No claim row becomes ACCEPTED.** No row that existed in `hho-v0.2` is regraded or promoted.
- Three rows are added, all conditional on named external inputs and CHECKED by two AIs (§3). No third-family check and no human refereeing exists for them.
- The pin of HCG stays at `hcg-v0.2` (§4.1).

**Scope guard.** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist, and no statement about the Hodge conjecture. Severn's results stay CLAIMED. A failed gate excludes a datum or a class of data and nothing more.

## 2. Files of this edition

| File | Role | Change since `hho-v0.2` |
|---|---|---|
| `hho/HHO_CHARTER.md` | governance text | status line and §3 only (publication commit) |
| `hho/HHO_CLAIM_REGISTER.md` | the register | new section B.5 with three rows; three evidence abbreviations; notes of three open items in Part D |
| `hho/HHO_GATES.md` | live summary | one row in the table of local tools; the last paragraph of §5 |
| `hho/HHO_SUPPORT_RESULTS.md` | live summary | the paragraph "Two different objects"; new §3.4; two rows of §6; the first sentence of §4 names the pin for the locality theorem |
| `records/hho/HHO_SOURCE_MANIFEST.md` | source manifest | four rows in §3.2 (third-party sources of B1) |
| `records/hho/HHO_P1_KNOWN_RESULTS_AND_OPEN_GAP.md` | session record | one wording correction in Gap B, with a change-record row |
| `evidence/hho/b1/` | three session-native files and `SHA256SUMS` | **new** (merged with PR #49 and PR #51) |
| `evidence/hho/README.md` | guide to the evidence folder | scope of the root index stated; `b1/` listed (PR #49) |

Session records placed since `hho-v0.2`, not adopted as claims: the P1 source-review note and its review (PR #45, #46); the B1 proof and its two reviews (PR #49, #51). The B1 source-reading note of 11 Nov 2026 (SHA-256 `72683c0315adfb0075912a7e028a21ee9e9ee9ddbd714245dc448308596e5669`) was sent to the PI and is cited by hash in the proof; it is **not** in the repository.

## 3. Changes of scientific content since `hho-v0.2`

Three new rows in the register, section B.5. No other claim, grade or review state changes.

| RID | Statement, in short | Grade | State |
|---|---|---|---|
| `HHO-LEM-B1-O2` | On Z = ker C, the triangular form B of the locality proof is the Dettweiler–Wewers cup pairing. | `[THM-cond: DW06 Thm 2.5]` | CHECKED |
| `HHO-LEM-B1-O1` | For a finite Galois cover and σ absolutely irreducible over K with character field K: h_W = c·δ·S with c ∈ ℚ^×; in rank 8 the classes agree; also with Γ = G/ker σ. | `[THM-cond: DW06 Thm 2.5; cup product under a finite direct image]` | CHECKED |
| `HHO-COR-B1-GATE` | A nonsplit rank-eight parabolic-cup class of signature (4,4) needs a prime p ≡ 2 (mod 3) dividing \|Γ\|/χ(1). | same | CHECKED |

- **Provenance.** Proof: ChatGPT session (`records/hho/HHO_B1_O1_O2_CHATGPT_PROOF.md`). Receiving reviews, an independent line-by-line derivation of O2 and of the defining identity in O1, and an independent exact check of O2 on noncommutative tuples: Claude session. Both owners read §§2.2–2.4 of Dettweiler–Wewers 2006 in the PI's copy.
- **Conditions, named.** (i) Dettweiler–Wewers 2006, Thm 2.5, whose proof rests on the Poincaré isomorphism for local coefficients. (ii) For O1 and the gate: multiplicativity of H*(Y,K) ≅ H*(X, f_*K) for a finite map and agreement of the local-coefficient cup product with the sheaf cup product. These are standard; **no statement of (ii) was read by either owner.**
- **Not used.** Locality, (D), (L), the budget, the dimension d, Severn's texts.
- **Prior art.** The comparison is Steps 3–4 of Severn's Prop. 5.1 ([386]) = Prop. 7.1 (v2) as HCG reads it (`HCG-EXT-PO6`). HHO claims no novelty. What is new in HHO is a proof that does not depend on those texts, and the combination with `HHO-THM-SUPPORT`.
- **What the gate is not.** It is a necessary condition. It does not decide P1. It says nothing about Severn's polarized factor: bridge B2 (`HHO-OPEN-SUPPORT-TRANSFER`) stays open.

**Open items restated.** `HHO-OPEN-LOCAL-EVEN`: with the gate, the question remains at inert primes dividing \|Γ\|/χ(1). `HHO-OPEN-POSDEFECT-GLUE`: named as the next study target (PI decision of 12 Nov 2026).

## 4. Received inputs

### 4.1 HCG — the pin stays at `hcg-v0.2`

HCG published `hcg-v0.4` on 11 Nov 2026 (notice `pipes/HHO/20261111-HCG-v0.4-release.md`). Its ledger records the locality theorem and the induced-period bound as `[THM]`, CHECKED by two AIs. **HHO does not re-pin in this release.**

- The three new rows do not depend on locality or on the induced-period bound.
- The rows graded `[THM-cond: locality]` keep that grade under any pin: an HCG result does not gain HHO grade by citation (charter §5.1).
- A re-pin needs the comparison of the later ledger with HHO's uses of (L), (D), (H0)–(H4) and W5. That comparison has not been made.

### 4.2 RTG

None.

### 4.3 Third-party sources

Added to the manifest §3.2: the two Dettweiler–Wewers papers (bibliographic identifiers and the SHA-256 of the PI's copies; not stored), Hatcher's textbook as cited by ChatGPT, and the unfixed sheaf-theory reference. No LIT-backed validation is claimed.

## 5. Review corrections applied

| Correction | Where | Source |
|---|---|---|
| F1–F3 and scope refinements of the P1 note | `records/hho/HHO_P1_KNOWN_RESULTS_AND_OPEN_GAP.md` | ChatGPT review `HHO_P1_CHATGPT_REVIEW_20261111.md`; PR #45 |
| C1–C4 of the O1 proof | `records/hho/HHO_B1_O1_O2_CHATGPT_PROOF.md` | Claude review, PR #51; applied by ChatGPT at `55f4280` |
| B1 files moved to `evidence/hho/b1/` with their own index | `evidence/hho/` | Claude review P1; ChatGPT at `55f4280` |
| Gap B wording of the P1 note | same note | ChatGPT's non-blocking note on PR #45 |
| Locality is "pending at the HHO pin `hcg-v0.2`", with the later HCG state named | `hho/HHO_SUPPORT_RESULTS.md` §4 | ChatGPT review `5872680250` of this record, clarification 1 |
| The B1 source-reading note stays outside the repository, cited by hash | §2 of this record | same review, clarification 2 |
| Checks are listed by who ran them; proof review and frozen evidence kept apart | §8 of this record | same review, clarification 3 |

## 6. Not part of this release

- **Any ACCEPTED claim, and any regrading or promotion of a row that existed in `hho-v0.2`.**
- **A re-pin of HCG** (§4.1).
- **Bridge B2.** A question was sent to HCG (`pipes/HCG/20261112-HHO-question-severn-polarized-factor.md`, PR #54); no answer is part of this release.
- **A source for condition (ii)** of §3.
- **A third-family check** of the new rows.
- **A re-check of the Part A proofs**, and a full comparison of Part B with every Δ27 report. The P1 note records what was read.
- **Any import or transfer to HCG or RTG.**
- **Work on `HHO-OPEN-POSDEFECT-GLUE`.** The session records and evidence of 12 Nov 2026 on `main` (`records/hho/HHO_POSDEFECT_*`, `records/hho/HHO_C6_P2_INTEGRAL_MODEL_CHATGPT.md`, `evidence/hho/posdefect/`; PR #56, #58, #59) are **not** part of this edition. They add no register row.
- **Two pipe items received after the draft:** HCG's answer on Severn's polarized factor and the `hcg-v0.5` notice (both of 12 Nov 2026). They stay open and are handled after this release.

## 7. Adoption manifest

**Status: ADOPTED (2026-11-12).** SHA-256 of the bytes in the publication commit (§9).

| File | Role | SHA-256 |
|---|---|---|
| `hho/HHO_CHARTER.md` | charter (governance text; no scientific claim) | `cbce7ba8a106e1254d61e19a0447fed768f1503188fac22802c0d42474d4853f` |
| `hho/HHO_CLAIM_REGISTER.md` | claim register (adopted as a register; no row ACCEPTED) | `5290b0fc8e814cfe0a9676b2b32570f9705c8a3e732d3c0d354de3a6c16751f0` |
| `hho/HHO_GATES.md` | live summary: gates, bounds, calibration objects | `3695bae7976f4a3aa09c82e674335d42c99796d5491e384c1e5adb62a196e030` |
| `hho/HHO_SUPPORT_RESULTS.md` | live summary: support results and bridge B1 | `61d25bc973488fee742dc738fa9099e1a62e71076d78894b1c7ebe61af00187f` |
| `records/hho/HHO_SOURCE_MANIFEST.md` | source manifest | `443f7fd543d29305f89747dee8129dfad39c035cdcb7214a64c552f73e9adb5b` |
| `evidence/hho/SHA256SUMS` | index of the 54 placed evidence files (unchanged since `hho-v0.2`) | `e042d035534ca134ffed143eba41d97895dbe3de83ec5e6fec91db9ca77a5ae6` |
| `evidence/hho/b1/SHA256SUMS` | index of the three B1 files | `340c812af34e3b47ed37f47b6eeb6e4024e2f90dbde7d1876fe9d777a87d8fac` |
| `evidence/hho/README.md` | guide to the evidence folder | `9fed0f76ef2d75b8cfda28fe2ac5e96169ad71ad40b04b346b698dbf761139fa` |
| `upload/hho/SHA256SUMS` | index of the 57 uploaded source files (unchanged since `hho-v0.1`) | `50417fca3c82ad7a487d0c986047ecb002d86aa5f5cbffe087672df33d60b410` |
| `records/hho/HHO_B1_O1_O2_CHATGPT_PROOF.md` | B1 proof (session record; evidence of the three new rows) | `a3a0c6c65fa0b0a63d83c3741aa7a64f6eca18651b3070fd16895469110493b3` |
| `records/hho/HHO_B1_O1_O2_CLAUDE_REVIEW.md` | first receiving review (session record) | `7e949171d4e9dc383d497102e2638f7d8990380fb52aa27e82cadd9cd4f27cb6` |
| `records/hho/HHO_B1_O1_O2_CLAUDE_REVIEW_ROUND2.md` | second receiving review (session record) | `a8238f5a5abfec0e8ac0b18ac2da93d1c4e6847bf9f99fa46c166416518af7c5` |
| `pipes/HHO/20261111-HCG-v0.4-release.md` | received notice, dispositioned | `80ed5aa5cb5ecc5a7780f549d472afeebcdda45d44d2a3c3d0721644f4654a87` |
| `REGISTRY.md`, the `hho` row | the single line of the `hho` study, with its line feed | `1e6c7f62d36d3801b0441c6a72f969b11be2645df5f38d301f0c2cd9f9a91551` |

- The 54 files of the root index and the three B1 files are adopted as **evidence as it stands**, not as claims.
- The three session records of B1 are listed because the new rows cite them. They are not adopted as claims; the register rows carry the grade and the state.
- HCG material that is pending at the pin stays pending for HHO.
- Only the `hho` row of `REGISTRY.md` is hashed, because other studies change the same file.
- The SHA-256 of this record is stated in the tag message, not here.

## 8. Checks and decisions

**Checks run for this edition.**

| Check | Result | By |
|---|---|---|
| `sha256sum -c` for `evidence/hho/b1/SHA256SUMS` (3 files) and for the root index (54 files) | pass | Claude; the PI's merge runs of 12 Nov 2026 |
| Replay of `b1_o2_noncommutative_check_claude.py` (1264 entries) | byte-identical output | Claude only |
| Replay of `hho_b1_o2_exact_check.py` (9 entries) | 9/9 PASS | ChatGPT (author); Claude (replay) |
| Every RID used in the two live summaries and in this record exists in the register | pass | Claude (script) |
| 40 earlier RIDs retained; exactly three new RIDs; no earlier grade or state changed | pass | ChatGPT (review `5872680250`) |
| Other computations | none | — |

**Proof review, kept apart from the checks.** O2 and O1 were proved by the ChatGPT session and reviewed twice by the Claude session, which re-derived O2 and the defining identity of O1 independently. Both owners read §§2.2–2.4 of Dettweiler–Wewers 2006. Neither read a statement of the second named input. **The 54 frozen files were not replayed for this edition.**

**Decisions.**

| Decision | By | Entry |
|---|---|---|
| Start of P1, first stage: source review | PI, 11 Nov 2026 | relayed in the HHO conversation |
| Start of B1 | PI, 11 Nov 2026 | "B1 e başlayalım" |
| B1 results enter the register with `hho-v0.3`; question on B2 to HCG; next target `HHO-OPEN-POSDEFECT-GLUE` | PI, 12 Nov 2026 | "1- girsin hho-v0.3 ile 2- gönderilsin 3- önerin uygun HHO-OPEN-POSDEFECT-GLUE" |
| Co-owner review of this record | ChatGPT HHO owner session | PR #55, review `5872680250` at `855cd8e`: ACCEPT AS A DRAFT RELEASE RECORD, with three non-blocking publication clarifications. All three are applied (§5). The review supports keeping the pin at `hcg-v0.2`. |
| Adoption of `hho-v0.3` with the scope of §§1–6, including the pin at `hcg-v0.2` | PI, 12 Nov 2026, 16:28 +03:00 | "hho-v0.3 ü benimsiyorum." — I adopt hho-v0.3. The scope put to the PI before the decision: register edition only; the three B1 rows conditional and CHECKED; no row ACCEPTED; pin at `hcg-v0.2`. |
| Publication | PI | the PI merges PR #55 with a merge commit and creates the annotated tag |

## 9. Publication step (applied on 12 Nov 2026)

The sequence is: PI adoption decision → **one** publication commit → PI merge → annotated tag.

The publication commit contains all of the following and nothing else:

1. Status lines of the five live files: `hho/HHO_CHARTER.md`, `hho/HHO_CLAIM_REGISTER.md`, `hho/HHO_GATES.md`, `hho/HHO_SUPPORT_RESULTS.md` and `records/hho/HHO_SOURCE_MANIFEST.md`.
   - In the charter, §3 is brought up to date: the governing edition is `hho-v0.3`, and one bullet describes this edition.
   - In `hho/HHO_SUPPORT_RESULTS.md`, the first sentence of §4 names the pin for the locality theorem (clarification 1 of the co-owner's review).
   - No other text changes in these files.
2. `REGISTRY.md`, `hho` row: the governing edition is `hho-v0.3` with this record.
3. This record: "DRAFT" removed; the three clarifications applied; §6–§9 completed.

Before the commit, `main` at `cb742f8` was merged into the release branch. That merge touched no file of §7 except `REGISTRY.md`, where it changed another study's row.

The hashes of §7 are those of the files in the publication commit itself. This record cannot contain its own hash; the tag message states it.

## 10. Pipe items handled with this release

| Item | Action |
|---|---|
| `pipes/HHO/20261111-HCG-v0.4-release.md` | dispositioned: accept. The notice is taken into §4.1; the pin stays at `hcg-v0.2`. |
