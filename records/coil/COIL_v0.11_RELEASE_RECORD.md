# COIL v0.11 — release record (DRAFT): maintenance; reviewed analytic working records linked; checker hardening; errata

**Status:** DRAFT — not adopted. Candidate successor of `coil-v0.10` (`c9f96150f4250d5dc456ae7596ce210621f12029`). A **maintenance** release: no new computation of dynamics, no preregistration, no campaign, no frozen file of an earlier release touched. Scope agreed with the co-owner (16 Nov 2026), who asked that maintenance and any change of scientific status be kept apart: §2 lists them as separate decisions.

## 1. Files

**Analytic working records (reviewed `[SESSION]`; linked, not adopted unless decision S1 says otherwise):**
- `records/coil/COIL_PKAPPA_SCALING_NOTE.md` — on `main` by PR #71 (head `ffcf32c6d5209e383a89e08613e0a9c63d813bb3`, merge `beb40a8`); co-owner reviews `5906961563`, `5917828658` (ACCEPT SCOPED). Check `evidence/coil/code/pkappa_scaling_check.py` with output `evidence/coil/outputs/pkappa_scaling_check.txt`.
- `records/coil/COIL_OFFCLUSTER_OBJECT_NOTE.md` — PR #79 (head `10db926cbe5c782e4bffd9bfcd529f2ce7a01ba9`); co-owner reviews `5920662270`, `5921182988`, `5921512620` (ACCEPT SCOPED). Check `evidence/coil/code/offcluster_object_check.py` with output `evidence/coil/outputs/offcluster_object_check.txt`. If PR #79 is not merged before this release, it reaches `main` with it.

**New maintenance tool:** `evidence/coil/code/monodromy_hardened_check.py` with output `evidence/coil/outputs/monodromy_hardened_check.txt`; rows appended to the two `SHA256SUMS` files.

**Live (changed):** `coil/COIL_CHARTER.md` (§0.3 interfaces; §10.4 pointer), `coil/COIL_INDEX.md` (§3a rows, §6 rows), `REGISTRY.md` (COIL row) at adoption only.

**Unchanged:** every frozen file; the two analytic notes, their check scripts and their outputs exactly as reviewed (the hardening is a separate tool, so the reviewed bytes stand).

## 2. Decisions put to the PI

| # | Decision | Proposed by |
|---|---|---|
| **M1** | **Maintenance** as in §3: the LIT statement of Charter §0.3 corrected; the two notes linked from the Index and Charter §10.4 **as reviewed `[SESSION]` working records**; the hardened check added; the errata of §4 recorded | both sessions |
| **S1** | **Scientific status of the two notes — a separate choice.** (a) *keep them as reviewed working records* (no adopted result; the default of M1); or (b) *adopt their stated, scoped results* — the conditional statements at the scope fixed by the reviews (for the P-κ note: §§2–3 under the conditions of its §5; for the off-cluster note: the sampled-energy agreement, the RW amplitude law, and κ_T as the first detected transverse-rate crossing on the sampled branch), with every open item left open | owner session recommends **(a)** until the LIT reply has fixed the strong null; the co-owner asked only that the choice be explicit |

Under S1 (b) a further row would be added to §5 and the Index rows would read "adopted at `coil-v0.11`, scope: …". Under either choice Charter §9.4 is unchanged: no campaign is opened and S-5 stays open.

## 3. Changes of meaning in live documents

| Document | Place | Before (`coil-v0.10`) | Now |
|---|---|---|---|
| Charter | §0.3 Interfaces | "COIL is not an admitted consumer of LIT (`REGISTRY.md`: \"not yet\")" — stale since the PI's admission of 9 Nov 2026 | COIL is an admitted LIT consumer (`rtg-lit/CONVENTIONS.md` §8.2); admission is not validation; the open request of 14/16 Nov 2026 named, filing not an answer (co-owner finding, review `5890536858`) |
| Charter | §10.4 | — | pointer to the two reviewed working records, marked *not adopted results*, with κ_frac, S-5 and the §9.4 condition open |
| Index | §3a | header "numbers in them are `[EXPLORE]`" | header distinguishes exploration records from analytic notes; two rows added with heads, reviews and scope |
| Index | §6 | — | the three check scripts listed with their status |

