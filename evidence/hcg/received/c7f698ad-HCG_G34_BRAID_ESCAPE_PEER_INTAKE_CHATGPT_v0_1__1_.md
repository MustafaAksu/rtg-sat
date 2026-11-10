# HCG — Independent peer replay intake, G34-BLOCK-01-BRAID-ESCAPE-01 v0.1

**Date:** 23 October 2026  
**Status recommendation:** `CHECKED` for the fixed pure-braid connection and exact H0–H4 witness; **NOT a new universal theorem or a PI adoption decision**.  
**Scope:** internal HCG R1; keep separate from the blind G34-D/Severn Priority B reviewer.

## 1. Received evidence

- Input ZIP `H3_BRAID_ESCAPE_REPLAY_v0_1.zip`: Claude's independently authored `replay_braid.py`, `reconstruct_target.py`, `generic_engine.py`, reported exact execution outputs, SHA256SUMS, source-review note and final root data.
- The peer states that only the original ChatGPT certificate's 868-letter word, original/final roots and 17 curves were borrowed, and that the cocycle/braid/cup engine was separately written. This is **independent implementation but not source-independent choice of witness**.
- The manifest's `cert.json` was not in the received ZIP; the separately available `HCG_G34_BLOCK_BRAID_ESCAPE_01_CERTIFICATE_v0_1.json` has exactly its pinned SHA-256, `44030b5f557722836b99736ea38751ce254b8982fca3920679136874279462e6`. This omission should be fixed before archiving a self-contained replay bundle.
- All eight included manifest-listed artifacts independently hash-checked; only missing `cert.json` failed the full in-ZIP manifest check.

## 2. Independently checked in present intake

The ChatGPT quick checker does **not** call either original engine. Starting from the fixed certificate matrix arrays it recomputed:

- Exact 868-letter strand permutation = identity (pure).
- Seventeen exact `T_j=I+N_j` identities.
- All 289 ordered `N_i N_j=0` products.
- `rank_K span{N_j}=16` and `rank_Q span{N_j}=16`.
- Exact sole Q-linear relation in certificate curve order: `[1,-1,0,0,1,0,...,0]`, i.e. `N_[1,4]=N_[1,2]+N_[3,4]`.

The first/last root-tuple correspondence, inverse braid return, transport of cocycles, cup preservation, (H0), (H2), (H3) and A3 were checked in Claude's separately implemented script according to its source/output record and already in ChatGPT's original production audit. The **current-turn attempt to rerun the 868-letter Claude script timed out**, so this note does not claim a fresh complete source replay.

## 3. Scientific conclusion and limitation

If the complete Claude source/output account is accepted as genuine, the fixed original 2/4-block tuple is connected by an **explicit pure braid** to an H4-successful marking. This exhibits that its failure in the restricted original interval family is **not a permanent obstruction along that pure-braid orbit**. The original fixed-marking bound `rho_tree<=b(b+1)/2` remains valid.

- This does **not** identify that orbit with W5, Severn's Appendix A component or NEW01–04.
- This does **not** establish that every generating G34 pure-braid orbit possesses a full-rank marking.
- It does **not** certify any global algebraicity theorem; the required geometry and polarized-family hypotheses are separate.
- A3 is not braid invariant in the displayed example. More generally A3 should not be used as a component invariant without proof.

## 4. Recommendation for next research gate

**Priority 1:** Close the reproducibility defect (include pinned `cert.json` alongside scripts and record execution environment). This is archival, not a new scientific validation requirement.

**Priority 2:** Explore existence of full-rank markings *component by component*, in terms of pure-braid Nielsen orbits. Test known component/lifting invariants and the **smaller repeated-root toy** before attempting any universal claim. Prefer a structural proof or a true counterexample over another unbounded random braid search.

**Priority 3:** Do not prioritize finding a braid to W5 unless needed to answer a precise component-identification research question; companion transfer Theorem 7.1 does not require that identity if its class datum, (D) and the polarization discriminant hold on the same component.

Do not send this internal material to the still-independent Hodge Priority B auditor.
