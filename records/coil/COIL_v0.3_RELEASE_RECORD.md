# COIL v0.3 — release record (DRAFT, batch 4)

**Status:** DRAFT — not adopted. Follows `coil-v0.2` (batch 3). Becomes the adoption record of tag `coil-v0.3` when the PI adopts it. All "adopted" fields read *pending PI adoption*.
**Scope:** audits, memo, casebook, the two recovered-rule records, closed handovers, scripts and run instructions, outputs, the frozen archive package. Completes the migration of the owner session's files; after this release the manifest's only "not available" entry is `AUDIT-R5-PAIR-BC-v1.0.md`.

## 1. Files in this release

**Live (`coil/`):** `AUDIT_CARRIER_COMPLETENESS.md`, `MEMO_GAUGE_CYCLE_FLUX.md`, `CASEBOOK_F2_H_NOISE.md`, `RINGDIAG_UPDATE_RULE.md`, `KSPARK_DEF_DEGNORM.md` (sources and hashes: manifest batch-4 rows).
**Records (`records/coil/`):** `HANDOVER_RINGDIAG_UPDATE_RULE.md`, `HANDOVER_KSPARK_DEF.md` — closed handovers, translated in full.
**Frozen (`evidence/coil/audit/`):** `AUDIT-MM1-WAVEFORM-v1.0.md`, `AUDIT-R5-PAIR-BC-v1.0.1.md` + `.en.md`. *(Deviation from the plan §2.1, which listed these as live: they are evidence records of closed campaigns and are kept frozen like RUNs.)*
**Code (`evidence/coil/code/`):** 20 `.py`, 7 `CLI-*.md`, `RUNBOOK-N3.md`, `EXEC-PATCH-RM02-N2-001.md` + 9 `.en.md`.
**Outputs (`evidence/coil/outputs/`):** owner-session result tables; `raw_from_pi/` with the run outputs exactly as received from the PI's machine and the two RTG-session notes. Co-owner review texts and console pastes stay on `upload/coil-sources` only (not placed; recorded in the manifest).
**Archive (`evidence/coil/archive/`):** `COIL_ARSIV_frozen_20261106.zip` (16 members; zip hash + member hashes; PI decision Q3, 6 Nov 2026).

## 2. RTG pins

Unchanged (`legacy-v0.7`, `dyad-v6.4.23`, `programme-v1.4`, `methodology-v1.4`). New quotations from `legacy-v0.7` in this batch: the recovery-table rows on `step_inertial`/`deg_vec`, `build_ringdiag_spec`'s single-term form and the cancelling `(1+eps)` factor, `lyap_qr`'s `lmax` as a volume-growth sum; OPEN-L0L1-0 and OPEN-L0L1-1 status ACTIVE. Copied as written; none restated.

## 3. Changes of meaning

### 3.1 Carrier audit (`AUDIT-CARRIER-COMPLETENESS-v3.1.md` → `coil/AUDIT_CARRIER_COMPLETENESS.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| A1 | header | v3.1 as a correction of v3.0 | current verdict stated first; v3.0 → v3.1 retraction kept as §0 `[COR]` `[RETRACTED]`; history pointer to the archive package | current state only; retraction preserved (note §6) |
| A2 | §5 | "does not hold Pair B/C hostage" | + Pair B/C ran and closed; status parked | state synchronisation |
| A3 | §3 | K*_transverse = 23.305 | + normalisation note (deg_vec = 5, factor 1.25 cancels) | consistency with the `deg_norm` resolution |
| A4 | §8 (new) | — | "what this audit does not establish": no named bridge; 23.305 ≠ recorded Def-C brackets; no RTG re-grading | boundary; the recorded legacy brackets quoted with the tag's grade |

