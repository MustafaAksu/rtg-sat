# Complex Geometry and Hodge Realization — Standalone Research Charter v0.1

**Date:** 21 October 2026  
**Status:** WORKING / NONCANONICAL / NOT RTG-ADOPTED  
**Research setting:** Independent session outside the RTG project. The programme consumes selected mathematical RTG findings, but is not an RTG stream and must not change any RTG owner DSN.  
**Purpose:** Test whether a mathematically precise RTG-inspired selection of a complex structure, lattice, polarization, or Weil-type signature leads to useful geometric constructions. The Hodge conjecture must not be represented as solved by these constructions.

## 0. Working contract

- **Evidence labels:** `[RTG-OWNER: owner/version/section/RID]`, `[CLASSICAL: theorem/reference]`, `[SESSION-ALG: derived/checked here]`, `[HYP: unproved]`, `[OPEN: specific closure criterion]`. An RTG owner result remains conditional on its chosen continuous model. Do not upgrade a SESSION result to owner status.
- **Scientific firewall:** Mathematics derived from RTG data is permitted as mathematical input; no claim that an integer lattice, abelian variety, Hodge class, or physical orientation is an RTG physical object without an additional selection or bridge theorem.
- **Outbound rule:** Results offered back to RTG require a dated noncanonical handoff note with explicit provenance and a receiving owner/PI decision. No direct DSN edits, no implied adoption, and no reciprocal scientific import.
- **Independent literature:** Read current primary proofs, not only secondary summaries. Reassess the frontier before opening a theorem claim; a proof of an already-known case is a verification, not a breakthrough.

## 1. RTG import ledger (one-way)

| Item | Imported object / fact | Authority / grade | Scope and limitation |
|---|---|---|---|
| R1 | Primitive linearization `A = [[1,-1],[1,0]]`, `A^3=-I`, `A^6=I` | `[RTG-OWNER: DYAD v6.4.18 §§6.1–6.3; GENESIS v2.8.9 §1]` | Selected continuous dyad model; not a primitive physical lattice |
| R2 | Invariant positive quadratic form `B = [[1,-1/2],[-1/2,1]]`; `A^T B A=B` | `[RTG-OWNER: DYAD v6.4.18 §6.3 / DYAD-ALG-Q-INVARIANT-FORM]` | Scale fixed by adopted convention |
| R3 | `J_Q=(2A-I)/sqrt(3)` and `J_Q^2=-I` | `[RTG-OWNER: GENESIS v2.8.9 §6.6, compatible with DYAD §§6.1–6.3]` | The **B-quarter-turn**, not a Euclidean 90-degree turn in raw `(x,y)` coordinates |
| R4 | Six-step return coefficient `mu=-1/2-2i sqrt(3)/3`; nonzero degree-five coefficient `a_05=-49/8640 - 307i sqrt(3)/25920` in the specifically fixed normal-form chart | `[RTG-OWNER: DYAD v6.4.18 §§6.7,6.14 / DYAD-THM-C21; DYAD-ALG-NF6]` | The normal-form chart matters; do not transplant coefficients into raw coordinates |
| R5 | Smooth local flow embedding for `T^6` and its smooth order-six generator | `[RTG-OWNER: DYAD v6.4.18 §6.17 / DYAD-THM-SMOOTH-EMBEDDING]` | Local smooth-germ existence, not holomorphic or physical selection |
| R6 | Local non-reversibility under an orientation-reversing `C^3` involution from `Re(mu) != 0` | `[SESSION-ALG: dyadic cubic-return comparison]` | Independent mathematical deduction; not owner-adopted here |
| R7 | Candidate nontrivial full formal centralizer with linear parts restricted to `mu_6`, based on the nonzero `a_05` slot | `[SESSION-ALG: FMS v0.6.4, NONCANONICAL]` | Needs independent review. Do **not** confuse with `Cent_GL2(R)(A)=R[A]^× ≅ C^×` |
| R8 | Programme boundary: no cross-branch or physical status from mere notation/representation | `[RTG-OWNER: Programme v1.2 SG-PROG-1; OFN v0.10]` | Governs all interpretation, not a Hodge proof |

