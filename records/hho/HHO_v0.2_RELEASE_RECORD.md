# HHO v0.2 — release record (DRAFT)

**Status:** **DRAFT. Not adopted.** Adoption is a PI decision, recorded in §8 after the co-owner review. Publication tag, once adopted: `hho-v0.2`, created on the merge commit of the pull request that carries this record.

**Release:** second repository edition of the HHO study. It supersedes `hho-v0.1` as the governing edition.

**Prepared by:** the Claude HHO owner session. **Review:** the ChatGPT HHO owner session. **Adoption:** PI Mustafa Aksu.

## 1. What this release is

`hho-v0.2` completes the move of HHO into `rtg-sat`. Like `hho-v0.1`, it is a **register edition**.

- **No claim row becomes ACCEPTED.** Every row keeps the review state written in the register.
- It adds the placed evidence, two live summaries, one new register row and four scoped corrections.
- No computation was run for this release, except two replays that confirmed the placed layout (§8).

**Scope guard.** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist, and no statement about the Hodge conjecture. Severn's results stay CLAIMED.

## 2. Files of this edition

| File | Role | Change since `hho-v0.1` |
|---|---|---|
| `hho/HHO_CHARTER.md` | governance text | one line in §2: the placement is recorded as done |
| `hho/HHO_CLAIM_REGISTER.md` | the register | evidence abbreviations name `evidence/hho/`; the withdrawn NPL is typed by object; one new row (§3) |
| `hho/HHO_GATES.md` | live summary: (H), gates G1–G12, dimension statements, calibration objects | **new** |
| `hho/HHO_SUPPORT_RESULTS.md` | live summary: current statements of the HHO conversation's results | **new** |
| `records/hho/HHO_SOURCE_MANIFEST.md` | source manifest | §6 records the placement; §4.1 records the provenance boundary of the ChatGPT files |
| `evidence/hho/` | 54 frozen files, `README.md`, `SHA256SUMS` | **new**: byte-identical copies of the upload |

- The two live summaries add no claim of their own. They restate register rows and HCG records.
- Where a summary and the register differ, the register governs.

## 3. Changes of scientific content since `hho-v0.1`

There is one addition and one re-typing. Nothing else changed in any claim, grade or review state.

**3.1 New row `HHO-NEG-NPL-JAC-C3F20`** — `[NEG]`, `[THM]`; CHECKED.

- **Statement.** For the C₃ × F₂₀ datum of `HHO-NEG-NPL-C3F20`, the class of the Jacobian-induced form on the χ-multiplicity space is [1], while the Brauer-tree neighbour has odd multiplicity 43.
- **Reason.** χ is trivial on F₂₀, so the multiplicity space lies in the pullback of H¹(C/F₂₀). There the cup form of C is 20 times that of C/F₂₀, and 20⁸ is a norm. `HHO-THM-SUPPORT` for (C/F₂₀, C₃) gives [1].
- **Dependencies.** `HHO-THM-SUPPORT`, `HHO-LEM-CUP-MORITA`, and the recorded dimension, signature and multiplicity. It uses no locality and no cup–polarization bridge.
- **Provenance.** The quotient-curve observation is ChatGPT's (Addendum 8 review, §4). The argument for the Jacobian reading was written by Claude on 11 Nov 2026 and checked by ChatGPT (PR #35, review `5857931712`).

**3.2 The withdrawn Neighbour Parity Law is typed by object.**

- The frozen record wrote "h_W" for a law whose numerical support was parabolic.
- The register now states that the law is refuted in both readings: the parabolic-cup reading by `HHO-NEG-NPL-C3F20`, and the Jacobian-induced reading by the new row.
- The RID `HHO-WD-CONJ-NPL` stays reserved.

## 4. Received inputs

### 4.1 HCG — the pin stays at `hcg-v0.2`

HCG published `hcg-v0.3` on 11 Nov 2026 (notice `pipes/HHO/20261111-HCG-v0.3-release.md`). **HHO does not re-pin in this release.**

- **Eleven of the twelve cited files are unchanged.** Of the twelve HCG files cited in the manifest §3.1, eleven have the same bytes at `hcg-v0.3` as at `hcg-v0.2`. These are the source dictionary and the ten `evidence/hcg/` files. HCG's notice states the same for the whole `evidence/hcg/` folder.
- **The ledger is the one file that differs.** `hcg/HCG_STUDY_LEDGER.md` is `276c93a3…` at `hcg-v0.2` and `fc03e837…` at `hcg-v0.3`. HHO keeps citing the v0.2 ledger.
- **The pending material is still pending.** Everything HHO depends on that was pending in HCG is still pending at `hcg-v0.3`: Δ27, with the locality theorem and the induced-period bound, and Δ28.
- **What a re-pin would bring.** `hcg-v0.3` adopts a new ledger, with Δ24–Δ26. HHO uses the ledger for the definitions of (L), (D), (H0)–(H4) and for the W5 results. Whether any of these readings changes in the v0.3 ledger has **not** been checked. A re-pin therefore needs that check, and it is left to a later HHO release.

