# COIL — migration plan (owner session)

**To:** PI (Mustafa)
**From:** COIL owner session ("Coil Like" conversation, RTG Dyadic project)
**Date:** 2026-11-04
**Replies to:** `records/coil/COIL_MIGRATION_NOTE.md` (branch `claude/sat-bootstrap`, commit `629cf83`)
**Status:** proposal; becomes binding only by PI decision. Revised 2026-11-04 after the PI's visibility decision (F1/Q1 closed).

---

## 1. Access audit (what was actually checked, 2026-11-04)

| Item | Result | How checked |
|---|---|---|
| `MustafaAksu/rtg-sat` clone | OK — `main` at `4c0a499` (README only) | `git clone`, `git rev-parse` |
| Bootstrap branch | `origin/claude/sat-bootstrap` at `629cf83`; PR #1 **open, not merged** | `git fetch`, `gh api .../pulls` |
| Push permission | OK — `git push --dry-run` of a `claude/coil-*` branch accepted; API reports `push: true` | dry run only; nothing pushed |
| Tags in `rtg-sat` | none yet | `git ls-remote --tags` |
| `MustafaAksu/rtg-corpus` read | OK — public repo, anonymous read, `main` at `1908e15` | clone (shallow) |
| Pin candidate for ringdiag update rule | tag **`legacy-v0.7`** (`39307e1`), `dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` v0.7, ADOPTED 22 Sep 2026; §3.1 QR-defined spark boundary; recovery table row on `step_inertial` / `deg_vec` | tag fetched and file read |
| Pin candidate for RM-01 (dyadic generator T) | tag **`dyad-v6.4.23`** (`e32abf0`), `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` v6.4.23, ADOPTED 30 Oct 2026; `DYAD-DEF-PRIMITIVE-MAP` | tag fetched and file read |
| PI's local source files | **not available** to this session (as the note states) | — |
| Working copies in this session's output folder | present, but **not sources**: they are the session's own drafts and must not be pushed; only files arriving on `upload/coil-sources` are migrated | — |

### 1.1 Findings the PI should see before batch 1

- **F1 — repository visibility. CLOSED.** README and `CONVENTIONS.md` §4 called `rtg-sat` *private*; the GitHub API reports `"private": false`. **PI decision (4 Nov 2026): `rtg-sat` stays public.** Open science applies to COIL's own research, code, outputs, negative results and records; source rights apply to third-party and licence-restricted material, which stays out of `rtg-sat` (`rtg-lit` remains private). README, `CONVENTIONS.md` §4 and the migration note are reworded accordingly in this branch. Consequence for COIL: no COIL batch may include a third-party document; the manifest gets a `rights` column (own / third-party → not migrated).
- **F2 — bootstrap not merged.** `CONVENTIONS.md`, `REGISTRY.md`, `pipes/COIL/`, `records/coil/` exist only on `claude/sat-bootstrap`. This batch-0 branch is based on it (`629cf83`) and its pull request targets `claude/sat-bootstrap`, so that the PI can fold it into PR #1 as one revision; later COIL PRs target `main` after PR #1 merges.
- **F3 — RM-01 version drift.** The local RM-01 record was written against an earlier Dyadic DSN edition. At migration it is pinned at the tag read now (`dyad-v6.4.23`); the batch-2 PR will state whether the T definition the record quotes matches `DYAD-DEF-PRIMITIVE-MAP` at that tag or whether a note is needed. RTG grades are copied as stated at the tag, never strengthened.
- **F4 — `.gitattributes` is `* -text`.** Good: no EOL conversion, so SHA-256 of uploaded files is preserved byte-for-byte. Frozen files must still be uploaded as binary-identical copies (no editor re-save).

## 2. Layout and filename map (proposal)

Live documents → `coil/` (fixed names, no version). Frozen originals → `evidence/coil/` with hashes. Records → `records/coil/`.

### 2.1 Live documents (`coil/`)

