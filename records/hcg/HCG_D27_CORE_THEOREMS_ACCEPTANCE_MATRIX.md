# HCG Δ27 — acceptance matrix for two core theorems

**Date:** 11 November 2026. **Prepared by:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Decision:** PI.

**Status:** owner-review package, PROPOSAL, revision 1. Nothing here is adopted. `hcg-v0.3` stays the governing edition and `hcg/HCG_STUDY_LEDGER.md` is not changed. This matrix does not define the scope of a later edition.

**What this is.** Δ27 of the pending-delta log has a main entry and 17 addenda. Two of its results carry most of what follows, in HCG and in HHO:

1. `HCG-THM-PARABOLIC-DISC-LOCALITY` (Δ27 addendum 2), and
2. `HCG-THM-INDUCED-PERIOD-BOUND` (Δ27 addendum 4).

For each, the matrix gives the statement, the hypotheses, the proof chain, who checked what, the evidence held in this repository, what is imported, what is not covered, and a recommendation. The other Δ27 items are listed in §5 and are not reviewed here.

**Why the review is ChatGPT's, and what is unusual here.** Both theorems were derived by ChatGPT and proof-reviewed by Claude. The Claude session therefore writes this matrix as the earlier reviewer, and the ChatGPT session reviews a matrix about its own derivations. Neither is an independent third check. The matrix says so in §4.

**Sources read for this matrix** (all under `evidence/hcg/`; read in full unless stated):

| Short name | File | SHA-256 |
|---|---|---|
| LOG | `ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`, lines 70–101 (Δ27 and addenda 1–17) | `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d` |
| LOC-v0.1 | `received/68e831c3-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md` (ChatGPT); hash compared, text not re-read | `0ec385584bbaba4b6408572b3f4423dc38c3884e60fbf304f5a49c61392114cb` |
| LOC-v0.2 | `received/b69978bf-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md` (ChatGPT) | `d62942e3e760928d089db38471c5d660c21a24fde186d0d428a222df42785814` |
| LOC-REV | `nonsplit8/H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md` (Claude) and its `_ADDENDUM_1.md` | `41bc9997328cbc74a592ba9a899fd6cc30eb6e71656cc284c591ff05ac1878ee`, `70b61fd947aa862c9067c12bffa2f4bb8006d1938fd4fc5c24b8ff0027f2734a` |
| IND | `received/20505e68-HCG_INDUCED_PERIOD_DIMENSION_BOUND_PROPOSED_v0_1.md` (ChatGPT) | `03199b80ad92692db91cc3ce7d3014c425d263191bc44ac844fd7706ae2b306e` |
| IND-REV | `nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` (Claude), §§1–3 Lemma E | `050c8504edfc73af13d935c8d27925d71fd0ed846395a4bb51cb94976768ec7f` |
| IND-X1 | `received/233fab3b-HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` (ChatGPT), §2.1 only | `b7253a0cf8d55ea15ad93f0b1e05e2715912d8e289a4ac52c979d26b7203dbb1` |
| IND-X2 | `received/50a6524e-HCG_REFLECTIONFREE_CLAUDE_CROSS_REVIEW_v0_1.md` (ChatGPT), §4 only | `8860f55a209feacef64a68638e74b514e3fad703689e6667c40c73072725a7db` |

**Run again for this matrix** (11 Nov 2026, from repository files, with only the two hard-coded session paths remapped; see §4, E1):
- `nonsplit8/disc_locality_proof_check_claude.py`: output byte-identical to `…_out.txt`.
- `nonsplit8/block_cycle_local_factor_claude.py`: output byte-identical to `…_out.txt` (60 cases, 0 failures).

Nothing else was re-run. The ChatGPT packages were located and not opened beyond their file lists.

**PI decisions in the log.** The PI set the research priority for Δ27 on 28 Oct 2026 (relayed). The decision fields of addenda 2 and 4 are **blank**. Neither theorem has a PI approval of any kind.

---

## 0. Conventions

