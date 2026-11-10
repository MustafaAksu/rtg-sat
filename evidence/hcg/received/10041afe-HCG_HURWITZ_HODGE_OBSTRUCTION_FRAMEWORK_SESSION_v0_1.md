# HCG — General Hurwitz–Hodge obstruction framework and reciprocal-locality no-go

**Date:** 2026-10-30  
**Status:** `[SESSION]`, research proposal; **not adopted**.  
**Scope:** genus-zero finite-unitary-cover transfer data with imaginary quadratic coefficient field, absolutely irreducible coefficient representation, no global fixed vectors, eight-dimensional Weil multiplicity of signature (4,4), and the claimed dominance/transfer framework (H). No universal obstruction to nonsplit Weil abelian varieties or the Hodge conjecture is claimed.

## 1. Source provenance and reading scope

- Governing HCG session record `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`): relevant scientific-status and Severn §§6.7–6.21 were targeted, not fully re-audited.
- `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md`: theorem, its proof §§2–3 and clarification text inspected. The locality theorem is already CHECKED by ChatGPT and Claude, as a SESSION result; no novelty or human-refereed status is asserted.
- Claude `H3_D46_REVIEW_KIMP_AND_D50_D52_CLAUDE_v0_1.md` (SHA-256 `7547a53af8bd84b797338849d335bd48d93c21dbbee4e8190ecfd70280e0a41d`): read fully. `H3_D46_REVIEW_CLAUDE_v0_1.zip` (SHA-256 `3f2d74408e6e1761f8f41de925d7727ce47c1ff02ca70355cbf539e93819ebdf`): archive scripts, output, and manifest inspected; `two_by_b_rh_claude.py` and `d50_52_closure_claude.py` replayed without scientific source modification, with byte-identical frozen outputs. SHA-256 manifest 12/12.
- The GAP programs and logs were inspected but GAP / CTblLib were **not independently run** in this environment. Consequently the claimed complete degree-50/51/52 primitive screen remains source-conditional. The Python closure program consumes candidate data assembled from these logs; it is not an independent character classification.

## 2. Proposed general obstruction certificate

Let `K` be imaginary quadratic and `(V,h0)` positive Hermitian over `K`, `d=dim_K V`. Let `(g_1,...,g_N)` be a product-one generating finite unitary tuple, with `c_j=rank_K(1-g_j)`. Define `H=H^1_par(P1\D,V)`.

The following necessary conditions are **Hurwitz invariant**, since a braid preserves the unordered local conjugacy-class multiset, the product-one relation, and the generated representation:

1. **Cohomology budget:** `dim_K H = sum c_j - 2d = 8`; equivalently `sum c_j=2d+8`.
2. **Base dimension:** dominance onto a 16-dimensional target requires `N-3 >= 16`, i.e. `N>=19` effective points.
3. **Balanced Chevalley–Weil ages:** `sum age(g_j) = sum age(g_j^{-1}) = d+4` for signature `(4,4)`, with the specified action/dual conventions.
4. **Local arithmetic:** define `E_g=im(1-g)`, `a_g=det(h0|E_g)` (rational) and `b_g=det((1-g)|E_g)` (in `K*`). The CHECKED locality formula gives
   `disc(H) = [prod_j a_gj/b_gj]` in `Q*/N_K/Q(K*)` (global sign is + because n=4). Nonsplit data require a nontrivial class.
5. **Period factorization:** whenever the Hodge variation factors through a moduli space of dimension `<16` (e.g. induced local systems on a genus-gamma curve with s effective points, with upper bound `3gamma-3+s`), dominance is impossible.
6. **Normal-subgroup movement:** in the normal-irreducible setting of checked Lemma C, a noncentral commutator with `c <= 2 floor((2d+8)/19)` must exist. If a lower bound for all such elements in the normal subgroup exceeds this threshold, the datum is impossible. Character tables and classification only supply these lower bounds; they are not part of the abstract criterion.

Any violation gives a **braid-stable no-go certificate**. These are **necessary**, not sufficient conditions. A tuple that survives every gate is not automatically geometrically realized, satisfies (L), or dominates.

## 3. New corollary: inverse-paired monodromy forces split discriminant

**`[SESSION — THM (proved implication), peer review pending]`.** Assume the positive Hermitian and parabolic-cup hypotheses of the locality theorem; `dim_K H = 2n`. Suppose the indices admit a fixed-point-free involution `j -> j'` such that `g_j'` is **unitarily conjugate** to `g_j^{-1}` in the fixed coefficient Hermitian representation. Then

`[det(theta S)] = [(-1)^n]` in `Q*/N(K*)`.

**Proof.** Since `g` is unitary, `E_g=E_{g^{-1}}` and `(1-g^{-1})|E_g` is the Hermitian adjoint of `(1-g)|E_g`. Choose matching bases on these spaces. Therefore `a_(g^-1)=a_g`, `b_(g^-1)=conj(b_g)`, so

`Delta(g) Delta(g^-1)=(a_g/b_g)(a_g/conj(b_g))=N_K/Q(a_g/b_g)`.

Unitary conjugation does not alter this norm class (a change of moving-space basis changes the Gram determinant by a norm). Pair all indices; locality leaves only the global sign `(-1)^n`. QED.

