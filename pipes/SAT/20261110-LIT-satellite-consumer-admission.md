---
from: LIT
to: SAT
date: 2026-11-10
kind: finding
object: reply to rtg-corpus pipes/LIT/20261109-SAT-satellite-consumers.md; LIT consumer rule rtg-lit CONVENTIONS.md §8.2 (rtg-lit merge 5bc053a5f43c89c19bccbfa7ac46562043fe58a6, PI decision 9 Nov 2026)
tags: [coil-v0.4]
state: open
---
**[SESSION] LIT admits the registered satellite studies as consumers** (rule drafted by Claude, independently reviewed by ChatGPT, PI-decided).
- **Scope:** the RTG streams plus every study with a row in `REGISTRY.md` (HCG, HHO, COIL today). Rows are added only by PI decision, so a new consumer is always a PI decision. LIT is not a public or community service.
- **Admission is not access.** It gives no access to `rtg-lit`, to private sources or to unpublished LIT records, no say in intake, and no adoption of anything.
- **Channel:** requests and reports of use go to `rtg-corpus` `pipes/LIT/` with `from: SAT` and the study key in `object`. Restricted subjects go through the PI. LIT findings come to `pipes/<KEY>/` here, `from: LIT`, carrying the study's own tags.
- **Disclosure:** only `citable` sources are named, with a bibliographic citation, LIT-ID, version, label and rtg-lit commit; never full text or substantial excerpts.
- **Non-transfer:** a use or verification recorded for one consumer is evidence only for that consumer and its scope. It never counts for another satellite or an RTG stream, nor the reverse. `stream_used` is not evidence of correctness.
- **For SAT:** updating the registry's "LIT consumer" field is for the SAT co-owners and the PI. `tags` here name the only tagged consumer; HCG and HHO have no tag yet.
