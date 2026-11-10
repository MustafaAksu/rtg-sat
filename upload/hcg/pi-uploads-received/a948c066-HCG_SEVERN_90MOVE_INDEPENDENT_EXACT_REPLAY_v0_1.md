# HCG — Independent exact replay of Severn's original-to-W5 G34 tuple chain

**Date:** 2026-10-25  
**Status:** SESSION / CHECKED — bounded algebraic braid-chain identity; not an owner adoption or a validation of the geometric transfer proof.  
**Confidentiality:** Internal HCG work; not for the blind Priority-B reviewer.

## Decision

The previously open ChatGPT-side source-replay obligation for the 90-move braid is **CLOSED**.
The original deposited 20-matrix tuple is mapped **entry-by-entry, 20/20**, by the deposited 90-letter braid to the deposited paired tuple. The inverse word restores the original tuple. The full next leg, using the already-reviewed explicit `P` and 618-letter braid, also maps the deposited paired tuple to the frozen W5 reflection tuple **entry-by-entry, 20/20**, in exact arithmetic over `Q(omega)`.

## Source inventory and reading extent

- Newly supplied archive: `weil-sixfolds-qsqrt3-certificates.zip`, SHA-256 `3a39a346ed98f0ff11c6fcf4efdf72ad8e72ef4ff72cf983b5c4e4c46c684134`.
- Source owner documentation inspected: `certificates/g34-d3/README.md` (full) and `T8BW/ref-T8BW-report.md` (full). Archive is attributed by its README to the transfer-paper v0.12 certificate record; that statement is metadata, not independently verified publication/adoption status.
- Source data read as inert bytes/text, not executed:
  - `tuples/g34_tuples.g`: SHA-256 `aebab6f41ae749c8f586d2666e025c0b9d7ee2c09156bc39fa9dd6912c2709e6`; unique record with datum `[[7,20]]`.
  - `T8BW/braid.txt`: SHA-256 `50f53f5be29b05d931d0bb3e83f5114cc08f9d5264b852f9c2391d4a96bd30ff`; 90 positive generators.
  - `D/tuple_pairs_D3.json`: SHA-256 `0021185d2111635f73d2b8c5b153c738015aef1c499394a0726a8b7ae72e5711`; 20 matrices.
  - `g34-d3/SHA256SUMS`: all **40/40** entries verified directly against source ZIP bytes.
- Second-leg **candidate certificate data**, taken unchanged from the prior ChatGPT source-bridge archive: `severn_to_w5.json` (`P` and 618-letter word) and `W5_BASELINE_ROOTS.json`. These inputs were independently *checked* against the original first-leg source in this session; this work does not claim to have rediscovered `P` or the word.
- Other archive sources, such as GAP/Python/Sage scripts, were **not executed**. The `.pkl` was not deserialized. This verification concerns the tuple chain, not the other theorems advertised in the archive.

## Exact algorithm and independent verification

`verify_exact.py` is an independent restricted GAP-scalar parser accepting only rationals and `E(3)`, `E(3)^2`; it reconstructs the 20 matrices from the `[[7,20]]` record without evaluating GAP code. Field arithmetic is exact in `K=Q(omega)`, `omega^2+omega+1=0`. Every braid generator acts **left to right** by

`(g_i,g_{i+1}) -> (g_i g_{i+1} g_i^{-1},g_i)`;

all tuple entries are rank-one involutions, so `g_i^{-1}=g_i`.

Exact results:

| Test | Result |
|---|---|
| Original 20 rank-one involutions | PASS |
| Original product of 20 matrices = identity | PASS |
| 90 positive generators; original -> deposited paired | **20/20 PASS** |
| Inverse 90 steps restores original | PASS |
| Original -> paired strand permutation | Nontrivial (not pure) |
| Change of basis `P` and inverse | Exact PASS |
| Deposited paired -> W5 with 618 letters | **20/20 PASS** |
| Inverse 618 letters restores transformed paired tuple | PASS |
| Paired -> W5 strand permutation | Identity (pure) |
| Corrupt one letter in each braid | Both rejected |

The independent replay used no GAP, Sage, original Severn computational code, Claude `generic_engine.py`, or earlier ChatGPT engines. The original archive is treated as untrusted input.

## Scope and limitations

**[SESSION]** The algebraic chain

`Severn original --(90, full braid)--> Severn paired --(P, 618, pure braid)--> W5`

is **CHECKED**. Together with previously checked W5-to-NEW01/02/03/04/BLOCK/ESCAPE pure-braid certificates, this fixes the named tuple-chain connection under Severn's `Sigma=S_20` framework, **subject to the geometric realization and family hypotheses of that framework**.

This session **did not** independently calculate the original tuple's generated group order `39,191,040` (the archive and Claude's previous independent computation report it), or redo the W5 cup/period map, PO-6, Priority-B supplier/spreading/compensation, or Severn Theorem 6.2. These remain governed by their separate evidence and their existing statuses; Severn Theorem 6.2 remains **CLAIMED**, not established by this chain replay.

## Replay

The attached source/data subdirectory permits a self-contained run without other mounted files:

```
python verify_exact.py
python verify_full_chain.py
```

Both scripts write structured JSON result files. Script imports are standard-library only and neither script executes source code from the uploaded archive.
