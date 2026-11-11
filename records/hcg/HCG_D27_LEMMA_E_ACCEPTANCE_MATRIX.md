# HCG Δ27 — acceptance matrix for Lemma E (reduction to the inducing datum)

**Date:** 11 November 2026. **Prepared by:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Decision:** PI.

**Status:** owner-review package, PROPOSAL, revision 1. Nothing here is adopted. `hcg-v0.4` stays the governing edition and `hcg/HCG_STUDY_LEDGER.md` is not changed. This matrix does not define the scope of a later edition.

**What this is.** Lemma E of Δ27 (addenda 4 and 5) says that a datum whose representation is induced over K from a block of rank ≥ 2 can be replaced by the smaller datum of the block, with the same discriminant class. It is the step that carries the two theorems of ledger §6.24 into the later Δ27 results (Theorem R and the bounds from d = 15 on). Those later results are not reviewed here (§5).

**Roles — reversed with respect to the earlier matrices.** Lemma E was **proposed by Claude** (addendum 4) and **checked by ChatGPT** (addendum 5), which also gave an independent proof of the local identity. So Claude writes this matrix as the deriver, and the ChatGPT review of it is a review by the earlier checker. Neither is an independent third check.

**Sources read for this matrix** (all under `evidence/hcg/`):

| Short name | File | Read | SHA-256 |
|---|---|---|---|
| LOG | `ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`, Δ27 addenda 4–5 | in full | `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d` |
| E-SRC | `nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` (Claude), header and §3 "Lemma E" | those parts | `050c8504edfc73af13d935c8d27925d71fd0ed846395a4bb51cb94976768ec7f` |
| E-REV | `received/233fab3b-HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` (ChatGPT), §2, §5, §7 | those parts | `b7253a0cf8d55ea15ad93f0b1e05e2715912d8e289a4ac52c979d26b7203dbb1` |
| D-14 | `nonsplit8/H3_REFLECTIONFREE_SCREEN_REVIEW_CLAUDE_v0_1.md` (Claude), the D-14 entry | that entry | not compared for this matrix |
| LEDGER | `hcg/HCG_STUDY_LEDGER.md` at `hcg-v0.4`, §6.24 | in full | `51487f925e34f01e0d233d1ff909e29357d3eadbf1b839f79f73e8fe84022949` |

**Run again** (11 Nov 2026, from repository files, with only the hard-coded session path remapped): `nonsplit8/block_cycle_local_factor_claude.py` (`78845d73…`): output byte-identical to the frozen output (`6ceda59c…`); 60 cases, 0 failures. It was run during the preparation of the core matrix and not again since; the files have not changed.

**PI decisions in the log.** The decision fields of addenda 4 and 5 are blank.

---

## 0. Conventions

- **K** = ℚ(√−3), **N** the norm, a **class** an element of ℚ^×/N(K^×).
- A **datum** (Γ, σ; g₁, …, g_N) is a finite group Γ ⊂ GL_d(K) acting by an absolutely irreducible representation σ, with a product-one generating tuple; it gives a family of Γ-covers C → P¹. c_j = rank(1 − g_j).
- **(H)**, the standing hypotheses of Δ27 as stated in E-SRC: base of genus 0; finite image; σ absolutely irreducible over K with **character field exactly K** and no fixed vector; dim_K M_σ = 8 (n = 4); **(D)**: period rank 16.
- **disc M_σ** is the class of the Hermitian form on the multiplicity space M_σ that the cup product induces with respect to the invariant form h_σ. In the language of ledger §6.24 (a) it is [det(ϑS_σ)].
- "Induced over K" is profile (i) of `HCG-THM-INDUCED-PERIOD-BOUND`: σ ≅ Ind_H^Γ τ with τ defined over K. The blocks are the K-subspaces V₁, …, V_k permuted by Γ, with H the stabilizer of V₁ and τ its action on V₁.

---

## 1. Statement

Let (Γ, σ; g_j) satisfy (H), and let σ ≅ Ind_H^Γ τ over K with r = dim τ ≥ 2. Put Y = C/H, of genus γ, and let D_τ ⊂ Y be the points with nontrivial τ-monodromy h_y. Then:

- **(i)** γ = 0, so Y ≅ P¹.
- **(ii)** The **τ-datum** (τ(H), τ; (h_y)_{y ∈ D_τ}) is a genus-zero datum in dimension r that satisfies (H). In particular it has at least 19 points, and r ≥ 6.
- **(iii)** [disc M_σ] = [disc M_τ].
- **(iv)** If the reflections of Γ generate a nontrivial subgroup W_R and the blocks V_i are its irreducible blocks, then τ(H) contains a reflection group that is irreducible on V₁.

