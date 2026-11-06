# COIL — Review of the memo "Gauge structure of edge offsets" (MM-1 line)

**Document class:** `[DRAFT]`; review record with adopted rules. **Reviewed memo:** *MM-1 Stream Memo — Gauge Structure of Edge Offsets and Research-Workflow Update*, 3 Sep 2026 (co-owner session; the memo itself is not among the uploaded sources — **not available**). **Reviewer:** owner session. **Disposition:** accepted, with one scope warning (§3).
**Source:** translation of the owner session's `MEMO-REVIEW-gauge-cycle-flux.md` (content v1.1; SHA-256 in `records/coil/COIL_SOURCE_MANIFEST.md`, batch 4), current state only; its §5 (mid-campaign partial results) was already marked `[SUPERSEDED]` in the source and is summarised, not reproduced.
**Where the adopted rules now live:** `coil/COIL_RMT.md` §4-B (gauge precondition) and §6 R5 (feasibility audit).

---

## 1. The result is correct and **retrospectively validates** our designs

β₁ = m − n + c for every architecture we ran:

| Architecture | m | n | c | **β₁** | What we used | Agreement |
|---|---|---|---|---|---|---|
| N = 2 dyad | 1 | 2 | 1 | **0** | α = 0 | ✔ canonical gauge representative |
| path-3 | 2 | 3 | 1 | **0** | α = 0 | ✔ canonical gauge representative |
| triangle (tri0/triF) | 3 | 3 | 1 | **1** | Φ ∈ {0, π, 3π/2} — one cycle flux | ✔ exactly β₁ parameters |
| K4 (paper, RM-02.a2) | 6 | 4 | 1 | **3** | — | (paper scope, not our run) |

**Two concrete consequences:**

1. **[THM/structural]** In MM-1's antisymmetric edge-offset family there is no independent gauge-invariant frustration coordinate on connected path-3; β₁ = 0. **[COR]** The phrase "we did not and could not scan it" was too strong — raw a_ij *can* of course be scanned; they are merely gauge-equivalent representatives, not an independent physical frustration parameter. Correct statement: **on path-3 an independent antisymmetric cycle frustration is structurally impossible** (within MM-1's edge-offset frustration family — not "every kind of frustration is conceptually impossible"). The N = 3 attribution's "no cycle, no frustration" is therefore not descriptive but **structurally forced**.
2. **Scanning triF with one parameter (Φ) was right** — β₁ = 1, so the independent content of the triangle is exactly one cycle flux. An extra edge-offset scan would have rerun gauge-equivalent points. **Additional note:** β₁ gives only the *dimension* of the gauge quotient; further symmetries (graph automorphism, orientation reversal) may additionally identify some Φ values. If a dense-Φ scan is ever run, the feasibility audit checks this separately.

So the memo **does not change** our existing results; it shows our parameterisation was already gauge-consistent.

## 2. Adopted rule

> Before a new MM-1 offset experiment, β₁ = m − n + c is computed; a spanning forest is gauge-fixed and only the independent cycle-flux sector is parameterised.

Recorded in the RMT as a precondition attached to the relational-structure field (`coil/COIL_RMT.md` §4-B). Raw edge-offset patterns **do not count as separate architectures**.

## 3. **Scope warning — the IC grid is not pointwise preserved under gauge** (reviewer's addition)

The memo says "do not count gauge-equivalent representatives as separate architectures"; this is correct **for the dynamics**. But a numerical campaign has a subtlety:

the gauge transformation a_ij ↦ a_ij − (θ_j − θ_i) **shifts the coordinates as well** (x_i = y_i + θ_i). The invariant is ℓ_ij = x_j − x_i − a_ij. Our IC grid, however, is fixed in φ (coordinate differences), not in ℓ.

> Hence two gauge-equivalent realisations give **conjugate dynamics**, but **a fixed finite IC grid samples different points of phase space**. CF/mask results measured with a finite IC grid therefore need not be identical.

Practical rule: once the gauge-fixed representative is chosen, the IC grid is defined **in that gauge**, and comparisons are made within the same gauge. This does not refute the memo's rule; it fixes how it is applied.

*(Does not affect our runs: α = 0 was used on the dyad and path-3, and on the triangle comparisons were made within the same Φ parameterisation.)*

## 4. Feasibility audit — **adopted**, and applied to ourselves at once

The memo's seven-item pre-audit is accepted and added as a precondition to the prereg of new campaigns (`coil/COIL_RMT.md` R5).

