# HHO — Independent mathematical review of Claude Support Lemma Addendum 2

**Date:** 2026-11-03  
**Status:** `[SESSION]` scoped review; noncanonical and not adopted.  
**Verdict:** Obligation (b) is **proof-checked** under its written representation-theoretic hypotheses. Obligation (d) remains an owner-dependent source-match. The norm-support theorem remains conditional on the previously stated local integral-Morita assumptions and this owner-match.

## 1. Provenance and reading extent

- Read completely: `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (2).md`, 172 lines, SHA-256 `cba601da2d1c8f4bb9406c5293b08566a0eb21d777ab40210d5df7d4699c5b3f`.
- Checked its successive local copies: original 80 lines SHA-256 `5c70ef22fbcd99173434a30da3ff7fbf1e69e2c0002243a81f5fe7fd248d9597`; Addendum 1 copy 123 lines SHA-256 `e7059f78e1695cabdbe41d084de09f3aa41d8b26c9eb6fd5d2f240060f4b0ea2`. Addendum 2 preserves the exact Addendum 1 byte prefix.
- Inspected targeted §§6.16–6.17 of local `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`, SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`, **not the complete DSN** and **without verifying the adopted tag or release record in a repository**.
- Sought Severn v2 `hexagon:2610.00387v2`; the version listing is externally visible, but direct PDF access failed (cache miss/download failure). **Severn §3.2 / Proposition 7.1 Steps 2–4 / Lemma 7.2 were not read from the governing source in this review.** Earlier crosswalk notes are secondary only.

## 2. Standalone theorem: a cup-induced Hermitian Morita pairing

**[SESSION — THM, mathematical implication checked]** Let `K/Q` be imaginary quadratic with nonzero skew `delta in K` (`bar(delta)=-delta`). Let `G` be finite, `U` a nonzero irreducible rational `Q[G]`-module with `End_{Q[G]}(U)=K`, and `h_U:U×U→K` a positive `G`-invariant Hermitian form, linear in the first argument. Let `(M,E)` be a rational G-module with a nondegenerate G-invariant alternating bilinear form E. Set `W=Hom_{Q[G]}(U,M)`, with K-action by precomposition.

Then there exists a **unique** K-Hermitian form `h_W` on W such that

```
E(f(u), f'(u')) = Tr_{K/Q}(delta^{-1} h_W(f,f') h_U(u,u')),
```

for all f,f'∈W, u,u'∈U. For every `u ≠ 0`, with `q=h_U(u,u)∈Q_{>0}`, its evaluation map satisfies

```
(ev_u)^*E(f,f') = Tr_{K/Q}(delta^{-1} q h_W(f,f')).
```

If M is `H^1(C,Q)` for a smooth projective curve and E is its cup polarization, the evaluation is an injective morphism of polarized rational weight-one Hodge structures (up to the explicitly displayed q-factor). Consequently h_W is nondegenerate and polarizing in the corresponding convention. For rank_K W=8, `det(q h_W)/det(h_W)=q^8=N_{K/Q}(q^4)`.

### Proof audit

1. `Tr(h_U)` is a G-invariant nondegenerate Q-bilinear form, so it identifies U with U*. By the commutant hypothesis, `Hom_{Q[G]}(U,U*)` has dimension 2 over Q.
2. The map `c∈K ↦ B_c(u,u')=Tr(c h_U(u,u'))` is Q-linear and injective: for fixed `u'≠0`, the values of `h_U(u,u')` as u varies fill K, and the trace pairing K×K→Q is nondegenerate. Thus c parametrizes **all** G-invariant rational bilinear forms on U.
3. `B_{f,f'}(u,u')=E(fu,f'u')` is G-invariant and hence equals a unique `B_{c(f,f')}`. This gives K-linearity in f and conjugate-linearity in f'.
4. Alternating E implies `c(f',f)=-bar(c(f,f'))`; therefore `h_W=delta c` is Hermitian. The displayed universal cup identity follows by substitution, independently of any guessed tensor/cup factorization.
5. For fixed u, h_U(u,u)=q positive rational, so evaluation gives the second identity. Evaluation is injective because ker(f) is a G-submodule containing u, hence f=0 by irreducibility. With U of Hodge type (0,0), it is a Hodge morphism. Pullback of the Jacobian cup polarization polarizes this Hodge subspace.
6. The adjoint of precomposition by `a∈K` equals precomposition by `bar(a)` because `h_W(af,f')=h_W(f,bar(a) f')`. This checks the Rosati property directly.

The result needs the stated endomorphism-field and positive-Hermitian assumptions. No claim is made that **every** field-K coefficient representation automatically satisfies them without checking the actual Schur algebra and rational model.

## 3. An explicit rank-one projector, reducing owner obligation (d)

Let `q=h_U(u,u)`. The K-linear orthogonal projector onto the K-line K·u in U is

```
P_u(x) = h_U(x,u) u / q.
```

It is idempotent and h_U-selfadjoint. On the U-isotypic rational Hodge space `U⊗_K W`, the Rosati-selfadjoint operator `P_u⊗id_W` has image

```
K u ⊗_K W = ev_u(W).
```

Thus **any owner factor defined by this specific Hermitian rank-one projector** is exactly the evaluated factor at the Hodge/rational level (up to isogeny). If the owner uses a conjugate K-structure, the Hermitian matrix is conjugated and its rational determinant is unchanged.

This calculation substantially reduces (d), but does not identify Severn's *actual* named projector or polarization. Those are still to be verified from the governing primary text rather than inferred from the secondary HCG summary.

## 4. Scope of normalization independence

The relation `E=Tr(c0 H)` with the **same** alternating E and K-Hermitian H forces `bar(c0)=-c0`. The space of skew K-elements is the 1-dimensional Q-line `Q delta^{-1}`; hence the resultant H differs from h_W by a Q-scalar. In even K-rank 8 this scalar changes determinant by a norm. K-antilinear reidentification conjugates h_W without changing its rational determinant.

**Important limit:** This proves independence of representations/trace normalizations for a **fixed polarization E**; it does **not** show that arbitrary different K-compatible polarizations have the same discriminant. Comparing unrelated polarizations requires an additional property such as generic `NS(A)_Q=Q` / `End^0(A)=K`, and verification of its hypotheses. The claimed irrelevance of (c) holds only when the owner's polarization is indeed Jacobian-induced (up to rational scale/isogeny).

## 5. Owner record consistency and remaining obligations

Local HCG v0.2 §6.16, `HCG-EXT-PO6`, records:

- Schur–Morita tensor form and Rosati-fixed rank-one projector;
- equality of the resulting polarized-factor discriminant with the parabolic Hermitian determinant **CHECKED for W5**, under its certified cup/polarization comparison;
- general identification beyond W5 as **PROPOSED/PARTIAL**;
- §6.17 explicitly says Severn's own printed polarization conventions have **not** been matched.

The present proof gives a general algebraic replacement for the rational cup/Morita **factorization**, but it cannot, without v2, upgrade the owner statement about Severn's particular `A_sigma` and its polarization. The precise pending source check is: Severn v2 §3.2, Proposition 7.1 Steps 2–4 and Lemma 7.2. Determine whether its idempotent/projector equals P_u⊗id_W (or its conjugate), and whether it uses the restriction of the Jacobian cup polarization up to Q×.

### Disposition

| Item | Review status |
|---|---|
| (a) Evaluation/Hodge embedding and induced polarization | SESSION THM — CHECKED (previous review, unchanged) |
| (b) Cup-derived h_W and rational-scalar comparison | **SESSION THM — independently PROOF CHECKED**, under the written assumptions |
| Rosati rank-one projector image | SESSION THM — CHECKED as an abstract algebraic statement |
| (c) Generic End^0(A)=K/NS(A)_Q=Q | Not needed for the same induced polarization; otherwise conditional on the owner's (D) hypotheses |
| (d) Severn v2 `A_sigma` and polarization match | **OPEN — primary owner sections unavailable** |
| HHO-HYP-SUPPORT full target conclusion | **CONDITIONAL** on local integral form and owner comparison; do not adopt yet |
| `(L)+(D) => [det h]=[1]` | **OPEN** |

No repo branch, PR, HCG/R TG document, adoption record, tag, or PI-decision field was changed.
