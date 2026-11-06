# evidence/coil/outputs — result data

- `*_results/`, `*_merged/`, top-level CSVs: result tables as produced by the campaigns (owner-session copies), unchanged.
- `raw_from_pi/`: run outputs **exactly as received from the PI's machine** during the study (`out_*.zip`, `n3_*.csv`, `pairbc_*.csv`, `stageA_A_euler.csv`, …) plus the two notes returned by the RTG session. ZIP members are identified as `zip path + member path + member SHA-256` (member list and hashes: `records/coil/COIL_PR3_INTAKE_REVIEW_20261106.md`).
- `SHA256SUMS` covers every file in this folder tree; all equal to the file's entry in `upload/coil/SHA256SUMS`.
