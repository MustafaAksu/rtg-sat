# HCG v0.2 DRAFT — independent change-focused QA

**Date:** 26 October 2026  
**Author:** ChatGPT (session reviewer)  
**Disposition:** **ACCEPT FOR REVISED DRAFT REVIEW; NOT ADOPTION-READY UNTIL R01–R03 ARE CORRECTED.** The independent scientific reading supports correction D-8. No HCG adopted text was changed.

## 1. Source and provenance manifest

| Input | Exact file/version | Reading scope | Identity |
|---|---|---|---|
| Governing HCG ledger | `HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` | Compared as build baseline; inspected relevant retained sections via the draft and builder; not re-refereed | SHA-256 `75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7` |
| Changes | `HCG_DSN_v0_2_PENDING_DELTAS.md` Δ1–Δ23 | SHA and structural provenance, targeted review, **not** independent full replay of every earlier scientific campaign | SHA-256 `8fb25dadfb4416136625d7b8d6eea9f20ea0d8234bdd32495f0ac12d069efd98` |
| Candidate | `HCG_HODGE_SESSION_DSN_v0_2_DRAFT.md` | 1,193 lines: headings and source/scientific-critical sections, §1, §2, §6.7–6.21, §8–§9, appendices; builder and full diff reviewed | SHA-256 `c15815efeefcdaafa97f3f98688661c27ff43263543fe1198b2c4eec8a33ab61` |
| Package | `HCG_V02_DRAFT_REPLAY_v0_1.zip` | All inventory entries; manifest checked; builder read and independently run in temporary directory; diff hunk comparison | SHA-256 `4e6890fff36091df5fd28a125d638b5d4dceb5c5c2e257e64554cb51f45c4b98` |
| Primary manuscript | Severn, `hexagon:2610.00387v1`, draft v0.5, 16 Oct 2026 | Targeted: §2.3, Thms 2.9/6.2, Lemma 2.10, Prop 5.2, Rem 6.3; PDF screenshots of pp. 4, 10–11, 13 | https://hexagonmath.org/pdf/2610.00387v1 |
| Companion | Severn, `hexagon:2610.00386v1`, draft v0.15, 16 Oct 2026 | Targeted: transfer theorem statement, definition and scope in introduction; not a full new independent audit of §6–§7 spreading argument | https://hexagonmath.org/pdf/2610.00386v1 |
| Methodology | `DSN_METHODOLOGY_v1_3.md` | Targeted: evidence-status and adoption axes; technical-ledger rules | Uploaded adopted version; repository tag/adoption provenance not independently re-fetched |

## 2. Reproduction and structure

**[SESSION — COMPUTATIONAL]** In an isolated temporary directory, running `make_v02.py` produced exactly the uploaded candidate (1,193 lines; byte-identical SHA). The adopted baseline and pending-deltas bytes remained unchanged. The diff's semantic hunk lines are identical to the supplied diff; the differing first two lines are path/time headers only.

- Manifest `SHA256SUMS.txt`: **23/24 entries PASS**. The only failure is `./SHA256SUMS.txt`: it has the SHA-256 of an empty file, `e3b0c442...`, while the manifest itself is nonempty. A manifest should not list its own digest. This is a **packaging reproducibility defect**, not a scientific counterexample.
- The artifact registry is reconstructed from the *frozen* `registry_hashes.tsv` because most session artifact paths are not present in the standalone replay bundle. Its hash references are reproducibly reproduced from the frozen file; the referenced source artifacts' bytes **were not independently verified** in this audit.

Full machine-readable results: `HCG_V02_DRAFT_QA_RESULTS_v0_1.json`.

## 3. Critical source correction D-8: independently VERIFIED

**[SOURCE: `hexagon:2610.00387v1`, §2.3, Thm 2.9, Prop 5.2, Thm 6.2, Rem 6.3]** The paper explicitly says that it does not use [17]. It proves / claims the conclusion for all split eightfold members in Thm 6.2(1), invoking transfer Thm 2.9 on a G34 datum with (L), (D) and discriminant `[1]`; Thm 6.2(2) invokes Prop 5.2 with `n=4, δ=1`. The transfer theorem states its conclusion with **for every polarized abelian 2n-fold** quantification. The proof of Prop 5.2 explicitly applies that claim to **the special member** `A × S` and explains that relative-Hilbert spreading and K-isogeny invariance are the intended mechanism.

Consequently **the outside-[17]-dependency allegation was false**; the manuscript does not use [17] to supply PO-1's eightfold premise. The draft's §6.20 correction and D-8 disposition are justified.

