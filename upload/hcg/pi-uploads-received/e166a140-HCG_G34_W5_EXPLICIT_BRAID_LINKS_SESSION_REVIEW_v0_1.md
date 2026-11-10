# HCG G34 — explicit paired-braid links to W5 (SESSION v0.1)

Date: 2026-10-25  
Status: **PROPOSED SESSION exact certificates; independent peer review not yet performed on the new words**  
Scope: Six named inputs in the fixed 6-dimensional Eisenstein reflection representation of the Shephard–Todd group G34. No global Hurwitz-orbit connectivity claim.

## Decision

Five explicit **pure** Artin braids carry each of NEW01, NEW02, NEW03, NEW04, and G34-BLOCK-01 to the W5 baseline paired-reflection tuple, **as actual ordered reflection matrices**. A sixth pure braid connects the previously verified G34-BLOCK-01-BRAID-ESCAPE-01 endpoint to W5 by combining the inverse of its earlier 868-letter certificate with BLOCK-01 → W5. No simultaneous global conjugation, branch-point relabeling, or unoriented endpoint equivalence is needed. Root vectors are compared modulo multiplication by the six norm-one Eisenstein units, precisely the equivalence preserving their reflection matrices.

| Starting paired tuple | Local conjugations | Raw elementary braid letters | Freely reduced letters | Endpoint / inverse / purity | Matrix corroboration |
| --- | ---: | ---: | ---: | --- | --- |
| NEW01 | 29 | 796 | 776 | PASS / PASS / PASS | PASS mod 10007 |
| NEW02 | 29 | 500 | 450 | PASS / PASS / PASS | PASS mod 10007 |
| NEW03 | 37 | 916 | 916 | PASS / PASS / PASS | PASS mod 10007 |
| NEW04 | 33 | 852 | 850 | PASS / PASS / PASS | PASS mod 10007 |
| G34-BLOCK-01 | 39 | 892 | 880 | PASS / PASS / PASS | PASS mod 10007 |
| BLOCK-ESCAPE-01 | 868 inverse + 39 above | 1748 | 1748 | PASS / PASS / PASS | PASS mod 10007 |

The braid words, full source/target roots, and the local conjugation decomposition are in the respective `*_CERT.json` files. Words are **1-based Artin-generator indices applied left-to-right**. A negative index means the inverse generator.

## Sources and reading scope

1. `W5_BASELINE_ROOTS.json` and four `NEWxx_roots.json`: byte-preserved from `HCG_H4_HOLDOUT_VERIFICATION_v0_1.zip`, under `input/HCG_H4_BLIND_CHALLENGE_v0_1/`; the challenge protocol states that each 10-root input generates the full G34 (faithful order 39,191,040) and uses a common Eisenstein root chart. These are data, not an adopted theorem.
2. `BLOCK_roots.json`: byte-preserved `HCG_G34_BLOCK_01_ROOTS_v0_1.json`; the group order and the 2/4-block obstruction were previously independently assessed. This session uses the ordered ten-root input only.
3. `HCG_G34_BLOCK_BRAID_ESCAPE_01_CERTIFICATE_v0_1.json`: byte-preserved previous session certificate; supplies the original 868-letter pure braid BLOCK → BLOCK-ESCAPE.
4. Ben Severn, *Weil Classes on Every Abelian Sixfold of Weil Type for Q(sqrt(-3))*, author-hosted `2610.00387v1`, internal Draft v0.5 dated 2026-10-16: targeted §4, Proposition 4.2 Step 0 (page 8 of printed text), read and visually checked. It says the class-preserving permutation group is `S_20` in the G34 datum; full braid is sufficient for transporting the generic period-map rank even where ordered Hurwitz components differ. Its global sixfold claims remain externally CLAIMED, not settled by this calculation.
5. Wood, *An algebraic lifting invariant of Ellenberg, Venkatesh, and Westerland*, Theorem 3.1: relied on the *earlier independent source audit* for context only, **not needed in these explicit certificates**. No bound on the abstract stability constant M is asserted.

## Constructive mechanism and checks

With `s_v(x)=x-(1/3) h(x,v)v` in the displayed root normalization `h(v,v)=6`, all arithmetic is exact in `Z[omega]`, `omega^2+omega+1=0`. For an adjacent pair of pairs `(s,s,t,t)`, the local braid `(sigma_2, sigma_1, sigma_1, sigma_2)` sends it to `(tst,tst,t,t)` in the declared Hurwitz convention. Its mirror replaces the second pair by `(sts,sts)`. For distant pairs, a pair-swap prefix and its inverse move a conjugator next to the target, perform the pure local operation, and restore positions.

For each input and coordinate i=1,...,10, a breadth-first search finds a sequence of conjugations of the current i-th root by **other fixed coordinate roots** that reaches the i-th W5 reflection. Earlier corrected coordinates are never changed. The word builder then expands each conjugation into explicit Artin generators. This is a constructive **finite witness**, not a general algorithmic theorem that it always succeeds.

The primary verifier `verify_links_exact.py` does not use the discovery path search. It replays every elementary Artin generator directly on the complete 20-root tuple, checks all ten pairs remain paired at the end of each local operation, checks that non-target pairs stay unchanged, checks the final 20 reflection matrices by root-line identity, checks all 20 braid-strand permutation positions return to identity, and checks the inverse word recovers the original tuple. For the sixth link it additionally checks that the prior 868-letter certificate's output equals the composition input.

A second verifier `verify_matrix_modp.py` explicitly constructs **6x6 matrices** over `F_10007[omega]` and acts on those matrices using `R_a R_b R_a` under each Artin move; all six resulting tuples match W5. This is a cross-implementation corroboration. Characteristic-zero exact root/Artin replay, not a modular rank test, is the primary proof of the endpoint statement.

Reproduction from within this folder:

```bash
python verify_links_exact.py
python verify_matrix_modp.py   # numpy required; optional corroboration
python construct_links.py      # regenerate five primary source-to-W5 words
```

All three commands were executed successfully in this session. Source SHA-256 values and the checksums of each scientific output are in `SHA256SUMS.txt`; that manifest deliberately does not hash itself.

## Consequences, limits, and disposition

**[SESSION]** These six explicitly listed paired-reflection tuples lie in a **single pure B20 orbit of ordered reflection tuples** in the supplied root chart. In particular the previously open BLOCK-01 versus W5/NEW01–04 comparison has a positive concrete answer. By Severn Proposition 4.2 Step 0, the corresponding full-B20 component comparison is sufficient for the generic rank issue (D), **conditional on the identified data being realized in the intended Severn family and on his Proposition 4.2's other hypotheses**. No use of Wood's unknown 20-reflection stability threshold is required for the named witnesses.

This does **not** prove all generating 10-pair G34 tuples are connected, nor identify W5 with Severn's actual published Appendix A base tuple without inspecting an explicit connecting braid. It does not prove supplier algebraicity, global transfer, or Severn Theorem 6.2. Blind third-family reviewer Priority B remains isolated.

Recommended ledger: `HCG-ALG-G34-NAMED-PURE-BRAID-LINKS -> SESSION PROPOSED (exact witness and local exact replay PASS; independent second-family peer verification pending)`. Existing HCG adopted v0.1 should not be changed on this evidence alone.
