#!/usr/bin/env python3
"""
kunye_completeness_certificate.py — KAMPANYA-KUNYESI.md §10 gate.

Scope (v1): COMPLETENESS ONLY, not scientific truth.
    "Is the Kunye a complete execution contract?"
NOT checked here (that is a separate future consistency audit):
    "Does the Kunye agree with the source prereg / code / RUN?"

Contract
  C1 campaign registry completeness  — all 11 §4 campaigns present exactly once
  C2 nine-field completeness         — per campaign, the nine §10 fields
  C3 no opaque exactness             — 'exact IC' must enumerate values, not name a function
  C4 campaign <-> code bijection     — every §4 campaign has a §6 execution mapping
  C5 artifact completeness           — canonical filenames, not just '*_results/'
  C6 source resolution               — named files exist; archived != active dependency
  C7 status coherence                — index may not call the Kunye self-contained while FAIL
  C8 immutability                    — this script writes nothing
  C9 provenance binding              — report the SHA-256 of the Kunye it certified

The script is READ-ONLY. It emits a campaign x field matrix and an exit code.
A first run is EXPECTED to FAIL; that is the point.
"""
import hashlib
import os
import re
import sys

KUNYE = "KAMPANYA-KUNYESI.md"
INDEX = "PROGRAM-INDEKSI.md"
ARCHIVE = "ARSIV"

CAMPAIGNS = ["N2", "N3", "GATE", "DYAD", "WAVEFORM", "ISOA",
             "TONGUESET", "ORTHO", "RANK", "RESOLVABILITY", "PAIRBC"]

FIELDS = ["exact_IC", "pair_constants", "waveform_params", "horizons",
          "scan_grid", "classifier", "decision_rule", "executables", "artifacts"]

# Field-presence probes. A field PASSes only if a campaign-scoped, explicit
# statement is found. Deliberately strict: presence must be demonstrable.
PROBES = {
    "pair_constants":  [r"Pair\s*[ABC]", r"\\gamma", r"a\s*=\s*\\gamma"],
    "waveform_params": [r"\\sin", r"arcsin", r"h_3", r"tanh"],
    "horizons":        [r"n_trans|burn|BURN|Lyapunov|lyap|B\s*=\s*70|70k"],
    "scan_grid":       [r"\\kappa\s*\\in|Δ0\.|\\Delta\\kappa|survey|refine|grid"],
    "classifier":      [r"Benettin|dört-çeyrek|four-quarter|CF\s*\\ge|persistence"],
    "decision_rule":   [r"karar|decision|P-\\kappa|P-β|VERDICT|D2|G1|I3|T1|W1"],
    "executables":     [r"\.py"],
    "artifacts":       [r"\.csv"],
    "exact_IC":        [r"\\{[^}]*\\}|IC|başlangıç"],
}

OPAQUE_PATTERNS = [r"\w+_ensemble\(\)", r"\w+\(\)\s*$"]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def section(text, start_marker, end_marker=None):
    i = text.find(start_marker)
    if i < 0:
        return ""
    j = text.find(end_marker, i) if end_marker else -1
    return text[i:j] if j > 0 else text[i:]


def campaign_block(appendix, name):
    """The §9 paragraph whose bolded heading names this campaign.
    Handles combined headings such as '**GATE / DYAD**'."""
    for m in re.finditer(r"\*\*([^*]+)\*\*(.*?)(?=\n\n\*\*|\Z)", appendix, re.S):
        if re.search(rf"\b{re.escape(name)}\b", m.group(1), re.I):
            return m.group(0)
    return ""


