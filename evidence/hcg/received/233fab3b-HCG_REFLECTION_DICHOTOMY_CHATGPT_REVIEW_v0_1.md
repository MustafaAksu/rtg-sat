# HCG — Independent review of the inducing-data reduction, symmetric-type bound, and reflection dichotomy

**Date:** 2026-10-29  
**Reviewer:** ChatGPT  
**Status:** SESSION scientific cross-review; proposed dispositions, NOT PI adoption.  
**Scope:** The attached Claude report §§2–3, Lemmas E/F and Theorem R, for the genus-zero finite-cover eightfold problem. No novelty claim. No modification of adopted HCG v0.2 or any RTG owner source.

## 0. Verdict and assumptions

**Lemma E, Lemma F and Theorem R pass independent argument-level review, with the field-of-imprimitivity and dominance qualifications below.** In particular the conclusion

> a dominant nonsplit datum in the stipulated class has reflection-free image and coefficient dimension at least 15

is supported. Do not abbreviate this to “a group containing a reflection always gives split discriminant”: dominance and multiplicity dimension eight are essential.

Write (H) for the following fixed conditions:

- A family of connected finite Galois covers of X = P^1, with faithful finite coefficient image Gamma after quotienting the representation kernel.
- An absolutely irreducible K-representation sigma, K = Q(sqrt(-3)), of dimension d, with character field exactly K and no invariant vectors. Its invariant coefficient Hermitian form is positive definite.
- The multiplicity variation M_sigma has K-dimension 8 and signature (4,4).
- The period map has complex rank 16 at an interior point, hence N_eff >= 19. Only points with nonidentity coefficient monodromy are counted.
- Parabolic cohomology and its Hodge/polarization realization are those of the finite-cover construction, not an arbitrary Hodge filtration imposed on an abstract representation.

The supplier condition (L) is NOT used in the new obstruction argument and is NOT asserted to pass to an inducing representation. Identifying the cup discriminant with the actual Jacobian-induced abelian-factor polarization retains the existing finite-cover comparison dependency.

## 1. Actual source identity, reading and replay

Read the entire delivered report `H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md`, SHA-256
`050c8504edfc73af13d935c8d27925d71fd0ed846395a4bb51cb94976768ec7f`, and its test program/output. The identical report is inside the supplied ZIP.

The ZIP SHA-256 is `d332c5cf22937206ad38b0316337c3741a96e2bbdf70befc93ea5dad9ec4de96`. Its manifest has **5 entries, all verified**; the manifest itself is not counted as a sixth hashed entry.

The source test imports an engine not included in this ZIP. Recovered the unchanged `generic_engine.py` from the available original `H3_P2P3_CHECK_v0_1.zip`, and verified its SHA-256:
`66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505`.
The producer script was read and run after changing only its hard-coded import path. All **60 cases** pass; the entire stdout is **byte-identical** to the supplied log. This is source replay, not a third geometric proof.

Independent code, with no import from the producer engine, checked:

- 27 block-cycle local determinant identities over Q(w); all norm classes agree. Omitting det(H)^(ell-1) is detected in 18 cases.
- 9,266 permutation cycle partitions, checking the exact scalar-eigenvalue multiplicity bounds in dimensions 6–24.
- Scalar budget inequalities in dimensions 6–10,000 and all six nontrivial product-one mu6 triples. These support, but do not prove, the new stronger type-A bound in the separate research note.
- A field-of-block-definition example distinguishing K-primitivity from complex primitivity.
- Ten semisimple rank-two characteristic-polynomial possibilities over K and absence of rank-one nontrivial powers. This is a finite spectral screen, not a classification of groups.

The previous 85-second package and the older G34/locality campaigns were not rerun. They are unchanged dependencies rather than new work in this review.

## 2. Lemma E — Hodge reduction and discriminant preservation

### 2.1 Factorization and the genus bound

Let sigma = Ind_H^Gamma tau, with a **K-defined** inducing block of rank r >= 2. Put Y = C/H, gamma = genus(Y), N_tau = ker(tau), and Y_tau = C/N_tau. The quotient Y_tau -> Y has faithful finite deck group H/N_tau. Its branch divisor is precisely D_tau, the points of nontrivial tau-inertia; branch points invisible to tau disappear in this quotient.

