# HCG — migration preparation and HHO source-interface note

**To:** HCG owner sessions (Claude and ChatGPT); PI Mustafa Aksu  
**From:** ChatGPT, SAT co-owner  
**Date:** 2026-11-10  
**Status:** SESSION / advisory, pre-intake; not scientific verification, owner adoption, release or a request to retag HCG.  
**Placement:** `records/hcg/HCG_MIGRATION_NOTE.md` (working record until the first HCG repository release).

## 1. Decision and source boundary

HCG (Hodge Conjecture / RTG Complex Geometry and Hodge Realization) is a separate satellite study under `rtg-sat/REGISTRY.md`; it is not an RTG scientific-owner stream. The registry records an HCG **session ledger v0.2 adopted in the conversation on 26 October 2026**, but **no HCG scientific file or adopted `hcg-v*` tag in this repository**. A chat-level edition must not be represented as a tagged repository release.

**PI decision, 10 November 2026 (first-edition policy).** The first HCG repository release is to be `hcg-v0.2`: a **faithful publication of the original chat-adopted v0.2**, followed by a separately reviewed successor (`hcg-v0.3`) for later updates. This is approval of the **edition strategy**, not a claim that the original file is already received, checked or released, nor a substitute for the release record, final integrity checks and PI publication authorization. The original v0.2 must be located and its actual bytes hashed before any release. HCG **makes no claim that the Hodge conjecture or Severn's claim is proved or refuted**; include this exact scope guard in the eventual HCG charter and publication-facing texts.

**Origin and owners (conversation-reported; verify original sessions).** HCG's principal owner sessions are in the **"Hodge Conjecture"** conversation of the RTG Dyadic project (Claude and ChatGPT, with PI Mustafa); this is also the conversation where the separate HHO track opened. An earlier RTG imaginary-unit / Eisenstein conversation may be part of the HCG source lineage: **conversation identity to be identified** by the owners, not presumed. Under the PI's 4 Nov 2026 rule, the conversations in which work was actually done determine session ownership; a third-family external "blind auditor" is a **reviewer, not an owner**.

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
| Governing study ledger | HCG session v0.2 (reported filename `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`); HCG pending-delta log including Δ28 and **reportedly Δ29** (reported `HCG_DSN_v0_3_PENDING_DELTAS`) | Conversation/reviewer-reported only; original versions and whether each delta is pending must be verified; no pending delta is silently adopted |
| Mathematical contracts | Exact (L), (D), (H0)–(H4) definitions, domains, clocks, representations, witness semantics and permitted equivalences | Need the original source text; cannot be supplied by HHO paraphrase |
| Finite witnesses / counterexamples | W5/W6/W7, NEW01–04, G34-BLOCK-01, ESCAPE, C₆ separator, other owner-named gates and their proof/negative verdicts | Inventory and actual statuses must be reconciled with originals |
| Independent HCG evidence | `generic_engine.py`, `cyclic_disc_claude.py`, exact input tables, code and outputs/certificates for witnesses and group computations | Two named scripts exist as **received HCG inputs** in HHO upload PR #16; not an HCG release or scientific replay |
| HCG mathematical provenance | Local discriminant / induced-period notes, review status records (including third-family blind-auditor reports), prior-art/novelty corrections, Severn links, errata, withdrawn arguments, named hypotheses and dependencies | HHO PR #15 / SAT PR #18 review report some items; source claims and exact status unverified here |
| HHO track opened inside HCG | HHO opening note, Δ28, G1–G12 catalogue, first claim register (including R1 d ≥ 53), HHO-SG-1…6 | Preserve as dated *HHO-track source evidence*, not as current HCG-owned HHO science |

The HHO review plan also lists `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md` and an induced-period review as missing to that session. These are **acquisition targets**, not evidence of loss. File names and session-reported hashes must be verified on the bytes actually received. Any unseen item is `not available`.

**Mandatory scope reductions (reviewer-reported; verify against HCG originals).** (i) An edge-flux theorem's *novelty* assertion was withdrawn/restricted after reported prior art by Alexeev–Donagi–Farkas–Izadi–Ortega (Crelle, 2020). Preserve this in the live claim register and cite the exact prior-art result after inspection; do not reassert novelty. (ii) Severn's proposed results remain **CLAIMED**. Checking an individual link or reconstructing a braid certificate is neither verification nor adoption of the entire Severn claim. (iii) The HHO Addendum 17 finding that **(L) alone does not force a split discriminant at the class-datum level** must also be recorded on the HCG side as a scoped negative witness, with its actual source and proof status, without upgrading HHO review evidence to HCG owner science.

