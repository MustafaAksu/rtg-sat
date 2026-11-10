# HCG — Effective-puncture bound for induced finite-monodromy variations

**Date:** 29 October 2026  
**Provenance:** SESSION derivation by ChatGPT; **PROPOSED, peer review pending**. INTERNAL.  
**Purpose:** Test whether the two d=10 cases left by Claude's normal-reflection-subgroup budget can actually satisfy period-map dominance. No novelty claim. No adopted HCG document is modified.

## 1. Precisely stated candidate theorem

Let C -> X=P1 be a family of connected finite Galois covers with a fixed finite deck group Gamma. Let sigma be an absolutely irreducible K-representation with

\[
\sigma\cong\operatorname{Ind}_H^\Gamma\tau,
\qquad [\Gamma:H]=k,
\qquad\dim_K\tau=r\ge2.
\]

Assume tau has no invariant vectors (automatic here for irreducible tau of rank >=2), and the sigma multiplicity variation has K-dimension 2n. Write Y=C/H, with genus gamma. Fix the topological representation and the K-action; a finite marking/level cover may be used locally.

Let D_tau consist of the points of Y at which the associated finite-image tau local system has **nontrivial** local monodromy, and write s=|D_tau|. Suppose the Hodge variation is the one induced by cohomology of these finite covers (not an arbitrary choice of Hodge filtration on the same abstract representation).

Then the proposed bound is

\[
\boxed{\operatorname{rank}_{\mathbb C}(\mathrm{Per}_{\sigma})
\le 3\gamma-3+s
\le 2n+2r-3+(3-2r)\gamma.}
\tag{P1}
\]

Only stable pointed-curve cases are used here; for 2n=8 and r>=2 the numerical conditions ensure stability. In particular, since 3-2r<0,

\[
\boxed{\operatorname{rank}_{\mathbb C}(\mathrm{Per}_{\sigma})
\le 2n+2r-3.}
\tag{P2}
\]

For n=4, an inducing block of rank r<=5 cannot dominate the 16-dimensional Weil-type period domain. A necessary condition for dominance by an induced rank-r finite system is

\[
r\ge \left\lceil\frac{n^2-2n+3}{2}\right\rceil
\quad(r\ge2).
\tag{P3}
\]

The total coefficient dimension d=kr does not substitute for the inducing rank r in this bound.

## 2. Cohomological and Hodge identification

Frobenius reciprocity gives, on the cohomology of each finite cover C,

\[
\operatorname{Hom}_{K[\Gamma]}(\operatorname{Ind}_H^\Gamma\tau,H^1(C,K))
\cong
\operatorname{Hom}_{K[H]}(\tau,H^1(C,K)).
\tag{P4}
\]

If the local-system convention uses the dual representation, use tau^vee on both sides; none of the dimension bounds changes. All maps in (P4) are induced by the fixed finite-group action, hence commute with the Hodge decomposition and with Gauss–Manin transport. The representation factor has Hodge type (0,0). This is a Hodge-compatible finite-cover Shapiro/Frobenius isomorphism, not merely an equality of dimensions.

The right hand side is parabolic cohomology on Y of the finite tau local system:

\[
M_\sigma\cong H^1\bigl(Y,j_*\mathcal L_\tau\bigr),
\quad j:Y\setminus D_\tau\hookrightarrow Y.
\tag{P5}
\]

A sheaf-level explanation is useful. The finite map C->Y has no higher direct images of the constant sheaf. Taking H-isotypic summands of its direct image is exact in characteristic zero. At a branch point, the stalk is precisely the inertia-invariant part; this is the stalk of j_*L_tau. Thus the cohomological comparison extends across the branch points. Its Hodge compatibility follows from the same algebraic finite-cover action on differential forms/cohomology.

At a point where tau-inertia is trivial, the tau local system extends nonsingularly. Such a point is **not** a puncture of the data determining (P5). Extra ramification of Y->X, or ramification of C->Y invisible to tau, cannot be counted as an independent period parameter for M_sigma.

## 3. Why the period map forgets Y -> X

For a fixed smooth pointed curve (Y,D_tau) and fixed finite image tau(H), there are only finitely many homomorphisms of the finitely generated pi_1(Y\D_tau) into that finite group. After local marking, the chosen representation is fixed. Its flat bundle and the Hodge structure on its parabolic cohomology are determined by this intrinsic pointed curve plus this discrete representation.

Consequently the sigma period map factors locally through the moduli of (Y,D_tau) equipped with finite, hence discrete, monodromy data. The meromorphic map Y->P1 and additional ineffective branch markings may vary in positive-dimensional fibers of the forgetful map, but do not change this Hodge structure there. Finite level structures or a flat basis choice do not create extra tangent dimensions.

