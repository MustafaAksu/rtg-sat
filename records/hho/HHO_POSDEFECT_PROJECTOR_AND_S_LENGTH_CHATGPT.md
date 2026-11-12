# HHO — positive-defect mechanism A: the projector denominator and gluing length

**Date:** 2026-11-12. **Status:** [SESSION — THM/ALG advisory, PROPOSED for co-owner proof review]. No adopted statement, new HHO RID, grade, register change, HCG pin or release decision.  
**PI scope:** Option A chosen on 12 November 2026: study the *mechanism* (M) of positive-defect parity before any new dominance/differential campaign (O). It is not a decision that P1 is solved.

**Owner identities:** HHO `hho-v0.2` (governing adopted register), source `HHO-THM-SUPPORT` and `HHO-LEM-CUP-MORITA`; HCG scientific inputs pinned by HHO at `hcg-v0.2`. The pending successor `rtg-sat` PR #55 is a **draft**, not a new adopted owner edition.  
**Session sources inspected:** complete PI-supplied 53-line `HHO_POSDEFECT_FIRST_READING.md`, SHA-256 `18aa8f7a24c9866674d7db6ea0064499885ac282ed5ebdf860bd0befd48bf3a6`; `evidence/hho/frozen/HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` at `hho-v0.2`, **targeted** A4.1–A4.2, A5.3–A5.5, A6.1–A6.3, A7.1–A7.2; HHO v0.2 support summary §§1–5; PR #55's register B.5 and draft release record (targeted). No GAP run or full scientific replay was performed.

## 1. The projector-annihilation lemma (proved)

**[SESSION — THM P, new conditional algebraic lemma.]** Let `T=Z_p`, `F=Q_p`, `M` a finite free **perfect** alternating `T[G]`-lattice with a G-invariant bilinear form `E`. Let `e\in F[G]` be a **self-adjoint central idempotent** (`e*=e`, where `g*=g^{-1}`). Set

\[
V=M\otimes_TF,\quad V_\Omega=eV,\quad
L=M\cap eV,\quad L'=M\cap(1-e)V,\quad
A=L^\#/L
\]

where `#` is the dual under the restriction of `E` to `eV`. Then