**Cross-line consistency guard.** HHO PR #15 reports the HCG-side `d >= 53` claim and an independent HHO-side `d <= 5`, `d = 6`, `d = 7` result family, with potentially different hypotheses: do not put them in one theorem inventory or infer a contradiction until exact source assumptions are recovered. The HHO migration note also identifies the withdrawn `HHO-CONJ-NPL` (C3 x F20 counterexample) and the reported Addendum 17 class-datum witness refuting `(L) => split`. Preserve the corresponding historical originals if received and route scientific custody to HHO; do not promote these into HCG theorems by co-location.

## 3. HCG ↔ HHO interface (no circular adoption)

1. **Scientific ownership.** HCG owns its own study statements, witnesses and engines as reviewed/adopted by its owners and PI; HHO owns its obstruction claims and the decisions on their hypotheses. A HHO claim created in the HCG conversation remains an HHO-track historical input, not an HCG result just because of storage.
2. **Until HCG has a tag.** HHO may keep its needed original HCG sources under `evidence/hho/received/`, unchanged, each with SHA-256, labelled `HCG input; not owner-adopted in rtg-sat; not an HHO result`. PR #16's two scripts are upload evidence at present, **not** a replacement for the complete HCG source package.
3. **After HCG releases.** Each HHO consuming statement is compared against the exact HCG adopted tag, release record, source labels/IDs and hashes. HHO owners decide a scoped re-pin in their own reviewed successor. An HCG tag does not automatically upgrade a HHO claim or validate a copied engine. Do not delete the frozen copies that establish historical HHO provenance.
4. **Reverse flow.** HHO → HCG may occur only with the PI adoption required by `REGISTRY.md`, an explicit owner disposition and an HCG release/import record. HCG may reference HHO research as noncanonical context without adoption. Neither transfer implies an RTG result.
5. **External mathematics.** A reference to a Severn or other third-party theorem retains its bibliographic origin, version and exact hypotheses. A HCG restatement or HHO citation is not an independent verification of that source.

The HHO PR #15 plan records that the PI selected the first HHO target as `(L)+(D) ⇒ [1]` at `d=8` (PI decision, 10 Nov 2026). This is **HHO planning**, not an HCG theorem. HCG Δ28's originally blank P1 decision field remains historical: reconcile its provenance with the later HHO decision without retroactively editing frozen deltas or claiming that all HCG Δ28 decisions are adopted. Check the exact definitions once acquired.

## 4. Intake, copyright and evidence protocol

- **No rewritten originals.** HCG's original owner sessions upload only their own unchanged files on `upload/hcg-sources` with a SHA-256 inventory (branches: `claude/hcg-*` and `chatgpt/hcg-*` for working changes; `upload/hcg-sources` for originals). PI-machine output is received unchanged under a separate source subfolder. If the PI instead supplies bytes, keep that acquisition path explicit. As with HHO PR #16, a source upload is not scientific adoption.
- Create `records/hcg/HCG_SOURCE_MANIFEST.md`: original name, conversation/session, source type (owner-produced / PI-received / third-party), exact hash, new path, version, acceptance status, and any HHO consumer copies/hashes. Record absence rather than inventing a missing primary source.
- **Live text:** fixed English names under `hcg/` (proposed `HCG_CHARTER.md`, `HCG_STUDY_LEDGER.md`, `HCG_CLAIM_REGISTER.md`). Versioned historical ledgers and original reviews are frozen under `evidence/hcg/`; review and release records under `records/hcg/`. Do not silently transform original proofs into live claims.
- **Two independent status axes.** The HCG charter must declare proof/evidence grades separately from **review states** `PROPOSED`, `CHECKED`, `THIRD-FAMILY CHECKED`, `ACCEPTED`; neither a third-family check nor any review status is a proof grade. A third-family blind auditor is a reviewer, **not** a scientific owner or substitute for PI adoption. Identify source-reported claims, numerical runs, independent checks, finite-scope conclusions and counterexamples independently; preserve all retractions and failed proofs. Before any novelty claim, request a bounded LIT prior-art check.
- **Severn's Zenodo deposit and other third-party files.** Check and record the exact deposit version, DOI, licence and redistribution conditions before any public copy. Store third-party originals in `rtg-sat` **only when redistribution is demonstrably permitted**; otherwise cite DOI/version and a SHA-256 of any held copy without publishing restricted bytes. HCG's **own independently reconstructed braid certificates** and reproducible computation outputs may be stored as first-party evidence, with producer/version/input hashes and the distinction from Severn's source reports. Other third-party papers and licence-restricted original text are not copied without authorization; cite them bibliographically, with exact versions where known. LIT's adopted §8.2 now permits registered satellite consumers to request service but confers no private-repository access or LIT-backed verification. Only `disclosure: citable` material may enter public pipes.
- **RTG import provenance.** HCG's Eisenstein / abelian-variety calibration was reportedly imported one-way from an RTG stream. HCG owners must locate its **actual adopted `rtg-corpus` tag, section/RID, assumptions and grade**, then record the import scope in HCG and update `REGISTRY.md`. Until verified, the registry's RTG input field remains **`not set` because the source owner/tag/RID are unverified**. Do not infer a source tag from a similarly named symbol or an HCG summary. RTG geometry motivation does not certify an HCG theorem.

