# upload/hcg — HCG source files as held by the Claude owner session

**What this is.** The unchanged source files of the HCG study (Hodge Conjecture / RTG Complex Geometry and Hodge Realization) held by the Claude HCG owner session: Claude Code session `session_012FfqyZ6c5FmBB2HuzwPfMz`, RTG Dyadic project, 21 Oct – 3 Nov 2026. A source upload is not a scientific adoption, a release or a tag.

## PI decisions (10 Nov 2026, 10:04 +03:00, in the HCG owner conversation)

Given in reply to the decision list of `HCG_SOURCE_INVENTORY_CLAUDE_20261110.md` (SHA-256 `594ff2bf744a44f1c1fb1f40fec7b6b7a6541b8b8fc2632e1e982a160d9aaa3b`). Quoted verbatim, with an English reading:

| # | PI text | Reading |
|---|---|---|
| 1 | "A" | First repository tag: Option A — `hcg-v0.2`, reproducing the chat-adopted v0.2 byte-exact. Δ24–Δ29 stay pending for a later edition. |
| 2 | "Gizliliği kaldırabiliriz." | The INTERNAL / SG-10 distribution guard may be lifted. The labels inside the original files are historical and are left unchanged. |
| 3 | "DIş kaynaklar için LIT'i ve LIT'in metodolojisini kullanacağız." | Third-party sources go through LIT and its methodology. None is placed here. |
| 4 | "Sen yükle" | The Claude owner session uploads these files itself, including the copies it received. |
| 5 | "Denetçi raporları yayınlanabilir. sorun yok." | The third-family auditor's reports may be published. |
| 6 | "rtg-corpus'ta güncellemeler oldu RID'leri bir noktada gözden geçirmek gerekecek. ilk adımda olması şart değil ama istersen olabilir." | The RTG RIDs are to be reviewed at some point; not required in the first step. |
| 7 | "kalsın" | Machine paths inside the originals stay as they are. |

No decision was given on the lineage conversation or on the RTG-Dyadic material `dyad_lh/`; both stay out of this upload.

## Folders

Every file is a byte-for-byte copy from the owner session's storage. No file was edited, renamed or re-saved.

- `owner-session-outputs/claude/` — 580 files produced by the Claude owner session. Original relative paths are kept.
  - `g34/dsn/` holds the ledgers: v0.1 ADOPTED (`75b5f58c…`), **v0.2 ADOPTED (`276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`)**, their drafts, release records, build and release scripts, and the pending-delta logs (Δ1–Δ23; Δ24–Δ29, live state `1f00a1eb…`).
  - `g34/` (top level, `h4sel/`, `nonsplit8/`, `severn_v2/`, `auditor_r1/`, `auditor_r2/`, `lemma62/`, `positive/`) holds reports, engines, scripts, GAP files, certificates, outputs and the bundles as sent.
  - `g34/hho/` and the framework reviews in `g34/nonsplit8/` are **HHO-track source evidence produced in the HCG conversation**. Scientific custody is with HHO.
  - `g34/cg_replay/` holds 10 path-adapted replay copies of ChatGPT's W6/W7 scripts and their results. Only file paths were edited by Claude.
  - `hodge_session/` and `litrev/` hold the first-day documents and Claude's literature reviews.
  - `scratch/` holds files kept only in the session's scratch area, including the three v0.2 replay packages and the earliest held state of the v0.3 delta log (`1fb44251…`).
- `pi-uploads-received/` — 168 files the PI sent into the conversation, as received, with their attachment-ID prefix: ChatGPT's documents, ledger deltas, certificates and ZIP packages; the third-family auditor's reports and packages; the PI's relays of chat messages (`*-attachment.txt`, partly in Turkish).
- `pi-uploads-received/session-start/` — the 6 files uploaded when the session opened on 21 Oct 2026 (charter v0.1 and five relayed texts from the earlier imaginary-unit discussion).

`SHA256SUMS` lists all 754 files. A hash certifies **byte identity of what was uploaded**. It does not certify scientific correctness, publication rights, or agreement with a copy held by the PI or by ChatGPT.

## Not uploaded

- **Third-party texts and data** (PI decision 3): Severn's Hexagon drafts and Zenodo deposit `10.5281/zenodo.23422649`, Schoen, Koike, Milne, Dettweiler–Wewers, ADFIO, Bader, McMullen, López-Hernanz, and page renders of them.
- **Three received ChatGPT ZIPs that contain Severn deposit data**, held back for the same reason. Cited by hash:
  - `120260e6-HCG_SEVERN_90MOVE_INDEPENDENT_COMPLETE_v0_1.zip`
  - `1951e0e2-HCG_SEVERN_V2_PART3_CHATGPT_CROSSWALK_REPRO_v0_1.zip`
  - `7f4ed11f-HCG_SEVERN_W5_SOURCE_BRIDGE_FINAL_REPRO_v0_1.zip`
- **Byte copies, ZIP extractions and duplicates** of files that are uploaded.
- **`dyad_lh/`** (López-Hernanz 2012 check): RTG-Dyadic material by its own header, not HCG.
- The session transcript.

## Not held by this session

- ChatGPT's own originals (only the relayed copies above).
- ChatGPT ZIPs `c27404ea…` and `6390df50…` (Severn v2 successor review), never received.
- States of files edited in place, beyond those kept in bundles.
- The identity of the earlier imaginary-unit conversation.

## Placement

Nothing here is a live document. Placement into `hcg/`, `evidence/hcg/` and `records/hcg/` happens in the HCG batch pull requests, each recording the source hash from this list in `records/hcg/HCG_SOURCE_MANIFEST.md`.
