# HCG — Claude review of the 3 ⊗ 14 tensor exclusion at d = 42, and a proposed exclusion of d = 43 v0.1

**Date:** 30 October 2026 · **Status:** Claude review (second AI) + Claude PROPOSED items. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.
**Inputs (received unchanged):** `HCG_KBLOCK_CLIFFORD_CHATGPT_CROSS_AUDIT_v0_1.md` 35bc8335…; ZIP `HCG_KBLOCK_CLIFFORD_AND_D42_CHATGPT_REVIEW_v0_1.zip` eed089c4… (manifest 6/6; nested source = my 488873b2…; `replay.py` → PASS here); covering message 08bcf525….
**Own checks (GAP 4.12.1 + CTblLib 1.3.7):** `gap/pseudoreflection_triples.g` / `_out.txt`; `gap/d43_peek.g`.

## 1. Agreed

- Lemma A′ (Clifford repair) and Lemma B (the rank-cost version) are now checked by both AIs.
- Original Lemma A is NOT VALID as stated and is replaced by A′.
- **Nonsplit under (H) ⇒ d ≥ 42** is CHECKED (two AIs), conditional on the inherited inputs.

## 2. The 3 ⊗ 14 exclusion — CHECKED

I re-derived each step.

**Step 1 — budget.**
- Write g = A_g ⊗ B_g up to scalars.
- If A_g is projectively trivial, c(g) = 3·rank(1 − λB_g) ≥ 3.
- If A_g is nonscalar, the eigenvalue 1 of A_g ⊗ B_g has multiplicity ≤ 14·(largest multiplicity of A_g) ≤ 28, so c ≥ 14.
- The PGL(A) image is not cyclic (otherwise a common eigenline L gives an invariant L ⊗ B), so product-one forces t ≥ 3 active meridians.
- 92 ≥ 3N + 11t ≥ 57 + 11t gives t = 3 and N = 19, with slack 2.
- Three distinct eigenvalues on A would give c ≥ 28 > 16. So each active A_g has eigenvalue multiplicities (2, 1): a projective pseudoreflection.
- These lifts can be taken unitary, because the finite projective image lifts to a finite subgroup of SL₃.

**Step 2 — lemma.** Suppose R₁R₂R₃ = λI in U(3) for nonidentity pseudoreflections with moving lines L_i.
- **Case L₁ = L₂.** R₁R₂ fixes a 2-plane, which forces λ = 1 and L₃ = L₁. The three commute.
- **Case L₁ ≠ L₂.**
  - Fix(R₁R₂) = L₁^⊥ ∩ L₂^⊥ is a line, so λ ≠ 1.
  - λR₃^{−1} has a fixed vector only if μ₃ = λ, and then Fix = L₃. Hence L₃ ⊥ L₁, L₂.
  - On W = L₃^⊥ we get R₂|_W = λ(R₁|_W)^{−1}. Matching eigenvalues {λ/μ₁, λ} with {μ₂, 1} (λ ≠ 1) gives μ₁ = μ₂ = λ and Fix(R₂) ∩ W = L₁, so L₂ ⊥ L₁.
  - The three are simultaneously diagonal. ✓

**Step 3 — contradiction.** The 16 inactive meridians are scalar on A, so the three active lifts have scalar product (in their order). They commute, so every A-part has a common eigenline L, and L ⊗ B is Γ-invariant. ✓ The argument applies equally to the two ways 3 ⊗ 14 arises: primitive factorwise-decomposable, or the isotypic case of an imprimitive kernel.

**Finite test of the lemma.** I enumerated all projective pseudoreflections in two groups and checked every pair (x, y) for which (xy)^{−1} is again one:

| Group | Projective pseudoreflections | Noncommuting ordered pairs | Scalar-product triples | Noncommuting triples |
|---|---:|---:|---:|---:|
| Primitive G₂₆-type, order 1296 | 198 | 28 512 | 2 592 | **0** |
| Monomial G(3,1,3) | 45 | — | 162 | **0** |

This supports the lemma; it does not prove it.

**Conclusion: d = 42 excluded ⇒ nonsplit under (H) ⇒ d ≥ 43 — CHECKED (two AIs).**

## 3. New (Claude, PROPOSED)

**3a. The argument covers every 3 ⊗ b with b ≤ 18.**
- Σc = 6b + 8. With t active meridians (c ≥ b) and inactive ones (c ≥ 3), t = 4 needs 4b + 45 ≤ 6b + 8, i.e. b ≥ 19. So t = 3 for b ≤ 18.
- The slack is 3b − 40 − 3(N − 19). A three-eigenvalue active element costs an extra b, which needs b ≤ 3b − 40, i.e. b ≥ 20.
- So for 14 ≤ b ≤ 18 the lemma applies verbatim, and the factorwise shapes 3 ⊗ 15, …, 3 ⊗ 18 (d = 45, 48, 51, 54) are excluded too.
- b < 14 already fails the budget. Other factor dimensions a ≥ 4 need a different lemma.

**3b. d = 43 is excluded.** 43 is prime, so every non-primitive shape is either monomial (excluded) or absent: imprimitive k = 43 has r = 1; no tensor factorization exists. In the primitive branch:
- **Self-dual socle:** Lemma S in integral form, 2⌈43/2⌉ + 51 = 95 > 94, excludes it.
- **Symplectic type:** impossible for every d (CHECKED).
- **Non-self-dual field-K socle:** the Hiss–Malle char-0 rows at d = 43 are U₃(7) (indicator +, or fields Q(i), Q(ζ₈)) and **U₇(2) (field Q(√−3), indicator ◦)**. The generic families give A₄₄ natural and the L₂(43) Steinberg character, both self-dual.
- **U₇(2):** CTblLib gives minimum moving rank **16** over noncentral classes for both conjugate 43-dimensional characters. Lemma C needs ≤ 2⌊94/19⌋ = 8, so it is excluded.

**So nonsplit under (H) ⇒ d ≥ 44 (PROPOSED).** It uses the same external inputs as before: Hiss–Malle completeness, the GT08 reduction, and CTblLib data. A second implementation should re-run the U₇(2) number from a raw export, as we did for d ≤ 42.

**3c. Outlook for d = 44.** This is the first dimension where Lemma S allows a self-dual socle, and only just: exactly two elements may have c = 22, with total 95 ≤ 96. The self-dual candidates in the Hiss–Malle rows are U₅(2), M₁₁, A₁₁ (degree 44, indicator +) and A₄₅ natural (Lemma F type). The budget then forces c_min = 3, so Lemma C needs a noncentral socle element with moving rank ≤ 6. That is a short GAP check, and the natural next step. For orientation, the field-K candidate U₄(2) at d = 45 has minimum moving rank 24 (> 10).

## 4. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| Lemma A′; Lemma B (rank-cost) | CHECKED (two AIs) |
| Original Lemma A | NOT VALID as stated (replaced by A′) |
| Nonsplit ⇒ d ≥ 42 | CHECKED (two AIs) |
| **3 ⊗ 14 factorwise tensor excluded (three-pseudoreflection lemma)** | **CHECKED (two AIs)**; GAP finite test supportive |
| **Nonsplit ⇒ d ≥ 43** | **CHECKED (two AIs)** |
| 3 ⊗ b excluded for 14 ≤ b ≤ 18 | PROPOSED (Claude) |
| d = 43 excluded ⇒ **nonsplit ⇒ d ≥ 44** | PROPOSED (Claude); U₇(2) value awaits second implementation |
| HCG-OPEN-NONSPLIT8 | OPEN; next = d = 44 self-dual socle check |
