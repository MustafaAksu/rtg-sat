# HCG — Independent review of the d=6 discriminator scan and local determinant proposal

**Date:** 2026-10-29  
**Status:** SESSION / NONCANONICAL / INTERNAL. No adopted HCG or RTG file modified.  
**Input report:** `H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md`, read in full, together with both supplied Python programs and their supplied logs.  
**Disposition:** The reported determinant classes are corroborated where inputs are available. A substantive sample-count correction is necessary. A new explicit proof of discriminant locality and a d=6 G34 exclusion are proposed for peer review; they are not yet jointly CHECKED.

## 1. Identity, availability and replay

The received original report, scripts and logs are preserved unchanged under `source/`. `generic_engine.py` was recovered byte-for-byte from the earlier uploaded `H3_P2P3_CHECK_v0_1.zip`, SHA-256 `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505`. Seven G34 root inputs were recovered from existing earlier certificate archives. Only import and file path literals were adapted in the producer replay programs.

**Missing source inputs:** W6 and W7 root JSONs were not in the current upload or accessible earlier archives. Some earlier uploaded files are no longer available. Neither of those two cases was rerun in this review. Their historical results are not erased, but the present review does not label them replayed.

The G34 producer replay reproduced every available row byte-for-byte: W5, NEW01–04, BLOCK-01, ESCAPE (7 of the 9 paired tuples), and all 9 W5 merges. Source-reported G34 determinants were unchanged. The G(3,1,3) replay log is byte-identical to the supplied log. The G(3,3,3) script also completed; its separate original output file was not supplied for byte comparison.

## 2. Required correction: the supplied script does not perform 120 + 480 tests

The actual control flow fixes `while got < 80` **for each N in (8,10)**. It does not allocate 80 samples to each local class multiset. Consequently:

| Group | N | Accepted samples | Distribution by the local-class multiset |
|---|---:|---:|---|
| G(3,3,3) | 8 | 80 | one class multiset: 80 |
| G(3,3,3) | 10 | 80 | one class multiset: 80 |
| G(3,1,3) | 8 | 80 | (0^6,1,2): 49; (0^4,1^2,2^2): 31 |
| G(3,1,3) | 10 | 80 | (0^8,1,2): 28; (0^6,1^2,2^2): 39; (0^4,1^3,2^3): 12; (0^4,2^6): 1 |

Thus the reproducible totals from this source revision are **160 + 160 = 320**, not 120 + 480 = 600. The source label `|G(3,3,3)| = 162` in G313 mode is also a cosmetic hard-coded label; the computed order is correctly 162 for G(3,1,3).

To check this without relying on the original group engine, `audit_sampling_counts.py` independently rebuilt the exact monomial groups (permutation plus Z/3 exponents) and reproduced the same random index stream with seed 20261029. It saved every accepted tuple. These are finite sampled tests; no uniformity or exhaustive coverage is claimed. In particular, the exceptional class multiset (0^4,2^6) has only **one** observed sample in this run.

The mathematical determinant-class results in the supplied log are correct for the actual samples. The correction concerns evidence counts/provenance, not a counterexample to locality.

## 3. New independent exact implementation

`local_determinant_independent.py` was written in this review using Python's Fraction pairs for K=Q(w), w²+w+1=0. It imports no Claude/HCG arithmetic or cohomology engine. It builds a fresh moving-space cochain basis, imposes closure, quotients by coboundaries, computes the skew-Hermitian pairing, and checks the determinant identity derived in the companion proof note.

Checks performed:
- The same seven accessible paired G34 inputs: class [1] in each.
- The nine W5 19-point merged data: class [1] in each.
- The previous C6 nonsplit control: class [2], and the C3 split control: class [1].
- One parabolic-dimension-two cyclic case: sign class [-1], showing that the (-1)^n term cannot be omitted.
- **320/320** exact sampled G333/G313 quotient calculations; each agrees with the new local determinant formula and with the reported class for its local multiset.
- For a representative of each sampled local multiset and the selected controls: the full triangular matrix identity B+B*=C^t H_0 conjugate(C), the block determinant identity, and the change-of-basis norm identity all hold exactly.

The determinant representatives differ from the producer's because these are new quotient bases. For example W5 is 1/3 and the C6 control is 4374 in this implementation; their classes are [1] and [2], respectively. Comparisons are explicitly in Q*/Nm(K*), not false equality of basis-dependent raw determinants.