## 5. Proposed batch order and acceptance conditions

| Batch | Output | Acceptance gate |
|---|---|---|
| 0 | This SAT preparation note, linked from the HCG registry row | Advisory only; no owner claim admitted |
| 1 | `upload/hcg-sources` with `SHA256SUMS` and acquisition README | Every available original hashed; third-party rights checked; missing sources named |
| 2 | HCG live charter, source manifest, scoped claim registry and exact (L)/(D)/(H) source dictionary | Owners have compared statements to original bytes and retained all domains/negative findings |
| 3 | Frozen HCG code, witness tables, certificates and historical HHO-track source material | Hash mapping PASS; numerical reports not silently promoted to exact proofs; HHO received copies reconciled |
| 4 | Prepare `hcg-v0.2` first: release record, independent co-owner identity/diff review, PI release decision, annotated tag | Faithful original v0.2 scientific body, verified original hash and publication hashes; no pending Δ content; SAT `CONVENTIONS.md` §§2–2.1 |

**Sequencing:** HHO intake can proceed with received, hash-pinned HCG inputs before HCG publication. For its *owner-dependent scientific conclusions* HHO must name missing HCG dependencies; once HCG is tagged, require a separate HHO consumer reconciliation. HCG and HHO first releases are independent; neither retroactively adopts the other.

## 6. Owner / PI decisions still needed

**First repository tag numbering — DECIDED by the PI on 10 November 2026:** publish the **original chat-adopted v0.2 faithfully as `hcg-v0.2`**; update later as `hcg-v0.3` through a separate review and adoption. The alternative of releasing a new edition first (recorded in the 10 November SAT co-owner review) is **not selected**.

**Faithful-publication contract for `hcg-v0.2`:**
1. Acquire the original chat-adopted v0.2 file **unchanged** via `upload/hcg-sources`. Record its actual SHA-256, exact version, source conversation and acquisition history; do not reconstruct or silently edit it. Preserve the original bytes under frozen evidence.
2. Install the v0.2 scientific content without incorporating any pending deltas (reportedly through Δ29), later witnesses, reinterpretations, claim changes, new proofs or regradings. Verify byte identity where the live file can be identical; if fixed canonical filename/publication metadata requires changes to the live copy, enumerate **every publication-only change**, preserve the original as the comparison base and identify both hashes. Any scientific-body difference blocks a purported faithful v0.2 release until separately reviewed and resolved.
3. Prepare `records/hcg/HCG_v0.2_RELEASE_RECORD.md` with the original and published file hashes, scope, evidence identity, any approved metadata-only differences, missing dependencies and explicit non-claims. Obtain an independent owner review before requesting final PI authorization and annotated-tag publication under SAT `CONVENTIONS.md` §§2–2.1.
4. Keep the Δ records **pending**; do not fill or rewrite original blank fields retroactively. The later HHO PI selection of a d=8 P1 target is recorded as HHO planning and does not amend HCG v0.2. Incorporate accepted successors only in a distinct reviewed `hcg-v0.3` release; HHO re-pinning to HCG v0.2 is a further separate consumer decision.

**Implementation still pending, not a new adoption.** HCG owners must identify the original files, verification scope, external bibliography, source licences and the RTG import tag/RID. The PI's edition-policy decision here is **not** an assertion that any source file has been received, validated, merged or tagged, and is not automatic authorization for a specific unreviewed publication payload. Branch work is on each session's own `claude/hcg-*` or `chatgpt/hcg-*`; first-source uploads use `upload/hcg-sources`. Live records are in English, machine-specific paths are excluded, and release tags are published only by the PI or under explicit PI-authorized single-use workflow rules (`CONVENTIONS.md` §2.1). No HCG proof, script run, original-source hash or first release is certified by this note alone.
