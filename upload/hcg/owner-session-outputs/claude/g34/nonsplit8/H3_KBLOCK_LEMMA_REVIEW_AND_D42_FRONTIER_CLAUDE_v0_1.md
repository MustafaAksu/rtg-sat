# HCG — Claude review of the k-block budget lemma (A) and the two-block scalar lemma (B); a Galois-stability repair and the d = 42 frontier v0.1

**Date:** 30 October 2026 · **Status:** Claude review (second AI) + Claude PROPOSED repair. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.
**Inputs (received unchanged):** `HCG_D26_D32_CHATGPT_CROSS_REVIEW_AND_BLOCK_EXTENSION_v0_1.md` acaaab40…; ZIP `HCG_D26_D32_CHATGPT_REVIEW_PACKAGE_v0_1.zip` 52ac8e3d… (manifest 4/4; `check_extension.py` read and rerun, output byte-identical); covering message 643b1d4b….
**Own check:** `imprimitive_closure_claude.py` / `_out.txt` (stdlib).

## 1. Agreed

- The d = 26 obstruction and the r = 13–16 two-block extension are now checked by both AIs. With d = 27, 29, 31 already excluded, **nonsplit under (H) ⇒ d ≥ 33** — proposed for CHECKED.
- The inequality E_k = 2r + 2k² − 21k + 8 ≥ 0 is correctly derived from the stated premises: J = 2(k − 1) at γ = 0; c ≥ r·ind for block-moving elements; c ≥ k for block-preserving elements when the ranks on the blocks are all equal; N ≥ 19. Every k ≥ 3 shape with d ≤ 42 has E_k < 0; I rechecked them all, not only the listed ones.

## 2. Lemma A as written has a gap: Galois must act on *this* system

The step "Galois acts transitively on the k blocks" presupposes that Gal(K̄/K) maps each block of the given C-system 𝓑 to a block of 𝓑. In general it only maps 𝓑 to some **other** system α(𝓑). For k = 2 this is automatic. There Λ = H has index 2, U₁ and U₂ are its two non-isomorphic irreducible constituents, hence its isotypic components, and Galois permutes isotypic components of a K-rational subgroup. For k ≥ 3 the kernel Λ of the block action can be strictly smaller than the block stabilizer. It may then act reducibly on a block, or isomorphically on two blocks, and the argument does not go through as written.

**Repair (Lemma A′, Claude, PROPOSED).** Let 𝓑 be any C-system, let Λ be its kernel (normal, K-rational), and consider V|_Λ.
1. **V|_Λ is not isotypic.** Its isotypic components form a Γ-system 𝓧 (Clifford). Because Λ ⊂ GL(V_K), 𝓧 is **Galois-stable**.
   - Galois commutes with the Γ-action, so the sums over Galois orbits form a K-defined Γ-system. K-imprimitive nonsplit data need d ≥ 50, so for d < 50 Galois is **transitive** on 𝓧.
   - ChatGPT's argument then applies verbatim to 𝓧, with its own shape (k′, r′): for k′ ≥ 3, E_{k′} ≥ 0 is needed (false for d ≤ 42); k′ = 2 is the two-block case.
2. **V|_Λ ≅ W^{⊕e} is isotypic.** e = 1 is impossible, since Λ preserves every block.
   - **dim W = 1, so Λ is scalar.** At most one branch element can be a scalar (two would cost 2d). So at least 18 elements move blocks, giving J = 2(k − 1) ≥ 18, k ≥ 10 and r ≤ 4. This contradicts r ≥ 6 from the field-free period bound.
   - **dim W ≥ 2, e ≥ 2.** Clifford gives a projective factorwise decomposition V ≅ W ⊗ U. The CHECKED factorwise tensor budget (2ab + 8 ≥ 3b + 16·max(a, 2)) allows only (3, 14) at d = 42 and nothing for d ≤ 41.

## 3. Lemma B — CHECKED, with a simpler cost step

