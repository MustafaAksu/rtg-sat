# R7 — Linear parts of the formal centralizer of T: proof note v0.1

**Date:** 21 October 2026
**Status:** PROPOSED — `[SESSION-ALG: derived Claude; independent check pending (ChatGPT)]`. Not RTG-adopted. Not "verified" until the verifier's independent check is recorded in the ledger.
**Claim ID:** R7-ALG-01
**Scope:** linear parts only. A classification of the full nonlinear centralizer stays with FMS v0.6.4 (noncanonical).

## 1. Statement

Let T be the primitive dyadic map
T(ρ,η) = (ρ − sin η, η + e^ρ − 1 − sin η)
near its fixed point 0. Let S be a formal power-series map (or a C⁵ germ) with S(0) = 0, DS(0) invertible and S∘T = T∘S.

**Then DS(0) is multiplication by c with c⁶ = 1.** Every such c is realized by S = T^k. In particular no formal or C⁵ map commuting with T has derivative ±J_Q.

## 2. Inputs

- **Chart.** Use the complex coordinate z = ρ + ζ₃η, with ζ₃ = e^{2πi/3}. In it the linear part of T is z ↦ ωz, with ω = ζ₆ = e^{iπ/3} (check NF-01).
- **Normal form.** A polynomial, tangent-to-identity Poincaré–Dulac change of coordinates H brings T to
  T_NF(z) = ωz + τ z²z̄ + τ₃₂ z³z̄² + τ₀₅ z̄⁵ + O(|z|⁶).
  Only resonant monomials remain: z^a z̄^b with a − b ≡ 1 (mod 6). No resonant monomial has even total degree, because a − b and a + b have the same parity.
- **Exact coefficients**, computed in exact Q(ζ₃) arithmetic by `h1_h2_exact_checks.py` (checks NF-02, NF-03):
  - τ = 1/8 − 7√3 i/72 ≠ 0
  - τ₀₅ = 43/17280 − 227√3 i/155520 ≠ 0
- **Consistency with the owner data.** In the same chart, F = T_NF⁶ reproduces both owner coefficients exactly (NF-06, NF-07):
  - μ = −1/2 − 2√3 i/3
  - a₀₅ = −49/8640 − 307√3 i/25920
  
  The iterate identities μ = 6ω̄τ and a₀₅ = 6ω̄τ₀₅ hold exactly (NF-05). So a₀₅ ≠ 0 ⇔ τ₀₅ ≠ 0, and the proof can use T's own coefficients.

**Chart invariance.** H is tangent to the identity in z, so S′ = H⁻¹SH commutes with T_NF and DS′(0) = DS(0). The z̄⁵ coefficient of T_NF is unchanged by the normal-form freedom that remains:
- Resonant changes at degree 3 (z²z̄) affect degree 5 only in the z³z̄² slot.
- Resonant changes at degree 5 commute with the linear part.

## 3. Homological operator

For a homogeneous polynomial P of degree d in (z, z̄), set

  L(P)(z) := P(ωz) − ωP(z).

On a monomial, L(z^a z̄^b) = (ω^{a−b} − ω) z^a z̄^b. So L is diagonal in the monomial basis:
- its kernel is spanned by the resonant monomials;
- its image is spanned by the non-resonant ones.

## 4. Proof

Since DS′(0) commutes with A, which acts as ωz, and ω ∉ ℝ, DS′(0) is complex-linear: S′(z) = cz + S₂ + S₃ + S₄ + S₅ + …, with c ∈ ℂ^×. Write the degree-d part of S′∘T_NF − T_NF∘S′ = 0 as an equation (E_d).

**(E₂) — the quadratic correction vanishes.** T_NF has no quadratic term, so (E₂) reads L(S₂) = 0. There are no resonant quadratic monomials: a + b = 2 gives a − b ∈ {2, 0, −2}, none ≡ 1 (mod 6). Hence **S₂ = 0**.

This is the step the verifier asked for. It closes at degree 2, not degree 4. The reason: T's linear part ω ≠ 1 makes L injective on quadratics. In the route through F = T⁶ alone, whose linear part is the identity, S₂ is constrained only at degree 4, by the bracket condition with F₃. It then feeds into degree 5, which is the contribution FMS v0.6.4 §5.2 warns about. Using T avoids that route.

**(E₃) — |c| = 1.** With S₂ = 0, (E₃) reads

  L(S₃) + c·τz²z̄ − τ(cz)²(c̄z̄) = 0,  i.e.  L(S₃) + τc(1 − |c|²) z²z̄ = 0.

z²z̄ is resonant, so it is not in the image of L. Therefore τc(1 − |c|²) = 0. Since τ ≠ 0 and c ≠ 0, **|c| = 1**. Then L(S₃) = 0, so S₃ is resonant: **S₃ = s z²z̄**.

**(E₄) — the quartic correction vanishes.**
- S₂ = 0, T₂ = 0 and T₄ = 0, so every cross term at degree 4 vanishes.
- S₃∘T needs T₂, and T₃∘S needs S₂, so both contribute nothing at degree 4.
- That leaves L(S₄) = 0, and there are no resonant quartic monomials.

Hence **S₄ = 0**.

**(E₅) — c⁶ = 1.** (E₅) reads

  L(S₅) + [c·T₅(z) − T₅(cz)] + Q₅ = 0,  Q₅ := (degree-5 part of S₃∘T_NF) − (degree-5 part of T₃∘S′).

Expanding with S₃ = s z²z̄ and T₃ = τz²z̄:
- S₃(ωz + τz²z̄) contributes s(2τ + ω²τ̄) z³z̄².
- T₃(cz + s z²z̄) contributes τ(2|c|²s + c²s̄) z³z̄².

So Q₅ lies in span{z³z̄²} and has **no z̄⁵ component**. The z̄⁵ coefficient of c·T₅(z) − T₅(cz) is τ₀₅(c − c̄⁵). z̄⁵ is resonant (−5 ≡ 1 mod 6), so it is not in the image of L. Therefore

  τ₀₅(c − c̄⁵) = 0  ⇒  c = c̄⁵ = c⁻⁵  (using |c| = 1)  ⇒  **c⁶ = 1**.

**Realization.** T^k commutes with T and has linear part ω^k, so all of μ₆ occurs. ∎

## 5. Consequences and limits

- J_Q corresponds to c = i, and i⁶ = −1 ≠ 1. So **no formal or C⁵ map commuting with T has derivative ±J_Q**. The nonlinear 𝓘 = Φ⁻¹J_QΦ commutes with G₆ but cannot be promoted to a symmetry of T.
- The two mechanisms are separate:
  - |c| = 1 comes from the cubic resonance (τ ≠ 0);
  - the restriction from S¹ down to μ₆ comes from the z̄⁵ resonance (τ₀₅ ≠ 0).
- The proof uses only degrees ≤ 5. It says nothing about higher-order terms of S. In particular it does not classify the nonlinear centralizer (for example whether it equals ⟨T⟩ formally).
- The proof does not need the owner's six-step chart. It recomputes μ and a₀₅ from T and matches them exactly, which also independently confirms owner data R4 in the chart z = ρ + ζ₃η.

## 6. What the verifier should check independently

1. The normal-form coefficients τ and τ₀₅, by an independent computation: a different algorithm, or a different coordinate convention followed by transformation back.
2. That Q₅ has no z̄⁵ component (the hand expansion in §4).
3. That the E₂/E₄ vanishing argument is complete: no omitted cross terms at degrees 2 and 4.
4. Optionally, the F-route proof (degree-4 bracket condition on S₂) as a second, independent derivation. Both routes must give the same conclusion.