\[
\boxed{L^\#=eM,\qquad
A=eM/L\simeq M/(L\oplus L')\simeq L'^\#/L'.}\tag{P1}
\]

If `p^t e\in T[G]`, then

\[
\boxed{p^t A=0.}\tag{P2}
\]

**Proof.** Self-adjointness gives the orthogonal, nondegenerate decomposition `V=eV \perp (1-e)V`; both L and L' are primitive T-sublattices of M. For `m\in M`, `l\in L`, `E(em,l)=E(m,l)\in T`, so `eM\subseteq L^\#`. Conversely, for `z\in L^\#`, the integral functional `l\mapsto E(z,l)` extends to all M because L is primitive. Perfectness of E gives `m\in M` inducing this functional; nondegeneracy on eV forces `em=z`. Thus `eM=L^\#`. The kernel of `M\to eM/L` consists exactly of `L\oplus L'`. The analogous map with `1-e` gives the second discriminant-group isomorphism. Finally, `p^t em\in M\cap eV=L`, for every m in M, if `p^t e\in T[G]` and M is G-stable; this proves (P2). No residual irreducibility or geometric dominance is used.

**[SESSION — COR]** For any simple `k[G]`-module `S` (`k=F_{p^2}` when p inert), base change A and L' to `R=O_{K,p}`. Since `p^t A=0`, the identification with the orthogonal complement gives an injection

\[
A\otimes_T R\hookrightarrow
p^{-t}(L'\otimes_T R)/(L'\otimes_T R)
\simeq (L'\otimes_T R)/p^t(L'\otimes_T R).
\]

The filtration by powers of p has t quotients isomorphic to `(L'\otimes R)/p(L'\otimes R)`. Thus the Jordan–Hölder multiplicity obeys

\[
\boxed{\ell_S(A\otimes_T R)\le
t\,\ell_S((L'\otimes_T R)/p(L'\otimes_T R)).}\tag{P3}
\]

For t=0, `A=0`; for t=1, A is p-torsion and its multiplicities are bounded by one residual copy of the complementary lattice. The inequality is a **length bound, not a parity theorem**.

## 2. Application: the rational pair χ + χ̄

**[SESSION — THM Q, conditional on the rational character-field profile.]** Let χ be a complex irreducible character with exactly `K=Q(omega)` as character field, realized over K, and let `Omega={χ,χbar}`. Its central idempotent over F is

\[
e_\Omega
=\frac{\chi(1)}{|G|}\sum_{g\in G}
\bigl(\chi(g^{-1})+\overline{\chi(g^{-1})}\bigr)g .
\tag{Q1}
\]

The coefficient in parentheses is `Tr_{K/Q}(χ(g^{-1}))\in Z` (character values are algebraic integers). The cup adjoint exchanges χ and χ̄, so `e_\Omega^*=e_\Omega`. Put

\[
t=v_p(|G|)-v_p(\chi(1))=v_p(|G|/\chi(1)).
\]

Then `p^t e_\Omega\in Z_p[G]`; by P2,

\[
\boxed{p^t (L^\#/L)=0.}\tag{Q2}
\]

This is an **explicit upper bound for the exponent of the entire paired-isotypic gluing group**. It does not assert that the group vanishes for positive t. Distinguish the *integer exponent t of the projector denominator* from the defect of the whole Brauer block (they can differ for positive-height characters).

**[NUM — exact elementary valuation, not a new GAP replay.]** At the source-reported `G34` group order `|G|=39,191,040=2^9·3^7·5·7` and χ(1)=6:
- p=5: `t=1`, hence `5A=0` for the paired χ/χ̄ subspace.
- p=2: `t=8`, hence `2^8A=0`; this **does not** say its 2-block has defect eight (source says block defect nine/height one).
At p=5 the source's Brauer-tree analysis identifies only the adjacent ψ84 (and conjugate) as carrying the χ-leaf simple `S`, and reports `m(ψ84)=512` on W5. Under that paired-block identification, (P3) gives `\ell_S(A\otimes R)\le512` for the relevant S-sector. This is a **coarse, conditionally sourced bound** and does not establish the parity of A or a new G34 nonsplitting result.

## 3. Integral Morita and the proposed S-length parity: different groups must not be conflated

**[SESSION — THM R1, conditional on absolutely irreducible residue.]** Let `R=O_{K,p}` (p inert, including p=2), and `U_R` a G-stable free R-lattice whose reduction `S=U_R/pU_R` is **absolutely irreducible** over `k=F_{p^2}`. The image of `R[G]` in `End_R(U_R)` is the entire matrix order:

\[
R[G]|_{U_R}=\operatorname{End}_R(U_R)\simeq M_{\chi(1)}(R).
\tag{R1}
\]

**Proof:** the mod-p image is all `End_k(S)` by the finite-field Jacobson density / Burnside theorem (absolute irreducibility is essential). Its integral image is a finite R-submodule whose reduction surjects; Nakayama gives (R1). A stable lattice for the *same* irreducible Kp-representation is therefore invariant under the full matrix order and is homothetic to `U_R`. For any invariant nondegenerate Hermitian `h_U`, choose a rational p-power normalization with integral, nonzero reduction on U_R. Its radical is G-stable and hence zero by irreducibility. Thus **the normalized coefficient Hermitian lattice is unimodular**. This does not assert that every *fixed unnormalized* h_U is unimodular.

**[SESSION — ALG R2, conditional on an integral paired χ/χ̄ comparison.]** Suppose additionally that the **χ-summand of the saturated cup lattice** admits an R[G]-equivariant, Hermitian-compatible identification

\[
L_\chi\simeq U_R\otimes_R W_R,
\]

and that the paired χ̄-summand supplies its conjugate dual with the trace-cup normalization `δ^{-1}` (a p-unit because p is inert). In particular, require the χ and χ̄ *integral* block projectors to separate and preserve the saturated lattice; this does **not** follow from absolute irreducibility of S alone.

With h_U normalized unimodular, the Hermitian dual of the **χ-summand** satisfies

\[
L_\chi^\#/L_\chi \simeq
U_R\otimes_R(W_R^\#/W_R).
\tag{R2a}
\]

The multiplicity of S in this **χ-Hermitian discriminant module** is

\[
\boxed{\ell_S(L_\chi^\#/L_\chi)
=\ell_R(W_R^\#/W_R)
=v_p(\det h_{W,p}).}\tag{R2b}
\]

A local rational normalization `h_{U,p}=p^a h_U` changes `h_{W,p}=p^{-a}h_W`; in multiplicity rank eight the determinant valuation changes by `-8a`, leaving parity unchanged. If the **χ-isotypic projection** of the full gluing group `A\otimes R` is proved to identify with the module on the left in (R2b), then

\[
\varepsilon_p\equiv \ell_S((A\otimes R)_\chi)\pmod2
\]

via the already reviewed B1 bridge. The preceding sentence is an **additional integral matching obligation**, not an unconditional conclusion of the full-gluing theorem.

**Important ambiguity in the uploaded first-reading note §3:** its `A=L^\#/L` is the *full paired rational* `Z_p`-gluing group, while its `U_R\otimes(W_R^\#/W_R)` is the *one-embedding χ-Hermitian* module. Writing `ℓ_S(A)` without saying whether S is over Fp, Fp², or which χ-sector is being counted is not yet a well-typed theorem. In the paired situation the χ̄-sector can contribute separately; counting total Jordan–Hölder length can differ by a factor two and lose the odd parity.

## 4. Scientific disposition and test obligations

- **Proved [SESSION]:** P1–P3 and Q1–Q2 (projector denominator / gluing exponent); R1 (integral matrix order and Hermitian normalization, conditional on residual absolute irreducibility). These are algebraic claims, not output of a numerical engine.
- **Conditional [SESSION / OPEN]:** R2's parity equality requires the stated *integral* paired χ/χ̄ splitting, trace normalization and an identification of the χ-sector of A. This is the next proof obligation; do not mark it CHECKED on the basis of the first-reading note.
- **Source-reported calibration, not independent gluing computation:** C6 rank one at p=2; G34 at p=5 and p=2; C3×F20 at p=5 (its ρ4 reduction is not simple, so R1/R2 do not apply as stated).
- **Recommended minimal actual tests:** (i) construct a saturated paired-isotypic lattice and its exact Gram on one recorded C6 datum, compute A and both χ/χ̄ sectors; (ii) verify `p^t e_\Omega M\subseteq L` and the Smith exponents in that example; (iii) for G34 p=5, use the *existing* block tables to verify the χ/χ̄ integral idempotents before attempting a new GAP campaign; (iv) do not infer P1/(D) from an integral gluing calculation.
- **Missing dependencies:** a targeted independent proof-review of the projector and χ-sector maps; the explicit cup lattice or Gram needed for a nontrivial test. No source hash, RID, acceptance, or PI decision is manufactured by this note.

**Next output:** a scoped exact integral test (starting with C6 p=2) and an owner disposition on whether the χ/χ̄ splitting makes R2 valid. The PI's Option A means the obstruction programme (O) is **not** pursued in this pass.
