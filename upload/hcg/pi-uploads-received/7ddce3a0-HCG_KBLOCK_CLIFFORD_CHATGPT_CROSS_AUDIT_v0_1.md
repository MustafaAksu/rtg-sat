# HCG — independent review of Clifford repair A′, two-block scalar bound B, and proposed d=42 tensor exclusion

**Date:** 30 October 2026  
**Provenance:** `[SESSION]`; internal research, not human-refereed and not adopted.  
**Reviewed source:** `H3_KBLOCK_LEMMA_REVIEW_AND_D42_FRONTIER_CLAUDE_v0_1.md` (complete, 60 lines), supplied source ZIP (all six archive members inspected or verified; script fully read). Pre-existing HCG (H) hypotheses and previous checked conclusions used as explicit dependencies, not rederived here.  
**External targeted reference:** classical Clifford theory: the normal-subgroup isotypic decomposition and, in the isotypic case, a factorwise *projective* tensor representation. See e.g. Späth, *Clifford theory via projective representations*, Theorem 1.1 and projective representation discussion; and *History of Projective Representations of Groups*, Theorem 8.

## Decision

- **Lemma A′ — CHECKED within (H) and the inherited K-imprimitive dimension bound.** The originally chosen complex system need not be Galois-stable. Replacing it by the canonical isotypic decomposition of its normal kernel repairs the proof.
- **Lemma B — CHECKED** for the two-block standard symmetric/skalar case, with the cost argument based on rank equality, not equality of scalar local values on the two lifts.
- **Consequence — CHECKED (conditional on inherited results):** Under (H), no nonsplit feasible datum of dimension less than 42; in dimension 42 the *only remaining structural branch prior to this report's new observation* is a factorwise 3×14 tensor structure.
- **New PROPOSED observation:** Under the same finite-unitary, genus-zero, irreducible, effective-branch budget assumptions, even a factorwise 3×14 tensor structure cannot attain the necessary 19-branch, rank-sum-92 budget. A self-contained lemma on the product of three unitary projective reflections is supplied below. If independently confirmed, the lower bound strengthens to **d≥43**, not adopted here.

## Package reproducibility

The original supplied ZIP SHA-256 is `488873b2f7966f597069eebbc5e565c8c76dba731a320cf5e89543d941c64e30`. Its `BUNDLE_SHA256SUMS.txt` validates **5/5** entries. The supplied `imprimitive_closure_claude.py` was run unchanged; its stdout exactly reproduces `imprimitive_closure_claude_out.txt` (exit 0). An independently written integer enumeration, `check_kblock_and_tensor_frontier.py`, passes 16 k≥3 shapes, ten r=13..22 scalar inequalities and the unique d42 projective-activity pattern. Neither integer script proves Clifford's theorem or the unitary-reflection lemma.

## 1. Lemma A′: detailed proof audit

Let Γ⊂GL_d(K) be finite with absolutely irreducible V. Let ℬ be a transitive complex imprimitivity system with normal kernel Λ; Λ consists of K-matrices and is normal in Γ.

### Non-isotypic restriction

Clifford's theorem gives an intrinsic decomposition `V|Λ = ⊕_{i=1}^k U_i` into isotypic components, permuted transitively by Γ. The absolute Galois group `Gal(\bar K/K)` permutes these components because Λ is K-defined, and it commutes with Γ's action on the set. Thus its orbits are permuted by Γ, and the sums of each orbit descend to K. If there is more than one Galois orbit, these sums form a proper K-defined Γ-imprimitivity system, excluded under the previously CHECKED nonsplit d<50 K-imprimitive bound. Hence Galois acts transitively on the intrinsic components.

For a local element fixing all these blocks, movement ranks are Galois-conjugate and therefore equal. An effective such element moves at least one dimension on **every** block: c_j≥k. An element with block permutation π_j moves at least r·ind(π_j). The genus-zero intermediate cover has `Σ_j ind(π_j)=2(k−1)`, and the number of block-moving branches is at most this sum. With N_eff≥19, this yields

`2kr+8 = Σ c_j ≥ 2r(k−1)+k(21−2k)`,

hence the required inequality

`E_k=2r+2k²−21k+8≥0`.

For k≥3, r≥6, kr≤42, integer enumeration gives E_k<0 in all 16 candidate shapes.

