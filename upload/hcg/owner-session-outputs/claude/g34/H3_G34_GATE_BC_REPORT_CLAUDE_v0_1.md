# H3 — G34-B/C: parabolic cohomology, boundary monodromy and (H0)–(H4) (Claude) v0.1

**Date:** 21 October 2026 · **Status:** PROPOSED (single-AI derivation); ChatGPT cross-check requested. **PO-5 is not closed:** G34-D, the geometric bridge, is still open.
**Independence:** We used no Severn code, tuple, certificate or braid word. Our inputs are our own K₁₂-based G₃₄ (gate A), our own paired tuples, our own cup-form derivation and our own decompositions. The one exception is the *Severn-shaped* interval pattern in §4, which we tested only as a control.

## 1. Model and conventions (derived here)

**Local system.** The fundamental group is π = ⟨g₁,…,g₂₀ | g₁⋯g₂₀ = 1⟩, with ρ(g_i) = s_i, the reflections of our paired tuple (s₁,s₁,…,s₁₀,s₁₀). The s_i are unitary for h_W(x,y) = Σ x_k ȳ_k on K⁶.

**Parabolic cocycles.** A cocycle u is determined by values u(g_i) = a_i v_i, since im(s_i − 1) = K v_i. They satisfy:
- closure: Σ_i Q_i a_i v_i = 0, where Q_i = s₁⋯s_{i−1};
- coboundaries: a_i = −2h(w,v_i)/h(v_i,v_i).

**Cup form, from relative group cohomology.**
- The relative fundamental class is Z = Σ_k [P_{k−1} | g_k], with ∂Z = Σ_k [g_k]; P_k = g₁⋯g_k.
- The relative lift is α_k with u(g_k) = (s_k − 1)α_k, i.e. α_k = −(a_k/2)v_k.
- The form is

  **S(u,u′) = Σ_k h_W(u(P_{k−1}), P_{k−1}u′(g_k)) − Σ_k h_W(α_k, u′(g_k)).**

- The correction sign was fixed by requiring S to be well defined on cohomology. A hand proof (telescoping) shows S is invariant under coboundaries in both slots and under the choice α_k ↦ α_k + (fixed vector). The script confirms both exactly.

**Dehn twist** along a curve around consecutive points a..b: φ(g_i) = c g_i c⁻¹ for a ≤ i ≤ b, with c = g_a⋯g_b. The monodromy is T = (u ↦ u∘φ^k), where k is the exact return power ρ∘φ^k = ρ, i.e. the pointed family. Then N = log(T^m), with m the semisimple order. One global orientation convention is used throughout.

**Cross-check of the implementation.** The fast twist formula u(c^k g c^{−k}) = u(c^k) + C^k u(g) − g·u(c^k) and a direct free-group word evaluation give identical results on two full decompositions.

## 2. G34-B results (tuple #0, the gate-A generators)

| Check | Result |
|---|---|
| closure rank / coboundary rank / dim_K H¹_par | 6 / 6 / **8**. Independently confirms ChatGPT's B0 reduction. |
| S vanishes on coboundaries, both slots | True |
| S skew-Hermitian, nondegenerate | True, True |
| h = ϑS (ϑ = √−3): Hermitian, signature | True, **(4,4)** |
| det h | 2,125,764 = 2²·3¹², a norm, so the class is **[1]** (split) |

Other tuples give det h = 3¹² or 3¹³. These values depend on the basis but are always norms, consistent with Severn's remark that his values (3⁶, 3⁷, 3⁸) are basis-dependent norms.

## 3. G34-C on tuple #0: a systematic (H4) shortfall (informative negative)

- Precomputed: all 187 interval curves [a,b] with 2 ≤ length ≤ 18. Return powers k ∈ {1,2,3}; every twist is unipotent (m = 1).
- Tested 1500 distinct random interval pants decompositions: **1499 pass (H0)–(H3); none pass (H4).** The ℚ-span of the N_j ranged over 7–15 and was never 16.
- Comb decomposition: span 14. Balanced decomposition: span 14.
- **Control, Severn's interval pattern** ([1,8],[1,18],[2,8],[3,8],[4,8],[5,6],[5,8],[7,8],[9,10],[9,12],[9,16],[9,17],[9,18],[11,12],[13,14],[13,16],[15,16]) applied to *our* tuple #0: (H0)–(H3) pass, span **14**. His certificate uses *his* braid-moved tuple, so this is not a contradiction.

## 4. G34-C on other tuples: an independent passing witness

We ran six further paired tuples, from our own random generating 10-sets of reflections, with the comb and balanced decompositions.

