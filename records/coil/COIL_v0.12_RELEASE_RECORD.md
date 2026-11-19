# COIL v0.12 — release record: maintenance; RTG line reopened for analytic comparison only; RTG pins moved; two reviewed working records linked

**Status:** **CANDIDATE — awaiting PI adoption.** Successor of `coil-v0.11` (`fae159f`; record `records/coil/COIL_v0.11_RELEASE_RECORD.md`).

**PI decisions behind this candidate (all given in chat):**
- **18 Nov 2026:**
  1. the RTG/RM-01 line is reopened, for analytic comparison only;
  2. COIL's RTG pins are updated;
  3. the comparison note is written.
- **19 Nov 2026** ("ikisine de evet"), two questions:
  - prepare `coil-v0.12` right after PR #87, without waiting for the global comparison;
  - use the scope the co-owner proposed (§2).

**Basis.** The candidate is stacked on the head of PR #87 (`5a1a2531b45b2453a0f4a66301ff06552ebd31e2`, co-owner ACCEPT SCOPED, review `5954908020`). If PR #87 is merged first, the release PR adds only the changes of §3. If it is not, PR #87 reaches `main` with this release.

## 1. Files

**Reviewed analytic working records.** These are `[SESSION]` records; they are linked, not adopted (decision S1, §2).

- **`records/coil/COIL_KSEP_WAVEFORM_NOTE.md`**
  - On `main` by PR #85 (head `aa688ac601a2e706fc18e981f8f1c8c252153381`, merge `c5d1e9e`).
  - Co-owner review `5945550412`: SCOPED REVISION; R1–R4 applied in `aa688ac`.
  - Check: `evidence/coil/code/ksep_waveform_comparison.py`, with output `evidence/coil/outputs/ksep_waveform_comparison.txt`.
  - With it, on `main` by the same PR: `records/coil/COIL_LIT_REPLY_20261117_DISPOSITION.md`, and the pipe item `pipes/COIL/20261117-LIT-strong-null-literature-reply.md` (state `dispositioned`, verdict `accept`).
- **`records/coil/COIL_RTG_MM1_COMPARISON_NOTE.md`**
  - From PR #87 (head `5a1a253`).
  - Co-owner reviews: `5953857852` (SCOPED REVISION, R1–R4 applied in `5a1a253`) and `5954908020` (ACCEPT SCOPED).
  - Check: `evidence/coil/code/rtg_mm1_comparison_check.py`, with output `evidence/coil/outputs/rtg_mm1_comparison_check.txt`.
  - **One sentence was added after the acceptance** (§4); the check script and its output are byte-identical to the reviewed head.

**Live documents, changed:**
- **`coil/COIL_CHARTER.md`:**
  - §0.2: RTG line reopened.
  - §0.3: Dyadic pin moved and RECOG pin added; the LIT sentence brought up to date.
  - §9.0 and §9.2: the RTG line's state.
  - §9.4: one bullet.
  - §10.4: pointer to the four reviewed working records.
- **`coil/records/RM-01.md`:** re-pinned to `dyad-v6.4.24`, with the re-pin check; `DYAD-ALG-P6-LINEAR-ORDER` named; the grade of `DYAD-ALG-NOT-AREA-PRESERVING` corrected to `[ALG]`.
- **`coil/COIL_INDEX.md`:**
  - §3a: rows for the two notes.
  - §6: row for their checks, with a warning about the self-writing κ_sep script.
  - §8: item 12, the RTG line.
- **`REGISTRY.md`:** COIL row: governing edition, purpose line and pins.

**Unchanged:** every frozen file. `git diff coil-v0.11 -- evidence/coil/prereg evidence/coil/run` is empty.

## 2. Decisions put to the PI

