# HHO PR #78 — independent exact Witt graph cross-check (ChatGPT)

**Date:** 2026-11-16. **Status:** [SESSION — ALG/NUM] receiving scientific review, NOT PI adoption, register promotion or a test of dominance (D).  
**Owner head inspected:** `9de64ea48327dddc3b7a1da52fe420e657205a8f`. Current governing HHO source is adopted `hho-v0.4`; HCG `hcg-v0.5` was inspected for W5 geometry, while the HHO scientific pin remained `hcg-v0.2`.  
**Reading extent:** Full `HHO_WITT_GATE_PREREGISTRATION_CLAUDE.md` (§§1–5) and `HHO_WITT_GATE_RESULTS_CLAUDE.md` (§§1–4), full original 266-line Claude Python script and 19-line output, HCG source W5 certificate's root vectors and curve intervals (targeted), HHO `g616.py` (complete, 51 lines), and HCG `hcg-v0.5` §§6.14–6.15 and §6.23 (targeted). Neither Severn nor the external admissible-cover LMHS sources was read first-hand.

## 1. Preregistration and source identity

**[SESSION — structural CHECK]** The Git history of PR #78 records `656e8857f5727deeae9961a7a11e67fa207faabb` at 2026-11-16 12:51:34Z with the **pre-fixed** Catalan(18) planar family, source paths/hashes, predicted W5/W6/W7 certificate `w=4`, predicted P1–P3 `w<=3` and class-[5] F20 `w<=3`. The run commit `9de64ea` at 12:56:47Z descends immediately from that prereg and **does not modify the prereg file**. This establishes Git ordering; it does not independently prove no exploratory computation occurred before the prereg was committed, and the prereg was **not sent for an external review before the run** (disclosed by the preparer).

**[SESSION — source hashes CHECK]** Source W5 SHA-256 `172766a91017aeac62e5c299a72b2c7582b0bb186c4feaa8b1906144eafb952e`; HHO `g616.py` SHA-256 `b07a560a751a3dd3871fb0397efc8dfe97776beb678160ba07f7b56f27baff7a`. Both equal the pinned identities in §3 of the prereg. Claude's script/output SHA-256 `656fff29ada8470b06958514271c0f1505202f4840f845171fbbbed85d09839a` / `315580fe64681813ce6b5b3deb8f2dbbf14660d1e59a1112eee90b12bf41cac6` also match repository content. A reported byte-identical replay by Claude is a *same-engine replay*, distinct from the independent checks below.

## 2. Independent graph-Witt algorithms and results

**W5: exact characteristic-zero Q(omega) implementation.** From the ten source root vectors, construct twenty reflections using `s_v=I-(2/h(v,v))v bar(v)^t`, `h(v,v)=6`; check product-one. With Python `fractions.Fraction` pairs for Q(omega), independently form every ordered interval product, compute `dim V^{g_arc}` and common invariants of two consecutive interval products by row-reducing their (g-I) matrices, then optimize the graph Euler sum over every binary interval partition. The original HHO/HCG cup and Witt code is not imported.

**[NUM — SESSION] W5**: `min w=max w=4` over the **477,638,700 planar trees**, via exact DP. Direct evaluation of the recorded balanced tree: edge-fixed dimension sum **102**, vertex-fixed dimension sum **98**, so `w=4`. Exact rank calculations visited 170 interval cases and 1140 vertex-split cases. All assertions PASS.

**G(6,1,6): independent monomial method.** Build the five recorded tuples P1–P3 and Q0/Q2 from the literal source reflection specifications, but represent each matrix by a permutation of six coordinates and six phases in `Z/6`. For every pair of interval products, compute the invariant dimension by a **phase-labelled constraint graph**: a connected coordinate component contributes one fixed coordinate iff all induced phase constraints on its cycles are consistent. This avoids *all* Q(omega) matrix multiplication and Gaussian elimination used in Claude's implementation. A separate exact interval DP computes extrema, with direct reconstruction of minimizing and maximizing witness scores.

| Tuple | Source-reported class (not recomputed) | min w | max w | maximal witness edge sum | maximal witness vertex sum |
|---|---|---:|---:|---:|---:|
| P1 | [2] | 3 | 3 | 75 | 72 |
| P2 | [2] | 3 | 3 | 75 | 72 |
| P3 | [2] | 3 | 3 | 73 | 70 |
| Q0 | [1] | 4 | 4 | 76 | 72 |
| Q2 | [1] | 4 | 4 | 76 | 72 |

All five source cases have `N=20`, verified product one and no common invariant vector. The **Catalan(18) = 477638700** family is the set of leaf-labelled *planar interval* trivalent trees rooted at leaf N; the DP proves the exact extrema without physically listing that many trees.

**Coverage boundary:** W6, W7 and the three nonsplit F20 cases were **not independently recalculated in this review**; their values in PR #78 remain source-reported from Claude's one implementation. The independently verified cases are W5 and P1–P3/Q0/Q2. The source classes/signatures and the B1/polarization linkage were not recomputed; consistency is not proof of them.

## 3. Family and output review

**[THM — combinatorial]** A noncrossing trivalent tree with the cyclic leaf order `1,...,N`, rooted at the last leaf, is a binary bracketing of the first `N−1` leaves. The Catalan number is `C_(N−2)`; for N=20, `C18=477638700`. The interval products in each child bracket and their fixed-space intersection give precisely the vertex stabilizer invariants. There is no enumeration of the arbitrary (nonplanar) tree family or braid orbit.

**Minor N=4 enumeration presentation issue:** Claude's loop evaluates **two planar trees on the original marking plus two on the braided marking** (four reported values), while the prose calls these “the three trees.” It should explicitly identify/deduplicate the overlapping topology or instead say “four evaluations covering the three labelled topologies.” For the three reported class-[5] tuples all four source-reported values are zero, so this does not affect the stated maximum. Do not assert that those four values are four distinct trees.

**[OPEN] Reflection constancy**: The independently checked G(6,1,6) cases and W5 have `min=max`; this is a datum/family-specific finite result. The claim that all complex-reflection tuples have constant graph w, or that `max_T w` always equals the Witt index, is not proved and is false in the stronger split-F20 sense recorded by Claude. Avoid a general theorem.

## 4. Interpretation and disposition

**[OWNER: HCG hcg-v0.5 §6.23 / HCG-COR-BOUNDARY-WITT]** A nonsplit (4,4) coefficient Hermitian form has K-Witt index at most 3. Under the **semistable/admissible-cover LMHS** conditions of the source-reading note, the graph Euler quantity agrees with `dim_K W0`, which is K-isotropic. Hence the consistency prediction `w<=3` is correct. The *identification* with the boundary weight filtration remains source-conditional: the primary admissible-cover and monodromy-weight literature was not read in this review.

**Verdict:** **ACCEPT AS [SESSION]/[NUM] CONSISTENCY EVIDENCE** for the preregistered finite family, with an independent **exact** W5 and monomial G616 cross-check. Do not mark every output row as independently CHECKED: W6/W7 and F20 remain one-implementation in this review. No new HHO claim RID or status is inferred. The computation is **not a (D) dominance test**, imposes no obstruction P1, and does not change the scientific pin to `hcg-v0.5`.

**Proposed follow-up:** The owner may consume this evidence after review and integrate it with PR #78 as a single research-cycle closeout; any `hho-v0.5` register upgrade/re-pin is a *separate PI-authorized scientific edition*. For the next scientific step, investigate which hypotheses guarantee graph-w constancy across planar trees, rather than assuming it from the observed reflection samples.