| Tuple | comb ℚ-span | balanced ℚ-span |
|---|---|---|
| #1 | 13 | 14 |
| #2 | 13 | 12 |
| #3 | 11 | 11 |
| #4 | 15 | 14 |
| **#5** | 15 | **16** |

**Witness W5 = tuple #5 with the balanced decomposition** (pairs, [1,4], [5,8], [9,12], [13,16], [1,8], [9,16], [1,16]):
- **(H0)** All boundary products are 1. Every pants contribution vanishes: (s,s,1) gives 1+1+0−12+2·5 = 0, and (1,1,1) gives 0−12+12 = 0.
- **(H1)** N_j N_k = 0 for all j,k.
- **(H2)** I = Σ im N_j has K-dimension **4**, is totally isotropic, and N_j(I) = 0.
- **(H3)** Every β_j is negative semidefinite, with signatures (0,1,3), (0,2,2) or (0,4,0); Σβ_j has signature **(0,4,0)**, i.e. definite.
- **(H4)** The ℚ-span of the N_j is **16 = n²**.
- All k_j = 1 and m_j = 1.

The full exact certificate (roots, cocycle basis, Gram of S, every T_j and N_j) is in `g34_cert_tuple5_balanced.json`. A verifier can recheck (H1)–(H4) from these matrices with different code, without running ours.

**Reading.** If the geometric bridge holds, W5 gives (D) for the Hurwitz component containing tuple #5. By the transfer theorem, together with (L) (Brauer, Thm 3.1, a property of the class datum) and d = [1], this would give Severn's Theorem 6.2(1) **independently of his tuple and code**. The many failing witnesses are consistent with Remark 4.3: failure of one decomposition proves nothing. They do show that a passing certificate is fragile, so W5 needs an independent recheck.

## 5. What is still open before PO-5 can be CHECKED

1. **ChatGPT cross-check of W5:**
   - recompute (H1)–(H4) from the JSON with different code;
   - ideally, recompute T_j and N_j from the definitions for tuple #5 with a different cohomology model;
   - audit the cup-form derivation (§1), the correction sign, and the twist convention.
2. **G34-D bridge, not done:**
   - Lemma 4.1: braid pullback equals Gauss–Manin monodromy (Dettweiler–Wewers), applied to *our* conventions;
   - the balanced maximal degeneration lies in the closure of tuple #5's component;
   - the CKS nilpotent-orbit step of Prop. 4.2.
   
   All twists here have k = 1, so no central-root ambiguity enters.
3. **Third model family / human referee.** Severn's chain was produced and audited by Claude and OpenAI models, so the PI's acceptance should involve a reviewer outside both families.

## 6. Proposed statuses

| ID | Status |
|---|---|
| G34-B (dim 8, S well defined and skew-Hermitian, signature (4,4), class [1]) | PROPOSED (Claude); B0 dimension now confirmed by both AIs |
| G34-C witness W5 (tuple #5, balanced): (H0)–(H4) all pass | PROPOSED; independent recheck requested |
| G34-C negative data (tuple #0, 1500 decompositions; tuples #1–#4) | RECORDED (non-decisive) |
| G34-D geometric bridge | OPEN |
| H3-PO-5 | OPEN; strong progress: an independent exact witness exists, pending cross-check and bridge |
| H3-FRONTIER-01 | HOLD |

## Files and SHA-256
- `g34_gateB.py` — engine `324f11e8f826c0c7b92fe0402406d861fd05409124f63286c96fe77bbd8a50c5`
- `g34_gateC_search.py` `fb8ad8417fe18304908415ef20374f797313f3ab54c4600f75ef92cefaa57321`; result `g34_gateC_search.json` `1353cfc35bb4c4f291dea27876a7778dfa056ce2452941afe09b10967417fb4e`
- `g34_gateC_stats.py` `f011c06191f88007293a4b185d915c80fc867bd46066af666c87c00c1abc67cf`
- `g34_gateC_alt.py` `efc5aaccdf02a213569637f4a51759ad23235e78246dd2959ac7d9a946b9ef2c`
- `roots_alt_5.json` `480cd6dc95f1a802943a621df632693eeb9aa7e8a9057ff5099e444950c9e35a`
- `g34_gateC_tuple5_log.txt` `6ce8a2dc3a2b8d83143518d8abb7af8d438896b18a64973ed20195281294b3a1`
- `g34_cert_tuple5_balanced.json` `172766a91017aeac62e5c299a72b2c7582b0bb186c4feaa8b1906144eafb952e`
