# Blind audit — reproducibility and integrity

## Runtime

Python 3.13.5 and SymPy 1.14.0 were used; scripts perform exact rational and Q(w) arithmetic. External Python packages needed for replay are identified in `round1/requirements.txt`. No floating-point thresholds certify ranks or discriminants.

## Original Round-1 archive (unaltered)

A byte-for-byte copy of `G34D_W5_FIRST_ROUND_GEOMETRIC_AUDIT_v0_1.zip` is included under `artifacts/`. Verify the original SHA-256:

```
6e5a6408884eca32e1d1bd454f21695659a4b100faaf03e0061e193989db705a
```

From the package root:

```sh
sha256sum artifacts/G34D_W5_FIRST_ROUND_GEOMETRIC_AUDIT_v0_1.zip
(cd round1 && sha256sum -c SHA256SUMS.txt)
```

All 34 entries match on an untouched extraction. `round1/` inside this package is the **pristine extraction**, not the mutable working extraction that was accidentally replayed during development.

## Independent R2 exact verification

```sh
python -m pip install -r round1/requirements.txt
python scripts/audit_r2_exact.py --output outputs/r2_rerun.json
python scripts/check_round1_provenance.py
```

The Round2 script reads ONLY the raw W5 JSON under `round1/supplied/v0_2/`, asserts frozen hash, then independently computes det S, det(theta S), norm witness, N17 relation, K-linear rank, nonrational coefficient, rank-two compensation and negative control alpha=2. The archived output is `outputs/round2_exact.json`.

`check_round1_provenance.py` expects a *freshly replayed* extracted folder at `round1_replayed/` to compare outputs while allowing documented volatile fields. For independent replay, first copy pristine `round1/` to `round1_replayed/` and execute the replay driver there:

```sh
cp -a round1/. round1_replayed/
(cd round1_replayed && python scripts/run_audit.py)
python scripts/check_round1_provenance.py
```

Run the driver only in the **copy**. It recreates the three algebraic output JSONs and four negative-control logs, and changes time/path-dependent output bytes. This does **not** invalidate pristine archived hashes.

**Computational scope:** No script formalizes the geometric degeneration, VHS polarization, full proof of Schmid, supplier algebraic correspondences, proper Hilbert-scheme arguments, Landherr, or a public global theorem. Those are argued and audited in mathematical prose with source references. No PDF binary downloaded from the web is asserted to be part of the reproducible package.

## Integrity incident

An initial five-output hash discrepancy reported during R2 was caused by running the audit in a working extraction before manifest checking. Independently extracting the original ZIP and checking all 34 entries removed it. This incident and the corrected check are preserved in `ROUND2_FINAL_REPORT.md` §8 and `outputs/round1_provenance_audit.json`. The original ZIP remains untouched.

## Manifest files

`SHA256SUMS.txt` hashes the *delivered bundle members* excluding itself; `BUNDLE_MANIFEST.json` includes file size and hashes. The original Round-1 nested archive has its original SHA manifest. Replay output checks compare invariants rather than naively assuming byte-identical elapsed times.
