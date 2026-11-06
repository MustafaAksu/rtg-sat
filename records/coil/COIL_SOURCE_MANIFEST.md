# COIL — source manifest

Every file migrated into `rtg-sat` from the PI's local copies is listed here with the SHA-256 of the bytes received on the `upload/coil-sources` branch, computed by the owner session from those bytes. No hash is taken from a file header, a conversation or memory. A file that was requested but not received is listed as **not available**. This manifest is also the old → new filename map required by `COIL_MIGRATION_NOTE.md` §6.

Columns: `old name` (as in the PI's folder) · `new path` · `kind` (live / frozen / code / output / archive) · `translation` (yes / no / n.a.) · `rights` (own / third-party — third-party content is not migrated) · `SHA-256` (of the uploaded original) · `batch` · `upload commit`.

## Batch 1 — index and charter

| old name | new path | kind | translation | rights | SHA-256 | batch | upload commit |
|---|---|---|---|---|---|---|---|
| `PROGRAM-INDEKSI.md` | `coil/COIL_INDEX.md` | live | yes | own | not available | 1 | — |
| `charter-v0.3.md` | `coil/COIL_CHARTER.md` | live | yes | own | not available | 1 | — |

## Batch 2 — record tool and records

| old name | new path | kind | translation | rights | SHA-256 | batch | upload commit |
|---|---|---|---|---|---|---|---|
| `RMT-v0.3.md` | `coil/COIL_RMT.md` | live | yes | own | not available | 2 | — |
| `RM-01-kayit-v0.1.md` | `coil/records/RM-01.md` | live | yes | own | not available | 2 | — |
| `RM-02-kayit-v0.3.md` | `coil/records/RM-02.md` | live | yes | own | not available | 2 | — |
| `MM-1-minimal-model-extraction.md` | `coil/MM-1.md` | live | yes | own | not available | 2 | — |
| `IDEALOG-coil-RCSJ-eslesmesi.md` | `coil/IDEALOG_COIL_RCSJ.md` | live | yes | own | not available | 2 | — |

## Batch 3 — preregistrations, run reports, campaign compendium

Rows are added when the batch is uploaded (file list in `COIL_MIGRATION_PLAN.md` §2.2).

## Batch 4 — audits, scripts, outputs, archive package

Rows are added when the batch is uploaded (file list in `COIL_MIGRATION_PLAN.md` §2.2).

## RTG inputs (pinned tags)

| COIL use | `rtg-corpus` tag | file | section / RID | grade as stated there |
|---|---|---|---|---|
| RM-01: RTG dyadic generator T | `dyad-v6.4.23` (`e32abf0`) | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` | `DYAD-DEF-PRIMITIVE-MAP` | to be copied verbatim at batch 2 |
| Carrier audit: ringdiag update rule | `legacy-v0.7` (`39307e1`) | `dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` | §3.1; recovery table row `step_inertial` / `deg_vec` | to be copied verbatim at batch 4 |
