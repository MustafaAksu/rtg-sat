# G34-D / W5 — First-round blind independent geometric audit

**Date:** 22 October 2026  
**Report:** v0.1, first geometric assessment; no previous AI review reports consulted  
**Basis:** supplied v0.1 instructions and v0.2 source correction; unchanged W5 raw data; primary mathematical sources listed in `SOURCE_ACCESS_LEDGER.md`  
**Status:** independent review conclusions, not author adoption or certification of Severn's global theorem

## 0. Verdict and exact scope

**VERIFIED for the Hurwitz component determined by the supplied W5 tuple.** The 17 supplied logarithms admit simultaneous geometric realization, after a single marking and, when required, a finite positive-power base change. A single common convention sign suffices. The associated polarized weight-one variation has a Hodge–Tate limit with graded pieces of K-dimensions 4, 0, 4. Its period map has complex rank 16 at interior points and hence generically.

This conclusion includes the independent geometric argument below; it does not follow merely from a matrix PASS report.

**CONDITIONAL as an identification with the particular component selected in Severn's manuscript.** Call the W5 component `S_W5`. The supplied certificate is not Appendix A's certificate: the curve lists and return exponents differ. Neither supplied ZIP contains the original manuscript gate tuple or a braid identifying that tuple with W5. The manuscript's public data directory could not be retrieved in this review. Thus `S_W5 = S_manuscript`, or equality after forgetting branch labels, has **not** been verified. A different curve list alone does not prove different components. The missing object is an identification, not a counterexample to the local bridge.

**NOT VERIFIED:** the companion transfer theorem, the supplier-lattice/Brauer/Schoen/Milne/spreading arguments, compensation to sixfolds, and the global algebraicity conclusions. None is inferred from the present dominance result.

### What VERIFIED means here

It means that the stated finite calculation was independently executed or that the mathematical implication has the written justification below using the stated classical results. It does not mean a machine has formalized the geometry, that the original sources' deep theorems were reproved, or that every sentence of either Severn manuscript has been checked.

## 1. Input integrity and blindness

The v0.1 instructions incorrectly identify Hexagon numbers as arXiv IDs. The original instructions are preserved unchanged. The v0.2 correction replaces those references by the author-hosted manuscripts:

- Ben Severn, *Weil Classes on Every Abelian Sixfold of Weil Type for Q(sqrt(-3))*, Draft v0.5, 16 October 2026, 17 pages.
- Ben Severn, *A Transfer Theorem for Weil Classes on Prym–Tyurin Factors of Galois Covers*, Draft v0.15, 16 October 2026, 31 pages.

Title pages were checked in the actual PDFs. This verifies identity, not truth. Both remain unrefereed drafts. The bibliographic correction is retained as an audit event, not converted into a mathematical objection.

The mathematical files in the two ZIPs are byte-identical:

| File | SHA-256 |
|---|---|
| `g34_cert_tuple5_balanced.json` | `172766a91017aeac62e5c299a72b2c7582b0bb186c4feaa8b1906144eafb952e` |
| `roots_alt_5.json` | `480cd6dc95f1a802943a621df632693eeb9aa7e8a9057ff5099e444950c9e35a` |

No prior AI reports or their scripts were supplied or opened. Author-reported checks mentioned inside the manuscript were not counted as evidence. The scripts in this package were newly written and executed in this review. Earlier conversation messages reported calculations, but their executable files were not present in the current sandbox; this package preserves fresh reconstruction, not an invented recovery of those earlier scripts.

## 2. Numbered obligation dispositions

