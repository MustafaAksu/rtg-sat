# evidence/hcg — frozen HCG files: ledgers, reports, code, certificates, outputs

This folder holds two kinds of file.
- **The 754 historical source files** listed in `SHA256SUMS`. Each is an **unchanged copy** of a file in `upload/hcg/`: nothing was edited, renamed or re-saved. Working folders are kept whole, so scripts, their inputs and their outputs stay together.
- **Files written for this repository:** this `README.md`, the indexes `SHA256SUMS`, `PLACEMENT_MAP.tsv` and `NAME_ALIASES.tsv`, and the scripts in `verification/`. These are not session originals and are not covered by the "unchanged copy" statement.

- `SHA256SUMS` lists all 754 placed files.
- `PLACEMENT_MAP.tsv` gives, for each placed file, its SHA-256 and its path in `upload/hcg/`.
- `verification/place_evidence.py` made the placement. It checks each source against `upload/hcg/SHA256SUMS` and re-hashes each copy.

A historical source file is frozen and is never edited. It keeps its original wording, including statements that were later corrected, its INTERNAL labels and its session paths (`/home/claude/...`). The current state of the study is in `hcg/`, not here.

**Placement is not adoption.** A file's presence here says nothing about the review state of what it contains.

## Folders

| Folder | Files | Content | Relation to the adopted ledger (`hcg-v0.4`) |
|---|---|---|---|
| `ledger-history/` | 61 | Ledger v0.1 (drafts, ADOPTED, release record, packages); ledger v0.2 (drafts, build fragments, `make_v02.py`, `release_v0_2.py`, diffs, QA record, ADOPTED, release record and addendum); the pending-delta logs for v0.2 (Δ1–Δ23) and v0.3 (Δ24–Δ29, live state) | v0.2 and its chain. The v0.3 log is pending. |
| `session-start/` | 11 | Charter v0.2, the H1/H2 problem contract and exact checks, the R7 proof note, the first verification ledgers, Claude's first H3 reviews | cited by v0.2 |
| `g34/` | 126 | G₃₄ gates A/B/C, W5/W6/W7 certificates and root files, the cup-form and monodromy scripts, verification ledgers v0.3–v0.4d, `SOURCE_MANIFEST.md`, auditor rounds R1/R2 (Claude's intakes and replays), Lemma 6.2 check, the toy model, bundles as sent | mostly v0.2-era. The auditor R2 final intake and bundle replay belong to Δ24 (**pending**), as do the two bundles named below. |
| `h4sel/` | 175 | H4 selection: edge-form and edge-flux, holdout test, P2/P3 with `generic_engine.py`, NEW01/NEW02, toy and block lemmas, braid escapes, G(3,3,3) scans, W5 links, Severn tuple and 90-move replays | cited by v0.2 |
| `received/` | 174 | Files received from the PI: ChatGPT's reviews, ledger deltas, certificates and packages; the third-family auditor's reports and packages; the PI's relays; `session-start/` holds the 21 Oct uploads | both v0.2-era and later |
| `literature-reviews/` | 2 | Claude's edge-flux literature review and comparison | cited by v0.2 (Δ7) |
| `severn-v2/` | 10 | Severn v2 successor audit | in `hcg-v0.3` (Δ25–Δ26) |
| `research-next/` | 1 | Boundary-rank note review | in `hcg-v0.3` (Δ25) |
| `nonsplit8/` | 173 | Nonsplit Weil eightfolds: `cyclic_disc_claude.py`, the locality checks, GAP screens, the reports of Δ27 addenda 1–17, and 17 states of the v0.3 log in `deliver*/` | two results in `hcg-v0.4` (§6.24); the rest **pending** (Δ27) |
| `positive/` | 6 | All-powers positive lane: CM rank scan | **pending** (Δ29) |
| `hho-track/` | 3 | The HHO opening note v0.1 and its bundle folder | **HHO-track source evidence**; custody HHO (Δ28, pending) |
| `scratch/` | 12 | Files kept only in the session's scratch area: the three v0.2 replay packages, the earliest held state of the v0.3 log, small probes | mixed |
| `verification/` | 2 | The manifest and placement scripts (written for this repository; not session originals) | — |

Two bundles sit in `g34/` because that is where they were written: `HCG_HHO_OPENING_NOTE_BUNDLE_CLAUDE_v0_1.zip` (HHO-track) and `HCG_POSITIVE_LANE_CLAUDE_REVIEW_v0_1.zip` (pending, Δ29).

## Finding a file named in the ledger

1. Look for the name in `PLACEMENT_MAP.tsv`. Received files carry an 8-character attachment prefix.
2. If it is not there, look in `NAME_ALIASES.tsv`. The session often held the same bytes under several names, and only one copy was uploaded. The table lists 44 such names with the placed file that has identical bytes. Example: `roots_alt_5.json` (the W5 tuple, `480cd6dc…`) is placed as `h4sel/severnlink/W5_BASELINE_ROOTS.json`.
3. A few names exist only inside the bundles (`*.zip`).
4. Three names cited by the ledger are Severn's deposited files (`braid.txt`, `tuple_pairs_D3.json`, `weil-sixfolds-qsqrt3-certificates.zip`). They are third-party data and are not stored here (`records/hcg/HCG_SOURCE_MANIFEST.md` §3).

`NAME_ALIASES.tsv` is derived from the owner session's inventory, `records/hcg/HCG_SOURCE_INVENTORY_CLAUDE_20261110.tsv`.

## Key files

| What | Path | SHA-256 (first 12) |
|---|---|---|
| Ledger v0.2 ADOPTED (chat level) | `ledger-history/adopted_v0_2/HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` | `276c93a3393d` |
| Ledger v0.1 ADOPTED (chat level) | `ledger-history/adopted/HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` | `75b5f58c30d6` |
| Pending-delta log v0.3 (live state) | `ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` | `1f00a1eb5dbe` |
| H1/H2 exact checks | `session-start/h1_h2_exact_checks.py` | `3b3deb4c5db2` |
| G₃₄ gate scripts | `g34/g34_gateA.py`, `g34/g34_gateB.py`, `g34/g34_gateC_search.py` | `b6b80208f7cb`, `324f11e8f826`, `fb8ad8417fe1` |
| W5, W6, W7 certificates | `g34/g34_cert_tuple5_balanced.json`, `g34/g34_cert_W6_comb.json`, `g34/g34_cert_W7_comb.json` | `172766a91017`, `ae9048784171`, `45097b3042f3` |
| Exact engine | `h4sel/p2p3/generic_engine.py` | `66f2c253d7b8` |
| NEW01, NEW02 certificates (ChatGPT) | `received/94297bd7-HCG_NEW01_MIXED_01_CERTIFICATE_v0_1.json`, `received/2c213fce-HCG_NEW02_MIXED_01_CERTIFICATE_CHATGPT_v0_1.json` | `aa7acd4322b8`, `b5b29332a777` |
| G34-BLOCK-01 roots; BRAID-ESCAPE-01 certificate (ChatGPT) | `received/4a8df43f-HCG_G34_BLOCK_01_ROOTS_v0_1.json`, `received/bfbf234e-HCG_G34_BLOCK_BRAID_ESCAPE_01_CERTIFICATE_v0_1.json` | `71a030ce52bb`, `44030b5f5577` |
| Auditor reports | `received/7a7f0cc1-GEOMETRIC_REPORT.md` (R1), `received/dfeaa2ff-ROUND2_FINAL_REPORT.md` (R2) | `d72d3616a4be`, `1a3a1d444faf` |
| Cyclic discriminant engine (pending, Δ27) | `nonsplit8/cyclic_disc_claude.py` | `da76a25f5781` |
| Locality proof check (`hcg-v0.4` §6.24; replay: `verification/replay_d27_core_checks.py`) | `nonsplit8/disc_locality_proof_check_claude.py` | `f538ce4deac1` |

## Running the scripts

The scripts were written for the session's storage and contain its absolute paths. They are kept as written. To replay one, copy its folder elsewhere and adjust the paths; a replay is new evidence and is recorded as such, not written back here. The heavy runs and their recorded outputs are described in the reports beside each script.
