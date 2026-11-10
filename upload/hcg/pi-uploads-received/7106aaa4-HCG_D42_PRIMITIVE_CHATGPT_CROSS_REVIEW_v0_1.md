# HCG — Cross-review of the proposed primitive exclusion, degrees 25–42

**Date:** 30 October 2026  
**Reviewer:** ChatGPT  
**Distribution:** INTERNAL; standalone HCG research, no export to the Hodge auditor or canonical RTG owners.  
**Disposition:** Proof-level agreement with the proposed reduction and exclusion, **conditional on the reported exact character-table data**. The numerical GAP stage was not independently executed in this environment. The missing symplectic Weil estimate is supplied below by a source-backed proof. No PI adoption is implied.

## 1. Received sources and actual reading extent

Read the entire Claude report `H3_D25_CLASSIFICATION_REVIEW_AND_D42_PRIMITIVE_CLAUDE_v0_1.md` (SHA-256 `6280194c61704fdac040b77f749a80ec3560e6ee7ac8522ef57032c794bb7863`) and all four relevant computational sources in the received ZIP. The ZIP SHA-256 is `f4d7d4fca2ae19c6010252f50503007c89196134f52c1b4030d854790dda3558`. Its manifest validates **10/10** files. The standalone report and archived report are byte-identical.

Primary literature inspected in targeted sections (not whole-paper reproofs):

- Guralnick–Tiep, *Symmetric powers and a problem of Kollár and Larsen*, arXiv:0810.0853: hypothesis (S), Lemma 2.5, Proposition 2.8 and its finite-group reduction, PDF pp. 5–10. These hypotheses include complex primitivity, tensor indecomposability and exclusion of tensor induction.
- Hiss–Malle, *Low-dimensional representations of quasi-simple groups* (2001): Theorem 1, notation for characteristic zero, §6 and the generic Table 2 (PDF pp. 1, 9–10).
- Hiss–Malle, corrigenda (2002): corrected Table 2, degrees 25–42, PDF pp. 8–11. The original generic table must be retained; the corrected exceptional table does not replace the generic cases.
- Teruji Thomas, *The character of the Weil representation*, arXiv:math/0610644v3, Theorem 1A and Remark 1.2, PDF p. 2.
- Katz–Tiep, *Rigid local systems and finite symplectic groups*, FFA 59 (2019), §2, PDF pp. 4–5: the two total Weil representations, decomposition into dimensions (q^n±1)/2, central parity, and absolute trace formula.
- ATLAS, O7(3) page: outer automorphism group of order 2 and the triple-cover extension.

PDF text was accessible; repeated web screenshot attempts failed with `Cache miss`. No successful visual check of the Hiss–Malle table or proof formulas is claimed. The PDFs were not locally materialized and are not supplied with invented file hashes.

## 2. What was actually recomputed

- Ran `d25_counts_and_gt13_claude.py`, changing only its absolute path to the frozen sieve file. It exited successfully and its stdout was **byte-identical** to `d25_counts_and_gt13_claude_out.txt`.
- The source uses exact rational age-profile arithmetic and floating-point character-gap arithmetic. It should not be described as entirely exact merely because the profile counts are exact.
- An independent standard-library program checked the self-dual and commutator inequalities, the remaining imprimitive degree list, and a source-repair for the 40/41-dimensional Weil representations. An explicit symplectic transvection and its negative verify that the reported universal bound b≤6 is false.
- Parsed the received broad GAP log: it contains **20** eligible character rows across **nine** group-degree pairs; the table values agree with the prose report. This is output consistency, not a re-execution of its character calculations.
- GAP was absent. Package installation was unavailable in the runtime, and external downloads could not be materialized. **Neither GAP source was run here.** Raw character values and power maps are not in the supplied package.
- Prepared a GAP raw-data exporter covering **all** relevant characters and a separate Python exact cyclotomic Fourier checker. The checker passed four synthetic restrictions and one negative control. The exporter has not been run, and the checker has not yet received the actual character tables.

The companion package and its replay log explicitly preserve this boundary. A successful Python package replay is not a GAP replay or a proof of classification completeness.

## 3. Hypotheses and scope

The reviewed branch is a faithful absolutely irreducible K-model, K=Q(sqrt(-3)), with character field exactly K, satisfying the inherited genus-zero Hodge/dominance hypotheses. Its complex representation is primitive, tensor-indecomposable, and **not tensor-induced**. We use the previously established no-junior result, hence every effective branch generator has moving rank c_j≥3. There are N≥19 effective branch points and Σ c_j=2d+8.

These hypotheses cannot be compressed to “all primitive groups.” At d=42, the factorwise tensor budget permits (a,b)=(3,14), so the present result does not exclude every primitive representation of degree 42.

## 4. Lemma S — verified, including alternating forms

Let L be a normal subgroup whose restriction on V is irreducible and self-dual. Let B be its nondegenerate invariant symmetric or alternating complex bilinear form. Schur's lemma and normality give a multiplicative character a:Γ→C× with B(gx,gy)=a(g)B(x,y).

