# COIL — The separatrix energy-balance value κ_sep against the locked dyad waveform results — analytic working note (unlocked)

**Status:** `[SESSION]` retrospective analytic note of the COIL owner session, 17 Nov 2026. Proposed in the LIT reply of 17 Nov 2026 (`pipes/COIL/20261117-LIT-strong-null-literature-reply.md`, Q2: "motivates a test; it identifies nothing") and endorsed by the co-owner (17 Nov 2026) with scope and acceptance criteria: same normalisation, exact coefficients, locked data identities, positive and negative comparisons, an explicit error table against the pre-locked predictor; status *only a candidate conditional position mechanism*. **No dynamics iterated, no campaign, no preregistration, no live document changed.** Every comparison is a **postdiction** on data locked before κ_sep was computed; the coincidence threshold of §4 was chosen after the data were seen.

## 1. Result

For the reduced dyad (Pair A arithmetic, a = 0.03) the leading-order separatrix energy-balance value κ_sep — a number computed from the force waveform alone, with no fitted parameter — **lies on or within 0.01 of a locked fracture cell for 8 of the 12 distinct waveforms that have a locked fracture set on κ ∈ [0.5, 8]**, where chance placement would give about 1.1 (§4). It also falls inside the locked R1 dyad fracture band (2.28–2.34) and is within 0.035 of the four locked smooth-triangle holdout positions — no better than the pre-locked A(q)-based predictor (mean error 0.0173 against 0.0163). It **fails** for two waveforms (t = −0.060: κ_sep 2.58, only tongue at 7.77; ORTHO A3: κ_sep 2.66, first fracture 4.60), and it **says nothing about existence**: κ_sep exists for every waveform, including those with no fracture in the scanned domain (sine to κ = 3; ISOA t = 0.000, +0.008 to κ = 8; smooth triangle q = 0.835, 0.845 in their windows). Reading: where a dyad fracture tongue exists, it is often located at the separatrix energy balance; whether it exists is decided by something else.

## 2. The quantity `[DERIVED]`

Dyad φ⁺ = φ + w, w⁺ = (1 − a) w − aκ g(φ), g odd, 2π-periodic, single-well (g > 0 on (0, π)), normalised g′(0) = 1 (R1 by s = g′(0)). In τ = √a·n at fixed κ the leading-order modified flow is φ″ = −g(φ) − √a[1/κ − g′(φ)]φ′ (P-κ note §2; LIT Q2). κ_sep is the κ at which the damping does no net work on the separatrix of φ″ = −g:

κ_sep = ∫ p dφ / ∫ g′(φ) p dφ, p = √(2W), W(φ) = ∫_φ^π g; equivalently (co-owner, by parts) κ_sep = 2∫₀^π √W dφ / ∫₀^π g²/√W dφ.

Both forms are computed and agree to the printed digits. Checks: sine 3 (P-κ note); exact triangle 1 + 4/π (LIT) to 10⁻¹⁰; R1 2.3293950 (LIT). `[COR]` The owner session's earlier triangle value 2.273228 was a quadrature error of 1.2·10⁻⁵ at the kink (co-owner); with a breakpoint at π/2 the closed form is reproduced.

**What κ_sep is not:** a finite-a bifurcation threshold, a Lyapunov criterion, an invariant-circle result, or a statement about the three-node κ_frac (LIT Q2; co-owner).

## 3. Comparison (script `evidence/coil/code/ksep_waveform_comparison.py`, output `evidence/coil/outputs/ksep_waveform_comparison.txt`)

Locked sources (all in `evidence/coil/outputs/`): `MM1_waveform_holdout_summary.csv`, `MM1_waveform_birth_summary.csv`, `tongueset_results/ts_geometry_summary.csv`, `ortho_results/ortho_*.csv` (coefficients a₃, a₅, a₇ read from the files); RM-02 for the sine and R1 dyads. ISOA/TONGUESET coefficients from the locked prereg (a₃ = c/2 + t, a₅ = c/2 − t, c = (1 − A₀)/4).