**Honest self-application (RESOLVABILITY campaign, item 3 — reachability):** the ladder starts at T = 270 and the h grid goes down to 9.1×10⁻¹⁵. The results show that for T ≥ 540 **all strata are LEFT-CENSORED** — the instrument's range is exhausted already on the second rung. **[COR — narrowed]** Had the feasibility audit been applied beforehand it **would have flagged the reachability risk and required short sub-transition pilot/calibration points.** (A stronger phrase — "it would have caught this from the start" — cannot be used: the predictor itself has not yet been validated at sub-transition points; its status is `prospective predictive validation [OPEN]`; `coil/CASEBOOK_F2_H_NOISE.md`.)

This **does not invalidate** the campaign; the audit's contribution would have been to **question in advance** the measurability of the scaling law and to require cheap calibration points.

## 5. Mid-campaign partial results `[SUPERSEDED]`

The source's §5 was written while the campaign was running and carried mid-campaign figures and claims (including a double-bracket format error). The complete, corrected result — the h_sep/h_res distinction, the direction-aware ULP floor, the N90 correction, the measured μ fit, and the right reason for "regular is harder to resolve" — is in `RUN-MM1-RESOLVABILITY-v1.0.md` (`evidence/coil/run/`) and is not repeated here.

**Candidate follow-up (needs a new prereg, still open):** a **sub-ladder** with the same 7:20 ratio — B = 7·2^m, L = 20·2^m, T ∈ {27, 54, 108, 216} — could see the region before the collapse and measure the scaling law. L stays divisible by 4. *(The validation task in the casebook uses a subset, T ∈ {54, 108} — consistent.)* Status: `[OPEN]`, not designed (`coil/COIL_INDEX.md` §8 item 7).

## 5b. Closed-form addition to the feasibility audit: the direction-aware h_coeff(d) floor `[DERIVED, distilled from RUN-MM1-RESOLVABILITY]`

The RESOLVABILITY campaign (`RUN-MM1-RESOLVABILITY-v1.0.md` §2) gave the feasibility audit's reachability item (R5.3) a general closed-form estimate:

**[COR] The bare-ULP formula was made direction-aware in the casebook; this section is aligned with it.**

$$h_{\rm coeff}(d) \sim \max_{i:\,d_i\neq0} \frac{\mathrm{ulp}(\theta_i)}{|d_i|} \qquad [\text{FP diagnostic}],\qquad \text{a fixed floor independent of } T$$

**Mechanism:** the perturbation h is applied by adding along direction d to the anchor coefficient **vector**: θ_i → θ_i ± h·d_i. Component i's contribution is lost when h·d_i ≪ ulp(θ_i) — not underflow but **floating-point absorption**. The floor is taken over the **most restrictive component** of the direction (max), depends only on coefficient magnitudes and d, and does not change as T grows. The bare ulp(θ) special case is for single-component directions such as d = (1, 0, …); for general d this is the right floor.

**Use:** if the growth rate of the sensitivity magnitude S(T) with T is known (e.g. a **direction-indexed** μ_d calibrated **locally from safely resolved points below the transition**, S_d(T) ~ C_{S,d} e^{μ_d T} — with a direction-aware floor the growth model must be direction-indexed too), the crossing of h_{sep,d}(T) = 1/S_d(T) with h_coeff(d) (T*_d; programme summary min_d T*_d) — a **"proxy-predicted numerical-risk crossing"**, not a theorem — can be computed in closed form. The real h_res also depends on higher derivatives beyond Y′ and on the cancellation structure; the 1/S–h_coeff crossing is a valuable **pre-flight warning**, not by itself a resolvability theorem. This adds a concrete tool to R5.3 (reachability).

**[COR] "Without the need for a pilot run" was misleading.** μ itself has to be measured from somewhere; the claimed gain is not "no data needed" but **"estimable from a few cheap points below the transition without running the expensive points beyond it"**. RUN-MM1-RESOLVABILITY's worked example violated this distinction — μ was fitted from the full ladder (4 of 5 points already beyond the transition), i.e. a **retrospective explanation**, not a validated **predictive** use. Detail and correction: `coil/CASEBOOK_F2_H_NOISE.md`.

**Record:** added as a reference to the RMT R5 definition; for a new campaign the h_coeff(d) floor is computed from the anchor coefficients and the directions to be used, and reported, before the prereg is written.

## 6. On RPS

The reviewer agrees that the generic core stays **frozen** and that RPS (the co-owner session's review/specialisation tool, as named in the memo) is used only on request as an audit/specialisation instrument. The only host-effective result from RPS in these campaigns is the gauge/cycle-flux rule, adopted above.

---

## Disposition

- **Tree-gauge / cycle-flux parameterisation rule: ADOPTED** (§2), with the IC-grid warning (§3).
- **Feasibility audit: ADOPTED**, precondition for new preregs (§4).
- **No change** to existing results; the N = 3 ladder parameterisation is retrospectively validated.
