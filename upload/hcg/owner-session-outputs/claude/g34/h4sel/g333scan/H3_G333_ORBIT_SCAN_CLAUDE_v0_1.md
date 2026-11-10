# HCG R1 — Exhaustive G(3,3,3), m = 6 pair-conjugation orbit scan (Claude) v0.1

**Date:** 24 October 2026 · **Status:** Claude computation, PROPOSED pending ChatGPT replay. PI decides. INTERNAL (SG-10): not for the blind auditor.
**Protocol:** `HCG_G333_PAIR_ORBIT_SCAN_PROTOCOL_v0_1.md` (ChatGPT), with its correction applied: A3-failing nodes are kept as bridges.

## 1. A3 bridge example (ChatGPT)

`g333_a3_bridge_check.py` was run unmodified (`python3 -I`). Output: `ALL EXACT CHECKS PASS`.

One pure pair move turns the A3 deletion flags from (T, T, T, T, F, T) into all T, while the group stays at order 54. Disposition: **CHECKED** (replay of ChatGPT's own code; the arithmetic is independent of Claude's engine).

## 2. Orbit graph (`g333_orbit_scan.py`)

- **Nodes:** all 9⁶ = 531,441 line-tuples, where the 9 lines form the reflection orbit of G(3,3,3).
- **Edges:** both orientations of the adjacent pure pair-conjugation (s,s,t,t) → (tst,tst,t,t) and (s,s,t,t) → (s,s,sts,sts) at the 5 adjacent pair positions.
- **Components:** computed by union-find over the whole graph, before any A3 filtering.
- **Generation:** constant on each component; checked by matrix closure.
- **Ranking:** on A3-valid nodes, the best of the 14 pair-containing hexagon trees, using the EDGEFLUX forms (mod p).

| Quantity | Result |
|---|---|
| Components (all tuples) | 22 |
| Components generating G(3,3,3) (order 54) | **1**, with 522,720 tuples. The remaining 8,721 tuples do not generate it. |
| Components with a rank-9 witness | **1/1** |
| PAIR-SUBGROUP NEGATIVE CANDIDATES | **0** |

Full distribution over the generating component (exhaustive; two runs with identical counts):

| Best pair-tree rank | Nodes |
|---|---|
| A3 fails | 97,200 |
| 6 | 6,480 |
| 7 | 106,704 |
| 8 | 200,880 |
| **9** | **111,456** (about 26 % of A3-valid nodes) |

## 3. Witness certified by actual operators (`reconstruct_witness.py`)

- Line tuple: (0, 0, 1, 2, 5, 6). Tree: the six pair curves, plus [3,6], [3,8] and [3,10].
- (H0): 10/10.
- (H1): 81/81.
- (H2): dim I = 3, isotropic and killed by every N_j.
- (H3): Σβ has signature (0, 3, 3).
- **(H4): Q-rank 9**; no relations.

## 4. Meaning and scope

- **Result.** For G(3,3,3) with m = 6, every generating paired tuple lies in **one** pair-conjugation orbit, and that orbit contains full-rank markings. Within this setting, the question "can a non-real-character orbit fail H4 in all markings?" has the answer **no**.
- This is a finite classification for one group and one m. It does not cover G34.
- It also does not cover unpaired tuples. Pure-braid orbits contain unpaired tuples, but here a single pair-orbit already covers all generating paired tuples, so nothing more is needed for paired starts.
- **Ranking method.** Ranks were scored with the EDGEFLUX formula, which holds for paired tuples. The rank-9 claim for the component rests on the operator-certified witness in §3. The histogram itself is predictor-based.
- **Analogue for G34 (suggestion).** The same question for G34, m = 10, is far too large to enumerate. Two routes are possible:
  - a connectivity proof for pair-conjugation orbits, plausibly a known Hurwitz-orbit result for reflection tuples;
  - a random-walk density estimate.

## 5. Files (SHA-256)

| File | SHA-256 |
|---|---|
| g333_a3_bridge_check.py (ChatGPT, unmodified) | fc7945e2a4f6785648500f3951043334f9901da7d26ad7eb1781d0ed5952ccde |
| g333_orbit_scan.py | b6df59fd260f9865a64c7507481ce837ba43006c83c561a4b6958f327526552a |
| g333_orbit_scan_out.txt | 2ef44c22a9dd562095632308d845e9a6deab24cda5abaaa1bf68baf5445aaa94 |
| g333_orbit_scan.json | 513f907c9f286d5b64a796a6b744c338e3cd9871d68d48cf6012ab85af20de0a |
| g333_dist.py | 8dc82547b48f9f46ec89089d2bc100a5dee5173f45d901b09e72f9b3f9c3d419 |
| g333_dist_out_run1.txt | 909dbd6eb99c131d76f686c8cce5c7972a79e2c5747ddc06f9a1487c7d506ba3 |
| g333_dist_out_cached.txt (second run, same script) | 7751662e2be4fd0f11cd3613de930ed2e9dbeb990dbc65aa00d1e7542ec53f0d |
| witness_roots.py | 84e123640b004db592b791061e3795d05e51d024891015eee5cbd170811ce6c2 |
| g333_witness_roots.json | e91da6bfe75ef589028d7bd2f2f0033cc8ca4bb5c88d42e01bf2f9f2501e456b |
| reconstruct_witness.py | 71c1a4b0e61170a6eac3de9c0abfa60c262ed5c9bdb005b95c350d92bd091aa6 |
| reconstruct_SCANW_out.txt | c1da3ef33e43ea1114a7b03b7f5b7de8b7e07d35cd80200276c67ef5aa15170c |

Dependencies, included in the package: `toy_braid_bfs.py` (line orbit, action table and best-rank routine), `reconstruct_toy.py`, `generic_engine.py`, and the toy roots.

**Provenance note.** The distribution script that was actually run is the version without the conjugation cache; a planned cached rewrite was never saved. Both runs used the same file (hash above) and gave identical counts. The two output files differ only in the timing line.
