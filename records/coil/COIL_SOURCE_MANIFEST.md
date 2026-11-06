# COIL — source manifest

Every file migrated into `rtg-sat` is listed here with the SHA-256 of the bytes on the `upload/coil-sources` branch (`upload/coil/SHA256SUMS`, PR #3; independently re-verified by the intake review in PR #4), computed from those bytes. **Source of the upload (PI decision, 6 Nov 2026):** the owner session's own artefacts, uploaded by the owner session, not the PI's local copies. No hash is taken from a file header, a conversation or memory. A file referenced but not held is listed as **not available**. A hash certifies **byte identity of the uploaded file only** — not publication rights, not scientific correctness, and not agreement with the PI's local copies. Files that exist only inside a ZIP are identified as `ZIP path + member path + member SHA-256` when they are placed. This manifest is also the old → new filename map required by `COIL_MIGRATION_NOTE.md` §6.

Columns: `old name` (as in the PI's folder) · `new path` · `kind` (live / frozen / code / output / archive) · `translation` (yes / no / n.a.) · `rights` (own / third-party — third-party content is not migrated) · `SHA-256` (of the uploaded original) · `batch` · `upload commit`.

## Batch 1 — index and charter

| old name | new path | kind | translation | rights | SHA-256 | batch | upload commit |
|---|---|---|---|---|---|---|---|
| `owner-session-outputs/PROGRAM-INDEKSI.md` | `coil/COIL_INDEX.md` | live | yes | own | `86dec073a7638e729479157e878f549b0ae6a015544cbf5030ff01a8839a93df` | 1 | `01a262e` |
| `owner-session-outputs/charter-v0.3.md` | `coil/COIL_CHARTER.md` | live | yes | own | `80cbbb236e4c3be874c15b508dbdb5ecb36fb216c2c2a4ff78a3d4f2da7f1e8b` | 1 | `01a262e` |

## Batch 2 — record tool and records

| old name | new path | kind | translation | rights | SHA-256 | batch | upload commit |
|---|---|---|---|---|---|---|---|
| `owner-session-outputs/RMT-v0.3.md` | `coil/COIL_RMT.md` | live | yes | own | `4f60447429d09e95452a132ba4b25004102122ab4c24c4d8ff617aeddcfa3c2b` | 2 | `01a262e` |
| `owner-session-outputs/RM-01-kayit-v0.1.md` | `coil/records/RM-01.md` (path pending Q4) | live | yes | own | `879317e405365172e670d2ee40c2aa15063dd3d9a66625e2940260a17128ad01` | 2 | `01a262e` |
| `owner-session-outputs/RM-02-kayit-v0.3.md` | `coil/records/RM-02.md` (path pending Q4) | live | yes | own | `bcb8f4206d933caf2ac25e76ce328ba1a6c1e97d450c0bea0e0f703f968807b0` | 2 | `01a262e` |
| `owner-session-outputs/MM-1-minimal-model-extraction.md` | `coil/MM-1.md` | live | yes | own | `3ea2067d8a37f8b53c074ecc6004ab96aa827246a4fbe23a474d0213f2994051` | 2 | `01a262e` |
| `owner-session-outputs/IDEALOG-coil-RCSJ-eslesmesi.md` | `coil/IDEALOG_COIL_RCSJ.md` | live | yes | own | `7d61172e7914cd803015c9644754a96745da9fdaaa6f49107799b742ac1aa45d` | 2 | `01a262e` |

## Batch 3 — preregistrations, run reports, campaign compendium

Rows are added when the batch is uploaded (file list in `COIL_MIGRATION_PLAN.md` §2.2).

## Batch 4 — audits, scripts, outputs, archive package

Rows are added when the batch is uploaded (file list in `COIL_MIGRATION_PLAN.md` §2.2).

## Not available

| old name | referenced by | note |
|---|---|---|
| `AUDIT-R5-PAIR-BC-v1.0.md` | `PROGRAM-INDEKSI.md` §9 S-3 (old EXPLORE record) | superseded by `AUDIT-R5-PAIR-BC-v1.0.1.md`, which is held; the v1.0 bytes are not held by the owner session — **not available** |

## RTG inputs (pinned tags)

| COIL use | `rtg-corpus` tag | file | section / RID | grade as stated there |
|---|---|---|---|---|
| RM-01: RTG dyadic generator T | `dyad-v6.4.23` (`e32abf0`) | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` | `DYAD-DEF-PRIMITIVE-MAP` | `[DEF]` `[v6.4.11, provisional]` (as written at the tag) |
| Carrier audit: ringdiag update rule; charter/index: §12.5, OPEN-L0L1-0/-1/-O5, SG-L0L1-6 | `legacy-v0.7` (`39307e1`) | `dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` | §3.1; recovery table row `step_inertial` / `deg_vec`; §12.5; §9 | §12.5 parameter entries `[ONTO legacy]`/`[MATH]`; OPEN items `[OPEN]`; §3.1 numbers `[NUM strong legacy-report]` (as written at the tag) |
| Charter §0.2, §4, §9.0: separation guard SG-PROG-1 | `programme-v1.4` | `dsn/RTG_PROGRAMME_OVERVIEW.md` | SG-PROG-1 | guard, not a graded claim |
| Charter §0.1: nearest-DSN-grade column | `methodology-v1.4` | `dsn/DSN_METHODOLOGY.md` | §8 tag registry | — |
