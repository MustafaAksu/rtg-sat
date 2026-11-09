#!/usr/bin/env python3
"""One-off PI-authorized COIL adoption preparation; no campaign code is executed.

Verify the approved payload and frozen evidence, then create three metadata-only
adoption commits on the fixed ChatGPT publication branch. Never merge or tag.
"""
from __future__ import annotations
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import zipfile

CONTENT = "3d0306058495121df91e900a6ea9454185402462"
CANDIDATE = "91c5c4fc961fac806300be85a7d82a2cf89b88ae"
BRANCH = "chatgpt/coil-adoption-20261109"
COUNTS = {"0.1": 8, "0.2": 51, "0.3": 59}
DATE = "2026-11-09"
ROW = re.compile(r"^\| `([^`]+)` \| `([a-f0-9]{64})` \|$", re.M)


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args])


def blob(ref: str, path: str) -> bytes:
    return git("show", f"{ref}:{path}")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sums(data: bytes) -> list[tuple[str, str]]:
    rows = []
    for line in data.decode("utf-8").splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"([a-f0-9]{64})\s+\*?(.+)", line)
        require(match is not None, f"Invalid checksum row: {line!r}")
        sha, path = match.groups()
        require(not path.startswith("/") and ".." not in PurePosixPath(path).parts,
                f"Unsafe checksum path: {path}")
        rows.append((sha, path.removeprefix("./")))
    require(len({p for _, p in rows}) == len(rows), "Duplicate checksum paths")
    return rows


def verify() -> dict[str, list[tuple[str, str]]]:
    require(os.environ.get("GITHUB_REPOSITORY") == "MustafaAksu/rtg-sat", "Wrong repository")
    require(os.environ.get("GITHUB_REF_NAME") == BRANCH, "Wrong publication branch")
    require(not git("status", "--porcelain"), "Worktree is not clean")
    require(not git("diff", CANDIDATE, "HEAD", "--", "coil", "upload/coil"),
            "Approved source/live payload changed before preparation")
    registry = {}
    for version, count in COUNTS.items():
        path = f"records/coil/COIL_v{version}_RELEASE_RECORD.md"
        text = Path(path).read_text(encoding="utf-8")
        require(CONTENT in text, f"v{version}: missing content commit binding")
        require("**Status: CANDIDATE — not adopted.**" in text,
                f"v{version}: record is not an unadopted candidate")
        section = text.split("## 6. Candidate adoption manifest", 1)[1]
        entries = ROW.findall(section)
        require(len(entries) == count and len(dict(entries)) == count,
                f"v{version}: incorrect or duplicate manifest rows")
        for filename, expected in entries:
            require(digest(blob(CONTENT, filename)) == expected,
                    f"v{version}: content-commit hash mismatch {filename}")
            require(digest(Path(filename).read_bytes()) == expected,
                    f"v{version}: current hash mismatch {filename}")
        registry[version] = entries
        print(f"PASS manifest v{version}: {count}/{count} at content commit and publication tree", flush=True)
    require(len({p for rows in registry.values() for p, _ in rows}) == 118,
            "Release payload sets overlap unexpectedly")
    total = 0
    for group, count in (("prereg",14),("run",11),("audit",2),("code",29),("archive",1),("outputs",108)):
        base = Path("evidence/coil") / group
        entries = sums((base / "SHA256SUMS").read_bytes())
        require(len(entries) == count, f"Wrong nested inventory size: {group}")
        for expected, filename in entries:
            require(digest((base / filename).read_bytes()) == expected,
                    f"Nested evidence mismatch: {group}/{filename}")
        total += len(entries)
        print(f"PASS nested {group}: {count}", flush=True)
    archive = Path("evidence/coil/archive")
    members = sums((archive / "MEMBERS_SHA256SUMS").read_bytes())
    require(len(members) == 16, "Wrong archive member inventory")
    with zipfile.ZipFile(archive / "COIL_ARSIV_frozen_20261106.zip") as zf:
        require(zf.testzip() is None, "Archive CRC failure")
        actual = {i.filename for i in zf.infolist() if not i.is_dir()}
        require(actual == {p for _,p in members}, "Archive member set differs")
        for expected, filename in members:
            require(digest(zf.read(filename)) == expected, f"Archive member mismatch: {filename}")
    print(f"PASS nested evidence: {total}; archive members: 16", flush=True)
    index = Path("coil/COIL_INDEX.md").read_text(encoding="utf-8")
    require("`coil/AUDIT_R5_PAIR_BC.md`" not in index, "Stale audit pointer")
    require("evidence/coil/audit/AUDIT-R5-PAIR-BC-v1.0.1.md" in index,
            "Frozen audit pointer missing")
    require(not git("diff", CONTENT, "HEAD", "--", "upload/coil"), "Upload changed")
    print("VERIFICATION=PASS (byte/reference scope; not a scientific replay)", flush=True)
    return registry


