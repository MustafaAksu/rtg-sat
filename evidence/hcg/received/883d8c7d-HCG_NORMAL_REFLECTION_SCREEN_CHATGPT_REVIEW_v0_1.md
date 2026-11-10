# HCG — Independent review of the normal-reflection-subgroup screen

**Date:** 29 October 2026  
**Status:** SESSION; independent proof cross-review, not PI adoption. INTERNAL.  
**Reviewed source:** `H3_D7_SCREEN_REVIEW_AND_D7_9_EXCLUSION_CLAUDE_v0_1.md`, SHA-256 `6095beaf916a712df6aca70dc32ca30056ec11ec5a115ecce895e820a6ac259b`.  
**Original bundle:** `H3_D7_SCREEN_REVIEW_CLAUDE_v0_1.zip`, SHA-256 `5ae991fba47db3ebadea88dd3904370b7682218c9a3607371a72d63af8edc62e`.

## 1. Decision and limits

**Lemma B (real Weyl normalizer), Lemma C (monomial normalizer), Lemma D (block rank bound), and the resulting exclusion of coefficient dimensions 7, 8, 9 and 11 pass independent mathematical review under the stated hypotheses.** The previous three rank profiles at d=7 are not remaining candidates once this additional argument is used.

The d=10 table correctly identifies what survives the *reflection-subgroup branch budget*: two blocks of rank 5 or five blocks of rank 2, in each case with a genus-zero intermediate curve. It does **not** establish feasibility or dominance of either type. A separate new proposed note, `HCG_INDUCED_PERIOD_DIMENSION_BOUND_PROPOSED_v0_1.md`, derives period-rank bounds 15 and 9 respectively, which would exclude these two residual types as well. That additional deduction has not yet undergone peer review and is not included in the CHECKED decision above.

These are statements about the finite-monodromy genus-zero Hurwitz construction of a weight-one multiplicity variation of K-dimension 8. They do not exclude arbitrary Weil eightfold families, other geometric constructions, or smaller-rank period maps. No assertion of novelty is made.

## 2. Evidence and reading extent

- Read the complete uploaded Claude report, its D-11/D-12 addendum, current pending-delta entry, source script, exact output and closeout replay log.
- Verified **6/6** entries of the submitted bundle manifest; standalone report and ZIP copy are byte-identical.
- Read and executed `nonsplit8_budget_screen_claude.py` without changing its code. Its output is byte-identical to `nonsplit8_budget_screen_claude_out.txt`.
- Independently rederived the mathematical arguments below, and wrote a separate standard-library exact checker. It verifies the seven-dimensional profiles implicitly through the dimension screen, the incidence inequalities, the block-cycle rank identity and the d=10 intermediate-genus calculation. Arithmetic output alone is not a proof of the classification or of period factorization.
- Consulted Marin–Michel, *Automorphisms of complex reflection groups*, arXiv:math/0701266v3, **§3 (pp. 8–9), Lemma 4.2 (p. 10), and the relevant field entries and rational Weyl-group discussion on pp. 18–21**, using parsed primary text. PDF screenshot requests failed in this tool session; no successful visual-PDF comparison is claimed.
- Consulted the official Magma handbook, *Construction of Finite Complex Reflection Groups*, for the rank-5 through rank-8 exceptional list and the classification of imprimitive reflection groups. This is a classification lookup, not an executed Magma calculation.
- Consulted Dettweiler–Wewers (2006), §1.2, for the parabolic-cohomology model used in the separate induced-variation note.
- Hexagon v1/v2 could not be fetched in this session. The specific Severn §8 wording is therefore not newly source-verified here. Its already-recorded monomial factorization is retained as an explicit dependency of the submitted screen; the separate note also spells out the relevant finite-cover argument.
- Did **not** rerun the unchanged 85-second locality closeout, its 320-case campaign, or the earlier G34 rank-2 census. Their receipt/peer replay is reported by Claude, not newly executed here.

## 3. Hypotheses and notation

Let K=Q(sqrt(-3)), let Gamma=sigma(G) be the finite faithful image on V, and assume the representation is absolutely irreducible of K-dimension d, with character field exactly K. Work with an effective, product-one, generating local monodromy tuple g_1,...,g_N in Gamma. Let

\[
c_j=\operatorname{rank}_K(1-g_j)\ge1,
\qquad \dim_K H^1_{\rm par}=8.
\]

The no-invariants parabolic Euler formula and the necessary dimension for dominance are

\[
\sum_jc_j=2d+8,\qquad N\ge19,
\qquad \varepsilon:=\sum_j(c_j-1)=2d+8-N\le2d-11.
\tag{1}
\]

Points invisible to sigma are not counted as effective punctures; allowing extra such points does not add variation to the target local system. All dimension exclusions concern dominance to a 16-dimensional period domain, not the existence of product-one tuples in themselves.

For d<=12, the tuple must contain a reflection: if c_j>=2 for every j then 2N<=2d+8, incompatible with N>=19. More generally this argument works for d<=14.

