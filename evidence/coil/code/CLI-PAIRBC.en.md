> **Translation; the frozen original governs.** Original: `CLI-PAIRBC.md`, SHA-256 `fa07361dd08146aaa3d0146e519bf0dcf3d14bddde9e4c5e28dc8758a389be85`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PAIR B/C CAMPAIGN — Run CLI

**Prereg:** `PREREG-MM1-PAIRBC-v1.0.3.md` (LOCKED). **Audit:** `AUDIT-R5-PAIR-BC-v1.0.1.md`.
**Files:** `pairbc_certificate.py`, `pairbc_experiment.py` — into the same folder.
**Question:** How does $\kappa_{\rm frac}$ scale with $a=\gamma dt$? $H_\beta{:}\,p{=}1$ (β_c invariant) vs $H_\kappa{:}\,p{=}0$ (not).

---

## 0) Certificate (mandatory)

```powershell
python pairbc_certificate.py
echo $LASTEXITCODE
```
C1–C9. The critical ones: **C6** primary firewall (path3 data cannot enter the decision function), **C7** frozen Pair-A references (the runtime scan cannot change them), **C5** full coverage of the decision partition (4949 synthetic points).

## 1) Anchor guard (mandatory, before the run)

```powershell
python pairbc_experiment.py --anchor --outdir out_pairbc
echo $LASTEXITCODE
```
Verifies that the canonical pipeline reproduces the source bracket **classes**: path3 CF(2.30)<0.60 ∧ CF(2.35)≥0.60; tri0 CF(2.60)<0.60 ∧ CF(2.65)≥0.60. **If FAIL, the run stops** — a pipeline audit, not a scientific result.

## 2) Campaign

**Primary first** (the scientific weight is here):
```powershell
python pairbc_experiment.py --run tri0 B --outdir out_pairbc
```
```powershell
python pairbc_experiment.py --run tri0 C --outdir out_pairbc
```

Then replication (non-decisional):
```powershell
python pairbc_experiment.py --run path3 B --outdir out_pairbc
```
```powershell
python pairbc_experiment.py --run path3 C --outdir out_pairbc
```

Or a single command: `python pairbc_experiment.py --all --outdir out_pairbc`

## 3) Decision

```powershell
python pairbc_experiment.py --decide --outdir out_pairbc
Compress-Archive -Path out_pairbc -DestinationPath out_pairbc.zip -Force
```

## To be sent

`out_pairbc.zip` + the complete `--anchor` and `--decide` outputs.

## Things to know

- **Anchor FAIL → stop.** The new fine grid may find a value like 2.625; this is why the guard checks the **sentinel classes**, not the *exact equality* of the threshold.
- **The decision comes only from tri0.** path3 produces `REPLICATION-CONCORDANT / DISCORDANT / CENSORED` and can **under no circumstances** change the primary — the path3 data were seen before the prereg (§1.3).
- **P-cens is given only if tri0-B/C is censored**; path3 censoring does not affect the primary.
- Five decision branches: **P-β** (slope **and** level guard), **P-κ** (slope **and** level), **P-ara**, **P-other** (every other uncensored case — including being in the slope band but failing the level), **P-cens**.
- The reported $\kappa_{\rm frac}$ is the **operational** threshold of the locked coarse→refine procedure; not the continuum first-crossing (a narrow island falling between the coarse 0.25 spacing may escape).
- The Pair-A references are **frozen constants** (tri0 2.65 / path3 2.35); the anchor run does not change them.
- Cost: the canonical Pair-A horizons are preserved (70k/200k, 25 IC). The coarse scan stops early (at the first FRACTURE), so the actual cost depends on where the threshold lies.
