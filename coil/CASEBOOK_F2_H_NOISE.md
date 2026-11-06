# COIL — Casebook F2: worked example of the closed-form h_coeff(d) estimate

*(Note: T := B + L, the total number of updates. N is not used in this document — the μ_Y ≈ 2μ_X artefact in an earlier draft came exactly from that axis ambiguity.)*

**Document class:** `[DRAFT]`. **Status of the content:** `[DERIVED]` algebra verified; **retrospective** numerical illustration; **prospective predictive validation `[OPEN]`** (§ "Open validation task").
**Source:** translation of the owner session's `CASEBOOK-F2-worked-example-h_noise.md` (SHA-256 in `records/coil/COIL_SOURCE_MANIFEST.md`, batch 4), current state only; the document's own `[COR]` notices are kept because each names a retracted reading.
**Data source:** RUN-MM1-RESOLVABILITY v1.0 (`evidence/coil/run/`); independent re-fits from the archived CSVs (`evidence/coil/outputs/resolv_results/`).
**Context:** §8 of the co-owner memo (*Gauge structure of edge offsets*, reviewed in `coil/MEMO_GAUGE_CYCLE_FLUX.md`) left open how to estimate "h_noise(T), h_nonlinear(N)". This is a concrete closed-form answer to that gap. *(The expression `h_noise(T)` in this sentence is a verbatim quotation of the memo's §8 heading and is not changed.)*

---

## Formula

$$\boxed{h_{\rm coeff}(d) \sim \max_{i:\,d_i\neq0} \frac{\mathrm{ulp}(\theta_i)}{|d_i|}} \qquad [\text{FP diagnostic}],\qquad \text{a fixed floor independent of } T$$

**Notation decision (canonical):** one name is used — **h_coeff(d)**. The `h_noise` of earlier drafts was the direction-blind special case of the same object, valid only for single-component d; RMT R5 and the memo review §5b have also moved to h_coeff(d).

**Mechanism:** in a sensitivity experiment the perturbation h is applied by adding along direction d to the reference coefficient **vector**: θ_i → θ_i ± h·d_i. Component i's perturbation is lost when h·d_i ≪ ulp(θ_i) — not underflow but **floating-point absorption**.

**[COR] Direction-aware floor instead of bare ulp.** The first draft gave the floor as a single scalar ulp(coefficient), **ignoring the direction d**. The right floor is the most restrictive (largest) threshold over **all non-zero components** of the direction — if even one component is silently absorbed, the whole perturbation vector loses fidelity. (The exact threshold may shift by a factor depending on rounding mode/sign — hence the `[FP diagnostic]` status.) **Zero-valued components (θ_i = 0) are not binding**: ulp(0) is the smallest subnormal (~5×10⁻³²⁴), so that term never affects the max — perturbing a coefficient that starts at zero has no absorption problem.

**Computed for our directions u, v (independently verified):**

| direction | binding component | h_coeff | ratio to bare ulp(a) |
|---|---|---|---|
| u = (1, −1, 0)/√2 | a | 3.925×10⁻¹⁷ | √2 ≈ 1.414 |
| v = (1, 1, −1)/√3 | a | 4.807×10⁻¹⁷ | √3 ≈ 1.732 |

**[COR] Order-of-magnitude claim corrected.** RESOLVABILITY's T = 540 result gives h_sep(all, u) = 3.957×10⁻¹⁹ (recomputed independently from the archived CSV). Relative to the direction-aware floors:

$$h_{\rm coeff}(u)/h_{\rm sep} = 99.2 \;(\approx10^{2}), \qquad h_{\rm coeff}(v)/h_{\rm sep} = 121.5\;(\approx10^{2})$$

i.e. **about 2 orders of magnitude below** — "~4 orders" was wrong (even against bare ulp(a) the ratio is ~70×, again ~2 orders, never 4; the "~4 orders" figure arises only against the scan grid's floor 9.1×10⁻¹⁵). The conclusion does not change (T = 540 is still clearly below the floor; LEFT-CENSORED is consistent); only the magnitude statement is corrected.

## Worked example (with real numbers)

MM-1 anchor coefficients a = −0.172445798, b = 0.107554202:

$$\mathrm{ulp}(a) = 2.776\times10^{-17}, \qquad \mathrm{ulp}(b) = 1.388\times10^{-17}$$

**[COR] The μ value below was corrected.** The first draft said "μ ≈ 0.065, chaos-dominated stratum"; that was wrong — it pointed at the wrong stratum and applied a *global* 5-point fit to a *local* transition.

**Correct:** in the T = 270 → 540 window **94–99.96 % of the norm is carried by `regular`-classified cells**, not `chaos` (C_chaos: 0.0004 → 0.054). And the **local** (two-point) growth rate of this specific window is

$$\mu_{\rm local}(270{\to}540) \approx 0.0598 \qquad [\text{regular carries the norm here; NOT the chaos label}]$$

This matches neither the `regular` stratum's **global** 5-point fit (μ = 0.0421, R² = 0.947 — weaker, showing the single-exponential assumption does not hold exactly here) nor `chaos`'s global fit (μ = 0.0656). **Lesson:** the growth rate must be estimated locally, not borrowed from an unrelated global fit — especially when stratum dominance shows a crossover (RUN-MM1-RESOLVABILITY v1.0 §3, C_chaos table).

**Resolvability scale proxy** h_{sep,d}(T) := 1/S_d(T) (direction-indexed). It is an output-separation proxy for the observable Y, **not** h_res (RUN §2).

**[COR] The prefactor definition was ambiguous — corrected.** It was not written whether C is the intercept of S_d(T) or of h_{sep,d}(T); the two conventions give opposite signs inside the ln. **The only valid definition fixes C_S explicitly as the intercept of S(T):**

$$\boxed{S_d(T) = C_{S,d}\,e^{\mu_d T}} \quad\Longrightarrow\quad \boxed{h_{{\rm sep},d}(T) = \frac{1}{C_{S,d}}e^{-\mu_d T}}$$

From the condition h_{sep,d}(T*_d) = h_coeff(d) (with the algebra written out):

$$\frac{1}{C_{S,d}}e^{-\mu_d T_d^*} = h_{\rm coeff}(d) \;\Longrightarrow\; \boxed{T_d^* = \frac{1}{\mu_d}\ln\frac{1}{C_{S,d}\, h_{\rm coeff}(d)}}$$

and **only then** the programme-level summary:

$$\boxed{T^*_{\rm prog} = \min_d T_d^*}$$

**[COR] The previous version used direction-blind S(T), μ, C_S** — inconsistent with the direction-aware h_coeff(d), and ignoring the direction-dependent μ measured in RUN §3b.

**With our data (independently fitted from the archived CSV):**

| d | μ_d | C_{S,d} | R² | h_coeff(d) | T*_d |
|---|---|---|---|---|---|
| u | 0.064893 | 2.077×10³ | 0.999952 | 3.925×10⁻¹⁷ | **464.4** |
| v | 0.065530 | 4.904×10² | 0.999936 | 4.807×10⁻¹⁷ | **478.8** |

$$T^*_{\rm prog} = \min(464.4,\ 478.8) = 464.4$$

*(Independently verified: with synthetic test values μ_d = 0.06, C_{S,d} = 10¹¹, h_coeff(d) = 3×10⁻¹⁷ the formula satisfies h_{sep,d}(T*_d) = h_coeff(d) exactly.)*

**Two separate statements, not to be merged:**

1. **Proxy crossing** h_{sep,d}(T) = h_coeff(d), with the computed T*_prog ≈ 464, is **bracketed between** the ladder's T = 270 and T = 540 rungs.
2. **Independently**, the locked experiment is **measured** at T = 270 and **operationally LEFT-CENSORED** at T = 540.

The two support each other but **are not the same thing**: (1) is a proxy estimate, (2) is the prereg's operational status. Merging them into one sentence such as "T = 270 resolves / T = 540 does not" would re-blur the h_sep–h_res distinction carefully set up in the RUN.

**[COR] The claim "could have been predicted without a pilot run" is withdrawn — the example was circular.** In this campaign μ_d was fitted from the five points of the **full ladder** (T = 270 … 4320) — and **four of the five are already beyond the transition** (T ≥ 540, LEFT-CENSORED). So to obtain μ_d we had already measured directly the thing we were trying to predict (where the transition is). This shows the closed form has **retrospective explanatory** value (why the transition is there, what its mechanism is) — but **it is not validated as a forward, truly pilot-free prediction.**

**The reason it is unvalidated is concrete:** in the existing ladder T = 270 is the **only** point below the transition; calibrating μ only from safely resolved sub-transition points needs **at least two** such points, and we have one.

## Use protocol (for a new campaign) — corrected

1. Take the ulp of the anchor/reference coefficients and the direction(s) to be used → the h_coeff(d) floor.
2. **For each direction d separately**, calibrate μ_d **and** C_{S,d} **locally** from at least two short, cheap points (e.g. T₁ < T₂, both **clearly below** the estimated transition) — do not borrow from a global/remote fit.
3. Compute T*_d for each d in closed form, then T*_prog = min_d T*_d.
4. **Validation step (not skipped):** run a single control point slightly above T*_prog; check that it really comes out censored. If not, the μ_d calibration was not local — return to step 2.
5. Only after validation is the decision taken **not to** run a full-grid scan in the region T ≫ T*_prog.

**This campaign itself skipped step 2** (only one sub-T* point existed; the calibration was made from points that include the transition) — the method's use here is only the **explanatory** use of the worked example above, not a validated **predictive** use.

**Limits (both real, neither validated in this campaign):**
1. h_{sep,d} = 1/S_d(T) is an *order-of-magnitude* proxy, not the exact value of the true h_res (RUN-MM1-RESOLVABILITY §2: a ~100× difference measured at T = 270).
2. μ_d (and C_{S,d}) must be calibrated **locally, from sub-transition points, per direction**; taken from a global/remote fit they may reflect the wrong stratum or regime (this document's own correction history is the example).

## Open validation task `[OPEN]` (not done; subject to R5 decision relevance)

Run the T ∈ {54, 108} points named in step 2 of the use protocol, calibrate μ_u, μ_v and the corresponding C_{S,u}, C_{S,v} from them only, and check whether the T*_prog predicted from them alone is consistent with the locked experiment's measured (T = 270) / LEFT-CENSORED (T = 540) bracket — a cheap, decisive test that would validate the method as truly pilot-free predictive. Listed in `coil/COIL_INDEX.md` §8 item 7; needs its own prereg (sub-ladder B = 7·2^m, L = 20·2^m, `coil/MEMO_GAUGE_CYCLE_FLUX.md` §5).