Not claimed: any transfer of condition (L); anything for an induction that is defined only over ℂ.

## 2. Proof chain

| Step | Content | Uses | State of what is used |
|---|---|---|---|
| E1 | (i): for γ ≥ 1 and r ≥ 2 the period rank is ≤ 2n = 8 < 16 | `HCG-THM-INDUCED-PERIOD-BOUND` | §6.24 (b), CHECKED (two AIs) |
| E2 | The local monodromies h_y of Y_τ = C/ker τ → Y generate τ(H) and have product one, because Y_τ is connected and Y ≅ P¹ | steps P5–P6 of the same theorem | same |
| E3 | M_σ ≅ M_τ as Hodge structures, so dimension 8 and the signature are kept | steps P4–P6 | same |
| E4 | Period rank of the τ-family is 16: Per_σ factors through the family of τ-data, so its rank is ≥ 16, and it cannot exceed the dimension of the period domain | step P6; (D) for σ | same |
| E5 | τ is absolutely irreducible (because σ is) and has no fixed vector (irreducible of rank ≥ 2) | representation theory | classical |
| E6 | The character field of τ is K: it lies in K because τ is defined over K; it is not ℚ, because the induction of a rational-valued character is rational-valued and the character field of σ is K | (H) for σ: character field exactly K | classical |
| E7 | Hence the budget of `HCG-ALG-DIM-BUDGET` applies to the τ-datum: s ≥ 19, ε_τ ≤ 2r − 11, r ≥ 6 | E2–E6 | §6.23, CHECKED (two AIs) |
| E8 | (iii), **global proof.** For φ, ψ ∈ Hom_Γ(σ, H¹(C)) the pairing (v, w) ↦ ⟨φv, ψw⟩ is Γ-invariant, so ⟨φv, ψw⟩ = S_σ(φ, ψ)·h_σ(v, w). Take h_τ = h_σ\|V₁. Restriction to V₁ is the Frobenius isomorphism, and for v, w ∈ V₁ the same identity reads S_τ(φ\|V₁, ψ\|V₁)·h_τ(v, w). So the two forms agree on H¹(C). Passing to H¹(Y_τ) multiplies the cup form by the degree \|ker τ\|, a positive integer q. On a space of K-dimension 8 this changes the determinant by q⁸ = N(q⁴) | Schur's lemma; pull-back multiplies cup products by the degree | classical |
| E9 | (iii), **local proof (independent).** For g acting on a cycle of ℓ blocks with return map P: [a(g)b(g)] = [a(P)b(P)·det(h_τ)^{ℓ−1}]. Split W = Fix(P) ⊕ im(1 − P), f = dim Fix(P): on Fix(P)^ℓ the moving space is the sum-zero space, with Gram determinant ℓ^f·det(h_F)^{ℓ−1} and det(1 − g) = ℓ^f; on im(1 − P)^ℓ the moving space is everything. The cycles over one branch point are the points of Y over it, and ℓ is the ramification index. Multiplying over all points gives the extra factor [det h_τ]^{Σ(ℓ−1)}, and Σ(ℓ − 1) = 2(k − 1) + 2γ is even by Riemann–Hurwitz for Y → P¹. With `HCG-THM-PARABOLIC-DISC-LOCALITY` on both sides, the classes agree | locality (L1); Riemann–Hurwitz | §6.24 (a), CHECKED (two AIs) |
| E10 | (iv): the stabilizer of V₁ contains the irreducible factor W₁ of W_R, which acts on V₁ as an irreducible reflection group | structure of W_R | used only by Theorem R; not needed for (i)–(iii) |

**Two proofs of (iii), at two levels.** E8 compares the geometric cup forms and needs no locality theorem. E9 compares the algebraically defined classes of §6.24 (a) and needs no geometry beyond the correspondence between block cycles and points of Y. They agree, as they must once the form S is read as the cup pairing (layer L2).

## 3. Hypotheses, each with its role

| Hypothesis | Where it is used | If dropped |
|---|---|---|
| Induction **over K** | E6 (character field of τ), E8 (h_τ = h_σ\|V₁ is a K-form), the statement "τ-datum over K" | For an induction over ℂ only, (i) and the period-rank part still hold (profile (ii) of the ledger theorem), but (ii) and (iii) are not available. A K-primitive representation can be monomial over ℂ: AGL(1,7) × μ₃ in degree 6 (E-REV §5) |
| r ≥ 2 | E1, E5 | r = 1 is the monomial case; it is excluded by the ledger theorem and has no τ-datum of this kind |
| (D) for σ | E1, E4 | without dominance nothing forces γ = 0; the cyclic C₆ separator of Δ27 is nonsplit and not dominant |
| Character field exactly K | E6 | the τ-datum might have rational character field. The matrix for the d = 6 chain excludes rational representations by a Siegel-space bound; whether that makes this hypothesis unnecessary here is not examined |
| dim M = 8 | E8 (q⁸ is a norm) | for odd K-dimension of M the factor q need not be a norm |

