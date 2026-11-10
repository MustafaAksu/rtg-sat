# HCG — Severn deposited paired tuple ↔ W5: completed independent source-bridge audit v0.1

**Date:** 2026-10-25  
**Disposition proposed:** `HCG-ALG-SEVERN-APPXA-W5-LINK → CHECKED` in the narrowly stated paired-tuple / braid / basis-identification scope. This is a SESSION review, not HCG adoption.  
**Sharing:** INTERNAL. Do not transmit to the independent blind Priority B auditor.

## Decision

The only outstanding issue in the preceding PARTIAL audit was the identity of the reconstructed source matrices with Severn's *actual deposited paired tuple*. The file `tuple_pairs_D3.json` was supplied unchanged in this session and has SHA-256:

```
0021185d2111635f73d2b8c5b153c738015aef1c499394a0726a8b7ae72e5711
```

This agrees **in full** with the source pin that had been recorded in the independent handoff. All twenty `6×6` input matrices were read directly as `Q(omega)` coefficient pairs; no code from Severn's companion archive was executed.

The source matrices, under the already pinned **invertible** `P ∈ GL_6(Q(omega))`, coincide **entry-for-entry, for 20/20 positions**, with the source tuple reconstructed backwards from W5 using the recorded braid certificate. Therefore the remaining provenance-dependent *algebraic equality* is established:

\[
P M^{\rm supplied}_i P^{-1}=M^{\rm reconstructed}_i, \qquad i=1,\dots,20.
\]

With the certified 618-letter pure Artin braid, this identifies the supplied Severn Appendix-A paired tuple and W5 in the same **pure braid orbit, after a global linear change of basis**.

## Source identity and reading extent

| Input | Reading/check | SHA-256 |
|---|---|---|
| User-supplied `tuple_pairs_D3.json` | Full 20 matrices, parsed as untrusted data; exact equality to frozen certificate | `0021185d2111635f73d2b8c5b153c738015aef1c499394a0726a8b7ae72e5711` |
| `H3_SEVERN_LINK_v0_1.zip` | Targeted entire `severn_to_w5.json`, `W5_BASELINE_ROOTS.json`, review and manifest | See included original manifest |
| User-supplied `best_pairs_D3_D1.pkl` | SHA-256 only; **never deserialized** | `629df3f2d9eeb3904194a428af99b80e788560c1797e9eee428163e6c7dbc498` |
| `parab.py`, `cert.py`, `kfield.py` | Targeted, static inspection only; not executed | In accompanying hashes |
| `cert_rerun.log`, `out_D3.json` | Targeted reading; source-reported results, no computational replay of the author's campaign | In accompanying hashes |

**External provenance limit:** We verified the byte SHA against the frozen prior pin and the metadata recorded in Claude's earlier Zenodo source reading. An independent retrieval of the remote Zenodo record and its MD5 statements **was not completed in this environment**. Hence this report says *user-supplied, pinned Severn source bytes*, not an independently re-downloaded external source.

## Exact `Q(omega)` verification

Conventions: `omega^2+omega+1=0`, elements represented as rational pairs `(a,b)` meaning `a+b omega`; Artin generators are numbered 1–19 and applied left-to-right.

1. `P` is invertible; exact two-sided inverse identity `P P^{-1}=P^{-1}P=I_6`.
2. The source tuple contains twenty `6×6` rank-one involutions in consecutive identical pairs. Its product is `I_6`.
3. Applying `P M_i P^{-1}` to the *actual uploaded* twenty source matrices matches the independently reconstructed twenty reflection matrices from the W5-root certificate, **20/20 exactly**.
4. The braid word has **618** Artin letters and consists of **25** recorded pair-conjugation operations; final strand permutation is the identity.
5. Applying the 618-letter word to the conjugated source tuple produces the twenty W5 reflection matrices. The inverse word recovers the original tuple. All these comparisons use exact rational Eisenstein arithmetic through the reflection model.
6. Altering the sign of the first Artin generator destroys the target equality (negative control).

The earlier PARTIAL verifier had reconstructed its source only by reversing the braid, so its successful forward replay was insufficient to identify the *deposited* tuple. Step 3 above now uses the real independently supplied JSON and removes exactly that circularity.

## Separate matrix-level replay

A second script reads the original twenty input matrices, reduces coefficients modulo **10007** (where `t^2+t+1` is irreducible), conjugates by `P`, and performs **all 618 Hurwitz updates directly on dense 6×6 matrices**. It does *not* derive the braid moves from roots or use the P2/P3/EDGEFLUX predictions.

Results:

- Input tuple is paired, consists of non-identity involutions, and has product `I_6`: PASS.
- Input-to-target matrix-level braid: **20/20 PASS**.
- Inverse braid: **20/20 PASS**.
- Wrong-sign first-letter negative control: **REJECTED**.

The finite-field replay is an independent algebraic crosscheck, not a substitute for the exact source-to-reconstructed-matrix comparison.

## Consequence and limitations

**[SESSION — CHECKED, proposed register grade]** Via this `P`, the supplied Severn Appendix-A *paired tuple*, W5, NEW01–04, G34-BLOCK-01, and BLOCK-ESCAPE-01 are in one connected pure-braid class, where the latter named links retain their previously CHECKED certificates. This is stronger than the full-braid connectivity required by Severn's one-class Step 0, conditional on the associated family identification.

This does **not** replay Severn's separate original-gate-to-paired **90-move** word. It does **not** verify the global geometric realization or spread/compensation step of his paper; no status change to PO-6 or Priority B is implied. Severn Theorem 6.2 remains *CLAIMED*, not established by the present result. No files in adopted HCG v0.1 or RTG's canonical DSNs have been modified.

## Reproduction

```
python source_verified_braid_check.py
python direct_matrix_hurwitz_modp.py
```

Both use the original `tuple_pairs_D3.json` at `/mnt/data/tuple_pairs_D3.json` when run from the current shared sandbox; the packaged `replay.py` supplies a relocatable arrangement when run from an extracted ZIP. The first script copies exact-arithmetic functions from the preceding independent PARTIAL audit (authored in the ChatGPT session), then adds a direct source-file equality test. The second is a separate finite-field matrix implementation.

**Acceptance criterion met:** source hash verified; source matrices loaded unchanged; exact `P` equality verified for **20/20**; braid purity, endpoint and inverse verified. Recommend closing Δ22's source-identification dependency as `CHECKED`, retaining the above boundaries.
