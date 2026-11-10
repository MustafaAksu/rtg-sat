# Complex Geometry and Hodge Realization — Standalone Research Charter v0.2

**Date:** 21 October 2026
**Status:** WORKING / NONCANONICAL / NOT RTG-ADOPTED
**Supersedes:** Charter v0.1 (same date)
**Editors:** Claude (v0.2 edits, primary). ChatGPT (independent review of v0.2). PI: Mustafa (acceptance).
**Research setting:** an independent session outside the RTG project. It consumes selected mathematical RTG findings. It is not an RTG stream and must not change any RTG owner DSN.
**Purpose:** test whether a mathematically precise, RTG-inspired choice of complex structure, lattice, polarization or Weil-type signature leads to useful geometric constructions. These constructions must not be presented as a solution of the Hodge conjecture.

## Change log v0.1 → v0.2

| # | Change | Requested by |
|---|---|---|
| C1 | R6 rewritten. Owner local attraction is kept separate from the SESSION result that T and T⁻¹ are not topologically conjugate. The involution and C³ hypotheses are dropped. | Claude; agreed by ChatGPT |
| C2 | R7 now backed by a self-contained proof note (R7-ALG-01). The quadratic correction is shown to vanish at degree 2 in T's own normal-form chart. Status stays PROPOSED until ChatGPT's independent check. | ChatGPT (proof requirement) |
| C3 | R4 owner coefficients μ and a₀₅ independently recomputed from T itself in the chart z = ρ + ζ₃η, and matched exactly. Status PROPOSED. | Claude |
| C4 | §0: two-AI cross-verification protocol, status vocabulary, blind-verification rule, disagreement log and PI acceptance gate added. | Claude + ChatGPT |
| C5 | §3: the integral NS(E²) basis is now proved directly, by computing H^{1,1} ∩ H²(ℤ) and showing saturation. The classical discriminant match is kept as a cross-check only. | Claude |
| C6 | §7: deliverables updated to the actual first package. Working-directory separation rule added. | ChatGPT |

## 0. Working contract

### 0.1 Evidence labels (unchanged)
- Labels: `[RTG-OWNER: owner/version/section/RID]`, `[CLASSICAL: theorem/reference]`, `[SESSION-ALG: derived/checked here]`, `[HYP: unproved]`, `[OPEN: closure criterion]`.
- An RTG owner result stays conditional on its chosen continuous model.
- A SESSION result is never upgraded to owner status by this session.

### 0.2 Scientific firewall and outbound rule (unchanged)
- Mathematics derived from RTG data may be used as mathematical input.
- No integer lattice, abelian variety, Hodge class or orientation is claimed to be an RTG physical object without an additional selection or bridge theorem.
- Results offered back to RTG need a dated, noncanonical handoff note with explicit provenance and a decision by the receiving owner and the PI.
- No direct DSN edits, no implied adoption, and no reciprocal scientific import.

### 0.3 Two-AI cross-verification protocol (new)

**Roles.**
- **H1/H2:** Claude is primary deriver and producer of exact computations; ChatGPT is independent verifier.
- **H3 literature and open-problem identification:** Claude and ChatGPT each work independently, then compare.
- **Acceptance and RTG handoff:** the PI. Both AI reports are inputs.

**Status vocabulary.** Each claim carries exactly one status:
- `PROPOSED`: derived by one AI.
- `CHECKED`: an independent check by the other AI is recorded, with method and output.
- `DISPUTED`: the check failed or disagrees; an entry exists in the disagreement log.
- `ACCEPTED`: PI decision.

`CHECKED` certifies correctness review. `ACCEPTED` certifies adoption into this session's record. Neither implies RTG adoption.

**Independence rule.**
- Re-running the deriver's script is **not** an independent check.
- The verifier first produces its own result, by a different construction, without seeing the deriver's script or output. Only then are the two compared.
- For this purpose the deriver's package is split into a **problem contract**, sent first, and a **sealed results bundle** (script, log, JSON and proof note), sent after the verifier's blind result is recorded.

**Disagreement log.** Disagreements are recorded in `DISAGREEMENT_LOG` (inside `VERIFICATION_LEDGER.md`) with both arguments side by side.
- Neither AI may close a disagreement silently.
- Neither AI may record a check on the other's behalf.
- The PI decides.

**Working-directory separation.**
- Session scripts run in a dedicated directory, separate from RTG scientific scripts.
- RTG sources are imported read-only.
- The first package's script reads no RTG file at all: imported data are hard-coded with provenance in §1.