In the W_R(τ₁) = S_{r+1} case τ₁ = std ⊗ ψ. If ψ is nontrivial, then at least **two** local points on Y = P¹ carry ψ ≠ 1, because the local ψ-values multiply to 1 and the meridians generate. Each such point has local rank ≥ T_r = r − ⌊(r+1)/2⌋.

- If such a point lies over a block-preserving g_j, its ρ_j ≥ T_r. The Galois rank equality gives the same ρ_j at the other lift, so g_j alone costs 2(ρ_j − 1) ≥ 2(T_r − 1) of the excess E.
- If both points are swap points, they cost ≥ 2T_r.

So a nontrivial ψ costs ≥ 2(T_r − 1) > E = 2r − 26 for 13 ≤ r ≤ 22. ψ is trivial, the character is rational, and we get a contradiction ✓.

This route does not need ChatGPT's claim that "if one lift has a nontrivial scalar, both do". That claim is plausible but needs an extra argument about scalar parts under conjugation by s; the rank equality alone suffices.

For r = 17–22 the other branches of the two-block lemma also close:
- **Reflection present:** at least 17 block-preserving elements against E/2 ≤ r − 13, so some ρ_j = 1.
- **Finer W_R(τ₁) systems:** the components of W_R(τ₁) in U₁, with their s-translates in U₂, form a Γ-system 𝓑′. It is Galois-stable, because Galois maps reflections of τ₁(Λ) to reflections of τ₂(Λ) and preserves or swaps U₁, U₂. So Lemma A applies to 𝓑′ directly, and E_{2k′}(r/k′) < 0 for every occurring shape: (4, 7), (4, 8), (4, 9), (6, 6), (4, 10), (6, 7), and (4, 11) at r = 22.
- **G(m, p, r) and diagonal W_R:** both make σ monomial, so they are excluded.
- **Exceptional groups:** none in rank ≥ 9.

## 4. Consequence (PROPOSED)

With A′ and B, **every C-imprimitive datum with d ≤ 41 is excluded**. Combined with the CHECKED exclusions — primitive tensor-indecomposable non-tensor-induced for 25 ≤ d ≤ 42, factorwise tensor needs d ≥ 42, tensor-induced needs d ≥ 256, K-imprimitive needs d ≥ 50 — this gives:

- **A nonsplit datum under (H) needs d ≥ 42.**
- At d = 42 the imprimitive branch closes as well (r = 21: scalar case by B; finer (6, 7) by A′; monomial excluded). The **only** surviving shape is the factorwise tensor decomposition **V ≅ C³ ⊗ C¹⁴**, either directly or as the isotypic case of an imprimitive kernel.

**Next target:** d = 42 with V = A ⊗ B, dim A = 3, dim B = 14. The budget there is tight: three branch entries with noncyclic PGL(A)-image cost ≥ 14 each, and the rest ≥ 3. Then d ≥ 43. Nothing here constructs a family.

## 5. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| d = 26 and r = 13–16 two-block extension; **nonsplit ⇒ d ≥ 33** | **CHECKED (two AIs)** |
| E_k inequality (given a Galois-transitive system) | CHECKED as arithmetic and derivation |
| Lemma A as stated (Galois transitivity on the given 𝓑) | gap: needs Galois-stability of 𝓑 |
| Lemma A′ (Clifford system of the kernel; isotypic case ⇒ scalar or factorwise tensor) | PROPOSED (Claude) |
| Lemma B (two-block scalar trivial for 13 ≤ r ≤ 22), via the rank-cost argument | **CHECKED** (Claude's cost step replaces ChatGPT's "both lifts" claim) |
| Imprimitive branch closed for d ≤ 42 ⇒ **nonsplit ⇒ d ≥ 42**; at d = 42 only factorwise 3 ⊗ 14 remains | PROPOSED (Claude), conditional on A′ |
| HCG-OPEN-NONSPLIT8 | OPEN |
