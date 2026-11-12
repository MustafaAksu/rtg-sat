# HHO B1 — independent O2/O1 proof (ChatGPT)

**Date:** 2026-11-12. **Status:** [SESSION — THM, PROPOSED for receiving proof review]. **Scope:** no adopted claim, HHO register change, HCG re-pin or Severn claim acceptance. PI selected route B (prove O2 then O1).
**Owner pins:** HHO `hho-v0.2` (governing); HHO cites `hcg-v0.2`. HCG `hcg-v0.4` §6.24 has since adopted the algebraic locality theorem (CHECKED, two AIs), **not** its cup/polarization bridge. This record is not HCG owner science.

## 0. Source identity and reading extent

- Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality*, arXiv:math/0411119, directly inspected §§1.2, 2.2–2.4 (Cor. 2.2, Lemma 2.4, **Thm. 2.5 and its proof**) and §3 Prop. 3.1. Supplied ar5iv-print PDF, 27 pp., SHA-256 `3a70bd23136771e8aa3e0fb2708d9c51c6ad57f2e7086c7d8cb89c4309744627`. Published version numbers this formula Thm. 2.6.
- Dettweiler–Wewers, *Variation of local systems and parabolic cohomology*, arXiv:math/0310139v2, directly inspected §1.3, §4.3 and §6.1 **Prop. 6.1 and proof**. Original PDF, 28 pp., SHA-256 `108c89a25c62f98eb5aa3f2d81084b7f7f711da15a090168783d9a582921938f`. Its Prop. 6.1 is the cyclic-degree-three case, not a general proof of cup compatibility.
- HCG `hcg-v0.2`: `evidence/hcg/received/b69978bf-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md` §§2–3.4 (the exact `C,D,Z,B` formula); HHO `hho-v0.2`: `hho/HHO_SUPPORT_RESULTS.md` §§1–3, including `HHO-LEM-CUP-MORITA` and `HHO-THM-SUPPORT`. Claude's `HHO_B1_SOURCE_READING.md` SHA-256 `72683c0315adfb0075912a7e028a21ee9e9ee9ddbd714245dc448308596e5669` is advisory context.
- Severn's original propositions and a separate categorical reference for finite-map trace **were not read**. The present derivation uses DW's theorem and standard topological cup/trace functoriality, not an assertion imported from Severn. No novelty claim.

## 1. O2: HCG triangular B equals the DW06 sheaf cup form

**[SESSION — THM, conditional on DW06 Thm. 2.5.]** Work over `K=Q(omega)`. Let `g_1...g_N=1` be unitary on a positive Hermitian `(V,h0)`, with `h0` linear in its first argument and no common fixed vectors. Put
\[
E_i=\operatorname{im}(1-g_i),\quad Q_i=g_1\cdots g_{i-1},\quad
C(x)=\sum_iQ_ix_i,\quad Z=\ker C,\quad D(v)=((g_i-1)v)_i.
\]
For `x_i in E_i` let `A_i(x)=(1-g_i)^{-1}_{E_i}x_i` and `F_i(x)=sum_{j<i}Q_jx_j`. The HCG triangular form is
\[
B(x,y)=\sum_i h_0(Q_i^{-1}F_i(x)+A_i(x),y_i).
\]
DW uses a **right** action and a **dual-first** cup. Set `v·g=g^{-1}v` and `f_y(v)=h0(v,y)`, so `f_y·g^*=f_{g^{-1}y}`. For `x,y in Z`, the DW ordinary cocycle and dual cocycle have components
\[
v_i=g_i^{-1}x_i,\qquad v_i^*=f_{g_i^{-1}y_i},\qquad v_i'=A_i(x).
\]
The preimage rule holds: `(g_i^{-1}-1)A_i(x)=g_i^{-1}x_i`. Direct substitution into **DW Thm. 2.5** yields
\[
P_{DW}(y,x)=\sum_i h_0(A_i(x)-x_i,y_i)
 -\sum_{j<i}h_0((g_j\cdots g_{i-1})x_i,y_j). \tag{O2.1}
\]
For `R_{ji}=g_j...g_{i-1}=Q_j^{-1}Q_i`, the exact closure `Cx=Cy=0` and unitarity imply
\[
0=h_0(Cx,Cy)=\sum_i h_0(x_i,y_i)
 +\sum_{j<i}h_0(R_{ji}^{-1}x_j,y_i)
 +\sum_{j<i}h_0(R_{ji}x_i,y_j). \tag{O2.2}
\]
Combining gives **equality of forms on Z**:
\[
\boxed{P_{DW}(y,x)
 =\sum_i h_0(A_i(x),y_i)
 +\sum_{j<i}h_0(R_{ji}^{-1}x_j,y_i)=B(x,y).} \tag{O2}
\]
Both descend to `Z/D(V)`; HCG locality §3.3 independently proves `rad(B|Z)=D(V)`. A global orientation reversal may multiply the pairing by -1, harmless to even-dimensional determinant classes.

**Exact control:** `python3 -I evidence/hho/code/hho_b1_o2_exact_check.py` tests all 9 pairings on the three-dimensional cocycle space of `(omega,omega^2,omega,omega^2)` over exact `Q(omega)`: **9/9 PASS**, no HCG engine. This is a small regression check, **not** a proof.

## 2. O1: finite G-cover comparison with cup and trace

**[SESSION — THM, conditional on standard finite-cover Leray and cup/trace functoriality.]**
Let `f:Y -> X=P1_C` be a connected finite **G-Galois** cover of smooth projective curves, branch divisor D, `U=X-D`, and `j:U->X`. Put `A=f_* K_Y`.

