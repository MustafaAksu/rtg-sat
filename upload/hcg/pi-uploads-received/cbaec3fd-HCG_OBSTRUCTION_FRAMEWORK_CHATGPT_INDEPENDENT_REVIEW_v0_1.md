# HCG — Independent review of the Hurwitz–Hodge obstruction framework, reciprocal discriminant, Euler gate, and `2 ⊗ b` certificates

**Date:** 2026-11-03  
**Status:** SESSION review; proposals are not adopted HCG science.  
**Governing HCG session record:** `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (source-reported adopted status).  
**Primary materials read:** entire `H3_FRAMEWORK_REVIEW_AND_EULER_GATE_CLAUDE_v0_1.md`, all source programs and frozen outputs in `H3_FRAMEWORK_REVIEW_CLAUDE_v0_1.zip`, and the prior `H3_D46_REVIEW_KIMP_AND_D50_D52_CLAUDE_v0_1.md` and its computational source. The present review does **not** re-prove the Hiss–Malle classification or independently regenerate CTblLib's 459 tables.

## Decision table

| Result | Independent assessment | Scope |
|---|---|---|
| Reciprocal-locality corollary | **CHECKED** | Pairing by a **K-linear coefficient-Hermitian isometry** between `g` and the inverse of its partner; conjugacy merely over C is insufficient. |
| Inert-prime norm criterion | **CHECKED** | Positive rational determinants in K=Q(sqrt(-3)). |
| `2 ⊗ b` exactly three projectively active local factors | **CHECKED** | Factorwise tensor + `W=S_(b+1)` standard-normalizer model, N>=19, total movement=4b+8. |
| Lemma T' | **CHECKED**, conditional on projective irreducibility and the genus-zero parabolic cohomology formula | See independent integer minimization below. |
| `2 ⊗ b`, `W=S_(b+1)`, 24<=b<=64 | **SOURCE-COMPUTED / PROPOSED for the whole range** | The source program and frozen scan were inspected; source-code replay performed only through b=35. A separate analytic argument now checks b=25 and b=26 without relying on exhaustive partitions. |
| `d=50,51,52` exclusion, hence `d>=53` | **Eligible for source-conditional CHECKED**, subject to the inherited classification/character data | b=25,26 and `4⊗13`, `3⊗17` are now closed by independent proofs. Hiss–Malle/CTblLib and other inherited normalizer inputs were not independently regenerated in this turn. |
| New dedicated obstruction track | **RECOMMENDED for PI approval** | A noncanonical HCG research track with claim-level status; not an automatic RTG canonical stream or an HCG v0.3 adoption. |

## 1. Reciprocal-locality formula

For positive K-Hermitian h0, set E_g=im(1-g), a_g=det(h0|E_g) and b_g=det((1-g)|E_g). With consistent K-bases, g and g^-1 have the same movement subspace, and the restrictions of 1-g and 1-g^-1 are h0-adjoints. Hence

`a_(g^-1)=a_g`, `b_(g^-1)=bar(b_g)`,

so the pair contributes `a_g²/(b_g bar(b_g))`, a norm. The same holds if the inverse partner is conjugate by a K-linear h0-isometry. In a dimension-2n parabolic setting, inverse pairing therefore gives

`[det h_par]=[(-1)^n]` in `Q×/N_(K/Q)(K×)`, and for n=4 the discriminant is split.

**Important notation limit:** An *individual* `a_g/b_g` need not be rational. Therefore an “inverse-imbalance class” should be represented by the product of K-valued local factors, and the `Q×/Norm` class applied **only to the total rational product**, not to individual generally nonrational local factors.

**Computational check:** the uploaded 40+40 exact K-unitary examples were rerun with a byte-identical result; the root-norm 1-versus-2 countercontrol correctly has nonsplit class [2]. This proves that C-conjugacy alone cannot replace the K-isometry requirement.

## 2. Inert-prime criterion

For `K=Q(sqrt(-3))`, `D∈Q_{>0}` is a norm iff `v_p(D)` is even for each rational prime `p≡2 (mod 3)`. At the ramified prime 3 the remaining local condition is implied by the norm product formula. The source check over integers D<=3000 reproduced. The statement must explicitly assume **D>0**; a negative rational is not a norm from an imaginary quadratic field.

## 3. Three-active reduction in the S_(b+1) tensor branch

Set V=A⊗B, `dim A=2`, `dim B=b`, with a factor homomorphism `g↦(A'(g),w(g))`, `B=std_(S_(b+1))` and `sum c_j=4b+8`. An A-projectively-active branch costs >=b, and each other effective branch costs >=2. Irreducibility of the projective A-image forces >=3 actives; four would cost at least `4b+30 >4b+8`. Therefore there are exactly three actives.

If an inactive has A'(g)=μI with μ≠1 of order q>=2, its 1-eigenspace has dimension at most `2 floor((b+1)/q)`, so its movement rank is at least `2b−2floor((b+1)/2)>=b−1`. Relative to the baseline inactive cost 2 this consumes >=b−3, whereas the entire slack after 3 active + 16 inactive minima is only b−24. Contradiction. Thus all inactives have A'=I and cost `2 ind(w)`. This justifies the cycle-index scan's assumptions.

## 4. Lemma T' — independent proof and cheaper integer optimizer

For a factorwise representation V=A⊗B, `dim A=a`, let active A-projective factors have largest-eigenspace codimensions `δ_i>=1`. Choose an index k with maximal δ_k. Normalize all other active A lifts so that their largest eigenspace has eigenvalue 1; normalize the inactive A parts to identity, and let the final A_k lift absorb the scalar needed to make the total product one. The resulting rank-a local system is irreducible because the projective A-image is, so

`sum_i rank(1−A'_i)−2a = dim H¹_par(P¹,A') >= 0`.

Ranks for `i≠k` are δ_i, and the final rank is <=a. Thus

`sum_i δ_i − max_i δ_i >= a`.

For t>=3 active branches, the smallest total codimension allowed by this gate is exactly

`D_min(a,t) = max(t, a + ceil(a/(t−1)))`.

The resulting lower movement cost is

`C_min = b D_min(a,t) + a max(19−t,0)`.

This **nonexponential independent optimizer** reproduces all submitted threshold rows: a=3→b>=19, a=4→b>=16, a=5→b>=15, a=6→b>=13, a=7→b>=12, a=8→b>=11. In particular, `4⊗13` and `3⊗17` are excluded directly.

## 5. An independent, nonenumerative closure for `2⊗25` and `2⊗26`

For a permutation w∈S_(b+1), let J=ind(w) and denote by m_ζ the ζ-eigenspace multiplicity on its b-dimensional standard representation. Then

- `m_1=b−J`;
- for ζ of order q>1, `m_ζ <= floor((b+1)/q)` and `m_ζ <= J/(q−1)`.

A nonscalar active factor has distinct eigenvalues x,y and movement cost

`c=2b−m_(x^-1)−m_(y^-1)`.

**b=25:** The unique cost pattern is three actives (25,25,26) plus 16 inactive cost-2 branches. The maximum active indices are (13,13,2), so total index <=44 while Riemann–Hurwitz on 26 sheets requires 50. Thus this S26 branch is impossible.

**b=26:** The total movement budget is 112. Exactly four possible sorted cost patterns remain:

1. (26,26,26) with 16 inactive and total inactive index 17;
2. (26,26,28) with 16 inactive and index 16;
3. (26,27,27) with 16 inactive and index 16;
4. (26,26,26) with 17 inactive and index 17.

For costs 26,27,28 the maximal permutation indices are 13,2,14, respectively. Case (3) has total index <=33<52 and fails Riemann–Hurwitz. In each of (1),(2),(4), the required active-index sum is at least 35 or 36. Even granting the other two their maximum, **each active index is at least 9**.

At b=26 a cost<=28 active with J>=9 necessarily has inverse A-eigenvalues `{1,-1}`. Proof: the fixed multiplicity is `52-c>=24`. If neither spectral eigenvalue equals 1, the total multiplicity is <=13+9=22. If one is 1 and the other has order q>=3, fixed multiplicity <=26−J/2, so J<=4. If the other eigenvalue is absent, J<=2. Thus for J>=9 the other eigenvalue is -1. Its A'-factor has determinant -1.

Consequently all three actives in the Riemann–Hurwitz-feasible cases have determinant -1, all inactives have A'=I, and `det(prod A'_i)=(-1)^3=-1`, contradicting `prod A'_i=I`. Thus the S27 branch of `2⊗26` is also excluded **without relying on the 24..64 partition scan**.

