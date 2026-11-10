# HCG — Claude's independent check of ChatGPT's research note §§A–C (P1/A2/A3, P2, P3) v0.1

**Date:** 23 October 2026 · **Status:** PROPOSED → CHECKED (Claude) for the algebraic statements listed in §5. PI decides. INTERNAL (SG-10): not for the blind auditor.
**Input:** `CHATGPT_RESEARCH_DERIVATIONS_PROPOSED_v0_1.md`. SHA-256 bfd9332656ed0a8d91d62d9959b3ebdf71013cc2aadd1be13a19d927fcffdbcf, which matches the value ChatGPT stated in `HCG_SERIES_BOUND_CHATGPT_REVIEW_v0_1.md` §7.
**Independence:**
- New engine `generic_engine.py`, written for this check. It handles arbitrary unitary tuples over K = ℚ(ω) with the standard h.
- It does not import `g34_gateB`, `edgeform_predict` or any ChatGPT code.
- Cochains are stored as coordinates on im(g_k − 1). The engine provides cocycles, coboundaries, the cup form, word evaluation and twists by conjugation.
- Twist convention: φ(g_k) = c g_k c⁻¹ for a ≤ k ≤ b, with T: u ↦ u∘φ^power. This is the same convention as the session certificates.
- Cup form: S(x,y) = Σ_k h(Q_k⁻¹F_k^x + α_k^x, y(g_k)), where (1 − g_k)α_k^x = x(g_k). For order-2 reflections this reduces term by term to the certificate convention, because −h(−(a/2)v, ·) = h((a/2)v, ·).

## 1. Algebraic re-derivation (common to P2 and P3)

Let g be unitary, so g* = g⁻¹, and let (1 − g)α = c.

- From the definition, gα = α − c, which gives **(1 − g⁻¹)α = −g⁻¹c**.
- With G_k := Q_k⁻¹F_k and F_{k+1} = F_k + Q_k c_k, we get **G_{k+1} = g_k⁻¹(G_k + c_k)**.
- Hence, for any w:
  - h(G_k + α_k, (1 − g_k)w) = h((1 − g_k⁻¹)(G_k + α_k), w)
  - = h(G_k − g_k⁻¹G_k − g_k⁻¹c_k, w)
  - = **h(G_k − G_{k+1}, w)**.

Both relations in note §B are therefore correct for general unitary g_k. Neither the involution property nor the rank-one property is used.

Iterate over an interval e = [a, b] with boundary word c = g_a⋯g_b and C = ρ(c). Using u_x(c) = c_a + g_a c_{a+1} + ⋯, this gives **G_{b+1} = C⁻¹(G_a + u_x(c))**, which is the relation in §C.

If (N y)(g_k) = (1 − g_k)w for k ∈ e and 0 otherwise, the sum telescopes:

- S(x, Ny) = h(G_a − G_{b+1}, w).
- When w ∈ Fix(C), unitarity gives h(C⁻¹z, w) = h(z, Cw) = h(z, w). So S(x, Ny) = −h(u_x(c), w).

The two specialisations follow:

- **P2, inverse pairs.** C = 1 and w = u_y(c) = Σ_{i∈e} τ_i y. This gives S(x, N_e y) = −h(Σ τ_i x, Σ τ_i y).
- **P3, finite order.** w = u_y(c^k) = Σ_{j<k} C^j u_y(c) = kΠ_C u_y(c). Π_C is the h-orthogonal (self-adjoint, idempotent) projector onto Fix(C). This gives **S(x, N_e y) = −k h(Π_C u_x(c), Π_C u_y(c))**. The factor is **k, not k²**.

Further checks:

- (N y)(c) = (1 − C)w = 0. Since T^k(Ny) = Ny, it follows that N² = 0.
- Coboundaries satisfy u(c) = (C − 1)v, and Π_C(C − 1) = 0, so the form descends to cohomology.
- The coboundary pair ((r − 1)v, (r⁻¹ − 1)v) has t = (r − 1)v + r(r⁻¹ − 1)v = 0, so τ is well-defined.
- The lift c_{2i−1} = t_i, c_{2i} = 0 is a parabolic cocycle, so τ is surjective.
- dim H_par = 2d: ΣW_i = V gives V^G = 0, the closure map has rank n, and the coboundary space has rank n.
- Aggregate claim: S(x, Σ_i N_i y) = −Σ_i h(τ_i x, τ_i y), which is definite on L_gen. Hence rank(ΣN) ≥ d, and since im N ⊂ ker τ with dim ker τ = d, we get im ΣN_pair = ker τ.

