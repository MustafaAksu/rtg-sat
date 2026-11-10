# HCG — Independent review of the tensor 3 x b extension and the d=43 exclusion

**Date:** 2026-10-30  
**Status:** SESSION / independent mathematical review. Not an adopted HCG result.  
**Input:** Claude, `H3_TENSOR_3x14_REVIEW_AND_D43_CLAUDE_v0_1.md` (full, 6.2 kB) and `H3_TENSOR_3x14_REVIEW_CLAUDE_v0_1.zip` (all eight entries inspected; source manifest verified).

## Decision

1. **3 x 14**: CHECKED, agreeing with the previous two-participant review.
2. **3 x b for 14 <= b <= 18**: CHECKED for factorwise tensor representations satisfying the inherited hypotheses (H). The argument requires no GAP enumeration.
3. **d=43**: CHECKED as a *conditional mathematical implication* using the previously reviewed normal-socle reduction and the Hiss–Malle ordinary-characteristic-zero completeness result. An independent published Weil-character estimate proves the sufficient movement rank >= 11 for the sole K-field, non-self-dual socle candidate `U7(2)`. This does not independently recover CTblLib's stronger exact minimum 16.
4. **Nonsplit feasible implies d>=44**: CHECKED, conditional on all inherited H hypotheses, normal-subgroup reduction, classification, and the previously checked exclusion through d=42. It is **not** existence at d=44.
5. **d=44 candidates**: still OPEN. No character-table exclusions for U5(2), M11, etc. were performed in this review.

## Source QA and computational extent

- Uploaded Claude ZIP internal manifest: 7 entries checked, **7/7 PASS**, excluding the manifest itself.
- Source `d43_peek.g` and output read; it reports two degree-43 U7(2) characters with minimum movement rank 16 and two degree-45 U4(2) with minimum 24. Source GAP itself **was not executed** in this environment.
- Source finite pseudoreflection triple enumeration read; finite examples supportive, not a proof.
- Independent `check_d43_analytic.py`: exhaustive exact integer bounds over three F4 eigenvalue multiplicities; tensor-budget inequalities for b=1..20; d=43 Lemma S/C numerical gate; d=44 factorwise-tensor preliminary budget. PASS.
- External source **read targeted text:** Katz–Tiep, *Hypergeometric Sheaves and Finite Symplectic and Unitary Groups*, §16, displayed equations (16.4.3)–(16.4.4) and the assertion on restriction to `SU_n(q)`, PDF pp. 45–46 in the web tool's zero-indexed view; Hiss–Malle (2001), degree-43 rows together with 2002 corrigendum record. No claim of full paper reading.

## A. Factorwise 3 x b, b=14..18

Set V=A⊗B, dim A=3 and dim B=b. Let N>=19, c(g)=rank(1-g), and sum c(g)=6b+8.
If g is scalar in PGL(A), then c(g)>=3 if effective. Otherwise c(g)>=b. The projective A-image is noncyclic (absolute irreducibility), so at least t>=3 branch generators have nontrivial projective A-image: t<=2 would make it cyclic by the product-one relation.

For t=4 and N=19, the minimum total movement is 4b+45; this exceeds 6b+8 for every b<=18. Thus t=3. The lower bound with t=3 and N=19 is 3b+48, leaving at most

    slack = 3b - 40.

An active A-factor with three distinct eigenvalues forces c(g)>=2b and hence costs >=b above the active baseline b. For b<=18, slack<b, so all three active A-factors have eigenvalue multiplicities (2,1), i.e. are projective unitary pseudoreflections. Since the other A-factors are projectively scalar, their product is projectively the identity. The three-pseudoreflection lemma (previously proved and independently reviewed) makes their moving lines mutually orthogonal or equal, hence the A-projective subgroup fixes a line. The full A⊗B representation would be reducible. Contradiction.

For b<14, the budget already excludes t=3. We do **not** infer that N=19 in all cases b>14; it is unnecessary.

## B. The independent U7(2) bound, eliminating d=43

