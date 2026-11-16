# HHO — (D) source reading: how dominance is established, what it says about the class, and the HCG re-pin diff (Claude)

**Date:** 16 Nov 2026. **Level:** `[SESSION]` reading note, Claude HHO owner session. PI decision of 16 Nov 2026: "(D) kaynak okumasına başlayalım o zaman." **Status:** PROPOSED reading by one AI. No computation was run. No register row, grade, release record or tag changes. HHO's governing edition is `hho-v0.4`, pinned to `hcg-v0.2`.
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist, and none about the Hodge conjecture. Severn's results stay CLAIMED. HCG material is cited as an **HCG input, not an HHO result**.

## 1. What was read

| Source | Extent | SHA-256 |
|---|---|---|
| `hcg/HCG_STUDY_LEDGER.md` at `hcg-v0.5` (commit `799081a`) | §1.5, §2 (OPEN registry), §6.1, §6.7–§6.17, §6.22–§6.25, in full | `650c301f8465536705c852113fa7c2e2288d8c3e3cae99fa92a9c466e47bf383` |
| `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md` at `hcg-v0.5` | in full | `7d2736efc9f49db336ef6279f7a9bd65f7071bd584e149fa08e145989d8f4419` (the hash HHO already cites) |
| `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` at `hcg-v0.5` | Δ25 (the boundary-Witt row), targeted | `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d` |

**Not read:** Severn's texts (all statements about them are HCG's readings); the auditor's own geometric report (HCG holds a received copy; I read only the ledger's summary of it, §6.15); Schmid, Cattani–Kaplan, Romagny–Wewers, Abramovich–Corti–Vistoli; Brosnan arXiv:2609.14169 (named in Δ25 as a prior statement, identity unconfirmed by HCG).

## 2. How (D) is established in the record

**One method, one component.** (D) — period rank n² = 16 at some point of a Hurwitz component — is proved in the whole record for exactly one component, S_W5 (`HCG-THM-G34D-SW5`, THIRD-FAMILY CHECKED, §6.15). The method has three parts.

1. **A boundary criterion.** Severn's Prop 4.2 (v1) / Prop 8.5 (v2), as HCG reads it: at a laminar boundary datum (a pants decomposition with nilpotent logarithms N_j and forms β_j(x, y) = S(x, N_jy)),
   - (H1) N_jN_k = 0; (H2) I = Σ im N_j is S-isotropic of K-dimension n and N_j(I) = 0; (H3) each β_j is semidefinite and Σβ_j definite. Together they make the limiting mixed Hodge structure **Hodge–Tate with W₀ = W₁ = I**.
   - (H4) dim span N_j = n², so the orbit map has full rank.
   - (H0), a Clemens–Schmid count, is a hypothesis in v1 and derived in v2.
