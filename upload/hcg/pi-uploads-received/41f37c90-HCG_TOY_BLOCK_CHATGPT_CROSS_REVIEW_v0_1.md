# HCG R1 — Repeated-block toy obstruction: independent proof and computation review

**Date:** 2026-10-23. **Distribution:** INTERNAL; do not send to the blind Priority-B auditor.  
**Primary derivation:** Claude, `H3_TOY_MIXED_CHECK_AND_EXPLANATION_CLAUDE_v0_1.md`.  
**Independent review:** ChatGPT. **Recommended state:** `HCG-ALG-TOY-BLOCK-LEMMA: CHECKED`, restricted to the stated tuple and cyclic interval class. No PI adoption or change to adopted HCG v0.1.

## 1. Actual inspection and source replay

The report, all five toy scripts and `generic_engine.py` were read. The nine full SHA-256 entries in the source report match. The root input is not included in the new producer ZIP; it was recovered byte-exactly from the already-mounted prior ChatGPT reproduction package, SHA-256 `01918b05c5ab35c2a35507fe9fc1c6773dd9a480cbdee446238458678ffc42b2`, matching the source's declared root pin.

Ran `toy_mixed.py`, `toy_explain.py`, `toy_explain2.py`, and `toy_realdescent.py` with ONLY hard-coded filesystem paths redirected. All four stdout files and `toy_mixed_hist.json` match the delivered outputs byte-for-byte. This is a replay of Claude's independently authored engine, not a new third implementation.

A separate ChatGPT implementation then used explicit block coordinates rather than the producer's nullspace/complement construction. It rebuilt all 54 monodromies from elementary Artin moves, reconstructed the cup form, and checked the endpoint-label formulas. It did not import `generic_engine.py` and did not define the operators by the proposed projector formula.

## 2. Canonical block description and the proof

Let `K=Q(w)`, `w²+w+1=0`, and

`a=(1,-1,0), b=(0,1,-1), c=(1,-w,0)`.

These three roots are K-independent, have squared length 2, and occur in the local-system tuple as

`(s_a,s_a,s_a,s_a, s_b,s_b,s_b,s_b, s_c,s_c,s_c,s_c)`.

Write a parabolic cocycle in one four-point block as `(a1 v,a2 v,a3 v,a4 v)`. Product-one closure and root independence force

`a1-a2+a3-a4=0`

in each block. Coboundaries act by adding an arbitrary common constant independently on the three blocks: the map from the ambient coefficient vector to its three pairings against `a,b,c` is invertible. Fixing the gauge `a2=0` yields the canonical representative

`(a1,a2,a3,a4) = (e,0,-f,e-f)`,

where `e=a1-a2=a4-a3` and `f=a2-a3`. Thus

`H=H_par^1 ≅ K^6`, in coordinate order `(e_a,e_b,e_c,f_a,f_b,f_c)`.

The directly evaluated cup form is

`S = [[0,-I3],[I3,0]]`

in the declared linear-first convention. In particular H decomposes into three 2-dimensional symplectic/skew-Hermitian block pieces. This canonical coordinate proof is independent of any numerical rank count.

### Endpoint classification

Full blocks contribute identity monodromy and zero cocycle flux. An interval has at most two incomplete endpoint blocks.

- Inside one block, even nontrivial portions give `E_L=|e_L|²` (first or last pair) or `F_L=|f_L|²` (middle pair). Odd portions have flux on the root line, killed by projection to the reflection's fixed space.
- For two distinct endpoint lines, two odd endpoint portions give zero: `Fix(s_i s_j)=Fix(s_i)∩Fix(s_j)=(Kv_i+Kv_j)^⊥`, since the two moving root lines are independent.
- One odd and one even endpoint gives a rational scalar times the even endpoint's `E_L`. Projection changes its length coefficient; it does not create a new cross direction.
- Two even endpoint portions give the flux `-e_i v_i+e_j v_j`. Its form is a combination of `E_i,E_j` and
  `X_ij = h(v_i,v_j)e_i conjugate(e_j) + conjugate(h(v_i,v_j))e_j conjugate(e_i)`.

Consequently every cut form is in the span of the nine independent labels

`E_a,E_b,E_c,F_a,F_b,F_c,X_ab,X_ac,X_bc`.

For the actual `Nhat=T^(ord C)-I` normalization, the three mixed representatives are

`R_ij = -2 E_i -2 E_j + X_ij`.