| No. | Obligation | Disposition | Scope / justification |
|---|---|---|---|
| 1 | Reflections, group and irreducibility | **VERIFIED** | Exact unitary involutions, product one, spanning connected root system, faithful finite orbit of size 756, generated group order 39,191,040. Character field exactly K; Schur index one over K. A fresh comparison with the original Shephard–Todd classification is not claimed or needed for the local construction. |
| 2 | Parabolic quotient and cup product | **VERIFIED** | K-dimension 8; proposed representatives form a genuine quotient basis. Cup recomputed, with a separate DW Theorem 2.6 implementation and an explicitly recorded single global convention sign. |
| 3 | Twist operators, logarithms and H0–H4 | **VERIFIED** | All 17 T and N reproduce; all exact return exponents are 1. H0–H4 hold; complex rank is independently checked, not inferred from arbitrary rational matrices. |
| 4 | Braid/Gauss–Manin and coefficient transport | **VERIFIED for S_W5** | DW transport term retained; finite G-torsor plus exact tuple return makes it finite central. Pointed family removes it; a common sixth-power cover also removes scalar characters. |
| 5 | Simultaneous boundary in the correct component | **CONDITIONAL** | The explicit marked degeneration is verified in the closure of S_W5. Its identification with a separately specified manuscript component is NOT VERIFIED. No assertion of component inequality is made. |
| 6 | Infinity and complementary curves | **VERIFIED** | Choose infinity as an unramified section; alternatively use complementary curves and the coboundary calculation. `[19,20]` and `[1,18]` induce equal operators on H1par, not inverses. |
| 7 | Common plumbing orientation | **VERIFIED** | One explicit annulus trivialization gives the same twist direction at all nodes. Base change multiplies winding positively. No curvewise sign choices. |
| 8 | Nilpotent orbit, limiting Hodge structure and interior rank | **VERIFIED for S_W5** | Uses the realized polarized VHS, Schmid (4.12), and Schmid (6.16) on a diagonal arc. Exact 16-minor and holomorphic untwisting give interior rank. Direct inspection of CKS 1986 is separately NOT VERIFIED. |
| 9 | Descent from finite covers | **VERIFIED** | Diagonal covers are étale on the punctured chart; derivative is invertible there. Generic rank descends on the same component. This is not a passage between unrelated components. |
| 10 | Secondary global transfer/algebraicity chain | **NOT VERIFIED** | Not audited in this report. No global algebraicity or Hodge-conjecture conclusion. |

Local wording/convention defects are recorded in §10, including the 17-to-16 “isomorphism” statement. They do not provide a counterexample to the corrected rank argument.

## 3. Independent finite reconstruction

[ALG — exact computation]
Let `K=Q(w)`, `w^2+w+1=0`, with `[p,q]=p+qw`. The ambient Hermitian form is linear in the first variable. Each supplied root has norm 6. Rebuilding

\[
s_v=1-\frac{2v\bar v^t}{h(v,v)}
\]

gives ten unitary involutive reflections. The roots span K^6; their nonorthogonality graph is connected. If a complex invariant subspace U were proper, U-perp would also be invariant. For each reflection its one-dimensional nontrivial eigenspace must lie in one of those two summands. Connected nonorthogonality forces all roots into the same summand; spanning then gives irreducibility. This proves absolute irreducibility, not just a rank test over K.

A separate Eisenstein-integer calculation closes the orbit of the first root at 756 vectors. All input roots belong to that orbit, and they span. Consequently the action on the orbit is faithful, so finiteness is proved without assuming the group name. The permutation-group order is 39,191,040. An independent word has

\[
\operatorname{tr}(s_1s_2s_3)=2-w\notin\mathbb Q.
\]

Since every matrix entry lies in K, the character field is exactly K. An absolutely irreducible realization over that field has Schur index one over K.

For the paired tuple, the closure map has rank 6 and the coboundary map rank 6. Thus `20-6-6=8`. The supplied eight representatives are checked to be closed, independent modulo all coboundaries, and a complement inside the cocycle kernel. No quotient basis is accepted merely because it appears in JSON.

For every interval, the cocycle action is reconstructed before passing to the quotient. If `c=g_a...g_b` and `rho(c)=1`,

\[
u(cg_ic^{-1})=u(g_i)+(1-\rho(g_i))u(c)
\]

for the enclosed generators. This produces every supplied T_j and N_j. All 17 boundary products are identity, so `k_j=1`, and `N_j=T_j-1=log T_j` because `N_j^2=0`.

The exact reconstructed facts are

\[
N_jN_k=0\quad(289\text{ pairs}),\qquad
I=\sum_j\operatorname{im}N_j,\quad\dim_K I=4,\quad S|_{I\times I}=0,
\]
\[
N_jI=0,\qquad \operatorname{rank}_{\mathbb Q}\langle N_j\rangle=16,
\qquad \operatorname{rank}_{K}\langle N_j\rangle=16.
\]

With the supplied column-coordinate convention and linear-first form,

