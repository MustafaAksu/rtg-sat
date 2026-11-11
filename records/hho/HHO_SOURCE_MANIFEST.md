# HHO — source manifest

**Status of this file:** adopted by the PI on 11 Nov 2026 as the source manifest of `hho-v0.1` (`records/hho/HHO_v0.1_RELEASE_RECORD.md`). It is a record of sources and hashes. It adopts no source and no claim. **Changed after `hho-v0.1`** (11 Nov 2026): §6 records the placement of 54 files in `evidence/hho/`; no hash and no source is changed. The governing text is the one at the tag until the next release.

A hash certifies byte identity. It does not certify correctness, publication rights or review state.

## 1. Intakes

| Intake | Where | Files | Uploaded by | Authority |
|---|---|---|---|---|
| HHO upload of 10 Nov 2026 | `upload/hho/` (PR #16, merge commit `8eb533c`); `upload/hho/SHA256SUMS` has SHA-256 `50417fca3c82ad7a487d0c986047ecb002d86aa5f5cbffe087672df33d60b410` | 57 | Claude HHO owner session | PI decision of 10 Nov 2026 ("1 sen yükle"), `records/hho/HHO_MIGRATION_PLAN.md` §7 |

No other intake exists yet. ChatGPT's own originals have not been uploaded.

## 2. Sessions

| Session | Conversation | Role | What it produced |
|---|---|---|---|
| Claude HHO owner | "HHO Hurwitz–Hodge obstruction research" (RTG Dyadic project), 3–10 Nov 2026 | owner | the append-only review file, scripts, outputs |
| ChatGPT HHO owner | the same line, relayed by the PI | owner | proof sketch, reviews, checkers, packages |
| PI | — | PI | runs on his machine (GAP, Windows), relays, decisions |
| Claude and ChatGPT HCG owners | "Hodge Conjecture" conversation, up to 3 Nov 2026 | owners of HCG | the HHO opening note and Δ27/Δ28, kept in `evidence/hcg/` |

## 3. Cited, not stored in `evidence/hho/`

### 3.1 HCG, at tag `hcg-v0.2`

The tag is annotated; it points to commit `543d09387d6d5df79d38fcd549090350f994d4e3`. Paths are under `evidence/hcg/` unless stated. Only the ledger is adopted in HCG. Every other row is **placed, pending in HCG, not adopted**.

| Used for | Path | SHA-256 | HCG state |
|---|---|---|---|
| Definitions of (L), (D), (H0)–(H4); W5 results; PO-6 | `hcg/HCG_STUDY_LEDGER.md` | `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` | adopted (`hcg-v0.2`); no claim row is ACCEPTED |
| Where those labels are stated | `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md` | `7d2736efc9f49db336ef6279f7a9bd65f7071bd584e149fa08e145989d8f4419` | HCG record; not a theorem and not an HHO result |
| HHO opening note v0.1: (H), gates G1–G12, R1–R3, P1–P6, HHO-SG-1…6, initial register | `hho-track/HCG_HURWITZ_HODGE_OBSTRUCTION_OPENING_NOTE_v0_1.md` | `6a7a8053b5590ff2b6693a0cfe5f750af7fbe3036fc0961a10a29cabf65eadb7` | HHO-track source evidence; custody HHO; Δ28 pending |
| HHO framework note (ChatGPT) | `received/10041afe-HCG_HURWITZ_HODGE_OBSTRUCTION_FRAMEWORK_SESSION_v0_1.md` | `aeb6f9e778f354af2c67b841dc6dda673eab0378aae9a75c5f1c2a34cf5eafd7` | pending (Δ27 add. 16) |
| Δ27 with addenda 1–17; Δ28 | `ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` | `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d` | pending |
| Locality theorem: proof note (ChatGPT) | `received/68e831c3-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md` | `0ec385584bbaba4b6408572b3f4423dc38c3884e60fbf304f5a49c61392114cb` | pending (Δ27 add. 2) |
| Locality theorem: review (Claude) | `nonsplit8/H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md` | `41bc9997328cbc74a592ba9a899fd6cc30eb6e71656cc284c591ff05ac1878ee` | pending (Δ27 add. 2) |
| Induced-period bound: proposal (ChatGPT) | `received/20505e68-HCG_INDUCED_PERIOD_DIMENSION_BOUND_PROPOSED_v0_1.md` | `03199b80ad92692db91cc3ce7d3014c425d263191bc44ac844fd7706ae2b306e` | pending (Δ27 add. 4) |
| Induced-period bound: review; reflection dichotomy (Claude) | `nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` | `050c8504edfc73af13d935c8d27925d71fd0ed846395a4bb51cb94976768ec7f` | pending (Δ27 add. 4–5) |
| d = 6 screen | `nonsplit8/H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md` | `de619ee49b8c9d90819e3ae977d889b3ac9783e84aedcda121e07516f55578b1` | pending (Δ27 add. 1–2) |
| Engine | `h4sel/p2p3/generic_engine.py` | `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505` | cited by the adopted ledger |
| Engine | `nonsplit8/cyclic_disc_claude.py` | `da76a25f57817fbeaf2b6deb749cda76cdefb5c8d59ec2d4b871a2778cf2afa9` | pending (Δ27) |

The Claude HHO session read the opening note in full, and the Δ27 entry, the HCG charter §5, the release record and the dictionary in outline. It did not re-check the proofs behind these files.

### 3.2 Third-party sources (bibliographic only)

| Source | Identifier | Held by HHO? |
|---|---|---|
| Severn, Weil classes for ℚ(√−3) | `hexagon:2610.00386`, `hexagon:2610.00387` (v1, v2) | **not available** to the HHO sessions; CLAIMED |
| Shephard–Todd classification | as given in the Magma Handbook, *Construction of Finite Complex Reflection Groups* | quoted through ChatGPT's reading |
| A. M. Cohen, *Finite complex reflection groups*, Ann. Sci. ÉNS 9 (1976), §§2.12–2.13 | numdam `ASENS_1976_4_9_3_379_0` | quoted through ChatGPT's targeted reading; not opened by Claude |
| GAP Character Table Library (CTblLib) | tables `6_1.U4(3).2_2`, `6.U6(2)M6`, `12_1.U4(3)` | data used; CTblLib 1.3.7 under GAP 4.12.1 on the PI's machine (reported by the PI on 10 Nov 2026, retrospectively; the runs were made on 4 Nov 2026). This is the same CTblLib version that HCG gate G10 records. |
| Matsumoto–Sasaki–Takayama–Yoshida (1993), structure of G₃₄ | cited by ChatGPT | not opened by Claude |
| D. Taylor, *Reflection subgroups of complex reflection groups* (2025) | cited by ChatGPT for the single reflection class of G₃₄ | not opened by Claude |
| Classification inputs of gate G10 | Hiss–Malle 2001 with 2002 corrigenda; GT08; GT12; Katz–Tiep §16 | as recorded in HCG Δ27; not opened in the HHO conversation |

No LIT-backed validation is claimed.

## 4. Not available

- **Superseded script revisions**, overwritten in place: `HHO_G34_BLOCKS_v0_1.g` r1 and r2; `f20_faithful.py` r1 with its output.
- **PI-machine output files** as files: `HHO_G34_BLOCKS_v0_1_out.txt` (its text is held as the relay `a4512a2f-attachment.txt`), `HHO_G34_REFLECTION_NEIGHBOR_CW_v0_2_out.txt` (SHA-256 reported by the PI: `e365da61e70ab11c5540bcdb3866b5e0c9c2b301e7acb57d21e27339de16187d`), `HHO_C6_LEAF_TEST_v0_1_out.txt` (reported: `bdc73ebb2a5d1dbc117d99770ef8c42d075cb00540ca91925ec04e247dfd2368`). The last two were seen only as text pasted into the conversation.
- **ChatGPT files that were not attached** to the conversation: its GAP script `HHO_G34_REFLECTION_NEIGHBOR_CW_v0_2.g`, its Addendum 10 and Addendum 12 review packages, and its own originals in general.
- **Severn's primary texts.**

### 4.1 ChatGPT-attributed received copies — source-access boundary (11 Nov 2026)

| Material | Verified custody and byte identity | Original-session status |
|---|---|---|
| 21 ChatGPT-attributed files in `evidence/hho/received/chatgpt/` | **RECEIVED COPY — SHA256 VERIFIED** against `upload/hho/pi-uploads-received/`; the corresponding 21 source and placed Git blobs match. Listed in `evidence/hho/SHA256SUMS`. | **ORIGINAL SESSION SOURCE — UNAVAILABLE**. The old ChatGPT HHO session's own originals were not fetched or independently authenticated. |
| 12 relayed message files in `evidence/hho/received/relays/` | PI-relayed text received through `upload/hho/pi-uploads-received/`; the corresponding 12 source and placed Git blobs match and are indexed in `SHA256SUMS`. | Relays are not independently verified transcripts of the inaccessible source session. |

This review could not access the old HHO ChatGPT conversation to extract source files directly. File hashes establish the identity of the **received bytes**, not that those bytes were obtained independently from the original ChatGPT session. No missing file has been reconstructed, no received file is relabelled as an authenticated original, and no earlier review status is upgraded. The absent originals remain an explicit bounded provenance limitation; they are **not** treated as an automatic blocker for preparing the next HHO register edition. Scientific adoption and any source-dependent acceptance remain separate decisions.

## 5. Identifier rename map

| Session-local RID (opening note §7) | HHO RID |
|---|---|
| HCG-HHO-R1 | HHO-THM-R1 |
| HCG-HHO-G4A | HHO-LEM-G4A |
| HCG-HHO-G4B | HHO-COR-G4B |
| HCG-HHO-G4C | HHO-LEM-G4C |
| HCG-HHO-T-PRIME | HHO-LEM-T-PRIME |
| HCG-HHO-2XB-REDUCTION | HHO-LEM-2XB-REDUCTION |
| HCG-HHO-2XB-SCAN | HHO-NUM-2XB-SCAN |
| HCG-HHO-LSEP | HHO-NEG-LSEP |
| HCG-HHO-T2 | HHO-OPEN-T2 |

| Label used in the HHO conversation | HHO RID |
|---|---|
| HHO-HYP-SUPPORT; HHO-COR-NO-INERT-GROUP-PRIMES | HHO-THM-SUPPORT |
| HHO-ALG-INTEGRAL-ISOTYPIC | HHO-LEM-ISOTYPIC |
| HHO-HYP-SUPPORT-MORITA | HHO-LEM-MORITA |
| HHO-HYP-SUPPORT-TRANSFER; obligations (a), (b), (c), (d) | (a) HHO-LEM-EVAL; (b) HHO-LEM-CUP-MORITA; (c) not needed for the Jacobian-induced polarization; (d) HHO-OPEN-SUPPORT-TRANSFER |
| HHO-CONJ-NPL | HHO-WD-CONJ-NPL (withdrawn; reserved) |
| HHO-LOCAL-SUPPORT | no RID; restatement of locality with HHO-LEM-G4A |
| HHO-Q-LOCAL-CANCEL | answered locally by HHO-LEM-LOCAL-LENGTH; the open part is HHO-OPEN-LOCAL-EVEN |
| HHO-OPEN-DEFECT-LOCAL | HHO-OPEN-POSDEFECT-GLUE |

RIDs of the form `HCG-…` without `HHO` are HCG's and are not renamed.

## 6. File table (57 files in `upload/hho/`)

"Place" is where an unchanged copy now stands (placed on 11 Nov 2026; 54 files; index `evidence/hho/SHA256SUMS`). Three files are deliberately not placed; the column says why. The upload in `upload/hho/` stays as it is.

| Path in `upload/hho/` | SHA-256 | Origin | Kind | Content | Place |
|---|---|---|---|---|---|
| `owner-session-outputs/claude/HHO_C6_LEAF_TEST_v0_1.py` | `30395da0f12e3c5d3a700a3c091c8c34d8a5eefacad95d120023dc5fed34aa57` | Claude HHO session (own) | code | C₆ leaf-criterion test runner | evidence/hho/code/ |
| `owner-session-outputs/claude/HHO_G34_BLOCKS_v0_1.g` | `3722966617f672c09d76bd3bb7034982a297704dd7fbfcbc13e1d0d0c6ab38ac` | Claude HHO session (own) | code | GAP: blocks and Brauer tree of G₃₄ (revision r3) | evidence/hho/code/ |
| `owner-session-outputs/claude/HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` | `2d58916317f3a0a8a0ae33e908dd7757b2ff9a40504526240f956e5896706f0d` | Claude HHO session (own) | frozen record | append-only review file with Addenda 1–14 (952 lines) | evidence/hho/frozen/ |
| `owner-session-outputs/claude/a4_direct.py` | `cd548934c63af78e688d0697cd23da05fe602d09de3df9bb4a0d28d03616bc9d` | Claude HHO session (own) | code | direct A4-form Gram computation | evidence/hho/code/ |
| `owner-session-outputs/claude/a4_direct_out.txt` | `8d54d6622be6cef8a5568df5bee2285f780834d446c23bd3c1eae0b9b9ba6f89` | Claude HHO session (own) | output | direct A4-form results, 40 tuples | evidence/hho/outputs/ |
| `owner-session-outputs/claude/c3s3.py` | `c78ef8601cd56b75aae9750057d1af14c4e2b466c3345023b58f2a821dffb089` | Claude HHO session (own) | code | C₃×S₃ test, (4,4) rows | evidence/hho/code/ |
| `owner-session-outputs/claude/c3s3_all.py` | `81ebcd4b7e5e8c879f3530ec78902353cc5c7d349b21d74a3a23042dcae338c1` | Claude HHO session (own) | code | C₃×S₃ test, all rows | evidence/hho/code/ |
| `owner-session-outputs/claude/c3s3_all_out.txt` | `c45be4b8e3a298be026ccbf6393a07c60bc528967efde94bb28bf190e6185a59` | Claude HHO session (own) | output | C₃×S₃ test, all rows | evidence/hho/outputs/ |
| `owner-session-outputs/claude/c3s3_out.txt` | `81d571d8732605965f36620a8b59373529f347a5518726370b3e735318a0cb0a` | Claude HHO session (own) | output | C₃×S₃ test | evidence/hho/outputs/ |
| `owner-session-outputs/claude/c6_sweep_r10.json` | `3f965fc5b1c002f714083810371b6d8763366dc555e9d09c605ded00c501a1d4` | Claude HHO session (own) | output | C₆ sweep, data | evidence/hho/outputs/ |
| `owner-session-outputs/claude/c6_sweep_r10_out.txt` | `7f39c878294343dac51848abea8faba58f65a0308e516eb07340f57bbd5b8615` | Claude HHO session (own) | output | C₆ sweep, text | evidence/hho/outputs/ |
| `owner-session-outputs/claude/dbg.py` | `fbf635dc13f4b1a80443112ff05c62d2bbe4d418978d5df99aefd5758b051f6c` | Claude HHO session (own) | code | debug script for the r1 dimension label | evidence/hho/code/ |
| `owner-session-outputs/claude/f20_check.py` | `4a449e11f09f76c2ea9574d226dd5e141e9e7c01b2767e30a254f976e9681820` | Claude HHO session (own) | code | C₃×F₂₀ NPL counterexample check | evidence/hho/code/ |
| `owner-session-outputs/claude/f20_check_out.txt` | `182617f7af8b3974ba7a744f31ba036098d349315b5270f487a023674ff11adb` | Claude HHO session (own) | output | NPL counterexample check | evidence/hho/outputs/ |
| `owner-session-outputs/claude/f20_faithful.py` | `0012b3961b9bfadcdf5f04cea6af827f7f963c7c5869684bc9fd5ae24fce5a8e` | Claude HHO session (own) | code | faithful C₃×F₂₀ search (revision r2); its quotient is not the ψ-class, see HHO-WD-F20-ALLSPLIT | evidence/hho/code/ |
| `owner-session-outputs/claude/f20_faithful_out.txt` | `6a3b4623ec5cc755d4c93fdb9c74686831a549f136193236aa34bf2546e61e01` | Claude HHO session (own) | output | 40 tuples; the printed classes are superseded by `a4_direct_out.txt` | evidence/hho/outputs/ |
| `owner-session-outputs/claude/g616.py` | `b07a560a751a3dd3871fb0397efc8dfe97776beb678160ba07f7b56f27baff7a` | Claude HHO session (own) | code | G(6,1,6) witnesses | evidence/hho/code/ |
| `owner-session-outputs/claude/g616_out.txt` | `0a8d98558539ee514e7e77094742f93b3a91338dc0e3452cbf774da030286fdf` | Claude HHO session (own) | output | G(6,1,6) witnesses | evidence/hho/outputs/ |
| `owner-session-outputs/claude/s.py` | `93e7c2b4e7a9b05e68e31c503aa8fb641886f9ca763e949aac096c03a9561848` | Claude HHO session (own) | code | early Hilbert-symbol check | evidence/hho/code/ |
| `owner-session-outputs/claude/sweep.py` | `094780674a48c3548f3ada4eb0267709cbca9fa02d70c2058ee146ff6f0d1156` | Claude HHO session (own) | code | C₆ r = 10 sweep | evidence/hho/code/ |
| `pi-uploads-received/0213d5f1-attachment.txt` | `835bdd0cebfec0fd36ffae83b2aa4455ae71f73c12511cc55cebf621484621c8` | PI relay | relay | ChatGPT message: review decision on Addendum 2 | evidence/hho/received/relays/ |
| `pi-uploads-received/06df848d-attachment.txt` | `0b3a35d893fd320f9ffb6ad545dc1af9850893c981357744562b21d3a32e1ca4` | PI relay | relay | ChatGPT message: assessment of Addendum 11 | evidence/hho/received/relays/ |
| `pi-uploads-received/0ea67bf5-HHO_SUPPORT_LOCAL_SYMBOL_CHECK_v0_1.py` | `04498c739089836f839f74898fd6b5f48eb694ec7b81071689e77e9bc5be6d3c` | ChatGPT, via PI | code | ChatGPT checker | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/1202abd0-independent_f20_locality.py` | `b5cea19db07ae6619a66495001590917dd203e5ee4cbd94591a066fff64d230f` | ChatGPT, via PI | code | ChatGPT checker | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/24d5a358-HHO_D7_REFLECTION_NORMALIZER_REVIEW_v0_1.zip` | `a8b5dd7e6699e634e1eff19568d5756e6201a5d60b22677e90d7688664c17980` | ChatGPT, via PI | package | ChatGPT review package | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/261c3351-attachment.txt` | `a0aaf5ac0983ee524d5b78b1722c16ee5075c68a8cc31c793066a2828fcde994` | PI relay | relay | ChatGPT message: d = 7 result (to Addendum 13) | evidence/hho/received/relays/ |
| `pi-uploads-received/2d4746c5-attachment.txt` | `5874a560e87cafda966d84ce7df352871a6afe02b24cc389bd8b9ee098b28595` | PI relay | relay | ChatGPT message: review of Addendum 5 | evidence/hho/received/relays/ |
| `pi-uploads-received/376737bb-HHO_ADDENDUM3_CHATGPT_LOCAL_GLOBAL_REVIEW_v0_1.md` | `fb82af9c2e30075c4a91adaaefa961d227a63f4e254679199cd993f7b382492c` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/3f4ace53-HHO_SUPPORT_ADDENDUM1_CHATGPT_SCOPED_REVIEW_v0_1.md` | `64626e5046140b28e72028cfc1244246d72379ba1065e99fdf75d86ba014ea00` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/55ff2cd3-generic_engine.py` | `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505` | HCG, via PI | code | HCG engine. **HCG input, not adopted, not an HHO result.** Same bytes as the copy in `evidence/hcg/` | not placed; cited at `hcg-v0.2` |
| `pi-uploads-received/655b3ef2-attachment.txt` | `fe9d3a4f55f28cb5f0cf0a4f6c7b2026839a01407761c285b805085ae335278f` | PI relay | relay | ChatGPT message: first proof review of the support hypothesis | evidence/hho/received/relays/ |
| `pi-uploads-received/74afb07c-HHO_D7_REFLECTION_NORMALIZER_NO_DOMINANCE_SESSION_v0_1.md` | `a4a72fd6c66d0442b8d9bea21926dfb4fb5dc9bdc197c72c048370f00c00d64f` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/7dc7f386-attachment.txt` | `c56e5d868ecb96169b54a483443442e69865f79bf5a7e88f4d4589ffcbe90bcd` | PI relay | relay | HHO migration note, as pasted by the PI | not placed (the repository copy is `records/hho/HHO_MIGRATION_NOTE.md`) |
| `pi-uploads-received/84581b51-HHO_A8_PARITY_TESTS_AND_NPL_COUNTEREXAMPLE_v0_1.md` | `b87269c4086766abfad7745e69cc8b1f5e6c8e9fe0c51a906a84c14ed5971704` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/87e3ed9d-HHO_TRACE_DUAL_EXACT_CHECK_v0_1.py` | `e08f49e19d0d611a3dc1888410bb70b06d153bcae3c0492981e0dadf90aadc7b` | ChatGPT, via PI | code | ChatGPT checker | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/8aa256d8-HHO_A8_PARITY_AND_NPL_COUNTEREXAMPLE_REVIEW_v0_1.zip` | `b0a5b649212bb6f1cd88a73570880713913386f043c1285c9db611b31f860303` | ChatGPT, via PI | package | ChatGPT review package | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/8b57a697-HHO_ADDENDUM11_A4_INDEPENDENT_REVIEW_v0_1.zip` | `5dead45675d719e4ab5edc50c74c297d4382bcac8171db01c224a69c03bc57d7` | ChatGPT, via PI | package | ChatGPT review package | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/97ca5dea-attachment.txt` | `51c24d04954688210d485760cac99f6293767460027a3f06e9063f8b909a8bd5` | PI relay | relay | ChatGPT message: decision on Addendum 12 | evidence/hho/received/relays/ |
| `pi-uploads-received/a4512a2f-attachment.txt` | `ae7459c278d197d10fc061c787b3cf300bf0c5a50a6cbb86329024a84c27fef0` | PI machine, relayed | output (pasted) | PI terminal relay: GAP output `HHO_G34_BLOCKS_v0_1_out.txt` (run on the PI's machine) | evidence/hho/outputs/pi/ |
| `pi-uploads-received/a57659c1-attachment.txt` | `0e05ae2d116efba67d501e488133f18c2d0cff9aad6d95186233c2678b767f7f` | PI relay | relay | ChatGPT message: results on Addendum 8 | evidence/hho/received/relays/ |
| `pi-uploads-received/b3ac71a9-HHO_ADDENDUM6_CHATGPT_NEGATIVE_LEAF_REVIEW_v0_1.md` | `2c8dc5195272a32c4b8526a2f46ca71c5d8e7d17c184b5e303355412d6a87dd1` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/b64ef29f-attachment.txt` | `1c822519cd5e2645b9e720cdda5316dfd09bd5a8184406541194333afced668f` | PI relay | relay | ChatGPT message: normalisation error in Addendum 10 | evidence/hho/received/relays/ |
| `pi-uploads-received/b90ba230-HHO_A9_LOCAL_SUPPORT_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` | `0cc34c30fa950c461d041b308cf1d7361793463200f817e17d6e2ad260a671f4` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/befd0170-HHO_G34_5BLOCK_LEAF_CHATGPT_REVIEW_v0_1.md` | `5a918fe5de61f281cc560db43393c20d8f73964c482d65f7b9772aa95a10a554` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/c698d54e-HHO_SUPPORT_LEMMA_PROOF_SKETCH_v0_1.md` | `326f9645c71cf44b429f30581c61dae8d99bf5ef216a262686a9076a64491f3d` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/c7b8b52e-attachment.txt` | `f85950264c3ebf02822a49804a70b7147aa22025747c157a4615c2ef7b69062e` | PI relay | relay | ChatGPT message: assessment of Addendum 1 | evidence/hho/received/relays/ |
| `pi-uploads-received/caf6fa7b-HHO_ADDENDUM12_G616_PERIOD_OBSTRUCTION_CHATGPT_REVIEW_v0_1.md` | `81fd1e361be3f56636394243408af8557251d3b78077ba7e10a5b2c5957a0b8e` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/cb4b13e4-HHO_ADDENDUM11_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` | `e016d5de99b47f5b2f13e95eecf0844978f0c23abe745fcb145b3b54ada7a8fc` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/ce5c16df-HHO_G34_A6_INDEPENDENT_REVIEW_v0_1.zip` | `d680a20470d93eb91a84732ce377f783daea00e3b8ef5070adae94cd83b32b75` | ChatGPT, via PI | package | ChatGPT review package | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/d6298205-attachment.txt` | `c74afb7cd2dd7c0d375be1cbc48fe14aea1ea9413bdd7ac310f71d879105d5b9` | PI relay | relay | ChatGPT message: review of Addendum 9 | evidence/hho/received/relays/ |
| `pi-uploads-received/db7f4c73-HHO_ADDENDUM10_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` | `8f4d958554b9abe96095170791ab28fb805e6ced620e97f05339686343b6dafc` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/e6154c96-attachment.txt` | `10f6247c73814a294bd54d39848342d0c140e09f4cc415d8197d0e83bf8bbee8` | PI relay | relay | ChatGPT message: assessment of the G₃₄ GAP results | evidence/hho/received/relays/ |
| `pi-uploads-received/e6bf6142-HHO_A9_LOCAL_SUPPORT_CHATGPT_REVIEW_v0_1.zip` | `63f388c0ba0a5ae408b05b1d108abc8c78b4dbcb0d5761d50eff94c444cbdb66` | ChatGPT, via PI | package | ChatGPT review package | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/eb26092d-cyclic_disc_claude.py` | `da76a25f57817fbeaf2b6deb749cda76cdefb5c8d59ec2d4b871a2778cf2afa9` | HCG, via PI | code | HCG engine. **HCG input, not adopted, not an HHO result.** Same bytes as the copy in `evidence/hcg/` | not placed; cited at `hcg-v0.2` |
| `pi-uploads-received/ec20808a-HHO_SUPPORT_LEMMA_CHATGPT_CROSS_REVIEW_v0_1.md` | `9981f634d898f5b28951a8ae12151cd248a0fb16f1139123231b029768c32d08` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/edd58b7f-HHO_SUPPORT_ADDENDUM2_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` | `262929bde34cf1617ed069d532ed0dd51b0b45448dc5561131bc309ff3dc2fe6` | ChatGPT, via PI | review | ChatGPT review or note | evidence/hho/received/chatgpt/ |
| `pi-uploads-received/f21284d7-attachment.txt` | `d439a53a077afec70422f240d30eb0cd1a9bf8f8a0fbabdb32eede124a253e5a` | PI relay | relay | ChatGPT message: review decision on the support lemma | evidence/hho/received/relays/ |

### Prefix-hash chain of the frozen review file

`HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` is append-only. The SHA-256 of each earlier edition, as a line prefix of the final file, is listed in `records/hho/HHO_MIGRATION_PLAN.md` §3.1 (15 entries, 80 to 952 lines). The ChatGPT owner session re-computed all 15 from its own copy and found them equal (co-owner check relayed on 10 Nov 2026).
