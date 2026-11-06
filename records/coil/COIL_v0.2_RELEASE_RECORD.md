# COIL v0.2 — release record (DRAFT, batch 3)

**Status:** DRAFT — not adopted. Follows `coil-v0.1` (batches 1–2, `COIL_v0.1_RELEASE_RECORD.md`). Becomes the adoption record of tag `coil-v0.2` when the PI adopts it. All "adopted" fields read *pending PI adoption*.
**Scope:** frozen preregistrations and run reports placed unchanged with English translations; the campaign compendium as a live document.

## 1. Files in this release

### 1.1 Frozen originals (byte-for-byte; hashes in `evidence/coil/{prereg,run}/SHA256SUMS`, equal to `upload/coil/SHA256SUMS`)

`evidence/coil/prereg/`: PREREG-RM02-N2-v1.0, PREREG-RM02-N3-v1.0, PREREG-MM1-GATE-v1.0, PREREG-MM1-WAVEFORM-HOLDOUT-v1_0, -BOUNDARY-v1_0, -BIRTH-v1_0, PREREG-MM1-WAVEFORM-ISOA-v1.0, -TONGUESET-v1.0, -TONGUESET-v1.0.1-ADDENDUM, -ORTHO-v1.0, PREREG-MM1-RANK-v1.0, PREREG-MM1-RESOLVABILITY-v1.0, -v1.0.1-ADDENDUM, PREREG-MM1-PAIRBC-v1.0.3 (14 files).
`evidence/coil/run/`: RUN-RM02-N2-A-v1.0, RUN-RM02-N3-v1.0-FINAL, RUN-MM1-GATE-v1.0, RUN-MM1-DYAD-v1.0, RUN-MM1-WAVEFORM-v1_0, RUN-MM1-WAVEFORM-ISOA-v1.0, -TONGUESET-v1.0, -ORTHO-v1.0, RUN-MM1-RANK-v1.0, RUN-MM1-RESOLVABILITY-v1.0, RUN-MM1-PAIRBC-v1.0.1 (11 files).

Frozen filenames keep their original names and version strings: they are evidence, not live documents (`COIL_MIGRATION_PLAN.md` §2.2).

### 1.2 Translations

One `<name>.en.md` beside each Turkish frozen file (21 of 25; the three WAVEFORM preregs and RUN-MM1-WAVEFORM-v1_0 are English originals and have none), headed "Translation; the frozen original governs" with the original's hash. Rules: `evidence/coil/TRANSLATION_RULES.md` (rule 9, locale number formats, added during the work). Translations reproduce the original's statements including later-corrected ones; translator's notes only point to the later document (§3.2). Produced by four parallel translation passes under the same rules; each pass reported its uncertain renderings, which were left literal, not corrected.

### 1.3 Live document

| Live file | Source (old name) | Source SHA-256 | Translation |
|---|---|---|---|
| `coil/COIL_CAMPAIGN_COMPENDIUM.md` | `KAMPANYA-KUNYESI.md` | see manifest batch-3 row | yes |

## 2. RTG pins

No new RTG material in this batch. Pins unchanged from v0.1.

## 3. Changes of meaning

