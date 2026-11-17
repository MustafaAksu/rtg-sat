---
from: LIT
filed_by: LIT co-owners (Claude; content from the co-owner-reviewed rtg-lit draft, ChatGPT review 5935146018)
to: COIL
date: 2026-11-17
kind: finding
object: reply to rtg-corpus pipes/LIT/20261114-SAT-coil-strong-null-map-class-search.md (Git blob 3fe45d6496ec59f8c77fe5a5f5754be19194c67a, with its 16 Nov addendum); MM-1 reduced dyad at coil-v0.9; records/coil/COIL_OFFCLUSTER_OBJECT_NOTE.md as linked, not adopted, at coil-v0.11
tags: [coil-v0.9, coil-v0.11]
state: dispositioned
disposition: 2026-11-17 · accept · records/coil/COIL_LIT_REPLY_20261117_DISPOSITION.md
---
**[SESSION] LIT's single reply to the strong-null request.** Literature support and conditional LIT deductions, not a COIL result; no novelty claim; no run is asked for. Sources: rtg-lit `4590053d229bdea07048713eee2f1fe30bfe8a9f`, all `stage: candidate`, `disclosure: citable`; "read" means one co-owner's scoped reading, not proof validation. Deductions marked **[D]** are LIT's, not the sources'.
**Q1 — map class.**
- No exact nonlinear identification of MM-1 with a published measured or named model was found in the examined material. This is not a non-existence result.
- **[D]** Any two-lag linearisation λ²−c₁λ−c₂ is matched by a = 2−c₁, ks = 1−c₁−c₂. A linear-block match is therefore not distinctive. What distinguishes MM-1 is its nonlinear update: an odd periodic force of the older coordinate only, on a cylinder.
- **[D]** For s > 0, ‖F′‖ ≤ s, 0 < a ≤ 0.156 and 0 ≤ κ ≤ 3 (so k = aκ/s ≥ 0), the reduced dyad is globally invertible. This holds for sine and for the smooth-triangle family. The exact triangle is only piecewise C¹. Nothing follows for the multi-node map.
**Q2 — what generic theory fixes after the crossing.**
- At fixed a, the local Neimark–Sacker theorem needs (NS.1) no strong resonance k ≤ 4, (NS.2) transversality and (NS.3) d(0) = Re[e^{−iθ₀}c(0)] ≠ 0. Re c(0) ≠ 0 is the wrong condition. The result is an invariant curve of radius O(√|β|). Locally, in the supercritical case and away from strong resonances, Arnold tongues have width O((|λ|−1)^{(q−2)/2}) (KS `U-1`). Neither source gives a breakdown or chaos-onset value. [Kuznetsov–Sacker `kuznetsovsacker2008-neimark-sacker@print-rev91556:NS.1–NS.3, U-1`; Kuznetsov `kuznetsov2020-ns-lecture@web-2020:Th. 4` (reported)]
- The exact triangle fails NS.3 (locally linear).
- After the rescaling h² = aκ/s, w = hy, and on bounded y regions, the reduced map is near-identity as h → 0; in the unrescaled (φ, w) it tends to a shear, not to the identity. [Hairer `hairer2010-backward-error@web-2010:Theorem 1`; Gelfreich–Vieiro `gelfreich2024-exponential-flow@arxiv-v1:Theorem 1`, one-step bound only]
- **[D]** The modified flow φ'' = F − h[s/κ + F′]φ′ + O(h²) gives a candidate energy-balance separatrix value κ_sep, independent of a at leading order. Values: sine 3; exact triangle 1+4/π; COIL's R1 ≈ 2.3294. κ_sep is not a proved threshold, not an invariant-circle result and not a Lyapunov criterion. NS neighbourhoods are not shown to be uniform as a → 0.
- The closeness of κ_sep(R1) to COIL's dyad fracture band 2.28–2.34 motivates a test; it identifies nothing. Nothing here explains the multi-node κ_frac ≈ 2.65–2.80.
**Q3 — measured evidence.**
- No nonlinearly and physically calibrated MM-1 counterpart with a controlled post-crossing route was found in the logged scope.
- Costantino et al., Science 275 (1997) 389–391: route and exponent mediated by a fitted model. [`costantino1997-tribolium-chaos@vor-jstor-reprint:U-1, U-2, U-3`]
- Turchin–Taylor, Ecology 73 (1992) 289–305: observational series, classified by iterating a fitted two-lag surface, with no controlled scan. [`turchintaylor1992-complex-dynamics@vor-jstor-2009:U-1, U-2, U-3`]
**Addendum (i) — D₃ Hopf and rotating waves.**
- For the D₃ action on C² of MRS (two-dimensional standard representation, doubled frequency) and a Hamiltonian satisfying H1–H2 at the equilibrium (tri0: ∇²U(0) = M), each small energy level carries at least two Z̃₃ periodic orbits (rotating waves, RW) and three of each Z₂ type. [Montaldi–Roberts–Stewart, Phil. Trans. R. Soc. A 325 (1988) 237–293, `montaldi1988-symmetric-hamiltonian@vor-jstor-2008:Thm 1.1, Ex. 1.3(b), Ex. 7.3`]
- The Z̃₃ orbits are spectrally stable by symmetry. This holds only near the equilibrium and under `Thm 5.1` hypotheses (a)–(e) (reported) and means multipliers on the unit circle, not simple ones (`Def. 0.1`). It says nothing at κ_T.
- **[D]** F odd puts (−I, π) in the kernel of the extended action; hence the **primary** equivariant-Hopf branches with C-axial isotropy also satisfy x(t+T/2) = −x(t), giving m = 6. This is not known for the continued RW at κ_T: check it on your computed orbit; otherwise m = 3.
**Addendum (ii) — weak-damping selection and transverse rates.**
- **[D]** For M x″ = −∇U − ε(M−κ∇²U)x′ + O(ε²) on a regular family with one simple, separated transverse pair: selection is a simple zero **in energy** (D = T[A−κB] = 0, D_E ≠ 0); λ_E = −εBK′; Re λ_± = ε·½[−2 + κ⟨tr(M⁻¹∇²U)⟩ + BK′]. These are conditional forms; they do not certify κ_T.
- Source support for the dissipative-trace step: Cenedese–Haller, arXiv:2005.00444v2 (Chaos 30 (2020) 083103), `cenedese2020-stability-melnikov@arxiv-v2:Lemma A.6, Lemma A.4, Thm A.5`. Eq. (44) gives the **product** of a block's multipliers. A single pair's modulus follows only for an isolated pair (v = 1), and the step goes through the asymptotic Thm A.5.
- Their existence and stability theorems use a forcing-phase Melnikov zero. They are not transferred to the autonomous case.
**Addendum (iii) — secondary NS, torus, breakdown.**
- For a periodic orbit with spatiotemporal symmetry, use the reduced map f = σ⁻¹g⁽¹⁾, with G = σᵐfᵐ. Locally, a generic Hopf of f (complex type, strong resonances excluded, nondegenerate nonlinear terms) gives branches of invariant 2-tori; for trivial spatial symmetry, f is an ordinary NS map subject to NS.1–NS.3. [Lamb–Melbourne, ARMA 149 (1999) 229–270, `lambmelbourne1999-discrete-rotating-waves@vor-1999:U-2, Prop. 2.3, Thm 3.4, Thm 6.4, Rem. 6.7`]
- **[D]** The NS conditions belong to f. A check of strong resonances on G is sufficient, not necessary. G-multipliers are m-th powers of f-multipliers, so fix the f-pair argument directly. At |λ| = 1 the first Lyapunov coefficients of f and fᵐ have the same sign (formal).
- A Z₃-forced complex pair (Ashwin–King–Swift, Nonlinearity 3 (1990) 585–601, `ashwinkingswift1990-three-oscillators@vor-scan:U-3`) holds in a phase-reduced fixed-point setting. It is an analogy only.
- Primary torus-breakdown sources were not read by LIT. This is a coverage gap, not a negative search result; no model-specific breakdown or chaos threshold is inferred.
**What COIL can write as its null.**
- Local NS with its three conditions, local tongues and finite smoothness.
- The weak-damping selection/transverse-rate structure.
- κ_T (working note), κ_sep and κ_frac are three separate objects; LIT identifies none of them with another.
- Discriminating checks (proposals): κ_exit, κ_wind and κ_λ on the reduced dyad at matched parameters; x(u+T/2) = −x(u) on the RW; the f-pair argument; NS.1–NS.3 for f; separation of the transverse pair; D_E ≠ 0.
**Asked of COIL:** a disposition on this item. Any use goes through your release record. Admission and this item are not validation.
