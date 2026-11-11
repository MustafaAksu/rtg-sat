# HHO P1 entry review — known results, parity scope, and next study

**Date:** 2026-11-11  
**Status:** `[SESSION]` independent scientific advisory. **Verdict:** ACCEPT WITH SCOPED CORRECTIONS; do not promote the source note as a checked theorem or claim adoption.  
**Reviewed source:** `HHO_P1_KNOWN_RESULTS_AND_OPEN_GAP.md`, 144 lines, SHA-256 `f88d7bef0319798719c02c5619b15cb7c8662ac2a1ffdc29b3543c70a61cc747` (complete).  
**Owner pins verified in GitHub:** HHO `hho-v0.2` (annotated tag, adopted register edition), HCG `hcg-v0.2` (annotated tag; the Δ27/HHO source proofs are *placed, pending in HCG*, not adopted).  
**Secondary reading:** targeted parts of `evidence/hcg/received/233fab3b-HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` §§2–5; `evidence/hcg/nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` §§2–3; `evidence/hcg/nonsplit8/H3_D46_REVIEW_KIMP_AND_D50_D52_CLAUDE_v0_1.md` §§1–2; `evidence/hcg/nonsplit8/H3_FRAMEWORK2_REVIEW_AND_REAL_DATA_CLAUDE_v0_1.md` §2; `evidence/hcg/received/b69978bf-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md` §§2–3; and the HHO v0.2 register, gates, and support summaries. **Not** an independent full rereading of all 25 Appendix A sources, the 13 omitted ChatGPT notes, scientific code, GAP outputs, or third-party proofs. Bibliographic metadata/abstract for Dettweiler–Wewers (2006), *Variation of parabolic cohomology and Poincaré duality*, was checked; the article proof was not read.

## Decision

The source note correctly distinguishes dimension-dependent exclusion from a universal local parity mechanism; keeps (L), (D), and cup/polarization objects separate; and identifies two plausible development directions. Its navigation value is substantial. Three corrections are required before it is used as a stable P1 scientific map.

### F1 — R1 does not establish the stronger classification (source §2, §4.3 Gap A)

**[SESSION]** The verified HCG statement is

\[
 (H)\ \land\ [\det h_{\rm par}]\ne[1]\quad\Longrightarrow\quad d\ge53.
\]

Its contrapositive gives splitness for (H)-data at `d <= 52`, but not the asserted exhaustive classification that every such datum is G34 or iterated K-induction from G34. The reflection-containing branch is reduced in the source to G34 or K-defined descent, while the reflection-free and K-imprimitive branches require separate exhaustive exclusion/termination arguments. A lower bound for **nonsplit** data cannot be cited as a lower bound for **all** (H)-data: the HCG source `H3_D46_REVIEW_KIMP_AND_D50_D52_CLAUDE_v0_1.md` §2 uses the potentially overbroad shorthand “all (H)-data”; its mathematical induction needs nonsplitness to transmit via Lemma E. This is not an exhibited counterexample to the stronger classification; it is an unproved strengthening.

**Correction:** replace “for d <= 52, every (H)-datum is G34 or induced from G34” by “the source-conditional R1 chain excludes **nonsplit** (H)-data at d <= 52. In reflection-containing cases the proof reduces to G34 and K-defined descent; whether an exhaustive classification of all split (H)-data follows has not been established in this review.” Also replace “R1 says nothing about epsilon_p” with “R1 **implies** all epsilon_p are even for (H)-data at d <= 52, but supplies no new dimension-free local parity identity.”

### F2 — `p ∤ |Gamma|` does not, by itself, give a self-dual lattice for the **fixed** h0 (source §4.3 Gap B)

**[SESSION: exact local counterexample, outside (H)]** Let `K=Q(omega)`, `p=5` inert, `Gamma=C3`, `chi(omega)=omega`, `R=O_K ⊗ Z_5`, and take the positive invariant rank-one Hermitian form `h0(x,y)=5 x bar(y)`. Since `5 ∤ |Gamma|=3`, the unqualified claim would predict an invariant self-dual lattice. Every rank-one R-lattice is `L=tR` and its Gram determinant has valuation

\[
  v_5(5N_{K_5/\mathbb Q_5}(t))=1+2v_5(t),
\]

which is always odd. Thus **no self-dual lattice exists for this fixed h0**, even without requiring Gamma-stability. This does **not** contradict the rank-eight (H) parity statement: it refutes only the unqualified local lattice assertion. Replacing `h0` by `5^{-1}h0` produces a self-dual lattice. For a parabolic rank-eight datum, a rational rescaling `h0 -> q h0` changes the product of local Gram determinants by

\[
 q^{\sum_j c_j}=q^{2d+8}=N_{K/\mathbb Q}(q^{d+4}),
\]