### 0.4 Independent literature (unchanged)
- Read current primary proofs, not only secondary summaries.
- Reassess the frontier before opening a theorem claim.
- A proof of an already-known case is a verification, not a breakthrough.

## 1. RTG import ledger (one-way)

| Item | Imported object / fact | Authority / grade | Scope and limitation |
|---|---|---|---|
| R1 | A = [[1,−1],[1,0]]; A³ = −I; A⁶ = I | `[RTG-OWNER: DYAD v6.4.18 §§6.1–6.3; GENESIS v2.8.9 §1]` | Selected continuous dyad model. Not a primitive physical lattice. |
| R2 | B = [[1,−½],[−½,1]]; AᵀBA = B | `[RTG-OWNER: DYAD v6.4.18 §6.3 / DYAD-ALG-Q-INVARIANT-FORM]` | Scale fixed by adopted convention. |
| R3 | J_Q = (2A − I)/√3; J_Q² = −I | `[RTG-OWNER: GENESIS v2.8.9 §6.6]` | The **B-quarter-turn**, not a Euclidean 90° turn in raw coordinates. |
| R4 | μ = −½ − 2√3 i/3; a₀₅ = −49/8640 − 307√3 i/25920 in the fixed normal-form chart | `[RTG-OWNER: DYAD v6.4.18 §§6.7, 6.14 / DYAD-THM-C21; DYAD-ALG-NF6]` + `[SESSION-ALG: recomputed from T in chart z = ρ + ζ₃η, exact match — checks NF-06/07; PROPOSED]` | Coefficients are chart-specific. The recomputation fixes the chart as z = ρ + ζ₃η to degree 5, up to resonant freedom that leaves μ and a₀₅ unchanged. |
| R5 | Smooth local flow embedding of T⁶; unique C^∞ tangent-to-identity sixth root; smooth order-six generator G₆ | `[RTG-OWNER: DYAD v6.4.18 §6.17 / DYAD-THM-SMOOTH-EMBEDDING]` | Local smooth-germ existence. Not holomorphic, not a physical selection. |
| R6 | **(a)** The origin is a local attractor of T⁶ (hence of T). **(b)** T is not locally topologically conjugate to T⁻¹ at the origin; no involution, orientation or smoothness hypothesis is needed. | (a) `[RTG-OWNER: DYAD v6.4.19 §6.14 / DYAD-THM-PRIM-CTR]`; (b) `[SESSION-ALG: imported from the 21 Oct 2026 imaginary-unit exchange; PROPOSED]` | (b) follows from (a): a local homeomorphism h with h(0) = 0 and hTh⁻¹ = T⁻¹ would carry the basin of 0 for T onto a basin of 0 for T⁻¹. For T⁻¹ the origin is repelling, so no such basin exists. Concerns the fixed T on the dyadic carrier only, not reversal operations on enlarged state spaces. Supersedes the v0.1 C³-involution formulation. |
| R7 | Every formal or C⁵ map commuting with T has linear part multiplication by c with c⁶ = 1. All six values occur, realized by T^k. In particular no commuting map has derivative ±J_Q. | `[SESSION-ALG: R7-ALG-01, derived Claude; independent check pending (ChatGPT); PROPOSED]`; consistent with `[FMS v0.6.4 §5.2, NONCANONICAL]` | Proof: `R7_CENTRALIZER_LINEAR_PART_PROOF_v0_1.md`. Linear parts only; no classification of the full nonlinear centralizer. Do **not** confuse with Cent_{GL₂(ℝ)}(A) = ℝ[A]^× ≅ ℂ^×. |
| R8 | Programme boundary: notation or representation alone confers no cross-branch or physical status | `[RTG-OWNER: Programme v1.2 SG-PROG-1; OFN v0.10]` | Governs interpretation; not a Hodge proof. |

**Availability/version receipt (from v0.1, verified by ChatGPT).**
- `RTG_DYADIC_OSCILLATOR_DSN_v6_4_19.md` declares PI adoption on 20 Oct 2026. SHA-256 `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`.
- Its new theorem concerns the L-PHASE remainder.
- The R1–R5 mathematics is unchanged from the audited v6.4.18 scientific sections.

**Crucial NON-import.** Λ = ℤ[ζ₆] is a **classically chosen lattice**, motivated by the integral matrix A. It is not an RTG owner claim that the dyad physically selects integer lattice points.

## 2. H1 — The Eisenstein elliptic realization