### 3.1 Campaign compendium (`KAMPANYA-KUNYESI.md` → `coil/COIL_CAMPAIGN_COMPENDIUM.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| K1 | §10 tail "(Old heading: §10 specification)" | "a simple script could check this mechanically; **not yet written**" | the nine-field contract and gates C1–C9 folded into §10 as the certificate's contract; "not yet written" removed | stale text: the certificate exists and was run (same document, §10 head). Flagged earlier by the co-owner review |
| K2 | §6 | no WAVEFORM row | row added: certificate "— (preregs hashed)", experiment "run by the co-owner session; audit `wf_verify.py`", CLI "—" | the certificate's C4 gap; content from the index §5 (RUN by co-owner session, AUDIT by owner session with `wf_verify.py`) |
| K3 | §4 ISOA result | "no fracture in the locked window" | + `[ABSENT-in-window]` | RMT §5b label; same meaning, scope made explicit |
| K4 | §4 RESOLVABILITY result | T = 270 measured, T ≥ 540 LEFT-CENSORED | + T ≥ 8640 `[UNMEASURED]` | the RUN's own status list |
| K5 | §5 decision rule | "Primary from tri0 only" | + path3 decision-free replication; triF rows not measured | scope sentence of RUN-MM1-PAIRBC v1.0.1 |
| K6 | §9 PAIRBC | `phi0_ensemble()` reference | + note that C3 flags this as opaque; enumeration pending | honest state; no values invented |
| K7 | §10 | — | "Pending certificate critique (not yet applied)" paragraph | open items from the consolidation review, listed in the index §8 item 8 |
| K8 | §1 Pair A campaigns | list without WAVEFORM | WAVEFORM added | the campaign ran at Pair A (§4 row 5) |
| K9 | §0 normalisation | K*₁ = γ/(dt·\|σ\|_max) | + σ over the force-Jacobian eigenvalues on the synchronous branch | charter C12 consistency |
| K10 | section order | §8 placed after §10 | §8 before §9 | wording/order only |

### 3.2 Translator's notes placed in frozen-file translations

| File | Note points to | Passage |
|---|---|---|
| `RUN-MM1-GATE-v1.0.en.md` | `RUN-MM1-DYAD-v1.0.md`, `coil/MM-1.md`, `coil/COIL_CHARTER.md` | §3 S3′ blockquote (≥ 2 modes AND periodicity) — superseded by the single-mode tri-dyad fracture (S3″) |
| `RUN-MM1-RANK-v1.0.en.md` | `RUN-MM1-RESOLVABILITY-v1.0.md` | §4 "Next" — T = 270 measured, T ≥ 540 LEFT-CENSORED |
| `PREREG-MM1-RESOLVABILITY-v1.0.en.md` (4 notes) | `PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` §A, §D, §B, §C/G4 | stratification classifier; program-level aggregation; h-grid extension j ≤ 40; censor-aware T_cross |
| `PREREG-MM1-WAVEFORM-ISOA-v1.0.en.md` | `RUN-MM1-WAVEFORM-ISOA-v1.0.md` §2/§4, `coil/MM-1.md` §6a | §5 decision table — zero fracture in the locked window is `[ABSENT-in-window]`, tongue found at κ ≈ 3.10 outside |
| `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.en.md` (3 notes) | `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md` §E/G2b, §D, §A–C | certificate paragraph; Stage B κ de-duplication; T1 |

Translator-flagged renderings left as written (no correction): "Hadi devam" kept as a quoted utterance; `k=2.90` lowercase k in RUN-RM02-N3; the broken LaTeX line break in the addendum's G4 heading preserved byte-for-byte; `\text{}` prose inside LaTeX translated (`\text{ve}` → `\text{and}` etc.); Turkish prose labels in backticks translated (`[eksik — eklendi]` → `[missing — added]`), identifier labels (`P-ara`, `P-κ`) kept.

## 4. Checks

- Frozen bytes: every file's SHA-256 verified equal to its `upload/coil/SHA256SUMS` entry at placement (step-1 commit message lists the check).
- Translations: numeric/label token check run on all 21 — every number and backticked label of each original occurs in its translation, the only differences being the rule-9 locale forms (`270.000` → `270,000`, `70.000` → `70,000`, `200.000` → `200,000`, `%x` → `x%`) and translated Turkish prose labels. Originals re-verified against `SHA256SUMS` after every pass.
- No source file edited; no claim corrected inside a translation; no hash or approval invented.

## 5. Revision log

- rev. 1: step 1 (placement) + compendium + this draft.
- rev. 2: translations complete (21 files, 11 translator's notes); §1.2, §3.2, §4 filled; English originals have no `.en.md`.
