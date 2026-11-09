# COIL — Carrier-completeness audit (MM-1 ↔ legacy ringdiag): current state

**Document class:** `[DRAFT]`; live audit record. **Verdict in force:** carrier match **stands**; the onset bridge is **neither closed nor built** — `[CAND] candidate bridge, wrong coordinate space`; open item `OPEN-QUOTIENT-EQUILIBRIUM`.
**Source:** translation of the owner session's `AUDIT-CARRIER-COMPLETENESS-v3.1.md` (SHA-256 in `records/coil/COIL_SOURCE_MANIFEST.md`, batch 4), current state only. The audit's history (v1.0 "cannot be established" → v1.1 handover → v2.0 "carrier MATCHES" → v3.0 "ONSET BRIDGE CLOSED" → v3.1 **retraction** of v3.0) is preserved in the frozen archive package (`evidence/coil/archive/`, members `AUDIT-CARRIER-COMPLETENESS-v1.0/2.0/3.0.md`) and summarised in `records/coil/COIL_v0.1_RELEASE_RECORD.md` I9–I10.
**RTG pin:** ringdiag belongs to the LEGACY bridge DSN at `rtg-corpus` tag `legacy-v0.7` (§3.1 QR-defined spark boundary; recovery table). COIL's recovered update rule: `coil/RINGDIAG_UPDATE_RULE.md`; estimator definitions: `coil/KSPARK_DEF_DEGNORM.md`.
**Boundary:** nothing here is an RTG result; no named bridge exists (SG-COIL-1, charter §0.2). The RTG-side open items remain RTG's (OPEN-L0L1-0, OPEN-L0L1-1).

---

## 0. Retraction notice `[COR]` `[RETRACTED]`

**Corrected:** the central claim of v3.0 §2–3 — *"on this substrate a fixed point does not exist structurally"* — and the **ONSET BRIDGE CLOSED** verdict derived from it.
**Source of the correction:** external review (co-owner session), two counter-examples; **both verified independently by the owner session**.
**Result: the verdict is withdrawn.** The bridge did not close; **it had been sought in the wrong coordinate space.**

## 1. Counter-example 1 — synchronous **relative equilibrium** (verified ✓)

With all phases equal, f_i = sin φ (the same at every node). Absolute v = 0 is **not** a fixed point — v3.0 was right there. But

$$v_i=\Omega=\frac{K\sin\phi}{\gamma} \qquad\Longrightarrow\qquad \Omega=(1-\gamma dt)\Omega+dt\,K\sin\phi$$

**is satisfied exactly** (numerical check: K = 12.545, Ω = 11.943973, v_next = 11.943973, identical). All nodes drift together, **phase differences constant** (verified).

> $$\boxed{\text{absence of an absolute FP} \;\neq\; \text{absence of a quotient/relative equilibrium}}$$

**And this is decisive for MM-1:** MM-1 is an object built **in phase-difference (reduced) coordinates** from the start. So the right counterpart is not an absolute θ-FP but the **relative equilibrium in the global-phase quotient**. v3.0 looked for the threshold in the wrong space.

## 2. Counter-example 2 — a **twisted absolute equilibrium** also exists (verified ✓)

With θ_i = iπ, v_i = 0:

$$f_i=\tfrac14\bigl[\sin(\phi{+}\pi)+\sin(\phi{-}\pi)+\sin(\phi{+}2\pi)+\sin(\phi{-}2\pi)\bigr]=0$$

Numerical check: max|f| = 2.2×10⁻¹⁶ — **exactly zero**. And under the full inertial map (θ, v) = (iπ, 0) **is a genuine fixed point** (θ unchanged, v stays at zero — for every K).

This equilibrium need not be the right/stable branch for the spark. But on its own it falsifies

> ~~"on this substrate a fixed point does not exist structurally"~~

**Five random restarts are not a non-existence certificate.** v3.0 used them as one; the error was the owner session's.

## 3. Re-assessment of the fallback numbers

v3.0 discarded the θ = 0 fallback of `find_k_spark` (23.305 / 24.857) as "linearisation at a non-solution". **This too must be re-examined:**

