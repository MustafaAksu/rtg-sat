# HCG migration to `rtg-sat` — source inventory of the Claude owner session (pre-intake)

**Date:** 10 November 2026

**From:** the Claude HCG owner session. **To:** PI Mustafa Aksu; the ChatGPT HCG owner session; the SAT co-owners.

**Status:** pre-intake inventory, SESSION.
- Nothing has been uploaded or pushed. No branch, tag or pull request has been created.
- No scientific statement is adopted or changed by this report.
- No `hcg-v*` version is chosen here.

**Read for this report:**
- **SAT migration note:** `records/hcg/HCG_MIGRATION_NOTE.md` at commit `cfe708ff95940748cf64e1d1e23b06984d908141` (branch `chatgpt/hcg-migration-preparation-20261110`). File SHA-256 `2c0b885e91e70302ae5d167841607266f19d855e05e0bb94c1abfcd2b29b0059`.
- **On `main` at `e130bc8`:** `rtg-sat` `CONVENTIONS.md`, `REGISTRY.md` and `records/hho/HHO_MIGRATION_NOTE.md`.
- **HHO migration plan:** `records/hho/HHO_MIGRATION_PLAN.md` on `claude/hho-batch0-plan`.
- **HHO source upload:** `upload/hho/README.md` and `SHA256SUMS` on `upload/hho-sources` (`516400d`).
- **RTG tags:** `rtg-corpus` tags `dyad-v6.4.19`, `gen-v2.8.9`, `programme-v1.2`, `ofn-v0.10`, fetched read-only.

---

## 1. Source conversations and sessions

| ID | Session | Role for HCG | What this session holds from it |
|---|---|---|---|
| S1 | **Claude HCG owner session.** Claude Code session `session_012FfqyZ6c5FmBB2HuzwPfMz` (local transcript ID `4791d90d-29fa-5681-8c6f-12a12403748a`), RTG Dyadic project, 21 Oct – 3 Nov 2026. The HHO track was opened here on 3 Nov (Δ28). | Owner | Everything in §2 marked "own". The PI's name for this conversation ("Hodge Conjecture") is to be confirmed by the PI. |
| S2 | **ChatGPT HCG owner session.** | Owner | Only copies the PI relayed into S1 (`pi-uploads-received/`). ChatGPT's own originals are with that session. |
| S3 | **Third-family blind auditor**, rounds R1 and R2. The identity is held by the PI. | Reviewer, not owner | Reports and packages as relayed. No file names the model family. |
| S4 | **Lineage: the RTG "imaginary unit / Eisenstein" discussion.** | Lineage only | The five PI uploads of 21 Oct 2026 (ChatGPT texts "The imaginary unit i in Relational Time Geometry", "RTG and the Hodge Conjecture: a concrete mathematical route", two review replies, and the protocol acceptance), plus charter v0.1. The conversation itself is **not identified**: a past-chat search found no matching title. It is not presumed. |
| S5 | **HHO conversation** "HHO Hurwitz–Hodge obstruction research" (`claude.ai/chat/bbf896a1-…`). | Consumer of HCG inputs | Nothing. Its two received HCG engines are byte-identical to S1's (§3.9). |

The session transcript itself is not proposed for upload. It is platform data, not a study file.

## 2. Storage inventory and the proposed upload

The script `hcg_inventory_stage.py` hashed every file in S1's storage. It covers:
- the working tree;
- the PI attachments and session-start uploads;
- the literature folders;
- the scratch area.

It also read every ZIP, including nested ZIPs, without extracting anything.

