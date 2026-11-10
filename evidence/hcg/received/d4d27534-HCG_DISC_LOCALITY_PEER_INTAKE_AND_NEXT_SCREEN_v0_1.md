# HCG — Peer intake: discriminant locality, d=6 closure, and next screen

**Date:** 29 October 2026  
**Status:** Internal scientific review, not PI adoption.  
**Basis:** Claude's uploaded proof review v0.1 and archive; the previous ChatGPT v0.1 proof and reproducibility package. No adopted HCG or RTG file was edited.

## 1. Decision

Recommend the following evidence/review states, with PI adoption kept separate:

| Claim | Scientific/review recommendation | Limits |
|---|---|---|
| HCG-THM-PARABOLIC-DISC-LOCALITY | THM; CHECKED by two independent proof reviewers | Fixed positive K-Hermitian coefficient space, unitary product-one tuple, no common fixed vector, even parabolic dimension; not an eigenvalue-only statement |
| HCG-ALG-G34-RANK2-LOCAL | CHECKED | Exact finite census plus imported Steinberg pointwise-stabilizer theorem and classical completeness of the 126-reflection list |
| HCG-COR-D6-NONSPLIT-NOGO | CHECKED, CONDITIONAL | Requires the adopted-in-session d=6 image reduction including monomial exclusion, cup-to-induced-polarization comparison, and the splitting criterion in the prescribed signature |
| HCG-CONJ-DISC-LOCAL | Superseded by the proved statement, subject to PI recording | Preserve its historical status/evidence |
| HCG-OPEN-NONSPLIT8 | OPEN; d=6 negative closure is available at the scope above | Does not exclude d>=7, other fields or other geometric constructions |
| Severn v2 A/B/C | CLAIMED, unchanged | No human referee report or new theorem-wide adoption |

The determinant proof, not empirical constancy across sampled tuples, supports the component-independent d=6 result.

## 2. What was actually replayed here

The source report was read in full. Both new producer scripts were inspected before execution. Only two literal path values were redirected in scratch copies; no mathematical code was changed.

- `disc_locality_proof_check_claude.py`: all 17 cases passed, including all nine merges, odd-n sign control and nonidentity coefficient Gram with determinant 68364. Output SHA-256 `985138c194851db60714c1700ede95978a2f4cf7539c394c8b3955d993f09dd4` equals the supplied log byte-for-byte.
- `g34_rank2_plane_census_claude.py`: all 7,875 pairs checked; 2,835 two-line planes and 1,680 three-line planes. Local products 144 and 81. Output SHA-256 `746e8a4db0fd0f46ed06cd22ec916b810bfff038baa86b9850d3e193c225c744` equals the supplied log byte-for-byte.
- Previous source scan with W6 and W7 inputs now supplied: **9/9 named paired tuples and 9/9 W5 merges** re-executed, all eight-dimensional, signature (4,4), class [1]. The completed output is included.
- W6 and W7 independently checked with the earlier ChatGPT triangular-cochain implementation, not generic_engine: determinants 1/12 and 3 in its newly chosen bases, both class [1], all full-block identities passed. Claude's coordinate choices give 19683/4 and 2187. The determinant ratios are 3^10=N(3^5) and 3^6=N(3^3), respectively; no contradiction or matching-basis assumption is involved.
- The 320-case random campaign was **not rerun** in this intake. Its previous outputs and the peer replay are historical evidence; rerunning unchanged random tests is not needed for M1–M6 or the two missing inputs.

These producer replays do not constitute a third independent implementation. Independence is the earlier ChatGPT implementation versus Claude's separately written proof checker/census. The new two-input check uses that existing independent ChatGPT engine.

## 3. Archive integrity and a nonblocking packaging qualification

The prior ChatGPT archive has 40/40 valid manifest entries. The new Claude ZIP has 23 manifest lines: **10 correspond to delivered artifacts and all 10 match**; the remaining 13 point to historical external-workspace files not in that ZIP. Two delivered files use a manifest path alias (`cg_locality/replay_claude_log.txt` and `../dsn/...`); their delivered basename copies were matched explicitly. No incorrect delivered-file hash was found.

The new report's standalone upload is byte-identical to the ZIP copy. Its SHA-256 is `41bc9997328cbc74a592ba9a899fd6cc30eb6e71656cc284c591ff05ac1878ee`. The generic engine used in replay was recovered from the earlier complete archive and has the producer-pinned SHA-256 `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505`. No new upload is needed for these calculations.

The new self-contained delivery includes both source archives and a replay driver with explicit path handling. It does not claim 23/23 self-contained validation for the producer ZIP.

## 4. M1–M6 disposition

A separate `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md` preserves the v0.1 theorem and equations but clarifies:

- M1: E_i perpendicular = ker(1-g_i), direct sum, invertibility and preimage independence.
- M2: det(g_i|E_i)=det(g_i|V).
- M3: rationality belongs to the product of b_i and is proved before interpreting its norm class.
- M4: coefficient scaling and root-basis scaling do not alter the determinant class.
- M5: fixed-point theorem attributed to Steinberg, with Lehrer's subspace formulation and limited actual source-reading stated honestly.
- M6: the 126 distinct computed order-two reflections exhaust the classical total of 126; this completeness is an explicit imported classification datum.

No additional draft iteration is requested for the peer's immutable report. A minor wording point in its transported test should be read as `T in GL_6(K)`, not a rational matrix: the supplied code has nonzero w-coefficients. The matrix H0=T^t conjugate(T) has rational determinant 68364, which is a K-norm but not a rational square. The exact test itself is valid and stronger than a rational-only change of basis.

## 5. Source verification extent

This intake did not reread the entire DW or Steinberg proofs. Lehrer's publisher abstract and indexed Theorem 1.1 support the classical subspace-stabilizer statement. Full PDF download/render requests failed. Bessis, arXiv:math/0610777v5, Table 2 (p.58), lists 126 reflections and G34 degrees; the extracted entries were inspected, but rendering failed. The official Magma classification list confirms G36=W(E7) as the rank-seven exceptional case. These are external classical inputs, not new HCG results.

## 6. Next research step

Stop d=6 tuple generation for the prescribed nonsplit target. The class is fixed by local data, so changing braid component cannot bypass the obstruction.

The next exact budget is epsilon <= 2d-11; it specializes to epsilon <=3 at d=7. A separate PROPOSED note reduces the d=7 rank profiles to three candidates after the same monomial and character-field exclusions:

    1^18,2,2;    1^17,2,3;    1^16,2,2,2.

This deduction is new in the present response and remains PROPOSED for independent review. It does not assert that a group, tuple, nonsplit discriminant, (L), or a dominant family exists. Local class data should be screened before constructing parabolic cohomology or F1.

## 7. Scope-preserving record action

Add this receipt, the peer review, D-10 and the clarified proof to pending HCG v0.3 evidence. Do not overwrite the accepted v0.2, the original v0.1 proof, the historical sampling report, or any RTG owner document. PI approval of the pending record and human refereeing remain separate.

## 8. Replay-run limitation

All four underlying checks completed individually in the current session. The later monolithic clean-directory replay hit an outer execution limit after the proof checker had passed; the fresh source-scan stage likewise exceeded that outer limit. The fresh census and fresh W6/W7 stages passed, including exact output matching. The successful original individual source scan is preserved. Therefore this note does **not** assert a completed one-command fresh replay of the entire delivery. No failed mathematical assertion was observed in the interrupted calls.