\[
S(x,y)=x^tS\bar y,\quad
\operatorname{Gram}\bigl(S(x,N_jy)\bigr)=S\bar N_j.
\]

This conjugation is essential. `S*N_j` is not Hermitian for 16 of the 17 supplied operators. The correct quotient forms have inertia `(0,rank N_j,4-rank N_j)`; their sum has inertia `(0,4,0)`. No floating eigenvalue test is used.

In the supplied basis, `I=span(e_1,...,e_4)` and the N_j have upper-right 4-by-4 blocks B_j. Flattening B_1,...,B_16 as columns gives

\[
\det\bigl[\mathrm{vec}(B_1)\ \cdots\ \mathrm{vec}(B_{16})\bigr]
=6144(1+w)\ne0.
\]

The only direction relation is

\[
\boxed{N_{17}=N_9+N_{10}.}
\]

All outputs, the tree, the quotient-form sum and the finite orbit/permutations are preserved in `outputs/`.

### Cup-product convention audit

The left-cocycle expression in the certificate is independently evaluated, giving its exact S. A second implementation follows DW2006 Theorem 2.6. The left-to-right conversion is

\[
\delta(g)=u(g)^t\rho(g^{-1})^t,
\quad\delta(gh)=\delta(g)\rho(h^{-1})^t+\delta(h).
\]

For reflections and parabolic cocycles, `delta(g_i)=-u(g_i)^t`. DW's dual-first pairing must then be converted to a linear-first sesquilinear form, including the order of degree-one factors and the chosen surface/generator orientation. The separately implemented right-action/dual-first convention gives `-S`; the declared left-cocycle convention gives `S`. The global sign is stored in the results, rather than hidden by a curvewise adjustment. The meaningful verification is the geometric cup form up to that declared single global convention, not an assertion that every printed source convention literally yields the same array. H0–H4 and the rank argument are invariant under changing that overall sign.

## 4. A simultaneous W5 boundary construction

[THM — independent geometric argument using RW2006 §3 and §5; ACV2001 §§3–4]

### 4.1 The stable marked base

The W5 intervals are:

```
[1,2] [3,4] [5,6] [7,8] [9,10]
[11,12] [13,14] [15,16] [17,18] [19,20]
[1,4] [5,8] [9,12] [13,16] [1,8] [9,16] [1,16].
```

They form a laminar collection: any two are nested or disjoint. Pinch these disjoint simple curves on the marked twenty-punctured sphere. The resulting stable marked rational curve has 18 components and 17 nodes. Each component has three special points. The exact tree in `bridge_exact.json` checks this, including all twenty leaf labels.

There are ten terminal components containing the paired branch points and eight components with no original branch point. At a terminal component the monodromy triple is `(s_i,s_i,1)`; at an internal component it is `(1,1,1)`. Their local parabolic dimensions are respectively

\[
2-2\cdot6+2\cdot5=0,\qquad 0-2\cdot6+2\cdot6=0.
\]

This is the independently verified H0 calculation.

### 4.2 The cover, not just the base curve

Start with the connected marked topological G-cover specified by the W5 epimorphism. The finite group and generation are proved in §3. Riemann existence supplies the corresponding smooth complex algebraic cover; this is also the construction underlying RW2006 Theorem 3.1.

Cut that cover along the preimages of the 17 chosen curves. The boundary monodromy is identity at every cut, so each lifted annulus maps isomorphically to its downstairs annulus. Compactification of a terminal piece is the induced cover

\[
G\times_{\langle s_i\rangle}\mathbb P^1\longrightarrow\mathbb P^1,
\]

whose connected degree-two pieces have two branch points and genus zero. Above an internal component are |G| disjoint copies of P^1. Glue the unramified node fibres by the sheet identifications inherited from the original marked cover. This inherited gluing is part of the construction; arbitrary unrelated G-torsor gluings are not being asserted to land in the correct component.

The resulting nodal cover is connected, since the original generating tuple is retained. It is admissible: all node stabilizers are trivial and hence balanced. Smooth each node orbit equivariantly using the same parameter on every lifted node in that orbit:

\[
xy=q_j,\qquad x'=x,\quad y'=y.
\]