| Old (local) | New | Translation | Note |
|---|---|---|---|
| `PROGRAM-INDEKSI.md` | `coil/COIL_INDEX.md` | yes | status map; version narratives move to release record |
| `charter-v0.3.md` | `coil/COIL_CHARTER.md` | yes | declares COIL status labels once (§ "Labels"), with DSN-grade mapping where honest |
| — (new) | `coil/COIL_GLOSSARY.md` | — | Turkish defined terms → English, once |
| `RMT-v0.3.md` | `coil/COIL_RMT.md` | yes | record tool; v0.3.x change log → release record |
| `RM-01-kayit-v0.1.md` (content v0.2) | `coil/records/RM-01.md` *(or `coil/RM-01.md`)* | yes | pins `dyad-v6.4.23` |
| `RM-02-kayit-v0.3.md` | `coil/records/RM-02.md` | yes | |
| `MM-1-minimal-model-extraction.md` | `coil/MM-1.md` | yes | SG-PROG-1 separation note kept |
| `IDEALOG-coil-RCSJ-eslesmesi.md` | `coil/IDEALOG_COIL_RCSJ.md` | yes | mixed-status lines keep their labels |
| `KAMPANYA-KUNYESI.md` | `coil/COIL_CAMPAIGN_COMPENDIUM.md` | yes | "guided reproduction, not self-contained" claim kept |
| `MEMO-REVIEW-gauge-cycle-flux.md` | `coil/MEMO_GAUGE_CYCLE_FLUX.md` | yes | |
| `CASEBOOK-F2-worked-example-h_noise.md` | `coil/CASEBOOK_F2_H_NOISE.md` | yes | T={54,108} validation stays OPEN |
| `AUDIT-CARRIER-COMPLETENESS-v3.1.md` | `coil/AUDIT_CARRIER_COMPLETENESS.md` | yes | **v3.0→v3.1 retraction kept in text**; v1.0/v2.0/v3.0 go to the archive package |
| `AUDIT-R5-PAIR-BC-v1.0.1.md` | `coil/AUDIT_R5_PAIR_BC.md` | yes | |
| `AUDIT-MM1-WAVEFORM-v1.0.md` | `coil/AUDIT_MM1_WAVEFORM.md` | yes | |
| `ringdiag-update-rule-RECOVERED.md` | `coil/RINGDIAG_UPDATE_RULE.md` | yes | pins `legacy-v0.7` |
| `kspark-def-degnorm-RESOLVED.md` | `coil/KSPARK_DEF_DEGNORM.md` | yes | |
| `HANDOVER-*.md` (2) | `records/coil/HANDOVER_RINGDIAG.md`, `records/coil/HANDOVER_KSPARK.md` | yes | closed handovers are records, not live docs |
| `RUNBOOK-N3.md`, `CLI-*.md` (8), `EXEC-PATCH-RM02-N2-001.md` | `evidence/coil/<campaign>/` alongside scripts | translation optional (short) | execution instructions travel with code |

Whether RM records sit in `coil/records/` or flat in `coil/` is a PI choice; the table uses the subfolder.

### 2.2 Frozen files (`evidence/coil/`)

Preregistrations (incl. addenda) and RUN reports are **frozen**: the original Turkish file is stored unchanged with its SHA-256; an English translation sits beside it, headed *"translation; the frozen original governs"*.

```
evidence/coil/
  prereg/   PREREG-RM02-N2-v1.0.md, PREREG-RM02-N3-v1.0.md, PREREG-MM1-GATE-v1.0.md,
            PREREG-MM1-WAVEFORM-{HOLDOUT,BOUNDARY,BIRTH}-v1_0.md,
            PREREG-MM1-WAVEFORM-{ISOA,TONGUESET,ORTHO}-v1.0.md (+TONGUESET v1.0.1 addendum),
            PREREG-MM1-RANK-v1.0.md, PREREG-MM1-RESOLVABILITY-v1.0.md (+v1.0.1 addendum),
            PREREG-MM1-PAIRBC-v1.0.3.md            + *.en.md translations
  run/      RUN-RM02-N2-A-v1.0.md, RUN-RM02-N3-v1.0-FINAL.md, RUN-MM1-DYAD-v1.0.md,
            RUN-MM1-GATE-v1.0.md, RUN-MM1-WAVEFORM-v1_0.md, RUN-MM1-WAVEFORM-{ISOA,ORTHO,TONGUESET}-v1.0.md,
            RUN-MM1-RANK-v1.0.md, RUN-MM1-RESOLVABILITY-v1.0.md, RUN-MM1-PAIRBC-v1.0.1.md   + *.en.md
  code/     n2_dyad_experiment_v1.1.2.py, n2_prereg_certificate.py, n3_ladder_experiment.py,
            n3_prereg_certificate.py, mm1_gate_experiment.py, mm1_certificate.py, wf_verify.py,
            isoa_*.py, tongueset_*.py, ortho_*.py, rank_*.py, resolv_*.py, pairbc_*.py,
            kunye_completeness_certificate.py
  outputs/  n3_merged/, mm1_merged/, isoa_results/, tongueset_results/, ortho_results/,
            rank_results/, resolv_results/, pairbc_results/   (CSV; stored once, as received)
  archive/  COIL_ARSIV_<date>.zip  + SHA256SUMS  (one frozen package of the old ARSIV/; not live)
```

Frozen filenames keep their original names (they are evidence, not live docs); the no-version rule applies to `coil/` only.

### 2.3 Records (`records/coil/`)

`COIL_MIGRATION_NOTE.md` (exists), `COIL_MIGRATION_PLAN.md` (this file), `COIL_SOURCE_MANIFEST.md` (SHA-256 per source + old→new map + "not available" rows), `COIL_v0.1_RELEASE_RECORD.md` (first release), later release records, reviews, closed handovers.

## 3. Batches and pull requests

