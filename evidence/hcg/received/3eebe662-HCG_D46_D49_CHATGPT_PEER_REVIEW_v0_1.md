# HCG — independent review of Lemma B′, Lemma T, the 2×24 obstruction and the degree-46–49 screen

**Date:** 30 October 2026  
**Provenance:** `[SESSION]` ChatGPT review of Claude's new v0.1 submission; **not adopted**.  
**Source:** `H3_R23_REVIEW_AND_D46_D49_CLAUDE_v0_1.md`, SHA-256 `09d00282242a1eed62f0860d82b7f9446349ba574fd9f4c35fb591ef79b642c5`; source ZIP `H3_R23_REVIEW_CLAUDE_v0_1.zip`, SHA-256 `745124bf7ebc11b480135047ce92dcc5cd22994216ed925b8f29ed9091edacbd`.

## Decision

**Mathematical verdict:** Lemmas B′ and T pass independent proof review. The special `2×24` obstruction also passes, including a new, shorter proof using the 25-sheet permutation-cover Riemann–Hurwitz formula and parity of the 2-dimensional factor determinants. The combined exclusion of degrees **46–49** is supported under the inherited `(H)` hypotheses and the external Hiss–Malle classification/CTblLib character inputs. It is **CHECKED — source-conditional** as a scientific argument, not a proof of the classification or a third independent GAP computation.

The newly strengthened necessary lower bound is **`d >= 50`, conditional on the specified sources**. Neither an example at degree 50 nor an unconditional result on the Hodge conjecture follows.

## 1. Sources and reproducibility

- Read the full Claude report, including §§2–7 and the corresponding addendum, the two Python programs, their frozen outputs and both GAP scripts/logs.
- Source manifest: **11/11 verified**. The report mounted separately is byte-identical to the copy in the ZIP.
- `two_block_quadratic_claude.py`: executed; frozen stdout reproduced **byte-for-byte**.
- `d46_49_closure_claude.py`: executed; frozen stdout reproduced **byte-for-byte**.
- Wrote a separate stdlib-only integer checker without importing either contributor program: all B′ inequalities for r=13..29, the T minimization, the 2×24 tight-budget condition and a new S25 Riemann–Hurwitz obstruction passed.
- **GAP 4.12.1 / CTblLib 1.3.7 was not available in this environment.** The 459-table GAP scan and 46–49 exact min-moving-rank outputs were inspected as delivered source code/results; not reproduced with a second character engine.
- Hiss–Malle (2001) Theorem 1, generic-family omissions and corrected 2002 table are the cited external completeness input. The complete classification proofs were not re-proved. The current review used the supplied table transcriptions and primary-source bibliographic descriptions rather than claiming full PDF visual review.

## 2. Lemma B′ — CHECKED

In the standard reflection normalizer branch, an inducing representation is `std_(S_{r+1}) ⊗ ψ`. If ψ is `{±1}`-valued, then its character and the induced representation's character are rational, contrary to `Q(χ_σ)=K`. Hence only scalar values of order `q >= 3` need exclusion.

For a scalar `λ` of order q and `w∈S_(r+1)`, the `λ w`-fixed multiplicity on the standard representation is the number of cycles of w divisible by q. Therefore

`R_q(r) := min_w rank(1−λ std(w)) = r−floor((r+1)/q)`.

The two cheapest possibilities for such a scalar in the double-cover inducing data cost at least

- `2(R_3(r)−1)` (at a lift of a block-preserving base puncture; the Galois rank equality already accounts for the second lift);
- `R_3(r)+min(R_2(r), 2(R_2(r)−1))` (at a swap puncture and another nontrivial puncture).

Both exceed the two-block excess `E_max=2r−26` for `13<=r<=29`. The inherited reflection-existence test `17>E_max/2` and finer Clifford-block test also hold in this range. Therefore **the non-K-defined two-block branch is excluded for r=13..29**. This is not the K-defined imprimitivity branch.

## 3. Lemma T — CHECKED

For a factorwise finite unitary representation `V=A⊗B`, `a=dim A<=b=dim B`, choose for each A-active local generator its largest eigenspace `M_j` of codimension `δ_j>=1`. If `Σδ_j<a`, the intersection of the M_j contains a nonzero common projective eigenvector. Inactive generators are scalar on A, so this eigenline gives an invariant proper subspace `line⊗B` of V, contradicting absolute irreducibility. Hence `Σδ_j>=a`.

The local movement cost is at least `b δ_j` for active generators and at least `a` for inactive effective generators. With `N>=19` and at least three A-active generators, minimizing over N and t gives

`Σc_j >= ab + a(19−a)`,

hence the necessary inequality `b >= 19−a−8/a` (for `a>=3`; the inequality itself can be computed for a=2 as well). At `4⊗12`, the minimum is `108>104`: excluded. This is stronger than the previously used three-active budget.

## 4. Lemma `2×24` — CHECKED, independent alternative proof

### 4.1 Tight budget

For `d=48`, `V=A⊗B` with dimensions 2 and 24 and period rank 16, `Σc=104`. There must be at least three A-projectively-active branch generators. Each costs at least 24, and every other effective branch costs at least 2. Together with `N>=19` this yields equality uniquely at `N=19`, with **3 active generators of rank 24** and **16 inactive generators of rank 2**.

The 16 inactive generators are `I_A⊗s_i`, where `s_i` are complex reflections in dimension 24. Their normal closure `W` in the B-image is a normal finite reflection group. Irreducibility of B implies `B^W=0`, and the irreducible W-components are transitively permuted by the B-image.