| # | Decision | State |
|---|---|---|
| **M1** | **Maintenance** as in §3: the RTG line reopened for analytic comparison only; pins `dyad-v6.4.24` and `recog-v0.3.27`; RM-01 re-pinned; the two notes linked **as reviewed `[SESSION]` working records**; REGISTRY row updated | scope chosen by the PI on 19 Nov 2026 (co-owner's proposal); **adoption of this candidate pending** |
| **S1** | **Scientific status of the two notes:** (a) they stay reviewed working records, with no adopted result; or (b) their stated, scoped results are adopted | the co-owner's proposal, accepted by the PI on 19 Nov 2026, is **(a)**; adopting the notes' mathematical findings is left as a separate later decision |

Under S1 (a), none of the following becomes an adopted COIL result:
- κ_sep as a position mechanism (8 of 12 waveforms match on nominal intervals, 7 of 12 on measured points);
- the linear identity between RTG's T at P₁ and the MM-1 spark point at a = 1;
- the exclusion of local C³ conjugacy between iterates of T and of the reduced MM-1 dyad.

## 3. Changes of meaning in live documents

| Document | Place | Before (`coil-v0.11`) | Now |
|---|---|---|---|
| Charter | §0.2, §9.0, §9.2 | RTG line "suspended, deliberately" | reopened 18 Nov 2026 **for analytic comparison only**: existing theorems of the pinned RTG tags applied to COIL's questions; no new orbits, no campaign; a comparison is not a bridge (SG-COIL-1) |
| Charter | §0.3 | Dyadic pin `dyad-v6.4.23`, label "[v6.4.11, provisional]"; "A COIL request to LIT is open" | `dyad-v6.4.24` with its `[scope:]` label (generator selection open, OPEN-P0) and the items the comparison uses; new row `recog-v0.3.27` §6.10; the LIT request answered on 17 Nov 2026 and dispositioned `accept` |
| Charter | §9.4 | — | the RTG-line reopening is analysis, not a campaign; the campaign condition is unchanged |
| Charter | §10.4 | pointer to two working records | pointer to four (adds the κ_sep note and the RTG/MM-1 comparison note), all marked *not adopted results*, with κ_frac, S-5 and §9.4 open |
| RM-01 | header, dynamical-rule row, (a) | pinned at `dyad-v6.4.23`; area-preservation statement shown as `[THM]` | pinned at `dyad-v6.4.24`; re-pin check stated; `DYAD-ALG-NOT-AREA-PRESERVING` `[ALG]` (retagged at v6.4.24; co-owner finding R3); `DYAD-ALG-P6-LINEAR-ORDER` named |
| Index | §3a, §6, §8 | — | rows for the two notes and their checks; item 12 (RTG line: local half done, global half next) |
| REGISTRY | COIL row | `coil-v0.11`; "RM-01 suspended"; pins `dyad-v6.4.23`, … | `coil-v0.12`; RTG/RM-01 reopened for analytic comparison only; pins `dyad-v6.4.24`, `recog-v0.3.27`, `legacy-v0.7`, `programme-v1.4`, `methodology-v1.4` |

**Re-pin check of `dyad-v6.4.24`.** Its release record states that no statement, constant or OPEN status changed, apart from two RID/label changes. The first is `DYAD-ALG-NOT-AREA-PRESERVING`, retagged from `[THM]` to `[ALG]`. The second replaces the bare "provisional" label of `DYAD-DEF-PRIMITIVE-MAP` with a `[scope:]` note; the definition is unchanged.

Every Dyadic RID cited by COIL's live documents is present at both tags. RM-01 is the only live COIL record that showed the retagged grade, and it is corrected.

The other pins (`legacy-v0.7`, `programme-v1.4`, `methodology-v1.4`) are each still the newest tag of their document, so they are unchanged.

## 4. Post-review change and errata

- **Note §4.4, step 1:** one parenthetical sentence was added after the co-owner's ACCEPT SCOPED (`5954908020`), which suggested it, non-blocking. It says real multipliers cannot match. T^k has linear part I or −I when k ≡ 0 or 3 (mod 6). F^m would then need multipliers ±1 with a diagonalisable linear part, and the only candidate, a = 4 at κ = 1, has a Jordan block. This makes explicit a case already covered by the argument; the statement and scope are unchanged. Co-owner confirmation: given in review `5974699838` (ACCEPT SCOPED, with editorial findings E1–E2, applied).
- **Index, process note:** `ksep_waveform_comparison.py` rewrites its own output file when run. A rerun check must therefore compare against the committed file (`git show HEAD:<file>`), not against the working tree. The PR #85 merge showed why: a working-tree comparison passed vacuously. The script is not edited (reviewed bytes).

## 5. Checks

- `rtg_mm1_comparison_check.py`: `RESULT: PASS (L1-L3, N1-N6, P1-P3, G1)`.
- `ksep_waveform_comparison.py`: `RESULT: PASS`. A rerun on the PI's server (python 3.12.3, numpy 2.5.4, scipy 1.18.1) agreed with the committed output on every line except line 1, which records the environment.
- `sha256sum -c` passes for both `SHA256SUMS` files.
- `tools/sat_check.py` on this branch:
  - ERROR `hho-v0.4` (pre-existing, HHO-owned);
  - WARN that REGISTRY names `coil-v0.12` before its tag exists, which the tag resolves;
  - the two title WARNs answered in the `coil-v0.11` record, §4.
- No frozen file differs from `coil-v0.11`.

## 6. Adoption manifest

*Filled at adoption:* the content-commit hash and the SHA-256 of every file in §1 that is changed or added relative to `coil-v0.11`. Files not listed are inherited unchanged from `coil-v0.11`.

**Limits of effect (proposed):**
- M1 adopts maintenance only.
- By S1 (a), the two notes remain reviewed `[SESSION]` working records.
- The pins bind COIL's citations only; nothing in `rtg-corpus` changes and nothing enters it by this adoption.
- The campaign condition of Charter §9.4 and the scientific state of §10.4 (S-5 open) are unchanged; only §10.4's pointer to the working records is updated (co-owner finding E2). SG-COIL-1 is unchanged.
- No preregistration is opened or changed.