| Class | Files | MB | Proposed treatment |
|---|---|---|---|
| `O` own original, unique bytes (includes 17 scratch-only files) | 570 | 12.06 | upload, unchanged |
| `O-ADAPTED` path-adapted replay copies of ChatGPT W6/W7 scripts (only file paths edited) | 10 | 0.04 | upload with this label |
| `R` received from the PI (ChatGPT, auditor, PI relays), no third-party content | 174 | 3.09 | upload, unchanged |
| `R-TP-ZIP` received ChatGPT ZIPs that contain Severn deposit data | 3 | 0.30 | **held back** (D3) |
| `X-COPY-RECEIVED` / `X-EXTRACT` / `X-DUP` byte copies, ZIP extractions, duplicates | 1216 | 12.22 | not uploaded; listed with a pointer to the original |
| `X-TP` / `X-TP-RECEIVED` third-party texts and renders | 149 | 17.28 | not uploaded; cited by identifier and hash |
| `X-RTG-DYAD` López-Hernanz 2012 check of the Dyadic return | 6 | 0.02 | not HCG material (§5) |

**Staged tree.** The proposed tree is staged locally only:
- `upload/hcg/owner-session-outputs/claude/…` keeps the original relative paths, so provenance stays visible;
- `upload/hcg/pi-uploads-received/…` keeps each attachment name with its ID prefix;
- `pi-uploads-received/session-start/` holds the 21 Oct uploads.

In total, 754 files and 15.2 MB, with `SHA256SUMS` verified (754/754 OK). The full classification of every held file is in `HCG_SOURCE_INVENTORY_CLAUDE_20261110.tsv`, with its class, hash, source path, proposed path and duplicate pointer.

**Screens run on the staged tree:**
- no e-mail addresses;
- no credentials;
- no personal paths;
- no name of the auditor's model family.

**INTERNAL labels.** 175 staged files carry `INTERNAL` or SG-10 distribution labels. See decision D2.

## 3. Scientific inventory

### 3.1 Governing records (chat-level adoptions)

| Object | SHA-256 | Held as |
|---|---|---|
| Charter v0.1 (received, 21 Oct) | `7bbd29e9ea8d…` | session-start upload |
| Charter v0.2 (Claude) | `8feed777abc7…` | `hodge_session/` |
| Ledger v0.1 DRAFT | `0818a709…` | own |
| Ledger v0.1 r2 | `959f6a03…` | own |
| Ledger v0.1 r3 | `a783e2da…` | own |
| Ledger v0.1 packages | — | three ZIPs, own |
| **Ledger v0.1 ADOPTED** | `75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7` | own |
| v0.1 release record | `8153fd9f…` | own |
| v0.2 change log Δ1–Δ23 (folded into v0.2) | `8fb25dadfb4416136625d7b8d6eea9f20ea0d8234bdd32495f0ac12d069efd98` | own |
| v0.2 DRAFT r1 | `c15815ef…` | own |
| v0.2 DRAFT r2 | `c8d595ae…` | own |
| v0.2 build fragments, `make_v02*.py`, diffs | — | own |
| v0.2 QA record | `96b1502b…` | own |
| v0.2 replay packages (three ZIPs) | — | **scratch only**; own |
| **Ledger v0.2 ADOPTED** (PI, 26 Oct 2026, 22:44 +03:00) | `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` | own; the bytes match the cited hash |
| v0.2 release record | `967732cd…` | own |
| v0.2 release record addendum 1 | `f16b5bed…` | own |
| `release_v0_2.py` | — | own |
| Diff r2 → ADOPTED | — | own |
| Verification ledgers v0.1, v0.2, v0.3, v0.4 and v0.4a–d | — | own |
| H1/H2 problem contract | — | own |
| `SOURCE_MANIFEST.md` | `3f9fd7bb…` | own |

### 3.2 Pending deltas (not adopted)

The live log is `HCG_DSN_v0_3_PENDING_DELTAS.md`, SHA-256 `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d`.

| Entry | Content | State |
|---|---|---|
| Δ24 | Auditor round 2 complete | PENDING; PI field blank |
| Δ25 | Boundary-rank corollary; one withdrawn proposal | PENDING; PI field blank |
| Δ26 | Severn v2 successor audit | PENDING; PI field blank |
| Δ27 + addenda 1–17 | Nonsplit eightfolds, up to d ≥ 53 | PENDING; PI field blank |
| Δ28 | HHO opening | PENDING; PI field blank |
| Δ29 | Positive lane | **record-only**; PI field blank |