def adoption_text(version: str, count: int) -> str:
    inherit = {
        "0.1": "None; first repository edition. Files assigned only to later release manifests are not adopted by this release merely because they are present in its Git tree.",
        "0.2": "The eight-file governing scope of coil-v0.1 is inherited unchanged, with its existing grades, limitations and corrections. This release adds the 51 entries above.",
        "0.3": "The complete scope of coil-v0.2, including its inherited coil-v0.1 scope, is inherited unchanged. This release adds the 59 entries above and incorporates the 108 output files bound by outputs/SHA256SUMS as frozen evidence."
    }[version]
    return f"""**PI adoption decision:** Mustafa Aksu, {DATE}. English rendering of the explicit decision in the COIL owner conversation: \"I adopt the study in its present state.\" This record implements that decision; the reviewer does not substitute a review verdict for PI adoption.

**Adopted tag:** `coil-v{version}` (annotated; publication follows the merge).
**Adopted files:** all {count} entries in the manifest above, at their stated SHA-256 values and content commit `{CONTENT}`.
**Inherited scope:** {inherit}
**Exclusions:** no manifest row is excluded. The two unavailable historical sources remain unavailable; upload-only working material is not silently added to governing scope. Frozen originals remain the authority for preregistrations and run reports; translations and archives do not reinstate superseded scientific claims.
**Scientific limits:** the current recorded study is adopted with every existing grade, assumption, negative result, retraction, scope limit and OPEN obligation. No new experiment, physical validation, cross-layer equivalence or transfer to RTG is asserted. Byte checks do not upgrade scientific grades. Existing DRAFT labels inside unchanged payload files do not override this explicit adoption record and its tag.
**Publication binding:** the annotated tag identifies the exact publication commit and includes this release record's SHA-256. Verify every adopted payload hash at that target; the record is not required to contain its own commit or hash. All three scopes were adopted on {DATE}, not retroactively at the earlier migration merges.
"""


