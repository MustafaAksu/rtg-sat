
### §6.19 Severn component connection `[ALG cert]` {#sec-severn-link}

> **[Guards SG-6, SG-11 apply]** An algebraic tuple chain. Its consequences for the polarized family are in §6.17.

**Source.** Zenodo 10.5281/zenodo.23422649 (Severn, v0.5; the deposit of hexagon:2610.00387v1). Record MD5 values matched; the deposited manifest `certificates/g34-d3/SHA256SUMS` verifies, 40 of 40 entries. `tuple_pairs_D3.json` (SHA-256 prefix 0021185d…) matches the prefix printed in the paper's Appendix A. The archive was treated as untrusted data; none of its code was executed.

**Braid convention.** σ_i: (g_i, g_{i+1}) ↦ (g_i g_{i+1} g_i⁻¹, g_i), words applied left to right ("convention A").

**The chain.** Each leg is verified at matrix level, 20/20 entries, by two independent implementations.

| Leg | From → to | Word | Pure? | RID | Record |
|---|---|---|---|---|---|
| 1 | Severn gate tuple (datum [[7,20]]; generates G₃₄, order 39,191,040) → Severn's deposited paired tuple | Severn's 90-move word (`T8BW/braid.txt`) | no; covered by Σ = S₂₀ | HCG-ALG-SEVERN-90MOVE | Δ23 |
| 2 | P·(Severn paired)·P⁻¹ → W5 paired tuple | 618 letters (25 pair moves) | yes | HCG-ALG-SEVERN-APPXA-W5-LINK | Δ22 |
| 3 | W5 → NEW01–04, BLOCK-01; and BLOCK-01 → ESCAPE | five words; composed ESCAPE word 1,748 letters | yes | HCG-ALG-G34-NAMED-PURE-BRAID-LINKS | Δ21 |

`[ALG cert]` [RID: HCG-ALG-SEVERN-COMPONENT-CHAIN] (new; collects Δ21–Δ23) [provenance: CHECKED — legs 1–2: Claude and ChatGPT, independent exact replays, corrupted-word controls rejected; leg 3: same deterministic rule implemented independently by both AIs, words identical element for element; the gate-tuple group order recomputed by Claude only]

Under the fixed K-linear intertwiner P (`severn_to_w5.json`; one-dimensional solution space, no Galois twist), the following lie in one component of H/Σ for the class datum (G₃₄, σ; 20·R), with Σ = S₂₀ (Severn Prop 4.2 Step 0): Severn's gate tuple, Severn's paired tuple, W5, NEW01, NEW02, NEW03, NEW04, BLOCK-01, ESCAPE.

Scope and premises:
- **Identification.** Other σ-compatible identifications differ by the linear normalizer of G₃₄ and act on all tuples at once; the rank question is invariant under them. No claim is made about outer automorphisms.
- **Not included.** W6 and W7; the global connectivity question (OPEN 2).
- **Not done.** Severn's 17-curve table and his (H0)–(H4) on his tree were not recomputed (OPEN 3); his certificates other than the tuples and the word were not used.
- **Kind of result.** An equality of Hurwitz components. Not a check of Severn's geometric chain, of his polarization conventions, or of Priority B (§6.17, SG-11).

**Correction (dated 25 Oct 2026, carried from Δ23).** Claude's report `H3_SEVERN_APPXA_TO_W5_LINK_CLAUDE_v0_1.md` states "all 42 files OK" for `g34-d3/SHA256SUMS`. The manifest has 40 entries, and all 40 verify. The report is left unchanged.
