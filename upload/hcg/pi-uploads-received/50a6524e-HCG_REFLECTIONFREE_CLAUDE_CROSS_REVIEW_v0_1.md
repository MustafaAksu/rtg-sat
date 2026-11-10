# HCG — Independent review of the reflection-free screen (ChatGPT) v0.1

**Date:** 2026-10-29. **Status:** SESSION REVIEW; not PI adoption. **Distribution:** INTERNAL.
**Reviewed source:** `H3_REFLECTIONFREE_SCREEN_REVIEW_CLAUDE_v0_1.md`, SHA-256 `3b9d0b8c33c853ce647487700c08ee4b1097f48ebc5a1b09d73bb85dd699cc89`.
**Source archive:** `H3_REFLECTIONFREE_SCREEN_REVIEW_CLAUDE_v0_1.zip`, SHA-256 `e01162dabad0c60c5ef2e02b96a74f59000e94481b11015ac5b9a0d9150363fe`.
**Reading extent:** Entire supplied report and script; targeted preceding induced-period and reflection-dichotomy notes. No claim that all historical HCG certificates were replayed.

## 1. Verdict and separation of review from new research

The scalar-triple lemma and the field-free induced-period bound are correct in their stated finite-cover setting. The K-imprimitive exclusion through coefficient dimension 29 follows from the previously reviewed Lemma E and the d<=14 obstruction. The listed complex-imprimitive possibilities for d=15,...,24 are correct as a preliminary necessary-condition list. The source-limited Huffman argument is logically consistent with the thesis theorem statements in Caltech's record, but its original full proof is not newly certified here.

A separate new note supplies a **PROPOSED** stronger exclusion of the entire range 15<=d<=24. It uses a sharper reflection-free block budget and Guralnick–Tiep (2012), Corollary 1.6, after explicitly disposing of its tensor-decomposability exception. Do not upgrade that new synthesis to independently CHECKED before Claude's review.

## 2. Computational audit

The archive manifest has five file entries and all five hashes pass. The standalone source report matches the archive copy. The source script was read, then executed unmodified with the Python standard library. Its stdout is byte-identical to the supplied `_out.txt`:

- 10 allowed spectral pairs;
- 21,600 unordered product-one triples with orders dividing 360, no violation;
- scalar-budget checks for d=6,...,400.

An independently written standard-library checker uses exact polynomial arithmetic in Q[z]/Phi_120(z), not the submitted Galois-pair-set test, to test both trace and determinant membership in Q(z^40). It reproduces all ten pairs. It additionally checks the new integer budgets and 2,040 finite tensor-eigenvalue examples. These finite checks support the written proofs; they do not establish classification or Hodge-factorization theorems by experiment.

No historic 60-case block-cup campaign was rerun in this review. The new package is self-contained and imports no `generic_engine.py`.

## 3. General scalar-triple lemma — CHECKED

Let lambda_1 lambda_2 lambda_3=1, with roots of unity lambda_i !=1. Write q_i=ord(lambda_i).

If every q_i>=3, sum 1/q_i<=1. Otherwise take q_1=2. Then lambda_3=-lambda_2^{-1}. A second order-2 entry would force the third root to be 1, which is excluded. If q_2=3 or q_3=3, the orders are (2,3,6); otherwise q_2,q_3>=4. In both cases sum 1/q_i<=1.

This proves the lemma for all roots of unity, not merely mu_6. Consequently the already reviewed type-A rank<=12 argument extends to arbitrary finite scalar groups, **provided** the same actual standard/scalar representation, product-one relation, eight-dimensional multiplicity, and nonrational character conditions hold. The last condition supplies at least two nonreal scalar entries; it must not be silently dropped.

## 4. Field-free induced-period bound — CHECKED

Fix a complex embedding of K. Let V_C=Ind_H^Gamma tau be any complex imprimitivity realization, r=dim_C tau. The corresponding complex multiplicity space has dimension eight:

M_iota = Hom_{C[Gamma]}(V_C,H^1(C,C))
       = Hom_{C[H]}(tau,H^1(C,C)).

This isomorphism commutes with Hodge decomposition and Gauss–Manin transport: its construction uses only fixed finite-group actions. With Y=C/H and Y_tau=C/ker(tau), the right-hand side is an isotypic summand of H^1(Y_tau,C). The cover Y_tau -> Y is branched exactly at the s points where tau-inertia is nontrivial. Its topological finite monodromy is discrete. Thus the varying Hodge filtration factors through the moduli of (Y,D_tau), without requiring a K-model of the blocks.

If gamma=g(Y), then

8 = 2r(gamma-1) + sum_y rank(1-h_y),
rank dPer <= 3gamma-3+s <= 2r+5+(3-2r)gamma.

For r=1, nontriviality of tau gives rank<=12. For r>=2, gamma>=1 makes the bound at most 8. Hence dominance forces gamma=0 and r>=6. Stable pointed-curve hypotheses hold in the cases used; degenerate pointed curves do not supply missing period directions.

