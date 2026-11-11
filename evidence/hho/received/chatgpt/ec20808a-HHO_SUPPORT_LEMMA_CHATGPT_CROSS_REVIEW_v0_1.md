# HHO — Cross-review of the prime-support lemma and its defect-zero refinement

**Date:** 2026-11-03  
**Status:** SESSION review; noncanonical, not adopted.  
**Reviewer:** ChatGPT  
**Inputs:** `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` (entire 80 lines, SHA-256 `5c70ef22fbcd99173434a30da3ff7fbf1e69e2c0002243a81f5fe7fd248d9597`), `HHO_SUPPORT_LEMMA_PROOF_SKETCH_v0_1.md` (entire 8619-byte file, SHA-256 `326f9645c71cf44b429f30581c61dae8d99bf5ef216a262686a9076a64491f3d`), `HHO_SUPPORT_LOCAL_SYMBOL_CHECK_v0_1.py` (whole file, SHA-256 `04498c739089836f839f74898fd6b5f48eb694ec7b81071689e77e9bc5be6d3c`; replayed PASS), and local snapshot `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`), targeted §6.16 and the Weil definitions. The Git adoption tag/release record and Severn v2 governing owner text have **not** been verified. The current review does not turn a local file title into an adopted-edition assertion.

## Decision

1. **Integral isotypic and Hermitian Morita arguments:** mathematically valid, with corrected coefficient ring and an explicit Morita-adjoint normalization step. Recommend **SESSION THM** under the stated representation-theoretic assumptions, rather than claim adoption.
2. **Global transfer without an integral parabolic-form comparison:** viable **conditional proof**, but it still needs the global rational Hodge polarization to be shown to be the polarization induced by the Jacobian factor and the `End^0=K`/`NS_Q=Q` premise established from the verified owner definition of (D). A local unimodularity result by itself does not identify the polarized abelian factor.
3. **Defect-zero refinement:** valid as a **sufficient criterion** for the required integral central idempotent and full matrix block. State `e_χ∈O_{K,p}[G]`, not `e_χ∈Z_p[G]` for a genuinely nonrational K-valued χ. No equivalence is needed to prove the support bound; avoid attaching an unqualified `iff` to the theorem.
4. **General no-inert-support corollary:** a proven implication conditional on the transfer/polarization identification. The refinement alone does not prove `(L)+(D) => [disc]=[1]` when inert positive-defect primes occur.

## 1. Correct local theorem

Let `K=Q(sqrt(-3))`; `p≡2 mod 3` be inert and `p != 3`; `R=O_K⊗Z_p` be an unramified quadratic DVR; and let σ be an absolutely irreducible **K-defined** degree-d finite-group representation with character χ, realized on a free R-lattice U. Assume χ has **p-defect zero**:

`v_p(χ(1)) = v_p(|G|)`.

Let M be a `G`-stable, self-dual symplectic `Z_p`-lattice (e.g. the Jacobian H¹ lattice), with `G` acting by isometries. Then:

- The central χ-projector

  `e_χ = (χ(1)/|G|) Σ_g χ(g^-1)g`

  belongs to `R[G]`, because χ-values are integral in `O_K` and `χ(1)/|G|` is a p-unit. It is Hermitian-adjoint fixed. Thus the full χ-isotypic summand of `M⊗R` is Hermitian-self-dual.
- Brauer's defect-zero block theorem, together with the assumed K-realization, gives `e_χR[G] ≅ M_d(R)`. The induced involution is adjoint for a G-invariant K_p-Hermitian form `H_U`.
- Because the involution preserves the maximal matrix order, `H_U` normalizes `M_d(R)`. The normalizer is `K_p^×GL_d(R)`, so `H_U=p^k H_U^0` for some integer k and unimodular **Hermitian** `H_U^0∈GL_d(R)`. This uses that p is a rational uniformizer of the unramified extension.
- Integral Hermitian Morita theory gives the χ-isotypic self-dual module as `U⊗_R W_R` and the form, after the above rational rescaling, as `H_U^0⊗H_W^0`. The tensor product is perfect and `H_U^0` is perfect; hence `H_W^0` is perfect. In particular its determinant is an R-unit, and at an inert unramified prime every unit is a norm.

**Conclusion:** The **rational induced rank-eight multiplicity form**, when compared with `H_W^0` up to a rational scalar, has local trivial norm class at p. Its determinant need not have a literally even valuation before normalizing the form: for rank eight, multiplication by `q∈Q_p^×` changes determinant by `q^8=N_{K_p/Q_p}(q^4)`, preserving its norm class and valuation parity.

