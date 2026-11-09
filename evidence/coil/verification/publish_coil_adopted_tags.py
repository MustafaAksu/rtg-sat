#!/usr/bin/env python3
"""Publish only the three PI-adopted COIL tags after their records reach main.

No owner, evidence or branch content is written. Existing tags are never moved.
"""
from __future__ import annotations
import base64
import hashlib
import json
import os
import re
import subprocess
import sys

CONTENT = "3d0306058495121df91e900a6ea9454185402462"
RECORDS = {
    "0.1": ("4f335334fe2c031e1cd4bef8cd49d7768755f71f", 8,
             "bab6b8aec9272318ecb81599967b37fb12ec0309e5fb01f174a3df11a32885cb"),
    "0.2": ("56e04763c33276ed96fac67b5624309b1f1d6390", 51,
             "61b363230acafa175c8313f7aa2fc03a0e9542fa42010c2d457a98c206f7e06f"),
    "0.3": (None, 59,
             "3ed4638d29ab00a3cdd58e2d26962dfa56131a69038aa19b66ba853059e4b886"),
}
ROW = re.compile(r"^\| `([^`]+)` \| `([a-f0-9]{64})` \|$", re.M)


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args])


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blob(ref: str, path: str) -> bytes:
    return git("show", f"{ref}:{path}")


def main() -> None:
    require(os.environ.get("GITHUB_REPOSITORY") == "MustafaAksu/rtg-sat", "Wrong repository")
    require(os.environ.get("GITHUB_REF") == "refs/heads/main", "Publication requires main")
    target = os.environ["GITHUB_SHA"]
    require(git("rev-parse","HEAD").decode().strip() == target, "Checkout differs from event commit")
    require(len(git("show","-s","--format=%P",target).decode().split()) == 2,
            "Publication target must be a merge commit")
    require(not git("status","--porcelain"), "Unclean publication checkout")
    cumulative = {}
    entries = {}
    for version, (commit, count, expected_record) in RECORDS.items():
        commit = commit or target
        subprocess.run(["git","merge-base","--is-ancestor",commit,target],check=True)
        record_path = f"records/coil/COIL_v{version}_RELEASE_RECORD.md"
        raw = blob(commit, record_path)
        require(sha(raw) == expected_record, f"Adoption record changed: v{version}")
        require(sha(blob(target,record_path)) == expected_record,
                f"Adopted record differs at publication tip: v{version}")
        text = raw.decode("utf-8")
        require("**Status:** ADOPTED by PI Mustafa Aksu on 2026-11-09" in text,
                f"Missing PI adoption: v{version}")
        rows = ROW.findall(text.split("## 6. Adopted payload manifest",1)[1])
        require(len(rows) == count, f"Wrong manifest count v{version}")
        for path, expected in rows:
            require(sha(blob(CONTENT,path)) == expected, f"Source identity differs: {path}")
            cumulative[path] = expected
        for path, expected in cumulative.items():
            require(sha(blob(commit,path)) == expected, f"Tag payload differs: {path}")
            require(sha(blob(target,path)) == expected, f"Published payload differs: {path}")
        entries[version] = {"commit":commit,"record_sha256":expected_record,
                            "direct_rows":count,"cumulative_rows":len(cumulative)}
        print(f"PASS v{version}: record and {len(cumulative)} cumulative payload hashes",flush=True)
    require(len(cumulative) == 118, "Cumulative scope mismatch")
    nested = 0
    for group, count in (("prereg",14),("run",11),("audit",2),("code",29),("archive",1),("outputs",108)):
        root = f"evidence/coil/{group}"
        lines = blob(target,root+"/SHA256SUMS").decode().splitlines()
        rows = [re.fullmatch(r"([a-f0-9]{64})\s+\*?(.+)",line) for line in lines if line.strip()]
        require(len(rows) == count and all(rows), f"Nested inventory differs: {group}")
        for match in rows:
            expected, path = match.groups()
            require(sha(blob(target,root+"/"+path.removeprefix("./"))) == expected,
                    f"Nested artifact changed: {group}/{path}")
        nested += len(rows)
    print(f"PASS nested artifact hashes: {nested}",flush=True)
    refs = [f"refs/tags/coil-v{v}" for v in RECORDS]
    existing = git("ls-remote","--tags","origin",*refs).decode().strip()
    require(not existing, "At least one tag already exists; never overwrite")
    subprocess.run(["git","config","user.name","ChatGPT (PI-authorized COIL publication)"],check=True)
    subprocess.run(["git","config","user.email","noreply@openai.com"],check=True)
    for version, info in entries.items():
        message = (f"COIL v{version}: PI Mustafa Aksu adoption, 2026-11-09\n\n"
                   f"Record: records/coil/COIL_v{version}_RELEASE_RECORD.md\n"
                   f"Record SHA-256: {info['record_sha256']}\n"
                   f"Approved payload commit: {CONTENT}\n"
                   f"Direct manifest rows: {info['direct_rows']}; cumulative: {info['cumulative_rows']}\n"
                   "Existing grades, OPEN obligations and retractions remain unchanged.\n"
                   "Frozen originals govern translations. No RTG adoption or physical-validation claim.\n")
        subprocess.run(["git","tag","-a",f"coil-v{version}",info["commit"],"-m",message],check=True)
    token = os.environ["GH_TOKEN"]
    header = "AUTHORIZATION: basic " + base64.b64encode(("x-access-token:"+token).encode()).decode()
    subprocess.run(["git","-c","http.https://github.com/.extraheader="+header,
                    "push","--atomic","origin",*refs],check=True)
    for version, info in entries.items():
        name = f"coil-v{version}"
        obj = git("rev-parse",name).decode().strip()
        peeled = git("rev-parse",name+"^{}").decode().strip()
        remote = git("ls-remote","--tags","origin",f"refs/tags/{name}",f"refs/tags/{name}^{{}}").decode()
        require(obj in remote and peeled in remote, f"Remote tag check failed: {name}")
        require(git("cat-file","-t",name).strip() == b"tag", "Tag is not annotated")
        info["tag_object"] = obj
    print("PUBLISHED_TAGS="+json.dumps(entries,sort_keys=True),flush=True)
    print("PUBLICATION=PASS; no tag replacement, branch write or evidence mutation",flush=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: publish_coil_adopted_tags.py REPOSITORY_DIRECTORY")
    os.chdir(sys.argv[1])
    main()