If a(g)≠1, Fix(g) is totally isotropic for B. Thus c(g)≥ceil(d/2). If a were trivial on every branch generator, Γ would preserve B, so its character would be real and K-valued, hence rational, contradicting the exact character field. The product-one condition therefore forces at least two nontrivial multipliers.

Consequently

    2d+8 = Σ c_j ≥ 2 ceil(d/2) + 3(N−2) ≥ 2 ceil(d/2)+51.

This excludes the self-dual normal-subgroup case for 25≤d≤42. The sharper integral form also excludes d=43: the first possible budget degree is 44. This last observation concerns only the self-dual branch, not all degree-43 candidates.

**Disposition:** CHECKED as a mathematical lemma, under the stated hypotheses.

## 5. Lemma C — verified after an explicit noncentrality step

Choose a branch generator g with c(g)≤floor((2d+8)/19). Since c(g)<d and the normal subgroup L (or the symplectic-type subgroup P) acts irreducibly, g is nonscalar and does not centralize that subgroup. Choose x with h=[g,x]≠1. Then

    h∈L,   c(h)≤c(g)+c(xg^{-1}x^{-1})=2c(g).

The received text goes directly from h≠1 to “h is noncentral.” That implication alone is false in general. Here it is repaired by the available strict inequality

    2c(g)<d.

A nonidentity scalar has moving rank d. Hence h is nonscalar; since the centre of an irreducibly acting subgroup is scalar, h is noncentral. The thresholds are 6 for d≤33 and 8 for 34≤d≤42.

For a subgroup P introduced by scalar normalization, explicitly retain C×H=C×Γ and H′=Γ′. Conjugation and commutators are unchanged by scalar factors, so the needed commutator lies in Γ∩P; no assertion that all normalizing scalars are K-rational is required.

**Disposition:** CHECKED with this added justification. This is a proof clarification, not a counterexample.

## 6. Symplectic-type normal subgroup

An order-p scalar in the commutator subgroup lies in Γ, hence in μ6. Thus p=2 or 3. In the degree range the only powers p^a are 27 and 32. On a noncentral element of the symplectic-type p-group, conjugation by a suitable group element multiplies the matrix by a primitive pth root. Its eigenvalues occur in p-cycles of equal multiplicity, giving dim Fix≤d/p and

    c(h)≥18  (d=27),     c(h)≥16  (d=32).

Both contradict the commutator threshold 6. This verifies the stated exclusion **in the inspected degree interval**. The source heading “for every d” should not be used as an unqualified global statement based only on this calculation.

## 7. Quasisimple candidates and computational evidence

Hiss–Malle's corrected characteristic-zero rows with nonreal field contained in K, together with its original generic table, agree with the following list. Self-dual rows have already been eliminated. Generic alternating natural modules are self-dual. In the SL2(q) families, the only nonreal field K occurs in the half-degree cases with q=3^{odd}; no such degrees lie between 25 and 42.

| L | d | Received minimum moving rank | Required upper bound from Lemma C | Review route |
|---|---:|---:|---:|---|
| 3.O7(3) | 27 | 6 | 6 | Outer-invariance and projective rank step needed |
| 3.G2(3) | 27 | 12 | 6 | GAP data + Lemma C |
| U4(2) | 30 | 12 | 6 | GAP data + Lemma C |
| 2.U4(2) | 36 | 18 | 8 | GAP data + Lemma C |
| 3_2.U4(3) | 36 | 16 | 8 | GAP data + Lemma C |
| 6.A7 | 36 | 24 | 8 | GAP data + Lemma C |
| 6.L3(4) | 36 | 16 | 8 | GAP data + Lemma C |
| U4(2) | 40 | 20 | 8 | GAP data + Lemma C |
| S8(3) | 41 | 16 reported; ≥9 suffices | 8 | Also follows from §8 independently of its GAP minimum |
| 2.S8(3) | 40 | ≥9 | 8 | Published Weil trace formula + §8 proof |

**Every-character coverage:** `candidates_pmr.g` examines `chis{[1]}` only. The broader `quasisimple_scan.g` does loop over all characters. Its supplied log contains two characters in each listed available pair except 3.G2(3), where there are four; all four have reported minimum 12. The finer projective/outer argument is essential only for 3.O7(3). Its two characters are a complex-conjugate pair, so moving/projective ranks agree and outer noninvariance is conjugation-stable. Thus this source-code observation does not by itself invalidate the theorem. Nevertheless the delivered portable exporter covers every character explicitly.

**3.O7(3):** ATLAS states Out(O7(3)) has order 2. If the index-two fusion computation is correct, norm 1 of the induced character means the unique nontrivial outer automorphism does not fix the character. Then Γ⊂C×L. The reported minimum projective moving rank 6 applies to any scalar multiple of a noncentral L-element; nonidentity central scalars have moving rank d. Therefore Σc_j≥19·6=114>62. This conclusion is conditional on the reported power-map and fusion values until those bytes are independently checked.

