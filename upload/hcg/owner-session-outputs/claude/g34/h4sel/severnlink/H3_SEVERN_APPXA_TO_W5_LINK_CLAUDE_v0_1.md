# HCG — Severn's deposited Appendix-A paired tuple braid-linked to the session W5 chart (Claude) v0.1

**Date:** 25 October 2026 · **Status:** Claude result, PROPOSED pending ChatGPT replay. PI decides. INTERNAL (SG-10): not for the blind auditor.

## Source (pointed to by the PI)

**Record.** Zenodo record 10.5281/zenodo.23422649: B. Severn, *Weil classes on every abelian sixfold of Weil type for Q(√−3)*, v0.5, published 16 Oct 2026 (the page notes that a newer version exists). This is the Zenodo deposit of hexagon:2610.00387v1.

**Downloaded files.** MD5 values match the record page:

| File | MD5 | SHA-256 |
|---|---|---|
| `weil-sixfolds-qsqrt3-certificates.zip` | 2b53c79c… | 3a39a346… |
| `.pdf` | a811d105… | 5bc6a282… |
| `.tex` | c41c8719… | 68095102… |

**Deposited manifest.** `certificates/g34-d3/SHA256SUMS` checks out: all 42 files OK.
- `D/tuple_pairs_D3.json` has SHA-256 0021185d2111635f…, which **matches the prefix printed in the paper's Appendix A**.
- `best_pairs_D3_D1.pkl` has 629df3f2…, which also matches.

**Handling.** The archive was treated as untrusted data. None of its code was executed; only the JSON tuple was read.

## Checks (`severn_link.py`, Claude code)

1. **Sanity of Severn's tuple.** Severn's 20 matrices (in his own basis):
   - each has order 2, with rank(1 − m) = 1;
   - their product is the identity;
   - the tuple is paired, (s₁, s₁, …, s₁₀, s₁₀).
2. **Linear intertwiner P ∈ GL₆(K).**
   - Found by backtracking on the pairwise product orders of 6 independent Severn reflections, against the session's 126 G34 reflections (generated from the W5 roots).
   - A linear solve P r = o P then gave a one-dimensional solution space with P invertible.
   - **All 10** conjugated reflections P sᵢ P⁻¹ lie in the session's reflection set.
   - No Galois twist was needed.
3. **Pure braid to W5.**
   - Method: coordinate-wise pair-conjugation BFS (the same rule as Δ21), expanded into Artin letters.
   - Matrix-level replay result: **25 pair moves, 618 letters**.
   - Checks: endpoint is exactly the W5 paired tuple; strand permutation is the identity; the inverse word returns to the start.

## Consequence and scope

- **Connected set.** Under the linear identification P, Severn's certified Appendix-A paired tuple, the session W5 baseline, NEW01–04, BLOCK-01 and BLOCK-ESCAPE-01 lie in **one pure-braid orbit** (via Δ21).
  - By Severn Step 0 (Σ = S₂₀) they lie in the same component of H/Σ.
  - This closes the open item "W5 ↔ Severn Appendix A" (Δ21).
- **Choice of identification.** Other σ-compatible identifications differ by the linear normalizer of G34. Such a change acts on all tuples at once, and the period-map rank question is invariant under it. No claim is made about outer automorphisms.
- **Not checked here:** Severn's 90-move word from his original (gate) tuple to the paired tuple. His own T8BW check covers it, and it was not re-run; only the paired tuple is used.
- **What this does not do:** it is not a check of Severn's geometric chain, of PO-6, or of Priority B. Severn Thm 6.2 remains CLAIMED.

## Files

| File | SHA-256 |
|---|---|
| `severn_link.py` | see SHA256SUMS.txt |
| `severn_link_out.txt` | see SHA256SUMS.txt |
| `severn_to_w5.json` (P, word, pair moves) | see SHA256SUMS.txt |

Dependencies: `build_links.py`, `replay_braid.py`, `generic_engine.py`, and the W5 baseline roots (all included). Severn's tuple must be fetched from the Zenodo record; it is not redistributed in this package.
