# COIL v0.9 — release record (DRAFT): CLUSTEROFFSET preregistration (lock candidate)

**Status:** DRAFT — not adopted; **the preregistration is not locked** until the PI merges the pull request after co-owner review. Scope at this stage: lock of `PREREG-MM1-CLUSTEROFFSET-v1.0.md` with its executables. The run and its result will be added to this record afterwards, as for v0.6. Base: `coil-v0.7` (`fa78f52`); independent of the v0.8 candidate (Synthesis source package, PR #39), with which it shares no file except `coil/COIL_INDEX.md` §8 item 3 (different sentences of the same row — a merge conflict there is resolved by keeping both).

## 1. Files

**To be frozen at lock:** `evidence/coil/prereg/PREREG-MM1-CLUSTEROFFSET-v1.0.md`; `evidence/coil/code/clusteroffset_experiment.py`, `clusteroffset_certificate.py`, `CLI-CLUSTEROFFSET.md`; `SHA256SUMS` rows.
**Live (changed):** `coil/COIL_INDEX.md` §8 item 3 (pointer). `.gitignore` (run-output folder of the new executor).
**Unchanged:** `PREREG-RM04-TRI0-CLOSURE-DRAFT.md` (stays an unlocked draft; its Q-A is now carried by the new prereg, its Q-B/Q-C are not); every frozen file of earlier releases.

## 2. Design decisions taken in this candidate (all open to review)

| # | Decision | Reason |
|---|---|---|
| D1 | 15 cells: per pair κ = 0.75, 1.50, 2.00 and both bracket endpoints | the 12 ICID cells with measured λ_⊥ plus one cell per pair below the first linear threshold |
| D2 | base states = the five ICID cluster ICs after the PAIRBC/ICID burn-in | the orbits whose λ_⊥ ICID measured; G-BASE ties the two runs together |
| D3 | two offset directions (δ, s), ε ∈ {1e-2, 1e-4, 1e-6, 1e-8}, only +ε | N2 makes −ε redundant; ε = 1e-2 as finite probe |
| D4 | labels decided on the last quarter; distance to the cluster by wrapped δ; SLIPS = still winding in the last quarter | "returns" must be physical (mod 2π); a past slip is recorded, not a label |
| D5 | D-FATE by unanimity of the 40 runs, else MIXED with the table | no aggregation rule to tune |
| D6 | **the v0.7 draft's Q-B is not a decision here**: in the linear phase the onset law follows from the base orbit's J_⊥ products; kept as instrument check D-LIN | owner's correction of the `[HEUR]` status; flagged for the reviewer |
| D7 | N-DEG (q = r = 0) as a per-cell control with outcome EXACT / BROKEN | co-owner's request to keep the invariant subset as negative control |
| D8 | executed on the PI's Ubuntu server (bash CLI) | ICID was run there; G-BASE compares like with like |

## 3. Checks

- `python3 -B clusteroffset_certificate.py` (owner session; Python 3.13, numpy): **CERTIFICATE PASS** (K1–K8) — classifier unit tests 12/12; N1 on three cells at toy horizon; N2 bitwise; N-DEG exact; linear fixture max relative error 7.5 × 10⁻⁹ over 600 updates (growth 3474×) with |eigenvalue| = √(1 − a + aκ); fail-closed tests (empty set, complete toy-horizon set refused for the recorded horizons only, executor mismatch); ICID reference lookup.
- No campaign-cell offset was run at a horizon that lets a small offset reach a classifiable size (prereg §0 item 5). Toy-horizon labels seen and discarded: UNRESOLVED and, for the finite D2 kick, BOUNDED-OFF-CLUSTER.
- Not re-run by the co-owner at the time of writing. No frozen file of earlier releases changed; no hash, approval or result invented.

## 4. Adoption manifest

**Status: CANDIDATE — not adopted, not locked.** SHA-256 at the **content commit** `a2b62c3f7316e72dbbea8ca69a4811d706945b84`. Files not listed are inherited unchanged from `coil-v0.7`.

| file | SHA-256 at content commit |
|---|---|
| `evidence/coil/prereg/PREREG-MM1-CLUSTEROFFSET-v1.0.md` | `ef22e8f48503f8115009fc8e2614bcc49fa0c0786370b74b37a6cd365d1fa4c6` |
| `evidence/coil/code/clusteroffset_experiment.py` | `77e6068d926d41ee1cdcdd92b379198c2ac09a1c1da14828e48cfd2e859bc253` |
| `evidence/coil/code/clusteroffset_certificate.py` | `bb1e9ba432ebd174821dddace388d60bae79355af236c4006d50c39c0b64b7bc` |
| `evidence/coil/code/CLI-CLUSTEROFFSET.md` | `dd1a298d41748932e66b095c4b98593c51f78c0335072747eb2b9253ac4c41fc` |
| `evidence/coil/code/SHA256SUMS` | `75755b6271a5fcc2119d52aa26fae96eba36a27bdcdfad692cb25cf2027567e5` |
| `evidence/coil/prereg/SHA256SUMS` | `81fb1aae23aa70e27b32b8d06054e5fd67689765c2aa78c8fc4cbf7ae51580e5` |
| `coil/COIL_INDEX.md` | `27b072269b8d5b768f9b45ef2ab01853c9e8648b945c05878af62b46f3c9bed8` |
| `.gitignore` | `416c7570e0bc89b87a0766a2352e9246ed144dc2654f0b6710a6ac5e11ac3399` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