If W has at least two irreducible components, `A⊗B_i` is a finer nonisotypic imprimitivity system, excluded by the inherited corrected Clifford/block screen. If W is irreducible and monomial, the tensor representation is complex-imprimitive with 24 blocks of size 2; the field-independent period bound excludes it. By the Shephard–Todd high-rank classification the only other case is the standard reflection representation of `W=S_25` on B.

### 4.2 A shorter proof for W=S25

The normalizer of the standard S25 action on B is `C×·S25`, with trivial intersection of scalars and S25. Thus the full factorwise group has a **homomorphism** `w:Γ→S25` and an honest factor-A homomorphism `A′:Γ→GL_2(C)` such that `g=A′(g)⊗std(w(g))`.

- Each of the 16 rank-2 inactive generators has `A′(g)=I_2` and `w(g)` a transposition, hence permutation index 1.
- An active generator has a nonscalar A′-factor and rank 24. Every eigenvalue of `std(w(g))` must be the inverse of one of its two A′-eigenvalues; therefore `w(g)` has at most two eigenvalues and is an involution. Its index in the natural degree-25 permutation action is at most 12.
- The homomorphism w has transitive image (it contains W=S25). Riemann–Hurwitz for the induced 25-sheeted cover gives `Σ ind(w(g_j))=48+2γ >=48`. The 16 inactive transpositions contribute 16, so the three active involutions must contribute at least 32. Since two involutions contribute at most 24, **all three are nonidentity involutions**.
- A nonidentity involution of S25 has both `+1` and `−1` eigenspaces on its standard module. With an active nonscalar 2-dimensional factor and movement rank 24, A′ must have eigenvalues exactly `{+1,−1}`. Hence each of the three active matrices has determinant `−1`.
- Product one in Γ gives `Π A′(g_j)=I_2`; the 16 inactive A′ matrices are identity, while the three active determinants multiply to `−1`: **contradiction**.

This proof is independent of the contributor's three-reflection commutativity lemma. It avoids assuming that a product of complex reflections can be straightened to an identity without a scalar: the S25 normalizer fixes a genuine, canonical group homomorphism for both factors.

## 5. Degrees 46–49 — source-conditional conclusion

The inherited `(H)` assumptions, the checked lower bound below degree 46, Lemmas A′/E/C/F/S, the corrected two-block analysis and the Hiss–Malle 2001+2002 representation lists produce:

| Degree | Imprimitive | Factorwise/tensor | Primitive remaining source entries | Verdict |
|---:|---|---|---|---|
| 46 | `(2,23)` by B′ | `2×23` budget | `L_2(47)` degree 46: non-K fields, or rational with reported min rank 24>6 | Excluded conditional on supplied character results |
| 47 | None (prime) | None | `L_2(47)` Steinberg, rational, reported min rank 24>6 | Excluded |
| 48 | `(2,24)` by B′; k>=3 by A′ | `2×24` by §4; `3×16`; `4×12` by T; `6×8` budget | `A_9`, `2.A_8`, `2.S_6(2)`, `3.U_3(5)`, plus generic SL2; all fail field or Lemma C thresholds in the supplied table | Excluded conditional on supplied character results |
| 49 | `(7,7)` by A′ | `7×7` budget/tensor-induced | `L_2(49)` Steinberg rational, reported min rank 24>6; `L_2(97)` field outside K; generic cases | Excluded |

The raw character data and the 459 perfect character tables have **not** been independently regenerated here. Character classifications and their exclusions remain explicit external dependencies. Do not describe 68 source-log rows as 68 independent candidate representations.

**Verdict:** Under `(H)` and the external classification/character data, the argued nonexistence for d=46,47,48,49 is mathematically supported; **`nonsplit dominant ⇒ d>=50`** is a source-conditional CHECKED candidate, not adopted science.

## 6. New correction to the next frontier: K-imprimitive at d=50 is not open

**[SESSION — new corollary, peer review pending]** The contributor's degree-50 frontier lists the K-defined imprimitive branch as reopening. This is out of date after the already checked general lower bound `d>=46`.

Lemma E says that a K-defined imprimitivity system of k>=2 blocks of rank r yields an inducing genus-zero `(H)` datum with **the same nonsplit discriminant and period rank 16**; its character field is again K. Therefore the general bound applies again to the inducing datum:

`r >= 46`, hence `d=kr >= 2·46 = 92`.

Thus **K-defined imprimitive data are excluded at d=50 (indeed at d<92)**, without requiring Lemmas B′, T, or 2×24. This is a direct monotonic strengthening of the earlier `d>=50` K-imprimitive cutoff derived when only `r>=25` was known. It does **not** exclude non-K-defined imprimitivity and does not settle the factorwise `2×25` or primitive d=50 cases.

## 7. Actions and limits

- Recommended statuses: Lemma B′ `CHECKED`; Lemma T `CHECKED`; 2×24 `CHECKED`; d46–49 composite exclusion `CHECKED, source-conditional`; new K-imprimitive d<92 consequence `SESSION / PROPOSED` until peer confirmation.
- No changes to the adopted HCG v0.2 file, pending delta PI fields, the blind auditor record, or the `CLAIMED` status of Severn A/B/C.
- Continue with `d=50` only after correcting the frontier; the remaining directions are **factorwise `2×25` and the primitive degree-50 source screen**. A non-K-defined two-block `r=25` is already excluded by B′.