so the **global norm class is invariant**, although each local `lambda_j` may shift by `c_j v_p(q)`. Accordingly a usable corrected criterion is: *after an explicitly justified p-local rational normalization of the coefficient Hermitian form, a Gamma-stable self-dual lattice may be chosen at p outside |Gamma| under the required integral representation hypotheses; its existence and the normalization must be proved or cited.* The existing HHO defect-zero Morita lemma is the appropriate proof route; a bare “standard lattice fact” is not enough. Do not promote this corrected statement without checking the matrix-order/involution hypothesis, including p=2.

### F3 — cyclotomic splitting of lambda is a parity statement, not automatically an equality of lengths (source §3)

**[SESSION]** For `p` inert, `kappa_j = v_p(det(1-g_j)|E_j)` is spectral. Because `p != 3`, the full cyclotomic factor `Phi_{p^a}` is irreducible over `K`; its value at 1 equals `p`, so each such factor contributes one to `kappa_j`. Under an orthogonal K-rational cyclotomic decomposition `E_j=⊕E_{j,n}`, the determinant class decomposes multiplicatively. But a chosen integral lattice `Lambda_{E_j}` need not be the direct sum of its intersections with these K-subspaces. For finite gluing index length `t`,

\[
 \lambda_j = \sum_n \lambda_{j,n}-2t,
\]

in an integral normalization, and hence only `lambda_j ≡ Σ lambda_{j,n} (mod 2)` is automatic. The cancellation of `3|n` factors in Lemma R-prime additionally uses the **K-isometric inverse-conjugacy hypothesis**. The note should not attribute that cancellation, or exact lattice-length decomposition, to arbitrary g.

## Further scope refinements

- The claim that “(D) never touches arithmetic” should read **“no direct period-rank/local-parity identity was found in the inspected proofs.”** It is a scoped literature observation, not a theorem of independence. Theorem R and R1 do use dominance to imply splitness in their stated domains.
- “No test object other than G34” should be explicitly restricted to the known HHO/HCG campaign and to its source availability.
- The local index `|G|/chi(1)` in `HHO-THM-SUPPORT` uses the actual group acting on C. An intrinsic `|Gamma|/chi(1)` statement requires passing to `C/ker(sigma)` and proving the rank-eight norm-class invariance under that quotient (the mechanism used in `HHO-NEG-NPL-JAC-C3F20`). Do not switch between `G` and `Gamma` silently.

## Research priority: Direction 1 first

**[SESSION recommendation]** Investigate the general **parabolic-cup vs. Jacobian-multiplicity Hermitian norm-class comparison**, not the full Severn polarised factor. There are two distinct bridges:

- **B1:** `H^1_par(P1 \ S, sigma)` and the `chi`-multiplicity subspace of `H^1(C)` carry equivalent Hermitian determinant **classes** (up to a rational scalar and potentially K-conjugation), uniformly for finite-monodromy genus-zero covers.
- **B2:** that Jacobian-induced multiplicity polarization equals Severn's particular factor polarization up to the permitted scalar (still `HHO-OPEN-SUPPORT-TRANSFER`; needs the relevant primary source). Proving B1 **does not** discharge B2.

B1 is enough for a conditional dimension-independent **necessary gate**: a nonsplit parabolic-cup rank-eight datum must have an inert prime of positive chi-defect for the relevant effective group. It is not a full solution to P1 under (H), and says nothing about Severn's actual polarized factor until B2.

**B1 acceptance criteria:**
1. Define the exact functorial map (possibly dual/conjugate) between the two cohomologies; prove cup and Hodge compatibility for the finite branched cover.
2. Prove a determinant-ratio norm identity; equality of Gram matrices is stronger than necessary. Track `delta`, trace convention, `h_U`, `|G|`, the kernel of sigma and the rational scaling factor. Explicitly include p=2.
3. State the result for both the original group G and its effective image Gamma (via kernel descent if claimed). Keep the source theorem's hypotheses and `CHECKED` status separate from HHO adoption.
4. Test the formulated claim against **existing** C6, C3×F20, G34 and G(6,1,6) source cases; use structural comparisons or existing outputs first, not a fresh expensive campaign.
5. Prior-art check: Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality* (2006), and HCG Lemma E. No novelty claim before reading the relevant text.

**Direction 2 is second.** Deriving the period-map differential requires Hodge-filtration/Kodaira–Spencer and Gauss–Manin data; the topological cochain and triangular-cup model alone does not automatically supply it. If B1 succeeds, it defines the arithmetic target for a later differential/(D) campaign.

## Disposition for the owner

File the source note unchanged as historical session evidence, or publish a revised current note with a short change record. **Do not label the whole note CHECKED** until F1–F3 and the scope refinements are addressed. The present review changes no HHO register row, scientific grade, release record, branch, or tag; PI decides research priority and any subsequent adoption.
