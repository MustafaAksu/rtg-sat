# COIL v0.2 — release record (DRAFT, batch 3)

**Status:** DRAFT — not adopted. Follows `coil-v0.1` (batches 1–2, `COIL_v0.1_RELEASE_RECORD.md`). Becomes the adoption record of tag `coil-v0.2` when the PI adopts it. All "adopted" fields read *pending PI adoption*.
**Scope:** frozen preregistrations and run reports placed unchanged with English translations; the campaign compendium as a live document.

## 1. Files in this release

### 1.1 Frozen originals (byte-for-byte; hashes in `evidence/coil/{prereg,run}/SHA256SUMS`, equal to `upload/coil/SHA256SUMS`)

`evidence/coil/prereg/`: PREREG-RM02-N2-v1.0, PREREG-RM02-N3-v1.0, PREREG-MM1-GATE-v1.0, PREREG-MM1-WAVEFORM-HOLDOUT-v1_0, -BOUNDARY-v1_0, -BIRTH-v1_0, PREREG-MM1-WAVEFORM-ISOA-v1.0, -TONGUESET-v1.0, -TONGUESET-v1.0.1-ADDENDUM, -ORTHO-v1.0, PREREG-MM1-RANK-v1.0, PREREG-MM1-RESOLVABILITY-v1.0, -v1.0.1-ADDENDUM, PREREG-MM1-PAIRBC-v1.0.3 (14 files).
`evidence/coil/run/`: RUN-RM02-N2-A-v1.0, RUN-RM02-N3-v1.0-FINAL, RUN-MM1-GATE-v1.0, RUN-MM1-DYAD-v1.0, RUN-MM1-WAVEFORM-v1_0, RUN-MM1-WAVEFORM-ISOA-v1.0, -TONGUESET-v1.0, -ORTHO-v1.0, RUN-MM1-RANK-v1.0, RUN-MM1-RESOLVABILITY-v1.0, RUN-MM1-PAIRBC-v1.0.1 (11 files).

Frozen filenames keep their original names and version strings: they are evidence, not live documents (`COIL_MIGRATION_PLAN.md` §2.2).

### 1.2 Translations

One `<name>.en.md` beside each frozen file, headed "Translation; the frozen original governs" with the original's hash. Rules: `evidence/coil/TRANSLATION_RULES.md`. Translations reproduce the original's statements including later-corrected ones; translator's notes only point to the later document. Translator's notes placed: listed in §3.2 once the translations are complete.

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

(to be filled when the translations are committed)

## 4. Checks

- Frozen bytes: every file's SHA-256 verified equal to its `upload/coil/SHA256SUMS` entry at placement (step-1 commit message lists the check).
- Translations: numeric-token check — every number, label and filename of the original occurs in the translation (script run recorded in the PR).
- No source file edited; no claim corrected inside a translation; no hash or approval invented.

## 5. Revision log

- rev. 1: step 1 (placement) + compendium + this draft.
