> **Translation; the frozen original governs.** Original: `CLI-RESOLVABILITY.md`, SHA-256 `81f6f7d67cb46787d162206abed9327562ddf399199e57412246ed98b1dd6df2`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RESOLVABILITY CAMPAIGN — Run CLI (copy-paste)

**Prereg:** `PREREG-MM1-RESOLVABILITY-v1.0.md` + `v1.0.1-ADDENDUM` (both LOCKED).
**Files:** `resolv_certificate.py`, `resolv_experiment.py` — into the same folder.
**Question:** **Up to which horizon** can RANK's derivative estimate be resolved, and is this carried by the **chaotic minority**?

**Cost:** Horizons are 15–1000× smaller than in the original RANK (T = 270…17280 vs 270,000). For each (T, direction) one sensitivity run + FD pairs on the h-grid. Total estimate **1–2 hours**; the most expensive point is m=6.

**Important:** At start-up the script freezes the strata **from the anchor baseline at the original RANK horizon** (70k/200k) — this one-off takes ~16 min and is repeated on every run. Running sequentially (`--all`) is therefore more efficient.

---

## 0) Certificate gate (mandatory)

```powershell
python resolv_certificate.py
echo $LASTEXITCODE
```

C4: **E(h) U-curve** in both the regular and the chaotic representative, in both directions (in RANK only a single regular representative/single direction had been done). **C7:** that the strata classifier is canonical (λ **and** four quarters). **C8:** that the h-grid extension goes below the chaotic U-minimum. **C9:** that the scaled norm gives `inf` in the overflow case (numeric-censor trigger). **C10:** that the CSV schema stays rectangular on mixed censored+measured rows and `summary()` does not crash.

## 1) Campaign — sequential (recommended)

```powershell
python resolv_experiment.py --all --outdir out_resolv
Compress-Archive -Path out_resolv -DestinationPath out_resolv.zip -Force
```

## 2) Piecewise alternative (m and direction separately)

```powershell
python resolv_experiment.py --m 0 --dir u --outdir out_resolv
python resolv_experiment.py --m 0 --dir v --outdir out_resolv
python resolv_experiment.py --m 1 --dir u --outdir out_resolv
```
… up to `--m 6` and `--dir v`. Then:
```powershell
python resolv_experiment.py --summary --outdir out_resolv
Compress-Archive -Path out_resolv -DestinationPath out_resolv.zip -Force
```

## To be sent

`out_resolv.zip` + the complete `--summary` output (especially the `T_cross` blocks).

## Things to know

- There are **five statuses** and none of them is a "failure": `measured`, `LEFT-CENSORED` (h_res < h_min), `RIGHT-CENSORED` (h_res ≥ h_max), `UNDEFINED-small-sensitivity`, `SENSITIVITY-NUMERIC-CENSORED` (overflow → no h_res is produced for that T and above; **not to be read as "no derivative"**).
- **Chaotic growth may go to overflow at T~10⁴** — this is a foreseen situation, not an error.
- The strata **are frozen from the anchor**, not recomputed for the perturbed waveform.
- The threshold ε=0.10 is **primary** and `[ARBITRARY-operational]`; ε ∈ {0.05, 0.20} are also written as secondary from the same data.
- **T_cross** (the first T at which h_res drops below 0.0025) is the most interpretable secondary output: if `all` crosses early and `regular` does not → the chaotic minority carries the RANK failure; if `regular` also crosses → the "regular-only non-convergence" is directly explained.
- Outputs: the per-direction `resolv_summary.csv` **and** the programme-level `resolv_program_level.csv` (min over {u,v}, censor-aware).
- If `--all` sees a numeric censor in one direction it **does not run** the higher T's for that direction (prereg: "that T and above").
- This campaign **does not ask the rank question**; it measures the precondition for returning to rank.