All 17 parameters are independent downstairs. The general tame deformation law is `q_j=t_j^{e_j}`; here `e_j=1` for all j. Thus no node-ramification base change is necessary for this W5 boundary. RW2006 Theorem 5.6 gives the corresponding formal deformation statement; ACV2001 Theorem 3.0.2 and Theorem 4.3.2 provide the smooth twisted-cover/admissible-cover framework. The explicit plumbing provides the analytic family used below.

Smoothing reverses the cut of the original marked cover. It therefore remains in S_W5, not merely somewhere in the same collection of conjugacy classes. This is the reason the constructed boundary lies in its closure.

### 4.3 Consistency checks and automorphisms

The upstairs normalization consists entirely of rational components. Its graph has `17|G|` edges and `8|G|+10|G|/2=13|G|` vertices, so, by connectedness,

\[
b_1=4|G|+1.
\]

Riemann–Hurwitz for a G-cover with twenty inertia-2 points gives the same genus. On the sigma multiplicity, the graph chain dimensions are `17*6=102` and `8*6+10*5=98`; the trivial representation contributes nothing to this nontrivial irreducible multiplicity. Thus its graph H1 has K-dimension 4.

Some source rational components are only semistable if ramification markings are forgotten. Nothing here assumes that the 17 parameters remain independent coordinates after contracting those components. Independence concerns the marked rational base and the admissible-cover chart, which are the relevant parameter spaces.

Choose one local unramified section in the exterior component, away from all collars and branch sections. The cover restricted to it extends as a finite étale G-torsor over the whole contractible polydisc, so it is constant and admits a sheet section. Use that sheet section as the pointing. A G-equivariant automorphism of the connected G-cover over its base is central; fixing that sheet section kills it. Ordered branch labels remove base automorphisms in the local marked chart. This provides an actual pointed family. Merely naming a rigidified coarse space would not by itself supply a universal cover; the explicit pointing avoids that shortcut.

## 5. Coefficient transport and the polarized variation

[THM — DW2004 Lemma 2.2 / Theorem 2.5, DW2006 Theorem 1.3, with independent finite-cover argument]

DW monodromy is the product of a braid action and a coefficient-transport action. It is not generally the braid term alone. For a loop beta in an actual G-cover family, the latter comes from an element h_beta of the finite G-torsor. Exact tuple return gives

\[
h_\beta g_i h_\beta^{-1}=g_i\quad\forall i.
\]

Generation forces `h_beta in Z(G)`. Absolute irreducibility makes its action on the coefficient representation scalar. **Its finiteness comes from finite G, not from Schur's lemma.** On the pointed family it is 1. On an unpointed realization it lies in `K` and has finite order, hence in `mu_6(K)`. This sixth-power bound requires no unverified computation of the entire centre.

Using one fixed identification of the fibre, all local operators therefore have the simultaneous form

\[
T_j^{\rm geom}=\zeta_jT_j^{\varepsilon},
\qquad \zeta_j^6=1,
\qquad\varepsilon\in\{+1,-1\}\ \text{independent of }j.
\]

There is at most one common basis conjugation, not seventeen independently chosen conjugations. The common sign includes the convention relating topological transport, cocycle pullback and the logarithms in the equivariant period map.

The cohomology of the smooth projective cover supplies a polarized integral weight-one VHS. Taking the relevant rational isotypic component and a primitive matrix factor produces a polarized rational VHS with underlying Q-dimension 16 and K-dimension 8. One concrete description is to take the rational central idempotent for the conjugate pair of representations and, inside that block, the idempotent `(1-s_1)/2`. It is rank one on the six-dimensional coefficient factor and self-adjoint for the invariant polarization. Clearing its denominator realizes its image as an abelian subvariety up to isogeny; no transfer theorem for algebraic cycles is used.

Equivalently, the multiplicity local system is the parabolic cohomology of the finite-monodromy coefficient system. A left-versus-right deck convention may name this factor by sigma or its dual; the convention is fixed once. The conjugate labels select the two K-embeddings of the same rational isogeny factor, not different signs for individual boundary loops.

The reflection eigenvalues are five 1s and one -1 at each puncture. The usual unitary parabolic Hodge calculation, as in the proof underlying DW2006 Theorem 2.3, gives `(10-6,10-6)=(4,4)`. Thus the relevant period domain has compact dual `Gr(4,8)` and complex dimension 16. The K-action is flat and of Hodge type (0,0). A stable integral lattice can be chosen in the rational summand by intersection with the integral cohomology lattice and clearing fixed denominators.