**Availability/version receipt:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_19.md` is available and declares PI adoption 20 Oct 2026; SHA-256 `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`. Its new theorem concerns an L-PHASE remainder; the mathematics imported in R1–R5 is unchanged from the explicitly audited v6.4.18 scientific sections. Supporting available sources: Genesis v2.8.9 and OFN v0.10. This charter is not a new review or replay of their computational certificates.

**Crucial NON-import:** `Lambda = Z[ζ6]` is a **classically chosen lattice**, motivated by the integral matrix `A`, not an RTG owner claim that the dyad physically selects integer lattice points. Its projective algebraic realization is this session's classical mathematical construction.

## 2. H1 — The Eisenstein elliptic realization

Take

\[
A=\begin{pmatrix}1&-1\\1&0\end{pmatrix},\qquad
B=\begin{pmatrix}1&-\tfrac12\\-\tfrac12&1\end{pmatrix},\qquad
J_Q=\frac{2A-I}{\sqrt3}.
\]

In complex coordinate `z=x+ζ3 y`, with `ζ3=exp(2πi/3)`, multiplication by `ζ6=exp(iπ/3)` represents `A`; multiplication by `i` represents `J_Q`. The integral lattice `Λ=Z+Zζ3=Z[ζ6]` is `A`-stable. Define

\[
E=\mathbb C/\Lambda,\qquad \operatorname{End}(E)\cong\mathbb Z[\zeta_6],\qquad j(E)=0.
\]

The compatible symplectic form, with declared sign convention `ω_B(v,w)=B(J_Qv,w)`, is

\[
\omega_B=\frac{\sqrt3}{2}\,dx\wedge dy,\qquad
\omega_0=\frac2{\sqrt3}\omega_B=dx\wedge dy,
\quad\int_E\omega_0=1.
\]

`[SESSION-ALG]` The resulting normalized polarization is integral and positive; standard elliptic-curve theory yields a smooth projective curve. **This is a representation constructed with a chosen integral lattice**, not a proof that the RTG physical dynamics selects it.

**H1 exit test:** Independent exact-arithmetic checks of `A^2-A+I=0`, `A^T B A=B`, `J_Q^2=-I`, lattice preservation, area normalization, and the algebraic model/CM endomorphisms. Explicit statement of each added choice.

## 3. H2 — Integral Néron–Severi basis and known Hodge rings

Let `X=E×E`. Let `D1={O}×E`, `D2=E×{O}`, `D3=Δ`, and `D4=Γ_A` (the graph of the elliptic-curve automorphism represented by A). Their intersection matrix is

\[
M=\begin{pmatrix}
0&1&1&1\\ 1&0&1&1\\ 1&1&0&1\\ 1&1&1&0
\end{pmatrix},\qquad \det M=-3.
\]

Set `C3=D3-D1-D2`, `C4=D4-D1-D2`. These classes are orthogonal to the hyperbolic plane generated by `D1,D2`, with pairing

\[
\begin{pmatrix}-2&-1\\-1&-2\end{pmatrix}.
\]

For this CM elliptic curve the classical integral identification is

\[
\operatorname{NS}(E^2)\cong U\oplus A_2(-1),
\qquad\det\operatorname{NS}(E^2)=-3.
\]

**[CLASSICAL + SESSION-ALG]** Matching the full Néron–Severi discriminant with `det M` proves that `D1,...,D4` have index one and form a **Z-basis**. The graph classes are concretely associated with the integral operator basis `{1,A}` of the Eisenstein ring.

This proves a stronger integral *divisor-basis* result than the preceding rational rank check, but **does not establish the general integral Hodge conjecture**. It is an example already governed by classical algebraic geometry.

For `E^4`, compute the rational Hodge ring via `H^*(E^4,Q)=Λ^* H^1(E^4,Q)` and compare it to the ring generated by divisor classes. For this fixed power of a CM elliptic curve, the rational Hodge classes are classically divisor-generated. A useful expected dimension check for rational classes in codimensions `k=0,...,4` is `(1,16,36,16,1)`, to be established with an independent exact rank computation, not assumed from the complex Hodge numbers alone.

**H2 exit test:** Reproduce the integral NS basis and discriminant; separately compute the rational Hodge classes and divisor-product span on `E^4` with explicit bases, cycle maps, ranks and rational-vs-integral wording. Report all as **known-case verification**.

## 4. Dynamical incompatibility gate

`[RTG-OWNER: DYAD v6.4.18 §6.7 / DYAD-THM-C21]` In an adopted complex chart of the six-step return:

\[
F(z)=T^6(z)=z+\mu z^2\bar z+O(|z|^4),
\qquad \Re\mu=-\tfrac12.
\]

`[SESSION-ALG]` Consequently

\[
|F(z)|^2-|z|^2=2\Re\mu\,|z|^4+O(|z|^5)
=-|z|^4+O(|z|^5),
\]

so the origin is a locally attracting weak sink for `F` (and thus `T`). In particular `T^6` is not locally the identity and cannot be locally **topologically conjugate** to a finite-order map of order dividing six. Holomorphy is not needed for this finite-order exclusion.

This **does not** prove that `T` lacks every algebro-geometric realization on another space, or that no abstract complex structure exists on its smooth dynamical germs. Do not identify the exact order-six smooth generator of Dyadic §6.17 with `T` itself: that generator and the dissipative primitive map are distinct.

## 5. Current external mathematics and frontier

1. `[CLASSICAL: Moonen–Zarhin]` Hodge rings of abelian varieties of dimension at most five can be reduced to divisors and Weil-type classes.
2. `[LITERATURE: Markman 2025, published ICM 2026]` Weil classes on polarized **split** (discriminant coset `[-1]`) Weil-type abelian sixfolds are algebraic over any imaginary quadratic field. The result implies algebraicity for all abelian fourfolds of Weil type, all fields and discriminants, hence the Hodge conjecture for all abelian varieties of dimension `<=5`.
3. `[LITERATURE: Floccari–Fu 2026]` Confirms the Markman fourfold advancement and notes older results for `K=Q(sqrt(-3))` in fourfold dimension. The published sixfold result is for split Weil type: do not overstate it as all sixfolds.
4. The **general Hodge Conjecture is unsolved**. In the abelian branch a potential direction is non-split Weil-type sixfolds `K=Q(sqrt(-3))` with polarization discriminant class `δ≠[-1]` in `Q^×/N_{K/Q}(K^×)`, but the precise open subset must be rechecked against the latest literature at the time of any study. Alternative: a demonstrably distinct non-abelian algebraic variety with an independently formulated open cycle problem.

**Primary references (verify dates/version when research starts):**
- Eyal Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds* (2025), https://arxiv.org/abs/2502.03415 .
- Eyal Markman, *Secant Sheaves and Weil Classes on Abelian Varieties*, ICM 2026, https://doi.org/10.1137/25M1803796 .
- B. J. J. Moonen and Yu. G. Zarhin, *Hodge classes on abelian varieties of low dimension* (1999), https://arxiv.org/abs/math/9901113 .
- Salvatore Floccari and Lie Fu, *The Hodge conjecture for Weil fourfolds with discriminant 1 via singular OG6-varieties* (2026), https://doi.org/10.1016/j.matpur.2026.103876 .

## 6. H3 — A nontrivial Weil-type or non-abelian research target

Fix `K=Q(sqrt(-3))` *as a choice motivated by R1–R3*. For a Weil-type abelian variety `Y` of complex dimension `2n`, require an algebraic `K` action with embeddings `σ` and `\bar σ` each occurring with multiplicity `n` on `H^{1,0}(Y)`. At dimension six this is the `(3,3)` signature. The two-dimensional rational space of candidate Weil classes is

\[
W_K(Y)=\bigwedge_K^{6} H^1(Y,\mathbb Q)
\subset H^{3,3}(Y)\cap H^6(Y,\mathbb Q).
\]

**`[HYP/INTERP]` only:** The pair of complex embeddings resembles the two orientations associated with `J_Q` and `-J_Q`, but it **does not mean** half of the dynamical factors physically run as `T` and half as `T^{-1}`. A signed `K`-action on a complex tangent space is not itself a physical reversal law. Nor does this interpretation supply the required polarization or any non-split sixfold.

**Non-frontier control:** `E^3×E^3` with opposite `K` embeddings on the two groups realizes the required balanced multiplicity but remains a highly special product of CM elliptic curves, with known algebraic Hodge classes. It is a control/example, **not** an open Hodge case.

**H3 entry gates:**
- Specify an actual algebraic family (period matrix/Riemann form, rational lattice, `K`-action, positivity and integrability), not just a real linear complex structure.
- Calculate the discriminant **coset**, show it is outside the covered split case when pursuing the non-split branch, and establish that the family is not merely an isogenous product already covered by classical theory.
- Separate `W_K(Y)` from divisor products through a rigorously computed Hodge group and cohomological decomposition.
- Identify a genuinely unresolved algebraicity question **before** proposing an RTG mechanism for cycles. Falsify novelty if known theorems already imply it.
- Only then formulate an explicit cycle construction or obstruction with computable tests.

## 7. Priority and deliverables

**First:** H1 + H2 as reproducible mathematical calibration (including the integral NS basis and a rational-versus-integral audit). **Second:** a carefully sourced frontier review on non-split Weil-type sixfolds over `Q(sqrt(-3))`, with the split and CM-product negative controls. **Third:** attempt H3 only after the open example and all required geometry are precisely specified.

Deliverables: (i) `SOURCE_MANIFEST.md` with exact owner and literature versions; (ii) `H1_H2_EXACT_CHECKS.py` or equivalent exact arithmetic; (iii) `HODGE_CLASS_AND_CYCLE_LEDGER.md` distinguishing classical inputs, checks, conjectures; (iv) optional `RTG_OUTBOUND_HANDOFF.md` containing only audited new mathematical results with their limitations. No owner DSN file may be edited by this session.

**First prompt in the independent session:**
> Work as an independent algebraic geometer, not an RTG advocate. Audit this charter's source ledger, verify the integral Néron–Severi basis by an independent construction, and reproduce the exact H2 classes and divisor spans. Then independently review the 2025–2026 Weil-type literature before selecting H3. Keep all classical, RTG-owner, derived-here, and conjectural results separate. Do not claim an open Hodge case without source validation and a concrete algebraic variety. Do not modify RTG documents.