The SAT note's "reportedly Δ29" is confirmed.

**Held states of the log.** The log was edited in place, so 19 byte states are held:
- one earliest state in scratch, `1fb44251…`, which is the state the HHO plan cites;
- 17 bundle states, `ed69b940…` → `59a7aabc…`;
- the live state `1f00a1eb…`.

Further states exist only inside the bundle ZIPs that were sent.

### 3.3 Proofs and reviews

- **Own documents:** 134 Markdown files, 57 of them `*_CLAUDE_*` reports. They span H1/H2, H3 (Severn PO-1–PO-6, Lemma 6.2, the v2 successor audit), the G₃₄ gates A/B/C, W5–W7, H4 selection (edge-form, edge-flux, holdout, P2/P3, NEW01/NEW02, toy and block lemmas, braid escape, G(3,3,3)), nonsplit eightfolds (Δ27), the HHO opening note and the positive lane.
- **Received documents (S2/S3):** ChatGPT reviews, ledger deltas and packages, and the auditor R1/R2 reports, packages and replays.
- **The locality proof sought by the HHO session is held here as received originals:**
  - `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md` (`0ec38558…`);
  - its v0.2 (`d62942e3…`);
  - the induced-period bound note (`03199b80…`).

### 3.4 Retractions, refutations, failed routes, concessions

| Register | Location |
|---|---|
| Appendix B (retired and rejected claims, including `[RETRACTED]`, `[REFUTED]` and `[FAIL]` rows); §6.21 negative results; the D-1–D-8 dispute log | v0.2 ledger |
| Concessions D-9–D-24 | v0.3 log |
| "Severn's method is capped at split eightfolds" — withdrawn by Claude | Δ25 |
| "(L) ⇒ split" shown false at the class-datum level (LSEP, PROPOSED, Claude) | Δ27 add. 17 |

### 3.5 Witnesses, counterexamples and certificates

**Own:**
- W5 certificate `g34_cert_tuple5_balanced.json` (`172766a9…`);
- W6 and W7 certificates (`ae904878…`, `45097b30…`);
- root files and gate outputs;
- Severn link replays (90-move word, W5 bridge);
- G(3,3,3) scan;
- nonsplit-eightfold GAP data;
- the C₆ separator (`cyclic_disc_claude.py` and its output);
- the G₂₆-type real-data witness (`real_g26_*`);
- positive-lane CM scan.

**Received:** NEW01/NEW02 certificates, G34-BLOCK-01 roots, BRAID-ESCAPE-01 certificate (ChatGPT).

The SAT note lists NEW03/NEW04. They occur only as named candidates in v0.2 (NEW01 is the certified case).

### 3.6 Engines and key scripts (own)

| Script | SHA-256 |
|---|---|
| `generic_engine.py` | `66f2c253…` |
| `cyclic_disc_claude.py` | `da76a25f…` |
| `disc_locality_proof_check_claude.py` | `f538ce4d…` |
| `real_g26_cup_claude.py` | `c09e8c0a…` |
| `h1_h2_exact_checks.py` | `3b3deb4c…` |
| `g34_gateA.py` | `b6b80208…` |
| `g34_gateB.py` | `324f11e8…` |
| `g34_gateC_search.py` | `fb8ad841…` |
| `audit_cert.py` | `83f05ba3…` |
| `h4_obstruction.py` | `0b262cf3…` |
| `cm_rank_primitivity_claude.py` | `ef64c2d6…` |

Beyond these: 138 own `.py` and `.g` files in total.

### 3.7 Third-party sources (cite only; not uploaded)

**Held locally, with hashes in the TSV:**
- Severn drafts `hexagon:2610.00246v2`, `.00371v1`, `.00386v1`, `.00387v1`, `.00387v2` (PDF, extracted text, page renders).
- **Severn Zenodo deposit** `10.5281/zenodo.23422649`:
  - TeX `68095102…`;
  - PDF `5bc6a282…`;
  - certificates ZIP `3a39a346…`.

  The deposit's licence is **not recorded** in the files, and a web search did not find the record.