**Field boundary:** This verifies the complex period-rank statement. It does not identify a K-discriminant for tau unless the blocks descend to K. The supplier condition (L) is not transported or used in this rank obstruction.

## 5. K-imprimitive data through d=29 — CHECKED with inherited hypotheses

For a K-defined block system, Lemma E gives an absolutely irreducible inducing K-datum of rank r=d/k, k>=2, with the same eight-dimensional Hodge variation and the same discriminant class. Its character field is exactly K: if the inducing character were rational, its induced character would be rational too.

For d<=29, r<=14. The previously reviewed no-nonsplit theorem in that range therefore applies. Thus a nonsplit dominant K-imprimitive datum requires d>=30. This statement retains the finite-cover/Hodge and polarization-discriminant assumptions of Lemma E and Theorem R; it does not assert transmission of (L).

## 6. Branch list and codimension-two count — CHECKED as a preliminary screen

Reflection-freeness gives c_j>=2 and sum c_j=2d+8, N_eff>=19. If a is the number of branch elements with c_j=2, then

2d+8 >= 3N_eff-a, hence a>=49-2d.

Thus a codimension-two element occurs for every d=15,...,24.

The field-free block bound requires r>=6. Factorizations d=kr with k>=2 give exactly the submitted list:

- d=16: (2,8);
- d=18: (2,9),(3,6);
- d=20: (2,10);
- d=21: (3,7);
- d=22: (2,11);
- d=24: (2,12),(3,8),(4,6).

No such factorization occurs at d=15,17,19,23. All block-permuting elements have movement rank at least r, so c_j=2 elements fix every block. This list is correct; the companion new note derives an additional necessary inequality that eliminates all entries.

## 7. Literature check: what was and was not actually read

### Huffman thesis and requested historical papers

Caltech's own record for W. C. Huffman, *Eigenvalue Structure in Primitive Linear Groups* (1974), DOI 10.7907/1hnq-y922, clearly displays the reciprocal cubic and reciprocal quartic theorem statements, including finite, faithful, irreducible, complex-primitive, unimodular hypotheses. It confirms the intended conjugation symbols in the summary. This is a primary institutional abstract, **not a fresh full-thesis proof review**.

The original thesis PDF was not retrievable as usable local bytes: the web request reported 38,665,317 bytes exceeding its limit, other host variants failed, and the container downloader could not fetch it. The 1975/1977/1978 Huffman–Wales full texts were also not acquired. No local PDF or full-text proof certification is claimed.

The reciprocal-type argument in source §3.4 is therefore a valid **conditional application** of the stated thesis results, with a remaining primary-full-text limitation. Complex primitivity, preservation of the selected spectrum under unimodular lifting, and identification of the alternating representation as the deleted standard representation remain essential.

### Alternative published primary result

A usable later source was found: R. M. Guralnick and P. H. Tiep, *A problem of Kollar and Larsen on finite linear groups and crepant resolutions*, JEMS 14 (2012), 605–657, DOI 10.4171/JEMS/313. Read the publisher-PDF text for Corollary 1.6 (pp. 608–609), Definition 2.1, the statement of Theorem 1.4 and the proof of Corollary 1.6 (§5.9, pp. 653–654). The arXiv preprint was checked for statement agreement. The article's entire 53-page proof campaign and its external dependencies were not independently reproved.

The usable consequence is: in complex dimension at least 11, a finite irreducible complex-primitive **tensor-indecomposable** group with a noncentral element of age<=1 has the deleted alternating-standard representation up to scalars. The central-junior alternative in Corollary 1.6 is incompatible with such a noncentral element. The published quotient formulation is invoked through its stated Reid–Tai setup; our application is reflection-free.

**Technical access limitation:** PDF screenshot commands were attempted on the publisher and arXiv copies but returned cache errors. The formulas above were checked in parsed primary text, not visually verified scans. No table or diagram from the article is used. The new deduction does not depend on garbled symbols in the unavailable Huffman PDF.

## 8. Proposed dispositions

| Item | Reviewer recommendation |
|---|---|
| General scalar-triple lemma and rank<=12 extension | CHECKED under the same standard/scalar model |
| Field-free complex induced-period bound | CHECKED; no automatic K-discriminant descent |
| K-imprimitive split through d=29 | CHECKED with Lemma E/Theorem R dependencies |
| Original d=15,...,24 branch map | CHECKED as a necessary-condition list, not an existence claim |
| Reciprocal Huffman route | Conditional proof; original full-text review still incomplete |
| New reflection-free imprimitivity budget | PROPOSED in companion note |
| New exclusion of 15<=d<=24 | PROPOSED, requiring independent peer review |
| HCG adopted v0.2; Severn A/B/C | Unchanged |

The new results, if confirmed, make acquiring every historical Huffman–Wales paper unnecessary for **this particular range**. That does not retroactively certify sources we have not read or establish publication novelty.
