# HCG — Independent change-focused audit of the degree-44/45 exclusion

**Date:** 2026-10-30  
**Provenance:** `[SESSION]`; mathematical review, not HCG adoption.  
**Inputs:** Uploaded Claude `H3_D43_WEIL_REVIEW_AND_D44_D45_CLAUDE_v0_1.md` and `H3_D43_WEIL_REVIEW_CLAUDE_v0_1.zip`.  
**Governing HCG source:** v0.2 ADOPTED; this report does not modify it. The hypotheses `(H)`, prior checked Lemmas A′, B, C, E, F, S, and the reflection-free and tensor budget results are inherited with their existing scope.

## Decision

1. **d=44 and d=45 are excluded under the inherited HCG nonsplit-dominance assumptions (H),** conditional on the external Hiss–Malle classification and the certified character-table facts. Recommend **CHECKED — source-conditional**. This advances the necessary lower bound from d>=44 to **d>=46**, not a construction at d=46.
2. **r=22 in the two-block Lemma B is rigorously within the checked range.** The numerical gap is strict, `20 > 18`; the finer 4-block pattern fails `E_4=-22`.
3. GAP's 68 reported exclusions are **68 output lines, not necessarily 68 distinct irreducible representations**, because L2(43) is reported both in the library loop and in explicit generic-family checks. Character eigenvalue computations in this turn were not rerun from primary table data; the executable GAP source and its frozen log were read and checked, and the separate Python budget checks rerun.

## I. Source identity, structure and computational scope

- The uploaded ZIP's SHA-256 matches the declared `103fac3c...e06e`.
- `BUNDLE_SHA256SUMS.txt`: 9/9 PASS.
- `d44_45_closure_claude.py`: rerun with Python isolated mode; produced the byte-identical source output.
- `gap/d44_45_screen.g`: read in full. Its classwise fixed-space multiplicity is `sum_{k=0}^{o-1} chi(g^k)/o`, which is the standard finite-order projection formula. Its condition `ClassPositionsOfKernel(chi)=[1]` selects faithful irreducibles. Character fields are compared to `CF(3)`. It enumerates the named quasisimple tables and separately the generic SL2(43)/SL2(89) and their PSL2 quotients.
- `gap/d44_45_screen_out.txt`: 68 verdict lines, all excluded. The independent audit script parses every line and verifies the thresholds for fields Q and K. No independent GAP installation or independent derivation of the underlying 459 CTblLib tables is claimed.
- Primary source targeted reading: Hiss–Malle 2001 *Low-Dimensional Representations of Quasi-Simple Groups*, Theorem 1, §6, generic Table 2; Hiss–Malle 2002 *Corrigenda*, corrected Table 2, degree-44/45 rows (printed pp. 105–106). OCR/extracted text was available via a hosted PDF. PDF screenshot requests failed with cache misses; printed tables were not visually checked in the web viewer. These sources provide source-level coverage of generic families omitted from the finite corrected table.

## II. The two-block r=22 gate

Let `d=44`, `k=2`, inducing rank `r=22`, with intermediate genus 0 and two swap branch points. The checked excess identity yields

\[
E\le2r-26=18.
\]

For the standard-reflection-subgroup case, `tau = std_{S23} tensor psi`. If a local scalar value `psi` is nontrivial, the local movement rank satisfies

\[
T_r=r-\lfloor(r+1)/2\rfloor=11.
\]

A nontrivial scalar character of the punctured sphere cannot have only one nontrivial local value because meridian values multiply to 1. If any nontrivial value lies over a block-preserving point, Galois equal-rank on both lifts makes that base point consume at least `2(T_r-1)=20` excess. If nontrivial values lie only over swap points, there are at least two and they consume at least `2 T_r=22`. Both contradict `E<=18`. Thus `psi=1`, and the standard inducing character is rational, contradicting the full K-character condition.

The reflection-presence argument is `17 > E/2=9`: not all 17 preserving branches can have movement rank >=2 on each block. Finer reflection imprimitivity would give `(k,r)=(4,11)`, which fails `E_4=2*11+2*16-21*4+8=-22`. Monomial alternatives are already excluded by the field-independent induced-period bound. Exceptional irreducible complex reflection groups have rank <=8. Hence the two-block branch closes at `r=22`.

## III. Remaining structural and character screens