## 4. Errata (frozen records are not edited)

- **`records/coil/COIL_v0.4_RELEASE_RECORD.md`** and **`records/coil/COIL_v0.5_RELEASE_RECORD.md`**: their titles still carry "(DRAFT, maintenance)" and "(DRAFT)". Both releases were adopted and tagged (`coil-v0.4`, `coil-v0.5`); the status lines inside the records state the adoption. The titles are a leftover of the drafting step and do not mean the releases are drafts. Under `CONVENTIONS.md` §§1–2 the records and their tags stay as they are; `tools/sat_check.py` will keep reporting the two titles as WARN, which this erratum answers.
- **`evidence/coil/code/offcluster_object_check.py`, K5b**: the printed label "window = one RW period" is wrong. The window is ⌊10/√(aκ)⌋ steps, i.e. about **10 u-units**, while the RW periods there are about 7.7–9.7 u-units. The measured quantity is unchanged and correctly described in the note's table ("slow modulation" = range of window means over that window); the script and its output stay as reviewed. (Co-owner, review `5920662270`.)
- **`offcluster_object_check.py`, `ok`**: K4 has no separate pass condition and solver success, endpoint, finiteness and pair selection were not enforced there; likewise for C4 in `pkappa_scaling_check.py`. Addressed by the separate hardened check (§5), not by editing the reviewed scripts.

## 5. Checks

- `monodromy_hardened_check.py` reproduces C4 (eight Lamé traces) and K4 (four transverse rates, κ_T) under enforced guards — solver success, endpoint reached, finite values, |det M − 1| ≤ 10⁻⁸, unique conjugate pair — with the scientific tolerances of the original checks. **Finding made while writing the negative tests:** `scipy.integrate.solve_ivp` does not stop on a non-finite right-hand side — with a NaN coefficient it kept rejecting steps without returning (stopped after 20 s); a success flag checked after the call can therefore never fire in that case. The hardened tool checks every right-hand-side evaluation. The original C4 and K4 integrations were not affected (their values are finite and reproduced). It shows on six negative tests (non-finite coefficient, terminal event, finite-time blow-up, determinant 1.1, no conjugate pair, two pairs) that each guard stops. Result: see its output.
- `sha256sum -c` passes for both `SHA256SUMS` files.
- `tools/sat_check.py` on this branch: no finding for COIL other than the two title WARNs answered in §4; the one ERROR it reports (`hho-v0.4` tag message lacks three lines) is pre-existing on `main` and HHO-owned.
- No frozen file differs from `coil-v0.10` (`git diff coil-v0.10 -- evidence/coil/prereg evidence/coil/run`, empty).

## 6. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `0000000000000000000000000000000000000000`. Files not listed are inherited unchanged from `coil-v0.10`.

| File | SHA-256 |
|---|---|
| `coil/COIL_CHARTER.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_INDEX.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `records/coil/COIL_PKAPPA_SCALING_NOTE.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `records/coil/COIL_OFFCLUSTER_OBJECT_NOTE.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/pkappa_scaling_check.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/offcluster_object_check.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/monodromy_hardened_check.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/pkappa_scaling_check.txt` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/offcluster_object_check.txt` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/monodromy_hardened_check.txt` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |

**Adoption scope (to be filled by the PI at adoption):** proposed — the files above as they stand at the content commit; everything else inherited from `coil-v0.10`; tag `coil-v0.11`. **Proposed limits of effect:** M1 adopts maintenance only; under S1 (a) the two notes remain reviewed `[SESSION]` working records and no statement in them is an adopted COIL result; Charter §9.4 and §10.4 (S-5) unchanged; no preregistration opened or changed; nothing enters `rtg-corpus` by this adoption.