The other nonzero forms are negative rational multiples of an E or F label. Thus there are exactly **nine projectively distinct nonzero actual cut-form directions**: six pure E/F directions and three R directions. Those nine actual directions are independent, by the triangular change of coordinates from X to R.

### Laminar incompatibility and the upper bound

The middle-pair curve in block L connects the two gaps adjacent to its middle gap. Every curve with a nonzero E_L contribution has an endpoint at that middle gap and its other endpoint outside the middle pair. Therefore it crosses the F_L curve. No laminar family contains both E_L and F_L in its label support.

There are at most three diagonal labels and three cross labels in any tree. Thus

`rank_Q span{N_e : e in T} = rank_Q span{S conjugate(N_e) : e in T} <= 3+3 = 6`.

This is the structural proof; the 16,796-tree calculation is an independent finite verification of its hypotheses and consequences, not the proof's sole justification.

If an F label occurs, at most two blocks can supply E labels, so at most one cross label can appear and rank is at most 4. Hence rank 5 or 6 requires exclusively E-type block functionals. A rank-6 tree spans all `E_a,E_b,E_c,R_ab,R_ac,R_bc`.

## 3. Independent exact results

| Check | Result |
|---|---:|
| Direct Artin cut operators | 54 |
| Nonzero operators | 27 |
| All-cut Q-span | 9 |
| K-dimension of all-cut image span | 6 |
| Actual independent projective form types | 9 |
| Predicted endpoint classification matches operator forms | 54/54 |
| E/F crossing pairs checked | 27/27 |
| H0-valid triangles | 220/220 |
| Trees represented by exact mask-count dynamic program | 16,796 |
| Rank histogram | 3:12,594; 4:3,678; 5:459; 6:65 |
| Trees with E/F conflicts | 0 |
| Rank no greater than number of labels | 16,796/16,796 |
| Equality rank = number of labels | 15,176 |

Unlike the producer's per-tree rational row reduction, the new counting proof uses a polygon dynamic program on subsets of the nine independent actual form types. Only 42 support masks occur. A tree's rank equals the number of distinct actual directions it contains, so the histogram follows without a rank calculation on each of the 16,796 trees.

## 4. Real-descent explanation: a short exact refutation

For the declared roots,

`c_ab=-1, c_bc=1+w, c_ac=-w`.

On the e-coordinate quotient of any rank-6 tree, all E_i and all X_ij belong to the form span. Set `G=E_a+E_b+E_c=I3`. Directly,

`tr(G^{-1}X_ab G^{-1}X_bc G^{-1}X_ac)=c_ab c_bc conjugate(c_ac)=-w`.

This is nonreal. Under any simultaneous Hermitian congruence of G and the X forms, the normalized operators `G^{-1}X` transform by similarity (with the linear-first convention), so the trace is invariant. If all forms could become real matrices, the trace would be real. Hence the common-real-basis explanation is impossible, even under a general complex basis change, not just a diagonal phase change.

The source's longer word-trace negative controls reproduce exactly; the single displayed invariant is a shorter structural obstruction.

## 5. Important scope clarification

The **global** nine-dimensional space generated by all 54 cut forms is a subspace of `Herm(H)`, where `dim_K H=6`. It is not a single `Herm(H/I)` for a common I attached to all cuts: their total image span is six-dimensional, not a common three-dimensional isotropic space. For an individual tree with maximal isotropic I, `dim_K(H/I)=3` and `dim_Q Herm(H/I)=9`. The nine global directions come from changing block-function choices across trees, not from one common three-dimensional quotient.

The fixed tuple, cyclic marking and standard interval-curve class remain essential. No statement about all braids or all representatives of the Hurwitz component follows. Global multiplication of the logarithms by the positive rational return-normalization factors does not affect these rank bounds, but changes the coefficients of named operator relations.

## 6. Recommended records

- `HCG-ALG-TOY-MIXED-OBSTRUCTION`: CHECKED (producer and reviewer exact constructions agree).
- `HCG-ALG-TOY-BLOCK-LEMMA`: CHECKED, scoped to the reported three-root block tuple and interval/planar trees.
- Common-real-basis hypothesis: REFUTED in this scope; explicit trace witness retained.
- Proposed general repeated-block extension and the new G34 example: separate first-party SESSION derivations, not automatically CHECKED by this review. See the companion G34 note.
- NEW02-MIXED-01 remains CHECKED from its prior verification; not newly rerun in this round.
- No DSN adoption, PO-6 change, or release to the blind Hodge auditor.
