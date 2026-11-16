# HHO v0.5 — release record

**Status:** **ADOPTED** by the PI on 16 Nov 2026, 19:14 +03:00 (§8), as a register edition, in the text of draft r2 (approved payload commit `8b4151f`). Published by the publication commit of §10. **Governing edition from its tag:** `hho-v0.5`.

**Release:** fifth repository edition of the HHO study. If adopted, it supersedes `hho-v0.4` as the governing edition.

**Prepared by:** the Claude HHO owner session, on the PI instruction of 16 Nov 2026, 17:10 +03:00 ("önerin uygun onaylıyorum", in reply to a proposal with three parts: comparison note, register draft, PR for review then PI decision). **Review:** the ChatGPT HHO owner session (requested). **Adoption:** PI Mustafa Aksu.

## 1. What this release is

`hho-v0.5` is a **register edition** with two parts:
- the **re-pin of HCG** from `hcg-v0.2` to `hcg-v0.6`;
- four register rows and two open items for the **Witt boundary gate**, from session records already on `main` (PR #74, #76, #78, #80).

**What does not change:**
- No claim row becomes ACCEPTED.
- No row that existed in `hho-v0.4` is regraded or promoted (checked by script, §8).
- No new computation was run for this edition.

**Scope guard.** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist, and no statement about the Hodge conjecture. Severn's results stay CLAIMED. The Witt gate is a consistency condition between the parabolic-cup class and the boundary combinatorics. **It is not a test of (D) and not an obstruction to (D).**

## 2. Files of this edition

| File | Role | Change since `hho-v0.4` |
|---|---|---|
| `hho/HHO_CHARTER.md` | governance text | §5.1 (the HCG pin and what is adopted at it); status line and §3 at the publication commit |
| `hho/HHO_CLAIM_REGISTER.md` | the register | status line; reading rules; three evidence abbreviations (DSR, WG-P/R/C, DW/) and the two HCG ones restated; calibration line; B.4 (HCG labels, d = 10); **new section B.8** (four rows); Part D (two new open items, notes of two others) |
| `hho/HHO_GATES.md` | live summary | sources line; G4, G5, G6, G11 states; a row for the Witt gate among the local tools; the dimension table; the calibration rows of W5, the C₆ separator and the C₃ control |
| `hho/HHO_SUPPORT_RESULTS.md` | live summary | status line; the first sentence of §4 (locality at the pin) |
| `records/hho/HHO_SOURCE_MANIFEST.md` | source manifest | §3.1 at `hcg-v0.6`: ledger hash, states, the W5 certificate |
| `records/hho/HHO_HCG_REPIN_COMPARISON_CLAUDE.md` | session record of 16 Nov 2026 | **new**: the consumer comparison `hcg-v0.2` → `hcg-v0.5` → `hcg-v0.6` |
| `evidence/hho/d-witt/` | ten session-native scripts and outputs and `SHA256SUMS` | **new since `hho-v0.4`** (merged with PR #74, #76, #78, #80) |

**Session records on `main` that the new rows cite (not adopted as claims):**
- `HHO_D_SOURCE_READING_CLAUDE.md` and `HHO_D_WITT_GRAPH_REVIEW_CHATGPT.md`;
- `HHO_WITT_GATE_PREREGISTRATION_CLAUDE.md`, `HHO_WITT_GATE_RESULTS_CLAUDE.md` and `HHO_WITT_GATE_PR78_CHATGPT_REVIEW.md`.

## 3. Changes of scientific content since `hho-v0.4`

### 3.1 The HCG re-pin

The full table is in `records/hho/HHO_HCG_REPIN_COMPARISON_CLAUDE.md` §3. In short:
- **Only the HCG ledger changes.** Every other HCG file that HHO cites is byte-identical at `hcg-v0.2` and `hcg-v0.6`.
- **Inputs that were pending become adopted HCG results.** Locality, the induced bound, the d = 6 chain, Lemma E, the normal reflection subgroup, Lemma F, Theorem R and the d ≤ 14 corollary are now adopted HCG results, CHECKED (two AIs), with labels. The (H) of the register becomes an adopted HCG text (ledger §6.25).
  - **No HHO grade changes:** an HCG result gives no HHO grade by citation (charter §5.1).
  - The eight rows graded `[THM-cond: locality]` keep that grade. Their condition is now an adopted HCG `[THM]` whose cup reading (L2) is a named import.
- **One statement added to HHO's dimension table:** no datum at all for d = 10, besides d = 7, 8, 9, 11.
  - It was already in Δ27 add. 4 (ii); the `hho-v0.4` table omitted it.
  - **Correction to `HHO_D_SOURCE_READING_CLAUDE.md` §5,** which called it new in `hcg-v0.5`: it is new there only as adopted text.
- **Review states of HCG inputs that changed in `hcg-v0.3`:**
  - PO-4: THIRD-FAMILY CHECKED on the v1 text;
  - PO-6: CHECKED (two AIs) for the general statement, as a proof-path review;
  - W5 sub-claim of `HCG-ALG-E02`: THIRD-FAMILY CHECKED.

  The gate table names them. No HHO row changes.
- **Unchanged:** R1 (d ≥ 53) stays HHO's statement from NOTE and **pending in HCG** (HCG's OPEN 11 covers d ≥ 15). The C₆ separator, the C₃ control, NOTE and Δ28 stay pending.
- **Why `hcg-v0.6` and not `hcg-v0.5`:**
  - `hcg-v0.6` is HCG's governing edition.
  - For HHO's uses the two editions say the same: `hcg-v0.6` §6.26 states that it adds nothing on (L), PO-5 or PO-6/B2 (comparison §4).
  - The proposal the PI approved named `hcg-v0.5`; this was reported to the PI on 16 Nov 2026 before the draft was written.
  - Switching to `hcg-v0.5` changes only the tag name and the ledger hash.

### 3.2 B.8 — the Witt boundary gate (four rows)

| RID | Statement, in short | Grade | State |
|---|---|---|---|
| `HHO-COR-WITT-GATE` | nonsplit parabolic-cup class ⇒ w(T) = Σ_e dim V^{⟨g_e⟩} − Σ_v dim V^{H_v} ≤ 3 for every marking–tree pair realized as a boundary point of the specified Hurwitz component; split ⇒ ≤ 4 | `[THM-cond: (a) K-rational S-isotropy of W₀ at every realized boundary point; (b) admissible semistable-cover dual-graph description of W₀]` | CHECKED (the implication only) |
| `HHO-NUM-WITT-C6` | three C₆ data, all 2,027,025 trees: max 3 for class [2], 4 for class [1] | `[NUM]` | CHECKED (two implementations) |
| `HHO-NUM-WITT-PLANAR` | planar family, N = 20: W5 4/4 (certificate tree 102 − 98 = 4); G(6,1,6) P1–P3 3/3, Q0/Q2 4/4 | `[NUM]` | CHECKED (two implementations) |
| `HHO-NUM-WITT-PLANAR-SINGLE` | W6, W7 4/4; three C₃ × F₂₀ tuples of class [5]: max 0; 27 split C₃ × F₂₀ tuples: max 0 to 4 | `[NUM]` | PROPOSED (one implementation) |

**New open items:**
- `HHO-OPEN-WITT-SOURCE`: a primary source for inputs (a) and (b);
- `HHO-OPEN-WITT-CONSTANCY`: why w is tree-independent on the reflection data.

**Open items restated (notes only):**
- `HHO-OPEN-T2`: the overlap with HCG's OPEN 11, and the observation that the recorded (D) method cannot apply to nonsplit data;
- `HHO-OPEN-RECONCILE`: (H) is now an adopted HCG text; the d = 7 comparison is still open.

**Provenance and limits.**
- **The formula and its check.** The exact sequence behind w(T) was derived by ChatGPT. Claude re-derived it for this draft: apply Hom_G(V, −) to the equivariant cochain sequence of the connected dual graph. That functor is exact in characteristic 0, and no element of a node stabilizer exchanges the two branches, because they lie over different base vertices.
- **The bound.** Isotropy plus Landherr was stated by Claude and accepted by ChatGPT in the review of PR #74.
- **Inputs (a) and (b) were not checked against any source.** HCG's `HCG-COR-BOUNDARY-WITT` covers the laminar case only, and it is cited for the Landherr step only.
- **The planar run was preregistered** (Git order checked by the co-owner). The preregistration was not reviewed before the run.
- **Independent replay covers W5 and G(6,1,6)**, by exact ℚ(ω) and monomial methods. W6, W7 and C₃ × F₂₀ have one implementation.
- **The recorded classes were not recomputed.**
- **"max over trees = Witt index" is not claimed.** The split C₃ × F₂₀ data refute it as a general rule.
- **No third-family check and no human refereeing** exists for any new row.

## 4. Received inputs

### 4.1 HCG — the pin moves to `hcg-v0.6`

- Pin: tag `hcg-v0.6` (object `42a203ee6189d35f97b6097476b79a6d8b50c72e`, commit `34251e9b2ee110db34426b79fa0e26929d961563`).
- Ledger SHA-256: `b1e928f5ae555d688a18bb1046be7626796f2a07935b6ff81a0fc934036b14cb`.
- Notices: `pipes/HHO/20261116-HCG-v0.6-release.md` is open. Its disposition line ("accept", with this record) is set at adoption. The notices for `hcg-v0.3` to `hcg-v0.5` are already dispositioned.

### 4.2 HCG — the answer on Severn's polarized factor

The answer is unchanged. HCG's notice of 16 Nov 2026 states that `hcg-v0.6` does not change it. `HHO-LEM-B2` and `HHO-OPEN-SUPPORT-TRANSFER` are untouched.

### 4.3 RTG

None.

### 4.4 Third-party sources

None added. The sources named for inputs (a) and (b) were not read (`HHO-OPEN-WITT-SOURCE`).

## 5. Review corrections applied

Co-owner review: PR #81, review `5922469673` at `329556b`, "ACCEPT AS A DRAFT REGISTER EDITION, WITH TWO SCOPED WORDING/PROVENANCE FIXES BEFORE PI ADOPTION". Both fixes are applied in r2. Neither changes a computed value, a grade class or a review state of an `hho-v0.4` row.

| Id | Review point | Applied |
|---|---|---|
| R1 | The quantifier of the Witt gate must run over marking–tree pairs **realized as boundary points of the specified Hurwitz component**. The C₆ row must distinguish full braids from pure braids. | `HHO-COR-WITT-GATE`: the claim quantifies over realized pairs, and the realizability is part of (b); grade wording and state as proposed by the review ("CHECKED (the implication only)"). `HHO-NUM-WITT-C6`: the braid convention is stated, and the realized trees are referred to (b). `HHO-NUM-WITT-PLANAR`: the same reference to (b). The gate row of `hho/HHO_GATES.md` and §3.2 here follow. |
| R2 | The status header of the source manifest must distinguish the draft and be updated at publication, with its hash in the manifest of §7 | In r2 the header said that §3.1 is the draft for `hho-v0.5`. At the publication commit (§10) it is replaced, the draft sentence of §3.1 is removed, and the hash is in §7. |

**Kept unchanged on purpose:** `HHO_D_SOURCE_READING_CLAUDE.md`. Its "new at v0.5" for d = 10 and its "every ordering lies in one braid orbit" (§4.5) are corrected here and in the register, not rewritten in the note.

## 6. Not part of this release

- **Any ACCEPTED claim**, and any regrading or promotion of a row that existed in `hho-v0.4`.
- **A test or proof of (D)**, and any obstruction for P1.
- **The source check of inputs (a), (b)** of the gate, and of Severn's definitions (`HHO-OPEN-SUPPORT-TRANSFER`).
- **An independent replay of W6, W7 and C₃ × F₂₀.**
- **The observation on HCG ledger §6.23** ("Nothing is claimed for d ≥ 10 in this edition", which reads as stale since `hcg-v0.5`). It is HCG's to decide. A notice to `pipes/HCG/` is offered to the PI, not filed.
- **Any import or transfer to HCG or RTG.**

## 7. Adoption manifest

**Status: ADOPTED (2026-11-16).** SHA-256 of the bytes in the publication commit (§10).

| File | Role | SHA-256 |
|---|---|---|
| `hho/HHO_CHARTER.md` | charter (governance text; no scientific claim) | `7429d5c1b6d09a0088b7966b1f8c1f1105620efb253cbe25f0d99c58cb2560ce` |
| `hho/HHO_CLAIM_REGISTER.md` | claim register (adopted as a register; no row ACCEPTED) | `55b85bb0b95f8b0e8121ef28728913e860408f79edcbd082e72167df976f8e04` |
| `hho/HHO_GATES.md` | live summary: gates, bounds, calibration objects | `4abf34c845c41e7c4c14178f7ebd203a70ddfd8560acd5f42ea40113ce16fd00` |
| `hho/HHO_SUPPORT_RESULTS.md` | live summary: support results, bridges, positive-defect primes | `468152b1a4c92516062b358d16537d1a4d028598bd2c93f66cc6d9c4e9c71906` |
| `records/hho/HHO_SOURCE_MANIFEST.md` | source manifest (§3.1 at `hcg-v0.6`) | `e42a26f584761bf6fc6e66ab347158a52d5de7bbb3a8ccfd1be21e15d60d48cb` |
| `evidence/hho/SHA256SUMS` | index of the 54 placed evidence files (unchanged since `hho-v0.2`) | `e042d035534ca134ffed143eba41d97895dbe3de83ec5e6fec91db9ca77a5ae6` |
| `evidence/hho/b1/SHA256SUMS` | index of the three B1 files (unchanged since `hho-v0.3`) | `340c812af34e3b47ed37f47b6eeb6e4024e2f90dbde7d1876fe9d777a87d8fac` |
| `evidence/hho/posdefect/SHA256SUMS` | index of the ten positive-defect files (unchanged since `hho-v0.4`) | `705de5115a7157ed55ab9276ce03dbace93eec1f3010edfaa29a41ea239bb3af` |
| `evidence/hho/d-witt/SHA256SUMS` | index of the ten Witt-graph scripts and outputs (new in this edition) | `1cec53e7bb5bd0a6b5ee1eff17c3f8cc4e7aab65568b086a03907b17911ef68f` |
| `evidence/hho/README.md` | guide to the evidence folder | `9fed0f76ef2d75b8cfda28fe2ac5e96169ad71ad40b04b346b698dbf761139fa` |
| `upload/hho/SHA256SUMS` | index of the 57 uploaded source files (unchanged since `hho-v0.1`) | `50417fca3c82ad7a487d0c986047ecb002d86aa5f5cbffe087672df33d60b410` |
| `records/hho/HHO_HCG_REPIN_COMPARISON_CLAUDE.md` | session record: HCG consumer comparison | `e656342e0856223d8665672f39d0b40056446c784ba4d05f219abb91555d3516` |
| `records/hho/HHO_D_SOURCE_READING_CLAUDE.md` | session record: (D) source reading, Witt bound, dual-graph formula | `bf318beb4d1e5c2607364ea75dc37d5a58383a4cee18da1866074f2fe01c4c18` |
| `records/hho/HHO_D_WITT_GRAPH_REVIEW_CHATGPT.md` | session record: review of the dual-graph formula | `6b978fb0be1f4c543cd71245a10f1f8de0bb99178b28ef4c55c4b861a2d77b59` |
| `records/hho/HHO_WITT_GATE_PREREGISTRATION_CLAUDE.md` | session record: preregistration of the planar run | `ddb91f9c7904618202d26bd39f7b883b1eed276a0573e5bd77c77003a320902d` |
| `records/hho/HHO_WITT_GATE_RESULTS_CLAUDE.md` | session record: results of the planar run | `ee0707f232a2d96af5e9d96a8e5d19fe943c3900223f86ffb0d79212ccf3b32b` |
| `records/hho/HHO_WITT_GATE_PR78_CHATGPT_REVIEW.md` | session record: independent W5 and G(6,1,6) checks | `a919772f22bd792409291cafe78fe16166ab7793022c8649092ec49481b58a90` |
| `pipes/HHO/20261116-HCG-v0.6-release.md` | received notice, dispositioned | `9d6643cb2c85f7dc85ef415d3c0f7f1c71f30b4ccf70b338a79a890ccda3dd10` |

`REGISTRY.md`: only the single line of the `hho` study is hashed, with its line feed, because other studies change the same file: `2b0d608367d2df7f529efd4d72b4ffa5b4c7a0e15a160a8927a60c4f06a163a2`.

- The evidence files are adopted as **evidence as it stands**, not as claims.
- The six session records are listed because the new rows cite them. They are not adopted as claims; the register rows carry the grade and the state.
- HCG material that is pending at the pin stays pending for HHO.
- The SHA-256 of this record is stated in the tag message, not here.

## 8. Checks and decisions

**Checks run for this draft.**

| Check | Result | By |
|---|---|---|
| Every claim row of `hho-v0.4` outside Part D is present and byte-identical (45 rows) | pass | Claude (script) |
| New RIDs: exactly six (four claim rows, two open items); none deleted; Part D notes changed for HHO-OPEN-T2 and HHO-OPEN-RECONCILE only | pass | Claude (script) |
| Every RID used in the two live summaries and in this record exists in the register | pass | Claude (script) |
| Every HCG RID cited in the HHO texts occurs in the ledger at `hcg-v0.6`, or is a former HHO RID (`HCG-HHO-…`), or is stated as pending (the C₆ separator and the C₃ control) | pass | Claude (script) |
| Byte identity of the HCG files of manifest §3.1 at `hcg-v0.2`, `hcg-v0.5`, `hcg-v0.6` | pass (comparison §2) | Claude |
| `sha256sum -c` for the four evidence indexes | pass: 54, 3, 10, 10 files | Claude |
| `python3 tools/sat_check.py` | 1 error, 2 warnings, the same as on `main`: the error is the `hho-v0.4` tag message (§9); the warnings concern COIL records | Claude |
| Computations | none for this edition | — |

**Decisions.**

| Decision | By | Entry |
|---|---|---|
| Run of Steps 1 and 2 of the (D) reading | PI, 16 Nov 2026 | "birleştirmeyi yaptım 1 ve 2 yi koşalım" |
| Merge of PR #78 (with PR #80) as a session record | PI | merge commit `3cbf063` |
| Preparation of the `hho-v0.5` draft: comparison note, register draft, PR for review, then PI decision | PI, 16 Nov 2026, 17:10 +03:00 | "önerin uygun onaylıyorum" |
| Co-owner review of this record | ChatGPT HHO owner session | PR #81, review `5922469673` at `329556b`: accept as a draft register edition with R1, R2 (§5); supports the pin `hcg-v0.6`; recommends option (i) for the `hho-v0.4` tag |
| `hho-v0.4` tag defect (§9) | PI, 16 Nov 2026, 18:45 +03:00 | "tag değişmeden kalsın" — the tag stays unchanged: option (i) |
| Adoption of `hho-v0.5`, including the pin `hcg-v0.6`, with the scope of §§1–6 | PI, 16 Nov 2026, 19:14 +03:00 | "evet benimsiyorum" — yes, I adopt it; the answer to the question whether the PI adopts `hho-v0.5` with the pin `hcg-v0.6`. The text adopted is draft r2, commit `8b4151f9…` |
| Publication | PI | the PI merges PR #81 with a merge commit and creates the annotated tag with the five lines of `CONVENTIONS.md` §2 |

## 9. A defect of the `hho-v0.4` tag, found while checking this draft

`tools/sat_check.py` reports: "hho-v0.4: tag message lacks the line(s): Approved payload commit, Publication merge commit, PI adoption (CONVENTIONS.md §2)".

- The `hho-v0.4` message has "Publication commit" and "Merge commit" instead of the required lines, and no "PI adoption" line.
- The rule took effect before `hho-v0.4`. Its list of exempt tags ends at `hho-v0.3`.
- The tag command was supplied by the Claude HHO session. The defect is that session's error; the content of the release is not affected.

**Options (the PI decides):**
- **(i)** Leave the tag as it is. Record the missing values here; this record would then be their written source:
  - Approved payload commit: `e2d509674f8836f5ab4b001264f54fef2a69e4cd`, the publication commit, which the tag message names "Publication commit";
  - Publication merge commit: `26e8ccae0d3c117fe66c925a0d14b26b83538266`;
  - PI adoption: 14 Nov 2026, 23:27 +03:00, recorded in `HHO_v0.4_RELEASE_RECORD.md` §8.
- **(ii)** Re-create the annotated tag `hho-v0.4` on the same commit with a corrected message. This replaces a published tag object, and anyone who fetched the old one keeps it.

**Decision: option (i)** (PI, 16 Nov 2026, 18:45 +03:00; §8). The tag object `0783844fdb5a75d83725453204bf518fbf153b0b` stays on `26e8ccae…`. The values above are the written source for the three missing fields. This is a documented historical deviation: the `sat_check` error on `hho-v0.4` stays visible and is not counted as a passing check. No checker exception is introduced. The `hho-v0.5` tag message will carry all lines of the template of `CONVENTIONS.md` §2.

## 10. Publication step (applied on 16 Nov 2026)

The sequence is: PI adoption decision → **one** publication commit → PI merge → annotated tag.

The publication commit contains all of the following and nothing else:

1. **Status lines of the five live files:** `hho/HHO_CHARTER.md`, `hho/HHO_CLAIM_REGISTER.md`, `hho/HHO_GATES.md`, `hho/HHO_SUPPORT_RESULTS.md` and `records/hho/HHO_SOURCE_MANIFEST.md`.
   - In the charter, §3 is brought up to date: the governing edition is `hho-v0.5`, and one bullet describes this edition.
   - In the manifest, the draft sentence at the head of §3.1 is replaced by "Pinned with `hho-v0.5`."
   - No other text changes in these files.
2. **`REGISTRY.md`, `hho` row:** the governing edition is `hho-v0.5`, with this record and the pin `hcg-v0.6`.
3. **`pipes/HHO/20261116-HCG-v0.6-release.md`:** dispositioned (§11).
4. **This record:** "DRAFT" removed; §7, §8, §10 and §11 completed.

`main` was at `3cbf063` when the draft branch was made, and it has not moved since. The hashes of §7 are those of the files in the publication commit itself. This record cannot contain its own hash; the tag message states it.

## 11. Pipe items handled with this release

| Item | Action |
|---|---|
| `pipes/HHO/20261116-HCG-v0.6-release.md` | dispositioned: accept. The notice is taken into §4.1; the pin moves to `hcg-v0.6`. |
