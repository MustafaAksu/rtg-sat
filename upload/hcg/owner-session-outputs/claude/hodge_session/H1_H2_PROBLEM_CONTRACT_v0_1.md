# H1/H2 Problem Contract v0.1 — for blind independent verification

**Date:** 21 October 2026 · **Deriver:** Claude · **Verifier:** ChatGPT · **Charter:** v0.2
**Purpose:** This file states the problems, conventions and claims. It contains **no** script output. You can verify every claim marked **BLIND** from this file alone. Quantities marked **SEALED** are withheld: compute them yourself and record your values in the ledger before you request the sealed bundle.

---

## 1. Conventions (binding for comparison)

| Item | Convention |
|---|---|
| Real coordinates on one factor | (x, y) ∈ ℝ², lattice ℤ² |
| Complex coordinate | z = x + ζ₃y, with ζ₃ = e^{2πi/3} and ζ₆ = e^{iπ/3} = 1 + ζ₃ |
| Linear data | A = [[1,−1],[1,0]]; B = [[1,−½],[−½,1]]; U = 2A − I = [[1,−2],[2,−1]]; J_Q = U/√3 |
| Forms | dx∧dy(u,w) = u₁w₂ − u₂w₁. A 2-form W acts as ω(u,w) = uᵀWw. |
| Orientation of E | dx∧dy > 0. This is the complex orientation, since Im ζ₃ > 0. |
| Orientation of Eⁿ | dx₁∧dy₁∧…∧dxₙ∧dyₙ > 0 |
| Polarization convention | ω_B(v,w) = B(J_Q v, w) and ω₀ = (2/√3) ω_B |
| Cohomology class of a cycle Z | the Poincaré dual η, defined by ∫_X η ∧ α = ∫_Z α. Curves are oriented by their complex structure. |
| Hodge (k,k) test on a torus | A rational 2k-form is of pure type (k,k) iff it is killed by the derivation of Λ*(H¹) induced by J. Equivalently, since J = U/√3, killed by the integral derivation D_U. Another valid test (invariance under K-characters, Hermitian forms, …) may be used. |
| Automorphism a | the automorphism of E = ℂ/ℤ[ζ₆] induced by A, which is multiplication by ζ₆ |

## 2. H1 claims (all BLIND)

| ID | Claim |
|---|---|
| H1-01 | A² − A + I = 0 |
| H1-02 | A³ = −I and A⁶ = I |
| H1-03 | AᵀBA = B |
| H1-04 | J_Q² = −I and J_QᵀBJ_Q = B |
| H1-05 | A = ½I + (√3/2)J_Q, and J_Q commutes with A |
| H1-06 | In z = x + ζ₃y, A acts as multiplication by ζ₆ and J_Q as multiplication by i |
| H1-07 | A ∈ SL₂(ℤ), so Λ = ℤ[ζ₆] is A-stable |
| H1-08 | The integral centralizer of A in M₂(ℤ) is ℤ[A] = ℤI + ℤA ≅ ℤ[ζ₆] |
| H1-09 | j(E) = 0. Give an exact argument; a numerical cross-check is optional. |
| H1-10 | ω_B = (√3/2) dx∧dy, and ω₀ = dx∧dy with value 1 on the basis (e₁, e₂) |
| H1-11 | ω₀(J·, J·) = ω₀, and ω₀(u, J_Q w) = (2/√3) B(u,w) is symmetric positive definite |

## 3. H2 claims

### 3a. E × E
Define D₁ = {O}×E, D₂ = E×{O}, D₃ = Δ and D₄ = Γ_a.

| ID | Claim | Mode |
|---|---|---|
| H2-01 | The intersection matrix is [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]] | BLIND |
| H2-02 | det M = −3 | BLIND |
| H2-03 | dim_ℚ (H^{1,1} ∩ H²(E², ℚ)) = 4 | BLIND |
| H2-04 | Each [Dᵢ] is of type (1,1) | BLIND |
| H2-05 | The ℤ-span of [D₁], …, [D₄] is saturated in H²(E², ℤ); hence it equals NS(E²). This must be shown **without** using the classical value disc NS = −3. | BLIND |
| H2-06 | C₃ = D₃ − D₁ − D₂ and C₄ = D₄ − D₁ − D₂ are orthogonal to ⟨D₁, D₂⟩, with Gram [[−2,−1],[−1,−2]] | BLIND |

