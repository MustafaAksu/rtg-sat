# HCG-HURWITZ-HODGE-OBSTRUCTION — opening note v0.1

**Track:** HCG-HURWITZ-HODGE-OBSTRUCTION (short form **HHO**). This is a noncanonical research track inside the standalone HCG session.

**Date:** 3 November 2026

**Status:** OPEN research track. This note is INTERNAL. It is not adopted science and not part of HCG v0.2 or of any HCG v0.3 draft. **It is not part of RTG** (SG-1).

**Opening decision (PI, quoted verbatim):** "HCG-HURWITZ-HODGE-OBSTRUCTION'ın kanonik olmayan bir HCG kolu olarak açılması uygun". English: "Opening HCG-HURWITZ-HODGE-OBSTRUCTION as a noncanonical HCG track is appropriate."
- Source: PI session message, Tue 3 Nov 2026, 10:22 +03:00.
- The decision covers opening the track only. It does not accept any claim listed here. Every claim keeps the review state recorded below, and the PI-decision fields for claims stay blank.

**Governing records (unchanged by this note):**
- `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (SHA-256 276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0)
- `HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` (75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7)
- The noncanonical change log `HCG_DSN_v0_3_PENDING_DELTAS.md`. Its Δ27 entry and addenda 1–17 hold all evidence cited here.

**Founding documents:**
- ChatGPT `HCG_HURWITZ_HODGE_OBSTRUCTION_FRAMEWORK_SESSION_v0_1.md` (aeb6f9e7…)
- Claude `H3_FRAMEWORK_REVIEW_AND_EULER_GATE_CLAUDE_v0_1.md` (cc31ef06…; ZIP c1059007…)
- ChatGPT `HCG_OBSTRUCTION_FRAMEWORK_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` (9e465f38…)
- Claude `H3_FRAMEWORK2_REVIEW_AND_REAL_DATA_CLAUDE_v0_1.md` (72130efc…; ZIP 062353a4…)

---

## 1. Purpose and scope

**Object.** Severn-type genus-0 Hurwitz transfer data

  𝒟 = (K, Γ, σ, (g₁, …, g_N), h₀),

where:
- K = Q(√−3);
- σ: G → GL_d(K), with image Γ = σ(G);
- g₁ ⋯ g_N = 1 is a generating product-one tuple;
- h₀ is a positive K-Hermitian form preserved by Γ.

The track asks which necessary conditions such a datum must meet to produce a **nonsplit, dominant Weil-eightfold family**. It builds those conditions into reproducible, braid-stable **obstruction certificates**.

**Two targets, kept apart.**

| Target | Content | State |
|---|---|---|
| **T1** (reachable) | Proved necessary conditions ("gates") and finite certificates that rule out specific data or classes of data | substantial partial results (§4) |
| **T2** (open) | A dimension-independent reason why the Severn genus-0 transfer method cannot reach a nonsplit cell under (H) | OPEN |

**Out of scope:**
- Any statement that nonsplit Weil eightfolds do not exist.
- Any negative or positive statement about the Hodge conjecture.
- Any RTG claim.
- Any change to the status of Severn's Theorems A/B/C. These stay **CLAIMED**, and Severn's documents are cited as `hexagon:2610.00xxxvN` (SG-3, SG-5).

## 2. Standing hypotheses (H)

As used throughout Δ27:

1. Γ is finite and absolutely irreducible over K, with character field exactly K. It preserves the positive Hermitian form h₀ and has no fixed vectors.
2. The Weil part M_σ = H¹_par(P¹, σ) has dim_K M_σ = 8 (n = 4) and signature (4, 4).
3. **(D) dominance:** the period map has rank 16.
4. The budget relations hold. With c_j = rank(1 − g_j):
   - Σ_j c_j = 2d + 8 (an identity, from dim H¹_par = Σc_j − 2d = 8);
   - N_eff ≥ 19 (the base dimension N − 3 must reach 16);
   - ε := Σ_j (c_j − 1) ≤ 2d − 11.

**(L)**, Severn's supplier condition e_σ ∈ L(D) (HCG v0.2 §6.9 and §6.11), is a **separate** hypothesis and is not part of (H).

## 3. Gate catalogue (necessary conditions)

Each gate is a necessary condition. Failing any gate excludes the datum, and in most cases the whole braid orbit, since the gates depend only on the multiset of local Γ-classes and on Γ itself.

| Gate | Statement | Review state | Record |
|---|---|---|---|
| **G1 Budget** | Σc_j = 2d + 8 | identity under (H) | Δ27 |
| **G2 Base dimension** | N_eff ≥ 19 for (D) | identity under (H) | Δ27 |
| **G3 Ages / signature** | Σ age(g_j) = Σ age(g_j⁻¹) = d + 4 | CHECKED (two AIs) | add. 7 |
| **G4 Local discriminant** | HCG-THM-PARABOLIC-DISC-LOCALITY: [det ϑS] = [(−1)ⁿ Π a_j b_j], a_j = det(h₀\|E_j), b_j = det((1 − g_j)\|E_j) | CHECKED (two AIs); the formula Severn announced, proved independently here | add. 2–3 |
| G4a Inert-prime criterion | for D > 0: [D] = [1] ⇔ v_p(D) is even for every p ≡ 2 (mod 3) | CHECKED (two AIs) | add. 16 |
| G4b Reciprocal pairing | local classes pairable by **K-isometric** (e.g. Γ-) conjugacy to inverses ⇒ [(−1)ⁿ], hence split for n = 4; C-conjugacy alone is insufficient | CHECKED (two AIs) | add. 16 |
| G4c Real local monodromies (Lemma R′) | for g K-isometrically conjugate to g⁻¹: [a b] = [Π_{n≥2, 3∤n} disc(E_{Φₙ})·Φₙ(1)^{dim/φ(n)}] | PROPOSED (Claude) | add. 17 |
| **G5 Period factorization** | induced-period bound rank Per ≤ 3γ − 3 + s (field-free: any C-imprimitive datum needs γ = 0, r ≥ 6); Lemma E (K-defined induction keeps (H) and the class) ⇒ K-imprimitive needs d ≥ 2L, for the current bound L | CHECKED (two AIs); cutoff checked at L = 46 | add. 4–6, 15 |
| **G6 Reflection dichotomy** | Theorem R: a complex reflection in Γ ⇒ split | CHECKED (two AIs) | add. 5 |
| **G7 Primitive movement** | Lemma C: some noncentral element h of the socle has c(h) ≤ 2c_min; Lemma S sharpens this for self-dual socles; symplectic type impossible; Lemma F (S_{d+1}·scalars) | CHECKED (two AIs) | add. 5, 8–10 |
| **G8 Imprimitive** | Lemma A′ (Clifford system of the kernel); two-block lemma with Lemma B/B′ for non-K-defined blocks, 13 ≤ r ≤ 29; E_k = 2r + 2k² − 21k + 8 ≥ 0 | CHECKED (two AIs) | add. 10–12, 14–15 |
| **G9 Tensor** | tensor-induced needs d ≥ 256; **Lemma T′** for factorwise A ⊗ B: Σδ_i − max δ_i ≥ a (Euler count; it contains the three-pseudoreflection lemma) | CHECKED (two AIs) | add. 7, 12, 15, 17 |
| G9a 2 ⊗ b, S_{b+1} branch | three-active reduction | CHECKED (two AIs) | add. 16 |
| | gates (E) Euler, (Di) dihedral, RH parity, determinant; scans close 24 ≤ b ≤ 64; analytic reduction leaves two type patterns for large b | PROPOSED (Claude); ChatGPT replayed to b = 35 | add. 16–17 |
| **G10 Classification inputs** | Hiss–Malle 2001 + 2002 corrigenda, including the generic families; GT08 reduction; GT12 Cor. 1.6; CTblLib 1.3.7 data; Katz–Tiep §16 (U₇(2)) | source-conditional external inputs, not reproved | add. 6–15 |
| **G11 Supplier (L)** | PO-4: every local monodromy conjugate to its inverse ⇒ (L) | INTERNAL CHECKED in v0.2; THIRD-FAMILY upgrade proposed in Δ24 | v0.2 §6.11; Δ24 |
| **G12 Cup to polarization** | moving the parabolic-cup class to the polarized abelian factor needs the cup–polarization identification. This is established for W5 only (HCG-EXT-PO6). | requirement | v0.2 §6.16 |

## 4. Results that seed the track

**R1 (CHECKED, two AIs; source-conditional).** Under (H), a nonsplit dominant datum needs **d ≥ 53** (Δ27 add. 17). Dependencies:
- gates G3–G10;
- the classification inputs G10;
- the cup/polarization bridge G12 wherever the class is read as a polarization discriminant.

R1 is not a construction and not an existence result.

**R2 — calibration objects** (all CHECKED unless marked):

| Datum | (L) | (D) | Class | What it separates | Record |
|---|---|---|---|---|---|
| G₃₄ / W5 | ✓ | ✓ on S_W5 | **[1]** | passes every gate and is split | v0.2 |
| C₆ separator (2⁵, 3, 4³, 5) | ✗ | impossible | **[2]** | nonsplit is possible without (L) | Δ27 |
| C₃ control (1⁵, 2⁵) | ✓ | impossible | [1] | — | Δ27 |
| **G₂₆-type real witness**: N = 6, c = (2,3,2,3,2,2), dim H¹_par = 8, signature (4, 4), field K | ✓ by PO-4 | impossible (N − 3 = 3) | **[2]**, computed directly from the cup form | **(L) does not force split** | add. 17, PROPOSED |

**R3 — structural facts** (PROPOSED, Claude; add. 17):
- The reciprocal-pairing gate G4b is strictly stronger than reality: real data can be nonsplit, pairable data cannot. This follows from G4b and the R2 witness.
- Monomial data built from order-2 reflections with the standard form are always split, by the parity of the diagonal character.

## 5. Research programme

These are proposals; their ordering is a PI decision.

| Code | Question | Closure criterion |
|---|---|---|
| **P1 — revised first target** | **Dominance versus the local class product.** Is there a d-independent obstruction to a nonsplit class under (H)? "(L) ⇒ split" is false at the class-datum level (R2), so any such theorem must use (D) or the budget. | Written theorem with explicit hypotheses, or a dominant candidate that survives every gate |
| P1a | Can the mechanism of the R2 witness (Φ₄ factors with odd total contribution, G4c) be realised inside a group large enough to meet N ≥ 19 and the budget? Under R1 this needs d ≥ 53. | Explicit search space and screen |
| **P2** | 2 ⊗ b for all b: finish the analytic reduction of the S_{b+1} branch (the two remaining type patterns), and close the block-system branches. | Universal exclusion, or the smallest escaping b |
| **P3** | The imprimitive frontier beyond r = 29 (the two-block S_{r+1} branch for r ≥ 30, d ≥ 60), and Galois-stable systems in general. | Lemma covering all r, or an explicit gap list |
| **P4** | A family-level primitive movement gate: replace the degree-by-degree CTblLib screens by uniform character-ratio bounds for groups of Lie type in cross characteristic. These sources still have to be found and read; none is cited yet. | Sourced lemma with explicit constants |
| **P5** | Certificate format and tooling: a braid-stable certificate schema (local Γ-classes, Gram data, budget, gate verdicts); reproducible scripts; a registry of calibration objects. | Schema document plus a reference checker replayed by both AIs |
| **P6** | The structure of (L) beyond PO-4's sufficient condition, and its relation to G4b and G4c. | Characterization, or a separating example list |

## 6. Working rules

**Inherited.**
- All HCG rules and safeguards SG-1 to SG-12 of v0.2 apply, including the SG-10 blindness rule and the separate human-referee process.
- Two-AI protocol with review states PROPOSED → CHECKED → THIRD-FAMILY CHECKED → ACCEPTED. ACCEPTED is a PI decision only.
- Hashes on every deliverable; received archives are extracted into their own directory and replayed with `python3 -I`.
- Never invent hashes, approvals or file contents.
- Light GAP runs in the session workspace; heavy runs on the PI's machine.
- No RTG owner DSN edits, and no session files written into the RTG project.

**Track-specific safeguards.**
- **HHO-SG-1.** A failed gate excludes that datum or class of data only. Never write "nonsplit Weil eightfolds do not exist" or any Hodge-conjecture conclusion.
- **HHO-SG-2.** A source-conditional result lists its external inputs (G10) every time it is restated.
- **HHO-SG-3.** (L), (D) and "split" are independent gates. None is inferred from another without a proof; R2 shows that (L) does not imply split.
- **HHO-SG-4.** A parabolic-cup class is not a polarization discriminant without the identification of G12.
- **HHO-SG-5.** A finite scan certifies only its stated range and model (SG-6); scans stay PROPOSED until replayed independently.
- **HHO-SG-6.** Toy witnesses that fail (D) are not counterexamples to any Severn theorem and say nothing about (H)-data.

**Naming.**
- New claims use RIDs `HCG-HHO-…` in the HCG session-local namespace; this is not an RTG namespace.
- Files are named `HCG_HHO_…` (ChatGPT) and `H3_HHO_…_CLAUDE` (Claude).
- Evidence continues to be logged in `HCG_DSN_v0_3_PENDING_DELTAS.md` under a new entry, Δ28 (HHO).

## 7. Initial claim register

| RID | Claim | Review state |
|---|---|---|
| HCG-HHO-R1 | Nonsplit under (H) ⇒ d ≥ 53 | CHECKED (two AIs), source-conditional |
| HCG-HHO-G4B | Reciprocal-pairing corollary (K-isometric pairing) | CHECKED (two AIs) |
| HCG-HHO-G4A | Inert-prime norm criterion | CHECKED (two AIs) |
| HCG-HHO-G4C | Lemma R′ | PROPOSED (Claude) |
| HCG-HHO-T-PRIME | Lemma T′ (Euler gate for factorwise tensors), D_min = max(t, a + ⌈a/(t − 1)⌉) | CHECKED (two AIs) |
| HCG-HHO-2XB-REDUCTION | Three-active reduction in the S_{b+1} branch | CHECKED (two AIs) |
| HCG-HHO-2XB-SCAN | S_{b+1} branch closed for 24 ≤ b ≤ 64 (Euler, dihedral, RH parity, determinant) | PROPOSED (Claude); ChatGPT replayed to b = 35 |
| HCG-HHO-LSEP | Real data with (L) and a nonsplit class exist (G₂₆-type witness; fails (D)) | PROPOSED (Claude) |
| HCG-HHO-T2 | Dimension-independent obstruction under (H) | OPEN |

The earlier RIDs keep their names and records (Δ27): HCG-THM-PARABOLIC-DISC-LOCALITY, HCG-THM-INDUCED-PERIOD-BOUND, HCG-LEM-NONSPLIT8-NORMAL-REFL, the C₆ separator and the C₃ control, among others.

## 8. Open PI decisions (blank)

- Confirmation of the first target (P1 as revised above): *(blank)*
- Any review-state upgrades in §7: *(blank)*
- Whether and when HHO results are proposed for an HCG v0.3 draft: *(blank)*
- Third-family audit or human-referee plans for R1 or for the gates: *(blank)*