## 4. Normal reflection subgroup and block decomposition

Set

\[
W_R=\langle s\in\Gamma:\operatorname{rank}(1-s)=1\rangle.
\]

It is nontrivial and normal. Its fixed space is Gamma-stable, so absolute irreducibility implies V^{W_R}=0.

A concrete way to see the decomposition is to put an edge between two reflection lines when they are not orthogonal for a Gamma-invariant positive Hermitian form. The connected components span mutually orthogonal subspaces V_i, each preserved irreducibly by the subgroup W_i generated by its reflections. Reflections from one component fix every other component. Thus

\[
V=\bigoplus_{i=1}^{k}V_i,\qquad W_R=\prod_{i=1}^{k}W_i.
\]

Gamma permutes the reflection lines and hence their connected components. If this permutation were not transitive, the sum over one orbit would be a proper Gamma-invariant subspace. Hence dim V_i=r and d=kr. Since the reflection matrices and their moving lines are K-defined, these component subspaces are K-defined as well.

This establishes the structural reduction without presupposing that Gamma itself is reflection-generated.

## 5. Lemma C: normalizers of G(m,p,d) are monomial for d>=5

Write eta=1 if p<m and eta=0 if p=m. For a line represented by a vector with z zero coordinates, the number of reflecting hyperplanes through it satisfies

\[
f(z)\le m\binom z2+\binom{d-z}2+\eta z.
\]

The first term counts all hyperplanes between zero coordinates; at most one hyperplane x_i=zeta x_j contains a given nonzero coordinate pair. The final term counts coordinate hyperplanes only when they actually occur. For a coordinate line,

\[
M=m\binom{d-1}2+\eta(d-1).
\]

The upper-bound polynomial is convex in z. On 0<=z<=d-2 it suffices to compare endpoints:

\[
M-f(0)=\frac{d-1}{2}\{m(d-2)-d+2\eta\}>0,
\]
\[
M-f(d-2)=m(d-2)-1+\eta>0
\]

for m>=2,d>=5. Coordinate lines are therefore intrinsically the lines of maximum incidence. A normalizer permutes them and is monomial.

**Minor wording repair:** the report's preliminary inequality should consistently use `eta*z`, not an unconditional `+z`; its final endpoint calculation already uses the correct eta.

This also agrees with Marin–Michel Lemma 4.2: in rank at least five, the diagonal subgroup is characteristic; its common eigenspaces are the coordinate lines. Low-rank exceptions such as D4 triality are real and are not being ignored—they are outside this k=1,d>=6 application. The exact checker verifies 29,412 finite incidence inequalities and explicitly catches the D4 equality; the proof is the two inequalities above, not that finite regression.

## 6. Lemma B: simply-laced real Weyl normalizers

For W of type A_d, E6, E7 or E8 in its reflection representation, let q be its standard nondegenerate invariant symmetric bilinear form. If g normalizes W, irreducibility gives g^t q g=lambda^2 q. Then u=lambda^{-1}g is q-orthogonal and permutes reflection lines. Normalizing all roots to q-length 2 shows u maps each root to a root or its negative. Thus u belongs to Aut(Phi).

For these types Aut(Phi) is W or W times the global sign. Therefore

\[
N_{GL(V)}(W)=\mathbb C^\times W.
\]

For finite Gamma, the scalars occurring in lambda*w are roots of unity. The scalar modulo {+1,-1} defines a well-defined homomorphism from Gamma. If it is trivial, all traces are rational, contradicting the character-field hypothesis. Therefore a generating product-one branch tuple contains at least two entries lambda*w with lambda non-real.

A real w has equal multiplicities at non-real conjugate eigenvalues, giving

\[
\operatorname{rank}(1-\lambda w)\ge\lceil d/2\rceil.
\]

For type A_d, w is the standard part of a permutation of d+1 letters. A non-real eigenvalue of order t>=3 has multiplicity at most floor((d+1)/t), hence at most floor((d+1)/3). Thus

\[
\varepsilon\ge
\begin{cases}
2\bigl(d-\lfloor(d+1)/3\rfloor-1\bigr),&A_d,\\
2\bigl(\lceil d/2\rceil-1\bigr),&E_6,E_7,E_8.
\end{cases}
\tag{2}
\]

This proof does not assume a specific cubic scalar extension in advance. It applies to all finite groups in the indicated linear normalizer. The character-field hypothesis is essential.

## 7. Lemma D: exact block-cycle identity and budget

For g inducing a block permutation pi, let P_a be its return map on one rank-r block around a cycle a of pi. Then

\[
\operatorname{rank}(1-g)
=r\,\operatorname{ind}(\pi)+\sum_{a}\operatorname{rank}(1-P_a).
\tag{3}
\]

Indeed, on a cycle of length ell, a fixed vector is determined by its initial block vector, constrained by P_a v=v. The formula follows by subtracting the fixed dimension from r*ell.