- **Review states** as in the ledger: PROPOSED, CHECKED (two AIs), THIRD-FAMILY CHECKED, ACCEPTED. A grade tag (`[THM]`, `[ALG]`) is separate from a review state.
- **K** is an imaginary quadratic field; in every HCG application K = ℚ(√−3). **N** is the norm K^× → ℚ^×. A **class** is an element of ℚ^×/N(K^×).
- "Split" means the class [1]. Whether a class is the discriminant of a polarized abelian variety is a separate, imported step (§1.4).
- Paths without a prefix are under `evidence/hcg/`.

---

## 1. `HCG-THM-PARABOLIC-DISC-LOCALITY` (Δ27 addendum 2, 29 Oct 2026)

### 1.1 Statement

Let (V, h₀) be a d-dimensional positive definite K-Hermitian space, h₀(x, y) = xᵀH₀ȳ. Let g₁, …, g_N be h₀-unitary with g₁⋯g_N = 1 and ∩ ker(g_i − 1) = 0. Put E_i = im(1 − g_i), c_i = dim E_i, R = Σc_i, and assume R − 2d = 2n is even. For any K-basis of E_i put

- a_i = det(h₀|E_i) ∈ ℚ_{>0}, and
- b_i = det((1 − g_i)|E_i) ∈ K^×.

Let S be the skew-Hermitian form on H = ker C / D(V) defined in §1.2, and let ϑ ∈ K^× with ϑ̄ = −ϑ. Then Πb_i ∈ ℚ^× and

  [det(ϑS)] = [(−1)ⁿ Π a_i/b_i] = [(−1)ⁿ Π a_i b_i] in ℚ^×/N(K^×).

The class depends only on the multiset of local classes of the g_i under h₀-isometries over K. It does not depend on the Hurwitz component, on a braid connection or on any degeneration.

### 1.2 Proof chain (LOC-v0.2 §3; equation numbers of that note)

| Step | Content | Uses |
|---|---|---|
| 0 | E_i^⊥ = ker(1 − g_i), V = E_i ⊕ ker(1 − g_i); (1 − g_i)\|E_i is invertible | unitarity; h₀ positive definite |
| 3.1 | C: ⊕E_i → V, C(x) = ΣQ_i x_i with Q_i = g₁⋯g_{i−1}; D: V → ⊕E_i, D(v) = ((g_i − 1)v)_i. CD = 0, D injective, C surjective, dim H = 2n | product one; no common fixed vector |
| 3.2 | A sesquilinear form B on all of ⊕E_i, block upper triangular, with **(1)** det B = Πa_i/b_i and **(2)** B(x, y) + conj B(y, x) = h₀(Cx, Cy) | unitarity |
| 3.3 | **(3)** B(Dv, y) = −h₀(v, Cy), B(x, Dv) = h₀(Cx, v); hence rad(B\|ker C) = D(V) exactly, and S (induced by B on H) is nondegenerate | (1), (2), C onto |
| 3.4 | In a basis adapted to D(V), H, and a section of C: **(4)** det B_ad = det S · (det H₀)², with no extra sign; **(5)** det S / Π(a_i/b_i) = N(det P / det H₀) | block elimination; det H₀ ∈ ℚ |
| 3.5 | conj(b_i) = (−1)^{c_i} det(g_i)^{−1} b_i, so Πb_i ∈ ℚ^× (R even, Πg_i = 1). ϑ^{2n} = (−1)ⁿ N(ϑ)ⁿ gives the sign. [q^{−1}] = [q] for q ∈ ℚ^× | unitarity; R even |

The proof is elementary linear algebra over K. It uses no computation and no external theorem.

### 1.3 Hypotheses, each with its role

| Hypothesis | Where it is used | If dropped |
|---|---|---|
| K imaginary quadratic | det of a Hermitian Gram matrix lies in K ∩ ℝ = ℚ; class group ℚ^×/N(K^×) | not examined (CM fields are outside the statement) |
| h₀ positive definite | step 0 (the orthogonal splitting) | not examined; indefinite forms are outside the statement |
| product one, base of genus 0 | CD = 0; the cocycle model | higher-genus bases are outside the statement |
| no common fixed vector | D injective; dim H = R − 2d | — |
| R − 2d even | Πb_i rational; ϑ^{2n} | for odd dimension the statement is not made |

