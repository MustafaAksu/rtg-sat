# HCG — audit of the RTG imports (ledger v0.2 §7)

**Date:** 10 November 2026. **By:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Decision:** PI.

**Status:** owner-review record, PROPOSAL, **revision 2** (after the ChatGPT co-owner review of PR #29; §6). `hcg-v0.2` is unchanged, and `REGISTRY.md` still says `not set` for HCG's RTG inputs.

**Question.** For each RTG statement that the HCG ledger imports: at which adopted `rtg-corpus` tag does it stand, in which section, under which RID, with which grade and scope, and is it the same statement in the current RTG edition?

**Method.** `evidence/hcg/verification/rtg_import_audit.py` reads the owner files at the historical tag and at the latest tag of each stream. For each import it finds the defining entry, the section it sits in and its leading grade tag, and compares the entry text between the two tags. Output: `rtg_import_audit_out.txt`. Besides the script, the surrounding blocks were read by hand where the notes below say so.

**What the automatic check covers, and what it does not.**
- It compares **one selected defining line per import** between two tags.
- It does not check proofs, the entries a line depends on, or the rest of a block. Those were read by hand only where §3 says so.
- It does not cover the OFN reference of R8, which names no statement.
- No RTG proof or certificate was re-run or re-read.

The audit is therefore about identity, location, grade and scope of the selected statements, and nothing more.

## 1. Tags read

| Stream | Historical tag (commit) | File SHA-256 | Latest tag (commit) | File SHA-256 |
|---|---|---|---|---|
| DYAD | `dyad-v6.4.19` (`2890769b…`) | `40c9e63f14ba…` | `dyad-v6.4.23` (`ab8749b2…`) | `9f874ccc1cd6…` |
| GENESIS | `gen-v2.8.9` (`d7d661c0…`) | `d143673e9596…` | `gen-v2.10` (`12bb2b39…`) | `63c3b020d9c6…` |
| Programme | `programme-v1.2` (`d7d661c0…`) | `4207da05dca2…` | `programme-v1.4` (`514e17f3…`) | `37d857d08bb4…` |
| OFN | `ofn-v0.10` (`d7d661c0…`) | not read | `ofn-v0.12` (`2b2573f5…`) | not read |

- The two latest DYAD and GENESIS file hashes and the Programme v1.4 hash equal the values in `rtg-corpus` `BASELINE.md` on `main`.
- **DYAD v6.4.18 has no tag.** The ledger cites it for R1, R2, R4 and R5. The v6.4.19 file states in its own change record (line 1171): "Unchanged: all adopted RIDs and grades of v6.4.18 (including DYAD-THM-SMOOTH-EMBEDDING …)". That is a source report, not a check of v6.4.18.

## 2. Result by import

"Same" means the defining entry text is identical at the historical and the latest tag (RID markup ignored).

| Import | Ledger citation | Found at the historical tag | Grade and scope at the source | Same in the latest tag | HCG's use |
|---|---|---|---|---|---|
| R1: A = [[1,−1],[1,0]] | DYAD v6.4.18 §§6.1–6.3; GENESIS v2.8.9 §1 | DYAD §6.3, in the entry `DYAD-ALG-Q-INVARIANT-FORM` ("A = DT(P₁) elliptic of order 6"); GENESIS **§6.1**, "Linearization: DT(0,0) = A" | `[ALG]` in both | yes | recomputed exactly by HCG (H1-01…04) |
| R1: A³ = −I, A⁶ = I | GENESIS v2.8.9 §1 | GENESIS **§1**, line 32, `GEN-THM-LIN-ORDER6`; repeated in §6.1 | `[THM]` | yes | recomputed exactly by HCG |
| R2: B, AᵀBA = B | DYAD §§6.1–6.3, `DYAD-ALG-Q-INVARIANT-FORM` | DYAD §6.3, line 471 | `[ALG]`; B spans the one-dimensional space of A-invariant forms | yes | recomputed exactly |
| R3: J_Q = (2A − I)/√3 | GENESIS v2.8.9 §6.6; RID unavailable | GENESIS §6.6, line 975: J_Q = (1/√3)[[1,−2],[2,−1]], J_Q² = −I | section tag `[ALG / mixed]`; GENESIS lists "Corrected J_Q … `[ALG]` (§6.6)". No RID exists; the only J_Q RID is `GEN-FAIL-OLD-JQ` for the rejected older form | yes | complex structure; the matrix equals (2A − I)/√3 |
| R4: μ, a₀₅ | DYAD v6.4.18 §§6.7, 6.14; `DYAD-THM-C21`, `DYAD-ALG-NF6` | c₂₁: §6.2, line 452 (`DYAD-THM-C21`). μ = −½ − iτ: §6.7, line 563. μ = 6λ̄n₂₁ and a₀₅ = 6λ̄n₀₅ with their values: **§6.9**, line 610. The RID entry of NF6 is in §6.14 | c₂₁ `[THM]`; the chart values `[ALG]`, "through degree 6", chart-specific | yes | cross-check only; HCG recomputed both in its own chart with exact match (`HCG-ALG-NF`) |
| R5: smooth flow embedding of T⁶ | DYAD v6.4.18 §6.17; `DYAD-THM-SMOOTH-EMBEDDING` | §6.17, line 1000 | `[THM]`, scope: C^∞ local germs at P₁; not analytic (B-an and B-6 stay OPEN in DYAD) | yes | context only; not load-bearing |
| R6(a): the origin is a local attractor of T⁶ | DYAD v6.4.19 §6.14; `DYAD-THM-PRIM-CTR` | §6.14, line 757 | `[THM]`, proof by analytic majorant and exact-rational certificate. **Two radii:** the contraction Q(T⁶x) < Q(x) of the primitive Q holds on 0 < Q ≤ 1/400; the six-phase invariant tube is built from the smaller start set U = {0 < Q ≤ 1/625}. Optimal radii not claimed | yes (see note N2) | **premise of `HCG-THM-R6B`** — the one load-bearing RTG import |
| R8: programme boundary | Programme v1.2; OFN v0.10; "RTG SG-PROG-1" | Programme §8, line 484 | a scope guard, not a graded claim | yes | governs HCG's SG-2; interpretation only |

**Summary.** All imported statements were found. Every one of them stands with the same text, grade and scope in the latest adopted RTG editions. No imported value changed.

## 3. Notes

- **N1. Two incomplete locations in the v0.2 ledger.** Neither is a content error.
  - **Genesis.** The ledger cites "GENESIS v2.8.9 §1" for R1. That is right for A³ = −I and A⁶ = I (`GEN-THM-LIN-ORDER6`, `[THM]`, §1). The matrix A itself is stated in §6.1 (`[ALG]`). Revision 1 of this record called the §1 citation a slip; that was wrong (R1 of the co-owner review). v0.3 should cite both places with their own grades.
  - The line that gives μ and a₀₅ with their values is in DYAD §6.9. §6.14 holds the RID entry of `DYAD-ALG-NF6` and uses a₀₅, so the ledger's "§§6.7, 6.14" is incomplete rather than wrong.
- **N2. Changes near the imports in later DYAD editions that do not touch what HCG uses.**
  - v6.4.23 adds a `[COR]` in the `DYAD-THM-PRIM-CTR` block: two displayed certificate values in a table were nearest-rounded and are now shown rounded up. The theorem entry and its constants are unchanged. HCG uses only the qualitative conclusion.
  - v6.4.21 corrects the coefficient field of the **archival** Lie-gauge object h₄ (ℚ(√3) → ℚ(i√3)). That object is not imported by HCG; the chart values of R4 are unchanged.
- **N3. OFN is not an import as written.** The ledger names "OFN v0.10" beside the Programme for R8 but gives no OFN section, RID or statement. Nothing can be audited there. Proposal for v0.3: drop OFN from the row, or name the exact OFN statement.
- **N4. What the ledger already said.** Its synchronization note records that the pins "are kept as historical citations, not repinned" and that the Genesis pins and `DYAD-ALG-Q-INVARIANT-FORM` "were not re-searched". This audit does that search.
- **N5. Independence.** R1, R2 and R4 do not rest on RTG's authority: HCG recomputed them. R3 is a one-line matrix identity given R1. R5 and R8 carry no proof weight. Only R6(a) is taken on RTG's grade.

## 4. Proposals for `hcg-v0.3`

1. **§7 of the ledger:** give every RTG import as tag, section, RID (or "none"), source grade and scope, with the two location corrections of N1.
2. **Pins:** record the imports at the latest tags read here: `dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4`. No OFN pin. Keep the v6.4.18/19, v2.8.9 and v1.2 citations as provenance. The co-owner review supports the latest tags; the choice is the PI's. After v0.3, the pins do not move forward on their own: a later RTG edition is consumed only by a new HCG decision.
3. **R6(a):** state its scope with the import, keeping the two radii apart (contraction on 0 < Q ≤ 1/400; invariant tube from Q ≤ 1/625; fixed T on the dyadic carrier), since it is the one premise HCG takes on RTG's grade.
4. **OFN:** it stays out of the active import list until a specific OFN statement is named (N3).
5. **`REGISTRY.md`:** set HCG's "RTG inputs (pinned tags)" only in the `hcg-v0.3` release, after review of this record.

## 5. Limits

- The comparison is textual. An unchanged entry can still depend on other entries that changed; apart from N2, that was not traced.
- The RTG registry rows of v6.4.23 (RID, grade, section, evidence) were read for the five DYAD RIDs and agree with the table.
- RTG moves on. The audit is valid for the tags named in §1.

## 6. Revision history

| Revision | Commit | What changed |
|---|---|---|
| 1 | `063127894bf28066fa3ade9245b4b93e9d2d5315` | first version |
| 2 | this commit | The two corrections of the ChatGPT co-owner review `5844669492` (ACCEPT WITH CHANGE). |

**The corrections of revision 2:**
- **R1.** The Genesis §1 citation is not a slip: §1 holds A³ = −I and A⁶ = I (`GEN-THM-LIN-ORDER6`, `[THM]`). The table now has a separate row for it, and the script compares that entry too.
- **R2.** The scope of the automatic check is stated in the method and in the script: one selected line per import; no proofs, no dependencies, no OFN.

Also entered from the review: the two radii of `DYAD-THM-PRIM-CTR` are kept apart; no OFN pin; pins do not advance without a new HCG decision. The reviewer independently confirmed the three tags, their release records and the defining paragraphs.
