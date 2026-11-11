# HCG v0.4 — release record

**Status:** **ADOPTED** by PI Mustafa Aksu on 11 November 2026 (§8). Publication tag: `hcg-v0.4`, created by the PI on the merge commit of the pull request that carries this record (PR #40).

**Release:** third repository edition of the HCG study. It is the ledger of `hcg-v0.3` with two results of Δ27 added as §6.24. Nothing else of v0.3 changes.

**Prepared by:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Adoption:** PI Mustafa Aksu.

## 1. What this release is

- **Scoped adoption.** The consolidated record is adopted as the governing record. No individual claim becomes ACCEPTED; every claim keeps its own review state.
- **Scope guard.** HCG makes no claim that the Hodge conjecture or Severn's claim is proved or refuted. Severn's Theorem 6.2 (`hexagon:2610.00387v1`) and Theorems A, B, C of `hexagon:2610.00387v2` stay CLAIMED.
- **AI review is not refereeing.** The two new results were each derived by one AI session and proof-reviewed by the other. No third model family and no human has read either proof. No literature search was made, and no novelty is claimed.

## 2. Changes from `hcg-v0.3`

| Item | State in `hcg-v0.4` |
|---|---|
| `HCG-THM-PARABOLIC-DISC-LOCALITY` (§6.24 a) | new; `[THM]`; **CHECKED (two AIs)**. The theorem is the algebraic identity (layer L1). The identification of the form with the parabolic cup pairing (L2, Dettweiler–Wewers) is a stated import. The polarization step (L3, Severn v2 Prop 7.1, unrefereed) is not part of the entry. |
| `HCG-THM-INDUCED-PERIOD-BOUND` (§6.24 b) | new; `[THM]`; **CHECKED (two AIs)**, argument-level reviews. Two coefficient profiles: (i) over K; (ii) over ℂ, period rank only, with no transfer of a K-discriminant or of (L). The (4,4) signature is a hypothesis of the n = 4 application, not of the theorem. |
| Accompanying lines | §1.4 (index); two rows of forbidden readings in §5; one limit in §6.21; import lines in §7; artefact lines in §8; D-10 to D-12 in §9; Appendix A |
| Every other statement, grade, review state, scope guard and OPEN item | unchanged from `hcg-v0.3` |

## 3. Identity of the adopted scientific record

| Item | Value |
|---|---|
| File | `hcg/HCG_STUDY_LEDGER.md` |
| SHA-256 | `51487f925e34f01e0d233d1ff909e29357d3eadbf1b839f79f73e8fe84022949` |
| Reviewed text | DRAFT r2, SHA-256 `a23aef682216df98b578d5ca4744465fa8ec9538b8edde68f8dd0ec9070a39ad`, at commit `e95f92c26844debfe18887ad993a688734791245` of PR #40 |
| Build | `evidence/hcg/verification/make_v04_draft.py`: 19 assertion-gated edits of the ledger at tag `hcg-v0.3` (SHA-256 `fc03e8376eb56c14abeae77c7f20c2fa70723977572744af8a0c4a38dcec814d`) |
| Release transform | `evidence/hcg/verification/release_v04.py`: rebuilds DRAFT r2, checks its hash, applies 12 edits of labels and metadata only |
| Previous edition | `hcg-v0.3` (`records/hcg/HCG_v0.3_RELEASE_RECORD.md`) |

**What the release transform changes.** Title, date, status, build line, "draft" and "proposed" in headings and labels, the PI role line, the version-history heading with the adoption entry, and the footer. No statement, grade, review state, scope guard or OPEN item differs from DRAFT r2.

## 4. RTG inputs (unchanged)

**`dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4`** in `rtg-corpus`; no OFN pin. These are the pins of `hcg-v0.3`, kept by PI decision (§8). The two new results use no RTG input. Nothing in HCG is an RTG result.

## 5. Not part of this release

- **The rest of Δ27:** the open item on nonsplit eightfolds, the d = 6 corollary and the rank-2 census in G₃₄, the normal-reflection lemma, Lemmas E and F, Theorem R, every bound from d ≥ 15 to d ≥ 53, and corrections D-13 and later. **Δ28** (HHO opening) and **Δ29** (positive lane). They stay pending in `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`.
- **Every application of the two results**, including any statement about nonsplit Weil eightfolds or about polarized abelian varieties.
- **HHO.** No HHO claim is an HCG result. HHO's pin of HCG does not change with this release; HHO re-pins only by its own decision.
- **A third-family or human reading** of the two proofs (PI disposition, 11 Nov 2026: not requested for now).
- **A literature search** for earlier proofs. None was made; a search would go through LIT.
- Third-party texts and data (Severn's papers and deposit), which are not stored in this repository.

## 6. Other files changed by this release

| File | Change |
|---|---|
| `hcg/HCG_CHARTER.md` | Status line; the edition table (row for `hcg-v0.4`); the content table (row for §6.24, pending row narrowed); the pending list; one sentence that the RTG pins are unchanged. No rule of the charter changes. |
| `REGISTRY.md` | `hcg` row: governing edition `hcg-v0.4`; RTG inputs unchanged. |
| `evidence/hcg/README.md` | Two labels (`nonsplit8/` and the locality check) now name `hcg-v0.4`. |
| `evidence/hcg/verification/` | New: `make_v04_draft.py`, `release_v04.py`, `replay_d27_core_checks.py`. |
| `records/hcg/HCG_D27_CORE_THEOREMS_ACCEPTANCE_MATRIX.md` | Already on `main` (PR #36, merged as a proposal record). It is the review basis and is not changed here. |

No frozen source file in `evidence/hcg/` or `upload/hcg/` is changed.

## 7. Checks

| Check | Result | By |
|---|---|---|
| Builder: every anchor occurs exactly once in v0.3; untouched text byte-identical | 19/19 | Claude (script); ChatGPT (independent reimplementation of r1, byte-identical; focused read-back of r2) |
| DRAFT r2 hash | `a23aef68…070a39ad` | Claude; ChatGPT |
| Release transform reproduces DRAFT r2 and changes labels and metadata only | pass | Claude |
| Statement of §6.24 against the proof texts (LOC-v0.2, IND) and the core matrix | pass, after S1 and S2 | ChatGPT (PR #40 reviews) |
| Core matrix, revision 2 (`4ccb992a…152402d6`) | ACCEPT SCOPED | ChatGPT (PR #36) |
| Replay of the frozen locality check from repository files (`replay_d27_core_checks.py`; four inputs pinned by full SHA-256) | output byte-identical, 17 PASS lines | Claude (owner-run; not run by the reviewer) |
| New proofs or new computation campaigns for this release | **none** | — |

**Corrections made during review** (PR #40, r1 → r2; none changes an inequality or a proof step): the (4,4) signature stated as a hypothesis of the n = 4 application (S1); the profile over ℂ stated with its embedding, complex realization and dimension (S2); full hash pins in the replay wrapper (E1).

## 8. Decisions

| Decision | By | Entry |
|---|---|---|
| No third-family reading for now; both results stay CHECKED (two AIs) | PI, 11 Nov 2026 | "ispat için üçüncü bir denetçiye şidilik ihtiyaç yok checked kalsın." — as quoted in the ChatGPT review of PR #36 (review `5857656869`) |
| Merge the core matrix as a proposal record; publish the two theorems in a small ledger edition | PI, 11 Nov 2026, 14:10 +03:00 | "1 - öneri kaydı olarak birleştirebiliriz 2- Burada durup iki teoremi küçük bir ledger edisyonunda yayımlamak iyi fikir" |
| Co-owner review of DRAFT r1 | ChatGPT HCG owner session | PR #40 review `5858056324`: scientific core accepted; S1, S2, E1 required. Applied in commit `e95f92c`. |
| Co-owner review of DRAFT r2 | ChatGPT HCG owner session | PR #40 review `5858163145`: ACCEPT SCOPED. |
| Adoption of v0.4 with the scope of §§1–5 | PI, 11 Nov 2026 | "1- İncelenen DRAFT r2'nin `hcg-v0.4` olarak scoped kabulü uygun" |
| RTG pins | PI, same record | "2- RTG pinleri `dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4` korunacak; OFN pini olmayacak. (deften söylendi)" |
| Publication | PI, same record | "3- tagi ben oluştururum" — the PI creates the annotated tag `hcg-v0.4`; the owner session supplies the command. |

The three adoption entries are quoted from the PI decision record on PR #40 (comment `6795173122`, posted from the PI's account on 11 Nov 2026, 14:57 +03:00). The Claude session received them through that record and the PI's relay.

Order: decision → release record → merge → tag (`CONVENTIONS.md` §2).

## 9. Adoption manifest

**Status: ADOPTED (2026-11-11).** SHA-256 of the bytes at the **content commit** `349355e59026200ea834a7e6e1e51ac9a002a56c` (this manifest-only commit follows it). If any listed file changes after this, the hashes are recomputed before the tag.

| File | Role | SHA-256 |
|---|---|---|
| `hcg/HCG_STUDY_LEDGER.md` | the adopted scientific record | `51487f925e34f01e0d233d1ff909e29357d3eadbf1b839f79f73e8fe84022949` |
| `hcg/HCG_CHARTER.md` | charter (governance text; no scientific claim) | `595d90f0e6c37cf70f7d797097cbb373ad824dfab72d5c3e94cca4b27cb92d0a` |
| `records/hcg/HCG_D27_CORE_THEOREMS_ACCEPTANCE_MATRIX.md` | review basis | `4ccb992a4b766e3e5a2a2d357d47db1f9a68ffadb24adbd70a60e042152402d6` |
| `evidence/hcg/verification/make_v04_draft.py` | builder | `2de5b0292b35a7975c25b8669621e59d96967fbc7fd2197ff0aace56d2aeaffa` |
| `evidence/hcg/verification/release_v04.py` | release transform | `f4f0c9f0246ad86185bdd0586de7ed6befda381a396c08f425a9a3f50382af4d` |
| `evidence/hcg/verification/replay_d27_core_checks.py` | replay wrapper | `44bb0e415cde7c9abf289917790c9cf60b40baefbb00c48c03789ab1537fa542` |
| `evidence/hcg/README.md` | evidence index text | `05a21abb75827f1e930e60364459c648ccd9dc103ca1ecce0276d747d99c7cc9` |
| `evidence/hcg/SHA256SUMS` | index of the 754 frozen files (unchanged) | `5950c6c8d1c8ebc22ee904211aecbeb8456f17ac87cb0b96532276d84d260fe3` |
| `REGISTRY.md` | `hcg` row | `af8c4a929582bec9225eac8ba9249f62c8ce04fab3536e061512fee273872465` |