Thus

\[
\operatorname{rank}(\mathrm{Per}_\sigma)\le\dim\mathcal M_{\gamma,s}=3\gamma-3+s.
\tag{P6}
\]

**This factorization is the load-bearing geometric step for peer review.** A cohomological dimension equality without (P4)–(P6) would not justify the period-rank conclusion.

## 4. Effective-puncture budget upstairs

For an irreducible nontrivial rank-r local system of finite monodromy on Y, parabolic H^0 and H^2 vanish. Let a_y=rank(1-h_y)>=1 for each y in D_tau. Euler characteristic gives

\[
2n=2r(\gamma-1)+\sum_{y\in D_\tau}a_y.
\tag{P7}
\]

Therefore

\[
s\le\sum_ya_y=2n+2r(1-\gamma).
\tag{P8}
\]

Substitution into (P6) proves (P1), and gamma>=0 proves (P2) for r>=2.

An independent local accounting is available. For a branch matrix g_j permuting k blocks, with permutation pi_j, let h_{j,a} be the return monodromy along one cycle a. Then

\[
\operatorname{rank}(1-g_j)
=r\,\operatorname{ind}(\pi_j)+\sum_a\operatorname{rank}(1-h_{j,a}).
\tag{P9}
\]

Summing (P9) and applying Riemann–Hurwitz,

\[
\sum_j\operatorname{ind}(\pi_j)=2(k-1)+2\gamma,
\]

recovers (P7) from the downstairs formula sum rank(1-g_j)=2kr+2n. In particular, the ranks at ramified preimages are not being omitted; they are exactly the cycle-return defects in (P9).

## 5. Consequence for d=10

Claude's independently reviewed group-theoretic screen leaves only:

| Block type | Intermediate genus | Inducing rank | Effective punctures at most | Period rank at most |
|---|---:|---:|---:|---:|
| k=2, r=5 | 0 | 5 | 18 | **15** |
| k=5, r=2 | 0 | 2 | 12 | **9** |

Hence, **if the stated Hodge-Shapiro factorization is accepted**, neither residual type can have period rank 16. The suggested G33 rank-5 block does not evade the bound: its finite group size and character field cannot enlarge the moduli dimension of a rational curve with at most 18 effective punctures.

Thus the proposed synthesis is:

- d=7,8,9,11 excluded by the already cross-reviewed normal-reflection-subgroup lemma;
- d=10 additionally excluded by (P1)–(P8);
- d=6 remains governed by the previously checked conditional split-discriminant result;
- no non-split dominant construction of the specified kind is available in coefficient dimensions <=11 under those combined hypotheses.

The last combined conclusion is **PROPOSED**, not adopted. In particular, this does not establish that d=12 is feasible. The genus-zero-imprimitive residual class in a general theorem is not itself an existence result at r=5 or r=2.

## 6. Relation to the monomial exclusion

For r=1 and a nontrivial finite character, (P7) still gives s=2n+2-2gamma. Now the right hand side of (P1) is 2n-1+gamma, not a decreasing function. Since s>=0 implies gamma<=n+1, one obtains

\[
\operatorname{rank}(\mathrm{Per})\le3n.
\]

This recovers the familiar n>=4 monomial obstruction, rather than assuming that the r>=2 formula can be extrapolated with its monotonicity unchanged. The trivial character case is excluded: inducing the trivial character gives a permutation representation containing a trivial summand, contrary to an absolutely irreducible sigma of dimension >1.

## 7. Scope and outstanding review

- The input is a **fixed finite monodromy** representation and its cohomological weight-one variation. Continuous character varieties are not being ignored; they are outside these hypotheses.
- The statement is independent of (L) and of whether the discriminant is split. It is an obstruction to (D), not a construction of algebraic cycles.
- No polarization class is transferred between unrelated families here. The fixed K-action and finite-cover isomorphism transport the same Hodge filtration; possible fixed scaling of the pairing does not change the period rank.
- The new proof does not assume Severn's all-members or compensation results.
- The exact arithmetic program checks (P9) on finite sample matrices and the numerical bounds; it does not establish (P4)–(P6) by computation.
- No original Severn §8 PDF could be reopened in this session. The comparison to that source's genus-zero-imprimitive wording remains source-limited. No claim of publication novelty is made.

**Suggested next peer check:** independently inspect (P4)–(P6), especially forgetting ramification points with trivial tau-monodromy. If that step passes, d=10 should be eliminated before any G33-induced tuple search is started.
