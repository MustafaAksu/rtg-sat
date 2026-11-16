# HHO — (D) source reading: how dominance is established, what it says about the class, and the HCG re-pin diff (Claude)

**Date:** 16 Nov 2026. **Level:** `[SESSION]` reading note, Claude HHO owner session. PI decision of 16 Nov 2026: "(D) kaynak okumasına başlayalım o zaman." **Status:** PROPOSED reading by one AI, **revised 16 Nov 2026** after the co-owner's review (ACCEPT AS A SESSION READING with three scoped corrections; change record §7). §4.2 now has two independent exact checks on three C₆ data (§4.5); no other computation was run. No register row, grade, release record or tag changes. HHO's governing edition is `hho-v0.4`, pinned to `hcg-v0.2`.
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

**4.2 A combinatorial form `[THM-cond: admissible-cover dual-graph description and its weight filtration]`.**

*Hypotheses, stated in full (correction (i)).* A connected G-cover of ℙ¹ degenerates, after a finite base change, to an admissible nodal cover over a stable trivalent tree of ℙ¹'s. Upstairs, the components over a base vertex v form one G-orbit with stabilizer H_v (generated by the three elements at v), and the nodes over an internal edge e form one orbit with stabilizer the inertia group ⟨g_e⟩, g_e the boundary product on one side of e. The family is semistable, so the weight-zero part of the limit of H¹ is the H¹ of the dual graph of the special fibre. The actions of G and of K on the family and on its limit are compatible.

*Formula.* The G-equivariant cochains of the dual graph give 0 → V^G → ⊕_v V^{H_v} → ⊕_e V^{⟨g_e⟩} → Hom_G(V, H¹(graph)) → 0, so

  dim_K W₀(σ) = Σ_{internal edges e} dim V^{⟨g_e⟩} − Σ_{vertices v} dim V^{H_v} + dim V^G.

For σ absolutely irreducible and nontrivial, V^G = 0 and the last term drops. Replacing V by its dual does not change any fixed-space dimension. The derivation of the exact sequence is ChatGPT's (`records/hho/HHO_D_WITT_GRAPH_REVIEW_CHATGPT.md` §2).

*What the formula is not.* It is not an unconditional statement about an abstract product-one tuple. It uses the geometric inputs above, which neither owner has checked against a primary source, and it does not construct the limit, prove (D) or show that a given tree occurs in a given component. Check on W5 (all boundary products 1; ten pair vertices with H_v = ⟨s⟩, eight vertices with H_v = 1): 17·6 − (10·5 + 8·6) = 4 = n, Hodge–Tate, as recorded.

*Consequence, under these hypotheses and 4.1:* a nonsplit datum has dim W₀ ≤ 3 for every marking in its braid orbit and every trivalent tree. This is a computable necessary condition for nonsplitness that uses neither (D) nor the budget. It is a **consistency gate** between the class and the boundary combinatorics, not an obstruction to (D).

**4.3 Where a nonsplit (D) could still come from `[HEUR]`.** Near a boundary point with dim W₀ = k, the tangent space of the period domain splits along the parabolic of W₀ into k² (the nilpotent directions, Herm_k) + 2k(4 − k) (extension directions) + (4 − k)² (the period domain of Gr^W₁). For k = 3 that is 9 + 6 + 1. The identity is algebra; by itself it says nothing about which directions smoothing parameters can produce.

- At a boundary point of a nonsplit datum the **limiting** nilpotent differential has rank at most 9.
- **This does not bound the rank at nearby interior points** (correction (ii)). The nilpotent-orbit expansion has holomorphic correction terms, so the interior differential can have rank 16 although its limit does not. HCG §6.15 uses one direction only: a nonzero limiting minor gives a nonzero nearby minor. The converse is false in general.
- My first version concluded that a nonsplit certificate "would have to sit on a boundary stratum of dimension ≥ 7". **That is withdrawn.** It is not a necessary condition and must not be used as a screen.
- What remains: a proof of (D) for nonsplit data needs a method other than a Hodge–Tate limit, and the record has none.

**4.5 First test of 4.2: three C₆ data, all trees `[NUM]`.** For the rank-one character χ₁ of C₆, dim V^{⟨g⟩} = 1 exactly when g = 1, and dim V^{H_v} = 1 exactly when all three elements at v are trivial. Over all 2 027 025 labelled trivalent trees on the ten branch points:

| C₆ tuple | Recorded parabolic-cup class | min dim W₀ | max dim W₀ |
|---|---|---|---|
| separator (2⁵, 3, 4³, 5) | [2] | 0 | **3** |
| (3⁸, 1, 5) | [1] | 0 | **4** |
| (3⁸, 2, 4) | [1] | 0 | **4** |