2. **A geometric bridge** (the third-family auditor's argument, §6.15): the boundary lies in the closure of the component (Romagny–Wewers, ACV); the coefficients are transported (DW06 Thm 1.3); Schmid's nilpotent orbit theorem gives the limit; the 16 columns M_j·F_∞ of the limiting differential have a nonzero 16 × 16 minor (det = 6144(1 + ω) on W5), which survives at nearby interior points.
3. **Transfer.** Thm 7.1 needs (D) at one point of the component; Remark 5.3: (D) and the discriminant are paired on the same component (`HCG-THM-ANYCOMP`).

W6 and W7 carry (H0)–(H4) certificates only; their components are not linked to S_W5 (OPEN 2).

**What refutes (D) in the record.** Upper bounds only: the induced-period bound (`HCG-THM-INDUCED-PERIOD-BOUND`, adopted in `hcg-v0.4`); the factorization through Siegel space for representations defined over ℚ (R7 of `HCG-COR-D6-NONSPLIT-NOGO`); Lemma F; the dimension budget (§6.23). Nothing in the record computes the rank of the period map at an interior point directly.

## 3. The one statement that links the (D)-method to the class

`HCG-COR-BOUNDARY-WITT` (§6.23; CHECKED, two AIs; no novelty claimed; also Severn v1 §6 (D∂), "only in a split cell", and v2 Prop 8.5 / Rem 8.6): under the laminar premises, dim span{N_i} ≤ r² ≤ w_K(S)², where r = dim I and w_K is the Witt index; a nonsplit form of signature (4,4) has w_K ≤ 3, so the bound is 9 < 16.

**Reading (mine; the argument is in the cited row, the consequence is not stated there).** (H2) asks for a K-rational S-isotropic subspace of dimension n = 4 in an 8-dimensional space, i.e. a Lagrangian, which exists exactly when S is hyperbolic, i.e. split. So:

> **For a nonsplit datum, the only method in the record that proves (D) cannot be applied — in every dimension d, with or without the budget.**

This is a dimension-independent statement, but about a method, not about (D). It changes the form of P1. Every proof of (D) in the record passes through a maximally unipotent (Hodge–Tate) degeneration, and for nonsplit data no such degeneration exists. Whether a nonsplit datum can be dominant is therefore **untested by every method the two studies have**.

## 4. What follows for P1 `[PROPOSED unless marked]`

**4.1 A bound at every boundary point, without (D).** At any boundary point of the compactified Hurwitz family, the weight filtration of the limit is defined over K and W₀ is S-isotropic. So dim_K W₀ ≤ w_K(S), which is 4 for a split datum and at most 3 for a nonsplit one. Only the laminar case is in HCG's row; the general case is the standard statement that the rational boundary components of the period domain correspond to K-isotropic subspaces. I have not read a source for it.

**4.2 A combinatorial form `[PROPOSED; unchecked; one consistency check]`.** At a deepest boundary point (a trivalent tree of P¹'s), W₀ is the σ-part of H¹ of the dual graph of the admissible cover, so

  dim_K W₀ = Σ_{internal edges e} dim V^{⟨g_e⟩} − Σ_{vertices v} dim V^{H_v},

with g_e the boundary product of the edge and H_v the subgroup generated by the three elements at v. Check on W5 (all boundary products 1; ten pair vertices with H_v = ⟨s⟩, eight vertices with H_v = 1): 17·6 − (10·5 + 8·6) = 4 = n, Hodge–Tate, as recorded.

*Consequence, if right:* a nonsplit datum has dim W₀ ≤ 3 for every marking in its braid orbit and every trivalent tree. This is a computable necessary condition for nonsplitness that uses neither (D) nor the budget.

**4.3 Where a nonsplit (D) could still come from `[HEUR]`.** Near a boundary point with dim W₀ = k, the tangent space of the period domain splits along the parabolic of W₀ into k² (the nilpotent directions, Herm_k) + 2k(4 − k) (extension directions) + (4 − k)² (the period domain of Gr^W₁). For k = 3 that is 9 + 6 + 1.
- A nonsplit dominant datum would need the Witt bound to be attained (nilpotent span 9).
- The other 7 directions would have to come from variation along the boundary stratum. A 0-dimensional stratum (a deepest point) supplies none of them at the limit.
- So a certificate would have to sit on a boundary stratum of dimension ≥ 7, where Gr^W₁ is a family over a compact Shimura curve (signature (1,1), anisotropic). The record contains no method for this.

**4.4 No link yet to the positive-defect results.** The parity at a positive-defect prime is a Chevalley–Weil count of branch points (register B.7, two blocks). dim W₀ in 4.2 is a count of fixed spaces of boundary products. Both are computed from the same braid-orbit data, but no statement in either study relates them. `[OPEN]`

## 5. HCG re-pin: consumer diff from `hcg-v0.2` to `hcg-v0.5`

| HHO use | Where in HHO | State at `hcg-v0.2` | State at `hcg-v0.5` | Effect of a re-pin |
|---|---|---|---|---|
| Locality, [det ϑS] = [(−1)ⁿΠa_jb_j] | G4; the eight register rows whose grade contains `[THM-cond: locality]` (HHO-COR-G4B, HHO-LEM-G4C, HHO-THM-RANK-ONE, HHO-THM-C6-PARITY, HHO-THM-C3S3, HHO-LEM-TAME, HHO-LEM-LOCAL-LENGTH, HHO-THM-F20) | pending (Δ27) | `HCG-THM-PARABOLIC-DISC-LOCALITY`, `[THM]`, CHECKED (two AIs), since `hcg-v0.4`; its cup reading (L2) is an import; L3 is not part of it | Grades unchanged (no upgrade by citation, charter §5.1). The condition becomes an adopted HCG result. L2 is now also covered independently by HHO-LEM-B1-O2. |
| Induced-period bound | G5 | pending | `HCG-THM-INDUCED-PERIOD-BOUND`, `[THM]`, CHECKED, since `hcg-v0.4` | Wording "pending" → adopted. |
| d = 6 | dimension table | pending (Δ27 add. 1–2) | `HCG-COR-D6-NONSPLIT-NOGO`, CHECKED, `hcg-v0.5` | Wording. |
| d = 7, 8, 9, 11 excluded | dimension table | pending (Δ27 add. 4) | `HCG-LEM-NONSPLIT8-NORMAL-REFL`, CHECKED, `hcg-v0.5`: "no datum at all for d = 7, 8, 9, 11, **and none for d = 10**" | **Content:** add d = 10 to the HHO table. |
| Theorem R | G6 | pending | `HCG-THM-REFLECTION-DICHOTOMY`, CHECKED, `hcg-v0.5` | Wording; new label. |
| d ≤ 14 | dimension table | pending (Δ27 add. 5) | `HCG-COR-NONSPLIT8-D14`, CHECKED, `hcg-v0.5` | Wording; new label. |
| Lemma E, Lemma F | P1 note | pending | `HCG-LEM-INDUCING-DATUM`, `HCG-LEM-SYMMETRIC-TYPE-PERIOD-BOUND`, CHECKED, `hcg-v0.5` | Labels only (session record). |
| R1: nonsplit ⇒ d ≥ 53 | HHO-THM-R1 | pending (Δ27 add. 17) | **still pending**: `hcg-v0.5` excludes "15 ≤ d ≤ 24 and every bound from d ≥ 25 to d ≥ 53"; HCG's OPEN 11 (`HCG-OPEN-NONSPLIT8`) is "nonsplit data under (H) for d ≥ 15" | None. |
| Cyclic separators, C₃ control | calibration table | pending (Δ27 main entry) | still pending | None. |
| Opening note, HHO track (Δ28) | Part A | pending | still not included | None. |
| W5: (D) on S_W5; class [1]; PO-6 for W5 | calibration table; G12 | adopted (ledger v0.2) | unchanged | None. |
| (H) | gates §1 | opening note §2 (pending) | restated in ledger §6.25: genus-0 base; character field exactly K; no fixed vector; dim_K M_σ = 8 of signature (4,4); (D). The budget is derived; "only effective points count". Finiteness, absolute irreducibility and h₀ are in the definition of a datum. | The two lists agree item by item as I read them. **The (H) used by HHO's register rows becomes an adopted HCG text.** |
| Source dictionary | charter notation | `7d2736ef…f4419` | same hash | None. |

**Summary.** A re-pin to `hcg-v0.5` changes one content item (d = 10), several labels and the word "pending" in seven places. It changes no HHO grade and no HHO result, because HHO results that use HCG material are already graded conditionally. R1 and the HHO track stay pending.

**Overlap to note (HHO-SG-9).** HCG's OPEN 11 and HHO's P1 now ask about the same objects. HCG's route is dimension by dimension (d ≥ 15); HHO's target is a dimension-independent obstruction. §3 of this note bears on both.

## 6. Proposed next steps (at most two; the PI decides)

**Step 1 — the Witt boundary gate, on recorded data (`[ALG]`, short, here).**
- Check the formula of 4.2 against a second split datum (W6 or W7), then evaluate max over trees of dim W₀ on the recorded nonsplit witnesses: the C₆ separator, G(6,1,6) P1–P3 and C₃ × F₂₀. **Prediction:** ≤ 3 in every case, 4 for W5.
- A value of 4 on a nonsplit witness would show that the formula, or locality, or B1, is wrong somewhere. That makes it a sharp cross-check.
- If the prediction holds, record the gate (nonsplit ⇒ dim W₀ ≤ 3 at every boundary point) with its conditions. It is a necessary condition for nonsplitness that the record does not have in this form.

**Step 2 — re-pin to `hcg-v0.5` in the next HHO edition, with the diff of §5.** The work is mostly wording. Its one content change is d = 10.

Not proposed: a direct attack on "(D) ⇒ split". By §3 and §4.3 it needs a method to certify (D) away from Hodge–Tate boundaries, which neither study has.