def main() -> int:
    if not os.path.exists(KUNYE):
        print(f"FATAL: {KUNYE} not found"); return 2
    text = read(KUNYE)
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    sec4 = section(text, "## 4. Kampanya künyeleri", "## 5.")
    sec6 = section(text, "## 6. Kod ↔ kampanya", "## 7.")
    sec9 = section(text, "## 9. Appendix", "## 10.")

    results = {}
    notes = {}
    mapped = {}

    # ---- C1 registry completeness
    c1_missing = [c for c in CAMPAIGNS if sec4.count(c) == 0]
    c1 = not c1_missing

    # ---- C2/C3/C5 per campaign
    for c in CAMPAIGNS:
        blk = campaign_block(sec9, c)
        row4 = "\n".join(l for l in sec4.splitlines() if re.search(rf"\b{c}\b", l))
        scope = blk + "\n" + row4
        res = {}
        for f in FIELDS:
            hit = any(re.search(p, scope, re.I) for p in PROBES[f])
            res[f] = hit
        # C3 — opaque exactness
        if res["exact_IC"] and any(re.search(p, scope) for p in OPAQUE_PATTERNS):
            res["exact_IC"] = False
            notes.setdefault(c, []).append("exact_IC opaque (function name, not values)")
        # C5 — artifacts must be concrete filenames, not just a results dir
        if res["artifacts"] and not re.search(r"[\w\*]+\.csv", scope):
            res["artifacts"] = False
            notes.setdefault(c, []).append("artifacts not concrete filenames")
        results[c] = res
        # C4 is a SEPARATE check (§6 mapping), not the same thing as the
        # 'executables' presence probe on the §9/§4 scope. Keep them distinct,
        # otherwise the C4 failure list silently absorbs probe misses.
        mapped[c] = bool(re.search(rf"\b{c}\b", sec6, re.I))
        if not mapped[c]:
            notes.setdefault(c, []).append("no §6 execution mapping row")

    # ---- C6 source resolution
    named = set(re.findall(r"`([\w\-.]+\.(?:py|md))`", text))
    missing, archived_active = [], []
    for f in sorted(named):
        if os.path.exists(f):
            continue
        if os.path.exists(os.path.join(ARCHIVE, f)) or \
           os.path.exists(os.path.join(ARCHIVE, "kod", f)):
            archived_active.append(f)
        else:
            missing.append(f)
    c6 = not missing and not archived_active

    # ---- C7 status coherence
    idx = read(INDEX) if os.path.exists(INDEX) else ""
    claims_self = bool(re.search(r"self-contained(?!\s*rerun contract\s*\*\*DEĞİL)", idx)) \
        and "DEĞİL" not in idx
    all_pass = (c1 and c6 and all(all(r.values()) for r in results.values())
                and all(mapped.values()))
    c7 = all_pass or not claims_self

    # ---------------- report ----------------
    print("=" * 72)
    print("KUNYE COMPLETENESS CERTIFICATE v1  (completeness only, not truth)")
    print("=" * 72)
    print(f"C9 provenance: {KUNYE} sha256 = {sha}")
    print()
    hdr = f"{'campaign':<15}" + "".join(f"{f[:9]:>11}" for f in FIELDS) + "   score"
    print(hdr); print("-" * len(hdr))
    for c in CAMPAIGNS:
        r = results[c]
        score = sum(r.values())
        cells = "".join(f"{'  ok':>11}" if r[f] else f"{'  --':>11}" for f in FIELDS)
        print(f"{c:<15}{cells}   {score}/9")
    print()
    for c, ns in notes.items():
        for n in ns:
            print(f"  note  {c}: {n}")
    print()
    print(f"[{'PASS' if c1 else 'FAIL'}] C1 registry completeness"
          + ("" if c1 else f" — missing: {c1_missing}"))
    n_full = sum(1 for r in results.values() if all(r.values()))
    print(f"[{'PASS' if n_full == len(CAMPAIGNS) else 'FAIL'}] C2 nine-field completeness "
          f"({n_full}/{len(CAMPAIGNS)} campaigns complete)")
    c3_bad = [c for c in CAMPAIGNS if not results[c]["exact_IC"]]
    print(f"[{'PASS' if not c3_bad else 'FAIL'}] C3 no opaque exactness"
          + ("" if not c3_bad else f" — {c3_bad}"))
    c4_bad = [c for c in CAMPAIGNS if not mapped[c]]
    print(f"[{'PASS' if not c4_bad else 'FAIL'}] C4 campaign<->code bijection (§6 mapping)"
          + ("" if not c4_bad else f" — {c4_bad}"))
    exe_bad = [c for c in CAMPAIGNS if not results[c]["executables"]]
    if exe_bad:
        print(f"       (separately: 'executables' field absent in §9/§4 scope for {exe_bad})")
    c5_bad = [c for c in CAMPAIGNS if not results[c]["artifacts"]]
    print(f"[{'PASS' if not c5_bad else 'FAIL'}] C5 artifact completeness"
          + ("" if not c5_bad else f" — {c5_bad}"))
    print(f"[{'PASS' if c6 else 'FAIL'}] C6 source resolution"
          + ("" if c6 else f" — missing={missing} archived-as-active={archived_active}"))
    print(f"[{'PASS' if c7 else 'FAIL'}] C7 status coherence "
          f"(index claims self-contained: {claims_self})")
    print("[PASS] C8 immutability — this script wrote nothing")
    print()
    verdict = all_pass and c7
    print("CERTIFICATE:", "PASS — Kunye is a self-contained execution contract"
          if verdict else "FAIL — Kunye is NOT yet self-contained (expected on early runs)")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