The finite classification input is not established by “459 tables scanned” alone: completeness comes from Hiss–Malle, not the size of the installed library.

## 8. Missing 2.S8(3) row — source-backed repair

The received report uses a≤7 and b≤6 for noncentral h∈Sp8(F3), where a=dim ker(h−1), b=dim ker(h+1). The b≤6 claim is false. If T is a nontrivial transvection, h=−T has (a,b)=(0,7). This was verified by an explicit 8×8 symplectic matrix over F3.

The needed trace bound is nevertheless correct with a symmetric proof:

1. For h≠±I, a,b≤7 and a+b≤8.
2. If a=7, h−1 has rank one and det h=1. All eigenvalues are 1, so b=0. Likewise b=7 forces a=0.
3. Thomas Theorem 1A gives |χ_W(h)|=3^{a/2} for the total degree-81 Weil representation. The degree-40 and degree-41 constituents are the two central-parity pieces; hence

       |χ_40(h)|, |χ_41(h)| ≤ (3^{a/2}+3^{b/2})/2.

4. If a,b≤6 with a+b≤8, the right side is at most 15. At the two exceptional pairs (7,0),(0,7), it is (27√3+1)/2. Therefore uniformly

       |χ_40(h)|, |χ_41(h)| ≤ (27√3+1)/2 < 24.

   The last inequality follows exactly from 47²−3·27²=22>0.
5. For a finite-order D-dimensional matrix, D−Reχ(h)≤2c(h). Thus

       c_40(h)≥9,    c_41(h)≥9,

   because each is an integer and (D−|χ(h)|)/2>8.

This excludes both the faithful 40-dimensional Sp8(3) case and the 41-dimensional PSp8(3) case required here. It does not compute their exact minimum ranks. It needs no absent Sp8(3) CTblLib table.

**Evidence:** direct inspection of Thomas Theorem 1A/Remark 1.2 and Katz–Tiep §2, plus the written argument and independent exact finite checks. This is a new repaired source-backed argument, not a claim that Claude had already reread these sources.

## 9. Conclusion and dispositions

No unrepaired mathematical obstruction to the proposed exclusion was found. The logical argument is coherent after §5 and §8. However a complete independent computational check of the quasisimple table entries has not occurred here.

| Item | ChatGPT recommendation |
|---|---|
| Existing degree-25 exclusion / d≥26 | Retain CHECKED from the previous review |
| Lemma S | CHECKED; optional stronger self-dual threshold 44 |
| Lemma C | CHECKED with explicit 2c<d noncentrality argument |
| Symplectic-type 27/32 exclusion | CHECKED, scoped to the relevant branch |
| Hiss–Malle candidate list | SOURCE-CROSS-CHECKED from primary text; no successful visual PDF check |
| 40/41-dimensional Weil lower bound ≥9 | Source-backed repaired proof; peer review requested for the written repair |
| GAP moving/projective ranks and outer fusion | SOURCE-REPORTED; scripts/logs inspected, NOT independently executed |
| Primitive tensor-indecomposable non-tensor-induced exclusion 25–42 | CONDITIONAL proof-level agreement; full second-implementation data check pending |
| Overall nonsplit feasibility | OPEN; no all-d≤42 exclusion |

For d≤41, the stated imprimitive-only list follows conditional on the table-dependent exclusion and prior tensor bounds. At d=42, factorwise tensor 3⊗14 remains a budget possibility; the review does not exclude it. HCG v0.2, PI disposition fields and Severn A/B/C CLAIMED status remain unchanged.

## 10. Minimal remaining computational handoff

Rather than rerunning the broad 459-table scan, export the raw character values and class power maps of the nine available group-degree pairs, for all 20 eligible characters, plus the 3.O7(3)→3.O7(3).2 fusion. A GAP exporter and a separate standard-library exact cyclotomic checker are supplied.

The exporter is marked NOT EXECUTED in this environment. It includes version metadata. The Python verifier computes cyclic eigenvalue multiplicities from the raw values; it does not trust the printed minimum-rank summaries. The all-character version addresses the first-character shortcut. Its synthetic tests passed, but the actual raw table export is still required.

## Primary sources

- GT08: https://arxiv.org/pdf/0810.0853
- Hiss–Malle 2001: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E38996E7B21A5CC48280AC441B6054AA/S1461157000000796a.pdf/lowdimensional_representations_of_quasisimple_groups.pdf
- Hiss–Malle corrigenda: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A3E3E934BEB019B905E1BBCA4A0F20D5/S1461157000000711a.pdf/corrigenda_lowdimensional_representations_of_quasisimple_groups.pdf
- Thomas: https://arxiv.org/pdf/math/0610644
- Katz–Tiep: https://web.math.princeton.edu/~nmk/KT9_published.pdf
- ATLAS O7(3): https://brauer.maths.qmul.ac.uk/Atlas/clas/O73/