Let J=sum_j ind(pi_j), and let t be the number of nonidentity pi_j. Transitivity and product one give a connected degree-k cover Y of P1 with genus gamma and

\[
J=2(k-1)+2\gamma.
\]

For the t block-moving entries, c_j-1>=r*ind(pi_j)-1; other entries contribute nonnegatively. Since t<=J,

\[
\boxed{\varepsilon\ge(r-1)J
=2(r-1)(k-1+\gamma).}
\tag{4}
\]

This strengthens the stated bound by retaining the intermediate genus. The independent exact matrix checker verifies (3) on 366 signed block-permutation matrices and detects 347 failures of the deliberately incorrect formula obtained by omitting the return-map defects. These computations test the identity, not the existence of Hurwitz tuples with arbitrary prescribed cycle types.

## 8. Classification and dimension decisions

Using the Shephard–Todd list, the only additional primitive reflection groups of ranks 6,7,8 are respectively G34 and E6; E7; E8. In higher ranks only the symmetric and imprimitive families remain. For d>=7, there is no non-real exceptional full-rank reflection group. Normalizers must still be considered; Sections 5–6 do that.

| d | epsilon max | type-A lower | E-type lower if applicable | smallest proper nonmonomial-block lower | Result of this screen |
|---:|---:|---:|---:|---:|---|
| 6 | 1 | 6 | 4 | 4 | G34 remains; prior locality result addresses nonsplitness |
| 7 | 3 | 8 | 6 | none | excluded |
| 8 | 5 | 8 | 6 | 6 | excluded |
| 9 | 7 | 10 | — | 8 | excluded |
| 10 | 9 | 12 | — | 8 | (k,r)=(2,5),(5,2) survive this budget only |
| 11 | 11 | 12 | — | none | excluded |
| 12 | 13 | 14 | — | 10 | several proper block types survive this budget only |

The r=1 and monomial-normalizer cases use the stated monomial period-dimension exclusion, not just branch counting. They are not assertions that such group representations do not exist.

For the d=6 survivor, the G34 normalizer has only scalar freedom modulo G34 (Marin–Michel §3). In a K-model the extra scalars must lie in K; finite order makes them elements of mu6, already central in G34. Thus the faithful image is G34, not an uncontrolled scalar extension. This is a small additional precision in the d=6 reduction, and is not needed for the new d=7/8/9/11 exclusions.

## 9. d=10: what the submitted lemma actually establishes

For (k,r)=(2,5), (4) and epsilon<=9 force J=2, gamma=0. For (k,r)=(5,2), they force J=8, gamma=0. These are genus-zero induced representations sigma=Ind_H^Gamma tau, dim_K tau=r.

**The conclusion 'next search d=10' does not yet follow:** these residues survive only the downstairs branch-count screen. Applying the same effective-puncture count to the inducing rank-5 or rank-2 system on Y=P1 gives at most 18 or 12 active punctures, hence potential period dimensions at most 15 or 9, provided the Hodge-Shapiro factorization is made explicit. The separate proposed note proves that factorization in the finite-cover setting and formulates the resulting additional exclusion. Keep it separate from Claude's independently CHECKED lemma until its peer review.

## 10. Proposed record disposition

- `HCG-LEM-NONSPLIT8-NORMAL-REFL`: **CHECKED**, with faithful-image/effective-puncture conventions and inherited monomial exclusion explicit.
- d=7,8,9,11 dominance exclusions: **CHECKED under the submitted hypotheses**; no local-discriminant scan is needed at those ranks.
- Earlier three d=7 rank profiles: retain historically as 'not excluded by the earlier budget alone'; now excluded by the normal-reflection-subgroup argument.
- d=10 residue: **not a constructed candidate**. Its two allowed block types and gamma=0 conclusion are CHECKED. The new induced-period-rank exclusion is **PROPOSED**.
- Existing locality theorem and d=6 conditional closure: unchanged. Source closeout replay completed by Claude, not re-executed here.
- HCG v0.2 ADOPTED, Severn A/B/C CLAIMED and PI decision fields: unchanged.

## References and source limitations

1. I. Marin and J. Michel, *Automorphisms of complex reflection groups*, arXiv:math/0701266v3 (12 March 2009), especially §3 and Lemma 4.2. https://arxiv.org/pdf/math/0701266
2. Magma Handbook, *Construction of Finite Complex Reflection Groups*, rank list and G(m,p,n) classification. https://magma.maths.usyd.edu.au/magma/handbook/text/1228
3. M. Dettweiler and S. Wewers, *Variation of parabolic cohomology and Poincare duality*, Seminaires et Congres 13 (2006), 145–164, §1.2. https://www.emis.de/ft/47210
4. Severn, hexagon:2610.00387v1, §8: inherited source pin; retrieval failed this session. No new full-text source verification claimed.

No public-priority or novelty assertion is made. The new imprimitive rank bound should be compared with Severn's existing genus-zero-imprimitive discussion before any publication claim.
