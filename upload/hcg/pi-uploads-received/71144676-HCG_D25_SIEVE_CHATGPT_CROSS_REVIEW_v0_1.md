# HCG — Independent review of Claude's rank-3/rank-4 terminal sieve v0.1

**Date:** 2026-10-30. **Distribution:** INTERNAL, HCG exploratory research.  
**Scope:** Source-code replay, independent exact cyclotomic/age enumeration, interpretation of the 2545 count, GT deviation bounds, and a separate proposed degree-25 classification argument. No adopted DSN is modified.

## 1. Intake and independent calculations

The input `H3_D25_SIEVE_REVIEW_CLAUDE_v0_1.zip` contains five files under its manifest. All **5/5** hashes match. The original script `d25_terminal_sieve_claude.py` ran unchanged and its output was byte-identical to the supplied `d25_terminal_sieve_claude_out.txt`. The previous full tensor-frontier replay mentioned in the producer's log was not rerun in this review.

A new implementation does not import the source code. It derives admissible root orders from `[Q(zeta_q):K]<=4`, constructs primitive Galois orbits, crosschecks their lengths using exact cyclotomic factorization over K in SymPy, enumerates multiplicities and tests the age of **every nonidentity power** with rational arithmetic. No floating-point rank or age decisions are used.

| Check | Source | Independent result |
|---|---:|---:|
| Galois-stable rank-3 spectra | 54 | 54 |
| Terminal rank-3 spectra | 5 | 5 |
| Galois-stable rank-4 spectra | 150 | 150 |
| Terminal rank-4 spectra | 28 | 28 |
| 18 rank-3 type counts + rank-4 **age**, total age 29 | 2545 | 2545 |

**Recommendation:** these finite results can be marked CHECKED (two implementations). They do not assert that a group, a product-one tuple, or a family exists.

## 2. Exact meaning of 2545

The producer's script counts a rank-4 age once even when several rank-4 spectra have that same age. This matches its stated 'type counts using the eleven ages' interpretation. It is not an error.

If the rank-4 spectrum itself is also distinguished, the exact number of local profiles is **6548**, not 2545. Neither number counts ordered branch tuples or group-conjugacy data.

The determinant condition adds nothing at the spectral level: `prod det(g_j)=exp(2*pi*i*sum age(g_j))=1`. This does **not** imply the matrix identity `prod g_j=1`.

## 3. Theorem 1.1 is weak here, but Theorem 1.3 is useful

[GT12] defines `d_2(g)^2=2(d-|Tr g|)`. For d=25 the five rank-3 types give:

| Moving type (with its inverse where distinct) | |Tr g|^2 | d_2(g)^2 |
|---|---:|---|
| `(zeta6,zeta6,bar zeta6)` | 553 | `50-2 sqrt(553)` |
| `(w,w,bar w)` | 421 | `50-2 sqrt(421)` |
| `(-1,-1,-1)` | 361 | 12 |

Taking C=12 in Theorem 1.1 gives `f(C)=480`, so it does not exclude dimension 25. This confirms the source review's tentative reading after explicitly computing the deviations.

However, Theorem 1.3 applies to the remaining complex-primitive, tensor-indecomposable, not-tensor-induced branch. For a noncentral element not a scalar reflection it gives

`Delta(g)=25-|Tr g| >= 8-4 sqrt(2)`.

The two order-six rank-3 types have `Delta=25-sqrt(553)` below that threshold. They are excluded by primitivity, although they pass the age test. Every nonidentity power of a terminal rank-3/4 spectrum has rank at least 3 and fixes at least 21 dimensions; hence it is neither scalar nor a scalar reflection. The theorem can therefore be applied to all such powers.

Independent exact results after this stronger screen:
- Rank-3 types: **3** (the two mixed cubic types and the involution).
- Rank-4 types: **24**.
- Age-level profiles: **92**.
- Profiles distinguishing the rank-4 spectrum: **210**.