| family | waveform | κ_sep | locked observation | agreement |
|---|---|---|---|---|
| RM-02 | sine | 3 | no fracture for κ ≤ 3 | — (scan ends at κ_sep) |
| RM-02 | R1 | 2.3294 | fracture band 2.28–2.34 | inside |
| holdout | q = 0.875 / 0.9125 / 0.9475 / 0.9675 | 2.5804 / 2.5211 / 2.4524 / 2.4034 | κ_near 2.5880 / 2.5356 / 2.4397 / 2.3691 | −0.008 / −0.015 / +0.013 / +0.034 |
| birth | q = 0.835, 0.845 | 2.6335, 2.6211 | ABSENT in window | κ_sep in the window, no tongue |
| birth | q = 0.850, 0.855, 0.875 | 2.6146, 2.6081, 2.5804 | PRESENT | — (window centres only) |
| ISOA | t = −0.300 / −0.220 / −0.140 | 3.0436 / 3.1244 / 2.8920 | first components 3.074 / 3.089 / 2.891 | 0.030 / 0.002 / 0.000 |
| ISOA | t = −0.060 | 2.5764 | only tongue at 7.77 | **fails** |
| ISOA | t = 0.000, +0.008 | 2.3452, 2.3158 | none in [0.5, 8] | no tongue |
| ORTHO | A2 / A4 / B1 / B2 / B3 / B4 | 3.307 / 2.444 / 3.048 / 3.052 / 2.745 / 2.573 | κ_sep on or within 0.008 of a fracture cell | hits |
| ORTHO | A1 | 3.316 | nearest cell 0.039 away (first fracture 2.26) | near miss |
| ORTHO | A3 | 2.662 | first fracture 4.60 | **fails** |

Holdout error table (the pre-locked predictor `kappa_pred` is the A(q)-based position prediction of the holdout prereg): mean |κ_sep − κ_near| 0.01727, mean |κ_pred − κ_near| 0.01625 (co-owner's figures reproduced). Inside the smooth-triangle family κ_sep is not better than the existing proxy. Across families it differs: the A-proxy is constant on the ISOA family (A fixed by design; ISOA's I3 result), whereas κ_sep moves with the waveform and lands on the first tongue for t = −0.220 and −0.140.

## 4. Chance

For each of the 12 distinct waveforms with a locked fracture-cell set (ISOA t = −0.300 … −0.060 from TONGUESET; ORTHO A1–A4, B1–B4; the ORTHO anchor is the same waveform as t = −0.140 and is counted once) the chance p of a point lying within 0.01 of the set was computed for a uniform point on [0.5, 8] and, stricter, on [2.2, 3.4] (the range of the κ_sep values). Observed: 8 hits. Expected under chance: 1.16 and 1.14. Poisson-binomial tail P(≥ 8): 7·10⁻⁷ and 2·10⁻⁷. **Limits:** the threshold 0.01 was chosen after the data were seen; independence across waveforms is assumed (the ORTHO waveforms are perturbations of one anchor and their tongue sets are correlated); uniform placement is a crude null. The figure says the coincidence is unlikely to be accidental; it is not a calibrated significance.

## 5. Reading and scope

- **Candidate conditional position mechanism.** Where a dyad fracture tongue exists in the tested range, it is frequently located where the leading-order damping work on the separatrix vanishes — the κ at which the selected oscillation reaches the separatrix. This is consistent with the dyad fracture being **chaos near the separatrix**, a generic mechanism of weakly damped pendulum-type systems; it does not say how chaos arises there.
- **Existence not explained.** κ_sep exists for every waveform; tongues do not. The smooth-triangle birth bracket q_c ∈ (0.845, 0.855], the absence for t = 0.000 and +0.008, and the two failures show that a second ingredient decides existence and, in some waveforms, position. Candidate from the locked record: harmonic content / waveform sharpness (TONGUESET's monotone shrinkage with H_high); not tested here.
- **Strong null.** κ_sep is computed from the generic weak-damping reduction; a match is an agreement with the null's own computation, not evidence beyond it. What it adds is a computable position for the dyad and the separation of "where" from "whether". Charter §10.4 (S-5) is **not** discharged; the campaign condition of §9.4 is **not** met (this is a within-family, cross-waveform comparison).
- **Not covered:** the three-node κ_frac (2.65–2.80); finite-a corrections; the multi-component tongue sets beyond the component nearest to κ_sep.

## 6. Open, in order of use

1. Independent check of §3–§4 (co-owner).
2. If wanted, a genuine prediction: κ_sep for waveforms **not yet run**, written down before any run, with a preregistered hit criterion — a within-family test that §9.4 does not license as a campaign without a PI decision.
3. The "whether" question: what separates waveforms with and without a tongue at κ_sep.