Frobenius reciprocity and characteristic-zero descent give

Hom_Gamma(sigma,H^1(C,K))
  ~= Hom_H(tau,H^1(C,K))
  ~= Hom_{H/N_tau}(tau,H^1(Y_tau,K)).

These are induced by group action and finite pullback/trace, and commute with Hodge decomposition and Gauss–Manin transport. The Hodge variation depends on the intrinsic pointed curve (Y,D_tau) and discrete finite monodromy, not on the meromorphic map Y -> P^1. This proves the local period factorization through a finite-cover moduli problem over M_{gamma,s}.

Consequently

rank(d Per_sigma) <= 3 gamma - 3 + s,
8 = (2 gamma - 2)r + sum_y rank(1-tau(h_y)),
s <= 8 + 2r(1-gamma),

and therefore

rank(d Per_sigma) <= 2r+5+(3-2r)gamma.

For gamma >= 1 and r >= 2 this is at most 8. Rank 16 forces gamma = 0 and r >= 6. The gamma=0 case is stable: a nontrivial finite local system on P^1 with <=2 effective punctures cannot have the positive parabolic dimension eight here. The potentially unstable cases do not require assigning a negative moduli dimension.

For rank-one induction the same finite-cover factorization gives rank <= 12 when the target multiplicity has dimension 8. Thus the earlier monomial exclusion no longer requires Severn's unrefereed monomial result as a separate dependency; it still relies on the classical finite-cover/Hodge constructions.

### 2.2 The inducing datum inherits the required conditions

Absolute irreducibility of sigma implies absolute irreducibility of tau. If the character of tau were rational-valued, its induced character would be rational-valued, contradicting Q(chi_sigma)=K. Since the block is K-defined, Q(chi_tau)=K.

The connected cover Y_tau -> Y makes the induced local monodromies generate tau(H), with their product equal to one when Y=P^1. Replace H by tau(H) to obtain a faithful image. The Hodge and cup identifications preserve dimension and signature. Because the original rank-16 period map factors through this inducing family, the ambient inducing family also has rank 16 somewhere; it need not be dominated by the original family for this implication.

No automatic assertion about supplier lattices or (L) is made.

### 2.3 Discriminant preservation

Choose an induced invariant coefficient metric with the translates of the inducing block orthogonal and h_sigma restricted to the first block equal to h_tau. On H^1(C), restriction of equivariant maps to that block identifies the two multiplicity pairings. Pullback H^1(Y_tau)->H^1(C) multiplies the cup form by the positive integer degree |N_tau|. Different conventional normalizations of finite-cover trace may introduce another positive rational degree factor; all are harmless for the claim actually needed:

h_{M_sigma} ~= q h_{M_tau}, or its uniform conjugate, with q in Q^×.

Since dim_K M = 8, q^8 = N_{K/Q}(q^4), and conjugation fixes a Hermitian determinant. Therefore

[disc M_sigma] = [disc M_tau].

This is the general proof, not an inference from 60 tested cases.

### 2.4 Independent derivation of the local identity

For a cyclic block operator g on W^ell with return operator P, decompose W orthogonally as F=Fix(P) and U=im(1-P), f=dim F. On F^ell, the moving subspace is the sum-zero space. In a difference basis its Gram determinant is ell^f det(h_F)^(ell-1), and det(1-g) on it is ell^f. On U^ell the moving space is all of U^ell, with Gram determinant det(h_U)^ell and det(1-g)=det(1-P|U).

Thus, modulo basis-change norms,

[a(g)b(g)] = [a(P)b(P) det(h_W)^(ell-1)],

because ell^(2f) is a norm. Multiplication over branch points introduces [det h_tau]^(sum ind pi_j); Riemann–Hurwitz makes this exponent 2(k-1)+2gamma even. This independently proves the exact local identity checked by the 60 producer and 27 reviewer computations.

**Disposition: Lemma E CHECKED, explicitly for K-defined induction.**

## 3. Lemma F — symmetric-type complement