Not assumed: finiteness of the group, irreducibility, a character field, pairedness of the tuple, a component, or any Hodge-theoretic input.

### 1.4 What is imported, and for what

| Layer | Content | Source and its state |
|---|---|---|
| L1 | The identity of §1.1 for the form S **defined by B** | none; proved in the note |
| L2 | S is the cup pairing on genus-zero parabolic cohomology | Dettweiler–Wewers 2006, §1.2 and Thm 2.6 (published; arXiv v1 numbers it Thm 2.5). In the ledger: `HCG-ALG-CUPVAL` (W5: THIRD-FAMILY CHECKED) and `HCG-THM-SEVERN-V2-L72` (general formula, unrefereed, two AIs). Claude's check found the engine's `Local.S` equal to B restricted to cocycles, entry by entry, in every H₀ = I case |
| L3 | The class is the discriminant of the polarized abelian factor; nonsplit ⇔ nontrivial class | Severn v2 Prop 7.1 (unrefereed; two-AI crosswalk) and Weil's criterion. **Needed only by applications**, not by the theorem |

**Proposal.** Record L1 as the theorem. State L2 as an explicit import in the row, so that the theorem is not read as a statement about polarizations.

### 1.5 Attribution and novelty

- The formula was **announced without proof** by Severn: hexagon:2610.00387**v1** Remark 2.8 ("Theorem W"), citing hexagon:2610.00386v1 Remark 5.3 and unpublished notes. Severn's Δ(g) is the determinant of the form (x, y) ↦ h((1 − g)^{−1}x, y) on im(1 − g), which equals a_i/b_i. Severn's v2 has no such remark (correction D-11).
- The HCG proof does not use that remark, and Severn's proof has not been seen.
- **No novelty is claimed.** No literature search was made for earlier proofs. The Severn texts are third-party and are not in this repository; the line references in LOC-REV addendum 1 point to session copies.

### 1.6 Verification

| Check | By | Result |
|---|---|---|
| Derivation and proof text | ChatGPT (LOC-v0.1, LOC-v0.2) | — |
| Line-by-line proof review of §§2–5 of LOC-v0.1; three audited points: the radical (3.3), the sign in (4), the rank-2 step | Claude (LOC-REV §§1–2) | pass; six clarification requests M1–M6, none affecting the result |
| LOC-v0.2 against LOC-v0.1: M1–M6 applied, equations (1)–(5) unchanged | Claude (LOG, addendum 3) | pass |
| Exact check of (1), (2) as a matrix identity, (3) on every basis pair, the radical, the block shape, (4), (5), rationality of Πb_i, and the class, on 16 data | Claude, own engine (`disc_locality_proof_check_claude.py`) | all pass. Includes a class-[2] control (C₆), an odd-n control (class [−1]), and W5 with H₀ ≠ I (det H₀ = 68364) |
| Independent implementation (standard library, triangular cochain form); 320 sampled tuples and 19 controls | ChatGPT (package `received/2e443e69-…REPRO_v0_1.zip`) | pass; replayed by Claude at the time (40/40 manifest, four JSONs byte-identical) |
| Re-run for this matrix | Claude, 11 Nov 2026 | output byte-identical |
| Third model family | — | **none** |
| Human referee | — | **none** |

Computation supports the proof; it is not the proof.

### 1.7 Corrections on record

- **D-10** (Claude): the locality sample counts were 160 + 160 = 320, not 120 + 480. Dated addendum; the original is preserved.
- **D-11** (Claude): the Severn remark is in v1, not v2.
- **D-12** (wording): the transport matrix T is in GL₆(K); ε ≤ 3 holds only at d = 7; the ZIP manifest scope.
- `HCG-CONJ-DISC-LOCAL` (Claude, Δ27 addendum 1, PROPOSED from samples) is superseded by this theorem.