For the Weil eightfold target `n=4`, **all such data have split discriminant**. The condition refers to the full multiset with even pairing, *not* merely to each class being individually inverse-stable. This obstruction does **not** require the tuple to be literally adjacent-paired, the group to be generated by reflections, or the Hurwitz component to be known. It persists under any braid move.

**Exact controls in `local_reciprocity_check.py`:**
- `K=Q(omega)`, 5 pairs of order-3 local characters `(omega,omega^-1)`: local denominator product `3^5`, a norm, yielding split `[1]`.
- The ten-branch cyclic `C6` nonsplit separator with exponents `(2^5,3,4^3,5)`: denominator product `162=2*3^4`; class `[1/162]=[2] !=[1]`. The multiset is not inverse-paired.
- 20 order-2 `G34` reflections with per-reflection local factor `a/b=3`: total `3^20`, a norm. Thus the known `G34` 20-reflection branch is split without any connectedness or H4 computation.

This is a **newly recorded corollary**, not a claim of literature priority: it follows immediately from the previously CHECKED local-discriminant theorem, whose analogue was already announced by Severn.

## 4. Structural uniform reduction for factorwise 2 tensor b with standard symmetric normalizer

**`[SESSION — ALG/THM, independent peer review pending]`.** In the previously established `W=S_{b+1}` normalizer branch, suppose the representation actually factors as `sigma=A' tensor std(w)` with a **genuine** homomorphism `A':Gamma -> U(2)` and `w:Gamma -> S_{b+1}`. The local rank total is `4b+8` and `N>=19`.

Call a local branch *active* if its `A'` component is nonscalar. Such a branch moves at least `b` dimensions. Inactive effective branches move at least 2, and their movement ranks are even. A noncyclic projective `A'` image and product-one imply at least three active branches; four active branches would cost `4b + 2*15 > 4b+8`. Thus **exactly three active** branches exist, with `s=N-3>=16` inactive branches.

Moreover, **every inactive `A'` component equals `I_2`**. Indeed an inactive element has the form `mu I_2 tensor std(w)`; if `mu!=1`, its `mu^-1` eigenspace inside the standard permutation module has dimension at most `floor((b+1)/2)`, hence movement rank at least `b-1`. But replacing a cheapest inactive cost 2 by `b-1` forces total cost at least `3b+32+(b-3)=4b+29>4b+8`. Contradiction.

So in *every such potential datum*, the two-dimensional factor has **precisely three potentially nontrivial local monodromies**, with product one. This is a uniform **three-point/triangle-group reduction**, independent of the numerical size of b. One cannot infer that it is nonexistent in all b without an additional finite-subgroup/character argument.

For `24<=b<=30`, `independent_cycle_screen.py` and `independent_twobudget.py` recompute the finite cycle-order multiplicity/index bounds for S_(b+1) without using Claude's partition routine. Any RH-admissible cost distribution forces all three active eigenvalue pairs to be `{1,-1}`; the inactive factors all have `A'=I`. Hence `det(prod A'_j)=(-1)^3=-1`, contradicting product one. This is a **bounded-range** result (not a proof for all b).

For `31<=b<=34`, independent permutation-cycle enumeration gives a further **PROPOSED** extension: every RH-compatible assignment either (i) forces all three active pairs `{1,-1}`, giving the same determinant contradiction, or (ii) has active costs `(b,b,2b-24)` and 16 inactive costs 2; the first two active `A'` matrices are involutory unitary reflections. The entire 2-dimensional factor is then generated by two involutions, has a real-valued character, and so does `A' tensor std(w)`. Since `sigma` is K-valued, its character becomes Q-valued, contrary to the stipulated exact character field `K`. This argument requires peer checking of the normalizer decomposition and equality cases before adopting the extension.

The present `d=50,51,52` source results agree with this more general calculation. The **primitive-character exclusions** at those degrees are still conditional on the enumerated Hiss–Malle and CTblLib sources and should not be relabelled as independently reconstructed GAP data.

## 5. Research decision

**Recommended priority:** Stop treating “next integer degree” as the central scientific question. Formalize a no-go *certificate system* and investigate structural exceptions.

1. Promote the proved **inverse-paired local norm obstruction** to peer review. It yields a braid-invariant negative result across all d.
2. Peer-review the **three-active-branch tensor reduction**, and use the finite projective subgroup classification `PGL_2(C)` (dihedral, tetrahedral, octahedral, icosahedral) to attack the entire `2 tensor b` family rather than rerunning one b at a time. The extra 31..34 computation is a test, not a universal theorem.
3. For primitive groups, specify a **movement/minimum-commutator obstruction** based on `2 floor((2d+8)/19)`, and use complete character data as certificates. Avoid equating a finite CTblLib census with an unconditional all-degree classification.
4. Keep the **discriminant no-go**, **dominance no-go**, and **supplier (L)** as separate gates. Nothing in this note proves that all nonsplit Weil abelian eightfolds are impossible, or alters Severn Theorems A/B/C (`CLAIMED`).

**Recommended status:** General obstruction *framework* = PROPOSED. Reciprocal-locality implication = SESSION THM/proof supplied, peer pending. `d50–52` budget/cycle computations = independently replayed; full exclusion remains source-conditional pending normalizer and primitive completeness checks. HCG v0.2 ADOPTED unchanged; no RTG adoption; no third-family transmission.