If the intrinsic decomposition has **k=2**, the block stabilizer has index two, is K-defined as a subgroup and acts irreducibly on each block (otherwise inducing a proper invariant summand for Γ). Since the two isotypic blocks are Galois-swapped, this reduces to the already checked two-block setup, now extended by Lemma B.

### Isotypic restriction

Suppose `V|Λ ≅ W^{⊕e}`. If e=1, Λ acts irreducibly, incompatible with its preservation of the proper original block system ℬ. If dim W=1, Λ acts by scalars. At most one of N_eff≥19 nonidentity branch elements can be a nontrivial scalar, since two would already cost 2d movement and leave at least 17×2 further movement (exceeding 2d+8). Thus at least 18 branches move blocks; the degree-k intermediate genus-zero cover has `J=2(k−1)≥18`, giving k≥10 and r=d/k≤4 for d≤42, contrary to the previously checked field-independent induced-period necessity r≥6.

If dim W≥2 and e≥2, the isotypic Clifford theorem yields a projective factorwise tensor structure `V ≅ W⊗U` of dimensions dim W,e≥2. The previously CHECKED tensor budget

`2ab+8≥3b+16a`, `2≤a≤b`, `ab≤42`,

has exactly one solution, (a,b)=(3,14), in the dimension range. This is a structural alternative, not a constructed geometric family.

**Critical scope:** Galois stability is asserted for the canonical Λ-isotypic system, **not** for the original arbitrary ℬ. K-primitivity is derived only *within the nonsplit d<50 assumptions*; the result does not classify arbitrary complex representations.

## 2. Lemma B: independent cost argument

In a non-K-defined, Galois-swapped two-block system with d=2r, the genus-zero intermediate double cover Y has exactly two swap branch points. The movement budget has an excess E≤2r−26. The inducing representation has reflection subgroup standard symmetric in the case under consideration, so `τ=std_{S_{r+1}}⊗ψ` for a finite scalar character ψ. A nontrivial scalar twist λ of a standard S_{r+1} matrix has local movement rank at least

`T_r=r−floor((r+1)/2)`.

At least two local ψ-values on Y are nontrivial, by the meridian product-one relation. If one lies over a block-preserving branch, its local rank is at least T_r; Galois equality of movement ranks on the two lifts makes its base-branch excess at least `2(T_r−1)`. If both nontrivial points lie over the two swap branches, each incurs excess at least T_r (since `c(g)-r=rank(1−g²|U_1)`), hence total at least 2T_r. Therefore any nontrivial ψ costs at least `2(T_r−1)`.

For each r=13,…,22, `2r−26<2(T_r−1)`; hence ψ is trivial. This **does not require the two lifts to have the same scalar character value**, only the inherited Galois equality of their movement ranks. The other reflection-group options are either monomial (induced rank-one period bound) or refine to a Galois-stable higher-k system (excluded by A′); high-rank exceptional primitive reflection groups do not occur.

## 3. New SESSION PROPOSED theorem: factorwise 3×14 at d=42 is impossible

### Statement

Assume finite positive-unitary monodromy, absolute irreducibility, a product-one tuple with at least 19 **effective** branch meridians and `Σ c(g_j)=2d+8`. If `d=42` and the representation is factorwise tensor decomposable as `V=A⊗B` with `(dim A,dim B)=(3,14)`, then these assumptions are inconsistent.

This claim depends only on the specified local movement budget, unitarity, factorwise tensor structure and absolute irreducibility. It does not assume K-defined factors or (L).

### Step 1: only three meridians move the projective A-factor

For an effective g=A_g⊗B_g, if A_g is projectively trivial, then `c(g)=3 rank(1−B'_g)≥3`. If A_g is projectively nontrivial, the maximum A_g eigenvalue multiplicity is at most two, so `dim Fix(A_g⊗B_g)≤2·14` and `c(g)≥14`.

Let t be the number of meridians whose PGL(A) images are nontrivial. Since their product is projectively 1 and they generate a projective action irreducible on A, t≥3: if t≤2 the image is cyclic and has an invariant eigenline. With N≥19,

`92=Σ c(g_j)≥14t+3(N−t)=3N+11t≥57+11t`.

