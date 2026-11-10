# HHO Addendum 10 — independent review, local cancellation, and a normalization correction

**Date:** 2026-11-09  
**Scientific status:** `[SESSION]`. Noncanonical; no HCG/RTG change or PI adoption.  
**Decision:** The tame/unimodular lemma and the individual A4 translation cancellation are correct. The claimed **30/30 balanced split** `C3×F20` result for the faithful four-dimensional representation is **incorrect**: the quotient of two Gram determinants omits a factor `5^{m(χ)}` arising from the natural norm-five constant line in the permutation representation. Corrected outcomes: **27 split, 3 nonsplit of class [5]** among the 30 balanced cases. These three counterexamples all generate the entire nonabelian group, have all branches effective, parabolic dimension 8 and balanced signature (4,4). They do **not** satisfy dominance (D), as they have only four branch points.

## Sources and extent of verification

- `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (10).md`: read the full Addendum 10 (§A10.0–A10.6) and checked the earlier source section relevant to the cancellation/locality formula. File SHA-256 `593ca8a82325d38aa5ea20d5534dd6378216e3c0ba6785de6a0ee440993d5ec9`, 643 lines. The preceding Addendum 9's 555 lines are a byte-exact prefix (SHA-256 `486288f5cc68ebd08c1c835e8bf5f12dfdcd8af45f2523b1c9a7b74fe0a7bc44`).
- `HHO_F20_TESTS_v0_1.zip`: read the full `f20_faithful.py` and its output, `f20_check.py`, and the manifest; ZIP SHA-256 `0bc778a422b9b10ee732b524e7f0fc95b5de6e28b2ced66c198cb6ff2ba5ee84`. **Five present files validate; two manifest-listed dependencies (`generic_engine.py`, `cyclic_disc_claude.py`) are not bundled**.
- Recovered both dependencies with matching **exact SHA-256 hashes** from the older, intact `HHO_A8_PARITY_AND_NPL_COUNTEREXAMPLE_REVIEW_v0_1.zip`; did not edit them. Ran the supplied original `f20_faithful.py` unchanged, with **byte-exact reproduction** of its 40-row frozen output (SHA-256 `6a3b4623ec5cc755d4c93fdb9c74686831a549f136193236aa34bf2546e61e01`).
- An independent exact-rational `Q(ω)` implementation reconstructs each local factor for the **actual four-dimensional coefficient form**, checks the Chevalley–Weil signatures and product-one/generation of every tuple, and compares 40/40 locality products to the corrected Gram representatives by checking their ratios belong to `N_{K/Q}(K×)`. This code imports **no HCG Gram engine**. A further direct, correctly polarized `A4` parabolic Gram computation (a separately adapted coefficient-form implementation of the existing cocycle cup algorithm) independently reproduces the corrected 5-adic parities in **all 40/40 source tuples**. The three balanced nonsplit cases have direct Gram determinants **405, 135, 1125**, respectively, and signature (4,4).
- The original HCG locality proof is not re-proved in this review. Its previously recorded two-AI CHECKED implication is used as a named dependency.

## 1. Verified local linear algebra: lattice discriminant vs cokernel length

Let `p≡2 mod 3` be inert, `R=O_{K,p}` the unramified quadratic DVR, `Λ` an integral, nondegenerate Hermitian `R`-lattice with `gΛ=Λ`. Put `E=im(1−g)` and `Λ_E=Λ∩E`. Since `(1−g)|E` is invertible over `K_p`, `(1−g)Λ_E` has finite index in `Λ_E`. Write `D_E=Λ_E^#/Λ_E`, using the Hermitian dual of the *induced* integral form.

For an `R`-basis of `Λ_E`, let `a=det(h_0|E)` and `b=det((1−g)|E)`. Since `R` is an unramified DVR with uniformizer `p`, Smith normal form gives the **exact integer identity**

`v_p(a) − v_R(b) = length_R(D_E) − length_R(Λ_E/(1−g)Λ_E)`.

The mod-2 reduction of this identity is the local support criterion from the prior CHECKED locality theorem. It is not a new independent way to compute global discriminants: it *repackages the two local factors*, but it makes cancellation mechanisms visible. The lengths depend on the chosen integral model; the parity of the total norm class is invariant under the allowed Hermitian basis/normalization changes.

**Illustrative cases:**

| Local representation | Gram valuation | `(1−g)` cokernel length | Local `p`-parity |
|---|---:|---:|---:|
| `ρ4` on `A4` at untwisted 5-cycle, `p=5` | 1 | 1 | 0 |
| `ρ4⊗ω^k` at an `F20` element with `k≠0`, `p=5` | 1 | 0 | 1 |
| Rank-one `−1`, `p=2` with unit Gram | 0 | 1 | 1 |
| Rank-one `G34` reflection line, `p=2`, root norm 6 | 1 | 1 | 0 |

The first line confirms Claude's reported `A4` cancellation **at an untwisted translation**. The second line is the missing effect in the previous 40-row class computation.

## 2. Exact source of the missing factor five

Let `P` be the five-point permutation representation of `F20 = C5 ⋊ C4`. Over `K=Q(ω)` there is an orthogonal decomposition (for the standard positive dot product)

`K^5 = K·(1,1,1,1,1) ⊥ A4_K`.

The first line has **Gram norm 5**, not 1. Hence for `g=(ω^k,f)` the corresponding coefficient representations split orthogonally as

`ω^k P = (ω^k·1) ⊕ (ω^k ρ4)`, but the coefficient forms are `h_total = (5 h_χ) ⊕ h_ψ`.

The engine calculates `D_total` with `h_total=I_5`, and `D_χ` independently with the **unit** rank-one form. At the parabolic cohomology level, let `m_χ=dim H¹_par(χ)`. Then, **modulo a norm arising from changing cohomology bases**, the correct relation is