- Schoen 1988; Koike; two further papers (`abelian_powers.pdf`, `cm.pdf`); Milne 1999; Dettweiler–Wewers 2004; ADFIO (arXiv:1507.05710); Bader; McMullen; López-Hernanz 2012.

### 3.8 HHO interface

**HHO-track files held here:**
- the HHO opening note v0.1 (`6a7a8053…`) and its bundle;
- Δ28 inside the log;
- the founding documents: ChatGPT framework and review (`10041afe-…`, `cbaec3fd-…`, `fc36903f-…` ZIP); Claude reviews `cc31ef06…` and `72130efc…`.

They are proposed for upload as **historical HHO-track source evidence produced in S1**. Scientific custody stays with HHO.

**Consumer copies.** HHO PR #16 carries `55ff2cd3-generic_engine.py` and `eb26092d-cyclic_disc_claude.py`. They are **byte-identical** to S1's `66f2c253…` and `da76a25f…`.

**Two corrections to the SAT note (provenance only):**
1. The "(L) ⇒ split is false at class-datum level" witness, called "HHO Addendum 17" in the note, is **HCG Δ27 addendum 17**:
   - made in S1 on 3 Nov, before HHO opened;
   - source `H3_FRAMEWORK2_REVIEW_AND_REAL_DATA_CLAUDE_v0_1.md` (`72130efc…`);
   - state PROPOSED (Claude).

   It is HCG-side evidence. HHO's register carries a copy as LSEP.
2. R1 "d ≥ 53" is the HCG Δ27 chain (addenda 2–17, CHECKED by two AIs, source-conditional). It sits under the (H) of the HHO opening note.
   - HHO's d ≤ 5 / d = 6 / d = 7 family is a separate line with its own hypotheses. HCG's own d = 6 proof (Δ27 add. 2) appears there as prior art.
   - No contradiction is implied. The two lines are compared only after their exact hypothesis lists are recovered.

### 3.9 RTG import provenance (targeted check at tags)

| Import | Source | Check at tag |
|---|---|---|
| R1, R2 | DYAD §§6.1–6.3, `DYAD-ALG-Q-INVARIANT-FORM` | `dyad-v6.4.19`: RID present |
| R4 | `DYAD-THM-C21`, `DYAD-ALG-NF6` | present |
| R5 | `DYAD-THM-SMOOTH-EMBEDDING` | present |
| R6(a) | `DYAD-THM-PRIM-CTR` | present |
| R3 | J_Q = (2A − I)/√3; Genesis §6.6, RID unavailable | `gen-v2.8.9` §6.6 gives J_Q = (1/√3)[[1,−2],[2,−1]], the same matrix |
| R8 | SG-PROG-1 | `programme-v1.2`: present |
| OFN v0.10 | — | `ofn-v0.10` exists |

**Byte match.** The DSN file at `dyad-v6.4.19` has SHA-256 `40c9e63f…`. This matches the receipt in charter v0.1 exactly.

**v6.4.18 has no tag.** It is not tagged in `rtg-corpus`; it was adopted before the repository's tags began. The v6.4.18 pins in the ledger are therefore historical.

**Not checked:** the grades at each RID. The registry field stays `not set` until the owners record the import (decision D6).

## 4. Missing or not held

- ChatGPT ZIPs `c27404ea…` and `6390df50…` (Severn v2 successor review). The log already records them as never received.
- **ChatGPT's own originals.** Only relayed copies are held. ChatGPT's session uploads its own files, and duplicates are reconciled by hash.
- **The S4 conversation and any RTG-side record of the lineage.** Not identified.
- **States of files edited in place**, beyond those preserved in bundles and the 19 log states.
  - One cited state is recoverable exactly: `H3_BOUNDARY_RANK_NOTE_REVIEW_AND_SCOPE_CLAUDE_v0_1.md` was cited as `bd4bcc1a…` in Δ25. It is the first 5,200 bytes of the held file (6,531 bytes). The rest is the later dated addendum.
