# HHO — re-pin of HCG: consumer comparison `hcg-v0.2` → `hcg-v0.5` → `hcg-v0.6` (Claude)

**Date:** 16 Nov 2026. **Status:** `[SESSION]` preparation note for a draft `hho-v0.5` (PI instruction of 16 Nov 2026, 17:10 +03:00: "önerin uygun onaylıyorum"). It is not an adoption, and it changes no grade. Prepared by the Claude HHO owner session.

**Relation to the earlier note.** `records/hho/HHO_D_SOURCE_READING_CLAUDE.md` §5 compares `hcg-v0.2` with `hcg-v0.5` for the Δ27 material. This note:
- extends that comparison to `hcg-v0.6`;
- adds the items §5 did not list: the changes of `hcg-v0.3` (the third-family states and §6.23) and the use of `HCG-COR-BOUNDARY-WITT` by the Witt gate;
- checks every HCG file that HHO cites by hash at all three tags.

## 1. Which HCG edition

`REGISTRY.md` names `hcg-v0.6` as HCG's governing edition. It was adopted on 16 Nov 2026 at 09:36 +03:00 (notice `pipes/HHO/20261116-HCG-v0.6-release.md`).

The PI's instruction followed a proposal that named `hcg-v0.5`. That proposal was written without noticing `hcg-v0.6`.

| Tag | Tag object | Commit | Ledger SHA-256 |
|---|---|---|---|
| `hcg-v0.2` (current pin) | `7e8b02792da542c28809f362a6a97b6d357b9178` | `543d09387d6d5df79d38fcd549090350f994d4e3` | `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` |
| `hcg-v0.5` | `ec17e2da73e237ba9e9f719550b1f453c4beadc5` | `799081a6bf7f6149ff1b01e3e05e9d82efda0827` | `650c301f8465536705c852113fa7c2e2288d8c3e3cae99fa92a9c466e47bf383` |
| `hcg-v0.6` (governing) | `42a203ee6189d35f97b6097476b79a6d8b50c72e` | `34251e9b2ee110db34426b79fa0e26929d961563` | `b1e928f5ae555d688a18bb1046be7626796f2a07935b6ff81a0fc934036b14cb` |

**Recommendation: pin `hcg-v0.6`.**
- For everything HHO uses, `hcg-v0.5` and `hcg-v0.6` say the same (§4).
- Pinning the governing edition avoids citing a superseded one.
- Pinning `hcg-v0.5` would be equally correct for content. The draft can be switched by changing the tag name and the ledger hash only.

## 2. HCG files cited by HHO: byte identity at the three tags

Each file listed in `records/hho/HHO_SOURCE_MANIFEST.md` §3.1 was hashed with `git show <tag>:<path> | sha256sum`. One input of the Witt gate was added to the list.

| File | `hcg-v0.2` | `hcg-v0.5` | `hcg-v0.6` |
|---|---|---|---|
| `hcg/HCG_STUDY_LEDGER.md` | `276c93a3…` | `650c301f…` | `b1e928f5…` |
| `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md` | `7d2736ef…` | same | same |
| NOTE `hho-track/…OPENING_NOTE_v0_1.md` | `6a7a8053…` | same | same |
| `received/10041afe-…FRAMEWORK_SESSION_v0_1.md` | `aeb6f9e7…` | same | same |
| Δ27, Δ28: `ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` | `1f00a1eb…` | same | same |
| `received/68e831c3-…LOCALITY_PROOF_v0_1.md` | `0ec38558…` | same | same |
| `nonsplit8/H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md` | `41bc9997…` | same | same |
| `received/20505e68-…INDUCED_PERIOD_DIMENSION_BOUND_PROPOSED_v0_1.md` | `03199b80…` | same | same |
| `nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` | `050c8504…` | same | same |
| `nonsplit8/H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md` | `de619ee4…` | same | same |
| `h4sel/p2p3/generic_engine.py` | `66f2c253…` | same | same |
| `nonsplit8/cyclic_disc_claude.py` | `da76a25f…` | same | same |
| `g34/g34_cert_tuple5_balanced.json` (W5 certificate; Witt gate input) | `172766a9…` | same | same |
| `pipes/HHO/20261112-HCG-answer-severn-polarized-factor.md` (B2 input) | — | (as received) `8b376b6e…`, manifest §3.3 | unchanged by `hcg-v0.6` (notice of 16 Nov) |