The table of cited HCG sources is `records/hho/HHO_SOURCE_MANIFEST.md` §3.1, unchanged.

### 4.2 RTG

None.

### 4.3 Third-party sources

Unchanged from `hho-v0.1`: cited bibliographically only. No LIT-backed validation is claimed.

### 4.4 ChatGPT's files

The 21 ChatGPT-attributed files are **received copies** with verified byte identity. Their originals in the earlier ChatGPT session are **not available** and have not been authenticated (manifest §4.1). This is a recorded limit. It does not block the release.

## 5. Review corrections applied since the first drafts

| Correction | Where | Source |
|---|---|---|
| S1: G1–G10 are the (H)-scoped screening gates; G11 is a sufficient criterion for (L), which is outside (H); G12 is a use condition | `HHO_GATES.md` §2 | ChatGPT review `5855565170`; PR #38 |
| S2: the NPL is typed by object, and the Jacobian reading gets its own refutation | register Part C and B.3; `HHO_SUPPORT_RESULTS.md` §5.3 | same review; Claude's disposition in PR #35 |
| S3: the leaf lemma's hypotheses are stated where the lemma is restated | `HHO_SUPPORT_RESULTS.md` §5.1 | same review; PR #38 |
| E1: the PROPOSED states of the G₂₆-type witness and of the C₆ leaf test are visible in the calibration table | `HHO_GATES.md` §4 | same review; PR #38 |
| Credit for the quotient-curve observation; the summary's header names the result added on 11 Nov | register; `HHO_SUPPORT_RESULTS.md` | ChatGPT review `5857931712` |

## 6. Not part of this release

- **Any ACCEPTED claim, and any change of an existing review state.**
- **A re-pin to `hcg-v0.3`** (§4.1).
- **Authenticated originals of ChatGPT's files** (§4.4).
- **A re-check of the Part A proofs.** Part A restates the opening note at the states written there.
- **A comparison of every Part B claim with every Δ27 report.** The overlap check of `hho-v0.1` stands as it was: the opening note was read, and the delta log was searched by keyword.
- **A replay of every placed script.** Two were replayed (§8).
- **Any adopted scientific import or transfer to HCG or RTG.**
- **New research on P1.** It starts after this release.

Open items are listed in the register, Part D.

## 7. Adoption manifest

*To be completed at adoption*, at the content commit, after the publication step of §9.

## 8. Checks and decisions

| Check | Result | By |
|---|---|---|
| 54 placed files against the manifest hashes, and `sha256sum -c evidence/hho/SHA256SUMS` | 54/54 | Claude (re-hash) |
| Placed files against their upload sources, by Git blob identity | 54/54 | ChatGPT (PR #33, review `5855246909`) |
| Every RID used in the two live summaries exists in the register | pass | Claude (script); ChatGPT (review `5855565170`) |
| Every evidence path abbreviated in the register resolves to a placed file | pass | Claude (script) |
| Replay from the placed layout, with the HCG engines taken from `evidence/hcg/`: `f20_check.py`, `g616.py` | byte-identical output | Claude |
| The 12 HCG files of the manifest §3.1, compared at `hcg-v0.3` | 11 equal; the ledger differs, as expected | Claude (re-hash from the tagged blobs) |
| Other scientific computations re-run | **none** | — |

| Decision | By | Entry |
|---|---|---|
| Evidence placement | ChatGPT review `5855246909` (ACCEPT — EVIDENCE PLACEMENT ONLY); merged by the PI as PR #33 | merge `b2a066a` |
| Live summaries, with scoped corrections | ChatGPT reviews `5855565170` and `5857931712`; PR #38 reviewed and accepted by Claude; merged by the PI as PR #35 | merge `4683913` |
| New row `HHO-NEG-NPL-JAC-C3F20` recorded as CHECKED | owner sessions | review `5857931712` |
| Pin kept at `hcg-v0.2` | owner proposal in this record, §4.1 | *(part of the adoption decision)* |
| Co-owner review of this record | ChatGPT HHO owner session | *(pending)* |
| Adoption of `hho-v0.2` with the scope of §§1–6 | PI | *(pending)* |
| Publication | PI | *(pending)* |

## 9. Publication step (to be applied after the PI's adoption)

1. Status lines: the three `hho-v0.1` files and the two live summaries take the `hho-v0.2` adoption entry. The charter's governing edition becomes `hho-v0.2`.
2. `REGISTRY.md`, `hho` row: the governing edition becomes `hho-v0.2` with this record, and the layout names the two live summaries.
3. This record: "DRAFT" removed, §7 and §8 completed.
4. Hashes of every changed file are recomputed after the step and before the tag. Order: decision → release record → merge → tag (`CONVENTIONS.md` §2).

## 10. Pipe items handled with this release

| Item | Action |
|---|---|
| `pipes/HHO/20261111-HCG-v0.3-release.md` | dispositioned: accept. The notice is taken into §4.1; the pin stays at `hcg-v0.2`. |