def prepare(registry: dict[str, list[tuple[str, str]]]) -> None:
    initial = git("rev-parse", "HEAD").decode().strip()
    subprocess.run(["git","config","user.name","ChatGPT (PI-authorized COIL publication)"],check=True)
    subprocess.run(["git","config","user.email","noreply@openai.com"],check=True)
    results = {}
    for version, count in COUNTS.items():
        path = Path(f"records/coil/COIL_v{version}_RELEASE_RECORD.md")
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        lines[0] = f"# COIL v{version} — release and adoption record"
        status_lines = [i for i, line in enumerate(lines) if line.startswith("**Status:** DRAFT")]
        require(len(status_lines) == 1, f"v{version}: unexpected header")
        lines[status_lines[0]] = f"**Status:** ADOPTED by PI Mustafa Aksu on {DATE}; publication tag `coil-v{version}`. The adopted scope and payload identity are fixed in §6."
        for i, line in enumerate(lines):
            if line.startswith("**Adoption:** pending PI adoption."):
                lines[i] = f"**Adoption:** PI decision {DATE}, recorded in §6. **Tag:** `coil-v{version}`."
        text = "\n".join(lines) + "\n"
        text = text.replace("## 6. Candidate adoption manifest", "## 6. Adopted payload manifest", 1)
        text, number = re.subn(r"^\*\*Status: CANDIDATE — not adopted\.\*\*.*$",
            f"**Status: ADOPTED.** The manifest fixes the approved payload bytes at content commit `{CONTENT}`. Publication changes only adoption/registry metadata, not these payloads. Any later payload change requires its own reviewed successor; this adopted record is frozen.", text, count=1, flags=re.M)
        require(number == 1, "Candidate status paragraph not uniquely replaced")
        text, number = re.subn(r"^\*\*Adoption scope \(to be filled by the PI at adoption\):\*\*.*$",
                              lambda _: adoption_text(version, count), text, count=1, flags=re.M)
        require(number == 1, "Adoption placeholder not uniquely replaced")
        path.write_text(text, encoding="utf-8", newline="\n")
        reg = Path("REGISTRY.md")
        lines = reg.read_text(encoding="utf-8").splitlines()
        hits = [i for i,line in enumerate(lines) if line.startswith("| `coil` / COIL |")]
        require(len(hits) == 1, "COIL registry row not unique")
        parts = lines[hits[0]].split("|")
        require(len(parts) == 10, "Unexpected registry schema")
        parts[3] = ' Claude and ChatGPT (COIL / "Coil Like" co-owner sessions); PI Mustafa Aksu '
        parts[4] = ' RMT and COIL labels; fixed live documents in `coil/`, RM records in `coil/records/` '
        parts[5] = f' `coil-v{version}` — PI-adopted {DATE}; governing scope: `records/coil/COIL_v{version}_RELEASE_RECORD.md`; publication identified by the annotated tag '
        parts[6] = ' `dyad-v6.4.23`, `legacy-v0.7`, `programme-v1.4`, `methodology-v1.4` (unchanged pins; historical unrepinned readings remain qualified) '
        lines[hits[0]] = "|".join(parts)
        reg.write_text("\n".join(lines)+"\n", encoding="utf-8", newline="\n")
        subprocess.run(["git","add",str(path),str(reg)],check=True)
        subprocess.run(["git","commit","-m",f"Record PI adoption of COIL v{version} ({DATE}); preserve approved payload hashes"],check=True)
        sha = git("rev-parse","HEAD").decode().strip()
        results[version] = {"adoption_commit":sha,"record_sha256":digest(path.read_bytes())}
        for rows in registry.values():
            for filename, expected in rows:
                require(digest(Path(filename).read_bytes()) == expected, f"Payload changed: {filename}")
    changed = set(git("diff","--name-only",initial,"HEAD").decode().splitlines())
    allowed = {"REGISTRY.md"} | {f"records/coil/COIL_v{v}_RELEASE_RECORD.md" for v in COUNTS}
    require(changed == allowed, f"Unexpected adoption delta: {changed}")
    require(not git("diff",CANDIDATE,"HEAD","--","coil","upload/coil",
                    "evidence/coil/prereg","evidence/coil/run","evidence/coil/audit",
                    "evidence/coil/code","evidence/coil/outputs","evidence/coil/archive"),
            "Scientific/evidence payload changed")
    require(not git("status","--porcelain"), "Uncommitted preparation changes")
    print("ADOPTION_COMMITS="+json.dumps(results,sort_keys=True),flush=True)
    token = os.environ["GH_TOKEN"]
    import base64
    header = "AUTHORIZATION: basic " + base64.b64encode(("x-access-token:"+token).encode()).decode()
    subprocess.run(["git","-c","http.https://github.com/.extraheader="+header,
                    "push","origin",f"HEAD:refs/heads/{BRANCH}"],check=True)
    print("PREPARATION=PUSHED_TO_REVIEW_BRANCH_ONLY; no merge, no tags",flush=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: prepare_coil_adoption.py REPOSITORY_DIRECTORY")
    os.chdir(sys.argv[1])
    prepare(verify())
