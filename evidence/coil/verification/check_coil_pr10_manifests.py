#!/usr/bin/env python3
"""Review PR10 manifest binding without executing or modifying COIL science.

The references are deliberately pinned. A nonzero exit reports review findings,
not a failed scientific campaign. No repository file is written by this script.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
import sys
import zipfile
from pathlib import PurePosixPath

BASE = "878958641039364f5e71a6f1c1087080357eff06"
CANDIDATE = "69a5516cfa9e39ec6477f243b553fb3ace9e061c"
ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|\s*$", re.M)
SUM = re.compile(r"^([0-9a-f]{64})\s+\*?(.+)$")


def main(repo: str) -> int:
    def git(*args: str) -> bytes:
        return subprocess.check_output(["git", "-C", repo, *args])

    def data(ref: str, path: str) -> bytes:
        return git("show", f"{ref}:{path}")

    def digest(ref: str, path: str) -> str:
        return hashlib.sha256(data(ref, path)).hexdigest()

    before = git("status", "--porcelain")
    candidate_paths = set(git("ls-tree", "-r", "--name-only", CANDIDATE).decode().splitlines())
    rows_by_version = {}
    findings = []
    for version, expected_count in [("0.1", 8), ("0.2", 51), ("0.3", 59)]:
        path = f"records/coil/COIL_v{version}_RELEASE_RECORD.md"
        text = data(CANDIDATE, path).decode("utf-8")
        section = text.split("## 6. Candidate adoption manifest", 1)[1]
        rows = ROW.findall(section)
        if len(rows) != expected_count or len({p for p, _ in rows}) != len(rows):
            findings.append({"kind": "manifest_count_or_duplicate", "version": version})
        base_ok = head_ok = 0
        for file, stated in rows:
            actual_base = digest(BASE, file)
            actual_head = digest(CANDIDATE, file)
            base_ok += actual_base == stated
            head_ok += actual_head == stated
            if stated != actual_base or stated != actual_head:
                detail = {"kind": "hash_binding", "version": version, "file": file,
                          "stated": stated, "base": actual_base, "candidate": actual_head,
                          "matches_base": stated == actual_base,
                          "matches_candidate": stated == actual_head}
                findings.append(detail)
                print("HASH_DETAIL " + json.dumps(detail, ensure_ascii=False))
        rows_by_version[version] = rows
        print(f"MANIFEST v{version}: rows={len(rows)} matches_declared_base={base_ok} matches_candidate={head_ok}")

    nested_total = 0
    for version, rows in rows_by_version.items():
        for path, _ in rows:
            if PurePosixPath(path).name != "SHA256SUMS":
                continue
            n = 0
            for line in data(CANDIDATE, path).decode().splitlines():
                if not line.strip() or line.startswith("#"):
                    continue
                match = SUM.fullmatch(line)
                if match is None:
                    raise ValueError(f"Unparsed checksum row in {path}: {line!r}")
                claimed, relative = match.groups()
                rel = PurePosixPath(relative)
                if rel.is_absolute() or ".." in rel.parts:
                    raise ValueError(f"Unsafe checksum path: {relative}")
                target = str(PurePosixPath(path).parent / rel)
                if digest(CANDIDATE, target) != claimed:
                    findings.append({"kind": "nested_hash", "file": target})
                n += 1
            nested_total += n
            print(f"NESTED_MANIFEST {path}: entries={n}")

    archive = "evidence/coil/archive/COIL_ARSIV_frozen_20261106.zip"
    member_rows = []
    for line in data(CANDIDATE, "evidence/coil/archive/MEMBERS_SHA256SUMS").decode().splitlines():
        if line.strip():
            match = SUM.fullmatch(line)
            if match is None:
                raise ValueError("Unparsed archive member checksum")
            member_rows.append(match.groups())
    with zipfile.ZipFile(io.BytesIO(data(CANDIDATE, archive))) as zf:
        actual_names = {x.filename for x in zf.infolist() if not x.is_dir()}
        if actual_names != {name for _, name in member_rows} or zf.testzip() is not None:
            findings.append({"kind": "archive_inventory_or_crc"})
        for claimed, name in member_rows:
            if hashlib.sha256(zf.read(name)).hexdigest() != claimed:
                findings.append({"kind": "archive_member", "file": name})
    print(f"ARCHIVE_MEMBERS_CHECKED={len(member_rows)}")
    print(f"NESTED_ARTIFACT_ROWS_CHECKED={nested_total}")

    for path in ["coil/COIL_INDEX.md", "coil/COIL_CAMPAIGN_COMPENDIUM.md"]:
        text = data(CANDIDATE, path).decode()
        for number, line in enumerate(text.splitlines(), 1):
            for target in re.findall(r"`((?:coil|records/coil|evidence/coil)/[^`]+\.md)`", line):
                if target not in candidate_paths:
                    detail = {"kind": "missing_exact_pointer", "document": path,
                              "line": number, "target": target}
                    findings.append(detail)
                    print("POINTER_DETAIL " + json.dumps(detail))
            if re.search(r"\bbatch [1-4]\b", line, re.I):
                print(f"PLACEMENT_MARKER_CANDIDATE {path}:{number}: {line}")

    evidence_diff = git("diff", "--name-only", BASE, CANDIDATE, "--", "upload/", "evidence/").decode().splitlines()
    if evidence_diff:
        findings.append({"kind": "evidence_changed", "paths": evidence_diff})
    print("FROZEN_EVIDENCE_UNCHANGED=" + str(not evidence_diff))
    unchanged = before == git("status", "--porcelain")
    print("REVIEW_WORKTREE_UNCHANGED=" + str(unchanged))
    if not unchanged:
        findings.append({"kind": "review_worktree_mutation"})
    print("FINDINGS=" + json.dumps(findings, ensure_ascii=False))
    print("LIMITS: byte/reference checks only; no scientific replay, semantic proof or adoption.")
    return 1 if findings else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_coil_pr10_manifests.py REPOSITORY")
    raise SystemExit(main(sys.argv[1]))