**Stalks and cohomology.** Over U, `A|U` has regular G-fibre `K^G`; deck action and base monodromy commute. At a branch point with inertia subgroup I, its stalk is `K^{G/I}=(K^G)^I`. Consequently
\[
A=j_*(A|_U).
\]
Finite proper fibres are discrete: `R^q f_*K_Y=0` for `q>0`. Hence `H^1(Y,K)=H^1(X,A)`. For an absolutely irreducible K-representation `V_sigma` with `End_{K[G]}(V_sigma)=K`, semisimplicity and the corresponding central idempotent give
\[
e_\sigma A\simeq V_\sigma\otimes_K j_*\mathcal L_\sigma,\quad
e_\sigma H^1(Y,K)\simeq V_\sigma\otimes_K
H^1(X,j_*\mathcal L_\sigma),\qquad
\mathcal L_\sigma=\operatorname{Hom}_{K[G]}(V_\sigma,A|_U).
\tag{O1.1}
\]
The multiplicity sheaf has monodromy `sigma^vee`; switching to its conjugate isotypic component and the positive invariant coefficient metric fixes the requested sigma/dual convention. This is the natural finite-cover identification of the **parabolic** multiplicity space with `Hom_G(V_\sigma,H^1(Y,K))`, compatible with the Hodge structure induced from `H^1(Y)`.

**Cup and trace.** Multiplication in A followed by the finite-map trace defines `A tensor A -> K_X`. Over U the trace is the sum of all `|G|` sheets; at a branch stalk the terms are counted with **inertia multiplicities**. Standard pushforward/trace compatibility of the cup product gives
\[
\int_Y a\smile b=\int_X \operatorname{Tr}_f(a\smile b)
\quad(a,b\in H^1(Y,K)). \tag{O1.2}
\]
One elementary justification: transverse cycles for the H1 intersection pairing may be chosen away from the finite branch set, where the cover is unramified and the trace sums each intersection contribution once; the inertia-invariant stalk formula extends this to the compact curves.

On the regular G-fibre the generic trace pairing is the usual permutation pairing. Its restriction to dual isotypic factors, after identifying the dual by the positive invariant `h0`, is a **nonzero rational multiple** of the tensor product of `h0` and the coefficient-dual pairing. Indeed, the group-average matrix-coefficient orthogonality supplies `|G|/dim(V_sigma)` before rational choices of the dual metric; the ratio of two invariant K-Hermitian coefficient metrics lies in `K^{bar=1}=Q` by Schur. The trace/cup factorization thus identifies the Jacobian **skew** multiplicity form with a rational multiple of the DW parabolic sheaf cup form (or its K-conjugate).

Using (O2) and the **uniqueness** in `HHO-LEM-CUP-MORITA`, with `delta=sqrt(-3)`, gives
\[
\boxed{h_W=c\,\delta S\quad\text{or its conventionally conjugate form},
\qquad c\in Q^\times.} \tag{O1}
\]
When `dim_K W=8`, `c^8=N_{K/Q}(c^4)`, and conjugation fixes a Hermitian determinant. Therefore
\[
\boxed{[\det h_W]=[\det(\delta S)]\in
Q^\times/N_{K/Q}(K^\times).} \tag{B1}
\]
No dominance (D), supplier (L) or Severn polarization hypothesis was used. The statement is for a **finite-cover** datum, not an abstract tuple without realization; Riemann existence supplies the connected cover for a finite generating product-one tuple.

**Effective group.** For `N=ker(sigma)`, pass to `Y'=Y/N`, `Gamma=G/N`. Pullback identifies `H^1(Y',Q)` with the N-invariants and scales the cup form by `|N|`. In rank 8 the determinant scales by `|N|^8=N(|N|^4)`. Thus the class is preserved and the eventual support gate can be stated with `|Gamma|/chi(1)`, not only `|G|/chi(1)`.

## 3. Conditional consequence; remaining boundary

**[SESSION — THM implication using already registered HHO-THM-SUPPORT.]** For a rank-eight finite-monodromy genus-zero datum of signature (4,4), a **nonsplit parabolic-cup class** requires an inert prime `p ≡ 2 (mod 3)` such that
\[
p\mid |\Gamma|/\chi(1).
\]
B1 transfers the parabolic determinant class to the Jacobian multiplicity class; the HHO support theorem excludes all inert primes of defect zero; effective-group descent makes the bound intrinsic. **Necessary only. Not a no-go for P1.** This is a new SESSION proof route for a previously source-claimed bridge, **not a novelty claim**.

**B2 remains OPEN:** nothing here identifies the Jacobian multiplicity polarization with the specific Severn factor `A_sigma` and its chosen polarization. Severn [386] Prop. 5.1 / v2 Prop. 7.1 have not been read as primary texts. HHO's `hcg-v0.2` pin is unchanged. Any requested HCG pipe item about Severn's exact definition is separate from this proof.

## 4. Verification and receiving-review obligations

- [THM] O2: complete formula conversion (O2.1–O2.2), source inspected directly (DW06 printed pp. 15–19).
- [NUM] Independent exact stdlib 9/9 control; executed in this session; no external/GAP run.
- [THM] O1: finite-map sheaf identity, Leray, duality/trace and group-average factorization. **Standard finite-cover trace functoriality is used**, not independently sourced as a new theorem.
- [OPEN] Co-owner must verify (i) DW dual/conjugation sign, (ii) branch-weighted trace identity (O1.2), and (iii) rationality of the scalar in the chosen coefficient convention before recording CHECKED.
- [OPEN] B2 / Severn's specific polarization; literature novelty and any adoption are distinct decisions.

No register, accepted evidence grade, release, tag or owner pin changed by this advisory.
