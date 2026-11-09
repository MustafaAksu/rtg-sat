# evidence/coil — frozen files, scripts, outputs

Frozen files are stored **unchanged**; their SHA-256 is listed in the `SHA256SUMS` of each folder and in `records/coil/COIL_SOURCE_MANIFEST.md`, and equals the hash of the same file on `upload/coil-sources`. A frozen file is never edited: a preregistration is a decision contract locked before data, a run report is the evidence record of the run.

- `prereg/` — locked preregistrations and their addenda (Turkish originals).
- `run/` — run reports (Turkish originals).
- `<name>.en.md` beside a frozen file is its **English translation; the frozen original governs**. Four frozen files were written in English by their authors (the three WAVEFORM preregs and RUN-MM1-WAVEFORM-v1_0) and have no `.en.md`. A translation reproduces the original's statements, including any statement later corrected elsewhere; it does not silently fix them. Where the owner session knows of a later correction, a clearly marked *translator's note* points to the live document that carries the current state (`coil/`), and the original wording stays.
- `code/`, `outputs/`, `archive/` — batch 4.