The four removed rank-4 spectra, written as rational eigenangles, are:
`(1/12,5/12,7/12,11/12)`, `(1/6,1/6,1/6,5/6)`, `(1/6,1/6,5/6,5/6)`, `(1/6,5/6,5/6,5/6)`.
The order-12 case fails on its square, demonstrating why all powers must be checked.

**Status:** this is a new source-based screen, PROPOSED pending peer review. A proof and exact algebraic comparisons, not only a numeric filter, underlie the code. No source claim was silently replaced: the original terminal list remains valid in its stated scope.

## 4. Stronger proposed result: d=25 is excluded by finite-group structure

See `HCG_D25_CLASSIFICATION_EXCLUSION_PROPOSED_v0_1.md` for a separate full proof. The main new idea is to combine a normal-quasisimple reduction with the degree-25 ordinary representation list, rather than to search thousands of local profiles.

The structure input [GT08] applies under (S), not under an unproved symmetric-power irreducibility hypothesis. Its symplectic-type option would force a scalar of order 5 in Gamma, impossible over K. The almost-simple option gives a normal quasisimple subgroup L acting faithfully and irreducibly. Its centre is trivial since its scalar orders divide both 6 and 25.

The degree-25 possibilities from the original generic table and corrected exceptional table of Hiss--Malle are A26, PSL2(25), PSL2(49) (all orthogonal) and PSp4(7) (character field Q(sqrt(-7)), not a subfield of K).

For the three orthogonal cases, normality makes every g a similitude of the unique L-invariant symmetric form. A fixed subspace of dimension >25/2 forces similitude multiplier 1. The branch generators fix 22 or 21 dimensions, so the entire finite Gamma becomes self-dual and has real character. Its K-valued character is then rational, contradicting exact character field K.

This is a proposed classification-based exclusion of the d=25 HCG datum. Combined with the earlier CHECKED d<=24 result, it proposes the next lower bound d>=26. It does not establish existence at d=26, a general nonsplit impossibility theorem, or any Hodge-algebraicity claim.

## 5. Primary-source provenance

- [GT12] Guralnick--Tiep, *A problem of Kollár and Larsen on finite linear groups and crepant resolutions*, JEMS 14 (2012); arXiv:1009.2535. Targeted reading: d_2 definition, Theorems 1.1 and 1.3. https://arxiv.org/pdf/1009.2535
- [GT08] Guralnick--Tiep, *Symmetric powers and a problem of Kollár and Larsen*, Invent. Math. 174 (2008); arXiv:0810.0853. Targeted reading: (S), Lemma 2.5, Proposition 2.8 and its finite-group proof.
- [HM01]/[HM02] Hiss--Malle, LMS J. Comput. Math. 4 (2001), 22--63 and corrigenda 5 (2002), 95--126. Targeted reading: Theorem 1, original generic Table 2 and corrected degree-25 rows. The dimension-25 row for 3D4(2) is characteristic 3 only and is not a complex representation.
- [ATLAS] Primary S4(7) group page crosscheck: degree-25 characteristic-zero representation over Z(b7).

**Access limitation:** The relevant primary PDFs were text-accessible, but screenshot requests failed with Cache miss. No visual table verification or PDF-byte hash is claimed, and these source PDFs are not included in the reproduction archive. The next peer should specifically visually check the degree-25 rows and the retained generic cases. The complete external classification proofs were not independently re-established.

## 6. Proposed dispositions

| Record | Status recommendation |
|---|---|
| Claude terminal rank-4 sieve and 2545 age-profile count | CHECKED, finite arithmetic scope |
| Correct distinction: 6548 actual spectral profiles | New exact clarification, PROPOSED pending peer confirmation |
| GT1.3 screen: 3 / 24 spectra, 92 / 210 profiles | PROPOSED |
| Degree-25 group exclusion | PROPOSED, classification inputs and source-access limitation recorded |
| Nonsplit lower bound d>=25 | Existing CHECKED status unchanged |
| Strengthening to d>=26 | PROPOSED corollary, not adopted |
| HCG-OPEN-NONSPLIT8 | OPEN |

The previous independent audits, PI fields, adopted HCG v0.2 and Severn A/B/C CLAIMED status are unchanged.