For `p∤|G|`, p-defect zero is automatic; this recovers the original prime-to-group-order statement.

**Arithmetic check:** `G=C3×S3`, `χ=ζ3⊗std_2`, is a K-valued degree-two representation with `|G|=18`, `χ(1)=2`. The prime p=2 divides |G| but χ has 2-defect zero; `χ(1)/|G|=1/9` is 2-adically integral and `|G|/χ(1)=9`. This checks that the refinement genuinely goes beyond `p∤|G|`. It is not a constructed admissible HHO Hurwitz family.

## 2. Exact form-transfer obligations

The suggestion to bypass an **integral parabolic-to-Jacobian comparison** is mathematically reasonable; the obstruction only needs a p-unimodular lattice for **one global K-Hermitian polarization form** on the weight-one multiplicity Hodge structure, up to rational scaling. But it must be proved that:

(a) `W_Q=Hom_{Q[G]}(U_Q,H¹(C,Q))` (or its precisely identified K-linear avatar) is a polarizable weight-one rational Hodge structure with the same rational K-action as the geometric abelian factor;

(b) the Hermitian form obtained from Jacobian cup pairing by Schur–Morita is **a polarization** of that factor, rather than merely a nondegenerate rational form on its underlying vector space;

(c) for a general member, the actual induced polarization and this rational Morita polarization differ by a rational scalar. This follows if the generic `End^0(A)=K` with Rosati acting by conjugation; then `NS(A)_Q = End^0(A)^{Rosati=1} = Q`. Showing (D) entails the required generic condition is a **source-specific dependency**;

(d) the h-normalization, K-embedding/conjugation, and rank-one Rosati projector conform to the governing Severn owner statement. A nonzero rational scalar is harmless to an 8-dimensional determinant class, while an unverified non-scalar correspondence is not.

The local HCG v0.2 **snapshot §6.16** states that the W5 application of PO-6 was verified, but that general PO-6 remains `[EXT-CLAIM]/PROPOSED`. Thus this new argument could *replace* the unverified general integral comparison for a more restricted generic-polarization statement; it should not simply overwrite the general owner limitation before (a)–(d) are discharged.

## 3. Defect-zero support theorem (conditional on §2)

For an actual rank-eight polarized factor with signature (4,4), let `D=det h∈Q_{>0}`. The local argument shows

`(D,-3)_p = +1` for inert p with `v_p(|G|/χ(1))=0`.

The only potential negative finite local symbols are at

`{3} ∪ {p≡2 mod 3 : p | |G|/χ(1)}`.

If no inert prime divides that quotient, the infinite sign is positive, and Hilbert reciprocity forces the remaining sign at 3 to be positive. Hence `[D]=[1]` in `Q×/N(K×)`.

This is **dimension-independent in the group parameter**, but uses the **even rank eight** in the scalar-independence step and the Hodge signature (4,4) for positivity. It does not assert universal splitness without the defect/no-inert hypothesis.

## 4. Dispositions and acceptance criteria

| Item | Status recommended |
|---|---|
| Full isotypic p-self-duality | SESSION THM, checked at the algebraic level |
| Local Hermitian Morita reduction at inert defect-zero p | SESSION THM, checked under the stated splitting/involution hypotheses |
| Defect-zero support-set refinement | Conditional SESSION THM (sufficient direction) |
| Generic Jacobian-factor polarization matching | OPEN until (a)–(d) are documented; no need for an *integral* parabolic comparison if this rational route works |
| `(L)+(D)` forces split | OPEN — **not** implied by defect-zero at some primes |
| PO-6 general or canonical HCG/RTG adoption | Unchanged; PI authority required |

**Next minimal test:** a character-by-prime matrix for every target tuple, recording `v_p(|G|)`, `v_p(χ(1))`, inert status, expected support and observed symbol. In a second table, identify which owner hypotheses certify the rational polarized factor, End⁰=K, Rosati conjugation and the scaling relation. Tests must distinguish a formal group representation from an actual dominant family; C3, C21 and 7:3 are examples of candidate prime support, not asserted HHO constructions.

## Sources

- GAP CTBlocks reference on defect-zero blocks and the character-degree defect formula: https://www.math.rwth-aachen.de/homes/Thomas.Breuer/ctblocks/doc/chap3_mj.html
- Curtis–Reiner/Brauer block theory, as summarized in the finite-group representation guidebook (defect-zero matrix blocks): https://dokumen.pub/representation-theory-of-finite-groups-a-guidebook-1nbsped-978-3-030-21.html
- Local owner snapshot: `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` §6.16, sha256 as above; adopted tag not independently verified.
