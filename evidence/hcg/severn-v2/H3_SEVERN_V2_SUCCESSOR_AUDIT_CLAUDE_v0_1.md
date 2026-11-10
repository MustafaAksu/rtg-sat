# HCG — Severn v2 successor audit, part 1: source identity, crosswalk, and an independent review of Lemma 4.4 (Claude) v0.1

**Date:** 28 October 2026 · **Status:** Claude review, one AI; PROPOSED dispositions. INTERNAL. Written before reading any ChatGPT assessment of Lemma 4.4 (the handoff `HCG_SEVERN_V2_NEUTRAL_SOURCE_HANDOFF_v0_1.md`, adcb3401…, contains none).
**Governing record:** `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (276c93a3…); change log `HCG_DSN_v0_3_PENDING_DELTAS.md` (Δ24 approved, Δ25 pending).

## 0. Source identity

| Object | Value |
|---|---|
| `2610.00387v2.pdf` (PI upload, 28 Oct) | SHA-256 **ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4**; 31 pages; pdfTeX, created 22 Oct 2026 17:00 +03 |
| Internal identity | "Date: 21 October 2026 (version 1.5)"; title *Weil classes on abelian sixfolds and eightfolds of Weil type for ℚ(√−3)* |
| Citation form | hexagon:2610.00387v2 (SG-5) |
| v1 under audit so far | hexagon:2610.00387v1, Draft v0.5, 17 pp. (PDF 7aa80a3b…) |

The PDF bytes were not obtainable from the workspace; the PI supplied the file. ChatGPT's reading was of the online copy, so the two readings are of the same version but not of a hash-matched file.

## 1. Structural finding: v2 is self-contained

The v2 bibliography (35 entries) contains **neither the companion transfer paper hexagon:2610.00386 nor any OpenAI manuscript**. The −2 paper [27] (hexagon:2610.00246) is cited for context only (§1.2). Everything the v1 chain imported from [386] and [19] is now proved inside v2:

| Chain link (HCG name) | v1 location | v2 location | Change |
|---|---|---|---|
| PO-4 (L) by Brauer/reality | v1 Thm 3.1 | **Thm 5.1** | same statement; proof now writes out the quaternionic parity step explicitly |
| PO-2 supply (Schoen cycles, Milne contraction) | [386] Prop 3.7, Cor 3.8, Lemma 3.4 | **Lemma 4.3, Prop 4.6, Cor 4.7** | now internal; **new Lemma 4.4** (see §3) |
| PO-3 spreading and transfer | [386] Lemmas 6.1–6.2, Thm 7.1 | **Lemma 6.1, Thm 6.2** | now internal; relative-Hilbert-scheme proof written out; every-member step via Lemma 2.2 (isogeny) + Baire + irreducibility |
| PO-6 polarization bridge | [386] Prop 5.1, Lemma 2.4 | **Prop 7.1** (Steps 1–4) | now internal |
| Cocycle formula ([19, Lemma 6.2]; OPEN 5) | [386] Lemma 5.2 → [19] | **Lemma 7.2**, with a written Δ-complex proof and Figure 1 | **new written proof** |
| PO-5 dominance criterion | v1 Prop 4.2 with (H0)–(H4) | **Lemmas 8.1–8.4, Prop 8.5, Rem 8.6** with (H1)–(H4) | (H0) dropped as a hypothesis (derived, see §4); base change |Z(G)|·k_j·m_j and the central element made explicit (Lemma 8.2); single global sign ε proved |
| E02 wording ("isomorphism") | v1 Prop 4.2 Step 4 | Lemma 8.4 "maps … **onto** the tangent space"; Prop 8.5 chooses n² indices with a nonzero minor | **repaired** |
| PO-1 compensation | v1 Lemma 5.1, Prop 5.2 | **Lemma 10.1, Prop 10.2** | same argument; m chosen in the class [−1/t]; α = 1+ω with α² = ω |
| Thm 6.2(1), (2), (3) | v1 Thm 6.2 | **Theorems A, B, C**; Thm 11.2 for powers; §12 type III | renumbered; same content |
| G₃₄ datum and certificate | v1 §6, Appendix A | **§9, Appendix A** | tuple and curve table unchanged (§5 below); Appendix A now prints the basis, the Gram matrix S and the seventeen 4×4 blocks X_j; adds a Shephard–Todd identification by order and an irreducibility proof by reduction mod (7, ω−2) |

Consequences for our records: the grade column of the PO matrix was earned on v1/[386] texts. Where v2 restates the same argument (PO-1, PO-3, PO-4, PO-6 bridge), the review carries over only after a targeted identity check of statement and proof; where v2 adds a step (Lemma 4.4) or a new proof (Lemma 7.2), fresh review is required. None of this changes CLAIMED.

## 2. Schoen's gap, verified against Schoen's text

Local copy: `h3_src/schoen88.pdf` (3794a85d…), pp. 11–19 read.
- Thm 2.0 (p. 11): hypothesis is only that the (ℤ/m)^×-orbit of (α_1,…,α_{2r}) ∈ (ℤ/m − {0})^{2r} is simple; exponents need not be prime to m. So the case α_j = m/2 is inside the stated hypotheses.
- Lemma 2.8 (p. 18): reduces the claim "primitive characters of ℤ/m do not occur in H(W_i)/φ*H(W_{i−1})" to "no primitive character in H^n(F_i)" via the long exact sequence → H^n(W_{i−1}) → H^n(W_i) ⊕ H^n(K'_{i−1}) → H^n(F_i) →. I checked that vanishing of H^n(F_i)^χ suffices: an element (x, 0) with x ∈ H^n(W_i)^χ maps to x|_{F_i} = 0, hence comes from H^n(W_{i−1}).
- Sublemma 2.9 (pp. 18–19): proves H(F_i)^χ = 0 by choosing a prime p | m such that the ℤ/p-quotient cover is ramified over b_{2i−1}, i.e. **p ∤ α_{2i−1}**. If α_{2i−1} = m/2 and 4 | m, every prime divisor of m divides m/2: no such p exists. (If m ≡ 2 mod 4, p = 2 works. The same failure occurs for other exponents, e.g. m = 36, α = 6.) **Severn's diagnosis is correct.**

## 3. Lemma 4.4: independent proof review — correct

Statement: for every i ≤ r and every primitive χ of ℤ/m, H*(F_i, ℂ)^χ = 0; hence Thm 2.0 and Cor 3.1 of Schoen hold under their stated hypotheses without the choice of p.

Checked step by step:
1. H*(F_i, ℂ)^χ = H*(E_i, (β_{i*}ℂ)^χ|_{E_i}): β_i finite, F_i = β_i^{−1}(E_i), proper base change for the closed inclusion; the ℤ/m-isotypic decomposition of a sheaf of ℂ[ℤ/m]-modules is a direct sum of sheaves. ✓
2. Stalks: (β_{i*}ℂ)_y = ℂ[β_i^{−1}(y)], a transitive permutation module ℂ[ℤ/m / Stab]; its χ-part is nonzero iff χ|_{Stab} = 1 (Frobenius reciprocity). A primitive χ is faithful, so the χ-part vanishes wherever Stab ≠ 1. ✓
3. Where Stab ≠ 1: at every point of a branch divisor S_{j,i}. By Schoen's Lemma 2.5 the local model is the normalization of A[v]/(v^m − unit·∏_{j∈J} s_j^{α_j}); the inertia at a point above S_{j,i} contains the subgroup ⟨α_j⟩ ⊂ ℤ/m of order m/gcd(α_j, m) ≠ 1 (for α_j = m/2 this is {0, m/2}, on which a primitive χ takes the value −1). ✓ Away from ∪S_{j,i} the local model is étale (J = ∅), so (β_{i*}ℂ)^χ is a rank-one local system there. ✓ Hence (β_{i*}ℂ)^χ|_{E_i} = j_!L exactly as claimed (a constructible sheaf that is a local system on U and has zero stalks on E_i − U is j_!(L)). ✓
4. E_i is not a branch divisor: Schoen's proof of Lemma 2.5, multiplicity α_{2i−1}+α_{2i} = m. ✓
5. Geometry of E_i → K_{i−1} (ℙ¹-bundle): S_{2i−1,i} and S_{2i,i} meet E_i in two disjoint sections, and every other S_{j,i} meets E_i in whole fibres over K_{i−1} ∩ S_{j,i−1}. Both facts are stated by Schoen himself in the proof of Sublemma 2.9 ("two disjoint sections", "R = (ρ_i|_{E_i})^{−1}(ℛ)"), resting on his transversality claim (p. 14, "an induction argument shows"). ✓ (Transversality is asserted, not written out, in Schoen; this is a pre-existing feature of Schoen's proof, not a new gap.)
6. Fibres: a fibre inside some other S_{j,i} carries the zero sheaf; any other fibre ℙ¹ meets the closed set only at the two section points, and j_!L restricts to the extension by zero of a rank-one local system on ℂ^× with monodromy χ(α_{2i−1}) ≠ 1. H^0_c = 0 (noncompact connected), H^2_c ≅ H^0(dual)^∨ = 0 (nontrivial monodromy), χ_c = 0 ⇒ H^1_c = 0. ✓
7. Proper base change for p (proper): (R^b p_* j_!L)_k = H^b(p^{−1}(k), j_!L|) = 0 for all k, so Rp_*(j_!L) = 0 and H*(E_i, j_!L) = 0 by Leray. ✓
8. Only α_{2i−1} ≢ 0 (mod m) is used, so the lemma covers every case of Thm 2.0, not only m/2 with 4 | m. ✓

**Disposition (Claude):** `[THM]` [import: hexagon:2610.00387v2 Lemma 4.4] **CHECKED (Claude proof review; ChatGPT independent review pending)**. It closes a genuine gap in Schoen's Sublemma 2.9 for the stated hypotheses. It does not by itself make Cor 4.7 or Theorem A established.

## 4. Other v2 changes that affect our records

- **(H0) removed from the criterion.** Lemma 8.3 derives, from (H1)–(H3) and dim I = n, that im M = ker M = I for every positive combination M, so W_0 = W_1 = I and Gr^W_1 = 0; Remark 8.6 then notes via Clemens–Schmid that the parabolic cohomology of every pair of pants vanishes "as it must". I checked the Hodge-type argument: for a weight-one variation the limit's Gr^W_0 can only be of type (0,0) and Gr^W_2 of type (1,1), so Hodge–Tate follows once Gr^W_1 = 0. Consequence for our H4 theory: our laminar reduction "(H0)+(H4)" could be sharpened to "(H4)" alone under the laminar premises; every (H0) value we computed was 0, consistent. PROPOSED, to be checked by ChatGPT.
- **Lemma 8.2** states the base change w_j^{|Z(G)| k_j m_j} = q_j, the central element from the G-torsor (Lemma 8.1), and the single sign ε by a plumbing argument. This is the content the auditor's round-1 report supplied independently (steps 2 and 4 of §6.15). It does not change our grades; the auditor's E03/D-2/D-3 notes are now addressed in the source.
- **E02 repaired** ("onto"). HCG-ALG-E02's wording correction is now in the source; keep the record as a dated note.
- **Theorem 6.2 (spreading)** in v2 states the conclusion "for every polarized abelian 2n-fold of Weil type for K with discriminant d(S)" and proves it by Lemma 2.2 (every such variety is K-isogenous to a fibre of the universal family) + Baire + irreducibility of M. OPEN 8's question is unchanged by v2; the auditor's B6 verdict concerned the same argument in [386] form.
- **Appendix A irreducibility and the Shephard–Todd label.** v2 adds an order-based identification (G(m,p,6) orders 720m⁶/p never equal 39,191,040; S₇ and W(E₆) excluded) and an absolute-irreducibility check modulo (7, ω−2). This answers the auditor's catalogue remark.

## 5. Appendix A tuple and curves: identical to the deposited v1 data

- Script `compare_v2_roots.py` (exact ℚ(ω) arithmetic) rebuilds the ten reflections from the roots printed in v2 Appendix A and compares them with the deposited `tuple_pairs_D3.json` (SHA-256 0021185d…, Zenodo 23422649): **all 20 matrices identical**; all ten are involutions.
- The seventeen curves and their (k_j, m_j, rank N_j, signature β_j) table are the same as in v1 (k_j = 2 exactly for [2,8], [4,8], [9,17]).
- Therefore §6.19 (component chain gate → paired → W5 → …) applies to v2's tuple without change: v2's certified tuple lies on S_W5 under P.
- **New opportunity.** v2 prints the basis b_1…b_8, the Gram matrix S and the seventeen blocks X_j. This makes OPEN 3's last sub-item (recompute Severn's own 17-curve table) feasible from the paper alone: run `reconstruct_generic.py` on the deposited tuple, change to the printed basis, and compare S and the X_j entry by entry. Proposed next computation (light; minutes).

## 6. Supplier rows (deposit, not v2 bytes)

`certificates/g34-d3/L/rebuild_rerun.log` (SHA-256 7c824f4e…, matches ChatGPT's value): 84 rows, all `ok=true`, identity holds on every coordinate. Rows with s > 0: 23, with m ∈ {6 (19 rows), 12 (3 rows: 42, 43, 44), 18 (1 row)}. Exactly the three m = 12 rows have 4 | m, so exactly three suppliers need Lemma 4.4, as v2 Rem 9.2 states; for m = 6 and 18 Schoen's choice p = 2 is available. (Rows 9, 11, 78 have m = 12 but s = 0: unramified, r = 0, no lemma needed.)

## 7. Proposed items for the v0.3 change log (PI decides)

| Item | Proposed |
|---|---|
| HCG-OPEN-SEVERN-V2 | ACTIVE, with sub-items: (a) Lemma 4.4 — Claude CHECKED, ChatGPT pending; (b) Lemma 7.2 — review open (would close OPEN 5 if the written proof holds); (c) Appendix A printed data vs. session engine — computation proposed; (d) identity checks v1/[386] → v2 for Thm 5.1, Thm 6.2, Prop 7.1, Prop 10.2 — targeted, pending; (e) (H0)-is-derived — check |
| v2 external dependencies | [386] and [19] are no longer cited by v2; the chain's only unrefereed source is v2 itself (plus Severn's own deposit) |
| Severn Theorems A/B (v2) | CLAIMED; same content as v1 Thm 6.2(1),(2); no grade transfers automatically |
| §6.19 component chain | applies to v2's tuple (identical bytes) |

## 8. Files

| File | SHA-256 |
|---|---|
| `h3_severn_v2/2610.00387v2.pdf` | ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4 |
| `severn_v2/compare_v2_roots.py` | see SHA256SUMS |
| Schoen 1988 (local) | 3794a85d4671d0fe95113b972bcbe708588e2884d52b36910727a3c363ecdc73 |
| Deposited rebuild log | 7c824f4e2895d75a8e1c99e5f77fb1b73c6078b28932c6e47a9c1792935a2b21 |
| Deposited tuple | 0021185d2111635f73d2b8c5b153c738015aef1c499394a0726a8b7ae72e5711 |