`[det h_ψ] = [D_total/(5^{m_χ} D_χ)]`.

The submitted program instead labels `D_total/D_χ` as the four-dimensional coefficient determinant. For the present connected tuples, the number `t` of local `C3` labels `k≠0` satisfies

`m_χ = t−2`.

Therefore an **odd** `t` changes the inert-5 class by `[5]`. Scaling the *four-dimensional* coefficient form cannot remove it: it would multiply the 8-dimensional parabolic determinant by an eighth power, which is a norm.

## 3. Independent local formula and the corrected 40 cases

For an affine permutation `f` of five points, all its cycle lengths belong to `{1,2,4,5}`; none is divisible by 3. Write `ℓ` for the cycle lengths of `f`.

- If `k=0`, `E=im(1−ρ4(f))` is a direct sum of cycle root lattices. Each length-ℓ cycle contributes both Gram determinant and `(1−f)|E` determinant equal to ℓ; hence `Δ_ψ(0,f)=1`.
- If `k=1` or `2`, `ω^kρ4(f)` has **no eigenvalue 1**, hence `E=A4_K`, with `det h_{A4}=5` and

`det(1−ω^kρ4(f)) = (∏cycles(1−ω^{kℓ}))/(1−ω^k)`.

Thus the **independently evaluated local factor** is

`Δ_ψ(k,f)= 5(1−ω^k)/∏cycles(1−ω^{kℓ})` for `k≠0`.

Every factor `(1−ω^j)` has only ramified-3 support; therefore at the inert prime 5 the contribution is 1 per `k≠0`, and zero for `k=0`. The 5-adic parity of the full determinant is **`t mod 2`**. This local proof is independent of the source code's quotient trick.

Replaying all 40 frozen tuples and independently calculating exact ages and local products gives:

| Signature | Split (`5` even) | Inert-5 nonsplit | Total |
|---|---:|---:|---:|
| (4,4) | **27** `[1]` | **3** `[5]` | 30 |
| (5,3) or (3,5) | 8 negative, no inert-5 support | 2 negative, with inert-5 support | 10 |

All 40 local products are rational and their ratio to `D_total/(5^{mχ}Dχ)` is a norm. All 40 tuples generate the entire `|G|=60` group, have product one, dimension 8, and have signatures matching independently calculated Chevalley–Weil ages.

### Three explicit balanced nonsplit examples

| Local tuple `(k,(a,b))` with affine `(a,b): x↦ax+b (mod5)` | Source-printed `D_total/Dχ` | Corrected Gram representative | Direct local product |
|---|---:|---:|---:|
| `[(2,(2,1)),(0,(1,2)),(2,(1,2)),(2,(3,3))]` | 81 | **81/5** | **125/3** |
| `[(1,(2,2)),(0,(1,2)),(1,(4,2)),(1,(2,0))]` | 27 | **27/5** | **125/9** |
| `[(2,(2,0)),(2,(2,0)),(2,(4,1)),(0,(1,1))]` | 9 | **9/5** | **125/9** |

All three are class **[5]** in `Q×/N_{K/Q}(K×)`; each is a genus-zero 4-branch nonabelian, faithful, all-effective example with parabolic signature `(4,4)`. For the first tuple, `(125/3)/(81/5)=625/243 = N_{K/Q}(25/(1−ω)^5)`, an explicit norm ratio.

**Limitation:** Four effective branch points imply the family base dimension is `4−3=1`, not 16. These **do not satisfy dominance (D)** or the as-yet-uncertified supplier condition (L). They are a decisive counterexample to the blanket assertion that every such faithful balanced F20 tuple has split discriminant, not to `(L)+(D)⇒[1]`.

## 4. Decisions, necessary corrections, and next test

1. **Tame/unimodular lemma:** retain `[SESSION THM — two-AI CHECKED]` under the previously stated shared-self-dual-lattice hypotheses. The present examples do not contradict it: `A4` is not self-dual at 5.
2. **Translation `A4` cancellation:** `[ALG — CHECKED]`, `a=b=5` at `g=(1,u)`. Do **not** elevate this to a general exclusion of `p=5` support for the whole ψ-local system.
3. **Faithful `C3×F20` 40-row conclusion:** **RETRACT** “30/30 balanced split”; correct to `27/30 split, 3/30 [5]`. The old Gram output itself is reproducible, but it is a quotient with a missing Hermitian scaling factor, not the correct ψ determinant class. The correctly polarized direct `A4` Gram calculation independently confirms the correction in **40/40** cases (three balanced nonsplit determinants: **405, 135, 1125**).
4. **Local cancellation formula:** record as an exact **local lattice identity** (`[THM]` for the identity), with the global parity corollary conditional on the CHECKED locality theorem. It is a diagnostic identity, not by itself a complete no-go theorem.
5. **New example:** `[SESSION THM/NUM]` faithful nonabelian, balanced **nonsplit [5]** examples in dimension 8 with only 4 branch points; first genus-zero coherent examples in the specified coefficient family, **not** dominant.
6. **NPL:** remains withdrawn/refuted. **HHO-Q-LOCAL-CANCEL:** its length-parity expression is now an exact identity; the open scientific problem is what geometrically forces **evenness** of the sum under `(L)+(D)`.
7. **HHO Support Lemma / PO-6 / canonical records:** no change. No classification/adoption is inferred from a script passing.

**Independent direct-form test completed:** The `A4`-basis calculation with invariant coefficient Gram `I4+J4` reproduced all 40 corrected 5-adic parities and all 40 Chevalley–Weil signatures. The remaining external obligation is a second-family review of the correction and its impact on the proposed faithful F20 control; the dominant `(D)` regime and the general supplier hypothesis `(L)` remain OPEN.