**Important limitation:** The phrase "for every member" is **verified as the source theorem's stated scope**. Whether the proof establishes it (particularly for the special product `A×S`) is not settled by repeating the theorem statement. That scientific issue lies in companion [386] §6–§7 and the pending blind auditor Priority B items 6–7. OPEN 8 should be described explicitly as **proof-validation**, not source-statement identification. No newly discovered independent outside premise replaces [17].

Thus the intended chain is conditionally: `(L)+(D)+d(S)=[1]` ⇒ `[386] Thm 7.1/[387] Thm 2.9` (all split eightfold members) ⇒ `[387] Prop 5.2` (sixfold every discriminant). No inference of `ESTABLISHED` is warranted.

## 4. Findings and proposed bounded corrections

**R01 — REPAIR (packaging, required).** `SHA256SUMS.txt` hashes itself with the empty-file digest. Remove that line (or make a separate externally recorded manifest hash); regenerate the ZIP manifest. Acceptance: `sha256sum -c SHA256SUMS.txt` returns all PASS in clean unpack, excluding the manifest itself. Keep historical package unchanged; issue an amended package.

**R02 — REPAIR (scientific scope/wording, required).** Draft §1.2 summarizes the mixed P2/P3 results as "every interval form of a paired tuple factors through the same τ" without the hypotheses. The precise result in §6.18.3 requires **distinct rank-one involution root lines and consecutive intervals**. This is crucial: the earlier repeated-root toy example is an exception to the overbroad phrasing. Add the hypothesis in §1.2, or say "for W5/NEW01 and the stated distinct-line paired class". Acceptance: both summary and owner claim have the same quantifiers.

**R03 — REPAIR (notation, required).** Draft §6.18 begins with `\widehat N_e=T_e^{ord C}-1=(ord C/(k m))N_e`, where `k` and `m` are Severn's separate return/semisimple orders. §6.18.3 then writes P3 with `k=ord C`, reusing `k` for a **different** exponent. Rename the boundary product order `q_e=ord(C_e)` or `d_e`; write `S(x,\widehat N_e y)=-q_e h(\Pi_{C_e}u_x(c_e),\Pi_{C_e}u_y(c_e))`, reserving `k_e,m_e` for Severn's convention. Acceptance: the NEW02 `[16,18]` case (`ord C=2`, `k_e=1`) is unambiguous.

**R04 — CLARIFY (source/open-problem typing).** §2 OPEN 8 and §6.20 should say the "every-member" **scope is explicit in the imported source**, whereas **the derivation of that scope** remains under blind Priority B audit. This avoids implying that the source only states a generic-member conclusion. Such a clarification should not reopen internal PO-1–PO-4 verification.

**R05 — CLARIFY (scientific label).** §2 closed-modules line `W6/W7 algebraic :: CLOSED` is susceptible to being read as "Weil classes are algebraic on W6/W7". Replace with `W6/W7 finite (H0)–(H4) algebraic witness checks :: CLOSED (internal only)`.

**R06 — CLARIFY (registry availability).** §8 adds source-artifact rows marked `AVAILABLE (Claude workspace)` while the package's replay falls back to `registry_hashes.tsv`. State explicitly that this replay verifies the *frozen registry*, not the actual bytes or availability of every referenced source artifact; the archived files remain recorded in the Δ lineage.

**R07 — EDITORIAL.** §1.1 `Retained from v0.1 (unchanged text and grades)` should read `Retained scientific conclusions and review grades from v0.1`; §1 was replaced as a whole, so summary text is not literally unchanged.

## 5. Review judgement, negative checks and remaining obligations

The draft does **not** conflate the `H/Σ` tuple connection with arbitrary polarized-family equivalence. §§6.16–6.19 correctly separate third-family checked (D), third-family checked W5 Jacobian-induced polarization/discriminant, the unverified conventions for Severn's own projector, and the remaining transfer theorem. It excludes W6/W7 from the certified braid component. W5 named links, exact 90-move chain and H4 finite programmes were checked against the recorded Δ claims and source descriptions; **the expensive original campaigns were not rerun**.

The source `[19, Lemma 6.2]` general Alexander–Whitney proof remains OPEN; DW06 supplies the W5-specific independent source only. Severn Thm 6.2 stays `CLAIMED`. The blind Priority B review remains separate.

**Verdict:** Revise R01–R03 together, preferably R04–R07 in the same editorial pass, then perform one byte-exact rebuild and a scoped diff check. **No new scientific computation or fresh review of PO-1–PO-4 is justified by this QA.** PI adoption/release is a separate decision after the revised candidate is available. This audit is an advisory review, not adoption.
