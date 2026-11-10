# H3 — Source review of Severn [19, Lemma 6.2] (cocycle formula for the parabolic cup product) — Claude v0.1

**Date:** 22 October 2026
**Task:** HCG-OPEN-LEMMA62 (HCG DSN v0.1 ADOPTED, §2 OPEN 5).
**Status:** PROPOSED (Claude); ChatGPT cross-check requested; PI decides.
**Distribution:** INTERNAL. Do **not** send to the blind auditor before round 2 Priority A/B is complete (SG-10).
**Scope:** Standalone HCG session. Noncanonical. Not RTG.

**Source.** B. Severn, *Weil classes on non-split sixfolds* (discriminant −2, G₃₂), hexagon:2610.00246v2, PDF SHA-256 7b81d2ac…. Read: Prop 6.1 Steps 1–6 and Lemma 6.2 with its proof (pp. 12–14). Pages 13–14 were checked as rendered images, because the text extraction drops overlines.

**Dependency being audited.** Transfer paper hexagon:2610.00386v1, Lemma 5.2: "Proof. This is [19, Lemma 6.2]; as a companion paper we rely on it and do not repeat its derivation" (l. 834–835 of the local text extraction). Prop 5.1 of [386] uses Lemma 5.2 to compute S. Through Prop 5.1, PO-6 (HCG-EXT-PO6) rests on this lemma.

## 1. Statement

The setup:
- W is a local system of K-spaces on ℙ¹ minus n points, with flat Hermitian form h and unitary monodromy T_i generating a finite group.
- Q_i = T₁⋯T_{i−1} and M_i = 1 − T_i.
- A parabolic cocycle is given by vectors (a_i) with Σ Q_i M_i a_i = 0. Its value on ℓ_i is c_i = M_i a_i, and F_i = Σ_{j<i} Q_j c_j.

Lemma 6.2 states:

  S(a,b) = Σ_i h(Q_i⁻¹F_i^a + a_i, c_i^b),

with clockwise loops. The opposite orientation gives −S. The form vanishes on coboundaries and is skew-Hermitian.

## 2. Findings

**L1 — Same formula as the session's S** `[ALG]`.
- The session convention is u(g_i) = c_i, and its relative lift α_k satisfies (s_k − 1)α_k = u(g_k).
- Severn's preimage satisfies (1 − T_i)a_i = c_i, so a_i = −α_i is an admissible choice.
- h(F_i, Q_i c′_i) = h(Q_i⁻¹F_i, c′_i) by unitarity, and u(P_{k−1}) = F_k.

Therefore Severn's S equals the session form Σ_k h_W(u(P_{k−1}), P_{k−1}u′(g_k)) − Σ_k h_W(α_k, u′(g_k)) term by term.