- **Coordinates.** In the complex coordinate z = x + ζ₃y, A acts as multiplication by ζ₆ and J_Q as multiplication by i. The lattice Λ = ℤ + ℤζ₃ = ℤ[ζ₆] is A-stable, since A ∈ SL₂(ℤ).
- **The curve.** E = ℂ/Λ, with End(E) = ℤ[A] ≅ ℤ[ζ₆] and j(E) = 0.
- **Polarization.** With the declared convention ω_B(v,w) = B(J_Q v, w):
  - ω_B = (√3/2) dx∧dy;
  - ω₀ = (2/√3)ω_B = dx∧dy, with ∫_E ω₀ = 1;
  - ω₀(J·, J·) = ω₀, and ω₀(u, J_Q w) = (2/√3)B(u,w) is positive definite.
  
  So ω₀ is a principal polarization compatible with J_Q.

`[SESSION-ALG; PROPOSED]` This is a representation built with a chosen integral lattice, not a proof that the RTG dynamics selects it.

**H1 exit test:** independent exact checks of claims H1-01 … H1-11 in the problem contract. Every added choice is stated explicitly.

## 3. H2 — Integral Néron–Severi basis and known Hodge rings

**Divisors on X = E×E.** Let
- D₁ = {O}×E,
- D₂ = E×{O},
- D₃ = Δ (the diagonal),
- D₄ = Γ_A (the graph of the automorphism a, represented by A).

Intersection matrix: M = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], with det M = −3.

**Direct integral argument (new in v0.2).**
1. H^{1,1} ∩ H²(ℤ) is computed as the integer kernel of the derivation induced by U = 2A − I, acting factorwise on Λ²ℤ⁴. It has rank 4.
2. The classes [D₁], …, [D₄] lie in it.
3. Their ℤ-span is saturated in Λ²ℤ⁴: all Smith invariants equal 1.

Hence span_ℤ{[Dᵢ]} = H^{1,1} ∩ H²(ℤ) = NS(E²), by Lefschetz (1,1).

The classical identification NS(E²) ≅ U ⊕ A₂(−1), with discriminant −3, is retained only as a **cross-check**. The adjusted classes C₃ = D₃ − D₁ − D₂ and C₄ = D₄ − D₁ − D₂ realize the A₂(−1) summand. The graph classes correspond to the integral operator basis {1, A} of ℤ[A].

**E⁴.**
- Take the 16 explicit divisors pr_i*[pt], pr_{ij}*[Δ] and pr_{ij}*[Γ_A].
- Compute the rational Hodge spaces in H^{2k}(E⁴, ℚ) for k = 0, …, 4, the ranks of the spans of divisor products, and, as information only, the integral indices of the divisor-product lattices inside H^{k,k} ∩ H^{2k}(ℤ).

All of this is **known-case verification**. An integral index > 1, if found, would not by itself bear on the integral Hodge conjecture, because other cycles may exist.

**H2 exit test:** independent verification of claims H2-01 … H2-10 in the problem contract, by a construction different from the deriver's.

## 4. Dynamical incompatibility gate

`[RTG-OWNER: DYAD v6.4.18 §6.7 / DYAD-THM-C21; DYAD v6.4.19 §6.14 / DYAD-THM-PRIM-CTR]` In the chart z = ρ + ζ₃η:

  F(z) = T⁶(z) = z + μz²z̄ + O(|z|⁴),  Re μ = −½.

`[SESSION-ALG; PROPOSED]` It follows that |F(z)|² − |z|² = −|z|⁴ + O(|z|⁵), so the origin is a weak sink. Consequently:
1. T⁶ is not locally the identity, and T is not locally topologically conjugate to any map of finite order dividing 6. Holomorphy is not needed.
2. T is not locally topologically conjugate to T⁻¹ (R6b).
3. By R7, no map commuting with T has derivative ±J_Q. The order-four structure J_Q is representational, not a symmetry of T.

None of this proves that T lacks every algebro-geometric realization on another space. The exact order-six smooth generator G₆ (R5) and the dissipative map T are distinct objects.

## 5. Current external mathematics and frontier