The cup pairing comes from the positive coefficient form and the oriented surface pairing. Comparison with the induced polarization is a fixed positive normalization and, depending on the recorded conventions, one global sign. The geometric argument never declares that a separately chosen sign for each beta_j is permissible.

## 6. Infinity and the uniform plumbing sign

### 6.1 An unramified infinity is available

Use a local affine framing with all twenty branch sections finite and the extra unramified section at infinity. The parameters still describe the same marked curves: the auxiliary section is chosen locally, not added as an independent varying branch parameter. DW2004 Definition 2.4 and §2.3 explicitly allow this case, as well as the distinct case in which infinity is a branch section and a tangential base point is used.

These two conventions must not be conflated. A literal fibre over a ramified branch point is not an unramified G-torsor. For the present construction no such identification is required: the auxiliary section is outside the ramification divisor and outside every twist collar.

### 6.2 Complementary curves

A Dehn twist about a simple unoriented curve on an oriented surface does not invert when the two sides of that curve are interchanged. There is also an exact cocycle check. Write `AB=1` for complementary boundary words. In W5 both boundary products are identity in the coefficient group, so

\[
u(B)=-u(A).
\]

For the A-side and B-side twist automorphisms, their cocycle changes differ, on every generator, by

\[
(1-\rho(g_i))u(A)=(\rho(g_i)-1)(-u(A)),
\]

a single coboundary. Therefore they induce the same operator on H1par. The script checks `[19,20]` against `[1,18]` exactly. It does not replace one operator by its inverse or ignore coefficient transport while moving a base point.

### 6.3 Plumbing

In the local model `xy=q`, let `q=r exp(i theta)`. Choose a radial cutoff chi on the annulus, 0 at the outer x-boundary and 1 at the outer y-boundary. A trivialization along the argument loop is

\[
x_\theta=e^{i\theta\chi}x_0,
\qquad y_\theta=e^{i\theta(1-\chi)}y_0.
\]

At `theta=2pi` both boundaries are fixed and the transition is one full twist. The same formula in every holomorphic node chart gives the same direction. Exchanging x and y changes both annular coordinates coherently and does not reverse the surface-oriented twist. Multiplication of q by a holomorphic unit preserves its positive local winding. Replacing q by `t^c` multiplies it by positive c. Inverting q is not a holomorphic local coordinate change at the node.

Comparison with the fixed Artin/cocycle convention can reverse all 17 twists together. It cannot produce independent signs. This is a geometric conclusion from the local models, not an inference from the observed common sign of the certificate.

## 7. Finite base change

[THM — independent covering argument]

In the pointed W5 chart, exact tuple return and trivial node inertia already give unipotent operators. On an unpointed realization, the simultaneous cover `q_j=t_j^6` kills all finite scalar factors. Further divisible powers may be used for a chosen family/level chart. The general form is

\[
M_j=\log T_j^{\rm geom,new}=\varepsilon c_jN_j,
\qquad c_j\in\mathbb Z_{>0}.
\]

If a finite local cover corresponds to a finite-index subgroup `Lambda < Z^17`, some `L Z^17` lies in Lambda. Taking diagonal positive powers therefore dominates a connected branch of that cover. There is no need to assume that every finite-index subgroup is already a product of coordinate subgroups.

Positive rescaling preserves the generated open positive cone, the common image, nilpotent products, semidefiniteness, definiteness of positive sums and span dimension. In particular the nonzero 16-minor is multiplied by a nonzero positive integer product (and by `epsilon^16`). An arbitrary signed or singular linear recombination of logarithms is not substituted for this argument.

On `(Delta*)^17`, the Jacobian of the power map is diagonal with entries `c_j t_j^(c_j-1)`, all nonzero. It is therefore étale there and preserves differential rank. A finite level cover of the target similarly changes no generic rank. The conclusion descends to S_W5, but this does not identify S_W5 with an unrelated Hurwitz component.

## 8. Nilpotent orbit and the limiting mixed Hodge structure

[THM — independent application of Schmid1973 (4.12) and (6.16)]

