# HHO Addendum 12 — independent review of monomial `G(6,1,6)` witnesses and the dominance obstruction

**Date:** 2026-11-09  
**Reviewer:** ChatGPT / `[SESSION]`. **HHO noncanonical.** No HCG or RTG owner disposition or scientific adoption is implied. Severn A/B/C remain CLAIMED.

## 1. Inputs and evidence scope

- `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (12).md`: targeted Addendum 12, §§A12.0–A12.5, read in full, along with its preceding transition §A11.5. Full-file SHA-256: `5931034dde275dca9959cf2e797fdc4a5bdbd1a50ec404126cc0db000dea00b3`.
- `HHO_G616_D6_BUDGET_v0_1.zip`: entire ZIP; SHA-256 `7ebd3fa9b8af5246a6abc797bc6137b080c5a18dfb4f0e839b868d18a786b729`; **4/4 internal SHA-256 entries valid**. Source code read: `g616.py`, `generic_engine.py`, and `cyclic_disc_claude.py`.
- `HCG_DSN_v0_3_PENDING_DELTAS (6).md`: targeted Δ27/addendum 1 (29 Oct 2026), SHA-256 `1fb44251de898f6fd40c0288a5ed7a73246bbd56fd3e3289142d4c2e47e6b213`. **Nonadopted pending ledger**; this copy is historical, not a verified current governing edition.
- `H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md`: targeted §1(a), SHA-256 `de619ee49b8c9d90819e3ae977d889b3ac9783e84aedcda121e07516f55578b1`.
- `H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md`: read §2 (P1–P8), especially the Hodge-compatible factorization through `Y_tau`, SHA-256 `050c8504edfc73af13d935c8d27925d71fd0ed846395a4bb51cb94976768ec7f`. A **session peer review**, not Severn's governing owner text.
- `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`, SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`, available locally; current adopted identity not verified against a governing release tag in this review.
- **Unmet primary-source dependency:** Severn `hexagon:2610.00387v1` §8 could not be downloaded/read. Public online abstract/version metadata were located, but they do not count as inspection of §8. An exact quotation from this missing text is not supplied. The induced-period argument was independently sourced to the accessible HCG review instead.

## 2. Mathematical verdict

**P1–P3 are genuine nonsplit, balanced, rank-eight finite monodromy data but NOT dominant Hodge-transfer data.** Their base Hurwitz dimension is 17, but their period-map ranks satisfy the much sharper bounds **10, 10 and 9**, respectively. This is a proof-level obstruction from the Hodge-compatible induced-period factorization, not a numerical estimate from a rank-16 period matrix.

### 2.1 Group-theoretic proof: full `G(6,1,6)`, not just `>50,000`

Each source tuple includes a spanning chain of five transposition-type reflections with underlying permutations `(01),(12),(23),(34),(45)`. Thus the permutation image equals `S_6`. Each tuple also includes at least one pure diagonal reflection with eigenvalue a **primitive sixth root of unity** (`D(i,1)` or `D(i,5)`). Conjugation by the monomial permutation lifts sends it to the primitive diagonal reflection in any coordinate, and hence generates the entire diagonal subgroup `(mu_6)^6`. Therefore the generated group is **exactly** the natural monomial group `G(6,1,6)`, of order `6^6*6! = 33,592,320`.

This replaces the supplied BFS result capped at 50,000, which *alone* did not prove the full image or connectedness. The same argument covers P1, P2, P3, Q0 and Q2.

### 2.2 Structural quotient and Hodge factorization

The permutation projection `G(6,1,6) -> S_6` determines a connected six-sheeted cover `Y -> P^1` whose local permutations are **transpositions** at the `T` branches, and identity at the diagonal `D` branches. For a tuple with `t` transposition branches and `s` diagonal branches (`t+s=20`):

`2 gamma - 2 = -12 + t`, so `gamma=(t-10)/2`.

The natural rank-six representation is induced from a rank-one local character on the stabilizer of a sheet. The local system upstairs on `Y` has nontrivial inertia at **exactly one point over each diagonal base branch**. Over each transposition base branch, inertia upstairs is represented by the **square** of an order-two reflection, thus trivial. Therefore the effective upstairs puncture number is `s`.

By Hodge-compatible Shapiro/Frobenius reciprocity and the induced-period factorization checked in the HCG review (§2), the period map factors through a finite cover of `M_(gamma,s)`. Therefore

`rank(dPer_sigma) <= 3 gamma - 3 + s`.

| Case | t | s | gamma | H1-par rank 2gamma−2+s | Period-rank upper bound |
|---|---:|---:|---:|---:|---:|
| P1 | 16 | 4 | 3 | 8 | **10** |
| P2 | 16 | 4 | 3 | 8 | **10** |
| P3 | 14 | 6 | 2 | 8 | **9** |
| Q0 | 16 | 4 | 3 | 8 | **10** |
| Q2 | 16 | 4 | 3 | 8 | **10** |

Dominance `(D)` needs rank 16. **Every one of these cases fails (D)** despite `N=20` and base dimension `N-3=17`.

More generally, in any monomial-induced **rank-one** datum with eight-dimensional parabolic multiplicity space, `2 gamma-2+s=8` implies `s=10-2gamma`. Consequently `rank(dPer) <= gamma+7 <= 12` because `s>=0` gives `gamma<=5`. This recovers the scope of Severn v1's reported monomial exclusion through an independently inspected, HCG-internal mathematical argument. The **exact text** of Severn v1 §8 remains unavailable.

### 2.3 Computational replay

Original source hashes verify 4/4. The exact source parabolic Gram program was rerun with **one line changed only in the displayed BFS group size**: the original `closure_size(gs)` call was replaced by a fixed string to skip an expensive, capped 50,000-element enumeration. All local matrices, parabolic cohomology, cup formula, determinant and Hermitian signature code remained unchanged.

| Case | N | sum rank | dim H1par | determinant | signature | norm class |
|---|---:|---:|---:|---:|---|---|
| P1 | 20 | 20 | 8 | 54 | (4,4) | [2] |
| P2 | 20 | 20 | 8 | 54 | (4,4) | [2] |
| P3 | 20 | 20 | 8 | 27/8 | (4,4) | [2] |
| Q0 | 20 | 20 | 8 | 324 | (4,4) | [1] |
| Q2 | 20 | 20 | 8 | 81 | (4,4) | [1] |

**5/5 replay outputs match** the frozen mathematical results. This is **same-engine replay**, not an independently implemented parabolic Gram formula. A separate `g616_independent_structural.py` checks all five product-one tuples using explicit monomial semidirect-product arithmetic, the group-generation condition, Chevalley–Weil age 10/10, the rank budget and the genus/period upper bounds without importing any source engine. It does not compute the actual derivative matrix of the period map.

## 3. HCG source comparison and correction of interpretation

The **historical** HCG v0.3 pending Δ27 addendum 1 says: `d=6` plus the `(D)` budget forces reflection generation; the reflection-classification stage, including **the monomial exclusion**, leaves `G_34` up to the specified projective/normalizer conditions. Without that exclusion the phrase "hence G34" is incomplete. The 29 Oct second-AI review explicitly lists the monomial rank-six groups and cites Severn v1 §8 for their exclusion. A later 29 Oct HCG review rederives Severn's monomial bound from Hodge-compatible induced-period factorization and states `rank <= 3n =12` for `n=4`.

Therefore these five monomial data **do not contradict** the HCG small-rank screen. They demonstrate sharply why the necessary numerical Hurwitz dimension test cannot be substituted for the actual `(D)` period-dominance condition.

No direct v1 §8 manuscript reading was possible; avoid putting `[OWNER: Severn v1 §8]` on this reconstructed argument.

## 4. Decisions and open obligations

- `[ALG/NUM CHECKED]` P1–P3 are balanced eight-dimensional `[2]` nonsplit parabolic-form data; Q0/Q2 are `[1]` controls.
- `[ALG CHECKED]` Each of the five tuples generates **full** `G(6,1,6)`, not just a subgroup larger than 50,000.
- `[THM — proof checked, inherited factorization]` All five fail `(D)`; bounds 10,10,9,10,10.
- `[OPEN]` Supplier criterion `(L)` for each tuple was **not** checked. It is unnecessary for the negative dominance conclusion.
- `[SOURCE GAP]` Primary Severn v1 §8 text remains to be inspected against the newly direct factorization proof, if owner-source concordance is required. The v0.3 ledger remains nonadopted.
- The broader conjecture `(L)+(D) => split` remains OPEN, with no nonsplit dominant counterexample produced here.

## Next scientific direction

Avoid running a numerical period derivative for P1: the strict analytic upper bound already proves failure of `(D)`. For a genuinely distinguishing test, seek nonsplit tuples whose coefficient representation is **not** induced from a rank-one system; or prove an additional general restriction on induced rank-r systems. Preserve the `(D)` budget as a necessary prefilter rather than a certificate of dominance.
