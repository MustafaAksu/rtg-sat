# HHO — Independent review of Addendum 11: faithful C3 × F20, actual A4 coefficient form, and the 5-adic local mechanism

**Review date:** 9 November 2026  
**Status:** `[SESSION]`, noncanonical; no PI scientific adoption, no HCG/RTG edits.  
**Source basis:** Claude `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (11).md` (targeted Addendum 11, lines 644–728; earlier 643 lines checked for unchanged byte prefix, not scientifically re-reviewed), supplied `HHO_A4_DIRECT_v0_1.zip` and hash-matching antecedent numerical source packages.  
**External theorem dependency:** previously two-AI-checked parabolic Hermitian discriminant locality formula. Its governing owner proof and its applicable conventions were not re-proved in this review.

## Decision

1. **Addendum 11's retraction is correct.** The former 30/30 split finding resulted from dividing a 5-point permutation-system determinant by a *unit*-normalized rank-one determinant. The orthogonal constant vector `(1,1,1,1,1)` has squared norm 5, so the proper quotient includes `5^{m_chi}`, where `m_chi=t−2`.
2. **Direct A4-form confirmation:** the uploaded 40-row direct Gram output was replayed **byte-for-byte** with the exact prior-source dependencies. Balanced cases: 27 class `[1]`, **3 class `[5]`**, all signature `(4,4)`. Their actual direct Gram determinants are **405, 135, and 1125**.
3. **Independent implementation:** a newly written local-factor and finite-group implementation (SymPy for rational matrices; exact rational arithmetic for `Q(omega)`) reconstructed all **40/40** source norm classes without importing the HCG Gram or locality code, checked all 40 product-one tuples and that each generates all **60** elements, and checked all **60** possible local group elements.
4. **General conditional theorem for this exact rank-four coefficient representation:** at the inert prime 5, `v_5(det h_par) ≡ t (mod 2)`, with `t=# {j : k_j != 0}`. For the target signature `(4,4)` and `dim_K H_par = 8`, the full norm class is `[5^t]`. This holds for any tuple satisfying the same monodromy, cohomological, and positivity conditions, not just the 40 random tuples. The global statement uses the parabolic locality theorem.
5. **Dominance obstruction:** in any genus-zero rank-4 local system with `dim H_par=8`, all effective local movement ranks satisfy `sum c_j=16`, so `N_eff<=16`. Dominance to a 16-dimensional period space requires `N_eff>=19` under the inherited (D) model. Therefore **this exact rank-4 representation cannot be made (D)-dominant by adding branch points while keeping the target rank eight**. The global `(L)+(D) => split` question remains OPEN.

## 1. Source identities and computational limitations

| Artifact | SHA-256 / identity | Actually verified |
|---|---|---|
| Uploaded Addendum 11 Markdown | `77252c32b8994cacc801a2f0358222d977310273db599148c29b045e4ea8c850` | 728 lines total, Addendum 11 targeted |
| Addendum 10 prefix (643 lines) | `593ca8a82325d38aa5ea20d5534dd6378216e3c0ba6785de6a0ee440993d5ec9` | Byte-identical prefix |
| `HHO_A4_DIRECT_v0_1.zip` | `10ba31592a123728f97d3ae3fd8ec5973f6f0848a67b00c92ac9952da0218f59` | Both included entries hashed |
| `a4_direct.py` | `cd548934c63af78e688d0697cd23da05fe602d09de3df9bb4a0d28d03616bc9d` | Read fully, replayed |
| `a4_direct_out.txt` | `8d54d6622be6cef8a5568df5bee2285f780834d446c23bd3c1eae0b9b9ba6f89` | Replayed bytes exactly |
| `generic_engine.py`, `cyclic_disc_claude.py` | `66f2c253...6e46`, `da76a25f...6e61e` | Exact full hash matches antecedent supplied ZIP |
| Source tuples | `f20_faithful_out.txt` from `HHO_F20_TESTS_v0_1.zip` | Frozen tuples used unchanged |

**Archive limitation:** the newly uploaded A4 ZIP lists four files in its manifest but physically contains only two (`a4_direct.py`, `a4_direct_out.txt`). The two missing engine files were recovered **unchanged and with full SHA verification** from the earlier `HHO_ADDENDUM10_F20_NORMALIZATION_CORRECTION_v0_1.zip`. The 40 tuple input was recovered unchanged from `HHO_F20_TESTS_v0_1.zip`. The package attached to this review bundles all inputs for repeatability.

The direct source `LocalH0` rewrites the cup product with the actual invariant `H0` but reuses the generic engine's cocycle-space algorithm. Its exact replay is thus a **same-engine replay of the new Gram implementation**, not a fully independent third cohomology engine. The new local-factor implementation is algebraically independent but invokes the same prior **mathematical locality theorem**.

## 2. Exact coefficient-form distinction

Let `F20=F5 ⋊ F5^×` act on five letters by affine permutations. The permutation module over `K=Q(omega)` decomposes as

`K^5 = K·(1,1,1,1,1) ⊥ A_{4,K}`.

The constant-line norm is 5, while the `A4` basis `f_i=e_i−e_4`, `i=0,...,3`, has Gram

`H0=I4+J4`,  `det(H0)=5`.