Paths are under `evidence/hcg/` unless stated.

**Only the ledger changes.** Every other cited file is byte-identical. So the re-pin changes the citation of the ledger and of the states recorded in it, and nothing else.

## 3. Ledger items that HHO uses

States are as written in the ledger at each tag. "pending" means placed in `evidence/hcg/` and not in the adopted ledger.

| HHO use | Where in HHO | `hcg-v0.2` | `hcg-v0.6` (since) | Effect in HHO |
|---|---|---|---|---|
| Locality, `HCG-THM-PARABOLIC-DISC-LOCALITY` | G4; reading rule of the register; eight rows graded `[THM-cond: locality]` | pending (Δ27 add. 2) | §6.24 (a), `[THM]`, CHECKED (two AIs), since v0.4. L2 (cup reading) is a named import; L3 is not part of it | Wording and citation. **Grades unchanged** (charter §5.1). L2 is also covered by HHO-LEM-B1-O2. |
| Induced bound, `HCG-THM-INDUCED-PERIOD-BOUND` | G5; HHO-NEG-G616; reading rule | pending (Δ27 add. 4–6) | §6.24 (b), `[THM]`, CHECKED (two AIs), since v0.4; two coefficient profiles | Wording and citation. |
| d = 6, `HCG-COR-D6-NONSPLIT-NOGO` | gates, dimension table; register B.4, C | pending | §6.25 (b), `[THM]` with `[assuming:]`, CHECKED (two AIs), since v0.5 | Wording. |
| d = 7, 8, 9, 11, `HCG-LEM-NONSPLIT8-NORMAL-REFL` | gates, dimension table; register B.4 | pending (Δ27 add. 3–4) | §6.25 (d), CHECKED (two AIs), since v0.5: "no datum at all for d = 7, 8, 9, 11, **and none for d = 10**" | **Content: add d = 10.** It was already excluded in Δ27 add. 4 (ii), through the induced bound. HHO's table of `hho-v0.4` omitted it, and the D note §5 called it new in `hcg-v0.5`. It is new only as adopted text. |
| Theorem R, `HCG-THM-REFLECTION-DICHOTOMY`; d ≤ 14, `HCG-COR-NONSPLIT8-D14` | G6; dimension table | pending (Δ27 add. 4–5) | §6.25 (f), (g), CHECKED (two AIs), since v0.5 | Wording; new labels. |
| Lemma E, Lemma F | session records only | pending | `HCG-LEM-INDUCING-DATUM`, `HCG-LEM-SYMMETRIC-TYPE-PERIOD-BOUND`, since v0.5 | Labels only. No register row cites them. |
| (H) | gates §1; charter | NOTE §2 (pending) | §6.25 standing hypotheses, since v0.5 | The (H) of the register rows becomes an adopted HCG text. As read in the D note §5, the two lists agree item by item. HHO-OPEN-RECONCILE stays open: it also asks for the two d = 7 proofs. |
| Budget, `HCG-ALG-DIM-BUDGET` | register B.4, row 1 | not in the ledger | §6.23, `[ALG]`, CHECKED (two AIs), since v0.3 | The B.4 row can name the adopted label. |
| **Boundary Witt bound, `HCG-COR-BOUNDARY-WITT`** | the Witt gate (new) | not in the ledger | §6.23, `[ALG]`, CHECKED (two AIs), since v0.3. Laminar premises only; Landherr gives w_K(S) ≤ 3 for a nonsplit (4,4) form | **Needed by the new rows.** It covers only the laminar case. The gate's general form (D note §4.1–4.2) rests on inputs outside this row; see §5. |
| PO-4, (L) by Brauer induction, `HCG-THM-PO4` | G11; HHO-NEG-LSEP | CHECKED (two AIs) | THIRD-FAMILY CHECKED as a theorem-level argument on the v1 text, since v0.3 | Review state of an HCG input. No HHO grade changes. |
| PO-6, `HCG-EXT-PO6` | register B.5 (provenance of the B1 statement); G12 | PROPOSED for the general statement | CHECKED (two AIs) for the general statement, as a proof-path review, through v2 Lemma 7.2, since v0.3 | The B.5 sentence that names `HCG-EXT-PO6` stays true. No HHO grade changes. Bridge B2 is untouched: `hcg-v0.6` §6.26 says it adds nothing on PO-6. |
| W5: `HCG-ALG-E02` §6.14; (D) on S_W5 §6.15; class [1] | calibration table; Witt gate | adopted, CHECKED | W5 sub-claim THIRD-FAMILY CHECKED, since v0.3; §6.15 byte-identical | Calibration row may say so. |
| d ≥ 53 (HHO-THM-R1); 15 ≤ d ≤ 24 | Part A; gates | pending (Δ27 add. 5 (ii)–17) | **still pending**; OPEN 11 (`HCG-OPEN-NONSPLIT8`): nonsplit data under (H) for d ≥ 15 | None. R1 stays HHO's statement from NOTE, pending in HCG. |
| C₆ separator, C₃ control | calibration table | pending (Δ27 main entry) | still pending | None. The two RIDs are not in any adopted ledger. |
| NOTE, Δ28 | Part A | pending | still pending | None. |

