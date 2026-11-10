# HCG — NEW02: projected-span prefilter reproduced; full-rank mixed tree found and certified (Claude) v0.1

**Date:** 23 October 2026 · **Status:** Claude computation, PROPOSED pending ChatGPT peer replay. PI decides. INTERNAL (SG-10): not for the blind auditor.
**Inputs:**
- `HCG_LAMINAR_H0H4_CHATGPT_REVIEW_v0_1.md` (4a634118…), read in full. The ZIP and the prefilter JSON were not received.
- NEW02 roots from the frozen blind input: d166a844…, which matches ChatGPT's stated hash.

## 1. Prefilter (ChatGPT §4) reproduced independently

`new02_mixed_search.py` uses Claude's arithmetic. It does not use ChatGPT's code.

| Family | Count | Exact Q-span rank |
|---|---|---|
| pair-aligned, unprojected cuts | 45 | **15** |
| all proper cuts, projected forms d·h(P F_J ·, P F_J ·) | 170 | **16** |

Both numbers agree with ChatGPT's values. Proposed state: **CHECKED** (two implementations).

## 2. H0 structure and search

H0 test per triangle (i < j < k) of the 20-gon, with A = g_{i+1}⋯g_j and B = g_{j+1}⋯g_k:

c(A) + c(B) + c(AB) − 12 + 2 dim(Fix A ∩ Fix B) = 0.

- **1138 of 1140** triangles pass.
- A DP count gives **474,632,697** H0-valid triangulations.
- **Uniform sampling** of 3000 triangulations: the rank histogram peaks at 10–11, and only one sample reached 15. A random tree is almost never full rank.
- **Flip-walk search:** simulated annealing over H0-preserving flips, with mod-(2⁶¹−1) ranks and seed 7. It found 3 rank-16 trees in 13 restarts, each re-verified as exact Q-rank 16.
- By the laminar reduction (HCG-ALG-LAMINAR-H0H4, now CHECKED by both AIs), H0 together with rank 16 suffices algebraically. Even so, the witness below was checked operator by operator.

## 3. NEW02-MIXED-01: operator-level certificate (`reconstruct_generic.py`, Severn §4 definitions, Claude engine)

Curves:

```
[1,12],[1,14],[2,11],[2,12],[3,4],[3,6],[3,11],[5,6],[7,8],[7,10],[7,11],[9,10],[13,14],[15,18],[15,19],[16,18],[17,18]
```

| Check | Result |
|---|---|
| Laminar; pants count | yes; 18 |
| (H0) | all 18 defects 0 |
| (H1) | 289/289 products are zero |
| (H2) | dim I = 4, isotropic, killed by every N_j |
| (H3) | every β_j ≤ 0; Σβ_j has signature (0, 4, 4), so it is definite on H/I |
| **(H4)** | **Q-rank 16** |
| Q-relations | one: N_[16,18] = N_[17,18] |
| τN_j = 0 | all 17 |
| Return data | k = 3 on [2,11]; k = 2 on [2,12], [3,11], [7,11], [15,19]; **[16,18] has ord(C) = 2 but k = 1** |

The last row is the first case observed in practice where the P3 power and Severn's k differ. The exact scaling N̂ = (ord C/(k m)) N holds there with factor 2. Every m_j = 1.

**Only 6 original pair curves remain:** [3,4], [5,6], [7,8], [9,10], [13,14], [17,18].

## 4. Consequence

- NEW01 and NEW02 both have full-rank (H0)–(H4) trees on their **unchanged** fixed tuples, once mixed laminar trees are admitted.
- In both cases the earlier obstructions were specific to the pair-containing class.
- Of the blind-challenge tuples, all four (NEW01–NEW04) now have certified full-rank trees in the fixed marking. NEW03 and NEW04 already had them in the pair-containing class.
- **No universal existence theorem is claimed.**
- Open R1 question: is there a tuple in the paired G34 component with **no** H0-valid full-rank laminar tree? The toy example rules out every pair-preserving subset-tree for its own data (6 < 9), but it has not been retested with mixed trees.

## 5. Dyadic intake (ChatGPT `DYAD_LH2012_CHATGPT_PEER_INTAKE_v0_1.md`, 3a28be99…)

Accepted:
- **The all-order filtration argument for the formal log** (Δ = F̃* − Id raises the z-order by at least 3). It, rather than my degree-7/8 symbolic test, is the proof that higher terms do not touch the Briot–Bouquet coefficients. My symbolic test is evidence only.
- **The refinement** that "at most six non-summable directions" holds per lifted branch, not as a common set.
- **Recording:** a separate Dyadic SESSION note with explicit dependence on LH2012 Cor 5.2. OPEN 20 unchanged; owner decides.

## 6. Files (SHA-256)

| File | SHA-256 |
|---|---|
| new02_mixed_search.py | 75e8779e49d4fe3042a2dfb05351d38d1cd024ec163a574900b4a986a824739e |
| search_NEW02_out.txt | 99271e374ce53810c6ef92bd35273d06c366e0973e6b0b5dc050ac86fe4192b5 |
| NEW02_search.json | 534e9774d060638a99ad59a8d99fafedccb094bb1604cdc049483777b845523f |
| flip_search.py | 1a21a97200e30cf26418fae973158220e5fb646de790b8b43f07f69bc63aa326 |
| flip_NEW02_seed7_out.txt | 5162354f5206f280d112e67e3e60e1c8b1e27ccb2b4d459ec2fdb78f39b6dac1 |
| NEW02_flip_hits.json | a0c6ba34799b2e87e6ae7da72c3fb4ad27ca71bd7914ad5e9158431008cbc58e |
| reconstruct_generic.py | dbb0b5146ea3311ae78e6cd8074ace1f67af03329eac56cf547597daf474c8f6 |
| reconstruct_NEW02_out.txt | eb16c661a5214488440bcd2dc244f0ae2b55e7000b985988cd50bb5155863706 |

Engine: `generic_engine.py` (66f2c253…).

**Reproduce:**

```
python3 new02_mixed_search.py 20261023 NEW02 3000
python3 flip_search.py NEW02 7 600
python3 reconstruct_generic.py NEW02 '<curve JSON>'
```