**Independence limitation:** the same root/monodromy inputs and accepted sample indices are used. This is a new algebraic implementation, not independent acquisition of source data, and not a second human review. The proof itself is separate from these finite checks.

## 4. Proposed theorem, not an inference from sampling

Let E_i=im(1-g_i), a_i=det(h_0|E_i), b_i=det((1-g_i)|E_i), and dim_K H_par=2n. Under the hypotheses detailed in `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md`,

  [det(theta S)] = [(-1)^n product_i a_i/b_i]
                 = [(-1)^n product_i a_i b_i].

The product of the b_i is rational, although the individual b_i can be non-real. This is an explicit local formula, with the coefficient Hermitian form included in the local data. It is **not** a statement that the determinant representative or full cup matrix is determined by local classes, nor a claim that signature alone determines the discriminant.

The proof extends the cup form to a triangular sesquilinear form on all moving-space cochains. In a basis adapted to coboundaries, quotient cohomology, and the closure map, the determinant reduces to det(S) times the square of det(H_0). All remaining changes are field norms. The companion note provides the full argument, including nondegeneracy, surjectivity of closure, and the global sign.

**Current status:** complete SESSION proof supplied, **PROPOSED / peer review pending**. No assertion of research novelty. The source's unpublished “Theorem W” was not used as an assumption.

## 5. Why both d=6 G34 budgets are excluded if the proof is accepted

For a norm-six root reflection s: a_s b_s=6*2=12. Twenty such local terms have product 12^20, a norm; n=4 has positive global sign.

For eighteen reflections plus one rank-two element, a subtle point must be justified: the rank-two element is not known to be a product of two reflections merely because it is the inverse of a product of eighteen. This review supplies the missing classification through Steinberg's theorem plus the G34 rank-two root-flat census.

The exact orbit of the ten W5 generating roots yields 126 lines, 756 vectors, and group order 39,191,040. All 7,875 pairs have squared inner product 0 or 9. The rank-two flats are 2,835 orthogonal two-line flats and 1,680 three-line flats. A Gram-rank inequality gives at most three such root lines in a two-plane. Steinberg's theorem therefore restricts every rank-two element to a parabolic of type A1×A1 or A2. Its local product is respectively 144=N(12) or 81=N(9).

Hence both budgets have cup discriminant [1] on **every** component. With the separate cup-to-induced-Jacobian-polarization comparison, no nonsplit eightfold candidate can occur in this d=6 G34 screen. This is stronger than constancy along a known braid orbit.

**Do not overstate:** the global nonexistence statement remains a proposed corollary until the new proof is peer-checked. The reduction of all d=6 candidates to G34 still uses the earlier assumptions and monomial exclusion. General nonsplit eightfold existence, other methods, and d>=7 are not excluded.

## 6. Provenance / structural points

- The nine paired G34 observations alone cannot establish locality: paired structure already supplies split models, and several of the named tuples have been explicitly linked in the same component.
- 'G itself may be a central extension' in the input report should be read cautiously: an unfaithful sigma gives an extension of its image; centrality of its kernel requires another hypothesis. The discriminator result depends on the image representation, so this does not affect it.
- This review did not rerun the intermediate-cover computation or the already checked scalar-extension exclusion.
- No current Severn-v2 theorem status, PI adoption, HCG v0.2 bytes, or external auditor disposition changed.

## 7. Proposed dispositions and next action

| Record | Proposal |
|---|---|
| Available G34 scan subset (7 paired + 9 merged) | CHECKED finite replay; W6/W7 not replayed here |
| G333/G313 source sample results | CHECKED for the actual 160+160 accepted cases; correct report counts |
| Local determinant formula | SESSION THM / PROPOSED, independent peer review required |
| G34 rank-two classification supplement | SESSION ALG plus classical Steinberg theorem; peer review required |
| d=6 nonsplit exclusion in current screen | PROPOSED consequence of the new theorem and classification supplement |
| HCG-OPEN-NONSPLIT8 | OPEN, next coefficient rank d>=7 if the exclusion is accepted |

Send the proof note and executable package to Claude for an independent proof audit. Prioritize equations (3)–(5) in the proof and the rank-two parabolic step. No wider search campaign is needed to decide the d=6 question first.
