# HHO — Support Lemma: prime-to-group-order discriminant obstruction

**Date:** 2026-11-03  
**Status:** `[SESSION]` proof sketch. The full eight-dimensional Hurwitz–Hodge claim is **PROPOSED**, not adopted.  
**Scientific owner:** HHO research track (noncanonical); no HCG/RTG repository edits.

## 0. Sources and reading extent

- `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`, SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`; *targeted local snapshot* §§6.15–6.17, especially §6.16 PO-6 and the general-projector limitation. The adopted Git tag and release record were **not independently verified** in this session.
- `H3_NONSPLIT8_CYCLIC_SEPARATOR_CHECK_CLAUDE_v0_1.md`, SHA-256 `b7599e26599f55ececaa547af2505692ebfc4aadea5f4a15728e51c36dfbbde7`; targeted §§1–2 (C6/C3 discrimination, (L)/(D) caveats); secondary session evidence, not an owner statement.
- User-supplied HHO hypothesis and Hilbert support; owner definitions of (L), (D), and (H0)–(H4) were **not verified**. The general Severn v2 polarization theorem was **not re-read**.

## 1. Exact target and the essential distinction

Let `K=Q(sqrt(-3))`, `O=Z[omega]`. Let `C` be a smooth projective complex curve with finite group `G` acting by automorphisms, and let `E` be the integral unimodular symplectic cup form on `M=H^1(C,Z)`. Suppose `sigma:G→GL_d(K)` is absolutely irreducible with character `chi`, and its parabolic multiplicity module `W` has K-rank 8, signature `(4,4)`.

**HHO-HYP-SUPPORT (target).** If the natural comparison between `W` and the `G`-isotypic part of `H^1(C,K)` respects the local Hermitian forms up to a rational scalar (and possibly conjugation), then for every inert rational prime `p≡2 (mod 3)` with `p∤|G|`,

`v_p(det h_W) ≡ 0 (mod 2)`.

**Important:** A central character projector `e_chi` selects an isotypic module of rank `8d`, **not** the rank-eight multiplicity space. Unimodularity of the first does not by itself prove the claimed statement for the second. The rank-one integral Morita projector is the essential step.

## 2. Local p-integral isotypic lemma — proved

Let `p∤3|G|` be **inert** in K, set `R=O⊗Z_p` (an unramified quadratic DVR over `Z_p`), and `delta=sqrt(-3)=1+2omega`, a unit of R. Put `M_R=H^1(C,Z_p)⊗Z_p R`.

1. Extend E and define `H(x,y)=delta^{-1} E_R(x,bar y)` (conventions may transpose x,y). Since E is perfect alternating and delta is a unit, H is a **perfect Hermitian form over R**.
2. Every element of G acts by an H-isometry. The central idempotent

   `e_chi = (d/|G|) Σ_(g∈G) chi(g^{-1}) g`

   belongs to `R[G]`: all character values are algebraic integers in O and `|G|` is a p-unit. Under the Hermitian adjoint `g↦g^{-1}`, `a↦bar a`, one has `e_chi^*=e_chi` because `bar chi(g)=chi(g^{-1})`.
3. Hence `M_R=e_chi M_R ⊥ (1−e_chi)M_R`. Both summands are R-direct summands and **perfect**. In particular, the full `chi`-isotypic lattice is p-unimodular.

This local implication is established without any Hurwitz-period or (L)/(D) hypothesis.

## 3. Integral Morita reduction to rank-eight W — proof sketch; requires a precise comparison

Choose a G-stable R-lattice `U` in sigma. The action is integral because G is finite. At p prime to |G|, matrix coefficient orthogonality gives integral matrix units:

`E_ij = (d/|G|) Σ_(g∈G) [sigma(g^{-1})]_{ji} sigma(g)`

(up to the harmless index convention). Consequently the image of `R[G] e_chi` on U is all `End_R(U)≅M_d(R)`.

Let `H_U` be the G-invariant K_p-Hermitian Gram matrix. The star involution preserves this full matrix order. Therefore its adjoint involution is represented by a matrix which normalizes `M_d(R)`, i.e. `H_U∈K_p^× GL_d(R)`. Because K_p/Q_p is unramified and H_U is Hermitian, a **rational p-power** rescaling makes H_U lie in `GL_d(R)`. Its norm class is then p-unimodular.

Using the integral matrix units and Hermitian Morita equivalence, the perfect isotypic lattice has an integral decomposition `e_chi M_R≅U⊗_R W_R` with Hermitian form `H_U⊗ H_W`, and `W_R` is a perfect rank-eight Hermitian R-lattice. Thus `v_p(det H_W)=0` in an integral R-basis.

**[OPEN / source dependency]** One must now identify the *parabolic* Hermitian form used in the HHO discriminant with this Morita form (or its conjugate), up to `q∈Q_p^×`. If this comparison is valid,

`det(q H_W)=q^8 det H_W=N_(K_p/Q_p)(q^4) det H_W`,

so the local norm class is unaffected even if q is not a p-unit. A corresponding global cup–polarization/projector comparison is needed before asserting the result for the **actual polarized eightfold**. `HCG v0.2 §6.16` explicitly distinguishes the W5-specific comparison (checked) from the general external claim (not generally checked).

**Review request:** Check the integral matrix-unit/Morita step at p=2 and the general parabolic–Jacobian factor pairing. These are the actual scientific proof obligations; changing the `e_chi` denominator alone is not enough.

## 4. Conditional support theorem and dimension-free no-go

Assuming §3's form comparison, put `D=det h_W∈Q_{>0}` (signature `(4,4)`). At inert primes `p≡2 (mod 3)`, `p∤|G|`, the class is unramified and the valuation is even. At split primes, every local rational is a norm. Thus nontrivial local Hilbert symbols `(D,-3)_v=-1` can occur only at

`{3} ∪ {p : p| |G|, p≡2 mod 3}`.

By Hilbert reciprocity, the sign at 3 is determined by those inert support primes because the infinite sign is +1. In particular, if `|G|` has **no** inert prime divisor, the class is split:

`[det h_W]=[1]`.

This conditional implication is **dimension independent**. It does not assert that `(L)` implies a split discriminant, that all eightfolds split, or that the Hodge conjecture fails.

## 5. Exact control table

| Example | Positive class representative D | Inert primes with odd v_p(D) | Hilbert -1 places | Consistent with group-order support? |
|---|---:|---|---|---|
| C3 (split) | 1 | none | none | Yes, |G|=3 |
| C6 (nonsplit) | 1/2 or 3/2 | {2} | {2,3} | Yes, 2||G| |
| G34 20-reflection W5 (split) | 1 | none | none | Yes, 2 and 5 can divide |G| but need not occur |
| Illustrative arithmetic [5] | 5 | {5} | {5,3} | Can occur only if 5||G| under support theorem |
| Illustrative arithmetic [10] | 10 | {2,5} | {2,5} | Ramified 3 can have sign +1 despite nonsplitting |

The table only tests arithmetic classes. It does not reconstruct a genus-zero Hurwitz tuple or an actual polarized factor in the illustrative rows.

**Source arithmetic correction:** The group order stated in the preliminary HHO notes as `2^7·3^7·5·7` is not the full order of G34: the established value `39,191,040` equals `2^9·3^7·5·7`. The inert-prime *set* `{2,5}` is unchanged, so this correction does not affect the support argument.

## 6. Negative control: an arbitrary rational projector can introduce an inert prime

Over R=O⊗Z_2 equip `R^9` with the unimodular Hermitian Gram matrix `diag(1,1,1,1,1,-1,-1,-1,-1)`. Take the rank-eight K-linear subspace generated by `(e1+e2),e3,...,e9`. The restricted Gram matrix is `diag(2,1,1,1,-1,-1,-1,-1)`, of signature `(4,4)` and determinant 2 (an inert-prime obstruction). Its orthogonal projector includes the coefficient `1/2`, so it is **not** integral at p=2. This does not contradict §2 because the projector is not the integral `e_chi` or an integral Morita idempotent. It shows why an arbitrary Rosati-selfadjoint **rational** projector cannot simply be assumed to preserve local unimodularity.

## 7. Disposition and acceptance criteria

- **HHO-ALG-INTEGRAL-ISOTYPIC:** `[THM; SESSION]` as a proved p-local implication for a unimodular G-symplectic lattice and a K-valued character, with p∤3|G|.
- **HHO-HYP-SUPPORT-MORITA:** `[SESSION — proof draft]` requires an independent check of the integral Morita structure and Hermitian involution, especially p=2.
- **HHO-HYP-SUPPORT-TRANSFER:** `[OPEN]` pending the explicit parabolic/Jacobian comparison for the target rank-eight form and its polarization.
- **HHO-COR-NO-INERT-GROUP-PRIMES:** `[THM | conditional on Morita+transfer]`. No promotion to adopted science before both dependencies close.

Acceptance requires: (i) an integral p-local model of the actual target multiplicity form, (ii) statement of any conductor/polarization/projector denominators, (iii) check that p∤3|G| excludes **all** such denominators except rational scales whose eighth power is a norm, and (iv) source-verified definitions of HCG `(H)` and Severn `(L),(D)` before any method-level application. The report is intentionally separate from the HCG owner ledger.
