# HHO — migration plan (Claude owner session)

**To:** PI (Mustafa); ChatGPT HHO owner session
**From:** Claude, owner session of the "HHO Hurwitz–Hodge obstruction research" conversation (RTG Dyadic project)
**Date:** 2026-11-10
**Replies to:** `records/hho/HHO_MIGRATION_NOTE.md` (merged in PR #14, `main` at `4bf99b4`)
**Status:** plan with the PI decisions of 10 Nov 2026 recorded in §7. Items not listed there remain proposals. Nothing in this plan is a scientific adoption.

---

## 1. Access audit (checked on 2026-11-10)

| Item | Result | How checked |
|---|---|---|
| `MustafaAksu/rtg-sat` read | OK. Public; `main` at `4bf99b4` ("Merge pull request #14 … claude/hho-migration-note"). | anonymous `git clone` |
| `records/hho/HHO_MIGRATION_NOTE.md` | Present, SHA-256 `44c5843ad07902db4c7d5a8f31e9b2a9bd68bf5da4967a38a14b479b62c50964`. The copy the PI pasted into this conversation has the same text; it differs only in line endings and the final newline. | `sha256sum`, `diff` after CR stripping |
| `REGISTRY.md` row `hho` | Present. Owners are named. Layout is "to be set in the HHO charter". Governing edition: "accepted at chat level only, no tag". RTG inputs: "not set". LIT: "not yet". | file read |
| `hho/`, `hcg/`, `pipes/HHO/`, `pipes/HCG/` | Empty directories. | `ls` |
| `upload/hho-sources` | **Does not exist yet.** | `git ls-remote` |
| HHO tags | None. | `git tag` |
| `.gitattributes` | `* -text`. There is no EOL conversion, so byte hashes survive. | file read |
| Push permission for this session | OK. First request was refused by the session's permission layer; granted on the PI's instruction on 2026-11-10. This plan is the first push (`claude/hho-batch0-plan`). | tool result; this PR |
| `gh pr list` | GraphQL is blocked in this environment. The REST API is available once the repository is attached. | tool result |

**F1 — push access. CLOSED.** Granted on 2026-11-10. This session pushes only to `claude/hho-*` branches.

**F2 — ephemeral workspace (urgent).** Claude's own HHO artefacts exist only in this session's cloud container, and the container is reclaimed after inactivity. They are bundled now with a `SHA256SUMS` file (§3.1). The bundle should reach `upload/hho-sources` soon. If the container is lost before then, the bundle sent to the PI is the only copy.

## 2. Upload rule (question to the PI)

The note (§4) says *the PI uploads the originals*. The COIL precedent (`COIL_SOURCE_MANIFEST.md`, PI decision of 6 Nov 2026) used *the owner session's own artefacts, uploaded by the owner session*. Proposal for HHO:

- each owner session uploads **its own** artefacts under `upload/hho/owner-session-outputs/<claude|chatgpt>/`;
- received HCG inputs go under `upload/hho/received-inputs/hcg/`;
- the PI uploads **PI-machine outputs** (GAP and Windows runs) under `upload/hho/pi-uploads-received/`;
- each group carries its own `SHA256SUMS`.

Claude's bundle is laid out this way already. **PI decision needed** (Q1).

## 3. Inventory held by this session

### 3.1 Claude's own artefacts (bundle `HHO_OWNER_OUTPUTS_CLAUDE_20261110.zip`)

| File | SHA-256 | Kind | What it is |
|---|---|---|---|
| `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` | `2d58916317f3a0a8a0ae33e908dd7757b2ff9a40504526240f956e5896706f0d` | frozen (append-only) | support-lemma review + Addenda 1–14, 952 lines |
| `HHO_G34_BLOCKS_v0_1.g` | `3722966617f672c09d76bd3bb7034982a297704dd7fbfcbc13e1d0d0c6ab38ac` | code | GAP block / Brauer-tree extraction for G₃₄ (r3) |
| `HHO_C6_LEAF_TEST_v0_1.py` | `30395da0f12e3c5d3a700a3c091c8c34d8a5eefacad95d120023dc5fed34aa57` | code | C₆ leaf-criterion falsification test (run by the PI) |
| `s.py` | `93e7c2b4e7a9b05e68e31c503aa8fb641886f9ca763e949aac096c03a9561848` | code | early Hilbert-symbol check (Addendum 0/1) |
| `sweep.py` | `094780674a48c3548f3ada4eb0267709cbca9fa02d70c2058ee146ff6f0d1156` | code | exhaustive C₆ r = 10 sweep (A8.2) |
| `c6_sweep_r10_out.txt` | `7f39c878294343dac51848abea8faba58f65a0308e516eb07340f57bbd5b8615` | output | A8.2 |
| `c6_sweep_r10.json` | `3f965fc5b1c002f714083810371b6d8763366dc555e9d09c605ded00c501a1d4` | output | A8.2 |
| `c3s3.py` | `c78ef8601cd56b75aae9750057d1af14c4e2b466c3345023b58f2a821dffb089` | code | C₃×S₃ defect-zero test (A8.4) |
| `c3s3_out.txt` | `81d571d8732605965f36620a8b59373529f347a5518726370b3e735318a0cb0a` | output | A8.4 |
| `c3s3_all.py` | `81ebcd4b7e5e8c879f3530ec78902353cc5c7d349b21d74a3a23042dcae338c1` | code | A8.4, all determinants |
| `c3s3_all_out.txt` | `c45be4b8e3a298be026ccbf6393a07c60bc528967efde94bb28bf190e6185a59` | output | A8.4 |
| `f20_check.py` | `4a449e11f09f76c2ea9574d226dd5e141e9e7c01b2767e30a254f976e9681820` | code | C₃×F₂₀ NPL counterexample check (A9.1) |
| `f20_check_out.txt` | `182617f7af8b3974ba7a744f31ba036098d349315b5270f487a023674ff11adb` | output | A9.1 |
| `f20_faithful.py` | `0012b3961b9bfadcdf5f04cea6af827f7f963c7c5869684bc9fd5ae24fce5a8e` | code | faithful F₂₀ run, r2; its A10.4 interpretation is retracted (A11.1), the output stands |
| `f20_faithful_out.txt` | `6a3b4623ec5cc755d4c93fdb9c74686831a549f136193236aa34bf2546e61e01` | output | A10.4 / A11.2 input tuples |
| `dbg.py` | `fbf635dc13f4b1a80443112ff05c62d2bbe4d418978d5df99aefd5758b051f6c` | code | A10.4 dimension-label debug |
| `a4_direct.py` | `cd548934c63af78e688d0697cd23da05fe602d09de3df9bb4a0d28d03616bc9d` | code | direct A4-form Gram run (A11.2) |
| `a4_direct_out.txt` | `8d54d6622be6cef8a5568df5bee2285f780834d446c23bd3c1eae0b9b9ba6f89` | output | A11.2 |
| `g616.py` | `b07a560a751a3dd3871fb0397efc8dfe97776beb678160ba07f7b56f27baff7a` | code | G(6,1,6) d = 6 budget witnesses (A12.3) |
| `g616_out.txt` | `0a8d98558539ee514e7e77094742f93b3a91338dc0e3452cbf774da030286fdf` | output | A12.3 |

All hashes above are taken from the bundle's `SHA256SUMS` (SHA-256 `d81071f5fc6321ffc328ecabb627b261be9b02ac1a24f9d5776f6b3614a03b2a`, 22 entries). Bundle SHA-256: `afcabb4f6e9c26e2e03451c09e29bc582581c1f45cd50f356333a9cb947ceb47`.

**Prefix-hash chain of the frozen review file.** All values were recomputed from the file today, and each matches the hash recorded at its addendum.

| Lines | SHA-256 of prefix | Edition |
|---|---|---|
| 80 | `5c70ef22fbcd99173434a30da3ff7fbf1e69e2c0002243a81f5fe7fd248d9597` | initial review |
| 123 | `e7059f78e1695cabdbe41d084de09f3aa41d8b26c9eb6fd5d2f240060f4b0ea2` | + Add. 1 |
| 172 | `cba601da2d1c8f4bb9406c5293b08566a0eb21d777ab40210d5df7d4699c5b3f` | + Add. 2 |
| 205 | `e2a2d708b936710645bb50085f4ab8c89bcdb177608e675c03009dd92275676b` | + Add. 3 |
| 237 | `16475d3b133e459e9357203ce7707e0b071a48d07b34d978d2cc546067cb6455` | + Add. 4 |
| 293 | `05ddafc22f18bcd5af0790d3c5e6ec4c06ca89c4cf35291906a3c750f60abc35` | + Add. 5 |
| 342 | `1ad8f1a412f7f93b5f32c7913614a3d9e53c116e3a4a96172acf392919418011` | + Add. 6 |
| 402 | `751c83446226db814e6b3ad82e1eea693bb3b3df958eafabdc52ace292dec7fe` | + Add. 7 |
| 479 | `14b1d67c2efef6994c75ed827a16632f46ed7dd63246780fda3ab8bccddaaa03` | + Add. 8 |
| 555 | `486288f5cc68ebd08c1c835e8bf5f12dfdcd8af45f2523b1c9a7b74fe0a7bc44` | + Add. 9 |
| 643 | `593ca8a82325d38aa5ea20d5534dd6378216e3c0ba6785de6a0ee440993d5ec9` | + Add. 10 |
| 728 | `77252c32b8994cacc801a2f0358222d977310273db599148c29b045e4ea8c850` | + Add. 11 |
| 825 | `5931034dde275dca9959cf2e797fdc4a5bdbd1a50ec404126cc0db000dea00b3` | + Add. 12 |
| 890 | `266a783f0f08b88a9a8e2c77c6018bb46c09e9f3d72e2fa350645bce052e8f07` | + Add. 13 |
| 952 | `2d58916317f3a0a8a0ae33e908dd7757b2ff9a40504526240f956e5896706f0d` | + Add. 14 (final) |

**One irregularity to record.** Addendum 3 was first appended with a heading line damaged by shell quoting, and then corrected in place before being sent. The 205-line hash above is that of the corrected file as sent. No earlier sent edition was altered.

### 3.2 Received inputs held by this session (not Claude's results)

| File | SHA-256 | Origin | Label |
|---|---|---|---|
| `generic_engine.py` | `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505` | HCG conversation (written by Claude in HCG); uploaded by the PI on 4 Nov | HCG input, not adopted, not an HHO result |
| `cyclic_disc_claude.py` | `da76a25f57817fbeaf2b6deb749cda76cdefb5c8d59ec2d4b871a2778cf2afa9` | HCG conversation; uploaded by the PI on 4 Nov | HCG input, not adopted, not an HHO result |

ChatGPT's HHO files that reached this session (reviews, proof sketch, checkers, ZIPs) are **ChatGPT's artefacts**. ChatGPT's session should upload its own copies. Claude can cross-check their hashes against those recorded in the addenda (§A*.0 tables).

### 3.3 Not available in this session

- **Superseded drafts.** The superseded revisions of Claude's scripts were overwritten in place:
  - `HHO_G34_BLOCKS_v0_1.g` r1 (`cab7acfe…`) and r2 (`a56019e2…`);
  - `f20_faithful.py` r1 and its r1 output.
  Their hashes are recorded only where the addenda state them. They are not reconstructed.
- **PI-machine outputs.** These were seen in this session only as pasted text:
  - `HHO_G34_BLOCKS_v0_1_out.txt` (attachment SHA `ae7459c2…`);
  - `HHO_G34_REFLECTION_NEIGHBOR_CW_v0_2_out.txt` (`e365da61…`);
  - `HHO_C6_LEAF_TEST_v0_1_out.txt` (`bdc73ebb…`).
  The PI holds the files.
- **HCG-side HHO track.** All of it was produced in the HCG conversation, and this session holds none of it:
  - the opening note v0.1, Δ28, gate catalogue G1–G12;
  - claim register R1 (d ≥ 53), G4A/G4B, T-PRIME, 2XB-REDUCTION, G4C, 2XB-SCAN, LSEP, T2;
  - safeguards HHO-SG-1…6;
  - the "add. 17" witness ("(L) ⇒ split" false at class-datum level).
- **HCG source texts used as dependencies.**
  - The locality proof note `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md`; only its review (`41bc9997…`) was seen.
  - The induced-period review (`050c8504…`).
  - `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (`276c93a3…`).
  - `HCG_DSN_v0_3_PENDING_DELTAS` (`1fb44251…`).
  - The canonical (L)/(D)/(H0)–(H4) texts.
- **Primary third-party texts.** Severn v1/v2 primary texts (`hexagon:2610.00387v1/v2`), Cohen 1976 and the CTblLib version are not held. They are to be cited bibliographically only.

## 4. Points to reconcile before the charter

- **F3 — two claim lines.** The HCG-side register (for example R1 "d ≥ 53") and this conversation's results do not yet have a common hypothesis list. This conversation's results are:
  - d ≤ 5: (D) impossible;
  - d = 6: (D) ⇒ [1];
  - d = 7: (D) impossible.

  The two lines may concern different hypothesis sets. The charter must state each claim's exact hypotheses before the claims share one register. Neither line overrides the other.
- **F4 — retractions to carry.** These are carried forward as withdrawn items in the register, and their RIDs are never reused:
  - HHO-CONJ-NPL, refuted by the C₃×F₂₀ counterexample;
  - A9.3.4, prior art `HCG-COR-D6-NONSPLIT-NOGO`;
  - A10.4 "30/30 split", retracted;
  - A8.2 count 54 → 53.
- **F5 — dependency labels.** Every HHO theorem that uses HCG locality, the induced-period factorization, or Shephard–Todd/Cohen must name that dependency at each restatement (HHO-SG-2).

## 5. Proposed conventions for the charter

- **One RID namespace: `HHO-<KIND>-<NAME>`.** KIND ∈ {THM, LEM, COR, CONJ, OPEN, NUM, ALG, NEG, WD}. `HCG-HHO-…` RIDs are mapped to `HHO-…` in the manifest's rename table. Withdrawn RIDs stay reserved.
- **Two separate axes.**
  - *Evidence grade:* `[THM]`, `[THM-cond: <dependency>]`, `[ALG]`, `[NUM]`, `[CONJ]`, `[OPEN]`, `[NEG]` (counterexample or negative control).
  - *Review state:* PROPOSED, CHECKED (two AIs), THIRD-FAMILY CHECKED, ACCEPTED (PI).
  Neither is an RTG grade.
- **Notation, fixed once.**
  - K = ℚ(√−3) = ℚ(ω), ω² + ω + 1 = 0.
  - Discriminant class [det h] ∈ ℚ^×/N(K^×).
  - Signature (p,q) of the parabolic Hermitian form.
  - Locality: Δ(g) = det(h₀|E)/det((1−g)|E), with E = im(1−g).
  - (L), (D), (H) as defined in the received HCG/Severn texts, cited by hash once available.

## 6. Batch order (each batch is its own PR on `claude/hho-batch<n>-*`)

| Batch | Content | Needs |
|---|---|---|
| 0 | this plan in `records/hho/` | this PR |
| 1 | `hho/HHO_CHARTER.md`, `hho/HHO_CLAIM_REGISTER.md`, `records/hho/HHO_SOURCE_MANIFEST.md` | Q1–Q3 decided; HCG-side track files uploaded by ChatGPT or the PI |
| 2 | support-lemma line: frozen review file and ChatGPT reviews to `evidence/hho/frozen/`; live `hho/HHO_SUPPORT_THEOREMS.md` stating current results only | uploads (§2) |
| 3 | gate catalogue and dimension bounds: `hho/HHO_GATES.md`, with the (D) budget, d = 6 / d = 7 results and the HCG-side G1–G12 | HCG-side files |
| 4 | scripts, GAP data, outputs to `evidence/hho/code`, `evidence/hho/outputs`; received HCG engines to `evidence/hho/received/` | uploads |
| — | `records/hho/HHO_v0.1_RELEASE_RECORD.md`, then the ChatGPT review, then PI adoption, then the tag `hho-v0.1` | batches 1–4 merged |

## 7. Questions for the PI — decided on 2026-11-10

PI decisions, given in the HHO conversation on 10 Nov 2026 (verbatim, Turkish): "1 sen yükle / 2 kabul ediyorum / 3 önerin uygun". The PI numbered the three questions that were still open, in order: Q1, Q3 and Q4. Q2 had been closed before.

1. **Q1 — upload rule. DECIDED:** the owner session uploads its own artefacts. Done in PR #16 (`upload/hho-sources`, commit `516400d`; `upload/hho/SHA256SUMS` SHA-256 `50417fca3c82ad7a487d0c986047ecb002d86aa5f5cbffe087672df33d60b410`, 57 files). The files the PI sent into the conversation are included as `pi-uploads-received/`.
2. **Q2 — push access. CLOSED** (granted on 2026-11-10).
3. **Q3 — RIDs and grades. ACCEPTED:** the single `HHO-` namespace and the two-axis grade/state convention of §5. They will be declared in the charter (batch 1).
4. **Q4 — first target P1. ACCEPTED as proposed:** "(L)+(D) ⇒ [1] at d = 8".

**Working order set by the PI** (same message): first settle the study fully in the repository; scientific work resumes once the co-owner session is settled too.

---

## 8. Update after `hcg-v0.2` (10 Nov 2026, afternoon)

HCG is now in this repository: tag `hcg-v0.2`, with `main` at `543d093` when read. This session read the following files there and nothing else:

- `hcg/HCG_CHARTER.md` §5;
- `records/hcg/HCG_v0.2_RELEASE_RECORD.md`;
- the outline of `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md`;
- `evidence/hcg/README.md` and `evidence/hcg/SHA256SUMS`;
- `evidence/hcg/hho-track/HCG_HURWITZ_HODGE_OBSTRUCTION_OPENING_NOTE_v0_1.md`, in full.

### 8.1 What HHO can now cite from `rtg-sat` (path and SHA-256 at `hcg-v0.2`)

| HHO need | File under `evidence/hcg/` unless stated | SHA-256 | HCG state |
|---|---|---|---|
| Definitions of (L), (D), (H0)–(H4); the HHO "(H)" as a different object | `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md`; `hcg/HCG_STUDY_LEDGER.md` | ledger `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` | ledger **adopted** (`hcg-v0.2`) |
| HHO opening note v0.1: scope, (H), gates G1–G12, R1–R3, programme P1–P6, HHO-SG-1…6, initial claim register | `hho-track/HCG_HURWITZ_HODGE_OBSTRUCTION_OPENING_NOTE_v0_1.md` | `6a7a8053b5590ff2b6693a0cfe5f750af7fbe3036fc0961a10a29cabf65eadb7` | HHO-track source evidence; custody HHO; Δ28 pending |
| HHO framework note (ChatGPT) | `received/10041afe-HCG_HURWITZ_HODGE_OBSTRUCTION_FRAMEWORK_SESSION_v0_1.md` | `aeb6f9e778f354af2c67b841dc6dda673eab0378aae9a75c5f1c2a34cf5eafd7` | received; pending |
| Δ27 (addenda 1–17), Δ28 | `ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` | `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d` | **pending**; not part of `hcg-v0.2` |
| Locality theorem: proof note | `received/68e831c3-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md` | `0ec385584bbaba4b6408572b3f4423dc38c3884e60fbf304f5a49c61392114cb` | pending (Δ27) |
| Locality theorem: Claude review | `nonsplit8/H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md` | `41bc9997328cbc74a592ba9a899fd6cc30eb6e71656cc284c591ff05ac1878ee` | pending (Δ27) |
| Induced-period bound: proposal | `received/20505e68-HCG_INDUCED_PERIOD_DIMENSION_BOUND_PROPOSED_v0_1.md` | `03199b80ad92692db91cc3ce7d3014c425d263191bc44ac844fd7706ae2b306e` | pending (Δ27) |
| Induced-period bound: review and reflection dichotomy | `nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` | `050c8504edfc73af13d935c8d27925d71fd0ed846395a4bb51cb94976768ec7f` | pending (Δ27) |
| d = 6 screen | `nonsplit8/H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md` | `de619ee49b8c9d90819e3ae977d889b3ac9783e84aedcda121e07516f55578b1` | pending (Δ27) |
| Engine `generic_engine.py` | `h4sel/p2p3/generic_engine.py` | `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505` | same bytes as the copy HHO received |
| Engine `cyclic_disc_claude.py` | `nonsplit8/cyclic_disc_claude.py` | `da76a25f57817fbeaf2b6deb749cda76cdefb5c8d59ec2d4b871a2778cf2afa9` | same bytes as the copy HHO received |

**Consequences for §3.3.**
- The HCG-side HHO track and the HCG dependency texts are no longer "not available". They are cited from `evidence/hcg/` and are not copied into `evidence/hho/`.
- **Pinning rule for HHO v0.1.** Cite the tag `hcg-v0.2`, with path and hash. Label every Δ27/Δ28 item "placed at `hcg-v0.2`, pending in HCG, not adopted". Only the ledger v0.2 is an adopted HCG edition.
- **Still not available:** Severn's primary texts and deposit (third party; LIT); ChatGPT's own originals; and the PI-machine output files of this conversation.

### 8.2 Overlap found: this conversation re-derived parts of the HCG-side track

The opening note was written on 3 Nov, before this conversation started. It already records the following (states as written there):

- G4 locality and G4a inert-prime criterion;
- G5 induced-period bound;
- G6 **Theorem R: a complex reflection in Γ ⇒ split**;
- HCG-LEM-NONSPLIT8-NORMAL-REFL;
- **R1: nonsplit under (H) ⇒ d ≥ 53** (CHECKED by two AIs, source-conditional);
- R2 calibration objects, including a real G₂₆-type witness with (L) and class [2];
- R3 (monomial data from order-2 reflections with the standard form are split).

This conversation did not hold those files. Its Addenda 12–14 are therefore **independent re-derivations of special cases**, weaker than R1. They are the (D) budget, the d = 6 synthesis and the d = 7 exclusion. In the HHO claim register they are entered as re-derivations and cross-checks, with R1/G5/G6 as the prior records. They are not entered as new results.

**What this conversation adds.** None of the following appears in the opening note; whether any of it is in Δ27 addenda 1–17 has **not** been checked yet:

- the Jacobian-lattice support line (evaluation embedding, cup-derived Morita form, defect-zero support bound);
- the tame-unimodular local lemma;
- the local lattice/cokernel identity;
- the rank-one law;
- the refuted NPL with its counterexample;
- the C₃×F₂₀ [5^t] family (nonsplit at an inert prime p ≥ 5);
- the G(6,1,6) witnesses.

Each is to be compared against Δ27 in batch 1 before it gets a register row.

### 8.3 Q4 (first target) needs a new PI look

The PI accepted "(L)+(D) ⇒ [1] at d = 8" as P1 on this session's proposal. That proposal was made without knowledge of R1. Under R1 (source-conditional), every d ≤ 52 is already covered, so "d = 8" is not an open target under (H). The opening note's own P1 is "dominance versus the local class product: a d-independent obstruction under (H)", with P1a–P6 behind it. Its PI-decision field is blank.

**Request to the PI:** withdraw or restate Q4. This session's suggestion is to adopt the opening note's P1 as HHO's first target. Until the PI decides, the charter will carry P1 as "to be decided".