## 6. Status of d>=53

The earlier source-conditional d=50..52 exclusion has the following now-independent algebraic inputs: the S26 and S27 tensor branches by §5; `4⊗13` and `3⊗17` via §4; all other imprimitive/tensor branches from earlier checked Clifford/normalizer arguments. The primitive shortlist still relies on the Hiss–Malle 2001/2002 classification and the source-reported CTblLib minimum movement ranks, which were not regenerated from all 459 tables here. Therefore the appropriate claim is **CHECKED as a source-conditional mathematical implication, not a fresh independent CTblLib campaign**. The lower bound d>=53 is not a theorem about all nonsplit Weil eightfolds or about the Hodge conjecture.

## 7. Recommended framework design

Treat `HCG-HURWITZ-HODGE-OBSTRUCTION` as a **noncanonical HCG research track**, subject to PI approval, with claim-level identifiers, exact assumptions and statuses. The core checks are:

1. parabolic dimension / age / Hurwitz moduli budget;
2. local determinant norm and inverse-pairing obstruction;
3. representation, Clifford, tensor and rank-motion obstructions;
4. transfer supplier (L) and geometric polarization/period hypotheses.

A failure of any necessary gate rules out that *particular Severn-type transfer datum*; it does not rule out all nonsplit Weil eightfolds or prove a negative case of the Hodge conjecture. In addition, moving a **parabolic cup** discriminant to the **polarized abelian factor** requires the relevant cup–polarization/projector identification (cf. the prior W5-specific verification); it must not be silently assumed for an unrelated family.

Do not modify HCG v0.2 ADOPTED or the PI-decision fields solely on this review. No new auditor round is required.