All of these steps agree with the note.

## 2. P2 exact tests (`test_p2p3.py`, `test_p2_random.py`, `test_p2_aggregate.py`)

| Case | n | m | Orders of r_i | dim W_i | d | dim H | S nondegenerate | Identity tests | Failures |
|---|---|---|---|---|---|---|---|---|---|
| order-3 reflections | 3 | 5 | 3 | 1 | 2 | 4 | yes | 224 + 168 random | 0 |
| order-6 reflections (eigenvalue −ω) | 3 | 5 | 6 | 1 | 2 | 4 | yes | 224 + 168 random | 0 |
| mixed, motion rank 2 | 3 | 5 | 4, 4, ∞, ∞, 3 | 2, 2, 2, 2, 1 | 6 | 12 | yes | 2016 | 0 |
| G34 W5 roots, order 2 | 6 | 10 | 2 | 1 | 4 | 8 | yes | 3456 | 0 |

- The W5 case reproduces the EDGEFLUX constant −1, which is a regression check against HCG-THM-EDGEFLUX.
- Twist versus formula: the twisted cocycle equals (1 − g_k)u(c) on e exactly, in every case.
- Negative controls:
  - Sign control (+h): rejected in every nonzero case (47, 47, 445 and 574).
  - Wrong inverse (r⁻¹ instead of r in τ): rejected 144/144 in the rank-2 case, and 166/166 (order 3) and 168/168 (order 6) on random cocycles.
  - On the complement-basis cocycles the wrong-inverse control was vacuous, because c_{2i} = 0 on most pairs. That is why the random-cocycle supplement was added.
- Aggregate: im(ΣN_pair) mod B¹ has rank d, and τ vanishes on it. Checked for order-3 (d = 2) and mixed (d = 6).
- **Order 4** was tested as a non-reflection unitary of motion rank 2. An order-4 *reflection* needs ℚ(i), so it is outside this K = ℚ(ω) engine.

## 3. P3 exact tests (`test_p2p3.py`)

| Tuple | Intervals | k values | dim Fix(C) | S identity | k²-control rejected | No-projector control rejected | N² = 0, (Ny)(c) = 0 |
|---|---|---|---|---|---|---|---|
| **G34 W5 actual tuple, intervals not aligned to pairs** | 7 | 2, 3 | 4–5 | 448/448 | 61/61 | 61/61 | 56/56, 56/56 |
| G(6,1,4), random monomial tuple, r = 6 | 7 | 3, 6, 9, 12, 18 | 0–1 | 1183/1183 | 21/21 | 13/21 | all |
| G(3,1,3), reflection tuple, r = 8 (product 1) | 7 | 2, 3, 6, 9 | 0–2 | 28/28 | 5/5 | 2/5 | all |

Notes on the controls:

- The no-projector control is not always rejected. When u(c) already lies in Fix(C), the projector does not change it. That is expected and does not count against the formula.
- When Fix(C) = 0, the prediction N_e = 0 held in all 6 such intervals.
- On W5, e = [2,3] and e = [8,9] give N = 0 although dim Fix(C) = 4. The reason is that u(c) ∈ W_{s} + W_{s′} = Fix(C)^⊥, so Π_C u(c) = 0. This is consistent with the formula.

**Total failures across all tests: 0.**

## 4. Corollaries A2 and A3 and the cut formula (`test_A23.py`)

- A2 and A3 follow algebraically.
  - Write the cut sum as f(I) = Σ_{a∈I} R_a − Σ_{a≠b∈I} C_ab.
  - The second difference over [i,j], [i+1,j], [i,j−1], [i+1,j−1] kills the part that is linear in the indicator. Of the quadratic part it keeps only the ordered pairs (i,j) and (j,i).
  - With B = −½f this gives Δ²B = C_ij.
- Exact results:
  - On W5 and NEW01: A2 holds for all i; A3 holds for all 45 pairs; the cut formula holds on all subsets of size ≤ 3.