**Request:** report the explicit Poincaré-dual 2-forms of D₁, …, D₄ in your own basis, so that classes can be compared after a change of basis.

### 3b. E⁴ (factors i = 0…3)
The 16 explicit divisors are:
- Fᵢ = pr_i*[pt], for i = 0…3;
- Δᵢⱼ = pr_{ij}*[Δ], for the 6 pairs i < j;
- Γᵢⱼ = pr_{ij}*[Γ_a], for the 6 pairs i < j, with factor i as source and factor j as target.

| ID | Claim | Mode |
|---|---|---|
| H2-07 | All 16 divisors are of type (1,1) | BLIND |
| H2-08 | dim_ℚ of the Hodge classes in H^{2k}(E⁴, ℚ), for k = 0…4, is (1, 16, 36, 16, 1) | BLIND (value already public in charter v0.1) |
| H2-09 | The ℚ-span of products of the 16 divisors fills the full Hodge space in every degree k = 0…4 | BLIND |
| H2-10 | The 16 divisors are a ℤ-basis of NS(E⁴) (index 1) | BLIND |
| H2-11 | The integral index [H^{k,k} ∩ H^{2k}(E⁴, ℤ) : ℤ-span of k-fold divisor products], for k = 2, 3, 4 | **SEALED** — compute and record |

## 4. R7 support: normal form of the primitive map (NF)

T(ρ, η) = (ρ − sin η, η + e^ρ − 1 − sin η). Work in z = ρ + ζ₃η.

| ID | Claim | Mode |
|---|---|---|
| NF-01 | The linear part of T is z ↦ ζ₆z | BLIND |
| NF-02 | A tangent-to-identity polynomial change of coordinates brings T to a normal form T_NF through degree 5 that contains only resonant monomials z^a z̄^b with a − b ≡ 1 (mod 6) | BLIND |
| NF-03 | The coefficients τ (of z²z̄) and τ₀₅ (of z̄⁵) of T_NF | **SEALED** — compute exactly and record |
| NF-04 | F = T_NF⁶ has no even-degree terms through degree 5 | BLIND |
| NF-05 | μ = 6ω̄τ and a₀₅ = 6ω̄τ₀₅, where ω = ζ₆ and μ, a₀₅ are the z²z̄ and z̄⁵ coefficients of F | BLIND, relation only |
| NF-06 | μ = −½ − 2√3 i/3 (the RTG owner value) | BLIND |
| NF-07 | a₀₅ = −49/8640 − 307√3 i/25920 (the RTG owner value) | BLIND |

**Invariance remark** (to verify or refute):
- The z̄⁵ coefficient of T_NF does not depend on the remaining normal-form freedom.
- The z²z̄ coefficient is likewise fixed once the linear chart is fixed.

**R7 proof (R7-ALG-01).** The statement is in charter v0.2, R7. The proof note is in the sealed bundle because it quotes the NF-03 values. Before opening it, you may draft your own proof of the requested sequence: |c| = 1, then vanishing of the quadratic correction, then c⁶ = 1.

## 5. Methods to avoid duplicating
These are the deriver's methods. Please use different constructions where feasible:
- Poincaré duals obtained by pulling back 2-forms along integral parametrizations and inverting the wedge pairing on Λ²ℤ⁴.
- Hodge test via the kernel of the integral derivation D_U on Λ^{2k}ℤ⁸.
- Saturation via Smith normal form (python-flint).
- Normal form via iterated exact Poincaré–Dulac conjugations, using exact arithmetic in ℚ(ζ₃) on truncated polynomials in z and z̄.

## 6. What to return
- For each ID: PASS, FAIL or UNABLE, with your method and exact output.
- Values for H2-11 and NF-03.
- Any convention mismatch, filed in the disagreement log before comparison.
