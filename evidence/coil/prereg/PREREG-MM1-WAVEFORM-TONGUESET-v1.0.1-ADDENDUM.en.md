> **Translation; the frozen original governs.** Original: `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md`, SHA-256 `633c5647d17159e97057dd8028a2fb63eb6e80e9ed044ca96c570a5f6018d6d9`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-WAVEFORM-TONGUESET v1.0.1 — Execution-Spec Addendum

**Status: [PREREG ADDENDUM — LOCKED, before data were seen].**
**Nature:** The scientific design has **not changed**. This addendum closes items defined in v1.0 but not operationalised (the full computation convention for T1), records an implementation-hygiene fix, and adds an equivalence check to the certificate. No prediction, threshold or decision rule has been loosened.

---

## A. T1 — full computation convention (locked)

**Set distance:** $\mathcal{T}(t)$ is treated as the union of the component intervals;
$$|\mathcal{T}_i \triangle \mathcal{T}_j| = |\mathcal{T}_i| + |\mathcal{T}_j| - 2|\mathcal{T}_i \cap \mathcal{T}_j|, \qquad d_{ij} = \frac{|\mathcal{T}_i \triangle \mathcal{T}_j|}{7.5}$$

**Correlation:** $\rho_{\rm obs}=\mathrm{Spearman}(d_{ij},\,|t_i-t_j|)$ over the 15 pairs. **Average rank** is used for ties.

**Exact p (one-sided):**
$$p=\frac{\#\{\pi \in S_6 : \rho_\pi \ge \rho_{\rm obs}\}}{720}, \quad \text{identity included.}$$
Since the $6!$ permutations are exhaustive, the Monte-Carlo-type $+1/(N+1)$ correction is **not used**.

**Undefinedness rule:** If $\rho$ is undefined because the variance of $d$ or of $|t_i-t_j|$ is zero, the T1 outcome is **UNINFORMATIVE / FAIL** — never PASS.

**Decision:** T1 PASS iff $\rho_{\rm obs}>0$ **and** $p \le 0.05$.

**Source:** `tongueset_experiment.py --t1`; output `ts_T1_result.csv`.

## B. Pre-run warning about the power of T1 `[LOCKED CAVEAT]`

A limitation measured during mechanical verification (synthetic data, not the real run):

**The symmetric-difference metric saturates for narrow and disjoint components.** If two tongue sets do not overlap at all, $d_{ij}=(|\mathcal{T}_i|+|\mathcal{T}_j|)/7.5$ and **the information of how far apart they are is lost**. In the synthetic "smoothly shifting set" scenario, because of this saturation, the result was $\rho=+0.44$, $p=0.067$ — i.e. in the right direction but above the threshold.

**Consequence:** Just as T1 FAIL does not mean "no waveform effect", it **may also not mean "no ordered structure"** — it may also stem from metric saturation. This warning was recorded before the data were seen and cannot be used to loosen the interpretation of T1 after the run; it only bounds what a FAIL *does not mean*.

**T1 REMAINS the locked primary.** It is not changed.

## C. Secondary descriptive measure (locked, OUTSIDE THE DECISION)

To document the saturation problem, a descriptive statistic **that does not enter the decision** is locked now (before the data were seen):

$$d^{\rm ctr}_{ij} = \min_{u \in \mathcal{C}_i,\ v \in \mathcal{C}_j} |u - v| \quad (\mathcal{C} = \text{component centres})$$

and the same Spearman + 720-permutation procedure is also reported on it.

**Status:** `[SECONDARY — DESCRIPTIVE ONLY]`. **It cannot change the T1 decision**, cannot enter a hypothesis update, and supports no claim on its own. It is recorded only to separate, later, the question "is a T1 FAIL due to saturation or to genuine disorder?". If one side is the empty set, $d^{\rm ctr}$ is undefined and that pair is not reported.

## D. Stage-B κ de-duplication `[implementation hygiene]`

Bracket widening rescans overlapping κ regions; the accumulated list could contain duplicate rows. Since the same κ deterministically yields the same classification, **de-duplication keyed on κ is exactly identical** and is applied before writing to file. Thus the Stage-B CSV is a true fine grid, not a multiset containing duplicates. Neither the dynamics nor the criterion has changed; no prereg change is required.

## E. Check added to the certificate: G2b

**G2b — legacy ISOA reference-equivalence:** The block-vectorised computation must show **exact equality** with the parent `isoa_experiment.cell()` implementation at κ = 3.05 / 3.10 / 3.15 ($n_{\rm chaos}$, $\lambda_{\max}$ and median $\lambda$ identical at float level). G2 showed only block-width independence; G2b binds a separate claim — *the same result with a different kernel* — into the certificate.

**State:** G1, G2, **G2b**, G3 → **PASS** (verified in this environment; to be rerun in Mustafa's environment as well).

---

*Apart from this addendum, no item of v1.0 has changed. The outcome of the campaign is still unknown: the single tongue may shift, branch, disappear, multiply, or the t-ordering may fail entirely.*