## 4. Verification

| Check | By | Result |
|---|---|---|
| Statement and global proof (E1–E8, E10) | Claude (E-SRC §3; LOG addendum 4: PROPOSED) | — |
| Review of (i)–(iii) with an independent write-up of E8 | ChatGPT (E-REV §§2.1–2.3) | "Lemma E CHECKED, explicitly for K-defined induction" |
| Independent proof of the local identity E9 | ChatGPT (E-REV §2.4) | proved; "not an inference from 60 tested cases" |
| Exact check of the local identity: 60 cases, r ≤ 3, ℓ ≤ 4, with det h_τ of non-norm classes [2], [5], [10]; the control without the factor det(h_τ)^{ℓ−1} fails exactly for even ℓ and non-norm det h_τ | Claude (`block_cycle_local_factor_claude.py`) | 60/60; 27 further cases by the reviewer (per E-REV) |
| Re-run | Claude, 11 Nov 2026 | output byte-identical |
| Scope correction D-14: Claude's sentence "by Lemma E one may assume σ primitive" was too strong; Lemma E gives a representative that is minimal for induction over K only | found by ChatGPT; conceded by Claude | recorded in the log |
| Third family, human | — | **none** |

Computation supports E9; it is not the proof.

## 5. What this matrix does not cover

- Lemma F, Theorem R and the corollary "no nonsplit datum for d ≤ 14".
- `HCG-LEM-NONSPLIT8-NORMAL-REFL` and the exclusions for d = 7 to 11.
- Every bound from d ≥ 15 on, with the classification imports of addenda 5–17.
- Statement (iv) beyond its one-line proof: it has no use outside Theorem R.
- Δ28, Δ29, and any claim of HHO.

## 6. Recommendation

| Field | Proposal |
|---|---|
| RID | none in the log ("Lemma E"). **Proposed: `HCG-LEM-INDUCING-DATUM`** — a new label; the reviewer and the PI may prefer another |
| Grade | `[THM]`, a result of this study, with `[assuming: (H); σ induced over K from a block of rank ≥ 2]` |
| Review state | **CHECKED (two AIs)** |
| Dependencies stated in the row | `HCG-THM-INDUCED-PERIOD-BOUND` (profile (i)); `HCG-ALG-DIM-BUDGET`; for the local proof also `HCG-THM-PARABOLIC-DISC-LOCALITY` |
| Guard wording | "Replaces a K-induced dominant datum by its inducing datum with the same discriminant class. It does not transport (L), and it does not apply to inductions defined only over ℂ." |
| Forbidden readings | "one may assume σ primitive" (only: minimal for induction over K); any use without (D); any statement about (L) |

## 7. Points for the reviewer and the PI

| # | Point | Proposal |
|---|---|---|
| Q1 | Is the statement of §1, with its four parts and the two "not claimed" items, the lemma that was checked in addendum 5 | reviewer to confirm |
| Q2 | E4 says the τ-family has period rank exactly 16. The sources say "≥ 16"; the matrix adds "and ≤ the dimension of the period domain". Is that right for the signature (4,4) target only | reviewer to confirm; if so the signature is named in the row |
| Q3 | Two proofs of (iii) at two levels (E8 geometric, E9 algebraic). Should the ledger row carry both | proposal: both, E8 as the proof and E9 as the independent route |
| Q4 | Should (iv) stay in the lemma or move to Theorem R when that is reviewed | proposal: keep it, marked "used only by Theorem R" |
| Q5 | The new RID label | reviewer and PI |
| Q6 | The character-field hypothesis (§3, last but one row): keep it as stated in (H) | proposal: keep; do not weaken (H) in this lemma |
| Q7 | Independence: two sessions; no third family; no human. The PI's dispositions of 11 Nov 2026 covered the two theorems of §6.24 and the two items of the d = 6 matrix | whether "CHECKED (two AIs), no third-family reading for now" also covers this lemma is the PI's to say |
| Q8 | The PI decision fields of addenda 4 and 5 are blank | any adoption needs an explicit PI decision |

## 8. Revision history

| Revision | Date | Change |
|---|---|---|
| 1 | 11 Nov 2026 | first version |
