# upload/coil — COIL source files as held by the owner session

**PI decision (6 Nov 2026):** the COIL owner sessions upload the study's files themselves, since they produced them; this replaces the migration note's "PI uploads his local copies" step. The PI's local copies were downloads of these same artefacts; where the two differ, the PI's copy is not known to this session and the difference is **not** checked here.

Two folders, copied byte-for-byte from the owner session's storage, no file edited, renamed or re-saved:

- `owner-session-outputs/` — every file the owner session produced during the study and still holds (live documents, locked preregistrations and addenda, run reports, audits, memos, handovers, scripts, certificates, merged result tables, the `ARSIV/` folder with its README). `__pycache__` omitted.
- `pi-uploads-received/` — files the PI sent into the owner session during the study, as received: run outputs from his machine (`out_*.zip`, `*.csv`, `pairbc*.csv`), two notes returned by the RTG session (`ringdiag-update-rule-RECOVERED.md`, `kspark-def-degnorm-RESOLVED.md`) and the co-owner's review texts (`attachment*.txt`, `paste*.txt`).

`SHA256SUMS` lists the SHA-256 of every file as uploaded (212 files). The hash certifies **byte identity of what was uploaded**; it does not certify publication rights or scientific correctness, and it does not certify agreement with the PI's local copies.

Known gap against the documents' own references: `AUDIT-R5-PAIR-BC-v1.0.md` (superseded by v1.0.1) is not held — **not available**. Everything else referenced by `PROGRAM-INDEKSI.md`, `KAMPANYA-KUNYESI.md` and `ARSIV/README.md` is present.

Rights: all files are the study's own work (owner sessions, co-owner session, PI) or run outputs from the PI's machine. No third-party publication or licence-restricted document is included.

Nothing here is a live document. Placement into `coil/`, `evidence/coil/` and `records/coil/` happens in the COIL batch pull requests, each recording the source hash from this list in `records/coil/COIL_SOURCE_MANIFEST.md`.
