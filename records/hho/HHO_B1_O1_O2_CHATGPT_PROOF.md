# HHO B1 — independent O2/O1 proof (ChatGPT)

**Date:** 2026-11-12. **Status:** [SESSION — THM, revised after PR #51]. O2: two-AI CHECKED, conditional on DW06 Thm 2.5. O1 and the gate: PROPOSED until C1–C4 are independently reviewed. **Scope:** no adopted claim, HHO register change, HCG re-pin or Severn claim acceptance. PI selected route B (prove O2 then O1).
**Owner pins:** HHO `hho-v0.2` (governing); HHO cites `hcg-v0.2`. HCG `hcg-v0.4` §6.24 has since adopted the algebraic locality theorem (CHECKED, two AIs), **not** its cup/polarization bridge. This record is not HCG owner science.

## 0. Source identity and reading extent

- Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality*, arXiv:math/0411119, directly inspected §§1.2, 2.2–2.4 (Cor. 2.2, Lemma 2.4, **Thm. 2.5 and its proof**) and §3 Prop. 3.1. Supplied ar5iv-print PDF, 27 pp., SHA-256 `3a70bd23136771e8aa3e0fb2708d9c51c6ad57f2e7086c7d8cb89c4309744627`. Published version numbers this formula Thm. 2.6.
- Dettweiler–Wewers, *Variation of local systems and parabolic cohomology*, arXiv:math/0310139v2, directly inspected §1.3, §4.3 and §6.1 **Prop. 6.1 and proof**. Original PDF, 28 pp., SHA-256 `108c89a25c62f98eb5aa3f2d81084b7f7f711da15a090168783d9a582921938f`. Its Prop. 6.1 is the cyclic-degree-three case, not a general proof of cup compatibility.
- HCG `hcg-v0.2`: `evidence/hcg/received/b69978bf-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md` §§2–3.4 (the exact `C,D,Z,B` formula); HHO `hho-v0.2`: `hho/HHO_SUPPORT_RESULTS.md` §§1–3, including `HHO-LEM-CUP-MORITA` and `HHO-THM-SUPPORT`. Claude's `HHO_B1_SOURCE_READING.md` SHA-256 `72683c0315adfb0075912a7e028a21ee9e9ee9ddbd714245dc448308596e5669` is advisory context.
- Severn's original propositions were **not read**. Textbook for singular cup naturality and Poincaré duality: A. Hatcher, *Algebraic Topology* (Cambridge UP 2002), §§3.2–3.3, https://pi.math.cornell.edu/~hatcher/AT/ATpage.html . Hatcher is **not** cited for the branched finite-map trace formula, derived in §2 below. DW06 §2.2 equations (17)–(18) and Cor. 2.2 supply the compact-support-lift pairing. No novelty claim.

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

**Exact control:** `python3 -I evidence/hho/b1/hho_b1_o2_exact_check.py` tests all 9 pairings on the three-dimensional cocycle space of `(omega,omega^2,omega,omega^2)` over exact `Q(omega)`: **9/9 PASS**, no HCG engine. This is a small regression check, **not** a proof.

## 2. O1: finite G-cover comparison with cup and trace

**[SESSION — THM, O1 PROPOSED; conditional on standard finite-map cup/trace functoriality.]** Let `f:Y→X=P¹_C` be a connected finite G-Galois branched cover of smooth projective curves, branch divisor D, `U=X-D`, `j:U→X`; `K=Q(omega)`. Fix a K-representation `sigma`, **absolutely irreducible over K, defined over K and with character field exactly K**, and a positive invariant coefficient K-Hermitian form `h_U`. Its dimension is `chi(1)`. These are needed for the rational HHO multiplicity module and the support theorem (C1).

**2.1 Comparison of the sheaves and multiplicities.** Put `A=f_*K_Y`. Away from D, A is the regular local system `K^G` with commuting base monodromy and deck action; at a branch point with inertia I, its stalk is `K^{G/I}=(K^G)^I`. Therefore `A=j_*(A|U)`. Finite fibres have vanishing higher cohomology, so `R^qf_*K_Y=0` for `q>0` and `H¹(Y,K)=H¹(X,A)`. Semisimplicity and the K-rational σ-idempotent give
\[
e_\sigma A\simeq V_\sigma\otimes_K j_*\mathcal L_\sigma,\qquad
\mathcal L_\sigma=\operatorname{Hom}_{K[G]}(V_\sigma,A|U),
\quad
\operatorname{Hom}_{K[G]}(V_\sigma,H¹(Y,K))
\simeq H¹(X,j_*\mathcal L_\sigma).
\tag{O1.1}
\]
The multiplicity local system has monodromy `sigma^vee`, which is identified with the conjugate representation through `h_U` (not silently with σ). One must use a single consistent σ/dual/conjugate convention through the pairing.

**2.2 Compact-support cup versus sheaf cup (C2).** DW06 Corollary 2.2 constructs the pairing on `H¹_p(U,L)=H¹(X,j_*L)` via lifts to `H¹_c(U,L)`. The map `j_!L→j_*L` induces the parabolic image. Its compatible coefficient contractions
\[
j_!L\otimes j_*L^\vee\longrightarrow j_!K_U\longrightarrow K_X,
\qquad j_*L\otimes j_*L^\vee\longrightarrow K_X
\]
give the **same pairing** after cup and integration, by naturality; this is exactly the compatibility of DW06 §2.2 equations (17)–(18). Hence the sheaf pairing below is the lift-defined DW cup, not a newly normalized form.

**2.3 Finite map, sheaf trace and cup (C3).** The sheaf A is a commutative K-algebra; multiplication gives `A⊗A→A`. The finite direct-image comparison `H*(Y,K)≅H*(X,A)` respects cup products with this multiplication, by naturality of the singular/sheaf cup construction (Hatcher, *Algebraic Topology*, §3.2); top-degree integration uses Poincaré duality (ibid., §3.3). Define `tr_f:A→K_X` by sheetwise summation off D. At a point `x∈D`, local sections are constant on inertia orbits and hence the trace extends as
\[
\operatorname{tr}_{f,x}((a_y)_{y|x})
=\sum_{y|x}e_y a_y,\tag{O1.2a}
\]
with `e_y` the positive local ramification index of `f` at y. It is a sheaf map with `tr_f\circ unit=(deg f)id`. In local coordinates `f(z)=z^{e_y}` is orientation-preserving of local degree `e_y`; hence `f^*:H²(X,K)→H²(Y,K)` multiplies the orientation generator by `deg f=|G|`. Since `tr_f f^*=|G|` and both top cohomologies are one-dimensional, the induced trace on `H²(Y,K)` is **integration-preserving**:
\[
\int_X\operatorname{tr}_f(\gamma)=\int_Y\gamma .
\]
Consequently, for `a,b∈H¹(Y,K)`, with the cup on H¹(X,A) followed by multiplication in A,
\[
\boxed{\int_Y a\smile b=\int_X\operatorname{tr}_f(a\smile_A b).}\tag{O1.2}
\]
This uses the cochain cup/finite-map comparison and explicit ramification weights, **not** a purported Hatcher theorem about branched traces and not just a transverse-cycle heuristic.

**2.4 Exact HHO W and the Morita defining identity (C4).** Let `U_Q=Res_{K/Q}(V_\sigma)` and `M_Q=H¹(Y,Q)`. Because the character field is exactly K and σ is realized over K, `U_Q` is irreducible over Q[G], `End_{Q[G]}(U_Q)=K`, and `U_Q⊗_QK≅V_\sigma⊕V_{\bar\sigma}`. The precise HHO space is
\[
W_Q=\operatorname{Hom}_{Q[G]}(U_Q,M_Q),\quad
W_Q\otimes_{K,\iota}K\simeq
\operatorname{Hom}_{K[G]}(V_\sigma,H¹(Y,K)),\tag{O1.3}
\]
or the conjugate factor for the other embedding. Thus the W of `HHO-LEM-CUP-MORITA` **is** the parabolic multiplicity module of (O1.1).

For `F,F'\in W_Q` and `u,u'\in U_Q`, HHO's Jacobian-induced K-Hermitian `h_W` is uniquely defined by
\[
E(Fu,F'u')=\operatorname{Tr}_{K/Q}\!
\left(\delta^{-1}h_W(F,F')h_U(u,u')\right),
\qquad\delta=\sqrt{-3}.\tag{O1.4}
\]
Under (O1.3), the **left-hand side** is the finite-cover cup of (O1.2); by C2 it is the DW parabolic cup, and by O2 that is HCG's skew-Hermitian S. In the regular G-fibre only σ and its contragredient pair nontrivially. Schur factorization writes the G-invariant coefficient metric as `q h_U` with `q∈K^\times`; both metrics are Hermitian, so `q=\bar q` and `q∈Q^\times`. The matrix-coefficient orthogonality normalization, including any `|G|/\chi(1)`, is also rational. Therefore the resulting **entire right-hand side** agrees with (O1.4) with `h_W=c\delta S` for one `c∈Q^\times` (or its consistently conjugate version). This checks the *defining identity* before applying the **uniqueness** of `HHO-LEM-CUP-MORITA`:
\[
\boxed{h_W=c\,\delta S,\quad c\in Q^\times,\qquad
[\det h_W]=[\det(\delta S)]
\text{ for }\dim_K W=8.}\tag{B1}
\]
Indeed `c^8=N_{K/Q}(c^4)`; Hermitian determinants are rational and conjugation-invariant. An overall cup-orientation sign is absorbed in c. The statement concerns the Jacobian multiplicity form, **not** the separately polarized Severn factor (B2).

**Effective group.** For `N=ker(sigma)`, pass to `Y'=Y/N`, `Gamma=G/N`. Pullback identifies `H^1(Y',Q)` with the N-invariants and scales the cup form by `|N|`. In rank 8 the determinant scales by `|N|^8=N(|N|^4)`. Thus the class is preserved and the eventual support gate can be stated with `|Gamma|/chi(1)`, not only `|G|/chi(1)`.

## 3. Conditional consequence; remaining boundary

**[SESSION — THM implication, conditional on B1 and the registered HHO-THM-SUPPORT.]** Let Γ be the finite effective group and σ **absolutely irreducible over K, defined over K with character field exactly K**, and assume the rank-eight parabolic multiplicity has signature (4,4). Then a **nonsplit parabolic-cup class** requires an inert prime `p ≡ 2 (mod 3)` such that
\[
p\mid |\Gamma|/\chi(1).
\]
B1 transfers the parabolic determinant class to the Jacobian multiplicity class; the HHO support theorem excludes all inert primes of defect zero; effective-group descent makes the bound intrinsic. **Necessary only. Not a no-go for P1.** This is a new SESSION proof route for a previously source-claimed bridge, **not a novelty claim**.

**B2 remains OPEN:** nothing here identifies the Jacobian multiplicity polarization with the specific Severn factor `A_sigma` and its chosen polarization. Severn [386] Prop. 5.1 / v2 Prop. 7.1 have not been read as primary texts. HHO's `hcg-v0.2` pin is unchanged. Any requested HCG pipe item about Severn's exact definition is separate from this proof.

## 4. Verification and receiving-review obligations

- [THM] O2: complete formula conversion (O2.1–O2.2); source read directly and independently validated in PR #51 as `[THM-cond: DW06 Thm 2.5]`, two-AI CHECKED (not adopted).
- [NUM] Independent exact stdlib 9/9 control; executed in this session; no external/GAP run.
- [THM] O1: finite-map sheaf identity, Leray, duality/trace and group-average factorization. **Standard finite-cover trace functoriality is used**, not independently sourced as a new theorem.
- [OPEN] O1 corrections C1–C4 are now explicit; the receiving reviewer must verify the branch-weighted trace/cup argument (O1.2) and the exact Morita normalization (O1.4) before recording CHECKED.
- [OPEN] B2 / Severn's specific polarization; literature novelty and any adoption are distinct decisions.

No register, accepted evidence grade, release, tag or owner pin changed by this advisory.

## 5. Change record — receiving PR #51

C1: exact K field and absolute irreducibility in gate; C2: compact-support-lift cup agrees with sheaf cup; C3: finite-map algebra/cup, inertia-weighted trace, and top-degree normalization with Hatcher textbook §§3.2–3.3 for naturality/duality; C4: rational/K multiplicity identification and the defining `E=Tr(delta^-1 h_W h_U)` identity. Original proof preserved in Git at `c61cd224`. Exact 9/9 script moved unchanged into `evidence/hho/b1/`; the PR #51 B1 index must include its SHA-256 upon integration. No HHO register, HCG pin or adoption changed.
