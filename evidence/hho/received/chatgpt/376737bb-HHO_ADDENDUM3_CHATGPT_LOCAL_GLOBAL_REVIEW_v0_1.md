# HHO — Independent review of Addendum 3, §A3.2 (local–global identification)

**Date:** 2026-11-04  
**Status:** SESSION mathematical review; noncanonical and not adopted.  
**Verdict:** **Valid after two necessary clarifications of integral models and normalization.** The intended norm-support conclusion follows under the already stated integral defect-zero Morita hypotheses. The literal assertion that the locally normalized and globally normalized Hermitian forms are *identical* is not generally true.

## 1. Sources and reading extent

1. Claude, `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (3).md`, SHA-256 `e2a2d708b936710645bb50085f4ab8c89bcdb177608e675c03009dd92275676b`: **complete**, 205 lines; §A3.2 examined in detail. The first 172 lines are byte-identical to the previous Addendum-2 snapshot.
2. `HHO_SUPPORT_LEMMA_PROOF_SKETCH_v0_1.md`: **targeted** §§2–3 (the integral isotypic and Morita premises).
3. Local `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`, SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`: **targeted** §6.16–6.17. The adopted Git tag/release record and Severn's governing v2 §§3.2, Prop. 7.1, Lemma 7.2 were **not verified** in this review. Accordingly no owner-dependent general PO-6 conclusion is promoted.

## 2. The correct integral coefficient model

Let `p ≡ 2 (mod 3)`, `F=Q_p`, `K_p=K⊗F` (a field), `R=O_K⊗Z_p` (its unramified quadratic integer ring), and `δ=√−3∈R×`. Fix an irreducible rational `Q[G]`-module U with `End_Q[G](U)=K`, a `G`-stable R-lattice `U_R`, and a **Z_p-valued**, perfect, G-invariant alternating lattice `(M_0,E_0)` originating in `H¹(C,Z_p)`.

The rational coefficient-extraction identity is

`E_0(fu,f'u')=Tr_(K_p/F)(c(f,f') h_U(u,u'))`,

with f,f' chosen from the Z_p-integral G-intertwining lattice into `M_0` (or the corresponding **rational isotypic** lattice with its integral K-centre action). Its values are in Z_p and can be tested against the integral trace dual.

**Do not silently substitute** `M_R=M_0⊗_(Z_p) R` and its **R-valued base-changed cup form** in that Z_p-valued equation. After scalar extension the χ and χ-bar summands and the sesquilinear/Hermitian conversion must be identified explicitly. That base-change compatibility is standard for an unramified étale algebra, but it is an additional map, not a consequence of notation.

A convenient unambiguous setup is to use the rational K-isotypic idempotent `e_Ω` in Z_p[G] and its self-dual lattice `M_0^Ω=e_Ω M_0`, with the order centre R acting integrally; then apply Morita to `U_R` and `M_0^Ω`. Alternatively work over `M_R` but write down the two conjugate eigensummands and the conversion of the R-valued pairing into the Z_p trace.

## 3. Independent proof of the integrality claim

The trace Gram matrix on the basis `(1,ω)` of R over Z_p is

```
Tr(1·1)       Tr(1·ω)    2   -1
Tr(ω·1)       Tr(ω·ω) = -1   -1
```

with determinant `−3`, a p-adic unit for every inert prime `p≠3`, **including p=2**. Thus the trace dual is exactly R:

`{c∈K_p : Tr(c R)⊆Z_p}=R`.

Since h_U is unimodular over R, its matrix coefficients `h_U(u,u')` as u,u' vary generate the unit ideal R. If f,f' are integral and the left side of the coefficient-extraction identity is Z_p-integral for all u,u', then `Tr(c(f,f') R)⊆Z_p`; hence **`c(f,f')∈R`**. Because δ is a unit, **`h_W=δ c` is R-integral**.

This proves §A3.2(1)–(2) with the coefficient-lattice distinction above. It does **not** by itself establish that h_W is perfect; that is the separate integral Morita-involution step using the self-duality of the chosen isotypic summand and unimodularity of h_U.

## 4. Exact local–global comparison and the normalization correction

The global Hermitian form h_W is uniquely characterized by the rational coefficient-extraction identity. Base-changing this identity to F and making the rational-to-χ component identification gives **the localization of the same form**, **provided the same h_U and trace convention are used**.

However, in the defect-zero proof the local coefficient form h_U is generally **renormalized by a rational p-power** to make its Gram matrix unimodular. If

`h_U,loc=t_p h_U,glob`, with `t_p∈F×`,

then uniqueness gives

`h_W,loc=t_p^(−1) h_W,glob`.

Thus `h_W,loc` is usually **not literally equal** to the localized global form. In K-rank 8, this has no effect on the desired discriminant norm class:

`det(h_W,loc)=t_p^(−8) det(h_W,glob)=N_(K_p/F)(t_p^(−4)) det(h_W,glob)`.

In particular, any p-adic valuation change is a multiple of 8, and `v_p(det h_W)` remains even at an inert prime. The original support obstruction is **repaired without requiring the stronger, generally false, literal equality.**

At the local-to-global stage one must also retain the fixed embedding of K, χ versus χ-bar, and any scalar from the δ/trace conversion. At an inert p≠3, δ is a unit; if the conversion uses an additional rational unit, its eighth power is a norm. A K-antilinear identification conjugates the Hermitian Gram form without changing its rational determinant.

## 5. Perfectness and scope

Assume, as in the previously checked defect-zero Morita lemma, that the relevant χ-block is an integral split matrix order, that its self-adjoint rational isotypic idempotent selects a perfect summand of the cup lattice, and that h_U,loc has unimodular Gram matrix. The Morita tensor-form decomposition then transfers perfection to h_W,loc. A mere R-valued Hermitian pairing, without the self-dual summand, would not suffice.

**Verdict on §A3.2:** The **local norm-class conclusion is CHECKED** with these explicit assumptions and the normalization correction. The wording “the same local/global Hermitian form” should be replaced by **“the localized global form, up to an explicitly controlled rational p-adic scalar (and possible χ/barχ conjugation)”**. This is enough for the eight-dimensional support theorem.

**Still OPEN:** Severn's actual A_sigma projector and the polarization used by his factor (obligation (d)). The abstract Morita and evaluation results do not establish that identification with the governing v2 paper. Nor does this review settle `(L)+(D) ⇒ [det h]=[1]` or the positive-defect cases p=2,5 for G34.

## 6. Status/disposition proposal

| Item | Recommended status |
|---|---|
| Addendum 3 trace-pairing integrality | SESSION THM — CHECKED after integral-model clarification |
| Local–global norm-class identification | SESSION THM — CHECKED **up to rational scale** |
| Perfect local h_W | Inherited integral-Morita theorem, conditional on perfect χ-summand and normalized h_U |
| Literal equality of locally normalized and global h_W | **Not generally valid**; correct the statement |
| HHO-HYP-SUPPORT | CONDITIONAL THM, no owner promotion |
| Severn v2 factor/polarization match (d) | OPEN — governing text required |
| `(L)+(D) ⇒ [1]` | OPEN |

No RTG/HCG canonical content or PI adoption status has been changed.
