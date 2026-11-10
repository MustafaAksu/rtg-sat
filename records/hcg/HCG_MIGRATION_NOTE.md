# HCG — migration preparation and HHO source-interface note

**To:** HCG owner sessions (Claude and ChatGPT); PI Mustafa Aksu  
**From:** ChatGPT, SAT co-owner  
**Date:** 2026-11-10  
**Status:** SESSION / advisory, pre-intake; not scientific verification, owner adoption, release or a request to retag HCG.  
**Placement:** `records/hcg/HCG_MIGRATION_NOTE.md` (working record until the first HCG repository release).

## 1. Decision and source boundary

HCG (Hodge Conjecture / RTG Complex Geometry and Hodge Realization) is a separate satellite study under `rtg-sat/REGISTRY.md`; it is not an RTG scientific-owner stream. The registry records an HCG **session ledger v0.2 adopted in the conversation on 26 October 2026**, but **no HCG scientific file or adopted `hcg-v*` tag in this repository**. A chat-level edition must not be represented as a tagged repository release.

This note prepares source intake only. The HCG owner sessions must inspect their original conversation files and PI-machine evidence before registering scientific claims. The inventory below is **reported by the HHO migration note/plan and prior conversation context, not verified by reading original HCG bytes**. Do not reconstruct missing sources from summaries.

