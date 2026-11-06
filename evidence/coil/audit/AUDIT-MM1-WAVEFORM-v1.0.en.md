> **Translation; the frozen original governs.** Original: `AUDIT-MM1-WAVEFORM-v1.0.md`, SHA-256 `84d57c7a18c0a3558da905ee03e7ac0a508d7aef502483907b569f7fa66ac54a`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# AUDIT-MM1-WAVEFORM v1.0 — Independent Verification

**Subject:** RUN-MM1-WAVEFORM v1.0 (executor: ChatGPT) — three locked preregs and their results.
**Auditor:** Claude, **independent implementation** (`wf_verify.py`, vectorised numpy; ChatGPT's code was not used).
**Rationale:** Charter §6.1 + the programme's relay discipline — external AI output is independently verified before it enters the canonical record.

---

## 1. Protocol compliance

The verification follows the specification of the locked preregs exactly: a = γdt = 0.03; reduced dyad φ⁺=φ+w, w⁺=(1−a)w−aκg_q(φ); 25 IC (φ₀∈{0.1,0.5,1,2,3} × u₀∈{0,±0.5,±2}), **w₀ = dt·u₀**; burn-in 70,000; Lyapunov 200,000; CHAOS iff λ and all four quarters > 10⁻³; FRACTURE iff ≥60% IC (≥15/25).

**Reduced map consistency check [PASS]:** The form used by ChatGPT is identical to the one derived from our two-group theorem (IDEALOG §C.2). Since dt²K·2 = κ·γdt = κa, w⁺=(1−a)w−aκg(φ) is correct.

**Analytic checks [PASS]:**
- For $g_q(\phi)=\arcsin(q\sin\phi)/q$, $g'_q(0)=\cos\phi/\sqrt{1-q^2\sin^2\phi}\big|_0 = 1$ — **exactly 1 for every q**. S1/S2 were indeed held fixed.
- $A(q)=\max|g_q|=\arcsin(q)/q$ ✔ (maximum at φ=π/2).
- Cubic coefficient $c_3=(q^2-1)/6$ ✔ (Taylor: $g_q=\phi+\frac{q^2-1}{6}\phi^3+O(\phi^5)$).

## 2. Numerical verification results

### 2.1 High-q holdouts (P-W1…P-W4)

| q | A(q) | κ_obs | χ = κA | Claude CHAOS | Verification |
|---|---|---|---|---|---|
| 0.8750 | 1.217641 | 2.58803 | 3.151291 | **25/25** | ✔ FRACTURE |
| 0.9125 | 1.259566 | 2.53556 | 3.193706 | **25/25** | ✔ FRACTURE |
| 0.9475 | 1.314327 | 2.43971 | 3.206576 | **25/25** | ✔ FRACTURE |
| 0.9675 | 1.359328 | 2.36910 | 3.220384 | **25/25** | ✔ FRACTURE |

All four cells gave fracture with **25/25 IC** in the independent implementation. The A(q) and χ values agree exactly.

**CV audit:** χ mean 3.192989 ✔. **Sample CV = 0.00935** (the value in the report) — sample deviation with n−1 denominator. Population CV = 0.00810. The report used the sample CV; since the P-W3 threshold is 0.03, it is **PASS under both definitions**. *(Note: which CV definition is used is not specified in the prereg; it does not affect the result, but the definition should be locked in future.)*

### 2.2 Peak-amplitude sufficiency test (B1)

q = 0.835, A = 1.183393, κ_pred = 2.69817, the **full locked window** (±0.08, step 0.005 → 33 cells) was scanned.

> **Result: 0 FRACTURE cells. B1 FAIL replicated.**

This is the most important negative result of the study and has been independently verified: **A(q) is not sufficient for the *existence* of the tongue.**

### 2.3 Birth bracket

| q | κ_pred | Claude result |
|---|---|---|
| 0.845 | 2.68048 | **ABSENT** (0 fracture in 33 cells) ✔ |
| 0.855 | 2.66199 | **PRESENT** — 25/25 at κ=2.617 ✔ |

The tight holdout bracket **q_c ∈ (0.845, 0.855]** was independently verified.

## 3. Audit verdict

**All locked results were replicated in the independent implementation.** The numbers, protocol and decision verdicts in the report are correct. It is also methodologically clean: pilot data are explicitly marked `[EXPLORE — not decision evidence]`, holdouts were locked before the data were seen, preregs are hashed with SHA256, and the "non-pristine" character of the narrow bracket at q=0.850 is declared by the report itself.

**Suitable for canonical integration.**

## 4. Auditor's additional notes (not objections to the report, scope markers)

1. **χ ≈ 3.193 is a collapse, not a law.** χ increases monotonically over the four points (3.151 → 3.220, also visible in the plot); the CV is small but there is a systematic slope. It is not a "constant" but a quantity "drifting slowly within a narrow band". The report is right to keep this `[NUM-in-scope]`; if the q range is widened in future, the slope itself may carry information.
2. **c₃ as an alternative measure.** While A changes by only 0.7% at the bracket ends ($1.1912\to1.1995$), the cubic coefficient $c_3$ changes by 6% ($-0.04766\to-0.04483$). For the birth surface, c₃ (or higher-order structure) may be a more sensitive candidate than A — it could be carried as a second descriptor in the next prereg.
3. **The design of the next test is right but hard:** constructing a family of periodic odd functions with the same $f'(0)=1$ **and** the same $A$ but different harmonic content is a variational problem with two constraints; e.g. in the family $g(\phi)=\sin\phi+\epsilon_3\sin3\phi+\epsilon_5\sin5\phi$ one can move along a curve satisfying the constraints $g'(0)=1$ and $\max|g|=A$. This is a designable prereg.
4. **Scope:** All results are for the single-mode dyad, Pair A, smooth-triangle homotopy. They **do not transfer** to path-3 and other topologies, other γdt values, or the sine family (q→0).

## 5. Effect on the programme

- **[HYP-MM1-WAVEFORM] strengthened and split in two** (birth vs location). MM-1 §6a should be updated with this distinction.
- **S-4** (index) now splits into two sub-questions: S-4a *which waveform quantity does tongue birth depend on?* (open); S-4b *is the tongue location given by A(q)?* (supported in tested-scope).
- The distinction that S1/S2 are local-linear and S3″ is global-nonlinear has been **empirically consolidated**: same $f'(0)$, same $(\gamma dt,\kappa)$, different behaviour.
