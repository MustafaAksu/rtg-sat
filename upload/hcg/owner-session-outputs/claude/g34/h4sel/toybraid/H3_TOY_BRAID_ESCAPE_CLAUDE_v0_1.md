# HCG R1 — The toy obstruction is also escaped by a pure braid (Claude) v0.1

**Date:** 23 October 2026 · **Status:** Claude result, PROPOSED pending ChatGPT replay. PI decides. INTERNAL (SG-10): not for the blind auditor.
**Prompt:** ChatGPT P1 (`HCG_G34_BRAID_ESCAPE_PEER_INTAKE_CHATGPT_v0_1.md`): test whether the toy's fixed-marking ceiling (6 < 9) survives pure braids.

## 1. Search (`toy_braid_bfs.py`)

**Search space.**
- Paired tuples (r₁, r₁, …, r₆, r₆).
- They are reached from the toy by the two adjacent pure pair-conjugations (ChatGPT's local identities):
  - (s, s, t, t) → (tst, tst, t, t), word σ₂σ₁σ₁σ₂;
  - (s, s, t, t) → (s, s, sts, sts), word σ₂⁻¹σ₃⁻¹σ₃⁻¹σ₂⁻¹.
- The root lines form a 9-line orbit; the group is G(3,3,3).

**Scoring.**
- Each state is scored by the best of the 14 pair-containing planar trees, using the EDGEFLUX edge forms on L.
- Arithmetic is mod p with p ≡ 1 mod 3, for search only.

**Result.**
- Start: best rank 6, consistent with the block bound.
- BFS reached rank 9 after **4 pair moves**, having explored 310 states.
- Final line tuple: (0, 3, 8, 5, 2, 2). One repeated line remains.

## 2. Certificate (`toy_braid_certify.py`, `reconstruct_toy.py`; Claude engine, actual operators)

Artin word, 16 letters:

```
4,3,3,4, -4,-5,-5,-4, 8,7,7,8, 6,5,5,6
```

| Check | Result |
|---|---|
| Pure (strand permutation) | identity |
| Final tuple paired, matching the predicted lines; inverse returns | yes; yes |
| Cocycle transport: images are cocycles; cup preserved exactly | yes; yes |
| Target tree: [1,2], [3,4], [5,6], [7,8], [9,10], [11,12], [3,10], [5,10], [7,10] | laminar, 10 pants |
| (H0) | all zero |
| (H1) | 81/81 |
| (H2) | dim I = 3, isotropic, killed by every N_j |
| (H3) | every β_j ≤ 0; the sum has signature (0, 3, 3) |
| **(H4)** | **Q-rank 9 = d²**; no relations |
| Return powers | all ord C = k = m = 1; τN = 0 |

## 3. Meaning

- The toy's mixed-tree ceiling of 6 is also a **property of the marking**.
- A 16-letter pure braid gives rank 9 with an ordinary pair-containing tree. The "block coalescence" that caused the obstruction is undone by conjugating pairs.
- So every fixed-marking obstruction found so far has been escaped within its pure-braid orbit:
  - pair-containing selection;
  - NEW02's ceiling of 15;
  - G34 blocks;
  - the toy.
- The P1 question therefore points toward a positive structural statement, not a counterexample:
  - *conjecture (heuristic, not claimed)*: every pure-braid orbit of a product-one, generating, paired reflection tuple with dim H = 2d has a pair-containing marking of rank d².
- A proof would need an argument that pair conjugations can always separate parallel classes (c_* = m) and resolve compatibility. No such argument is offered here.
- Archival fix: the replay package `H3_BRAID_ESCAPE_REPLAY_v0_1.zip` has been rebuilt with `cert.json` (44030b5f…) included.

## 4. Proposed dispositions

| Item | Proposed state |
|---|---|
| HCG-ALG-TOY-BRAID-ESCAPE-01 (new) | `[ALG cert]` PROPOSED (Claude); ChatGPT replay invited |
| HCG-ALG-TOY-MIXED-OBSTRUCTION, HCG-ALG-TOY-BLOCK-LEMMA | CHECKED; fixed-marking scope stressed |
| Pure-orbit full-rank existence | OPEN; a heuristic conjecture is recorded and not claimed |

## 5. Files (SHA-256)

| File | SHA-256 |
|---|---|
| toy_braid_bfs.py | e1cf941a278c31bb3f6d63b72b4c112ba944789f711e1157da8957d88587eae5 |
| toy_braid_bfs_out.txt | 88ca4c262130264a82adedac1c7853999eab554a9e09bde9442cf55468948179 |
| toy_braid_found.json | 1ef9f32abbc5c874eb2231ad5d3af59f2b4b4d3ea48616de1c2033f71bdd1dfd |
| toy_braid_certify.py | 7705c5290cf0174eeb039d32f7f233fd75477eca9b68b1e6cc97b75b41883a54 |
| toy_braid_certify_out.txt | 8a6bf92530dafa0272f8eec2ce2d781218e2c4d2bc31dba4c816284fe66674f6 |
| toy_final.json | 5645e5e1ffc12efe63b672f81bcbcc0a4603665137469fb1d7f90e73dbe80d39 |
| reconstruct_toy.py | 5ca93bd897f67aa210159661a277d57e6c399d64fd840bfca25ccc52b0acb1f3 |
| reconstruct_TOYESC_out.txt | 59557a56d4fffe1453ca186d056c991dcfdd18cb899cdc0e4c9a1003e252944d |

Dependencies, included in the package:
- `generic_engine.py`
- `braidescape/replay_braid.py`, for its `act()` function
- the toy roots (01918b05…)
