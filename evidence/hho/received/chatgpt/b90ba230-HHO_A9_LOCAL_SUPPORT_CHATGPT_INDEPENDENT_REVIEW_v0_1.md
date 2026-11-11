# HHO — Addendum 9 cross-review: local inert-prime support after the failure of Neighbour Parity Law

**Date:** 2026-11-04  
**Status:** [SESSION], noncanonical HHO research. No HCG/RTG adoption, no PI approval, no change to PO-6 or Severn A/B/C.  
**Scope:** genus-zero finite-unitary parabolic local systems over `K=Q(sqrt(-3))`, target `dim_K H^1_par=8`, signature `(4,4)` for the rank-one corollary. General local support results assume the independent locality theorem stated below; they do not establish its governing source identity.

## 1. Source identity and reading extent

- **Current Claude source:** `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (9).md`, SHA-256 `486288f5cc68ebd08c1c835e8bf5f12dfdcd8af45f2523b1c9a7b74fe0a7bc44`: Addendum 9 (§A9.0–A9.4, lines 483–555) read in full; earlier sections checked where necessary. The previous Addendum 8, 479 lines, is a byte-identical prefix, independently verified.
- **Current user computation:** `f20_check.py`, SHA-256 `4a449e11f09f76c2ea9574d226dd5e141e9e7c01b2767e30a254f976e9681820`: all 33 lines read; executed unchanged with the frozen motor sources, exit 0.
- **Recovered frozen motor:** `generic_engine.py` SHA-256 `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505` and `cyclic_disc_claude.py` SHA-256 `da76a25f57817fbeaf2b6deb749cda76cdefb5c8d59ec2d4b871a2778cf2afa9`, recovered unchanged from `HHO_A8_PARITY_AND_NPL_COUNTEREXAMPLE_REVIEW_v0_1.zip` (ZIP SHA-256 `b0a5b649212bb6f1cd88a73570880713913386f043c1285c9db611b31f860303`). The motor is **replayed, not independently reimplemented**.
- **Locality theorem proof review:** `H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md`, SHA-256 `41bc9997328cbc74a592ba9a899fd6cc30eb6e71656cc284c591ff05ac1878ee`; targeted §§0–1,3 read. This is a **second-AI session review of the proof**, not the full governing original `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md` (source hash prefix `0ec38558…`), which was not accessible. No adopted primary source is being inferred from the review.
- **HCG context:** local copy `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`, SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`; targeted §§6.7, 6.13–6.16 inspected, especially the distinction between the parabolic matrix and the polarized abelian factor. The governing adopted Git tag was not reverified in this session.

## 2. Computational verdict

`f20_check.py` executed unchanged with the restored, hash-verified engine. It returns:

```
chi: dim 8 det 1 sig (4, 4, 0) class [1]
omega(x)perm5: dim H1_par = 51  => m(psi) = 43
c_psi per branch [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4] sum 51 sum over chi-effective 40
```

The direct rank-one local calculation is independent of this motor: `chi` sees five `omega` and five `omega^2` branches, so its denominator is `((1-omega)(1-omega^2))^5=3^5`. In the quotient by norms, `[1/3^5]=[1]`. The difference from the motor's `det=1` is exactly `3^5=N((1-omega)^5)`, an allowed norm factor.

**Status:** HHO-CONJ-NPL as an unrestricted assertion is **REFUTED**; the counterexample has an odd degree-4 Brauer-neighbour multiplicity 43 but a split rank-eight parabolic discriminant. It is nonfaithful on `G=C3 × F20` and does not satisfy dominance `(D)`. Restricted statements remain OPEN.

## 3. Full mathematical statement of the previously checked locality formula

**[SESSION dependency — checked by two AIs in the 2026-10-29 review; original complete proof source unavailable]**

Assume:
- `g_1 ... g_N = I` are finite-order matrices over an imaginary quadratic `K`, preserving a fixed positive-definite coefficient Hermitian form `h0` on a `d`-dimensional `K`-vector space;
- there are no common global invariants;
- `E_j=im(1-g_j)`, `c_j=dim_K E_j`, and `Σ c_j=2d+2n`, so `dim_K H^1_par=2n`;
- the parabolic Hermitian form `h_par = vartheta*S`, where `vartheta` is a nonzero imaginary scalar, is the cup pairing under the stated left-action conventions.

Set `a_j=det(h0|E_j) in Q_{>0}` and `b_j=det((1-g_j)|E_j) in K×` in any matched `K`-basis of `E_j`. Then

    [det(h_par)] = [(-1)^n * Π_j (a_j / b_j)]

in `Q×/N_(K/Q)(K×)`. Equivalently, since `B=Π_j b_j in Q×`, the same class equals `[(-1)^n * (Π_j a_j b_j)]`. The sign `(-1)^n` is **essential for odd n**; at `n=4` it is +1. The product `Π(a_j/b_j)` is rational, although an individual `a_j/b_j` need **not** be rational. In the determinant proof, `(det H0)^2` and an adapted basis change contribute *norms only*. There is no untracked, potentially nonnorm global factor in this stated norm-class formula. **Exact determinants can differ by nontrivial norms**, e.g. `3^5` in the F20 test.

This records the exact mathematical hypothesis and claim of the reviewed proof. It is **not** a claim that the original owner text or Severn v2 polarization bridge has been independently obtained in this session.

## 4. [THM, conditional on locality] Rank-one class law

For `K=Q(omega)`, `dim_K V=1`, and target `dim_K H_par=8`, there are exactly 10 **effective** branch points. A positive coefficient form on V is `q in Q_{>0}`. Each moving-space determinant numerator is q, so their product `q^10=N(q^5)` is a norm. Every nontrivial local eigenvalue is in `mu_6(K)`. At an inert rational prime `p ≡ 2 (mod 3)`, the only `1-lambda` that is not a p-unit occurs at `p=2` with `lambda=-1`. Positive rational norm classes are detected by the parities of their inert valuations. Hence

    [det h_par] = [2^t],  t=#{j: chi(g_j)=-1}.

This statement requires the `(4,4)` signature (positive total rational determinant); it does not claim the class of arbitrary unbalanced Hermitian forms is positive. It proves that no inert p>=5 can be supported in **this rank-one class**. It does not rely on the Brauer tree or any neighbour multiplicity. **Status: SESSION THM, locality-conditional.**

## 5. [THM, conditional on locality] General inert-prime exact parity and necessary support

Let `p≡2 (mod 3)` be an inert rational prime, let `v_p` denote the normalized valuation on `K_p` (which agrees with `v_p` on rational scalars, since this extension is unramified), and use the `a_j,b_j` above. Then

    v_p(det h_par) ≡ Σ_j [v_p(a_j) - v_p(b_j)] (mod 2).

Here the left side means the rational representative of its norm class. The exact parity is basis-independent because a moving-space K-basis change multiplies `a_j` by `N_K/Q(det P)`, which has *even* p-valuation. For any nonidentity root of unity lambda, `1-lambda` is a p-adic nonunit iff lambda has **pure p-power order**. Thus:

    inert p-support => at least one nontrivial p-power-order eigenvalue
                      OR at least one moving-space Gram determinant of odd p-valuation.

This is a **necessary condition**, not an equivalence. Numerator and denominator contributions may cancel (example: a coefficient-metric-orthogonal order-2 transposition has root norm 2 and `det(1-g)|E=2`, hence local factor 1 at p=2 despite both potential triggers). Additionally, the parity of the individual Gram term can depend on rational rescaling of h0; the **sum** is invariant because `Σ c_j=2d+8` is even. Individual local factors may be K-valued, while only the total product is rational.

**Brauer scope correction:** Brauer block theory can affect the existence of a p-unimodular coefficient lattice and the reduction of moving spaces when p-power eigenvalues occur. It is too strong to claim that Brauer data enter *only* through unimodularity, or that a neighbour multiplicity can *never* be relevant after stronger hypotheses; the F20 example refutes only an unrestricted neighbour-parity rule.

## 6. [SESSION — new stronger local unit lemma] Tame eigenvalues + a perfect coefficient lattice

Let `R=O_(K,p)` (unramified DVR for inert p), and suppose a finite-order unitary g preserves a **self-dual** R-lattice `(Lambda,h0)`. If every nontrivial eigenvalue of g has order **not** equal to a power of p, then `det((1-g)|E)` is a p-unit. Write `A=1-g`, `Lambda_E=A Lambda`. Since `A` maps Lambda_E to itself and `det(A|Lambda_E)` is a unit, it is an R-automorphism of Lambda_E. For any x∈Lambda there is y∈Lambda_E with Ay=Ax, so x−y∈ker A; and ker A intersects Lambda_E trivially. Hence

    Lambda = ker A ⊕ Lambda_E.

Since g is unitary, this sum is h0-orthogonal. As Lambda is self-dual, both summands are self-dual, including the moving-space lattice Lambda_E. Therefore **the local Gram determinant and det(1−g)|E are p-units**; in an integral moving-space basis, `Delta(g)` is a p-unit. For an arbitrary K-basis it changes by a norm, so its valuation parity remains even.

**Proposed corollary:** At an inert p where the coefficient representation has a self-dual lattice, **if no branch monodromy has a nontrivial pure p-power eigenvalue then the local parabolic discriminant is split at p**. This is a strictly sharper, easily testable sufficient exclusion than listing both possible causes separately. It does not resolve cases where local p-power eigenvalues occur or where no self-dual coefficient lattice exists.

Status: SESSION THM, original proof presented here; **independent peer review pending**.

## 7. A correction to the previous cyclic sextic test census

`HHO_C6_C3S3_TESTS_v0_1.zip` has 55 balanced multisets (10 nonzero exponents whose sum is 30, so the rank-one signature is `(4,4)`). Exactly **two** fail to generate the full C6 monodromy image:

- `(2^5,4^5)` generates C3, not C6; its `m(chi4)=8` is nonnegative.
- `(3^10)` generates C2, not C6; its *formal* `m(chi4)=-2` is invalid as a genuine C6-isotypic H1 multiplicity.

Thus the correct count is **55 formal / 53 connected C6 covers**. The source's reported 54 arose from excluding only the negative-multiplicity row; it was not the connected-cover census. The exact cyclic parity law is valid for all 55 formal rank-one local systems with balanced Hodge numbers; its **connected-C6-cover** scope has 53 cases.

The new independent checker `independent_a9_exact_check.py` verifies all 55 exact Eisenstein products, rank-one parity classes, two disconnected shapes, F20's rank-one local denominator `3^5`, and a p=2 local cancellation example. It imports **none** of the HCG engine.

## 8. Disposition and next tasks

| Item | Decision |
|---|---|
| Original NPL | **WITHDRAWN/REFUTED**; no automatic rehabilitation under (L)/(D) |
| F20 counterexample | **NUM CHECKED**, unchanged motor replay + independent rank-one denominator |
| Rank-one inert-support law | **SESSION THM**, conditional on the full locality statement |
| `HHO-LOCAL-SUPPORT` general necessary condition | **SESSION THM (locality-conditional)**; an explicit sufficient *split* criterion is given in §6 |
| New tame-unimodular local lemma | **SESSION THM — PROPOSED pending second reviewer** |
| Current C6 connected-cover count | **53, not 54** |
| Source of complete original locality proof | **UNAVAILABLE** (but detailed independent review present) |
| Severn's general polarized-family bridge / PO-6 | **OPEN** outside W5; no claim of adoption |
| `(L)+(D) => [1]` | **OPEN** |

**Next:** Have the independent reviewer check §6 (tame-unimodular local lemma) first. Then search for faithful, all-branch-effective, nonabelian K-valued representations with p-power local eigenvalues and/or no self-dual coefficient lattice, and test gluing parity there. The `C3 × F20` example should remain an immutable regression counterexample for any future universal neighbour law.