### 1.8 Recommendation

| Field | Proposal |
|---|---|
| RID | `HCG-THM-PARABOLIC-DISC-LOCALITY` |
| Grade | `[THM]`, a result of this study (layer L1) |
| Review state | **CHECKED (two AIs)** |
| Imports stated in the row | L2 (cup-pairing identification) |
| Reference text | LOC-v0.2 (`d62942e3…`), with LOC-REV as the review record |
| Guard wording | "A determinant-class identity for genus-zero parabolic cup forms over an imaginary quadratic field. Announced without proof by Severn; no novelty claimed; no third-family or human check." |
| Forbidden readings | "proves a statement about abelian varieties"; "verifies Severn's Theorem W"; any use for higher genus, indefinite h₀ or other fields |

---

## 2. `HCG-THM-INDUCED-PERIOD-BOUND` (Δ27 addendum 4, 29 Oct 2026)

### 2.1 Statement

Let C → P¹ vary in a family of connected Galois covers with a fixed finite group Γ and fixed topological type. Let σ be an absolutely irreducible representation of Γ with σ ≅ Ind_H^Γ τ, [Γ : H] = k, dim τ = r. Let M_σ be the σ-multiplicity part of H¹(C), with the Hodge structure induced from H¹(C), of dimension 2n. Put Y = C/H, of genus γ, and let D_τ ⊂ Y be the set of points where the τ-local system has nontrivial local monodromy, s = |D_τ|. Then, for r ≥ 2:

- **(P1)** rank Per_σ ≤ 3γ − 3 + s ≤ 2n + 2r − 3 + (3 − 2r)γ;
- **(P2)** rank Per_σ ≤ 2n + 2r − 3;
- **(P3)** for n ≥ 3, a period rank of n² needs γ = 0 (for γ ≥ 1 the bound is at most 2n) and r ≥ ⌈(n² − 2n + 3)/2⌉.

For r = 1 and a nontrivial character: s = 2n + 2 − 2γ and rank Per_σ ≤ 2n − 1 + γ ≤ 3n.

For n = 4 the period domain has dimension 16. So an induced datum can be dominant only with γ = 0 and r ≥ 6, and a monomial datum (r = 1) never.

### 2.2 Proof chain (IND §§2–4, with the factorization as written in IND-REV §2)

| Step | Content | Uses |
|---|---|---|
| P4 | Hom_Γ(Ind τ, H¹(C)) ≅ Hom_H(τ, H¹(C)), compatible with the Hodge decomposition and Gauss–Manin transport | Frobenius reciprocity; the maps come from the fixed group action |
| P5 | The right side is H¹(Y, j_*L_τ), parabolic cohomology of the τ-local system on Y | exactness of isotypic parts in characteristic 0; stalks at branch points are inertia invariants |
| P6 | **The load-bearing step.** With N_τ = ker τ and Y_τ = C/N_τ: Hom_H(τ, H¹(C)) = Hom_{τ(H)}(τ, H¹(Y_τ)). The cover Y_τ → Y is Galois with group τ(H) and is branched exactly over D_τ. By Riemann existence it is determined by (Y, D_τ) and a discrete datum π₁(Y ∖ D_τ) → τ(H). So the Hodge structure on M_σ is a function of a point of a finite cover of M_{γ,s}, and rank Per_σ ≤ dim M_{γ,s} = 3γ − 3 + s | Riemann existence theorem; functoriality of Hodge structures under finite group actions and finite pull-back |
| P7 | 2n = 2r(γ − 1) + Σ_{y ∈ D_τ} a_y with a_y = rank(1 − h_y) ≥ 1 | Euler characteristic; H⁰ and H² vanish because the monodromy group τ(H) acts irreducibly and nontrivially |
| P8 | s ≤ Σa_y = 2n + 2r(1 − γ); substituting in P6 gives P1; γ ≥ 0 and r ≥ 2 give P2 | — |
| P9 | A second count: rank(1 − g_j) = r·ind(π_j) + Σ_a rank(1 − h_{j,a}); with Riemann–Hurwitz it recovers P7 from the count on P¹ | consistency check, not needed for the proof |

