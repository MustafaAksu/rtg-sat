> **Translation; the frozen original governs.** Original: `CLI-TONGUESET.md`, SHA-256 `4852a63c46763fd719381ad8ab5071fb5c8c2e580c9e347c1112fd87c7b2864e`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# TONGUE-SET CAMPAIGN — Run CLI (copy-paste)

**Prereg:** `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.md` + `v1.0.1-ADDENDUM` (both LOCKED).
**Files:** `tongueset_certificate.py`, `tongueset_experiment.py` (into the same folder).
**Object:** 𝒯(t) = {κ ∈ [0.5, 8] : CF(t,κ) ≥ 0.60} — the set-valued tongue geometry of the six waveforms.

**Cost (measured in this environment):** block-vectorized cell ≈ 1.3 s → **~16 min survey per waveform**. Parallel in six windows ≈ 20–25 min total (once Stage B is added). The block optimization is certified **bit-identical** (G2).

---

## 0) Certificate gate (mandatory)

```powershell
python tongueset_certificate.py
echo $LASTEXITCODE
```
If not `0`, no run is performed.

## 1) Campaign — parallel in six windows (recommended)

Each in a separate PowerShell window, the **same** `--outdir`:

```powershell
python tongueset_experiment.py --t -0.300 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t -0.220 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t -0.140 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t -0.060 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t 0.000 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t 0.008 --outdir out_tongueset
```

(The file names carry the t value; writing into the same folder is safe.)

## 2) Geometry summary + locked T1 test (after all six have finished)

```powershell
python tongueset_experiment.py --geometry --outdir out_tongueset
python tongueset_experiment.py --t1 --outdir out_tongueset
Compress-Archive -Path out_tongueset -DestinationPath out_tongueset.zip -Force
```

## 3) Sequential alternative (single window, ~2–2.5 hours)

```powershell
foreach ($t in -0.300,-0.220,-0.140,-0.060,0.000,0.008) {
  python tongueset_experiment.py --t $t --outdir out_tongueset
}
python tongueset_experiment.py --geometry --outdir out_tongueset
Compress-Archive -Path out_tongueset -DestinationPath out_tongueset.zip -Force
```

## To be sent

`out_tongueset.zip` + the `[ts A]` / `[ts B]` lines from the console and the `--geometry` output.

## Things to know

- **`GUARD FAIL` → stop and report.** Three guards: g'(0)=1, max|g|=A₀, no extra zero in (0,π).
- Stage A prints progress every 25 cells; a long silence is not normal.
- Stage B is **deterministic**: the bracket widens until two consecutive negatives appear on both sides of every positive run, then it is rescanned with Δκ=0.0025. No window is chosen by looking at the data.
- If no positive comes out at all for a waveform, Stage B is skipped and the status becomes **`ABSENT-in-tested-domain`** — **not `ABSENT`** (RMT v0.3.2 §5b).
- In the geometry summary the `*` mark = component resting against the domain edge (censored).
- **This campaign is not a law test**, it is a preregistered geometry inference. The descriptor choice (c₃, H₃, H_high) is not made from these data; an orthogonal second family is required.
