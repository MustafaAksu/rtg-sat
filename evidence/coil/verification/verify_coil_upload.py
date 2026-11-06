#!/usr/bin/env python3
"""Read-only source-intake verification; not a science or publication-rights certificate.

Uses only the Python standard library. Does not import or execute uploaded scripts,
extract archives, or modify source files. The optional JSON report must be outside
--root. SHA256SUMS is expected to use paths relative to --root.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import zipfile

CHUNK = 1024 * 1024
MAX_ZIP_BYTES = 1024 * 1024 * 1024  # aggregate uncompressed payload bound
MAX_ZIP_MEMBERS = 100_000
METADATA = {"README.md", "SHA256SUMS"}
REFERENCE_DOCS = (
    "owner-session-outputs/PROGRAM-INDEKSI.md",
    "owner-session-outputs/KAMPANYA-KUNYESI.md",
    "owner-session-outputs/ARSIV/README.md",
)


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def safe_name(name: str) -> str:
    # Windows-style ZIP paths are inspected but never extracted.
    p = PurePosixPath(name.replace("\\", "/"))
    if p.is_absolute() or ".." in p.parts or any(":" in v for v in p.parts):
        raise ValueError(f"unsafe relative path: {name!r}")
    if not p.parts:
        raise ValueError("empty relative path")
    return p.as_posix()


def audit(root: Path, expected_count: int | None = None) -> dict:
    root = root.resolve(strict=True)
    errors: list[str] = []
    manifest_path = root / "SHA256SUMS"
    before = {p.relative_to(root).as_posix(): digest(p)
              for p in root.rglob("*") if p.is_file() and not p.is_symlink()}
    links = [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_symlink()]
    if links:
        errors.append(f"source symlinks rejected: {links}")
    manifest: dict[str, str] = {}
    for number, line in enumerate(manifest_path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.fullmatch(r"([0-9a-fA-F]{64}) [ *](.+)", line)
        if not match:
            errors.append(f"invalid SHA256SUMS row {number}")
            continue
        try:
            name = safe_name(match.group(2))
        except ValueError as exc:
            errors.append(f"manifest row {number}: {exc}")
            continue
        if name in manifest:
            errors.append(f"duplicate manifest path: {name}")
        manifest[name] = match.group(1).lower()
    payload = set(before) - METADATA
    missing = sorted(set(manifest) - payload)
    unlisted = sorted(payload - set(manifest))
    mismatches = sorted(p for p in set(manifest) & payload if before[p] != manifest[p])
    if missing:
        errors.append(f"manifest paths absent from payload: {missing}")
    if unlisted:
        errors.append(f"payload files absent from manifest: {unlisted}")
    if mismatches:
        errors.append(f"SHA-256 mismatches: {mismatches}")
    if expected_count is not None and len(manifest) != expected_count:
        errors.append(f"expected {expected_count} source rows; got {len(manifest)}")
    by_digest: dict[str, list[str]] = defaultdict(list)
    by_basename: dict[str, list[str]] = defaultdict(list)
    for name in sorted(payload):
        by_digest[before[name]].append(name)
        by_basename[PurePosixPath(name).name].append(name)

    zip_reports = []
    total_uncompressed = 0
    total_members = 0
    rights_candidates = []
    for name in sorted(payload):
        if Path(name).suffix.lower() in {".pdf", ".epub", ".djvu", ".doc", ".docx"}:
            rights_candidates.append(name)
        if not name.lower().endswith(".zip"):
            continue
        members = []
        try:
            with zipfile.ZipFile(root / name) as archive:
                names_seen: set[str] = set()
                for info in archive.infolist():
                    member_name = safe_name(info.filename)
                    if info.is_dir():
                        continue
                    if member_name in names_seen:
                        raise ValueError(f"duplicate archive member: {member_name}")
                    names_seen.add(member_name)
                    if stat.S_ISLNK(info.external_attr >> 16):
                        raise ValueError(f"symlink in archive: {member_name}")
                    if info.flag_bits & 1:
                        raise ValueError(f"encrypted archive member: {member_name}")
                    total_uncompressed += info.file_size
                    total_members += 1
                    if total_uncompressed > MAX_ZIP_BYTES or total_members > MAX_ZIP_MEMBERS:
                        raise ValueError("ZIP inspection resource bound exceeded")
                    h = hashlib.sha256()
                    actual_size = 0
                    with archive.open(info) as stream:
                        while chunk := stream.read(CHUNK):
                            actual_size += len(chunk)
                            if actual_size > info.file_size:
                                raise ValueError("archive member size exceeds header")
                            h.update(chunk)
                    if actual_size != info.file_size:
                        raise ValueError("archive member size mismatch")
                    sha = h.hexdigest()
                    members.append({"name": info.filename, "size": actual_size,
                                    "sha256": sha, "loose_matches": by_digest.get(sha, [])})
                    if Path(member_name).suffix.lower() in {".pdf", ".epub", ".djvu", ".doc", ".docx"}:
                        rights_candidates.append(f"{name}!{info.filename}")
            zip_reports.append({"path": name, "status": "PASS", "members": members})
        except (OSError, ValueError, RuntimeError, zipfile.BadZipFile, NotImplementedError) as exc:
            errors.append(f"ZIP inspection failed: {name}: {exc}")
            zip_reports.append({"path": name, "status": "FAIL", "error": str(exc), "members": members})

    # Presence candidates only: does not infer that alternate paths/versions are equivalent.
    references = []
    for doc in REFERENCE_DOCS:
        if doc not in before:
            continue
        text = (root / doc).read_text(encoding="utf-8")
        for token in sorted(set(re.findall(r"`([^`\n]+)`", text))):
            if not re.search(r"\.(?:md|py|csv|zip|json|yaml|yml|png)$", token, re.I):
                continue
            if any(c in token for c in "*{}<> ") or token.startswith("..."):
                continue
            matches = by_basename.get(PurePosixPath(token).name, [])
            references.append({"document": doc, "reference": token,
                               "status": "PRESENT_BY_NAME" if matches else "UNRESOLVED_REFERENCE",
                               "paths": matches})

    after = {p.relative_to(root).as_posix(): digest(p)
             for p in root.rglob("*") if p.is_file() and not p.is_symlink()}
    if after != before:
        errors.append("source snapshot changed during audit")
    archive_members = [m for z in zip_reports for m in z["members"]]
    result = {
        "scope": "byte-integrity and source-inventory audit only",
        "science_replayed": False,
        "rights_certified": False,
        "original_PI_copy_equality_certified": False,
        "manifest_sha256": before.get("SHA256SUMS"),
        "readme_sha256": before.get("README.md"),
        "verdict": "PASS" if not errors else "FAIL",
        "source_count": len(payload),
        "manifest_count": len(manifest),
        "hash_matches": len(set(manifest) & payload) - len(mismatches),
        "source_bytes": sum((root / p).stat().st_size for p in payload),
        "extension_counts": dict(sorted(Counter(Path(p).suffix or "[none]" for p in payload).items())),
        "missing": missing, "unlisted": unlisted, "mismatches": mismatches,
        "read_only_check": "PASS" if before == after else "FAIL",
        "duplicate_content_groups": [v for v in by_digest.values() if len(v) > 1],
        "zip_count": len(zip_reports), "zip_members": len(archive_members),
        "zip_uncompressed_bytes": total_uncompressed,
        "zip_members_matching_loose_payload": sum(bool(m["loose_matches"]) for m in archive_members),
        "zip_audits": zip_reports,
        "reference_inventory": references,
        "document_format_rights_review_candidates": rights_candidates,
        "errors": errors,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--expected-count", type=int)
    parser.add_argument("--source-commit")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    if args.report and (args.report.resolve() == root or root in args.report.resolve().parents):
        parser.error("--report must be outside the source root")
    if args.source_commit:
        found = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
        if found != args.source_commit:
            parser.error(f"source commit mismatch: {found}")
    report = audit(root, args.expected_count)
    report["source_commit"] = args.source_commit
    if args.report:
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = {k: v for k, v in report.items() if k not in {"zip_audits", "reference_inventory"}}
    summary["unresolved_reference_candidates"] = [r for r in report["reference_inventory"] if not r["paths"]]
    summary["zip_inventory"] = [{"path": z["path"], "status": z["status"], "members": len(z["members"])} for z in report["zip_audits"]]
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
