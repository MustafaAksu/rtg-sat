# HCG v0.5 — release record

**Status:** **ADOPTED** by PI Mustafa Aksu on 12 November 2026, 14:58 +03:00 (§8). Publication tag: `hcg-v0.5`, created by the PI on the merge commit of the pull request that carries this record (PR #53).

**Release:** fourth repository edition of the HCG study. It is the ledger of `hcg-v0.4` with seven results of Δ27 added as §6.25 and one OPEN item. Nothing else of v0.4 changes.

**Prepared by:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Adoption:** PI Mustafa Aksu.

## 1. What this release is

- **Scoped adoption.** The consolidated record is adopted as the governing record. No individual claim becomes ACCEPTED; every claim keeps its own review state.
- **Scope guard.** HCG makes no claim that the Hodge conjecture or Severn's claim is proved or refuted. Severn's Theorem 6.2 (`hexagon:2610.00387v1`) and Theorems A, B, C of `hexagon:2610.00387v2` stay CLAIMED.
- **What the new section says.** Under the standing hypotheses (H) of §6.25, a datum whose image contains a complex reflection has split parabolic cup class; hence a nonsplit datum needs d ≥ 15. **It does not say that nonsplit Weil eightfolds do not exist**, and it says nothing about the Hodge conjecture for them.
- **AI review is not refereeing.** Each new result was derived by one AI session and checked by the other. No third model family and no human has read the proofs (PI standing decision, §8). The classification imports are classical and were not re-read. No literature search was made, and no novelty is claimed.

## 2. Changes from `hcg-v0.4`

| Entry of §6.25 | RID | Grade; state |
|---|---|---|
| (a) rank-2 elements of G₃₄ | `HCG-ALG-G34-RANK2-LOCAL` | `[ALG]`, census `[ALG cert]`; CHECKED (two AIs) |
| (b) the case d = 6 | `HCG-COR-D6-NONSPLIT-NOGO` | `[THM]` with `[assuming:]`; CHECKED (two AIs) |
| (c) reduction to the inducing datum (Lemma E of the log) | `HCG-LEM-INDUCING-DATUM` | `[THM]` with `[assuming:]`; CHECKED (two AIs) |
| (d) the normal reflection subgroup | `HCG-LEM-NONSPLIT8-NORMAL-REFL` | `[THM]` with `[assuming:]`; CHECKED (two AIs) |
| (e) the symmetric-group type (Lemma F) | `HCG-LEM-SYMMETRIC-TYPE-PERIOD-BOUND` | `[THM]` with `[assuming:]`; CHECKED (two AIs) |
| (f) the reflection dichotomy (Theorem R) | `HCG-THM-REFLECTION-DICHOTOMY` | `[THM]` with `[assuming:]`; CHECKED (two AIs) |
| (g) the corollary for d ≤ 14 | `HCG-COR-NONSPLIT8-D14` | `[THM]` with `[assuming:]`; CHECKED (two AIs) |

Also new: **OPEN 11** (`HCG-OPEN-NONSPLIT8`, ACTIVE: nonsplit data under (H) for d ≥ 15); §1.5 (index); three rows of forbidden readings in §5; one limit in §6.21; import lines in §7; artefact lines in §8; corrections D-13, D-14, D-25, D-26 in §9; Appendix A. One paragraph at the end of §6.24 now points to §6.25.

Four RID labels are new in this edition (the pending log had none for these items): `HCG-LEM-INDUCING-DATUM`, `HCG-LEM-SYMMETRIC-TYPE-PERIOD-BOUND`, `HCG-THM-REFLECTION-DICHOTOMY`, `HCG-COR-NONSPLIT8-D14`.

Every other statement, grade, review state and scope guard of `hcg-v0.4`, and OPEN 1–10, are unchanged.

## 3. Identity of the adopted scientific record

| Item | Value |
|---|---|
| File | `hcg/HCG_STUDY_LEDGER.md` |
| SHA-256 | `650c301f8465536705c852113fa7c2e2288d8c3e3cae99fa92a9c466e47bf383` |
| Adopted text | DRAFT r2, SHA-256 `d85e7fac6a9bac1af881595d7c48cc3e76216a17c958d8c70a649a9c8d93beb4`, at commit `6d8b665ad8ba751c1e25aaf9c742b5fc059537d7` of PR #53 |
| Build | `evidence/hcg/verification/make_v05_draft.py`: 25 assertion-gated edits (18 string anchors, 7 line-prefix anchors) of the ledger at tag `hcg-v0.4` (SHA-256 `51487f925e34f01e0d233d1ff909e29357d3eadbf1b839f79f73e8fe84022949`) |
| Release transform | `evidence/hcg/verification/release_v05.py`: rebuilds DRAFT r2, checks its hash, applies 12 edits of labels and metadata only |
| Previous edition | `hcg-v0.4` (`records/hcg/HCG_v0.4_RELEASE_RECORD.md`) |

**What the release transform changes.** Title, date, status, build line, "draft" and "proposed" in headings and labels, the PI role line, the version-history heading with the adoption entry, and the footer. No statement, grade, review state, scope guard or OPEN item differs from DRAFT r2.

## 4. RTG inputs (unchanged)

**`dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4`** in `rtg-corpus`; no OFN pin. Kept by PI decision (§8). The new results use no RTG input. Nothing in HCG is an RTG result.

## 5. Not part of this release

- **The rest of Δ27:** the cyclic separators and search gates of its main entry, and everything from addendum 5 (ii) on — the exclusion of 15 ≤ d ≤ 24 and every bound from d ≥ 25 to d ≥ 53, with their classification imports, and corrections D-15 to D-24. **Δ28** (HHO opening) and **Δ29** (positive lane). They stay pending in `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`.
- **The polarized reading as a result.** §6.25 carries it as one conditional sentence, on Severn v2 Prop 7.1 (unrefereed) and Weil's criterion.
- **HHO.** No HHO claim is an HCG result. HHO's pin of HCG does not change with this release; HHO re-pins only by its own decision.
- **A third-family or human reading** of the proofs, and **a literature search**.
- Third-party texts and data, which are not stored in this repository. Marin–Michel is named in the source notes and is not used.

## 6. Other files changed by this release

| File | Change |
|---|---|
| `hcg/HCG_CHARTER.md` | Status line; the edition table (row for `hcg-v0.5`); the content table (row for §6.25, pending row narrowed); the pending list; the sentences on adoptions and on the RTG pins. No rule of the charter changes. |
| `REGISTRY.md` | `hcg` row: governing edition `hcg-v0.5`; RTG inputs unchanged. |
| `evidence/hcg/README.md` | The column header and the `nonsplit8/` label now name the current edition. |
| `evidence/hcg/verification/` | New: `make_v05_draft.py`, `release_v05.py`, `replay_d27_reflection_checks.py`. |
| The three acceptance matrices in `records/hcg/` | Already on `main` (PRs #44, #47, #50, merged as proposal records). They are the review basis and are not changed here. |

No frozen source file in `evidence/hcg/` or `upload/hcg/` is changed.

## 7. Checks

| Check | Result | By |
|---|---|---|
| Builder: every anchor unique in v0.4; untouched text byte-identical | 25/25 | Claude (script) |
| DRAFT r1 (`a7c8e320…efbe1dbc`) against the three matrices: seven entries, OPEN 11, D-25/D-26 | ACCEPT SCOPED; one clarification requested | ChatGPT (PR #53 review `5872372439`) |
| DRAFT r2 (`d85e7fac…8d93beb4`): the clarification in §6.25 (a) (the values a = 36, 27 are Gram determinants in a basis of two roots; the invariant is the norm class) | applied in the scientific text | Claude. **A co-owner read-back of r2 was requested on PR #53 and was not yet recorded when this record was written**; the final review of the release candidate covers it |
| Release transform reproduces DRAFT r2 and changes labels and metadata only | pass | Claude |
| d = 6 matrix, revision 2 (`529c1b40…b59e97fe`) | ACCEPT SCOPED | ChatGPT (PR #44, review `5860829852`) |
| Lemma E matrix, revision 3 (`56355f09…de113265`) | ACCEPT SCOPED | ChatGPT (PR #47, review `5870547991`) |
| Reflection-dichotomy matrix, revision 1 (`af4b482a…e3558293`) | ACCEPT SCOPED | ChatGPT (PR #50, review `5871517852`) |
| Replay of the three frozen check scripts from repository files (`replay_d27_reflection_checks.py`; all inputs pinned by full SHA-256) | 3/3 byte-identical | Claude (owner-run; the reviewer compared the hashes and did not run it) |
| New proofs or new computation campaigns for this release | **none** | — |

**Corrections made during the reviews** (none changes a result): the local identity of (c) restated as a norm-ratio identity (D-25); the Siegel-space bound of (b) limited to representations over ℚ (D-26); the grade of the corollaries given as `[THM]` with `[assuming:]`, because `[COR]` is the Methodology's tag for a correction notice; the signature (4,4) written into (H); the exclusions for d = 7–11 stated as resting on the budget and classification steps, not on (f); the root-basis qualifier in (a).

## 8. Decisions

| Decision | By | Entry |
|---|---|---|
| Review ceiling: CHECKED (two AIs); no third-family reading for now | PI, 11 Nov 2026, 18:18 +03:00 (standing) | "“CHECKED kalsın, üçüncü denetçi şimdilik yok” aksi PI tarafından bildirilene kadar geçerli." |
| Co-owner reviews of the three acceptance matrices | ChatGPT HCG owner session | PRs #44, #47, #50: ACCEPT SCOPED (§7) |
| Co-owner review of DRAFT r1 | ChatGPT HCG owner session | PR #53 review `5872372439`: ACCEPT SCOPED; one clarification, applied in r2 |
| Adoption of v0.5 with the scope of §§1–5 | PI, 12 Nov 2026, 14:58 +03:00 | "1- Belirtildiği şekilde kabul ediyorum." — in reply to: adoption of DRAFT r2 (SHA-256 `d85e7fac…8d93beb4`) as `hcg-v0.5`, scoped; no claim ACCEPTED; the seven entries stay CHECKED (two AIs) |
| RTG pins | PI, same message | "2- RTG pinleri belirtildiği gibi OFN yok" — in reply to: `dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4` unchanged, no OFN pin |
| Publication | PI, same message | "3- Tagı ben atacağım" — the PI creates the annotated tag `hcg-v0.5`; the owner session supplies the command |

Order: decision → release record → merge → tag (`CONVENTIONS.md` §2).

## 9. Adoption manifest

**Status: ADOPTED (2026-11-12).** SHA-256 of the bytes at the **content commit** `02d0929d26cf9c15f85046208e964936e538114b` (this manifest-only commit follows it). If any listed file changes after this, the hashes are recomputed before the tag.

| File | Role | SHA-256 |
|---|---|---|
| `hcg/HCG_STUDY_LEDGER.md` | the adopted scientific record | `650c301f8465536705c852113fa7c2e2288d8c3e3cae99fa92a9c466e47bf383` |
| `hcg/HCG_CHARTER.md` | charter (governance text; no scientific claim) | `f0636e833d14062506a5de552a9babc486466c4a68973df64128885f380d2620` |
| `records/hcg/HCG_D27_D6_CHAIN_ACCEPTANCE_MATRIX.md` | review basis | `529c1b401827295c794854a73e804be627438f837f280fdff6b632edb59e97fe` |
| `records/hcg/HCG_D27_LEMMA_E_ACCEPTANCE_MATRIX.md` | review basis | `56355f09ec622c1a61a5e9c59bc906eeb89d86976e0f00d392f39107de113265` |
| `records/hcg/HCG_D27_REFLECTION_DICHOTOMY_ACCEPTANCE_MATRIX.md` | review basis | `af4b482a746d1d5a9cfa6618185395572fc9395eb7911024ea21e564e3558293` |
| `evidence/hcg/verification/make_v05_draft.py` | builder | `1b283edde9a77fb2a869feefdfae28ca90eb9ac566eb6e2e51a5cb68c744bdf8` |
| `evidence/hcg/verification/release_v05.py` | release transform | `fb81bb1e7043f3435209527cc8c4b577e689a29fc915bbb3e5f2ded086a890ec` |
| `evidence/hcg/verification/replay_d27_reflection_checks.py` | replay wrapper | `871a6e13d4affd7253ccb381701bb207fbfe9a6683e7626cc20a83de41725c6f` |
| `evidence/hcg/README.md` | evidence index text | `da62b2cb345f601d5e817f700e458e3a367395276cf58a30fcc8ac8a463582d6` |
| `evidence/hcg/SHA256SUMS` | index of the 754 frozen files (unchanged) | `5950c6c8d1c8ebc22ee904211aecbeb8456f17ac87cb0b96532276d84d260fe3` |
| `REGISTRY.md` | `hcg` row | `e1477de4b985a49ed4433bef29b4af4f564db03911d7719e8e1d2d7ce364064a` |
