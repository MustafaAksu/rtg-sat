# COIL v0.11 — release record: maintenance; reviewed analytic working records linked; checker hardening; errata

**Status:** **ADOPTED** by PI Mustafa Aksu on 2026-11-16 (COIL owner session: M1 "evet, hepsi"; S1 "a — incelenmiş çalışma kaydı olarak kalsınlar"), as the candidate stood at head `cb0bb6ffdf1878ba37345640d835f08626b1bb2d` of PR #82; publication tag `coil-v0.11`. **Successor of `coil-v0.10`** (`c9f96150f4250d5dc456ae7596ce210621f12029`). **Review state at adoption:** the scope of this release was proposed by the co-owner (16 Nov 2026, after review `5921512620` of PR #79); **no co-owner review of PR #82 was on record when the PI adopted it.** The record is frozen at adoption; a later review finding goes into a later release. **Post-adoption events (recorded 17 Nov 2026, before publication):** (1) co-owner review `5923410867` of PR #82 (16 Nov 2026, after adoption): ACCEPT SCOPED for the adopted payload — no blocking scientific or status-transfer finding; `monodromy_hardened_check.py` replayed in another environment with byte-identical output after the environment header; three findings on the external publication script (checker outcome suppressed, non-atomic push, manifest rows not checked on the merge commit), answered by a fail-closed publication script outside the release payload; (2) `main` advanced with the publication of `hho-v0.5`, which changed the HHO row of `REGISTRY.md`; `main` was merged into this branch (merge `3a0b439`), the conflict resolved by taking the HHO row from `main` and the COIL row unchanged from the adopted candidate. No COIL content changed; only the manifest row of `REGISTRY.md` and the content commit below moved. A **maintenance** release: no new computation of dynamics, no preregistration, no campaign, no frozen file of an earlier release touched. Scope agreed with the co-owner (16 Nov 2026), who asked that maintenance and any change of scientific status be kept apart: §2 lists them as separate decisions.

## 1. Files

**Analytic working records (reviewed `[SESSION]`; linked, not adopted unless decision S1 says otherwise):**
- `records/coil/COIL_PKAPPA_SCALING_NOTE.md` — on `main` by PR #71 (head `ffcf32c6d5209e383a89e08613e0a9c63d813bb3`, merge `beb40a8`); co-owner reviews `5906961563`, `5917828658` (ACCEPT SCOPED). Check `evidence/coil/code/pkappa_scaling_check.py` with output `evidence/coil/outputs/pkappa_scaling_check.txt`.
- `records/coil/COIL_OFFCLUSTER_OBJECT_NOTE.md` — PR #79 (head `10db926cbe5c782e4bffd9bfcd529f2ce7a01ba9`); co-owner reviews `5920662270`, `5921182988`, `5921512620` (ACCEPT SCOPED). Check `evidence/coil/code/offcluster_object_check.py` with output `evidence/coil/outputs/offcluster_object_check.txt`. If PR #79 is not merged before this release, it reaches `main` with it.

**New maintenance tool:** `evidence/coil/code/monodromy_hardened_check.py` with output `evidence/coil/outputs/monodromy_hardened_check.txt`; rows appended to the two `SHA256SUMS` files.

**Live (changed):** `coil/COIL_CHARTER.md` (§0.3 interfaces; §10.4 pointer), `coil/COIL_INDEX.md` (§3a rows, §6 rows), `REGISTRY.md` (COIL row: governing edition `coil-v0.11`).

**Unchanged:** every frozen file; the two analytic notes, their check scripts and their outputs exactly as reviewed (the hardening is a separate tool, so the reviewed bytes stand).

## 2. Decisions put to the PI — both decided on 16 Nov 2026: **M1 adopted; S1 (a) chosen**

