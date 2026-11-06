# evidence/coil/archive — frozen archive package

`COIL_ARSIV_frozen_20261106.zip` holds the study's superseded documents and old script versions exactly as they stood in the owner session's `ARSIV/` folder (PI decision Q3, 6 Nov 2026: one frozen package, not live files). It is **provenance only**: nothing in it is a current claim, and `ARSIV/README.md` inside the package states the supersession chain (charter v0.1/v0.2, RMT v0.1/v0.2.1, RM-02 v0.1, PREREG-RM02-N3 v0.9 draft, interim RUN reports, AUDIT-CARRIER-COMPLETENESS v1.0/v2.0/v3.0 — the chain in which the verdict changed three times —, CLI-N3 remaining runs, three old n2_dyad script versions).

- `SHA256SUMS` — hash of the zip.
- `MEMBERS_SHA256SUMS` — hash of every member file (uncompressed bytes), each equal to the file's entry in `upload/coil/SHA256SUMS`. Identity of a member is `zip path + member path + member SHA-256`.
- The zip was written with fixed timestamps and sorted member order so that it can be rebuilt from the members; the member hashes, not the zip hash, are the primary identity.
