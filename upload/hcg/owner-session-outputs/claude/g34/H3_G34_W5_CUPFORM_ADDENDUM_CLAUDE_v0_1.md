# H3 — G34 W5: cup-form robustness and monodromy diagnostics (Claude) addendum v0.1

**Date:** 21 October 2026 · **Responds to:** ChatGPT W5 review and ledger delta (CHECKED proposals) · **Status:** SESSION-ALG, PROPOSED

## 1. Review of ChatGPT's W5 checks

The three checks were read at code level. There is no mathematical disagreement.

- **Braid rebuild (strongest check).** The 17 T_j are reproduced exactly from elementary Artin moves σ_i. I checked the cocycle transformation line by line: u′(g_i) = u₀ + g_i u₁ − (g_i g_{i+1} g_i⁻¹)u₀ and u′(g_{i+1}) = u₀. It is correct.
- **(H0) is structural.** The H0 check infers trivial boundary products from interval parity; it does not multiply matrices. My engine computes the products and the pants contributions explicitly, so the conclusion is unchanged.
- **Cup form: same principle.** ChatGPT's "independent" cup formula is a pair-specialization of the same relative-fundamental-class construction I derived. It is algorithmically independent but not independent in principle. This matters because (H2) and (H3) are statements about the true intersection form.

## 2. Attempted principle-independent validation of S

**Idea.** If the monodromy-invariant sesquilinear forms on H¹_par have ℚ-dimension 2 (that is, K·S), then the true intersection form is a rational multiple of S. In that case (H2) holds as stated and (H3) holds up to one global sign, which (H3) allows.

**Results on tuple #5.** S is invariant under every element computed, about 300 of them in all:

| Element set | Size | Invariant forms, dim_ℚ | Non-commuting pairs |
|---|---|---|---|
| Balanced-decomposition twists | 17 | 34 | — |
| Interval twists, lengths 2–6 | 85 | 34 | — |
| Pair half-twists + all interval twists | 197 | 34 | — |
| β·twist·β⁻¹, random β of length 2–6 | 24 | 34 | 0 |
| β·twist·β⁻¹, random β of length 10–40 | 40 | 34 | 0 |
| Targeted search for new adjacent equal reflections | 600 braids tried | — | no element outside I₀ |

All computed elements commute, and all (T − 1) map into one 4-dimensional subspace I₀.

**This is not a model defect.** The same cocycle and braid model, run on toys where the answer is known (script `toy/toy_monodromy.py`), gives **non-abelian** monodromy:
- Z/2 with 6 points (hyperelliptic genus 2): 634 non-commuting pairs.
- Paired S₃ tuple: 128 non-commuting pairs.

The G₃₄ phenomenon is a **sampling limitation**:
- A pair (s,s) has trivial total monodromy, so moving it as a block acts trivially.
- New Picard–Lefschetz vanishing cycles need *new* coincidences of equal reflections at adjacent positions. With 126 reflections, random braid words essentially never produce them.
- The full monodromy is non-abelian, as Deligne semisimplicity requires for a polarized VHS. It is simply not reached by random sampling.

**Conclusion.** The uniqueness argument is **not completed**. Evidence for S being the intersection form is now:
1. derivation from relative group cohomology (Claude), reproduced by ChatGPT's specialization from the same principle;
2. S is well defined, skew-Hermitian, nondegenerate, with h of signature (4,4) as Hodge theory requires;
3. S is invariant under every monodromy element computed (about 300).

A principle-independent check remains open. Two routes:
- (a) implement the published Dettweiler–Wewers parabolic Poincaré-duality formula and compare;
- (b) construct explicit braids that create new equal-reflection coincidences, giving non-commuting Picard–Lefschetz elements, and redo the uniqueness test.

## 3. Proposed statuses (PI decides)

| ID | Status |
|---|---|
| G34-B-COH | CHECKED |
| G34-C-W5 matrices + braid rebuild | CHECKED |
| G34-C-W5 (H0)–(H4) | CHECKED, conditional on S being the intersection form, i.e. CUP-FORM-VALIDATION OPEN (route a or b) |
| G34-D geometric bridge | REVIEWED-OUTLINE / OPEN |
| H3-PO-5 | CONDITIONAL-HOLD |
| H3-FRONTIER-01 | HOLD |

## Files (SHA-256)
- `g34_w5_invariant_forms.py` 90077351dd99933666dca2e6b7f2db7e46a9e28fcd167bfce5a6ab341c61648e
- `g34_w5_invariant_forms_full.py` 216ee98b4f0a15952acafb2ec064378686b42949a5a14a35a01db5fcdb1f4d77
- `g34_w5_invariant_forms_full2.py` fc76772c6a2eebf156edc1d80622068040482859a6de420e9e6ada6ff1f81992
- `g34_w5_monodromy_forms.py` 5400431171bdc890de214d7bb7b1f6408c3c7d6a9e676dd5367be169b61b150e
- `g34_w5_braid_crosscheck.py` 7b1db2aa2931bab42c9ce1c9281d5573d931ff5f16f559ae0c3d0e69bc001c93 (crossing-interval twists: closed formula equals elementary braids)
- `g34_w5_monodromy_targeted.py`, `toy/toy_monodromy.py` (hashes in the delivery message)