Each batch: PI uploads the batch's files **unchanged** to `upload/coil-sources` → I record SHA-256 of each in the manifest → I translate/migrate on `claude/coil-batch<N>-<topic>` → PR with the §4 checklist → PI merges (and, for release batches, adopts and tags).

| Batch | Branch | Content | Source files requested from PI | Release |
|---|---|---|---|---|
| 0 | `claude/coil-batch0-plan` | this plan; `COIL_SOURCE_MANIFEST.md` skeleton; `COIL_GLOSSARY.md` skeleton | none | — |
| 1 | `claude/coil-batch1-index-charter` | `COIL_INDEX.md`, `COIL_CHARTER.md` (labels + DSN-grade map), glossary filled | `PROGRAM-INDEKSI.md`, `charter-v0.3.md` | — |
| 2 | `claude/coil-batch2-rmt-records` | `COIL_RMT.md`, RM-01, RM-02, `MM-1.md`, `IDEALOG_COIL_RCSJ.md`; RTG pins (`dyad-v6.4.23`, `legacy-v0.7`) | `RMT-v0.3.md`, `RM-01-kayit-v0.1.md`, `RM-02-kayit-v0.3.md`, `MM-1-minimal-model-extraction.md`, `IDEALOG-coil-RCSJ-eslesmesi.md` | **`coil-v0.1`** after PI adoption of `COIL_v0.1_RELEASE_RECORD.md` |
| 3 | `claude/coil-batch3-prereg-run` | frozen preregs + RUNs with hashes and translations; `COIL_CAMPAIGN_COMPENDIUM.md` | 15 prereg/addendum files, 11 RUN files, `KAMPANYA-KUNYESI.md` | `coil-v0.2` |
| 4 | `claude/coil-batch4-audits-code` | audits, memo, casebook, ringdiag/kspark notes, handovers; scripts, CLI/runbook, outputs; ARSIV frozen package | 3 audits, memo, casebook, 2 RECOVERED/RESOLVED notes, 2 handovers, 20 `.py`, 8 CLI + runbook + exec-patch, 8 result folders, `ARSIV/` as one zip | `coil-v0.3` |

Batch 0 can be pushed now (it contains no source content). Batches 1–4 wait for the corresponding upload.

## 4. Checklist applied to every PR (from the note §6, made mechanical)

1. Every migrated file row in `COIL_SOURCE_MANIFEST.md` has: old name · new path · SHA-256 of the uploaded source (computed by me from the `upload/coil-sources` bytes) · frozen/live · translation yes/no · rights (own work / third-party — third-party content is not migrated, only its bibliographic identity). A file not uploaded is written **"not available"**, never reconstructed.
2. Every claim keeps its COIL label, scope and evidence pointer (prereg / RUN / script / hash). Diff is checked for dropped `[OPEN]`, `[ABSENT-…]`, scope limits, negative results — explicitly: Pair B/C P-κ, v3.0→v3.1 carrier retraction, S-3 negative closure, RANK INCONCLUSIVE, RESOLVABILITY LEFT-CENSORED, S-1/S-2 parked on OPEN-QUOTIENT-EQUILIBRIUM.
3. Notation changes (κ = K/K*₁ with degree-normalised K*₁; β_c = κ/(γdt); a = γdt; |σ|max convention) are listed in the PR description under *meaning changes* vs *wording changes*; meaning changes are repeated in the release record.
4. RTG material appears only with `tag · section/RID · grade as stated`; no RTG grade restated stronger; SG-PROG-1 sentence present in `MM-1.md` and RM-01.
5. No hash, approval, date of adoption or file content is invented; adoption lines say "pending PI adoption" until the PI writes otherwise.
6. Live `coil/` files contain current state only; version narratives were moved to the release record (checked by grep for `v0.`-style change-log lines).
7. Translation of a frozen file is marked *"translation; the frozen original governs"* in its first line and names the original's hash.

## 5. Questions for the PI (decisions that are his)

- Q1 — answered: public (F1).
- Q2 — handled: batch 0 is based on `claude/sat-bootstrap` and targets it (F2).
- Q3 — ARSIV: leave out entirely, or one frozen zip in `evidence/coil/archive/` (plan assumes the zip; it preserves the carrier v1.0→v3.0 provenance chain the archive README was written for).
- Q4 — RM records in `coil/records/` or flat in `coil/`?
- Q5 — Source scope for batch 1: only `PROGRAM-INDEKSI.md` and `charter-v0.3.md`, or the PI's **whole** local folder at once (one upload, hashed once; later batches then only migrate)? A single upload is simpler for hash integrity; batch-wise uploads match the note's pace.

## 6. What this session will not do

Push anything outside `claude/coil-*`; merge; tag; write to `main` or `upload/*`; push the local working copies as if they were sources; write a hash it did not compute from uploaded bytes; translate a frozen file without storing the original beside it.
