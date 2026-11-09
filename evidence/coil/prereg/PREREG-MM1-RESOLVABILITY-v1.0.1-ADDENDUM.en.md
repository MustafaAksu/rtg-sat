> **Translation; the frozen original governs.** Original: `PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md`, SHA-256 `f87a6ea2dfe34c75c6726c214fe57b251ec8cf4e4b2bac87352868a16015c8be`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-RESOLVABILITY v1.0.1 — Pre-Execution Instrument Correction

**Status: [PREREG ADDENDUM — LOCKED, without data having been seen].**
**Nature:** The scientific design, the measured object, the decision logic and the status definitions **have not changed**. This addendum corrects **five execution-contract defects** that the certificate and the static audit caught before the run. No threshold has been relaxed, no result has been seen.

---

## A. **Strata classifier canonicalised** `[BLOCKER — corrected]`

The v1.0 code froze the strata using only $\lambda_{\rm total}>10^{-3}$. The programme's inherited CHAOS definition, however, is **λ_total AND all four quarters** > 10⁻³:

$$C_{ki}=(\lambda_{ki}>10^{-3})\wedge\bigwedge_{q=1}^{4}(\lambda_{q,ki}>10^{-3}), \qquad \text{chaos}_k=\exists i: C_{ki}$$

This changes strata membership **materially** and therefore affects the `regular`/`chaos` curves, $C_{\rm chaos}$ and $h_{\rm res}^{\rm regular/chaos}$.

**Verified (certificate C7, short-horizon demo):** over two κ the lam-only classifier gives `[True, True]`, the canonical classifier `[True, False]` — the difference is real.

## B. **h-range extended deterministically** `[certificate calibration]`

Certificate C4 found the U-minimum of the chaotic representatives at $h\approx10^{-11}$–$10^{-12}$. But v1.0's primary grid is $j=0..20$, i.e. $h_{\min}=9.54\times10^{-9}$ — **the chaotic branch would have been LEFT-CENSORED already at the first $T$**, whereas the same certificate had shown that this derivative is measurable in double precision.

**Locked rule:** the primary grid $h_j=0.01\cdot2^{-j}$, $j=0..20$ **is unchanged**; if still unresolved at $j=20$, a **deterministic dyadic extension** $j=21..40$ ($h_{\min}=9.10\times10^{-15}$) is applied. This is **not** a window choice made after looking at the data; the rule was written before data was seen and is audited by certificate C8.

## C. **$T_{\rm cross}$ made censor-aware** `[bug — corrected]`

The v1.0 code looked only at rows with `status=="measured"`. Yet if `LEFT-CENSORED: h_res < h_min` and $h_{\min}\ll0.0025$, **the crossing has certainly occurred**; the old code would wrongly have written "not reached" for this.

Locked logic: `measured` → is $h_{\rm res}<0.0025$; `LEFT-CENSORED` (bound ≤ 0.0025) → **crossed**; `RIGHT-CENSORED` (bound ≥ 0.0025) → **not crossed**; `SENSITIVITY-NUMERIC-CENSORED` → **UNRESOLVED** (not "not reached").

## D. **Program-level $\min_{d}$ aggregation coded** `[missing — added]`

The v1.0 prereg defined $h_{\rm res}^{s}(T)=\min_{d\in\{u,v\}}h_{\rm res}^{s,d}(T)$, but the code wrote only direction-based rows. Censor-aware aggregation rule (locked before data was seen):

| Case | Result |
|---|---|
| Any direction `SENSITIVITY-NUMERIC-CENSORED` | **UNRESOLVED** |
| Any direction `LEFT-CENSORED` | `LEFT-CENSORED` (minimum of the bounds) |
| At least one `measured` | minimum of the measured ones |
| All `RIGHT-CENSORED` | `RIGHT-CENSORED` |
| All `UNDEFINED-small-sensitivity` | `UNDEFINED-small-sensitivity` |

Output: `resolv_program_level.csv`.

## E. **Overflow safety and censor semantics** `[corrected]`