- **PI-machine outputs.** None are cited by the HCG ledgers or the log.
- **The licence of the Zenodo deposit.**

A name-and-hash check covered every file named and every hash cited in v0.2, the v0.2 log and the v0.3 log. Apart from the items above, everything is held.

## 5. Scientific scope boundaries

1. **What HCG is not.** HCG is not RTG and not HHO. It makes no claim that the Hodge conjecture, or Severn's claim, is proved or refuted. Severn A/B/C stay CLAIMED.
2. **Chat-level adoption.** v0.2 was adopted at chat level only, as a scoped consolidation. No claim row became ACCEPTED through that adoption.
3. **Pending entries.** Δ24–Δ29 are pending. Δ29 (positive lane) and the rStation paper-56 question are HCG-side and unreviewed beyond Claude's note.
4. **HHO-track material.** It stays dated HHO-track evidence. Moving files does not move scientific ownership.
5. **RTG-Dyadic material produced in S1.** `dyad_lh/` (the López-Hernanz 2012 check) declares itself "RTG-Dyadic material, separate from the standalone HCG session". It is excluded from HCG. Its routing — to a `rtg-corpus` DYAD pipe or nowhere — is a PI decision.
6. **The auditor.** The third-family auditor stays a reviewer. Its replays are evidence of review, not proof grades.

## 6. Decisions needed before the first HCG release

| # | Decision | Owner session's observation |
|---|---|---|
| D1 | **First tag numbering.** Option A: `hcg-v0.2`, byte-exact. Option B: a new first repository edition. | Option A is technically possible: the exact v0.2 bytes, the build chain, the release transform and the reverse check are all held. |
| D2 | **Public disclosure of INTERNAL / SG-10 material** (175 staged files, including v0.2 itself, which states "must not be sent to the third-family auditor until Priority A and B are submitted"). | Round 2 is complete (Δ24). Lifting or retiring SG-10 for publication is a PI decision, recorded in the intake. |
| D3 | **Third-party data.** The Severn deposit licence is unknown. | Proposed:<br>• the deposit, the drafts and the other papers are cited only;<br>• the 3 received ZIPs containing deposit data are held back;<br>• a separate PI decision is needed if the licence is later shown to permit redistribution. |
| D4 | **Who uploads received copies.** | Proposed, on the HHO precedent: S1 uploads its own outputs and the copies it received; S2 uploads its originals. |
| D5 | **Auditor materials in a public repository** (reports and packages; identity withheld). | — |
| D6 | **RTG input pins** for `REGISTRY.md`. | Proposed: `dyad-v6.4.19`, `gen-v2.8.9`, `programme-v1.2`, `ofn-v0.10`, with v6.4.18 recorded as a historical pin. Grades still to be checked by the owners. |
| D7 | **Scope of the first edition.** | v0.2 only (Option A), or with Δ24–Δ29 reviewed (Option B). |
| D8 | **Lineage conversation (S4).** | Identify it, or record it as "not identified". |
| D9 | **`dyad_lh/` (RTG-Dyadic material).** | Route or archive. |
| D10 | **Machine paths inside originals** (`/home/claude/...`). | Proposed: keep, as in the COIL decision of 6 Nov. |

**Owner tasks after the decisions:**
1. Push `upload/hcg-sources` (S1's staged tree with `README.md` and `SHA256SUMS`). This needs push access, which this session does not have yet.
2. Batch 2: charter, `HCG_STUDY_LEDGER.md`, claim register and the (L)/(D)/(H0)–(H4) source dictionary. Sources: v0.2 §§6.10–6.11, the Gate A report, Δ26, and Severn texts cited by version.
3. Batch 3: code, certificates and frozen evidence.
4. Batch 4: release record, the other owner's review, PI adoption.

## 7. Not done here

- No upload, push, branch, pull request or tag.
- No scientific re-review.
- No grade check at the RTG RIDs.
- No licence check beyond the files and one web search.
