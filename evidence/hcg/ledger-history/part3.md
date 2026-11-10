
### §6.15 G34-D — geometric realization and dominance on S_W5 `[THM]` {#sec-g34d}

> **[Guard SG-6 applies]** · **[Guard SG-3 applies]**

`[THM]` [scope: the Hurwitz component S_W5 determined by the W5 tuple] [proof: written geometric argument by the third-family auditor (`auditor_r1/AUDITOR_R1_GEOMETRIC_REPORT_received.md`), using the inputs listed below] [RID: HCG-THM-G34D-SW5] (aliases G34-D, G34-D-ORIENTATION, G34-D-BOUNDARY, G34-D-NILPOTENT, H3-PO-5) [provenance: THIRD-FAMILY CHECKED (auditor R1, fresh scripts); earlier mapped to sources by Claude (`H3_G34D_BRIDGE_PO2_REVIEW_CLAUDE_v0_1.md`) and cross-reviewed by ChatGPT; Claude's assessment of the auditor report: `auditor_r1/H3_G34D_AUDITOR_R1_ASSESSMENT_CLAUDE_v0_1.md`]

The 17 W5 logarithms are realized simultaneously as local monodromies of a polarized weight-one VHS over (Δ*)¹⁷ ⊂ S̄_W5, in the form

  M_j = ε·c_j·A N_j A⁻¹, with c_j ∈ ℤ_{>0}, one common ε ∈ {±1}, and one common A.

The limit is Hodge–Tate, with K-graded dimensions 4/0/4, and the period map to the 16-dimensional domain has complex rank 16 at interior points. Hence (D) holds for S_W5.

Proof structure, as given by the auditor and reviewed here:

1. **Boundary and component.** The 17 interval curves are laminar and form a pants decomposition. Pinching them gives a stable rational curve with 18 components and 17 nodes. Every boundary product is 1, so all node stabilizers are trivial and e_j = 1.
   - The cover is cut along the lifted curves and reglued with the inherited sheet identifications.
   - Smoothing reverses the cut, so the degeneration lies in the closure of S_W5.
   - Sources: Romagny–Wewers Thm 5.6; Abramovich–Corti–Vistoli Thms 3.0.2 and 4.3.2.
   - Upstairs b₁ = 4|G| + 1 agrees with Riemann–Hurwitz, and the σ-part of the graph H₁ has K-dimension 4.
2. **Coefficient transport** (DW06 Thm 1.3). An exact tuple return forces h ∈ Z(G). On σ this element is scalar by absolute irreducibility, and has finite order because G is finite. It lies in μ₆(K). Pointing by a sheet over an unramified exterior section removes it; alternatively, a common sixth-power cover does.
3. **Infinity and complementary curves.** All 20 branch points are kept finite, and ∞ is an unramified section. [19,20] and [1,18] induce **equal** operators on H¹_par: they differ by the coboundary g ↦ (1 − ρ(g))u(A), and are not inverse to each other.
4. **Uniform plumbing orientation.** Take x_θ = e^{iθχ}x₀ and y_θ = e^{iθ(1−χ)}y₀ in xy = q. One full turn gives one twist in the same direction at every node. Base change multiplies the winding by a positive integer. Only a single global convention sign can occur.
5. **Nilpotent orbit.** The VHS is geometric: the σ-isotypic factor of the Jacobian, cut out by a central idempotent and (1 − s₁)/2, with ℚ-dimension 16 and Hodge numbers (4,4).
   - Schmid (4.12) gives Φ̃ = exp(Σ z_j M_j)Ψ(t), with Ψ holomorphic on the full polydisc.
   - For every positive combination M one has M² = 0 and im M = ker M = I. The injectivity of V/I → I comes from semidefiniteness plus definiteness of the sum.
   - On the diagonal arc, Schmid (6.16) gives the limiting MHS. Hodge symmetry forces Hodge–Tate, with V_ι = I_ι ⊕ F¹_∞.
6. **Interior rank.** Write the N_j in blocks [[0,B_j],[0,0]] relative to I. Then det[vec B₁ … vec B₁₆] = 6144(1+w) ≠ 0.
   - The translated differential has columns M_j·Ψ(t) + 2πi t_j ∂Ψ/∂t_j, which tend to M_j·F_∞.
   - A nonzero 16×16 minor therefore survives at small t with every t_j ≠ 0.
   - Power-map covers are étale on (Δ*)¹⁷, so the rank descends.

Inputs read in primary text by the auditor: Schmid 1973, Cattani–Kaplan 1989, DW04/DW06, RW06, ACV 2001 (preprint). **Not read:** Cattani–Kaplan–Schmid 1986, Harris–Mumford 1982, Knudsen 1983. The argument avoids depending on CKS numbering; see E05.

`[COR]` [RID: HCG-COR-D3] The statement "e_j = 1 removes the D-2 base-change concern" was too strong. The correct scope: no node-ramification (Kummer) base change is needed, but finite étale covers for pointing, level or the μ₆ scalars may still be used. These preserve rank. See Appendix B, D-3.

Auditor qualifications retained (findings E01–E06):
- E01: the identification with Appendix A is missing; see §6.17.
- E02: the 17 → 16 map is surjective, not an isomorphism (§6.14).
- E03: exact return vs. return up to conjugation. Moot for W5, which has k = 1.
- E04: the Gram matrix of β_j is S·N̄_j (the session engine complies).
- E05: some sources were not inspected.
- E06: no global theorem is certified.

### §6.16 PO-6 — discriminant of the actual polarized factor `[THM]` {#sec-po6}

`[THM]` [import: hexagon:2610.00386v1 Prop 5.1, Lemma 2.4, §2.2 | RID unavailable] [RID: HCG-THM-PO6] (alias H3-PO-6) [provenance: REVIEWED (Claude, sealed note `auditor_r2/H3_PROP51_POLARIZATION_BRIDGE_CLAUDE_SEALED_v0_1.md`); ChatGPT: "follows conditionally from Prop 5.1"; third-family pending (R2 item 1, bridge part)]

disc H|_{A_σ(C)} = [det h] for C a point of S, and this class is constant on S (Lemma 2.4). The steps:
- H¹(C,K)_σ = V_σ ⊗ H¹_par(U_C, L′).
- β = h_V ⊗ S.
- ψ = c·S∘(Φ×Φ) with c ∈ ℚ^×.
- H|_{A_σ} = ±q·h (or its conjugate), with q = 2h_V(v,v)c ∈ ℚ^×.
- Since the rank is even, q^{2n} = N(q^n).

Applied to W5: d(S_W5) = [1].

Open dependency: Severn's Lemma 5.2 is his [19, Lemma 6.2] (hexagon:2610.00246v2), which is not yet reviewed (OPEN 5). The independent support is DW06 Thm 2.6 (§6.13).

### §6.17 The component question and the transfer theorem `[THM]` {#sec-component}

`[THM]` [import: hexagon:2610.00386v1 Thm 7.1, Remarks 5.3 and 7.3 | RID unavailable] [RID: HCG-THM-ANYCOMP] [provenance: CHECKED (Claude; ChatGPT, "not a logical premise"); third-family pending (R2 item 2)]

Theorem 7.1 requires (L) for the class datum, and (D) and d(S) on **one** connected component S. Remark 5.3 states that "Theorem 7.1 pairs (D) and d on the same component and needs no comparison", and Remark 7.3 says that (L) is a property of the class datum. Hence:

`[RESULT]` `[from: HYP]` [scope: application to Thm 6.2(1)] [RID: HCG-RESULT-SW5-SUFFICES]

S_W5 with (D) (§6.15) and d(S_W5) = [1] (§6.14, §6.16) is a sufficient witness for Thm 6.2(1). Identifying S_W5 with the Appendix A component is not required.
Depends on: HCG-THM-ANYCOMP, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-THM-PO6, and the unrefereed transfer theorem itself (hence `[from: HYP]`).
Consequence of E01: Severn's *own* Appendix A certificate has not been confirmed by anyone in this session (OPEN 3).

### §6.18 H4 selection — exploratory branch `[ALG]` — mixed content {#sec-h4sel}

> **[Local guard SG-9]** RTG-motivated, not RTG-derived; outside the main chain.

`[ALG]` [RID: HCG-ALG-H4-BOUND] [provenance: CHECKED — proposed by ChatGPT; verified by Claude]

Assume (H2): I is maximal isotropic and S is nondegenerate. Then N_j ↦ β_j is ℚ-linear and injective into Herm₄(K), which has ℚ-dimension 16. Consequences:
- dim_ℚ span N_j ≤ 16;
- 17 curves always carry a linear relation (this explains E02);
- (H4) ⇔ the β_j span Herm₄(K).

Herm₄(K) is the unipotent radical of the Siegel-type parabolic of U(4,4). The bound is standard. Only a predictive criterion would be new.

`[ALG cert]` [horizon: W5, W6, W7 tuples × {balanced, comb}] [RID: HCG-ALG-H4-OBS] [proof: `h4sel/h4_obstruction.py`] [provenance: PROPOSED (Claude); ChatGPT replication requested]

| Tuple | Decomposition | ℚ-rank of the β_j | dim of obstruction | Annihilating form Y |
|---|---|---|---|---|
| W5 | balanced | 16 | 0 | — |
| W5 | comb | **15** | 1 | rank 4, signature (2,2) |
| W6 | balanced | 15 | 1 | rank 2, signature (1,1) |
| W6 | comb | 16 | 0 | — |
| W7 | balanced | 15 | 1 | rank 2, signature (1,1) |
| W7 | comb | 16 | 0 | — |

Here Y is defined by tr(β_j Y) = 0 for all j. For all three tuples, I is the same in both decompositions: it is spanned by the images of the 10 shared pair curves. Obstruction directions are therefore comparable in one frame.

`[HYP]` [RID: HCG-HYP-EDGEFORM] The β_j are the σ-isotypic edge forms of the upstairs dual graph Γ, built from H₁(Γ)_σ of K-dimension 4 (chain dimensions 102 → 98). (H4) is then a tropical-Torelli-type spanning condition.
Test: an exact comparison on all 40 (tuple, decomposition) cases.
Literature to compare before any novelty claim: Caporaso–Viviani; tropical Prym work; Brosnan arXiv:2609.14169; Severn Rem 4.4; Alexeev–Donagi–Farkas–Izadi–Ortega.

---

<a id="hcg-7"></a>

## §7 Import Ledger

**RTG imports (one-way; charter §1).** All are hard-coded with provenance in `h1_h2_exact_checks.py`; no session script reads an RTG file.

- [RID: DYAD-ALG-Q-INVARIANT-FORM et al.] :: R1 A = [[1,−1],[1,0]], A³ = −I; R2 B, AᵀBA = B :: RTG_DYADIC_OSCILLATOR_DSN v6.4.18 §§6.1–6.3; GENESIS v2.8.9 §1 :: linear data, §6.1 :: selected continuous dyad model, not a physical lattice
  Source status: owner ALG. Verification: recomputed exactly (H1-01…04). Synchronization: v6.4.19 (SHA-256 40c9e63f…) declares the R1–R5 mathematics unchanged.
- [RID unavailable] :: R3 J_Q = (2A − I)/√3 :: GENESIS v2.8.9 §6.6 :: complex structure :: the B-quarter-turn, not a Euclidean 90° turn
- [RID: DYAD-THM-C21; DYAD-ALG-NF6] :: R4 μ, a₀₅ :: DYAD v6.4.18 §§6.7, 6.14 :: cross-check of the normal form :: chart-specific
  Verification: recomputed from T in the chart z = ρ + ζ₃η; exact match (HCG-ALG-NF).
- [RID: DYAD-THM-SMOOTH-EMBEDDING] :: R5 smooth flow embedding of T⁶; order-six generator G₆ :: DYAD v6.4.18 §6.17 :: context only :: local smooth germ, not holomorphic
- [RID: DYAD-THM-PRIM-CTR] :: R6(a) the origin is a local attractor of T⁶ :: DYAD v6.4.19 §6.14 :: premise of HCG-THM-R6B :: fixed T on the dyadic carrier
- [RID: RTG SG-PROG-1] :: R8 programme boundary :: RTG_PROGRAMME_OVERVIEW v1.2; OFN v0.10 :: governs SG-2 :: interpretation only
- Reference only, not load-bearing: FMS v0.6.4 §5.2 (noncanonical) is consistent with R7.

**External mathematical imports.** All Severn and Hippeläinen documents are unrefereed Hexagon drafts (SG-5). File hashes are in `SOURCE_MANIFEST.md`.

- [RID unavailable] :: Severn Thm 6.2, Thm 3.1, Prop 4.2, Lemma 4.1, Prop 5.2, Appendix A :: hexagon:2610.00387v1, Draft v0.5, 16 Oct 2026 (PDF 7aa80a3b…) :: §§6.6–6.17 :: unrefereed
  Verification: source read in full text (Claude); ChatGPT and the auditor read the relevant sections.
- [RID unavailable] :: Severn transfer theorem: Def 2.2, Lemmas 2.3–2.4, 3.4, Prop 3.7, Cor 3.8, Prop 5.1, Lemma 5.2, Lemmas 6.1–6.2, Thm 7.1, Rem 5.3/7.3 :: hexagon:2610.00386v1, Draft v0.15 (PDF d39fdb28…) :: §§6.9–6.17 :: unrefereed
- [RID unavailable] :: Severn [−2] paper; CONV-1; Lemma 6.2 (cocycle formula) :: hexagon:2610.00246v2 (PDF 7b81d2ac…) :: §6.6; OPEN 5 :: unrefereed
- [RID unavailable] :: Hippeläinen, non-split [−2] :: hexagon:2610.00371v1 (PDF fa33d20c…) :: CONV-1 only :: Claude-agent-produced; Claude recused
- `[MATH]` :: Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality*, Sém. Congr. 13 (2006), arXiv:math/0411119 (PDF 68a9f46f…) :: Thm 1.3, Rem 1.4, Asm 1.2, Thm 2.3, Thm 2.6 :: §6.13, §6.15
- `[MATH]` :: Milne, *Lefschetz classes on abelian varieties*, Duke Math. J. 96 (1999) (PDF 28ae245e…) :: Thm 3.2, Lemma 3.1 :: §6.9
- `[MATH]` :: Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Math. 65 (1988) 3–32 (PDF 3794a85d…) :: Thm 2.0, Cor 3.1, Thm 3.2 :: §6.6, §6.9
- `[MATH]` :: Schmid, Invent. Math. 22 (1973) :: (4.12), (6.16) :: §6.15 (read by the auditor)
- `[MATH]` :: Romagny–Wewers (2006) Thm 5.6; Abramovich–Corti–Vistoli (2001 preprint / 2003) :: §6.15 (read by the auditor)
- `[MATH]` :: Brauer induction (Serre, *Linear Representations* §10.5); Landherr; Baily–Borel; Lefschetz (1,1); Chevalley–Weil :: classical, not reread
- Not inspected by anyone in the session: Cattani–Kaplan–Schmid 1986 (bibliographic record only); Harris–Mumford 1982; Knudsen 1983.
- Literature-map sources (abstracts or secondary only): Markman, Floccari–Fu, van Geemen–Rapagnetta, Mostaed, Li, Patel–Zhang, Saller, Bhattacharjee, the OpenAI preprints and withdrawal, and the Voisin essay. See `SOURCE_MANIFEST.md` §B.

---

<a id="hcg-8"></a>

## §8 Artifact and Script Registry

Package root: the session workspace, directories `hodge_session/` and `g34/` (with subdirectories `auditor_r1/`, `auditor_r2/`, `cg_w6w7_in/`, `cg_replay/`, `h4sel/`). Full hash lists are in `SHA256SUMS_SESSION.txt` (53 artifacts, 21 Oct), `SHA256SUMS_W6W7.txt`, `auditor_r1/SHA256SUMS_AUDITOR_R1.txt`, `auditor_r2/SHA256SUMS_AUDITOR_R2.txt` and `h4sel/SHA256SUMS_H4SEL.txt`. Hashes below are 16-hex prefixes.

- [RID: HCG-ART-H1H2] :: `h1_h2_exact_checks.py` (3b3deb4c5db2636f) :: H1/H2/NF exact checks :: EXECUTED (Claude), 28/28 PASS; log `h1_h2_run_log.txt` (3c8db6710f5dcfd9)
  Independence: ChatGPT used fresh code with different constructions. The checks are algorithmically independent but **not historically blind**, because the sealed bundle arrived together with the contract.
- [RID: HCG-ART-E6] :: `e6_control.py` (1e0bb2946dd42a5e) :: E⁶ 400 = 400; A*-fixed 402 :: EXECUTED; CHECKED
- [RID: HCG-ART-G34A] :: `g34_gateA.py` (b6b80208f7cb13c3), `g34_gateA.json` (c8a4605175ff63cc) :: G₃₄ from K₁₂ :: EXECUTED (~30 s)
- [RID: HCG-ART-ENGINE] :: `g34_gateB.py` (324f11e8f826c0c7) :: exact ℚ(ω) engine (cocycles, S, twists, H0–H4); reads ROOTS_JSON :: EXECUTED. The fast twist formula was cross-checked against free-group words (`g34_w5_braid_crosscheck.py`, 7b1db2aa2931bab4)
- [RID: HCG-ART-SEARCH] :: `g34_gateC_search.py` (fb8ad8417fe18304), `g34_gateC_stats.py`, `g34_gateC_alt.py` (efc5aaccdf02a213), `g34_gateC_alt2.py` (7f3b375be60dc0f0), log `g34_gateC_alt2_log.txt` (c2510faa7849b4e0) :: witness searches :: EXECUTED
- [RID: HCG-ART-CERT-W5] :: `g34_cert_tuple5_balanced.json` (172766a91017aeac), `roots_alt_5.json` (480cd6dc95f1a802) :: W5 certificate :: AVAILABLE; rechecked by ChatGPT and by the auditor (byte-identical input confirmed)
- [RID: HCG-ART-CERT-W6W7] :: `g34_cert_W6_comb.json` (ae9048784171da49), `g34_cert_W7_comb.json` (45097b3042f30dcb), `roots_W6.json` (ca4551c2b651cce2), `roots_W7.json` (1b9e96aa495bceb1), dumper `g34_cert_dump_generic.py` (e38644342a22897f), reader `audit_cert.py` (83f05ba331b201ee) :: W6/W7 certificates :: AVAILABLE; ChatGPT scripts replayed in `cg_replay/` (all PASS)
- [RID: HCG-ART-CUPDIAG] :: `g34_w5_invariant_forms*.py`, `g34_w5_monodromy_*.py`, `toy/toy_monodromy.py` (95201ab54d6f6c75) :: cup-uniqueness diagnostic :: EXECUTED; inconclusive (§6.13)
- [RID: HCG-ART-E02] :: `auditor_r1/relation_check.py` (b48d4571e9140efc), output (669398de78fe57a5) :: N_j nullspace and return exponents :: EXECUTED
- [RID: HCG-ART-DISC-CG] :: `auditor_r2/h3_w5_disc_crosscheck_v0_1.py` (e9de258b6f2e85b4) :: ChatGPT det h check :: received; input hash matches the W5 certificate
- [RID: HCG-ART-H4SEL] :: `h4sel/h4_obstruction.py` (0b262cf3be24a307), `obs_alt_5.json` (45a0b19c5bec5fe7), `obs_W6.json` (e04d483b02f74524), `obs_W7.json` (7570d657cdd7900a) :: obstruction analysis :: EXECUTED (Claude only)
- [RID: HCG-ART-AUDITOR-R1] :: `auditor_r1/AUDITOR_R1_GEOMETRIC_REPORT_received.md` (d72d3616a4beb61b) :: third-family geometric audit :: RECEIVED. The auditor's executable package (`G34D_W5_FIRST_ROUND_GEOMETRIC_AUDIT_v0_1.zip`) has **not been received**.
- [RID: HCG-ART-AUDITOR-R2P] :: `auditor_r2/AUDITOR_R2_PARTIAL_DISC_received.md` (5b318e3fb96bd009) :: R2 discriminant (partial) :: RECEIVED, transcribed from the PI's message
- Sources: the PDFs and hashes are in `SOURCE_MANIFEST.md` §A.

---

<a id="hcg-9"></a>

## §9 Collaboration and Provenance

| Contributor | Actual role in this session |
|---|---|
| Mustafa (PI) | Session owner. Decides ACCEPTED. Relays all inter-AI and auditor traffic. Approved and sent the round-2 auditor request v0.2. No PI decision has been recorded on any row yet. |
| Claude (Anthropic) | Primary deriver for H1/H2/NF/R7 and all G₃₄ computations (gates A–C, W5–W7, H4 data). Independent H3 literature review. Full reviews of PO-1…PO-4. G34-D source mapping. Consolidation editor of this DSN. |
| ChatGPT (OpenAI) | Independent verifier of H1/H2/NF/R7. Independent H3 review; found the Severn preprints (H3-D1). Second proof of PO-1 (L_ξ). Cross-checks of G34-A, B0, the W5 braid rebuild, DW06 Thm 2.6 cup validation, PO-2/3/4, W5 discriminant, W6/W7. Proposed the H4 bound and the H4-selection branch. Scope corrections D-2 and D-3. |
| Third-family auditor (model family outside Claude/OpenAI; identity held by the PI) | Blind geometric audit of G34-D on W5 (round 1). Independent discriminant on W5 (round 2, partial). Detected the arXiv/Hexagon ID error (SRC-1). |

**Protocol** (charter §0.3; ledger v0.2 independence qualification):
- Each claim carries one review state.
- Neither AI may close the other's disagreement or record a check on the other's behalf.
- Corrections are dated addenda; immutable records are never silently edited.
- H3 literature reports were exchanged only through the PI.
- The auditor round is blind (SG-10).

**Conflict-of-interest record:** Severn's source page states that the work was developed mainly with Claude models and audited with OpenAI models, and Hippeläinen's note was produced by Claude agents. This is the reason a third-family review and a human referee are required (SG-4, OPEN 6).

**DISAGREEMENT_LOG** (all closed; each resolution recorded by the conceding party):

| # | Item | Resolution |
|---|---|---|
| D-1 | NF-04…07: ChatGPT's script set μ = 6ω̄τ instead of checking it | Closed. ChatGPT ran a sixfold composition plus an induction proof and withdrew its overstatement. |
| H3-D1 | Claude's v0.1 literature review missed the Hexagon preprints of 14–20 Oct 2026 | Closed. Claude conceded; the frontier is on HOLD (H3-FRONTIER-01). |
| D-2 | Claude: "k = m = 1 ⇒ no base change" | Closed. Claude conceded the scope correction; no effect on (H1)–(H4). |
| D-3 | Claude's 22 Oct chat summary: "e_j = 1 ⇒ the D-2 concern disappears" | Closed. Claude conceded; see HCG-COR-D3. |

---

<a id="hcg-appendix-a"></a>

## Appendix A — Version History

### v0.1 — 22 October 2026 — DRAFT (consolidation)

- **All sections [governance]:** First consolidated DSN of the session, written to DSN Methodology v1.3. It consolidates without changing scientific content. Inputs:
  - charter v0.1/v0.2;
  - H1/H2 contract;
  - R7 proof note;
  - ledgers v0.1–v0.4 and addenda v0.4a–d;
  - the Claude reports (H3 literature; proof-obligation review; G34 gates A, B/C; W5 cup addendum; G34-D/PO-2 bridge; PO-2/3/4 full review; W6/W7 witness addendum; auditor R1 assessment; sealed Prop 5.1 note; H4 first data);
  - the ChatGPT inputs received in this session (PO-2/3/4 cross-review and delta; next-step decision and discriminant check; W6/W7 review and repro package; H4 proposal);
  - the auditor's R1 report and R2 partial result.
- **Typing [scope/typing]:** Session review states were moved to the `[provenance:]` axis. External theorems are tagged `[EXT-CLAIM]` or imported `[THM]` with an unrefereed scope. RIDs were assigned in the session-local `HCG-` namespace, with historical aliases kept.
- **Status changes recorded here, all as proposals and not PI-adopted:**
  - G34-D on S_W5: EXPERT-CHECK PENDING → THIRD-FAMILY CHECKED.
  - H3-PO-5: CONDITIONAL-HOLD → CHECKED on S_W5.
  - G34-D-DISC-W5: three-family checked.
  - W6/W7: CHECKED.
  - H3-PO-6: REVIEWED.
  - The Severn Thm 6.2 grade is unchanged (CLAIMED).

**Underlying session chronology** (immutable records; 21–22 Oct 2026):

1. Imaginary-unit exchange: R6b, plus the R7 and uniqueness question.
2. Charter v0.1, then v0.2 (C1–C6).
3. H1/H2 contract, then Claude's 28/28 run, then ChatGPT's verification and ledger v0.2 (D-1 opened).
4. D-1 closed. H3 reports exchanged blind through the PI.
5. ChatGPT found the Severn and Hippeläinen preprints: H3-D1, frontier on HOLD, H3-T1 → H3-T1-R.
6. Claude's proof-obligation review: PO-1 proof, chain mapped.
7. ChatGPT's PO-1 cross-check and the G34 independent-certification contract.
8. Gate A: G₃₄ from K₁₂.
9. Gates B/C: engine, tuple #0 negatives, W5 found.
10. ChatGPT's W5 checks.
11. Cup-uniqueness attempt (inconclusive), then DW06 cup validation (CHECKED).
12. G34-D mapped to sources, then ChatGPT cross-review (D-2), then the third-reviewer packet.
13. PO-2/3/4 full review, then ChatGPT cross-review, then ledger v0.4.
14. Source-ID correction (SRC-1…3).
15. alt2 search: W6 and W7 (v0.4a).
16. Auditor R1, then Claude's assessment (v0.4b).
17. Auditor R2 request v0.2 sent by the PI. R2 partial discriminant result, then the sealed Prop 5.1 note (v0.4c; D-3).
18. ChatGPT H4 proposal, then H4 obstruction data.
19. ChatGPT W6/W7 review, replayed by Claude (v0.4d).

---

<a id="hcg-appendix-b"></a>

## Appendix B — Retired and Rejected Claims

`[SUPERSEDED]` [RID: R6 (charter v0.1)] Original: R6 stated through a C³-involution hypothesis. Reason: the hypothesis is unnecessary; local attraction alone gives non-conjugacy to T⁻¹. Replacement: HCG-THM-R6B. Recorded in: charter v0.2 (C1).

`[RETRACTED]` [RID: H3-CLAUDE-LIT-v0.1 §0.3, §4, §6] Original: "no 2026 preprint covers non-split generic Weil sixfolds"; "δ = −2 uncovered"; H3-T1 as a coverage task with a certified open class. Reason: the Hexagon preprints of 14–20 Oct 2026 (Severn, Hippeläinen) claim these cells (H3-D1). Replacement: HCG-RESULT-T1R; H3-FRONTIER-01 = HOLD. Recorded in: proof-obligation review v0.1 §0 (A-1).

`[SUPERSEDED]` [RID: CONV-1 (open)] Original: whether Schoen's "δ = 1" sixfolds are split was unresolved. Replacement: HCG-ALG-CONV1 (split, by citation). Recorded in: proof-obligation review v0.1 (A-2).

`[RETRACTED]` [RID: ChatGPT NF-04…07 report wording] Original: the coefficients were described as "obtained from the sixth iterate", when they were set from the relation μ = 6ω̄τ. Reason: D-1. Replacement: HCG-ALG-NF (explicit composition plus induction). Recorded in: ledger v0.3.

`[RETRACTED]` [RID: Claude G34-D-BOUNDARY wording] Original: "k = m = 1 ⇒ no base change"; later "e_j = 1 ⇒ the D-2 concern disappears". Reason: D-2 and D-3. Replacement: HCG-COR-D3. Recorded in: ledger v0.4 and addendum v0.4c.

`[COR]` [admin key SRC-1] In the first third-reviewer package, the Severn manuscripts were cited as arXiv 2610.00387 and 2610.00386. Those arXiv numbers belong to unrelated papers. The correct identifiers are hexagon:2610.00387v1 and hexagon:2610.00386v1. Claude's documents never used the "arXiv" label, but they used bare IDs (SRC-2); every bare 2610.0038x means hexagon:. Recorded in: ledger v0.4 §G.

`[FAIL]` [RID: HCG-ALG-CUP-UNIQ-ATTEMPT, route only] Route: certify S as the intersection form through uniqueness of monodromy-invariant forms, using sampled braids. Basis: all sampled elements commute (a 34-dimensional invariant space); this is a sampling limitation, not evidence against S. Replacement: HCG-ALG-CUPVAL (DW06 Thm 2.6). Recorded in: W5 cup addendum v0.1.

`[COR]` [admin key G34-D-STATUS] Ledger v0.4 and ChatGPT's W6/W7 delta (22 Oct, written before auditor R1) record G34-D as "EXPERT-SIGNOFF-PENDING". Superseded by HCG-THM-G34D-SW5 (THIRD-FAMILY CHECKED on S_W5). Recorded in: addenda v0.4b and v0.4d.

---

*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.1 · DRAFT · INTERNAL (withhold from the third-family auditor until round 2 is complete) · not RTG-adopted, not PI-adopted.*