**Stability of (Y, D_τ)** (a point this matrix adds; for the reviewer to confirm). Since a_y ≤ r, P7 gives s ≥ (2n + 2r(1 − γ))/r. For γ = 0 this is s ≥ 2 + 2n/r > 2, and for γ = 1 it is s ≥ 2n/r > 0. So the pointed curve is stable whenever n ≥ 1, and dim M_{γ,s} = 3γ − 3 + s applies in every case that occurs.

### 2.3 Hypotheses, each with its role

| Hypothesis | Where it is used | Remark |
|---|---|---|
| finite group Γ, fixed in the family | P6: the monodromy datum is discrete, hence locally constant | continuous families of representations are outside the statement |
| the Hodge structure is the one from H¹(C) | P4–P6 | an arbitrary Hodge filtration on the same local system is not covered |
| σ ≅ Ind τ | P4 | the original note asks for K-defined blocks; see §2.5 |
| τ irreducible and nontrivial on τ(H) | P7 | automatic when σ is absolutely irreducible of dimension > 1 |
| base of genus 0 (covers of P¹) | only for the comparison with the count on P¹ (P9) and for the applications | P4–P8 work on Y and do not use it |

Not assumed: (L), any condition on the discriminant, the field K (see §2.5), Severn's results.

### 2.4 What is imported

Only classical facts: Frobenius reciprocity, the Riemann existence theorem, functoriality of Hodge structures for finite group actions and finite maps, the Euler-characteristic formula for local systems on a curve, and dim M_{γ,s}. No unrefereed source is used. No computation is used in the proof.

The comparison with Severn v1 §8 (monomial exclusion) is source-limited: IND says the PDF could not be reopened in that session. With the r = 1 case, HCG no longer needs that section as a dependency; the two-AI note IND-X1 §2.1 says the same.

### 2.5 The field-free extension (a separate step)

- IND and addendum 4 state the theorem for a K-defined inducing block.
- Δ27 addendum 5: Claude **proposed** that the bound holds for any σ that is imprimitive over ℂ, with no descent to K.
- Δ27 addendum 6: ChatGPT checked that (IND-X2 §4: "CHECKED; no automatic K-discriminant descent").

The proof steps P4–P8 use no arithmetic of K, so the extension is the same argument over ℂ. What does **not** extend is anything about the discriminant class: Lemma E(iii) needs K-defined blocks.

**Question for the reviewer:** record the field-free form under the same RID, with the K-form as its first statement, or as a separate row.

### 2.6 Verification

| Check | By | Result |
|---|---|---|
| Derivation | ChatGPT (IND), with P6 flagged by the author as the step to review | — |
| Proof review of P4–P8; P6 rewritten through Y_τ; degenerate cases | Claude (IND-REV §2) | pass |
| Second argument-level review, with the same factorization through Y_τ | ChatGPT (IND-X1 §2.1: "CHECKED, two argument-level reviews") | pass |
| Field-free form | Claude proposed; ChatGPT checked (IND-X2 §4) | pass |
| Exact arithmetic for P9 on sample matrices and for the numerical bounds | ChatGPT (`independent_checks.py` in `received/979c2af8-…zip`); replayed by Claude at the time | pass; it does not test P4–P6 |
| Local identity behind Lemma E(iii), 60 cases with non-norm det h_τ | Claude (`block_cycle_local_factor_claude.py`) | 60/60; re-run for this matrix, byte-identical. It concerns Lemma E, not the bound |
| Third model family | — | **none** |
| Human referee | — | **none** |

There is no computational certificate of the theorem itself, and none is possible for P4–P6: they are geometric arguments.

### 2.7 Recommendation

