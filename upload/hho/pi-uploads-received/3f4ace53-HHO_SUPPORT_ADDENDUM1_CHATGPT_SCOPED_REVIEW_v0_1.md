# HHO — Scoped cross-review of Claude Support Lemma Addendum 1

**Date:** 2026-11-03  
**Provenance:** `[SESSION]` independent mathematical review, noncanonical.  
**Disposition:** Accept the new evaluation-map proof of obligation (a). Accept obligation (b) as a **conditional algebraic proof draft** pending explicit cup/Morita normalization; do not label it CLOSED unconditionally. Obligations (c) and (d) remain owner-dependent. No PI adoption or HCG/RTG modification.

## 1. Sources and reading extent

- `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (1).md`: entire 123-line file, including dated Addendum 1, SHA-256 `e7059f78e1695cabdbe41d084de09f3aa41d8b26c9eb6fd5d2f240060f4b0ea2`.
- `HHO_SUPPORT_LEMMA_PROOF_SKETCH_v0_1.md`: full; SHA-256 `326f9645c71cf44b429f30581c61dae8d99bf5ef216a262686a9076a64491f3d`.
- `HHO_SUPPORT_LEMMA_CHATGPT_CROSS_REVIEW_v0_1.md`: full; SHA-256 `9981f634d898f5b28951a8ae12151cd248a0fb16f1139123231b029768c32d08`.
- Local snapshot `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`: SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`; inspected §§6.12, 6.16, 6.17 and relevant general Weil definitions. The governing adopted tag/release was not independently verified.
- Secondary source crosswalk `H3_SEVERN_V2_SUCCESSOR_AUDIT_PART3_CROSSWALK_CLAUDE_v0_1.md`: targeted §4 and §3; SHA-256 `681efda7f71fcacc2be9f67af0e520151660d570090bba0b9ad46dcd5036e110`. It reports Severn v2 `hexagon:2610.00387v2`, §3.2 and Proposition 7.1, but the actual v2 PDF was not materialized in this review. The Hexagon landing page confirms that v2 is publicly listed, not the content of its proof.

## 2. Obligation (a): injective evaluation / Hodge realization — ACCEPT

Let `M_Q=H¹(C,Q)`, `U_Q` a nonzero irreducible rational `Q[G]`-module, and `W_Q=Hom_{Q[G]}(U_Q,M_Q)`. Treat `U_Q` as a weight-zero rational Hodge structure of pure type (0,0). Then W inherits a weight-one Hodge structure and for each `0!=u∈U_Q` the evaluation

`ev_u: W_Q → M_Q`, `f ↦ f(u)`

is a Hodge morphism. If `f(u)=0`, `ker(f)` is a G-submodule containing u. Irreducibility forces `f=0`. Thus ev_u is injective.

A polarizable weight-one rational Hodge substructure of `H¹(C,Q)` determines an abelian factor up to isogeny. Strictly, H¹ is contravariant: the sub-Hodge structure first corresponds to a quotient; using the Jacobian polarization and Poincaré complete reducibility it is isogenous to an abelian subvariety. The pullback of the Jacobian polarization is a rational polarization of W. No geometric dominance condition (D) is required for this implication.

## 3. Obligation (b): Morita-form scalar — ACCEPT AS PROOF DRAFT

With the assumed splitting `End_{Q[G]}(U_Q)=K`, compatibility of the Q-symplectic cup pairing E with the K-action, and a G-invariant positive K-Hermitian form h_U, Schur–Morita gives the sesquilinear factorization (modulo the common trace/δ normalization)

`E|_{U⊗_K W} = Tr_{K/Q}(δ^{-1} h_U ⊗ h_W)`.

Hence, on the image of evaluation at u,

`(ev_u)^* E = Tr_{K/Q}(δ^{-1} h_U(u,u) h_W)`,

where `h_U(u,u)∈Q_{>0}`. Consequently, the K-Hermitian polarization class of the evaluated abelian factor is that of `q h_W` for `q=h_U(u,u)` times any fixed **rational** trace/δ normalizing factor. Since `rank_K W=8`,

`det(q h_W)/det(h_W)=q⁸=N_{K/Q}(q⁴)`;

this scalar cannot alter the discriminant norm class. This proves the desired transfer **provided the Schur–Morita factorization and adjunction are shown with the actual E/h conventions**. A K-valued nonrational factor or an arbitrary non-selfadjoint projector must not silently be substituted for q.

The underlying Rosati compatibility also follows algebraically from the factorization: adjunction of precomposition by `a∈K` is precomposition by `bar(a)` because h_U is K-Hermitian. No general End⁰=K hypothesis is needed when comparing exactly the Jacobian-induced polarization. Nevertheless, the exact h convention and the v2 target factor need an owner-text comparison.

## 4. Obligation (c): generic End⁰=K — CONDITIONAL, NOT SIMPLY EDITORIAL

If (D) means the period map has maximal differential rank `16` onto the irreducible 16-dimensional unitary Weil moduli space, the family has Zariski-dense (indeed locally open) period image. Generic End⁰ of that moduli problem is K because the generic Mumford–Tate group's commutant is K. Its Rosati-fixed subalgebra is Q, giving NS_Q rank one. This standard moduli argument still needs its hypotheses stated: source target, irreducible component, generic Mumford–Tate group, and how the target factor is polarized. It is unnecessary when using the same Jacobian-induced polarization on both sides, but required to compare *arbitrary* K-compatible polarizations.

## 5. Obligation (d): Severn owner matching — OPEN

The local v0.2 §6.16 already states the exact desired comparison for W5 and keeps the general Proposition 5.1 as EXT-CLAIM. A secondary v2 crosswalk identifies Proposition 7.1 as an **explicit K-linear or K-antilinear, rational-scalar identification** of the polarized factor with the parabolic cup form, using a Rosati-selfadjoint rank-one projector and an internal v2 Lemma 7.2. This secondary report is not a substitute for a direct reading of the governing v2 PDF and the precise definition of (D). In particular, the notation `ev_u` by itself does not establish equality with Severn's chosen factor/projector unless the correspondences are matched.

## 6. Revised dispositions and minimal remaining check

| Item | Assessment |
|---|---|
| ev_u injective weight-one Hodge embedding and induced polarization | SESSION THM — CHECKED under rational irreducibility |
| Global Schur–Morita form is rationally proportional to ev_u-induced polarization | SESSION proof draft, algebraically justified; convention/adjunction identity still to be written explicitly |
| p-inert defect-zero multiplicity lattice norm support | Conditional SESSION THM, unchanged |
| (D) implies generic End⁰=K / NS_Q=Q | Conditional standard moduli argument; owner-specific verification needed only for arbitrary polarization matching |
| Match to v2 §3.2/Prop 7.1/Lemma 7.2 | OPEN until direct source comparison |
| `(L)+(D) ⇒ [disc]=[1]` | OPEN |

**Minimal next action:** Compare a single equation at the level of rational Hermitian forms:

`(ev_u)^* E_C = Tr_{K/Q}(δ^{-1} q h_W)` for `q∈Q_{>0}`,

with v2 Proposition 7.1 Steps 2–4 and the normalization in §3.2. Record the factor `q`, the K/antilinear convention, and the rank-one projector. This is much cheaper than a new integral parabolic-cup calculation or any expensive numerical campaign.

No adopted HCG, RTG or HHO scientific file was modified.