## 4. What `hcg-v0.6` adds, and why none of it reaches HHO

`hcg-v0.6` adds the following:
- **§6.26:** line reviews of Severn v2 Lemma 6.1, Thm 6.2 with Cor. 4.7, Lemma 2.2, Lemma 10.1 / Prop. 10.2, Lemma 11.1 and Thm 11.2. The two new results are `HCG-THM-SEVERN-V2-L111` and `HCG-THM-SEVERN-V2-T112`.
- **OPEN items:** OPEN 8 and OPEN 10 are closed in their scopes; OPEN 12 is new.
- **Scope guard:** SG-14 is new.

None of these is cited by an HHO file. The ledger states the point itself: §6.26 adds "nothing about (L) and the supply of cycles (PO-2, PO-4), about (D) on S_W5 (PO-5), or about the discriminant and the polarization comparison (PO-6; HHO's bridge B2)". The notice of 16 Nov repeats this for the B2 input.

So for HHO's uses, `hcg-v0.5` and `hcg-v0.6` are equivalent.

## 5. The Witt gate and its HCG input

The new HHO rows need a statement of the form "nonsplit ⇒ dim_K W₀ ≤ 3 at every boundary point". HCG's adopted `HCG-COR-BOUNDARY-WITT` gives the bound w_K(S) ≤ 3, through Landherr, together with isotropy, **only for simultaneous laminar degenerations**.

The gate needs the following inputs. None of them is in an adopted HCG text, and neither HHO owner has read a primary source for them:
- **(a)** at every boundary point of the compactified Hurwitz family, W₀ of the limit is defined over K and is S-isotropic;
- **(b)** the admissible-cover dual-graph description of W₀, with the formula of the D note §4.2.

The draft therefore grades the gate `[THM-cond]` with (a) and (b) named. It does not cite `HCG-COR-BOUNDARY-WITT` as covering it. That RID is cited only for the Landherr step.

## 6. One observation for HCG (not HHO's to decide)

`hcg-v0.5` and `hcg-v0.6` both keep a sentence in §6.23 from the v0.3 context: "Nothing is claimed for d ≥ 10 in this edition". Since v0.5, §6.25 claims d = 10 and d ≤ 14. The sentence reads as a stale current-state statement. It does not affect what HHO cites.

If the PI wishes, a short notice to `pipes/HCG/` can point to it. HCG decides.

## 7. Changes this note implies for the HHO texts

| File | Change |
|---|---|
| `hho/HHO_CLAIM_REGISTER.md` | reading rules (locality, induced bound: adopted at the pin, grades unchanged); NOTE and Δ27 cited at the new pin (byte-identical); B.4: d = 10 and HCG labels; calibration line: HCG states. A new section B.8 for the Witt gate is a separate change of content, recorded in the release record. |
| `hho/HHO_GATES.md` | sources line; G4, G5 and G11 source states; dimension table (d = 10; labels; R1 still pending); calibration W5 row |
| `hho/HHO_SUPPORT_RESULTS.md` | §5 header sentence on the pin |
| `hho/HHO_CHARTER.md` §5.1 | the edition named and what is adopted in it |
| `records/hho/HHO_SOURCE_MANIFEST.md` §3.1 | the pin, the ledger hash, and the HCG states of the rows; the W5 certificate added |
| `pipes/HHO/20261116-HCG-v0.6-release.md` | disposition at adoption |

No HHO grade or review state changes because of the re-pin.