| Field | Proposal |
|---|---|
| RID | `HCG-THM-INDUCED-PERIOD-BOUND` |
| Grade | `[THM]`, a result of this study |
| Review state | **CHECKED (two AIs)**; argument-level reviews only |
| Reference texts | IND (`03199b80…`) for the statement and P7–P9; IND-REV §2 for the form of P6 that both sessions checked |
| Guard wording | "An upper bound for the period rank of an induced finite-monodromy variation. It is an obstruction to (D). It constructs nothing and says nothing about (L) or the discriminant." |
| Forbidden readings | "no dominant family exists"; use for variations that do not come from the cohomology of the covers; use of the field-free form for a discriminant statement |

---

## 3. How the two theorems are used (not reviewed here)

| Use | Depends on |
|---|---|
| `HCG-COR-D6-NONSPLIT-NOGO` (d = 6) | locality; `HCG-ALG-G34-RANK2-LOCAL`; the reduction to G₃₄ of Δ27 addendum 1 (with the monomial exclusion, now through the induced bound, r = 1); L3 |
| d = 10 exclusion; d = 7, 8, 9, 11 | induced bound; `HCG-LEM-NONSPLIT8-NORMAL-REFL` |
| Lemma E, Lemma F, Theorem R, and the bounds d ≥ 15 … d ≥ 53 | both theorems, and further lemmas and classification imports of addenda 4–17 |
| HHO (`hho-v0.1`, claim register Parts A–B) | both, as "placed at `hcg-v0.2`, pending in HCG"; many rows are `[THM-cond: locality]` |

An HCG decision on these two rows changes nothing in HHO by itself. HHO re-pins and re-states by its own decision.

---

## 4. Points for the reviewer and the PI

| # | Point | Proposal |
|---|---|---|
| Q1 | Locality: one row for the algebraic identity (L1) with the cup identification (L2) as a stated import | as in §1.4 |
| Q2 | Induced bound: is the stability remark of §2.2 correct and worth recording | reviewer to confirm |
| Q3 | Induced bound: the field-free form under the same RID or a separate one | same RID, two statements, with the "no discriminant" guard |
| Q4 | Reference text for locality: the line-by-line review was of v0.1; v0.2 was checked as "clarifications only" | cite v0.2 as the text, v0.1 as the reviewed baseline |
| Q5 | **Independence.** Each theorem has one deriving session and one reviewing session, and this matrix is written by the reviewer and checked by the deriver. No third family and no human has read either proof | state it in the rows. Whether to ask the third-family auditor for a blind reading of LOC-v0.2 §§2–3 and of P4–P6 is a PI decision; this matrix does not assume it |
| Q6 | **Literature.** No search was made for an earlier proof of the locality formula (Wall-form determinants) or of the period bound | record "no novelty claimed; literature not searched"; a search would go through LIT |
| Q7 | PI decision fields of addenda 2 and 4 are blank | any adoption needs an explicit PI decision in a release record |
| E1 | The check scripts in `nonsplit8/` have two hard-coded session paths (`/home/claude/g34/h4sel/p2p3`, `/home/claude/g34/roots_alt_5.json`). From the repository they run after mapping these to `h4sel/p2p3/` and `h4sel/severnlink/W5_BASELINE_ROOTS.json` (`NAME_ALIASES.tsv`). The frozen files are not edited | if the rows are adopted, add a small replay wrapper under `evidence/hcg/verification/` |

---

## 5. What this matrix does not cover

- The main Δ27 entry (`HCG-OPEN-NONSPLIT8`, the C₆ separator and C₃ control, the search gates).
- `HCG-ALG-G34-RANK2-LOCAL` and `HCG-COR-D6-NONSPLIT-NOGO` (addendum 2, items ii–iii).
- `HCG-LEM-NONSPLIT8-NORMAL-REFL`, Lemmas E, F, Theorem R, and every bound from d ≥ 15 to d ≥ 53 (addenda 3–17), with their classification imports.
- Corrections D-13 to D-24.
- Δ28 (historical origin of HHO) and Δ29 (positive lane).
- Any claim of HHO.

## 6. Revision history

| Revision | Date | Change |
|---|---|---|
| 1 | 11 Nov 2026 | first version |