- **Scaled L2 norm.** While $|D_j|\sim10^{300}$ is finite, $D_j^2$ is not; the norm, $w_j$ and $C_{\rm chaos}$ are now computed scaled to the maximum. Only if the scaled norm is also unrepresentable is a numeric-censor given.
- **"That $T$ and above" semantics.** After seeing a numeric censor in a direction, `--all` now **does not run higher $T$** for that direction (the v1.0 code kept running — contrary to the locked semantics).
- **Tangent collapse.** The case $\alpha_n=0$ is **not** silently regularised with $10^{-300}$; since the recursion's exactness condition is violated, a numeric-censor is given.
- **Secondary ε censoring.** If $\varepsilon\in\{0.05,0.20\}$ is never satisfied in the scanned range, the entry is not left blank; `SECONDARY-CENSORED:<h` is written.

## F. A language correction regarding C4

The C4 criterion is **not** "threshold removed entirely": alongside the U-curve conditions there is also a loose $E_{\min}<10^{-2}$ **implementation-agreement guard**. Pure shape alone would not have sufficed — $E: 10\to1\to10$ is also a U-curve but is not derivative agreement. This 1% is not the primary $h_{\rm res}$ threshold.

## G. Two blockers caught in the second audit round `[corrected]`

**G1 — Censor propagation.** After seeing a numeric censor in a direction, `--all` correctly skipped the higher $T$, but **wrote no rows for the skipped points**. Since `summary()` aggregated only the directions present in the file, §D's "any direction censored → UNRESOLVED" rule was violated and the program-level result at higher $T$ wrongly appeared as `measured`. **Fix:** for every skipped $(T,d)$ a `SENSITIVITY-NUMERIC-CENSORED` placeholder row is written in the three strata; the output table stays rectangular. *(Verified with a synthetic fixture: $T=540$ is now `UNRESOLVED`.)*

**G2 — Non-finite scaled norm.** `snorm()` scales to the maximum, but the final product can still exceed the IEEE double range (a 10-element vector of $10^{308}$ → `inf`). In that case $E=\infty/\infty=$ `nan`, no h PASSes, and the result would wrongly have appeared as **LEFT-CENSORED** ("FD radius below the grid") — whereas the real cause is precision overflow. **Fix:** inside `run()`, if $S_n$ is not finite, directly `SENSITIVITY-NUMERIC-CENSORED`. Certificate **C9** verifies that this trigger works.

**G3 — C7 gate strengthened.** C7 previously checked only a source-code string; the difference was printed to the screen but did not enter the PASS condition. Now `canonical_classifier()` is a separate helper and is tested **as a unit on a synthetic fixture** (lam-only `[True,True]` vs canonical `[False,True]`); in addition, the two rules giving different results in the real short-horizon demo is also a PASS condition.

**G4 — $T_{
m cross}$ corner case.** If `UNDEFINED-small-sensitivity` is seen before the first crossing is found, the true *first* crossing can no longer be known. The code could silently have moved on to the next $T$ and reported it as the "first crossing". **Fix:** `UNRESOLVED (small sensitivity)` is written and the search for that direction stops. *(This is a secondary output; it does not affect the primary decision.)*

**G5 — CSV schema inconsistency** `[BLOCKER — corrected]`. Numeric-censor rows did not carry the secondary-ε columns; `summary()`, however, derived the schema from `rows[0].keys()`. If a real censor occurred at high $T$, it would have crashed at the merge stage with `ValueError: dict contains fields not in fieldnames` **after the measurement had been correctly made and written**.

*The reality of the bug was verified:* when the old schema-inference path is rebuilt, it produces exactly this exception.

**Fix:** a single fixed schema `ROW_FIELDS` and a single row factory `make_row()`; **all four of the four row-production paths** (D=None censor, non-finite norm censor, normal rows, skipped-high-$T$ placeholder) go through the same factory. Writers use the fixed schema instead of `rows[0].keys()` (`extrasaction="ignore"`). **Certificate C10** tests this end to end: with a mixed censored+measured fixture, identity of the schemas, `summary()` raising no exception, and the program-level output being `UNRESOLVED`.

---

**Certificate status (after the corrections):** C1–C10 **PASS**.
*Apart from this addendum, no item of v1.0 has changed. The campaign is ready to run.*