For Gamma containing the standard reflection group S_{d+1} in its K-model and lying in its scalar normalizer, write g = mu p. The scalar decomposition is unique for d>=2. Since Gamma contains the symmetric group and has K-matrices, its finite scalar subgroup lies in mu6, with nonreal scalars present by the exact-character-field condition. The same argument applies to the stated standard A_{d+1} extensions when the indicated scalar-character decomposition is actually supplied; mere abstract projective isomorphism is not a substitute for that representation identification.

Let t count branch monodromies with nonidentity scalar mu. The nontrivial rank-one character chi has parabolic dimension t-2. Since std tensor chi plus chi is the twisted permutation representation induced from the point stabilizer,

M_sigma (+) M_chi ~= H^1_par(Y,L_chi'),

dim H^1_par(Y,L_chi') = 6+t = 2gamma-2+s'.

The sigma factor is a canonical Hodge summand, so its period map also factors through the pointed curve and rank-one local-system moduli. Hence

rank(d Per_sigma) <= gamma+5+t <= 9+3t/2.

At least two scalar entries are nonreal. Their respective rank-excess cost is at least
A_d = d-floor((d+1)/3)-1;
any other nonidentity scalar has cost at least
B_d = d-floor((d+1)/2)-1.

For t>=5,
2 A_d+3 B_d >= (17d-43)/6 > 2d-11.
Thus t<=4, and rank <=15 as asserted.

**Disposition: Lemma F CHECKED in its stated standard/scalar representation scope.** The review also proves a stronger t=2 / rank<=12 statement using the product-one scalar constraint; it is kept as a separate PROPOSED extension, not silently substituted into the reviewed lemma.

## 4. Theorem R — all-dimensional reflection dichotomy

Let W_R be the subgroup generated by every complex reflection in Gamma. It is normal. Its moving root lines are K-defined. The connected components of their nonorthogonality graph span K-defined mutually orthogonal irreducible W_R-blocks. The common W_R-fixed space is Gamma-stable and zero by absolute irreducibility, so these blocks exhaust V. Gamma permutes them transitively, with equal dimension r.

- r=1: the representation is complex monomial. The rank-one induced-period bound excludes dominance, independently of the field of the monomial basis.
- At least two blocks, r>=2: Lemma E gives a genus-zero rank-r datum, same discriminant, rank-16 period map, and r>=6. Its reflection subgroup contains the irreducible factor W_1, and is therefore irreducible on that block. This reduction is genuinely K-defined; the field warning in §5 does not obstruct it.
- Irreducible reflection subgroup, rank at least six: the Shephard–Todd list leaves monomial G(m,p,r), symmetric type A_r, E6/E7/E8, and G34. No other exceptional ranks >=6 occur.
- The monomial normalizers for rank >=5 remain monomial, so the rank-one bound applies.
- Type A is excluded by Lemma F.
- For E6/E7/E8 the real-Weyl normalizer is scalar times the Weyl group. At least two nonreal scalar entries imply epsilon>=4,6,6, exceeding budgets 1,3,5.
- For G34 the linear normalizer acts by inner automorphisms modulo scalars. Any extra finite scalar in a K-model is in mu6, already in G34. The image is thus G34. Its rank-six budget allows 20 reflections or 18 reflections plus one rank-two element; the already peer-checked local determinant formula and rank-two classification give split class [1] in both cases.

**Therefore, under (H),**

Gamma contains a reflection AND rank(d Per)=16 ==> [disc M_sigma]=[1].

Equivalently a nonsplit dominant datum has reflection-free coefficient image. This does not assert that an arbitrary reflection-containing local system is split without dominance. The previously checked cyclic nonsplit separator has no dominance and is not a counterexample.

Since each effective c_j is now at least two,

38 <= 2N_eff <= sum c_j = 2d+8,

which proves d>=15. Hence the proposed exclusion of d<=14 is valid, with the same fixed hypotheses and classical classification inputs.

**Disposition: Theorem R and the d<=14 corollary CHECKED as conditional mathematical implications; PI adoption remains separate.** The split conclusion for the actual abelian factor retains the recorded polarization comparison, not just the matrix-class computation.

## 5. Required scope qualification: primitive over which field?

Lemma E permits descent through a K-defined imprimitivity system. Iterating gives a representative minimal for such K-defined induction. It does NOT by itself show that every original datum is primitive, or that the terminal representation is primitive over C.

This distinction is genuine. The deleted permutation representation of AGL(1,7), twisted by an independent cubic scalar, has character field K and is absolutely irreducible of degree six. An order-seven translation has characteristic polynomial Phi_7, irreducible over K. Any K-block system has fewer than seven blocks, so C7 fixes every block; irreducibility of Phi_7 then rules out a proper K-block. Over C, the six Fourier eigenlines of C7 form a monomial imprimitivity system. Thus K-primitivity and complex primitivity are not interchangeable, even for finite image with exact character field K. This example is excluded by the monomial period bound; it is a warning about field descent, not a candidate dominant nonsplit family.

For the NEXT Huffman step, formulate two branches: (i) genuinely complex-primitive candidates, (ii) complex-imprimitive but not K-induced candidates requiring a separate field-of-definition argument. The main reflection dichotomy does not need this extra argument because its normal-reflection blocks were already K-defined.

## 6. Literature access and what has NOT been proved

Inspected primary-source text from Marin–Michel (arXiv math/0701266v3), §3 and the relevant normalizer discussion; the Magma Handbook rank list; and DW06 §1.2, §2.3 for the parabolic/Hodge setting. These are targeted readings, not complete new proofs of the external classification.

Huffman's Caltech repository summary was readable; attempts to open/download the full thesis failed. The summary concerns primitive UNIMODULAR complex groups with exceptional eigenvalues (i,-i) or (omega,bar omega). The 1975 Huffman–Wales paper's bibliographic record was found, but its full theorem/proof was not accessible. Cohen's 1980 quaternionic-reflection paper was accessible as scanned pages; that is not a replacement for the general complex classification, and no broad exclusion is imported from it.

PDF screenshot requests for Marin–Michel and DW06 failed in this run; their parsed primary text was read, not a claimed successful visual review. A Cohen page was rendered, but it is not used as a load-bearing theorem here.

No exclusion of all dimensions 15–24, and no conclusion d>=25, is established by this review. The separate algebraic spectral note narrows which codimension-two types must be matched to the primary classification.

## 7. Proposed dispositions

| Item | Reviewer proposal | Limit |
|---|---|---|
| Induced-period bound and d=10 exclusion | CHECKED, two argument-level reviews | Finite-cover Hodge variation, effective punctures |
| Lemma E | CHECKED | K-defined inducing block; no automatic (L) transfer |
| Lemma F | CHECKED | Actual standard/scalar decomposition, not only an abstract quotient |
| Theorem R | CHECKED under (H) | Dominance, target multiplicity 8, exact K, absolute irreducibility |
| No dominant nonsplit datum at d<=14 | CHECKED under (H) | Cup-to-abelian polarization comparison recorded separately |
| Unqualified assertion that all remaining images are complex primitive | NOT ESTABLISHED by the submitted argument | Minimal K-induced model is justified; complex descent is additional |
| Stronger type-A rank<=12 and ten-type rank-two sieve | PROPOSED, new reviewer derivations | Written proofs and finite exact checks supplied; Claude review pending |
| Dimensions 15–24 | OPEN | Full classification hypotheses/source coverage pending |
| HCG v0.2 / Severn A/B/C / PI decision fields | Unchanged | No canonical edit or adoption |

## Primary references

- Marin–Michel, *Automorphisms of complex reflection groups*, arXiv:math/0701266v3, §3 and §4: https://arxiv.org/pdf/math/0701266
- Magma Handbook, *Construction of Finite Complex Reflection Groups*: https://magma.maths.usyd.edu.au/magma/handbook/text/1228
- Dettweiler–Wewers, *Variation of parabolic cohomology and Poincare duality*, Sem. Congres 13 (2006), 145–164: https://emis.de/ft/47210
- Huffman, *Eigenvalue Structure in Primitive Linear Groups* (1974), Caltech repository SUMMARY ONLY: https://thesis.caltech.edu/14100/ ; DOI 10.7907/1hnq-y922.
- Huffman–Wales, *Linear groups of degree n containing an element with exactly n-2 equal eigenvalues*, Linear Multilinear Algebra 3 (1975), 53–59; DOI 10.1080/03081087508817092. Full text not read.
