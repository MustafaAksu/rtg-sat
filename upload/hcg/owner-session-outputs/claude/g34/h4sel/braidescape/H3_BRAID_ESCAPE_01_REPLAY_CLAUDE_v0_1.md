# HCG R1 — Independent replay of G34-BLOCK-01-BRAID-ESCAPE-01 (Claude) v0.1

**Date:** 23 October 2026 · **Status:** Claude replay of ChatGPT's PROPOSED witness. PI decides. INTERNAL (SG-10): not for the blind auditor.
**Input:** `HCG_G34_BLOCK_BRAID_ESCAPE_01_CERTIFICATE_v0_1.json` (44030b5f…). Its `original_roots` are identical to Claude's frozen G34-BLOCK-01 roots (71a030ce…).
**Independence:**
- Engine: Claude's `generic_engine.py` only.
- Braid action: written here from the stated Artin convention. Inverse-letter and cocycle-transport formulas were derived here from u(xy) = u(x) + ρ(x)u(y).
- Not used: the ChatGPT engine, ChatGPT's transport matrix P, the pair-move macros or the modular filter.
- Used from the certificate: only the 868-letter word, the roots and the 17 curves.

## 1. Braid replay (`replay_braid.py`)

| Check | Result |
|---|---|
| Word length | 868 |
| Strand permutation | identity (pure) |
| Final matrix tuple equals the paired reflections of `final_roots` | **yes** |
| Inverse word returns the original tuple | yes |
| 8 H-representatives and 6 coboundaries, transported letter by letter | valid parabolic cochains; coboundaries remain coboundaries; the 8 stay independent mod B¹ |
| Cup form | **S_init(x, y) = S_fin(Tx, Ty)** on the 8×8 basis, exactly |
| Final roots: K-rank; A3 deletion ranks | 6; all ten equal 6 (A3 holds; it failed at the start) |

## 2. Target tree (`reconstruct_target.py`, Severn §4 definitions)

Curves:

```
[1,2],[1,4],[1,6],[1,12],[3,4],[5,6],[7,8],[7,12],[9,10],[9,12],[11,12],[13,14],[13,18],[15,16],[15,18],[17,18],[19,20]
```

- (H0): 18/18 zero.
- (H1): 289/289.
- (H2): dim I = 4, isotropic, killed by every N_j.
- (H3): every β_j ≤ 0; the sum has signature (0, 4, 4).
- **(H4): Q-rank 16.**
- Only relation: N_[1,4] = N_[1,2] + N_[3,4].
- Every ord C = k = m = 1, and τN = 0.

All of this matches ChatGPT's certificate.

## 3. Disposition

| Item | Proposed state |
|---|---|
| HCG-ALG-G34-BLOCK-BRAID-ESCAPE-01 | `[ALG cert]` **CHECKED** (ChatGPT production; Claude independent braid, transport, cup and H0–H4 replay) |
| HCG-ALG-BLOCK-A3-NONINVARIANT | CHECKED: A3 fails at the start and holds at the end of an explicit pure braid |
| HCG-COR-BLOCK-NOFULL | CHECKED; fixed standard-interval marking only |
| Interpretation | The G34-BLOCK-01 obstruction is a property of the marking, not of its pure-braid orbit (ordered Hurwitz component). The rank-8 bound stands for its restricted family. |
| Component identity with W5 / Severn / NEW01–04 | OPEN |

**What R1 now looks like.** Every fixed-marking obstruction we have met so far — pair-containing selection, NEW02's ceiling of 15, and the repeated blocks — has been overcome by enlarging the curve class or by braiding. The toy's mixed obstruction is still fixed-marking only; it was never braided. Two natural next questions:

1. A theorem-level question: is every pure-braid orbit of a generating G34 tuple of this type guaranteed a full-rank pair-containing marking?
2. Braid connection of the new witness to W5's component.

## 4. Files (SHA-256)

| File | SHA-256 |
|---|---|
| replay_braid.py | see `SHA256` below |
| replay_braid_out.txt | see `SHA256` below |
| reconstruct_target.py | see `SHA256` below |
| reconstruct_ESCAPE01_out.txt | see `SHA256` below |

The values are recorded in `SHA256SUMS.txt` in the package.
