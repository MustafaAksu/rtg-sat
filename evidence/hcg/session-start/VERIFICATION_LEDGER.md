# Verification Ledger — Hodge & Complex Geometry Session

**Opened:** 21 October 2026. **Charter:** v0.2.
**Status vocabulary:**
- `PROPOSED`: derived by one AI.
- `CHECKED`: an independent check by the other AI is recorded.
- `DISPUTED`: see the disagreement log.
- `ACCEPTED`: PI decision.

**Rule:** only the checking AI may fill its own "Independent check" cell. Only the PI may fill "PI decision".

## Claims

| Claim ID | Statement (short) | Derivation | Independent check | Status | Evidence | PI decision |
|---|---|---|---|---|---|---|
| H1-01…H1-11 | Eisenstein realization of (A, B, J_Q); E = ℂ/ℤ[ζ₆]; principal polarization ω₀ | Claude — `h1_h2_exact_checks.py`, 11/11 PASS | — | PROPOSED | script SHA-256 `3b3deb4c5db2636f6b41ad434e38e7f7614ae0efef40e1dd5828355a72fc5049` | — |
| H2-01…H2-06 | NS(E²) = ℤ⟨D₁, D₂, Δ, Γ_A⟩, direct saturation proof; det M = −3; A₂(−1) block | Claude — same script, 6/6 PASS | — | PROPOSED | same | — |
| H2-07…H2-10 | E⁴: Hodge dims (1, 16, 36, 16, 1); divisor products span all Hodge classes; 16 divisors are a ℤ-basis of NS(E⁴) | Claude — same script, 4/4 PASS | — | PROPOSED | same | — |
| H2-11 | Integral indices of divisor-product lattices, k = 2, 3, 4 (informational) | Claude — value SEALED | — | PROPOSED | `h1_h2_results.json` (sealed) | — |
| NF-01…NF-07 | Normal form of T; τ, τ₀₅ ≠ 0; μ and a₀₅ recomputed from T, exactly equal to the owner values | Claude — same script, 7/7 PASS | — | PROPOSED | same; values SEALED | — |
| R6b | T is not locally topologically conjugate to T⁻¹ | Claude (21 Oct imaginary-unit exchange); agreed in principle by ChatGPT | — (agreement recorded; a formal check has not been filed) | PROPOSED | charter v0.2 R6 | — |
| R7-ALG-01 | Linear parts of the formal or C⁵ centralizer of T are exactly μ₆ | Claude — proof note v0.1 | — (ChatGPT required the vanishing of the quadratic correction; addressed at degree 2, see note §4) | PROPOSED | `R7_CENTRALIZER_LINEAR_PART_PROOF_v0_1.md` SHA-256 `2ba2653f078031e69db23e73f66f8e103af0d4a8f6a55321bbb9d5a1e13e5949` | — |

**Run environment of the derivation:** Python 3.13, SymPy 1.14.0, python-flint 0.9.0, mpmath 1.3.0. Runtime about 1 s. Exit code 0.

## DISAGREEMENT_LOG

| # | Claim ID | Claude's position | ChatGPT's position | Opened | Resolution (PI) |
|---|---|---|---|---|---|
| — | — | — | — | — | — |
