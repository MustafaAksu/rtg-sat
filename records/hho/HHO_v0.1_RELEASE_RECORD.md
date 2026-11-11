# HHO v0.1 — release record

**Status:** **ADOPTED by the PI on 11 Nov 2026 as a register edition** (§8). Publication tag: `hho-v0.1`, created by the PI on the merge commit of the pull request that carries this record (PR #28).

**Release:** first repository edition of the HHO study.

**Prepared by:** the Claude HHO owner session. **Review:** the ChatGPT HHO owner session. **Adoption:** PI Mustafa Aksu.

## 1. What this release is

- `hho-v0.1` gives HHO a governed home in `rtg-sat`: a charter, a claim register and a source manifest.
- It is a **register edition**. It fixes what HHO claims, under which hypotheses, at which evidence grade and review state, and where the evidence is.
- **No claim row becomes ACCEPTED through this release.** Every row keeps the review state written in the register.
- It contains no new mathematics. Every statement in the register comes from the frozen records listed in §3 and §4.

**Scope guard.** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist, and no statement about the Hodge conjecture. Severn's results stay CLAIMED.

## 2. Files of this edition

| File | Role |
|---|---|
| `hho/HHO_CHARTER.md` | governance text: scope, (H), first target P1, grades, identifiers, interfaces, safeguards. It carries no scientific claim. |
| `hho/HHO_CLAIM_REGISTER.md` | the register: Part A (opening note), Part B (HHO conversation), Part C (withdrawn and corrected), Part D (open), Part E (answer to HCG) |
| `records/hho/HHO_SOURCE_MANIFEST.md` | intakes, sessions, cited sources, not-available list, rename map, file table |
| `upload/hho/SHA256SUMS` | index of the 57 uploaded source files |

Their hashes are in the adoption manifest, §7.

## 3. HHO's own sources

- **The upload of 10 Nov 2026**, `upload/hho/` (PR #16): 57 files, byte-for-byte.
  - 20 files are the Claude HHO session's own. Among them is the append-only review file `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` (952 lines, SHA-256 `2d58916317f3a0a8a0ae33e908dd7757b2ff9a40504526240f956e5896706f0d`), with its 15-step prefix-hash chain in `records/hho/HHO_MIGRATION_PLAN.md` §3.1.
  - 37 files were received from the PI: ChatGPT's reviews, checkers and packages; relays; and two HCG engines.
- **The opening note of 3 Nov 2026**, written in the HCG conversation and stored at `evidence/hcg/hho-track/` (SHA-256 `6a7a8053b5590ff2b6693a0cfe5f750af7fbe3036fc0961a10a29cabf65eadb7`). Its scientific custody is with HHO. It is cited there and is not copied.

**Not yet done.** The frozen files are not yet placed in `evidence/hho/`. Evidence pointers in the register name `upload/hho/` paths. Placement and the live result files are planned for the next edition (§6).

## 4. Received inputs

### 4.1 HCG — pinned at `hcg-v0.2`

Tag `hcg-v0.2`, annotated, on commit `543d09387d6d5df79d38fcd549090350f994d4e3`. The full table with paths and hashes is `records/hho/HHO_SOURCE_MANIFEST.md` §3.1.

| HCG object | HCG state | How HHO uses it |
|---|---|---|
| Session ledger v0.2 (`276c93a3…`) | **adopted** in HCG; no claim row ACCEPTED | definitions of (L), (D), (H0)–(H4); W5 results |
| Source dictionary (`7d2736ef…`) | HCG record | where the labels are stated |
| Locality theorem `HCG-THM-PARABOLIC-DISC-LOCALITY` | **pending** (Δ27) | dependency of every row graded `[THM-cond: locality]` |
| Induced-period bound `HCG-THM-INDUCED-PERIOD-BOUND` | **pending** (Δ27) | dependency of the (D)-failure statements |
| Δ27 addenda 1–17; Δ28 | **pending** | provenance of Part A |
| Engines `generic_engine.py`, `cyclic_disc_claude.py` | the first is cited by the adopted ledger; the second is pending | used unchanged by HHO scripts |

- Citation does not upgrade. A pending HCG item stays pending, and an HHO row that depends on it is conditional.
- Re-pinning to a later HCG tag is an HHO decision in a later HHO release.

### 4.2 RTG

None. HHO uses no RTG result. The `REGISTRY.md` field "RTG inputs" is set to `none` with this release (§9).

### 4.3 Third-party sources

Cited bibliographically only (`records/hho/HHO_SOURCE_MANIFEST.md` §3.2). Nothing of theirs is stored. No LIT-backed validation is claimed.

- Severn's primary texts were **not available** to the HHO sessions.
- Shephard–Todd and Cohen 1976 are quoted, not re-proved.
- CTblLib 1.3.7 under GAP 4.12.1 was reported retrospectively by the PI for the runs of 4 Nov 2026.

## 5. Changes made when moving the records into the register

No statement was changed in meaning. The following were changed in form.

| Change | Detail |
|---|---|
| Identifiers | Session-local RIDs `HCG-HHO-…` and the labels of the HHO conversation are mapped to `HHO-<KIND>-<NAME>` (manifest §5). Withdrawn RIDs are reserved. |
| Grades | The conversation's mixed tags (`SESSION THM`, `ALG CHECKED`, …) are split into an evidence grade and a review state. Rows that depend on pending HCG results are graded `[THM-cond: …]`. This is a stricter reading than "SESSION THM"; it lowers no review state. |
| Notation | `HHO-THM-F20`: the representation σ = ω ⊗ ρ₄ is fixed and the local exponents are k_j (the conversation wrote σ = ω^k ⊗ ρ₄). |
| Obligations (a)–(d) of the support line | (a) and (b) are lemmas with RIDs; (c) is not needed for the Jacobian-induced polarization; (d) is `HHO-OPEN-SUPPORT-TRANSFER`. |
| Re-derivations | The (D) budget, the d = 6 synthesis and the d = 7 exclusion of Addenda 12–14 are entered as re-derivations of HCG Δ27 addenda 1–4, without RID (register B.4). |
| Language | The register and charter are in English. PI decisions are quoted in Turkish as given, with an English gloss. Relayed ChatGPT messages in Turkish stay unchanged in `upload/hho/`. |
| First target | P1 is the opening note's "dominance versus the local class product". The earlier choice "d = 8" and its replacement are both recorded (charter §1). |

## 6. Not part of this release

- **Placement of frozen files** in `evidence/hho/`, and the live result files (support theorems, gates and bounds).
- **ChatGPT's own originals.** Its files are present only as received copies.
- **Any new scientific result**, and any change of review state.
- **A comparison of every Part B claim with every Δ27 report.** The overlap check was made by reading the opening note and by keyword search of the delta log.
- **A re-check of the Part A proofs.** Part A restates the opening note at the states written there.
- **Any adopted scientific import or transfer to HCG or RTG.** The answer filed in `pipes/HCG/` (§10) is a communication. It transfers no result and is no adopted use.

Open items are listed in the register, Part D.

## 7. Adoption manifest

**Status: ADOPTED (2026-11-11).** SHA-256 of the bytes at the **content commit** `7890a79a0a70250f45a88c7bcc0136da27adc796`. This manifest-only commit follows it and changes no other file. If any listed file changes after this, the hashes are recomputed before the tag.

| File | Role | SHA-256 |
|---|---|---|
| `hho/HHO_CHARTER.md` | charter (governance text; no scientific claim) | `dd647253b1a74cc8e4c45bbcace2e2ac8e3b33fea585ca7b525c6d0827ce6878` |
| `hho/HHO_CLAIM_REGISTER.md` | claim register (adopted as a register; no row ACCEPTED) | `668124e0d55032f76d68cbf819533c063d5322f83557150104db0bc92e1037dd` |
| `records/hho/HHO_SOURCE_MANIFEST.md` | source manifest | `80f88fe9c1c2bfffa9a1b3a1de154b5fb13ed277d17ef9bedb10e5835d600f49` |
| `upload/hho/SHA256SUMS` | index of the 57 uploaded source files | `50417fca3c82ad7a487d0c986047ecb002d86aa5f5cbffe087672df33d60b410` |
| `REGISTRY.md` | `hho` row: layout, governing edition, RTG inputs, transfer rule | `e7a18ad0c61304acbb8ca80f82d4544835f98348d8f80b7dfcade2bb725188e8` |
| `pipes/HHO/20261110-HCG-v0.2-release-and-citation-map.md` | received item, dispositioned | `489036c423462457d634f84e9170bbf09ede7e1921035f5acaa9662a8f2f440c` |
| `pipes/HHO/20261110-HCG-provenance-of-hho-track-claims.md` | received item, dispositioned | `497b60046cbd69ad40a0a6e167b27f2b24657214bda4feaf94f948d5eb6a9218` |
| `pipes/HHO/20261110-HCG-question-hypothesis-lists.md` | received item, dispositioned | `857a8e2aca746b170fc88e2e9b9b9bca6f9f25024dd28244e2a7de04ae6842e1` |
| `pipes/HCG/20261110-HHO-answer-hypothesis-lists.md` | answer filed to HCG (a communication, not a transfer) | `ca2626cff478b3f92a16918b67f26b23e86598026ca5497dc80fbce0f16d1cc6` |

The uploaded source files are adopted as **evidence as it stands**, not as claims. HCG material that is pending in HCG stays pending.

The SHA-256 of this record itself is stated in the tag message, not here.

## 8. Checks and decisions

| Check | Result | By |
|---|---|---|
| `upload/hho/SHA256SUMS`, 57 files | 57/57 | Claude (re-hash from the files) |
| Manifest file table against `upload/hho/SHA256SUMS` | 57/57 | Claude (re-hash); ChatGPT (cross-check of the two lists, not a re-hash) |
| HCG hashes in the manifest against `evidence/hcg/SHA256SUMS`, the ledger and the dictionary at `hcg-v0.2` | 12/12 | Claude; ChatGPT (dictionary hash) |
| Prefix-hash chain of the review file, 15 entries | 15/15 | Claude; ChatGPT (from its own copy) |
| Every `upload/hho/` path named in the register exists | pass | Claude |
| Scientific computations re-run for this release | **none** | — |

| Decision | By | Entry |
|---|---|---|
| Upload rule, conventions, first target | PI, 10 Nov 2026 | `records/hho/HHO_MIGRATION_PLAN.md` §7; charter §1 |
| Safeguards HHO-SG-7, -8, -9 | PI, 10 Nov 2026 | accepted with a proviso (charter §6) |
| Co-owner review of batch 1 | ChatGPT HHO owner session | PR #26, reviews `5842650405` (ACCEPT WITH SCOPED CHANGES) and `5843881129` (ACCEPT, at `e117f75`) |
| To issue v0.1 now, before evidence placement | PI, 10 Nov 2026, 18:18 +03:00 | "şimdi v0.1 çıkarabiliriz. merge işlemleri tamam." — "we can issue v0.1 now; the merges are done." |
| Co-owner review of this record | ChatGPT HHO owner session | PR #28, review `5844451467` at `04a5ca1`: ACCEPT AS A DRAFT RELEASE RECORD, with two nonblocking clarifications. Both are applied: §6 (the pipe answer is no transfer) and the closing of the migration note (below). |
| Adoption of `hho-v0.1` with the scope of §§1–6 | PI, 11 Nov 2026, 09:29 +03:00 | "PI olarak ben; hho-v0.1'i yalnızca kayıt sürümü kapsamında benimsiyorum. Charter, iddia kaydı ve kaynak manifesti bu kapsamda kabul edilmiştir. Hiçbir bilimsel iddia ACCEPTED statüsüne yükseltilmez; HCG sonuçları benimsenmiş sayılmaz ve Severn sonuçları CLAIMED kalır." — As PI, I adopt hho-v0.1 as a register edition only. The charter, the claim register and the source manifest are accepted within that scope. No scientific claim is raised to ACCEPTED; HCG results are not thereby adopted; Severn's results stay CLAIMED. |
| Publication | PI, same message | "Yayın commit'i hazırlansın; merge ve tag işlemlerini ben yapacağım." — The owner session prepares the publication commit; the PI merges and creates the tag. |
| Closing of the migration note | by its own §Status ("it changes by commit until the first HHO release, then it is closed") | `records/hho/HHO_MIGRATION_NOTE.md` is closed with this release. Its text is not changed. The migration plan stays a record of batch 0. |

## 9. Publication step (applied on 11 Nov 2026, after the PI's adoption)

1. Status lines of `hho/HHO_CHARTER.md`, `hho/HHO_CLAIM_REGISTER.md` and `records/hho/HHO_SOURCE_MANIFEST.md`: "draft for `hho-v0.1`" becomes the adoption entry.
   - In the charter, three further sentences that described the state before the release are brought up to date: the governing edition (§3, two bullets) and the registry field for RTG inputs (§5.2).
   - No other text changes in the three files.
2. `REGISTRY.md`, `hho` row:
   - layout names `hho/HHO_CHARTER.md` and `hho/HHO_CLAIM_REGISTER.md`;
   - governing edition becomes `hho-v0.1` with this record;
   - RTG inputs become `none`;
   - the transfer rule records that HHO → HCG needs an HCG owner disposition, PI adoption and an HCG release.
3. This record: "DRAFT" removed, §7 and §8 completed.
4. Before the step, `main` at `0c21155` (COIL v0.6, PR #30) was merged into the release branch. That merge changed the `coil` row of `REGISTRY.md` and no HHO file.
5. Hashes of every changed file were recomputed after the step (§7). Order: decision → release record → merge → tag (`CONVENTIONS.md` §2).

## 10. Pipe items handled with this release

| Item | Action |
|---|---|
| `pipes/HHO/20261110-HCG-v0.2-release-and-citation-map.md` | dispositioned: accept; followed in the manifest §3.1 |
| `pipes/HHO/20261110-HCG-provenance-of-hho-track-claims.md` | dispositioned: accept; carried in the register, Part A and Part C |
| `pipes/HHO/20261110-HCG-question-hypothesis-lists.md` | dispositioned: accept; answered in the register, Part E, and by `pipes/HCG/20261110-HHO-answer-hypothesis-lists.md` |
