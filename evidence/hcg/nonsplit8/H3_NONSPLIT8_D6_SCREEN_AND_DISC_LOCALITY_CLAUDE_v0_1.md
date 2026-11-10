# HCG — Claude check of ChatGPT's d = 6 group screen, and a discriminant-locality finding that bears on it v0.1

**Date:** 29 October 2026 · **Status:** Claude review (one AI) of ChatGPT's three SESSION claims, plus Claude's own PROPOSED result. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27).
**Inputs:** `HCG_NONSPLIT8_MINIMAL_RANK_GROUP_SCREEN_v0_1.md` (received copy); package `HCG_NONSPLIT8_GROUP_PRIORITY_REPRO_v0_1.zip` (5ee120ff…; manifest 4/4; `g34_intermediate_cover_probe.py` replayed: PASS lines reproduced).

## 1. ChatGPT's three claims — all CHECKED (Claude)

**(a) d = 6 reflection-group reduction.** Σ_j c_j = 2d + 8 = 20 and N ≥ 19 give ε = Σ(c_j − 1) ≤ 1. N = 20: all c_j = 1, all local monodromies are (complex) reflections. N = 19: one c_j = 2, and g_exc = (product of the other 18)^{−1} lies in the group they generate. Either way σ(G) is an irreducible rank-6 finite complex reflection group. By Shephard–Todd the rank-6 irreducible ones are G(m,p,6) (monomial, excluded for n ≥ 4 by Severn v1 §8), S₇ and W(E₆) (rational characters), and G₃₄. So the *image* is G₃₄ up to conjugacy; G itself may be a central extension. **Correct.** This does cancel, at d = 6, my Δ25 caveat about groups merely containing reflections. Note the reflections may a priori have any order; for G₃₄ they have order 2.

**(b) Intermediate covers.** Recomputed from the ten W5 roots alone (`g34_orbit_counts.py`, no archive data): orbit of v₁ under the reflections has 756 vectors, 126 lines; each reflection fixes 270 vectors (243 two-cycles) and 46 lines (40 two-cycles); Riemann–Hurwitz for 20 reflections gives g = 1675 for the 756-sheet cover and g = 275 for the 126-sheet cover. Frobenius: σ occurs in K[G/Stab(v)] since v ∈ σ^{Stab(v)}; it does not occur in K[lines] since ωI (central, in G₃₄) fixes every line and acts on σ by ω. **Correct.** (The explicit-F¹ problem on a genus-1675 curve is still unsolved; the point is only that genus ~1.6·10⁸ is not forced.)

**(c) Scalar-extension exclusion.** For G = ⟨W, ωI⟩ with W real: an element ω^a w, a ≢ 0 (mod 3), has fixed space = the ω^{−a}-eigenspace of the real matrix w, of dimension ≤ d/2, so codimension ≥ ⌈d/2⌉. G/W ≅ ℤ/3 (W ∩ ⟨ωI⟩ = 1 since ω^{±1}I is not real), the quotient classes of a product-one tuple sum to 0, so at least two local elements lie outside W. Hence ε ≥ 2(⌈d/2⌉ − 1), which exceeds 2d − 11 for d = 6, 7, 8, 9 (4 > 1, 6 > 3, 6 > 5, 8 > 7) and fails at d = 10 (8 ≤ 9). **Correct**, with exactly the stated scope.

Also: products of two distinct G₃₄ reflections have order 2 (45 of the 125 partners of s₁) or 3 (80); so the N = 19 data are exactly Severn v1 Rem 6.3's two "further class data" (bireflection of order 2, rotation of order 3). Both classes are real (s_i(s_i s_j)s_i = s_j s_i), so (L) holds for them by Thm 5.1.

## 2. New finding (Claude, PROPOSED): the discriminant appears to be a local invariant, and it is split for every d = 6 datum we can form

**Scan** (`g34_disc_scan.py`, 31 s): [det h] of H^1_par (Lemma 7.2 form) for the nine 20-reflection G₃₄ tuples at hand — W5, W6, W7, NEW01–04, BLOCK-01, ESCAPE — is **[1] in every case** (det h = 3^k or 3^k/4). For the nine 19-point data obtained from W5's paired tuple by merging one adjacent distinct pair into g = s_i s_{i+1} (seven rotations of order 3, two bireflections of order 2): **[1] in every case**, signature (4,4).

**Locality test** (`g333_disc_locality.py`): random product-one generating tuples of reflections,
- G(3,3,3) (one reflection class): N = 8 (dim 2): 60/60 tuples give [−1] (signature (1,1)); N = 10 (dim 4): 60/60 give [1].
- G(3,1,3) (three reflection classes: order 2, diag(ζ), diag(ζ²)): for each of six local-class multisets, 80/80 tuples give one and the same class; the class varies with the multiset ((0⁴,2⁶) gives [−1], the others [1]), and the sign is exactly (−1)^q from the Chevalley–Weil signature.

This is numerical evidence for Severn's "Theorem W" (v2 Rem 2.8, from his notes, used there only as a cross-check): [det h] = [(−1)^n Π_j Δ(g_j)] with Δ(g) a class attached to the conjugacy class of g. **Consequence if it holds:** for one-class reflection data, [det h] = [Δ(s)^{20}] = [1] on *every* Hurwitz component, so ChatGPT's Priority P1 (a nonsplit 20-reflection G₃₄ component) is impossible; for the N = 19 data, [det h] = [Δ(g)] for the rank-2 class, and the merged examples show [Δ(rotation)] = [Δ(bireflection)] = [1], so P2 is split as well. Then **no d = 6 datum is nonsplit**, and HCG-OPEN-NONSPLIT8 moves to d ≥ 7 (ε ≤ 3), where the scalar-extension lemma already removes the simplest families up to d = 9.

**Status of the locality statement:** PROPOSED, not proved. Severn's Rem 2.8 cites it as a global formula from the author's notes; no proof is in v2, and I have not derived it. Evidence: 9 + 9 G₃₄ data, 120 G(3,3,3) tuples, 480 G(3,1,3) tuples, all consistent. A proof (or a counterexample) is the decisive next step: it decides d = 6 outright.

## 3. Proposed dispositions

| Item | State |
|---|---|
| d = 6 ⇒ reflection-generated image, G₃₄ | CHECKED (two AIs) |
| 756- and 126-sheet covers, genera 1675 and 275; σ occurs only in the 756 action | CHECKED (two independent computations) |
| Scalar-extension exclusion for d ≤ 9 | CHECKED (two AIs) |
| G₃₄ discriminants: all 20-reflection tuples at hand and all merged 19-point data are split | `[ALG cert]` PROPOSED (Claude); ChatGPT replay invited |
| Discriminant is a function of the local classes (Severn "Theorem W") | PROPOSED conjecture with numerical support; **proof wanted** |
| Research steer | If Theorem W is proved, d = 6 is closed negatively and P1/P2 are dropped; the search moves to d ≥ 7 with the ε-budget and the exclusions above |

## 4. Files
`g34_disc_scan.py` / `_out.txt`, `g333_disc_locality.py` / `g333_disc_locality_out.txt`, `g313_disc_locality_out.txt`, `g34_orbit_counts.py` / `_out.txt` (hashes in SHA256SUMS.txt).