### 3.2 Ringdiag update rule (`ringdiag-update-rule-RECOVERED.md` → `coil/RINGDIAG_UPDATE_RULE.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| G1 | header, §8 | "Open item closed: OPEN-L0L1-0" | OPEN-L0L1-0 is **ACTIVE** at `legacy-v0.7`; the note supplied the artifact identity, closure is RTG's decision | COIL does not close RTG items; status quoted at the tag |
| G2 | §[4] | ε_asym as uniform amplitude 1.25 | + the later resolution: deg_vec = 5, the factor cancels (also stated in LEGACY v0.7's recovery table) | state synchronisation |
| G3 | §[6] | three definitions | + LEGACY v0.7's `lyap_qr` caveat (`lmax` volume-growth sum; θ₀ deletion not justified as the quotient) | quoted at the tag |
| G4 | §[7] | "on-disk presence [UNVERIFIED] pending local check" | unchanged; "not re-run by COIL" added | honest state |
| G5 | note | n = 4 builder | + LEGACY v0.7: the n = 4 builder yields C4, not K4 | quoted at the tag |

### 3.3 K_spark definitions (`kspark-def-degnorm-RESOLVED.md` → `coil/KSPARK_DEF_DEGNORM.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| S1 | Block A conclusion | "a synchronised fixed point does not exist structurally; Def-A undefined on this substrate; Def-C the only valid definition; comparison only via Def-B" | kept as A.1 (as recorded) + **A.2 `[COR]`: superseded** by the carrier audit v3.1 — absolute FP absent (stands); relative equilibrium and twisted equilibrium exist; Def-A definable in the quotient; fallback 23.305 = transverse crossing; open test OPEN-QUOTIENT-EQUILIBRIUM; Def-B after, not instead | the source predates v3.1; its conclusion was the premise v3.1 falsified |
| S2 | "Return note" | "Def-A/Def-C comparison not executable (third branch)" | "not yet executed, not inconclusive-by-construction" | same |
| S3 | Block B | unchanged | unchanged (+ cross-reference to LEGACY v0.7's cancellation statement) | stands |

### 3.4 Memo review (`MEMO-REVIEW-gauge-cycle-flux.md` → `coil/MEMO_GAUGE_CYCLE_FLUX.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| E1 | header | "Source: MM-1 Stream Memo …, 3 Sep 2026" | + the memo itself is **not available** among the uploads | manifest honesty |
| E2 | §5 | `[SUPERSEDED]` section with pointer | one-paragraph summary + pointer; sub-ladder follow-up kept `[OPEN]`, not designed | current state only |
| E3 | §6 | "RPS" unexplained | "(the co-owner session's review/specialisation tool, as named in the memo)" | reader orientation; no claim |

### 3.5 Casebook (`CASEBOOK-F2-worked-example-h_noise.md` → `coil/CASEBOOK_F2_H_NOISE.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| F1 | header | `[DER]` | `[DERIVED]` | label vocabulary |
| F2 | §[COR] order of magnitude | "~4 orders was wrong" | + where the ~4 figure comes from (scan-grid floor 9.1×10⁻¹⁵) | consistency with PR #6 review item 3 and the RUN |
| F3 | proxy definition | h_{sep,d} := 1/S_d(T) | + "output-separation proxy for Y, not h_res" | the RUN's own terminology |
| F4 | open task | "not done" | + index item 7 pointer and sub-ladder prereg pointer | cross-reference |

### 3.6 Translator's notes in frozen translations (batch 4)

| File | Note points to | Passage |
|---|---|---|
| `AUDIT-R5-PAIR-BC-v1.0.1.en.md` | `RUN-MM1-PAIRBC-v1.0.1.md` (PREREG v1.0.3) | Verdict "Pair B/C IS NOT RUN with its current prereg/script; β_c(frac) probably not invariant" → result P-κ, tri0 confirmatory, path3 REPLICATION-CONCORDANT |

No notes in the CLI/RUNBOOK/EXEC-PATCH or AUDIT-MM1-WAVEFORM translations. Translator-flagged renderings left as written: the AUDIT-R5 original's internally inconsistent predicted κ_frac values (7.83/12.22 vs 7.67/11.96 vs "3.5–13.8") reproduced exactly; "P-ara" kept as a label.

## 4. Checks

- Frozen bytes: `SHA256SUMS` in `code/`, `audit/`, `outputs/`, `archive/` all verified; every entry equal to its `upload/coil/SHA256SUMS` entry; zip members verified individually (`MEMBERS_SHA256SUMS`).
- Translations: token check on the 11 frozen translations — every number and backticked label present; only rule-9 locale forms differ (`70.000`/`200.000`/`270.000`/`18.775` → comma form; `%x` → `x%`).
- Live documents: every `[COR]`, retraction, `[OPEN]`, `[UNVERIFIED]`, `[UNRECOVERABLE]` of the sources kept; RTG items quoted at `legacy-v0.7` with their ACTIVE status; no RTG item closed or re-graded by COIL; SG-PROG-1 present in every live file.
- No hash, approval or file content invented. The co-owner memo of 3 Sep 2026 and `AUDIT-R5-PAIR-BC-v1.0.md` are "not available".

## 5. Revision log

- rev. 1: batch 4 complete.