Thus t≤3; t=3. N=20 would already require at least 93 movement units; hence **N=19**, t=3 and the absolute minimum is `3·14+16·3=90`, leaving slack two.

Each of the three A-active meridians therefore has movement rank at most 16. If A_g had three distinct eigenvalues, then `dim Fix(A_g⊗B_g)≤14`, making `c(g)≥28`, contradiction. Hence every projectively nontrivial A_g has eigenvalue multiplicities (2,1). After scalar normalization it is a unitary pseudoreflection of A, fixing a hyperplane pointwise.

### Step 2: three unitary pseudoreflections with scalar product commute

**Lemma.** Let R_1,R_2,R_3∈U(3) be nonidentity unitary pseudoreflections and `R_1R_2R_3=λI_3`. Then the three operators commute and have a common eigenbasis.

**Proof.** Let L_i be the one-dimensional movement line of R_i. If L_1=L_2, R_1R_2 fixes a 2-plane, so the product equality forces λ=1 and R_3 to have the same movement line. The operators commute.

Now assume L_1≠L_2. The identity `R_1R_2v=v` implies `(R_2−I)v=(R_1^{-1}−I)v∈L_1∩L_2={0}`, so

`Fix(R_1R_2)=L_1^⊥∩L_2^⊥`, of dimension one.

If λ=1, then `R_1R_2=R_3^{-1}`, which has a two-dimensional fixed space: impossible. Hence λ≠1. The eigenvalues of `λR_3^{-1}` are `(λ,λ,λ/μ_3)`, where μ_3≠1 is the exceptional eigenvalue of R_3. It has a one-dimensional fixed space only when μ_3=λ; that fixed space is L_3. Therefore `L_3=L_1^⊥∩L_2^⊥`. Put `W=span(L_1,L_2)=L_3^⊥`. On W, `R_1R_2=λI_W`, hence `R_2|W=λ(R_1|W)^{-1}`. Since R_2 is itself a pseudoreflection and λ≠1, its fixed line inside W must be L_1; its movement line inside W is L_1^⊥∩W. Thus L_1⊥L_2. The third movement line L_3 is orthogonal to both. All three pseudoreflections commute. ∎

### Step 3: reducibility contradiction

The original meridians satisfy `∏g_j=I_V`. In the projective A factor, the 16 inactive meridians are scalars. Consequently the three A-active pseudoreflection lifts have scalar product. By the lemma, they commute. All A-factor meridian lifts are therefore simultaneously diagonalizable, and each common A-eigenline `L⊂A` yields a nontrivial Γ-invariant subspace `L⊗B⊂A⊗B`. This contradicts absolute irreducibility.

**Proposed conclusion:** If the preceding A′/B exclusions are accepted, **all d≤42 are excluded** and the lower bound strengthens from d≥42 to **d≥43**. This is not registered as CHECKED until an independent peer checks the unitary pseudoreflection lemma, effective-branch counting and factorwise-lift argument.

### Caveat for the peer reviewer

The tensor factors A_g and B_g can be taken unitary *up to reciprocal scalars*: the finite projective A-image admits an invariant Hermitian metric. This ensures that normalizing the (2,1)-eigenvalue lifts to pseudoreflections does not lose positive unitarity. It is important not to silently assume these factors form honest ordinary Γ-representations; their projective multiplication is enough for the product-scalar argument.

## 4. Scope, suggested record dispositions, and next action

| Claim | Suggested status |
|---|---|
| Source archive and numerical inequalities | CHECKED (5/5 source hashes, byte-identical source replay, independent integer check) |
| Original Lemma A (arbitrary block system Galois-stable) | NOT VALID as stated; replace by A′ |
| Clifford repair Lemma A′ | CHECKED within the inherited nonsplit d<50 and induced-period hypotheses |
| Two-block Lemma B | CHECKED within the standard S_{r+1} branch |
| Nonsplit feasibility lower bound d≥42 | CHECKED as a **conditional** consequence of inherited HCG (H) results |
| New tensor 3×14 exclusion and d≥43 | SESSION PROPOSED; separate peer review required |
| HCG-OPEN-NONSPLIT8 | OPEN |

No modification was made to HCG v0.2 ADOPTED, the pending v0.3 ledger, or any PI decision field. Severn A/B/C remain CLAIMED.
