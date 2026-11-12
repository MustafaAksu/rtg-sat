# HHO v0.3 — release record

**Status:** **DRAFT.** Not adopted. It becomes the record of `hho-v0.3` only after the co-owner's review, the PI's adoption decision and the publication commit (§9).

**Release:** third repository edition of the HHO study. If adopted, it supersedes `hho-v0.2` as the governing edition.

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
| `hho/HHO_SUPPORT_RESULTS.md` | live summary | the paragraph "Two different objects"; new §3.4; two rows of §6 |
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

## 5. Review corrections applied before this draft

| Correction | Where | Source |
|---|---|---|
| F1–F3 and scope refinements of the P1 note | `records/hho/HHO_P1_KNOWN_RESULTS_AND_OPEN_GAP.md` | ChatGPT review `HHO_P1_CHATGPT_REVIEW_20261111.md`; PR #45 |
| C1–C4 of the O1 proof | `records/hho/HHO_B1_O1_O2_CHATGPT_PROOF.md` | Claude review, PR #51; applied by ChatGPT at `55f4280` |
| B1 files moved to `evidence/hho/b1/` with their own index | `evidence/hho/` | Claude review P1; ChatGPT at `55f4280` |
| Gap B wording of the P1 note | same note | ChatGPT's non-blocking note on PR #45 |

## 6. Not part of this release

- **Any ACCEPTED claim, and any regrading or promotion of a row that existed in `hho-v0.2`.**
- **A re-pin of HCG** (§4.1).
- **Bridge B2.** A question was sent to HCG (`pipes/HCG/20261112-HHO-question-severn-polarized-factor.md`, PR #54); no answer is part of this release.
- **A source for condition (ii)** of §3.
- **A third-family check** of the new rows.
- **A re-check of the Part A proofs**, and a full comparison of Part B with every Δ27 report. The P1 note records what was read.
- **Any import or transfer to HCG or RTG.**
- **Work on `HHO-OPEN-POSDEFECT-GLUE`.** It starts after this draft.

## 7. Adoption manifest

**Status: DRAFT.** The SHA-256 values are filled in by the publication commit (§9) for: the four live files of `hho/`; `records/hho/HHO_SOURCE_MANIFEST.md`; `evidence/hho/SHA256SUMS` (unchanged, `e042d035534ca134ffed143eba41d97895dbe3de83ec5e6fec91db9ca77a5ae6`); `evidence/hho/b1/SHA256SUMS` (`340c812af34e3b47ed37f47b6eeb6e4024e2f90dbde7d1876fe9d777a87d8fac`); `evidence/hho/README.md`; `upload/hho/SHA256SUMS` (unchanged); the `hho` row of `REGISTRY.md`; the dispositioned pipe item.

## 8. Checks and decisions

| Check | Result | By |
|---|---|---|
| `sha256sum -c` for `evidence/hho/b1/SHA256SUMS` (3 files) and for the root index (54 files) | pass | Claude; the PI's merge run of 12 Nov 2026 |
| Replay of `b1_o2_noncommutative_check_claude.py` | byte-identical output | Claude |
| Replay of `hho_b1_o2_exact_check.py` | 9/9 PASS | Claude; ChatGPT |
| Every RID used in the two live summaries exists in the register | pass | Claude (script) |
| Other computations | none | — |

| Decision | By | Entry |
|---|---|---|
| Start of P1, first stage: source review | PI, 11 Nov 2026 | relayed in the HHO conversation |
| Start of B1 | PI, 11 Nov 2026 | "B1 e başlayalım" |
| B1 results enter the register with `hho-v0.3`; question on B2 to HCG; next target `HHO-OPEN-POSDEFECT-GLUE` | PI, 12 Nov 2026 | "1- girsin hho-v0.3 ile 2- gönderilsin 3- önerin uygun HHO-OPEN-POSDEFECT-GLUE" |
| Co-owner review of this record | ChatGPT HHO owner session | pending |
| Adoption of `hho-v0.3` | PI | pending |

## 9. Publication step (not yet applied)

After the PI's adoption decision, one publication commit: status lines of the five live files and charter §3; the `hho` row of `REGISTRY.md`; this record with "DRAFT" removed and §7–§8 completed. Then the PI merges with a merge commit and creates the annotated tag `hho-v0.3`, whose message states the SHA-256 of this record.

## 10. Pipe items handled with this release

| Item | Action |
|---|---|
| `pipes/HHO/20261111-HCG-v0.4-release.md` | dispositioned: accept. The notice is taken into §4.1; the pin stays at `hcg-v0.2`. |