**Checked inputs (10 Nov 2026, targeted reading):**
- `rtg-sat/CONVENTIONS.md` §§1–7 and `REGISTRY.md`, on `main` after merged HHO PR #14 (`4bf99b4e4930a540fb39ee247b35444633e7f090`);
- `records/hho/HHO_MIGRATION_NOTE.md` (§§2–8, PR #14) and the HHO owner migration plan (PR #15, §§2–7; still a PR at this check);
- HHO original-upload PR #16 (`upload/hho-sources`), which contains two received HCG scripts;
- `rtg-lit/CONVENTIONS.md` §8.2 (satellite eligibility; separate from source verification).
The HCG original ledger, pending deltas, witnesses, GAP output and primary HCG proof packages were **not available in the SAT repository at this check**.

## 2. Requested original-source inventory — verify before placement

| Group | Source objects to request/identify | Status at this check |
|---|---|---|
| Governing study ledger | HCG session v0.2 (reported filename `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`); HCG pending-delta log including Δ28 (reported `HCG_DSN_v0_3_PENDING_DELTAS`) | Conversation-reported only; originals not received |
| Mathematical contracts | Exact (L), (D), (H0)–(H4) definitions, domains, clocks, representations, witness semantics and permitted equivalences | Need the original source text; cannot be supplied by HHO paraphrase |
| Finite witnesses / counterexamples | W5/W6/W7, NEW01–04, G34-BLOCK-01, ESCAPE, C₆ separator, other owner-named gates and their proof/negative verdicts | Inventory and actual statuses must be reconciled with originals |
| Independent HCG evidence | `generic_engine.py`, `cyclic_disc_claude.py`, exact input tables, code and outputs/certificates for witnesses and group computations | Two named scripts exist as **received HCG inputs** in HHO upload PR #16; not an HCG release or scientific replay |
| HCG mathematical provenance | Local discriminant / induced-period notes, accepted review records, errata, withdrawn arguments, named hypotheses and dependencies | HHO PR #15 reports some filenames; actual bytes and statuses unverified here |
| HHO track opened inside HCG | HHO opening note, Δ28, G1–G12 catalogue, first claim register (including R1 d ≥ 53), HHO-SG-1…6 | Preserve as dated *HHO-track source evidence*, not as current HCG-owned HHO science |

The HHO review plan also lists `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md` and an induced-period review as missing to that session. These are **acquisition targets**, not evidence of loss. File names and session-reported hashes must be verified on the bytes actually received. Any unseen item is `not available`.

**Cross-line consistency guard.** HHO PR #15 reports the HCG-side `d >= 53` claim and an independent HHO-side `d <= 5`, `d = 6`, `d = 7` result family, with potentially different hypotheses: do not put them in one theorem inventory or infer a contradiction until exact source assumptions are recovered. The HHO migration note also identifies the withdrawn `HHO-CONJ-NPL` (C3 x F20 counterexample) and the reported Addendum 17 class-datum witness refuting `(L) => split`. Preserve the corresponding historical originals if received and route scientific custody to HHO; do not promote these into HCG theorems by co-location.

## 3. HCG ↔ HHO interface (no circular adoption)

1. **Scientific ownership.** HCG owns its own study statements, witnesses and engines as reviewed/adopted by its owners and PI; HHO owns its obstruction claims and the decisions on their hypotheses. A HHO claim created in the HCG conversation remains an HHO-track historical input, not an HCG result just because of storage.
2. **Until HCG has a tag.** HHO may keep its needed original HCG sources under `evidence/hho/received/`, unchanged, each with SHA-256, labelled `HCG input; not owner-adopted in rtg-sat; not an HHO result`. PR #16's two scripts are upload evidence at present, **not** a replacement for the complete HCG source package.
3. **After HCG releases.** Each HHO consuming statement is compared against the exact HCG adopted tag, release record, source labels/IDs and hashes. HHO owners decide a scoped re-pin in their own reviewed successor. An HCG tag does not automatically upgrade a HHO claim or validate a copied engine. Do not delete the frozen copies that establish historical HHO provenance.
4. **Reverse flow.** HHO → HCG may occur only with the PI adoption required by `REGISTRY.md`, an explicit owner disposition and an HCG release/import record. HCG may reference HHO research as noncanonical context without adoption. Neither transfer implies an RTG result.
5. **External mathematics.** A reference to a Severn or other third-party theorem retains its bibliographic origin, version and exact hypotheses. A HCG restatement or HHO citation is not an independent verification of that source.

The HHO PR #15 plan records that the PI selected the first HHO target as `(L)+(D) ⇒ [1]` at `d=8`; this is **HHO planning**, not an HCG theorem, and must be checked against the original definitions once acquired.

## 4. Intake, copyright and evidence protocol

- **No rewritten originals.** Each source-owning session supplies its own unmodified files on `upload/hcg-sources` with a SHA-256 inventory; PI-machine output is received unchanged under a separate source subfolder. If the PI instead supplies bytes, keep that acquisition path explicit. As with HHO PR #16, a source upload is not scientific adoption.
- Create `records/hcg/HCG_SOURCE_MANIFEST.md`: original name, conversation/session, source type (owner-produced / PI-received / third-party), exact hash, new path, version, acceptance status, and any HHO consumer copies/hashes. Record absence rather than inventing a missing primary source.
- **Live text:** fixed English names under `hcg/` (proposed `HCG_CHARTER.md`, `HCG_STUDY_LEDGER.md`, `HCG_CLAIM_REGISTER.md`). Versioned historical ledgers and original reviews are frozen under `evidence/hcg/`; review and release records under `records/hcg/`. Do not silently transform original proofs into live claims.
- Identify proof grades, independent checks, source-reported claims, numerical runs, finite-scope conclusions and counterexamples independently. Retractions and failed proofs survive. Before any novelty claim, request a bounded LIT prior-art check.
- `rtg-sat` is public: third-party papers and licence-restricted original text are **not** copied there without authorization; cite them bibliographically, with exact versions where known. LIT's adopted §8.2 now permits registered satellite consumers to request service but confers no private-repository access or LIT-backed verification. Only `disclosure: citable` material may enter public pipes.
- Any HCG use of RTG material must cite an actual adopted `rtg-corpus` tag and owner RID/section; do not infer the source tag from a similarly named symbol or an HCG summary. RTG geometry motivation does not certify an HCG theorem.

## 5. Proposed batch order and acceptance conditions

| Batch | Output | Acceptance gate |
|---|---|---|
| 0 | This SAT preparation note, linked from the HCG registry row | Advisory only; no owner claim admitted |
| 1 | `upload/hcg-sources` with `SHA256SUMS` and acquisition README | Every available original hashed; third-party rights checked; missing sources named |
| 2 | HCG live charter, source manifest, scoped claim registry and exact (L)/(D)/(H) source dictionary | Owners have compared statements to original bytes and retained all domains/negative findings |
| 3 | Frozen HCG code, witness tables, certificates and historical HHO-track source material | Hash mapping PASS; numerical reports not silently promoted to exact proofs; HHO received copies reconciled |
| 4 | First HCG repository release record, independent co-owner diff review, PI adoption, annotated `hcg-v<version>` tag | Exact payload hashes and release scope; the chat-level v0.2 edition remains separately identified |

**Sequencing:** HHO intake can proceed with received, hash-pinned HCG inputs before HCG publication. For its *owner-dependent scientific conclusions* HHO must name missing HCG dependencies; once HCG is tagged, require a separate HHO consumer reconciliation. HCG and HHO first releases are independent; neither retroactively adopts the other.

## 6. Owner / PI decisions still needed

HCG owners identify their complete original packages, the exact current session ledger and proof/counterexample scope, the applicable source bibliography and the first repository release candidate. The PI decides any change of study scope, adoption and tag. No HCG proof, script run, chat authorization, existing tag or original-source hash is certified by this note alone.