- Two independent implementations agree.
  - ChatGPT's dynamic programme over subsets, with a root-invariance check: `evidence/hho/d-witt/hho_d_witt_c6_tree_dp_chatgpt.py` (SHA-256 `1c0319bbdfdcc1bcf8c1b72b97676184792da5f348665c1e3655dda58e2b0f0b`), replayed here with byte-identical output.
  - An explicit enumeration of every tree by leaf insertion, each evaluated with the general Euler formula: `evidence/hho/d-witt/witt_graph_c6_bruteforce_claude.py` (`9fe007155162f010212c90a1833c123253484b1ee8802856f0415c50dbcce87f`); output `1a8fe30b6a667a6b8c506f1eaf7fe7372425d10325e32303cc22ad8958b8d8d2`; about 60 seconds.
- The result is what the Witt bound predicts: the nonsplit datum never reaches 4, and the two split data do.
- The classes are taken from the record and were not recomputed. For a cyclic group every ordering of the branch points lies in one braid orbit, so every tree occurs.
- It is a consistency check of locality, bridge B1 and 4.2 on three data. It is not a test of (D) and not a new obstruction.
- An observation, not a conjecture: on these three data, the maximum over trees of dim W₀ equals the Witt index of the recorded class.

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

**Summary (correction (iii)).** A re-pin to `hcg-v0.5` changes one scientific statement in HHO's tables: HCG also excludes every datum with d = 10. The other changes are changes of **authority and provenance**, not cosmetic: seven results that HHO cites as pending become adopted HCG results, with new RIDs, stated conditions and review states, and the (H) that HHO's rows assume becomes an adopted HCG text. They change no HHO grade and no HHO result, because HHO results that use HCG material are graded conditionally and gain nothing by citation (charter §5.1). R1 (d ≥ 53) stays HHO's statement from the opening note and pending in HCG; HCG's adopted statement is the weaker d ≤ 14. Neither is to be replaced by the other.

**Overlap to note (HHO-SG-9).** HCG's OPEN 11 and HHO's P1 now ask about the same objects. HCG's route is dimension by dimension (d ≥ 15); HHO's target is a dimension-independent obstruction. §3 of this note bears on both.

## 6. Proposed next steps (at most two; the PI decides)

**Step 1 — the Witt boundary gate, on recorded data (`[ALG]`, short, here).** The C₆ part is done (§4.5).
- Next: an independent graph count on the actual trees of W6 and W7 (split; prediction 4), and on a small, preregistered family of trees for G(6,1,6) P1–P3 and C₃ × F₂₀ (nonsplit; prediction ≤ 3). A search over all trees on twenty points is not proposed.
- A value of 4 on a nonsplit witness would show that the formula, or locality, or B1, is wrong somewhere. That makes it a sharp cross-check.
- If the prediction holds, record the gate (nonsplit ⇒ dim W₀ ≤ 3 at every boundary point) with its conditions. It is a necessary condition for nonsplitness that the record does not have in this form.

**Step 2 — re-pin to `hcg-v0.5` in the next HHO edition, with the diff of §5.** The work is mostly wording. Its one content change is d = 10.

Not proposed: a direct attack on "(D) ⇒ split". By §3 and §4.3 it needs a method to certify (D) away from Hodge–Tate boundaries, which neither study has.

## 7. Change record

First version: commit `cbd0fdf`, SHA-256 `445f6e0c178097e7aa74a1702eee9cce8da7e2b29e4a3e845df737e83753e391`. Reviewed by the ChatGPT session: PR #74, review `5918157362`, ACCEPT AS A SESSION READING with three scoped corrections. The review is recorded in `records/hho/HHO_D_WITT_GRAPH_REVIEW_CHATGPT.md` (SHA-256 `6b978fb0be1f4c543cd71245a10f1f8de0bb99178b28ef4c55c4b861a2d77b59`, received through PR #76). The PI relayed a differently worded copy of the same review (SHA-256 `7ca766d1a923c027a710a7294645d097bbec774952408d0555c200f88fd5ba0f`); the repository copy is the one cited.

| Item | Change |
|---|---|
| (i) | §4.2: the admissible-cover, semistability and K-compatibility hypotheses are stated; the term + dim V^G is written; the grade is conditional. |
| (ii) | §4.3: the "boundary stratum of dimension ≥ 7" requirement is withdrawn; a limiting rank does not bound the interior rank. |
| (iii) | §5: the re-pin changes authority and provenance as well as one statement (d = 10); R1 and HCG's d ≤ 14 are kept apart. |
| Test | §4.5: three C₆ data over all trees, by two implementations. §6 Step 1 updated. |