All prerequisites now have geometric content: a genuine polarized weight-one VHS, a normal-crossing punctured polydisc, an integral lattice up to fixed denominators, commuting unipotent monodromies, a horizontal period map and flat K-action. H0–H4 alone, for arbitrarily chosen matrices without this realization, would not license this step.

Write `t_j=exp(2pi i z_j)`. Schmid's several-variable nilpotent-orbit theorem supplies

\[
\widetilde\Phi(z)=\exp\!\left(\sum_jz_jM_j\right)\Psi(t),
\]

where Psi is holomorphic on the **full** polydisc with values in the compact dual. Put `F_infty=Psi(0)`.

Let `M=sum a_j M_j`, with `a_j>0`. Since all pairwise products vanish, `M^2=0`. The common-image conditions give `M(V) subset I` and `M(I)=0`. If x is nonzero modulo I, then

\[
S(x,\varepsilon Mx)=\sum_j a_jc_j\beta_j(x,x)\ne0.
\]

The last inequality follows from common semidefinite sign and definite sum; it is not a determinant assertion for a single N_j. Hence `V/I -> I` induced by M is injective and therefore bijective. Thus

\[
\operatorname{im}M=\ker M=I,
\qquad W_0=W_1=I,\quad W_2=V.
\]

This identifies the same weight filtration for every positive combination directly, without an unchecked appeal to a cone theorem.

For the mixed-Hodge assertion itself, restrict to the diagonal `t_1=...=t_17=t`. Its logarithm is `sum M_j`, and its untwisted limiting filtration is the same `Psi(0)`. Schmid (6.16) gives the limiting mixed Hodge structure. Because the original variation has `F^0=V_C` and `F^2=0`, the same filtration bounds hold on the graded pieces. Hodge symmetry forces `Gr^W_0` to have only type (0,0) and `Gr^W_2` only type (1,1); `Gr^W_1=0`. This proves Hodge–Tate type. It does **not** assert that the extension splits over Q.

Consequently, at either K-embedding iota,

\[
V_\iota=I_\iota\oplus F^1_{\infty,\iota},
\qquad \dim_\mathbb C I_\iota=\dim_\mathbb C F^1_{\infty,\iota}=4.
\]

The normalizations of all components are rational, so §4 supplies an independent geometric explanation for the absence of a weight-one graded piece.

### CKS source limitation

The original 1986 Cattani–Kaplan–Schmid paper could not be retrieved beyond its journal metadata. Its exact numbered statements are therefore **not source-verified here**. The later original-author exposition by Cattani–Kaplan (1989), Theorems (2.1) and (2.3), was read and agrees with the required framework. More importantly, the present proof uses the directly inspected original Schmid results and a diagonal restriction; it does not use the inaccessible CKS theorem numbering as a hidden premise. This is a documented bibliographic limitation, not a counterexample to CKS or to the present implication.

## 9. From the boundary to an interior rank-16 point

[THM — independent tangent and analytic argument]

Set `F=F^1_{infty,iota}`. Every complex linear combination of the M_j kills I and maps V into I. The exact nonzero K-minor in §3 remains nonzero under either embedding and under positive rescaling. Thus these maps span

\[
\operatorname{Hom}_{\mathbb C}(V_\iota/I_\iota,I_\iota),
\]

which has dimension 16. Since `V_iota=I_iota directsum F`, restriction and projection identify this space with

\[
\operatorname{Hom}_{\mathbb C}(F,V_\iota/F)
=T_F\operatorname{Gr}(4,8).
\]

The infinitesimal nilpotent-orbit map is therefore surjective. The parameter map from C^17 has a one-dimensional kernel. It is an isomorphism only after quotienting by that kernel, or after restricting to the independent first sixteen directions. Rational rank alone would not justify complex rank for arbitrary matrices; here the exact K-minor independently settles it.

For the actual period map, translate its derivative by the differential of `exp(-sum z_j M_j)` at the point. Its j-th logarithmic-coordinate column becomes

\[
M_j\cdot\Psi(t)+2\pi i\,t_j\frac{\partial\Psi}{\partial t_j}(t).
\]

Because Psi is holomorphic on a neighbourhood of zero, these columns tend to `M_j dot F_infty`. In a fixed Grassmannian coordinate chart near F_infty, one 16-by-16 minor has nonzero limit. Continuity makes it nonzero for sufficiently small t with every coordinate nonzero. Translating by an invertible group action does not alter rank; nor does changing logarithmic coordinates to punctured-disc coordinates. Hence the original geometric period map has rank 16 at interior points.