- **Consequence, as ChatGPT also states.** span(intervals) = span(all subsets) is an identity, not an empirical phenomenon. The rank ρ_all is therefore a root-data invariant. The tree-compatibility obstruction is the separate question.

## 5. Proposed dispositions (Claude)

| Item | Proposed state | Scope |
|---|---|---|
| §A cut formula, A2, A3 | CHECKED (A1 is a restatement) | Algebraic; exact on W5/NEW01 (cut formula previously also on W6) |
| §B P2: inverse unitary pairs, S(x, N_e y) = −h(Στ x, Στ y), dim H = 2d, im ΣN_pair = ker τ | **CHECKED** | Algebraic statement for unitary r_i with ΣW_i = V over the stated K, for intervals made of whole consecutive pairs. Exact tests on orders 2, 3, 4 (non-reflection), 6 and infinite order. **No geometric realisation is claimed.** Infinite-order r_i are pure algebra, not finite covers. |
| §C P3: finite-order boundary projector, S(x, N_e y) = −k h(Π_C u_x(c), Π_C u_y(c)), N_e = T_e^k − 1, N_e² = 0 | **CHECKED** | Algebraic, for any single interval with C of finite order. Exact on real G34-W5 data (k = 2, 3) and on G(6,1,4) and G(3,1,3) (k up to 18). |
| Note's caveat "no common L or τ automatically across curves" | agreed | See §6 |
| Literature priority of P3 (DW / Völklein) | OPEN | Not assessed here; R0 reading item |

## 6. Consequence for R1 (PROPOSED, not checked by ChatGPT)

Non-pair-aligned curves on the *same* W5 tuple produce nonzero quasi-unipotent N_e: k = 2 or 3, with nonzero S-values in §3. Their forms −k h(Π_C u(c), ·) are generally **not** of the shape h(F_e(τ·), F_e(τ·)). They therefore need not factor through τ, i.e. they can lie outside Φ(Herm(L)), the space that bounds every pair-containing tree.

So the NEW01 fixed-order obstruction (7 dimensions available, 6 attainable per planar pair-tree) does not automatically survive when the H4 search admits pants trees that are not pair-containing. Two things would need checking first, before any use:

1. The (H0)–(H3) conditions, which are no longer automatic for such trees: commuting, common I, isotropy.
2. Whether Severn's Prop 4.2 setting admits k > 1 boundaries.

Proposed R1 sub-question: *is ρ for mixed trees (pair-containing curves plus finite-return curves) on NEW01 equal to 16?* Engine support now exists.

## 7. Files

| File | SHA-256 |
|---|---|
| generic_engine.py | 66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505 |
| test_p2p3.py | 2add5f38eac3cab2110784cc44f9c8e5f3b703f8c7fa456acf1b521f9f08e8e1 |
| test_p2_random.py | dac64f1d31b385eb3a0817b52c5e5943917941c87b82c2d46dce5336a278cb94 |
| test_p2_aggregate.py | b6bdf8754a4073ee29ffbb96abbf51c8b9b7ba09d779c03bdb27d420167b74d1 |
| test_A23.py | c71521e2e909da15509617b7a8b167a0afa8086807f26526015b88ceae5a055c |
| test_p2p3_out.txt | 7fbb84fb273a3a1c11f766299e577f3b25dc8dc57b6160b6947a6389d7b79ec4 |
| test_p2_random_out.txt | 6dbbe22a2c70944ed1ea0d22c1dcc469e644b6eee023b936a1b2668a3f338db5 |
| test_p2_aggregate_out.txt | 1bd462841d7413bd04b21c0e7575c2f3b55e0583543a66d221eea80af373933f |
| test_A23_out.txt | cf4eb33584e65a9d692ffd485827012ef413d497e556907c2bd4f32b8d0793f6 |

**Reproduce:**

```
python3 test_p2p3.py; python3 test_p2_random.py; python3 test_p2_aggregate.py; python3 test_A23.py
```

Pure Python with `fractions`. The run takes about 5 min here; the input roots are read from `roots_alt_5.json` and from `BLIND_INPUT/NEW01_roots.json`.

No novelty claim. No consequence for the algebraicity of Weil classes. HCG v0.1 ADOPTED is unchanged.
