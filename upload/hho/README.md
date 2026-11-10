# upload/hho — HHO source files as held by the Claude owner session

**PI decision (10 Nov 2026, in the HHO conversation):** the Claude owner session uploads these files itself ("1 sen yükle"). This replaces, for these files, the migration note's step "the PI uploads the originals" (`records/hho/HHO_MIGRATION_NOTE.md` §4), following the COIL precedent.

Two folders. Every file is copied byte-for-byte from the owner session's storage. No file was edited, renamed or re-saved.

- `owner-session-outputs/claude/` — the files the Claude owner session produced in the "HHO Hurwitz–Hodge obstruction research" conversation and still holds (20 files):
  - the append-only review file `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` (final state, 952 lines);
  - scripts and their outputs.
- `pi-uploads-received/` — the files the PI sent into that conversation, as received (37 files). The attachment-ID prefix of each name is kept. They are:
  - ChatGPT's review documents, checkers and ZIP packages;
  - the PI's relays of ChatGPT's chat messages (`*-attachment.txt`, in Turkish);
  - one relay holding GAP output from the PI's machine (`a4512a2f-attachment.txt`);
  - the migration note as pasted (`7dc7f386-attachment.txt`);
  - two **HCG inputs**, `55ff2cd3-generic_engine.py` and `eb26092d-cyclic_disc_claude.py`. These are HCG inputs, not adopted, and not HHO results.

`SHA256SUMS` lists the SHA-256 of every file as uploaded (57 files). A hash certifies **byte identity of what was uploaded**. It does not certify publication rights, scientific correctness, or agreement with any copy held by the PI or by ChatGPT.

## Not held by this session (not available here)

- **Superseded script revisions.** They were overwritten in place:
  - `HHO_G34_BLOCKS_v0_1.g` r1 and r2;
  - `f20_faithful.py` r1 and its output.
- **PI-machine output files.** The files themselves are not held; one was seen only as pasted text (see above):
  - `HHO_G34_BLOCKS_v0_1_out.txt`;
  - `HHO_G34_REFLECTION_NEIGHBOR_CW_v0_2_out.txt`;
  - `HHO_C6_LEAF_TEST_v0_1_out.txt`.
- **ChatGPT packages that were not attached to the conversation.** For example its Addendum 10 and Addendum 12 review ZIPs.
- **The HCG-side HHO track.** Opening note, Δ28, gate catalogue, claim register, safeguards.
- **HCG source texts.**
- **Third-party primary texts.**

## Rights

All files are the study's own work (owner sessions, PI) or outputs computed by them. ChatGPT's ZIP packages contain copies of the study's own files, and of HCG-internal review notes labelled `SOURCE_*`. No third-party publication is included; third-party sources appear only as citations and URLs.

## Placement

Nothing here is a live document. Placement into `hho/`, `evidence/hho/` and `records/hho/` happens in the HHO batch pull requests. Each of them records the source hash from this list in `records/hho/HHO_SOURCE_MANIFEST.md`.