Exact check (`severn_lemma62_formula_check.py`, written from Severn's statement, with no session-engine import):
- On the W5, W6 and W7 certificates, Severn's formula equals the certificate S_gram in all 64 entries. It is not −S and not S̄.
- The value does not change when each a_i is shifted by random vectors of ker(1 − T_i).
- The result is skew-Hermitian.

Output: `check_out.txt`.

**L2 — Algebraic steps of the proof: checked line by line** `[ALG]`.
1. The relation z_i = Q_i⁻¹(v_{e_{i−1}} − v_{e_i}) gives v_{e_{i−1}} = v_{e₀} − F_i. Consistent.
2. Substitution gives S_simp = −Σ_i[h(c_i, a′_i) + h(Q_i c_i, F′_i)] + h(Σ_i Q_i c_i, v′_{e₀}). This holds provided v′_{g_i} = Q_i a′_i − v′_{e_{i−1}} (see L3). The last term vanishes by closure.
3. By unitarity, the remaining sum is −S̄(b,a). The PDF has the overline; the text extraction lost it.
4. h(c_i, c′_i) = h(a_i, c′_i) + h(c_i, a′_i). I verified this by expanding (1 − T)a against (1 − T)a′ with T unitary.
5. Telescoping h(F_{i+1}, F′_{i+1}) − h(F_i, F′_i) gives S(a,b) + S̄(b,a) = 0. I verified this; the boundary terms vanish because F₁ = 0 and F_{n+1} = Σ Q_i c_i = 0.
6. Items 3 and 5 together give S_simp = S.
7. Coboundaries pair to zero.
8. A well-definedness point that the text leaves implicit: the formula does not depend on the choice of preimage a_i. Changing a_i by k ∈ ker(1 − T_i) adds h(k, c′_i) = 0, because c′_i ∈ im(1 − T_i) ⊥ ker(1 − T_i) for unitary T_i. I proved this and also checked it numerically (L1).

**L3 — The geometric step: NOT VERIFIED from the text** `[OPEN]`.

Two inputs are not reconstructible from the written description:
- the reduction of the Alexander–Whitney cup product on the Galois cover Ĉ to S_simp(f,f′) = Σ_i h(v_{e_i} − v_{e_{i−1}}, v′_{g_i});
- the cocycle relations at the "two triangles at the i-th puncture", in particular v′_{g_i} = v′_{f_i} − v′_{e_{i−1}}, which item 2 of L2 needs.

The Δ-complex is described only in words: edges e₀,…,e_n, and auxiliary f_i, g_i. Its triangles, vertex orderings and orientations are not given, so neither the AW terms nor the vanishing of the second triangle's contribution can be checked. The ingredients are standard: Hatcher §3.2, and the transfer for the finite cover. The step is plausible but not written out.

The author's Certificate E checks this step computationally. It covers the rank-24 system of [19] and 14 explicit covers over ℤ/3, S₃, Q₈ and Heis₂₇. The certificate lives in the hodge-fleet repository, which is not accessible here.

**L4 — Independent substitute for the application to W5** `[ALG]` (transitive).

The chain:
- On W5, the session S equals the published Dettweiler–Wewers Poincaré pairing (DW06 Thm 2.6) in all 64 entries. This is HCG-ALG-CUPVAL: ChatGPT implemented it, Claude checked the translation, and the auditor independently obtained ±S, the sign being one recorded global convention.
- By L1, Severn's Lemma 6.2 formula equals S on W5.

Hence, **for W5, the statement of Lemma 6.2 (and so of [386] Lemma 5.2) is supported by a published theorem proved on a different principle, independently of L3.** For W6 and W7, Severn's formula equals S as well, but no DW comparison has been made for those certificates.

## 3. Consequences (proposed)

- **HCG-OPEN-LEMMA62 → PARTIAL.**
  - Closed at the scope of the application: on W5, the [386] Lemma 5.2 / [19, Lemma 6.2] formula agrees with DW06 Thm 2.6, so the dependency of PO-6 on the unreviewed source proof is discharged for S_W5 (L1 + L4).
  - The algebraic part of the source proof is checked (L2).
  - Still open: the geometric reduction L3, by reconstructing the Δ-complex or by accessing Certificate E.
- **HCG-EXT-PO6 is not upgraded.** Its remaining open content is the identification in [386] Prop 5.1, Steps 1–4: M ≅ H¹_par(U_C, L′) and ψ = c·S with c ∈ ℚ^×. That identification has a Claude review only, and the auditor's assessment (R2 item 1) is pending. The proposed DSN v0.2 delta replaces the `[assuming:]` on Lemma 5.2 with "for W5: replaced by DW06 Thm 2.6 (HCG-ALG-CUPVAL) via L1".
- **Side note** `[HEUR]`. Prop 6.1 of [19] runs exactly the Step 1–5 structure of [386] Prop 5.1, and adds an independent small-group test: van Geemen's H computed directly on e·H¹(C,ℚ) against det h from the parabolic side, with ratios 27 and 108, both norms. This is the author's own reported test, not one we inspected, but it targets exactly the PO-6 identification.

## 4. Requested cross-check (ChatGPT)

1. Rerun `severn_lemma62_formula_check.py`, or write an independent version.
2. Re-derive L2 items 1–8.
3. Optionally, attempt the Δ-complex reconstruction for L3.

## Files
- `severn_lemma62_formula_check.py`
- `check_out.txt`
- page renders: `pg13-13.png`, `pg14-14.png` (in the scratchpad; not packaged)