The relative Jacobian and its fixed rational group-algebra factor define an algebraic map to the corresponding polarized K-moduli space after the indicated level/isogeny choices. This proves a nonempty open rank-16 locus on S_W5. Its image contains an analytic open subset of the 16-dimensional period-domain quotient, so it is dominant on the corresponding target component. No numerical radius or explicit interior algebraic curve is claimed; neither is required for this existence/rank conclusion.

## 10. Defects, qualifications and unresolved identifications

### E01 — Manuscript witness versus supplied W5: GAP FOUND in identification

Appendix A of the main manuscript lists a different interval decomposition, including `[2,8]`, `[4,8]` and `[9,17]` with return exponent 2. W5 has no such curves and has all exponents 1. The supplied JSON has no 90-move braid or original gate tuple. Consequently it cannot be described as an exact replay of that appendix. To transfer the present result to its preselected component, supply an exact tuple/braid/common-conjugation identification, or explicitly use S_W5 as the dominance witness. This is an evidence/identification gap, not a refutation of either decomposition.

### E02 — Seventeen parameters versus a sixteen-dimensional tangent: GAP FOUND in literal wording; repaired here

Proposition 4.2 Step 4 calls the coefficient map an “isomorphism.” On C^17 it is not injective: W5 gives `N17-N9-N10=0`. The correct conclusion is surjectivity, or an isomorphism from the quotient by the kernel. That is sufficient for Step 5. If the intended domain was instead the already-quotiented Lie algebra, the isomorphism statement is correct; that domain must be stated. This is a dimensional clarification/correction, not evidence that rank 16 fails.

### E03 — Exact return versus return up to conjugacy: CONDITIONAL convention

On an inner, unpointed Hurwitz space, a loop can close when the tuple returns up to simultaneous conjugation, possibly before literal return. The manuscript's least-exact-return interpretation needs its pointed/framed convention. An exact return is nevertheless sufficient. For W5 the literal return exponent is already 1 everywhere, so no earlier positive return can occur and the distinction causes no failure here.

### E04 — Linear-first matrix typing: VERIFIED correction for the supplied coordinates

The form beta_j has Gram `S*conjugate(N_j)`, not `S*N_j`. A general discussion using `SX` must specify a compatible alternative matrix convention. The geometric pairing statement is sound when typed correctly. A naive numerical Hermitian-sign check on `S*N_j` would be invalid for this input.

### E05 — Direct original-source inspection: NOT VERIFIED at the unavailable sources

CKS1986, Harris–Mumford1982 and Knudsen1983 were not read in full text. Their precise original claims are not represented as checked. The proof here uses the specified Schmid original text, ACV original preprint, RW author treatment and explicit construction instead. ACV's accessed version is the 2001 preprint, which contains editorial placeholders; it is not silently called the final 2003 journal text. These access limits do not invalidate the arguments actually given, but they matter for a full source-by-source audit of the author's bibliography.

### E06 — No global theorem certification

A dominant W5 period map does not on its own establish the transfer theorem, algebraic cycles on every member, any sixfold compensation statement, or all-powers Hodge conjecture. Obligation 10 remains NOT VERIFIED.

## 11. Reproduction and evidence boundaries

Run `python scripts/run_audit.py` from this directory. The three independent exact scripts use Python and SymPy only. The driver reruns them, verifies input hashes and runs deliberately corrupted-certificate controls. `REPLAY.md` explains outputs and limitations.

The executable checks cover arithmetic, group finiteness/order, quotient and cup conventions, twists, nilpotents, signs, ranks, the labelled tree, complementary twists and the one-dimensional relation. The geometric proof, construction of the VHS, application of Schmid and analytic interior-rank inference are written mathematics, not assertions tested by the scripts.

The source ledger records exact URLs, editions and inspected statements. Browser-accessible PDFs were read through extracted text and page screenshots. They were not saved as local PDF bytes; no PDF hashes are invented and no copyrighted manuscripts are redistributed in this package.

**Final disposition:** the W5-to-dominance bridge on S_W5 survives this first independent geometric review. Identification with the manuscript's preselected component remains conditional on missing data. The global Severn theorem is not certified.