the Jacobian is **independent of the common drift velocity** (the force depends on phase *differences* only). Verified numerically: the stiffness spectrum of the synchronous state has **exactly one zero mode** (global phase — expected) and transverse |σ|_max = 0.47677, i.e.

$$K^*_{\rm transverse}=\frac{\gamma}{dt\,|\sigma|_{\max}}=23.305$$

**This is the very number the fallback produces.** So 23.305 is probably not a meaningless artefact — it may be **the transverse stability threshold of the drifting synchronous branch**. v3.0's "discard" verdict was hasty. (Normalisation note: this K* is computed with the ringdiag force as recovered, deg_vec = 5 and amplitude factor 1.25 — `coil/RINGDIAG_UPDATE_RULE.md`; the σ convention follows charter §3.)

## 4. Corrected verdict

| Claim | State |
|---|---|
| Carrier structural match (update equation) | **STANDS** ✓ — between MM-1 and the **recovered ringdiag engine** (`coil/RINGDIAG_UPDATE_RULE.md`, three-layer table); the historical producer of the §3.1 brackets is not established at `legacy-v0.7` |
| No absolute synchronous FP (θ = 0, v = 0) | **TRUE** ✓ |
| Equilibrium object **globally** undefined | **NOT SHOWN — falsified** ✗ |
| ONSET BRIDGE CLOSED | **PREMATURE — withdrawn** ✗ |

## 5. The correct new open question

> **Is the ringdiag counterpart of MM-1's spectral K* object the *transverse spectral crossing* of the synchronous relative equilibrium in the global-phase quotient?**

This must be asked **before Def-B**, because perhaps no new threshold object has to be derived — **the existing threshold object was sought in the wrong coordinate space.** The numerical coincidence of §3 (23.305) supports this reading but does not prove it: whether the transverse branch is really the pre-spark attractor, and how it relates to the orbit phenomenon measured by Def-C (orbit QR-Lyapunov; `coil/KSPARK_DEF_DEGNORM.md`), **has not been tested**.

Recorded as `OPEN-QUOTIENT-EQUILIBRIUM`; it did **not** hold Pair B/C hostage (that campaign ran and closed — RUN-MM1-PAIRBC v1.0.1). Status: **parked** (`coil/COIL_INDEX.md` §8 item 2k); S-1/S-2 wait on it.

## 6. Narrowing of the RMT lesson

"Same equation ≠ same threshold object" **is valuable as a general methodological rule and is kept** (`coil/COIL_RMT.md` §4-H, carrier completeness). But the ringdiag *source case* there cannot be used as a settled example — §1–3 showed the case is probably not "no threshold object" but "threshold object sought in the wrong space". The source case is narrowed to `[CAND — under quotient-equilibrium audit]`.

## 7. Self-criticism

v3.0's error is exactly the one the RMT's own absence discipline (§5b: `[ABSENT-in-window]` ≠ `[ABSENT]`) **warns against**: a finite search (5 restarts) not finding an object does not mean the object does not exist. The owner session did not apply its own rule in its own audit. The correct label would have been `[ABSENT-in-tested-search]`.

## 8. What this audit does NOT establish

- A named bridge between MM-1 and ringdiag (none exists; SG-COIL-1).
- That 23.305 is the ringdiag spark threshold: the recorded legacy K_spark brackets are (12.54, 12.55) at φ = 1.26 and (13.48, 13.50) at φ = 1.28 (`legacy-v0.7` §3.1, `[NUM strong legacy-report]`, with the owner's source limitations); their attribution to a Def-C QR-Lyapunov run of the recovered engine is **source-reported, not owner-established**; the relation between the Def-A/B transverse crossing (a conditional spectral computation on the recovered engine) and the historical bracket is the open test (`OPEN-L0L1-KSPARK-DEF`, `coil/KSPARK_DEF_DEGNORM.md`).
- That the recovered engine is the historical producer of the §3.1 numbers (LEGACY v0.7: engine compatibility audit, not a historical-trajectory rerun).
- Any change to RTG's own grades or open items.