The parabolic multiplicity of the constant-line character `chi=omega^k⊗1` is `m_chi=t−2`. Hence the exact norm-class correction to the previous quotient is

`[det h_psi] = [D_total/(5^{m_chi} D_chi)]`.

There is no allowable substitution of the unit form for the *restricted* coefficient form. This is not a change to representation identity; it is a change to the determinant-normalization bookkeeping.

## 3. New family-wide 5-adic parity theorem

**`[SESSION — THM, conditional on the locality formula]`.** Let `sigma=omega^k⊗rho4`, where `rho4` is the faithful 4-dimensional `A4` constituent of the five-letter affine permutation action of `F20`; set `h0=I4+J4`. For each local monodromy `(k_j,w_j)`, define `E_j=im(1−sigma(k_j,w_j))` and `Delta_j=det(h0|E_j)/det((1−sigma(k_j,w_j))|E_j)`. Then:

`v_5(Delta_j) ≡ 1_{k_j!=0} (mod 2)`.

**Proof.** If `k_j=0`, every cycle of the permutation `w_j` of length `ell` contributes an orthogonal moving `A_(ell−1)` summand, with Gram determinant `ell` and with determinant of `1−w_j` restricted to its moving part also `ell`. Thus the local ratio is 1 in a cycle-root basis (and changes by a norm under an arbitrary K-basis change).

If `k_j!=0`, the scalar `omega^{k_j}` has order 3 while eigenvalues of the finite group `F20` on `A4` have orders dividing 1,2,4,5. Hence 1 is not an eigenvalue of `omega^{k_j} rho4(w_j)` and `E_j=A4_K`. Its Gram determinant is 5. Modulo the inert prime over 5, every eigenvalue of `rho4(w_j)` has prime-to-5 order dividing 4, so no eigenvalue equals `omega^{-k_j}`; thus the denominator is a 5-adic unit. Therefore `v5(Delta_j)=1`.

For other inert primes the untwisted ratio is a norm and the twisted denominator is supported only at the ramified prime 3: possible twisted eigenvalue orders are 3,6,12,15, and their relevant cyclotomic values at 1 have no inert-prime support. The target `dim_K H_par=8` has global sign `(-1)^4=+1`. A balanced `(4,4)` Hermitian form has positive determinant. The locality theorem gives

`[det h_par]=[5^t]`, `t=#{j:k_j!=0}`.

This **does not** establish (D) or (L), and does not claim that every such tuple produces an abelian eightfold with the necessary period dominance.

### Independent arithmetic controls

- Finite group order: `|C3×F20|=60`; **each of the 40 frozen tuples** has product one, generates the full group and has no identity branch element.
- Global norm classes computed afresh from local matrices over `Q(omega)`: **40/40 agree** with frozen direct-Gram classes.
- All **60 local group elements** examined: 40 twisted elements have odd 5-adic local class; 20 untwisted elements have even local class. Four of the untwisted elements have a ratio with **valuation 2** in the particular nonprimitive basis used by the independent checker; this is a norm-square and does **not** contradict the exact ratio 1 in a primitive cycle-root basis.
- Other tested inert primes 2 and 11 have even valuations for all 60 local factors.
- Balanced frozen tuples: **27 split and 3 nonsplit**; three nonsplit determinant values exactly **405, 135, 1125**.

## 4. Consequences for the HHO programme

The correction is a **positive counterexample** to any bare hypothesis that faithfulness, nonabelian monodromy and effective branching force split discriminant. The group is nonabelian, the coefficient representation is faithful, and the local forms have genuine inert-5 support.

However **dominance cannot be tested using the same coefficient rank**. For genus zero with no global invariants:

`dim H_par = sum c_j − 2d = 8`.

Since `c_j>=1` at every effective local branch, `N_eff<=2d+8`. At `d=4`, `N_eff<=16`, while dominance onto a 16-dimensional target requires `N_eff>=19` (necessary, not sufficient). Consequently no genus-zero rank-four monodromy tuple can serve as an (H)-dominant rank-eight datum in this model, irrespective of how many marked points are formally added.

**Recommended next search:** increase coefficient rank before seeking (D), keep the local parity computation as an independent early filter, and require all the gates in the correct order: `N_eff>=19`, `sum c_j=2d+8`, balanced ages/signature, nontrivial 5-adic local parity, then supplier (L), period-map rank (D), and polarization comparison. In the stronger inherited nonsplit `(H)` screen, degree lower bounds from the HCG programme are additional conditional dependencies, not independently adopted in HHO.

## 5. Scoped dispositions

| Item | Proposed scientific status |
|---|---|
| A10.4 `30/30 split` | **RETRACTED** |
| Direct A4 numerical results (27/30 split, 3/30 `[5]`) | **NUM — independently replayed and local formula cross-checked** |
| Full-group generation/product-one of the 40 tuples | **COMPUTATIONAL CHECKED** in an independent group implementation |
| General local 5-parity law for this `C3×F20` representation | **SESSION conditional THM** |
| Local lattice/cokernel length identity | **ALG THM**, already supported by exact Smith normal form; not re-proved here |
| (L)+(D) ⇒ split | **OPEN** |
| Severn canonical representation/polarization match | **OPEN** — requires owner source identity and text |

No changes were made to the original evidence, HCG v0.2, any RTG adopted DSN, PO-6 or PI decision fields.