| # | Decision | Proposed by |
|---|---|---|
| **M1** | **Maintenance** as in §3: the LIT statement of Charter §0.3 corrected; the two notes linked from the Index and Charter §10.4 **as reviewed `[SESSION]` working records**; the hardened check added; the errata of §4 recorded | both sessions |
| **S1** | **Scientific status of the two notes — a separate choice.** (a) *keep them as reviewed working records* (no adopted result; the default of M1); or (b) *adopt their stated, scoped results* — the conditional statements at the scope fixed by the reviews (for the P-κ note: §§2–3 under the conditions of its §5; for the off-cluster note: the sampled-energy agreement, the RW amplitude law, and κ_T as the first detected transverse-rate crossing on the sampled branch), with every open item left open | owner session recommends **(a)** until the LIT reply has fixed the strong null; the co-owner asked only that the choice be explicit |

**S1 (a) chosen:** the two notes remain reviewed `[SESSION]` working records; no statement in them is an adopted COIL result. Charter §9.4 is unchanged: no campaign is opened and S-5 stays open.

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

**Status: ADOPTED (2026-11-16).** SHA-256 at the **content commit** `0e7a931b0e116c707bf0a2308d957cae622dd0da`. Files not listed are inherited unchanged from `coil-v0.10`.

| File | SHA-256 |
|---|---|
| `coil/COIL_CHARTER.md` | `5b0f5be48d0974a788cd6eb921a3d56c8b5c4214ea059b05a0e83e7d0fe726cb` |
| `coil/COIL_INDEX.md` | `456535de7dee5337ac2c42086de2327c75a90816ab49496d45898da038dca758` |
| `records/coil/COIL_PKAPPA_SCALING_NOTE.md` | `f0e5090a1ee8a672f4d5cee6b5fc25cd8892848e293805e86af7bb8baf45cac6` |
| `records/coil/COIL_OFFCLUSTER_OBJECT_NOTE.md` | `6602ef6a89a53e8f151b642617d5a4f7678da4a8d8f57c8a361142faed423bde` |
| `evidence/coil/code/pkappa_scaling_check.py` | `cb704847fca1a13b9c4f22d9d54230a8bdf6ad21a719e75ed828589567b1ad10` |
| `evidence/coil/code/offcluster_object_check.py` | `404aa31ed9ce95e33585e074dd9758675f1bd8f24c45c9e2cfe3faeb45c7416d` |
| `evidence/coil/code/monodromy_hardened_check.py` | `830210be7a68cdae255ba2c8422a8da3c12f099b30db9624be4114a526ec6ea8` |
| `evidence/coil/code/SHA256SUMS` | `45ef3e93f1f53fd3fc694264738ad60d6b9bc7ab640498c76e39bf1e2f928447` |
| `evidence/coil/outputs/pkappa_scaling_check.txt` | `24648f3d37b91aea0dabca95dd843ad30d2f9d77e7d4bb7dc7d01f08d2bba6b8` |
| `evidence/coil/outputs/offcluster_object_check.txt` | `055427a4645a28e94c1f01c54b35bb962d23104c9a060eea2cb72928901e1fab` |
| `evidence/coil/outputs/monodromy_hardened_check.txt` | `12c6385fb2d0cc798a1b2c22fceaaf04370f1a6dcbc97e8c2225540144f7cc3f` |
| `evidence/coil/outputs/SHA256SUMS` | `657b8fb939815b7ee3b03ddbbfc1c190eb566e898cfdf31a974590235b381c40` |
| `REGISTRY.md` | `ae62af52a160254a56b525ec07d6bc52e72335ff39d1eccbe441ea82619e1624` |

**Adoption scope (PI, 2026-11-16):** the files above as they stand at the content commit; everything else inherited from `coil-v0.10`; tag `coil-v0.11`. **Limits of effect:** M1 adopts maintenance only; by S1 (a) the two notes remain reviewed `[SESSION]` working records and no statement in them is an adopted COIL result; the hardened check is a maintenance tool, not a certificate; Charter §9.4 and §10.4 (S-5) unchanged; no preregistration opened or changed; nothing enters `rtg-corpus` by this adoption.
