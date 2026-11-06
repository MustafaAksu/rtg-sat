> **Translation; the frozen original governs.** Original: `RUN-MM1-WAVEFORM-TONGUESET-v1.0.md`, SHA-256 `33ef275ef0d9df410e67fc6eb74a4a40e10055836219b038295e983599c8001a`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-MM1-WAVEFORM-TONGUESET v1.0 — Tongue-Set Geometry Map

**Prereg:** PREREG-MM1-WAVEFORM-TONGUESET v1.0 + v1.0.1 addendum (LOCKED, not modified).
**Certificate:** G1 / G2 / G2b / G3 **PASS**, run independently in Mustafa's environment.
**Executor:** Mustafa (6 waveforms × 751 survey cells + Stage-B). **Audit:** Claude (independent recomputation).
**Guards:** not triggered in any waveform.

---

## 1. Geometry (locked measures)

| t | c₃ | H_high | **N_comp** | **\|𝒯(t)\|** | Narrowest component | Components of 1-cell width |
|---|---|---|---|---|---|---|
| −0.300 | −4.188 | 0.29508 | **46** | **0.22000** | 0.00250 | 29 |
| −0.220 | −2.908 | 0.12835 | **26** | **0.21750** | 0.00250 | 10 |
| −0.140 | −1.628 | 0.04127 | **11** | **0.09000** | 0.00250 | 6 |
| −0.060 | −0.348 | 0.00711 | **1** | **0.00250** | 0.00250 | 1 |
| 0.000 | +0.612 | 0.00133 | **0** | **0.00000** | — | — |
| +0.008 | +0.740 | 0.00137 | **0** | **0.00000** | — | — |

t = 0.000 and +0.008 → **`[ABSENT-in-tested-domain | κ∈[0.5,8] | survey Δκ=0.01, refine Δκ=0.0025]`** — **not** `[ABSENT]`.

**The structure is monotone:** N_comp 46 → 26 → 11 → 1 → 0 → 0 and |𝒯| 0.220 → 0.218 → 0.090 → 0.0025 → 0 → 0. As harmonic content decreases, the tongue geometry loses both in **fragmentation** and in **measure**.

**Position shifts too:** the main cluster of t=−0.300 lies in the regions κ≈3.07–3.14, 4.33–5.13, 6.42–6.62, 7.06–7.28; at t=−0.220, κ≈3.09–3.32 and 6.98–7.79; at t=−0.140, κ≈2.89–2.92, 6.63–6.73, 7.27–7.57; at t=−0.060 a single needle at κ≈7.77.

## 2. T1 — locked test: **PASS**

ρ_obs = **+0.468163**, exact one-sided p = **28/720 = 0.038889** ≤ 0.05. **Exactly identical in the independent audit** (Claude, separate computation).

> **Ordered family structure supported:** the tongue geometries of nearby waveforms are closer to each other.

Secondary descriptive (outside the decision): centre-distance Spearman = +0.811679 (6/15 pairs usable).

## 3. **Audit warning — what drives T1?** `[CRITICAL INTERPRETATION LIMIT]`

The saturation warning recorded before the run in addendum v1.0.1 §B **materialised**:

| Measurement | Value |
|---|---|
| Mean overlap ratio, 2·\|T_i∩T_j\|/(\|T_i\|+\|T_j\|) | **0.0090** (i.e. the sets are practically **disjoint**) |
| Spearman(d_ij, \|Δt\|) — locked test | +0.468163 |
| Spearman(**measure-sum only** (\|T_i\|+\|T_j\|), \|Δt\|) | **+0.458640** |
| Spearman(d_ij, measure-sum) | **+0.975657** |

**[COR] Tie-detection correction:** In the first report these two secondary values were written as +0.441257 and +0.960432. These arose from values that are mathematically equal but differ in the last bits because of summation order **not being counted as ties**. When mathematical equality is taken as the basis (10⁻¹² tolerance), the correct values are those above. **T1 itself is PASS under both conventions** — exact float: ρ=+0.468163, p=28/720=0.0389; mathematical equality: ρ=+0.511251, p=26/720=0.0361. The decision is not sensitive to the convention. The interpretation, however, is **strengthened** by the correction: the correlation of d_ij with the measure-sum is 0.976.

Because the sets almost never overlap, $d_{ij}\approx(|T_i|+|T_j|)/7.5$ has resulted; that is, **T1 has largely measured the fact that "the total measure decreases monotonically with t"**, not "the sets shift in a regular way".

**This does not invalidate the T1 PASS** — the criterion was locked, correctly applied, and the ordered family structure does exist. But **the mechanistic reading of the PASS must be kept narrow:**

> Supported: **t ↦ 𝒯(t) carries a monotone shrinking/fragmentation structure.**
> Not supported: "the tongues shift regularly along the κ axis with t" — there is no separate evidence for this; the secondary centre-distance statistic (+0.81) *points* in this direction but is **outside the decision** and comes only from the 6 pairs of 4 waveforms.

## 4. Resolution limitation `[locked declaration materialised]`

The majority of the components are **one refined cell wide** (0.0025): 29 of 46 at t=−0.300, 10 of 26 at t=−0.220. Hence:

- **N_comp is a resolution-dependent number**, not a robust invariant. A finer grid will most probably produce more components (the behaviour expected in Arnold-tongue structures).
- **|𝒯(t)| is more robust** — the total measure is less grid-sensitive than the fragmentation detail.
- The prereg §4 declaration that "a component of width < 0.01 may escape the survey" holds; the true 𝒯(t) may be **richer** than what was measured here.

For this reason, in the §1 table **|𝒯(t)| should be read as primary, N_comp as secondary**.

## 5. Results returned to the programme

1. **t ↦ 𝒯(t) is systematic** (T1 PASS). The waveform organizes the geometry — this is the question 2c asked and the answer is yes.
2. **New observation (not a hypothesis):** as harmonic content decreases (H_high 0.295 → 0.001) the tongue geometry shrinks monotonically and disappears in the scanned domain. The direction is monotone in c₃ as well (−4.19 → +0.74). **Which descriptor is causal cannot be selected from these data** — in all six, all of them are deterministic functions of t (prereg §7).
3. **ISOA's I3 result explained:** ISOA had looked only at the window κ=2.535±0.16; it is now seen that the tongues of t=−0.300 start from κ≈3.07 — that is, **[ABSENT-in-window] was correct, and it was also correct that it was not [ABSENT].** The absence discipline (RMT §5b) found its concrete counterpart here.
4. **S-4a narrowing but not closed:** for t=0.000 and +0.008 `[ABSENT-in-tested-domain]`; there may be tongues at κ>8 or at different γdt.

## 6. What this run does NOT support

- Any descriptor law (no selection among c₃, H_high, H₃ — an orthogonal second family is required).
- That N_comp is a physical number (resolution-dependent).
- Global absence for t=0.000/+0.008 (`[ABSENT-in-tested-domain]`, not `[ABSENT]`).
- "The tongues shift regularly" (T1 does not show this; §3).
- Carry-over to the smooth-triangle family, path-3, other γdt or RTG.

## 7. Next

Per prereg §7, the law candidates arising from here are tested **in a third prereg**. Two natural candidates:
- **Orthogonal second waveform family** — the only route to descriptor selection (c₃ vs H_high).
- **|𝒯(t)| scaling law** — a quantitative relation between |𝒯| and a descriptor, separately and pre-locked.

**Artifacts:** `out_tongueset/ts_stageA_t*.csv` (6) · `ts_stageB_t*.csv` (4) · `ts_geometry_summary.csv` · `ts_T1_result.csv`