1. `[CLASSICAL: Moonen–Zarhin]` For abelian varieties of dimension ≤ 5, Hodge classes reduce to divisor classes and Weil-type classes. If the Hodge conjecture holds for Weil-type abelian fourfolds, it holds for all abelian fourfolds.
2. `[LITERATURE: Markman 2025; ICM 2026]` Weil classes on **split** Weil-type abelian sixfolds (discriminant −1) are algebraic for every imaginary quadratic field. By a degeneration argument this gives algebraicity for all Weil-type abelian fourfolds, for all fields and discriminants, and hence the Hodge conjecture for all abelian varieties of dimension ≤ 5.
3. `[LITERATURE: Floccari–Fu 2026]` A new proof for Weil fourfolds of discriminant 1 and all their powers. The published sixfold result is for split Weil type only; do not overstate it as covering all sixfolds.
4. **The general Hodge conjecture is unsolved.** A candidate abelian direction is non-split Weil-type sixfolds with K = ℚ(√−3) and discriminant class δ ≠ [−1] in ℚ^×/N_{K/ℚ}(K^×). The exact open subset must be re-established by **both** AIs independently at H3 entry. The alternative is a demonstrably distinct non-abelian variety with an independently formulated open cycle problem.

**Primary references** (both AIs verify versions and dates independently at H3):
- E. Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds* (2025), arXiv:2502.03415.
- E. Markman, *Secant Sheaves and Weil Classes on Abelian Varieties*, ICM 2026, doi:10.1137/25M1803796.
- B. Moonen, Yu. Zarhin, *Hodge classes on abelian varieties of low dimension* (1999), arXiv:math/9901113.
- S. Floccari, L. Fu, *The Hodge conjecture for Weil fourfolds with discriminant 1 via singular OG6-varieties* (2026), doi:10.1016/j.matpur.2026.103876; arXiv:2504.13607.

## 6. H3 — A nontrivial Weil-type or non-abelian research target

This section is unchanged from v0.1 in substance.

**Setup.**
- Fix K = ℚ(√−3) *as a choice motivated by R1–R3*.
- A Weil-type abelian variety Y of dimension 2n needs an algebraic K-action with σ and σ̄ each of multiplicity n on H^{1,0}(Y). In dimension six this is signature (3,3).
- The Weil classes are W_K(Y) = Λ⁶_K H¹(Y,ℚ) ⊂ H^{3,3}(Y) ∩ H⁶(Y,ℚ). This space has dimension 2 over ℚ.

**`[HYP/INTERP]` only.** The two embeddings σ and σ̄ resemble the orientations J_Q and −J_Q. This does **not** mean that half of the dynamical factors physically run as T and half as T⁻¹. R6b shows T and T⁻¹ are dynamically inequivalent, but a signed K-action is not a reversal law.

**Non-frontier control.** E³ × E³ with opposite K-embeddings on the two groups of three factors. Its Hodge classes are known to be algebraic.

**H3 entry gates:**
- an actual algebraic family: period matrix, Riemann form, K-action, positivity;
- the discriminant coset, shown to be outside the split case;
- non-isogeny to products already covered by classical results;
- a rigorous separation of W_K(Y) from divisor products;
- an open algebraicity question confirmed **independently by both AIs** before any RTG-motivated cycle mechanism is proposed.

## 7. Priority and deliverables

**Priority order.**
1. H1 + H2 calibration.
2. Two independent frontier reviews (non-split Weil sixfolds over ℚ(√−3), with negative controls).
3. H3, only after the gates in §6 are met.

**First package (delivered by Claude, 21 Oct 2026).**

| File | Role | Send to verifier |
|---|---|---|
| `HODGE_COMPLEX_GEOMETRY_STANDALONE_CHARTER_v0_2.md` | this charter | now |
| `H1_H2_PROBLEM_CONTRACT_v0_1.md` | definitions, conventions, claims to verify blind | now |
| `VERIFICATION_LEDGER.md` | claim ledger + disagreement log | now |
| `h1_h2_exact_checks.py` | Claude's exact computation | **after** the verifier's blind result |
| `h1_h2_run_log.txt`, `h1_h2_results.json` | Claude's outputs (28/28 PASS) | **after** |
| `R7_CENTRALIZER_LINEAR_PART_PROOF_v0_1.md` | R7 proof note | **after** (contains sealed values) |

Later deliverables: `SOURCE_MANIFEST.md`, H3 literature reports (one per AI), and an optional `RTG_OUTBOUND_HANDOFF.md`. No owner DSN file is edited by this session.

**First prompt to the verifier (ChatGPT):**
> Using only the charter v0.2 and the H1/H2 problem contract, produce your own exact verification of every claim marked BLIND, using constructions different from those suggested as the deriver's method. Record your values for the SEALED quantities before requesting the sealed bundle. Then compare, and file any mismatch in the disagreement log.