| Degree | Imprimitive cases | Factorwise cases | Primitive almost-quasisimple candidates with character field inside K |
|---|---|---|---|
| 44 | `(2,22)` closed by Lemma B; `(4,11)` by A′ | `(2,22)`: min sum 98 >96; `(4,11)`: 97 >96 | `A11` min 14, `U5(2)` min 16, `M11` min 20, `L2(43)` min 22, `SL2(43)` min 30. All rational/self-dual and > Lemma-C threshold 6. |
| 45 | `(3,15)` with E_3=-7; `(5,9)` with E_5=-29 | `(3,15)` by the checked three-pseudoreflection lemma; `(5,9)`: min sum 107 >98 | `A11` min 16, `M11` min 24, `M12` min 20: Q/self-dual with threshold 6; `U4(2)` min 24: field K with threshold 10. |

Other corrected-table ordinary representations are either modular-only (char0 excluded) or have character fields not contained in Q(sqrt(-3)). The corrected table includes the important `2.M12` at degree 44 (field Q(sqrt(-5))), and the generic Table 2 covers degree-44 `SL2(43)` and `L2(43)` and degree-44/45 half-degree `SL2(89)`/`L2(89)`. The latter's field is not contained in K. The natural alternating standard representations are excluded under the previously checked Lemma F (rank bound), not by omitting them from the classification.

The real normal forms can be orthogonal or alternating (FS indicator +1 or -1); inherited Lemma S covers both. In either degree the two similitude generators force Lemma C to produce a noncentral normal-socle element of movement rank <=6; no qualifying rational-character candidate does. Field-K non-self-dual candidates need rank <=10 and fail as well.

## IV. New narrowly scoped PROPOSED observation at d=46

In the two-block r=23 standard-symmetric branch, `E=20` and `T_r=11`, so the earlier Lemma B strict inequality becomes equality: `2(T_r-1)=20`. This equality can still be analyzed.

If scalar `psi` is nontrivial at any preserving base point, Galois equal-rank forces its two lifts each to have rank >=11 and uses all 20 units of excess. Thus N=19, both swap return maps are identity, and all other preserving points have rank 1. The product-one relation for `psi` requires at least two nontrivial local values, and the only locations where they can occur are the **two lifts of that single preserving base point**. At both points the movement rank is exactly 11.

For `std_{S24} tensor lambda`, nontrivial scalar `lambda` of order q has fixed-space multiplicity at most `floor(24/q)` in the 24-dimensional permutation module, and consequently the movement rank on the 23-dimensional standard module is at least `23-floor(24/q)`. Rank 11 forces q=2, `lambda=-1`; q>=3 would require rank >=15. Therefore the local values of `psi` are all +/-1 and `psi` has rational character. Its induced character is rational, contradicting full character field K.

If `psi` is nontrivial only at swap points, both swap points must contribute and cost at least `2T_r=22>E`; a mixed swap/preserving support is also impossible. Hence in the standard symmetric two-block case **the equality cannot furnish a nonrational scalar character**.

At r=23 the reflection-presence bound and the monomial branch remain closed, and there is no finer block system of inducing rank >=6 because 23 is prime. This suggests the **d=46 two-block imprimitive case is also excluded**, but does **not** exclude any primitive degree-46 group. Status: `[SESSION — PROPOSED]`; request independent proof checking before recording.

## V. Disposition

- `HCG-ALG-D44-D45-NONSPLIT-EXCLUSION`: **CHECKED recommendation, source-conditional**; nonsplit under (H) => `d >=46`.
- `HCG-ALG-TWOBLOCK-R22`: **CHECKED recommendation**.
- CTblLib 68 verdict lines: **SOURCE-LOG CHECKED**, not independent CTblLib re-execution.
- `HCG-ALG-TWOBLOCK-R23-EQUALITY`: **PROPOSED**; no upgraded global dimensional threshold.
- `HCG-OPEN-NONSPLIT8`: **OPEN**; Severn A/B/C remain CLAIMED; HCG v0.2 remains adopted; no RTG transfer/adoption.

## Primary references

- Hiss and Malle (2001), *Low-Dimensional Representations of Quasi-Simple Groups*, https://doi.org/10.1112/S1461157000000796 (Theorem 1 and Table 2).
- Hiss and Malle (2002), *Corrigenda*, https://doi.org/10.1112/S1461157000000711 (corrected Table 2, degree 44/45).
- GAP CTblLib source package v1.3.7, with frozen inputs and logs from the attached Claude ZIP.

Earlier GT08, induced-period, Lemmas A′/B/C/E/F/S, tensor and reflection-free results were **inherited**, not re-established by this audit. This is a scoped proof/source review.
