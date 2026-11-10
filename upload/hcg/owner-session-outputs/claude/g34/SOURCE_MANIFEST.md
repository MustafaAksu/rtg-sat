# SOURCE_MANIFEST — Hodge & Complex Geometry Session (charter §7 deliverable i)

**Date:** 21 October 2026 · **Maintainer:** Claude.
Primary sources were downloaded and hashed in this session and read in full text where stated. Artifact checksums are in `SHA256SUMS_SESSION.txt`.

## A. Primary mathematical sources (downloaded, SHA-256 of the PDF)

| Source | Where read | Used for | SHA-256 |
|---|---|---|---|
| Severn, *Weil classes on every abelian sixfold of Weil type for ℚ(√−3)*, hexagon:2610.00387v1 (draft v0.5, 16 Oct 2026) | full text | Thm 6.2; Lemma 4.1; Prop 4.2; Prop 5.2; Thm 3.1 | 7aa80a3b8b5914eb40da3bd36aa719a5cce1c379ee2fd299ab88b10a06ae761c |
| Severn, *A transfer theorem for Weil classes …*, hexagon:2610.00386v1 (draft v0.15) | §§1–3, 6–7 | supply; spreading; Thm 7.1 | d39fdb282e899b15e8e8f5d4aee004186001b64553f9e8c7092cc0dae3e7efb0 |
| Severn, ℚ(√−3), discriminant −2 (G₃₂), hexagon:2610.00246v2 | §1 (context, CONV-1) | split identification of Schoen's sixfolds | 7b81d2ac642a8e1ad647b16ca464960db21855c16554b15bac641514b2b304f7 |
| Hippeläinen, non-split sixfolds [−2], hexagon:2610.00371v1 | §1 and disclosure only (Claude recused) | CONV-1; provenance | fa33d20cb33b1fdd7df20bfbdf4c74c6ae6e139ef62bf37ecd2127a21909b9ac |
| Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality*, Sém. Congr. 13 (2006) (emis.de/ft/47210; arXiv:math/0411119) | §1.4–1.5, §2 | Thm 1.3 (monodromy), Thm 2.3 (signature), Thm 2.6 (cup form) | 68a9f46fd16753245511f3a67612eaeaf8ff5c135c8086029b7db9d702d4231a |
| Milne, *Lefschetz classes on abelian varieties*, Duke Math. J. 96 (1999) (jmilne.org 1999aP) | §§1, 3, Cor 4.5 | Thm 3.2; Lemma 3.1 (PO-2) | 28ae245e58748438b7070680cac83f8b2f695c43f1643b59cde21eb94077fe53 |
| Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio 65 (1988) (numdam) | intro, §2, Thm 2.0, Cor 3.1, Thm 3.2 | supplier lemma; ℚ(√−3) fourfolds | 3794a85d4671d0fe95113b972bcbe708588e2884d52b36910727a3c363ecdc73 |
| Koike, *Algebraicity of some Weil Hodge classes*, arXiv:math/0211304 (Canad. Math. Bull. 47, 2004) | §1–2 | Weil-type definitions; ℚ(i) sixfolds | b16de3871d59c4d3896b29700f8353479d9ccfce3ef784a1022e5b0c3ef2ff7f |
| OpenAI, *Weil classes and Hodge classes on abelian powers* (30 Sep 2026, github.com/openai/math) | abstract, §1 | scope (hyperbolic only); literature map | ef66240969f38c9a8c81c7d6821ba205b8a6055c0e0fcabea738c00d3623f56a |
| OpenAI, *The rational Hodge conjecture for CM abelian varieties* (30 Sep 2026) | abstract, §1 | scope of the CM claim | b8bdfb9767cc20f2748c8efe396068e9e540b3e675aa9726b1b0a53bbe35640c |

## B. Sources consulted through abstracts or secondary pages only (not hashed)

- Markman, arXiv:2502.03415 (v2) and ICM 2026, doi:10.1137/25M1803796 / arXiv:2509.23403v2; arXiv:2509.23079.
- Floccari–Fu, arXiv:2504.13607.
- van Geemen–Rapagnetta, arXiv:2607.18341.
- Mostaed, arXiv:2603.20268.
- Li, arXiv:2609.27916.
- Patel–Zhang, arXiv:2506.13729.
- Saller, Zenodo / github sallerk.
- Bhattacharjee, Zenodo 23272739.
- Schoen 1998 addendum (Compositio 114): abstract only.
- Voisin, guest essay on T. Tao's blog (12 Sep 2026).
- OpenAI withdrawal report (kucoin news); OpenAI math index (kisonecat).

**Not reachable:**
- Zenodo 23225483: HTTP 429.
- arXiv:2609.14169: PDF not machine-readable; Brosnan per Severn [3].
- github benzsevern/hodge-fleet: workspace proxy.

## C. Classical results used without fresh rereading (standard references)

Brauer induction (Serre, *Linear Representations*, §10.5); Landherr's classification of Hermitian forms; Cattani–Kaplan–Schmid (1986); Schmid (1973); Harris–Mumford (1982); Knudsen (1983); Lefschetz (1,1); Chevalley–Weil; Deligne's semisimplicity theorem.

## D. RTG imports (one-way; charter §1)

R1–R5 come from Dyadic v6.4.18/19 (owner); R6b and R7 are SESSION. All RTG-derived data are hard-coded with provenance in `h1_h2_exact_checks.py`; no RTG file is read by any session script.