**Inherited Hiss–Malle input.** In characteristic zero, after excluding self-dual representations via Lemma S and field-incompatible irreducibles, the remaining degree-43 non-self-dual simple-socle character with character field K=Q(sqrt(-3)) is the degree-43 Weil character of U7(2). The Hiss–Malle table has the row `43 U7(2) !=2,3 z3 (indicator circle)`; the tables' stated completeness and the GT normal-subgroup reduction are external theorem inputs, not reproved by the script.

**Independent source-based bound.** Let `G=SU_7(2)=PSU_7(2)`; its center has order gcd(7,3)=1. Katz–Tiep §16 gives an irreducible unitary Weil character for each i=0,1,2:

    zeta_i(g) = -(1/3) * sum_{j=0}^2 rho^(i*j) * (-2)^f_j(g),

where `rho` is a primitive complex cube root of 1, and `f_j(g)=dim_{F4} ker(g - xi^j I_7)` for a primitive xi in F4^×. The characters i=1,2 have degree 43 (i=0 has degree 42). Their restriction to SU_7(2) remains irreducible; this is explicitly asserted alongside eq. (16.4.4).

For nonidentity g in SU_7(2), each f_j<=6, because f_j=7 would make g=xi^j I and det(g)=xi^(7j)=xi^j, requiring g=I; and f_0+f_1+f_2<=7. Hence

    |zeta_i(g)| <= (2^f_0 + 2^f_1 + 2^f_2)/3 <= 67/3 < 23.

Every finite-order unitary 43x43 matrix has `Re trace(g) >= 43 - 2c(g)`; therefore

    c(g) >= (43 - |zeta_i(g)|)/2 > 10,
    i.e. c(g) >= 11 for every nonidentity g in U7(2).

The exact integer enumerator also finds the stronger upper bound `9|zeta_i(g)|^2 <= 4167`, over *all formal multiplicity triples*, without assuming they occur in SU7(2). This stronger numerical bound is not needed.

**Contrast with Lemma C.** In the inherited H framework, 19 effective branch generators with total movement rank 2*43+8=94 force at least one generator g with c(g)<=floor(94/19)=4. The normal-socle commutator lemma produces a **noncentral** h in the socle with c(h)<=2c(g)<=8, contradicting c(h)>=11 in U7(2). This proves the necessary contradiction without relying on the reported CTblLib exact min c=16. Thus the d=43 exclusion is verified from published source formulas plus the inherited classification chain.

**Independence caution.** This is an independent analytic lower bound for the last candidate, not an independent replay of the full U7(2) character table; it depends on the Hiss–Malle classification for *exhaustiveness*.

## C. The next dimension d=44

The self-dual-socle Lemma S first permits d=44: two nontrivial similitude multipliers require c>=22 each, and the other 17 effective branches have c>=3, giving 95 of the available 96 movement ranks. No d=44 feasibility is thereby constructed.

A preliminary *factorwise tensor* budget already excludes 2 x 22 and 4 x 11:

    2*44+8 = 96 < 3*22+16*2 = 98,
    2*44+8 = 96 < 3*11+16*4 = 97.

Both comparisons inherit the previously checked factorwise-tensor budget; other group types must be checked separately, especially ordinary self-dual simple socles. This is orientation, not a complete d=44 classification.

## Provenance and open obligations

- [SOURCE] Katz–Tiep (eq. 16.4.3, 16.4.4), https://web.math.princeton.edu/~nmk/kt15_105.pdf. Targeted PDF text read; visual screenshot unavailable in browser during this review.
- [SOURCE] Hiss–Malle 2001 and corrigenda 2002, https://agag-malle.math.rptu.de/~malle/download/low and https://doi.org/10.1112/S1461157000000711; relevant degree-43 rows read via indexed source text, not a new complete independent table construction.
- [SESSION] tensor 3xb proof and U7(2) trace bound, independently derived in this review.
- [UNVERIFIED] GAP's *exact minimum* c=16 for U7(2); source report plus output read, not independently recomputed. The weaker independently proved c>=11 suffices.
- [OPEN] Character-table or source-based d=44 exclusions, group-theoretic classification beyond the inherited regime, and construction of any nonsplit family.
- This has no effect on the adopted HCG v0.2, PI adoption decisions, or Severn Theorems A/B/C (CLAIMED).
