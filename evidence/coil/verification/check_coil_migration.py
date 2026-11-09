#!/usr/bin/env python3
"""Read-only byte/placement checks at fixed PR heads; no campaign code execution.
A disposable local worktree is used only to simulate the requested merge order.
This is not a scientific, translation-equivalence, or adoption certificate.
"""
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import zipfile

SOURCE = '01a262e3b1039ae394a3aca5891076cc511f22d5'
BASE = 'e90d9efc9c7b06581ae85d121d9b81584ea85459'
HEADS = {6: '899e75f5dc46794176313975dda664a5f2308d14',
         7: 'c08f43a8651ca55dae7a51809259ac2c77cac256',
         8: 'dba9dcf9d5ec5c86423a0e78a1c45131391a49cf'}
ROOT = Path(sys.argv[1]).resolve()
failures = []

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def data(ref, path):
    return git('show', f'{ref}:{path}')

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def tree(ref):
    result = {}
    for item in git('ls-tree', '-rz', '--full-tree', ref).split(b'\0'):
        if item:
            meta, path = item.split(b'\t', 1)
            if meta.split()[1] == b'blob':
                result[path.decode('utf-8')] = meta.split()[2].decode('ascii')
    return result

def sums(raw):
    result = {}
    for line in raw.decode('utf-8').splitlines():
        if not line.strip():
            continue
        m = re.fullmatch(r'([0-9a-f]{64})\s+\*?(.+)', line)
        if not m:
            raise ValueError(f'Invalid SHA256SUMS line: {line!r}')
        path = str(PurePosixPath(m[2]))
        if path.startswith('/') or '..' in PurePosixPath(path).parts or path in result:
            raise ValueError(f'Unsafe or duplicate manifest path: {path}')
        result[path] = m[1]
    return result

def check(name, condition, detail=''):
    print(f'{"PASS" if condition else "FAIL"} {name}: {detail}', flush=True)
    if not condition:
        failures.append(name)

source_tree = tree(SOURCE)
source_sums = sums(data(SOURCE, 'upload/coil/SHA256SUMS'))
check('upload_inventory', len(source_sums) == 212, str(len(source_sums)))
for path, expected in source_sums.items():
    check('source_hash:' + path, digest(data(SOURCE, 'upload/coil/' + path)) == expected)

for number, head in HEADS.items():
    t = tree(head)
    old = {p: h for p, h in source_tree.items() if p.startswith('upload/coil/')}
    new = {p: h for p, h in t.items() if p.startswith('upload/coil/')}
    check(f'PR{number}_unchanged_upload', old == new, str(head))

translated = 0
for number, groups in [(7, ['prereg', 'run']), (8, ['code', 'audit', 'outputs'])]:
    head = HEADS[number]
    t = tree(head)
    for group in groups:
        root = 'evidence/coil/' + group + '/'
        entries = sums(data(head, root + 'SHA256SUMS'))
        actual = {p[len(root):] for p in t if p.startswith(root)
                  and not p.endswith('.en.md') and p != root + 'README.md'
                  and p != root + 'SHA256SUMS'}
        check(f'PR{number}_{group}_manifest_coverage', actual == set(entries),
              json.dumps({'entries': len(entries), 'unlisted': sorted(actual-set(entries)),
                          'missing': sorted(set(entries)-actual)}))
        for name, expected in entries.items():
            payload = data(head, root + name)
            if group == 'outputs' and name.startswith('raw_from_pi/'):
                source_name = 'pi-uploads-received/' + name.removeprefix('raw_from_pi/')
            else:
                source_name = 'owner-session-outputs/' + name
            check('placed_hash:' + root + name, digest(payload) == expected
                  and source_sums.get(source_name) == expected,
                  'source=' + source_name)
        for p in sorted(t):
            if not p.startswith(root) or not p.endswith('.en.md'):
                continue
            original = p[:-6] + '.md'
            text = data(head, p).decode('utf-8')
            header = '\n'.join(text.splitlines()[:5])
            okay = original in t and 'the frozen original governs' in header.lower()
            okay = okay and digest(data(head, original)) in header
            check('translation_identity:' + p, okay)
            translated += 1
        print(f'GROUP_SUMMARY PR{number} {group} originals={len(entries)}', flush=True)
check('translation_header_count', translated == 32, str(translated))

head = HEADS[8]
arc = 'evidence/coil/archive/'
archive_sums = sums(data(head, arc + 'SHA256SUMS'))
member_sums = sums(data(head, arc + 'MEMBERS_SHA256SUMS'))
check('archive_count', len(archive_sums) == 1)
for name, expected in archive_sums.items():
    raw = data(head, arc + name)
    check('archive_zip_sha256', digest(raw) == expected, expected)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        members = [i.filename for i in z.infolist() if not i.is_dir()]
        check('archive_member_set', len(members) == len(set(members)) == 16
              and set(members) == set(member_sums), str(len(members)))
        check('archive_crc', z.testzip() is None)
        for member in members:
            h = digest(z.read(member))
            expected_source = source_sums.get('owner-session-outputs/ARSIV/' + member)
            check('archive_member:' + member, h == member_sums[member] == expected_source)

# Source documents and code are never imported/executed. Only Git manipulates
# the temporary worktree. No branch ref in the remote repository is changed.
with tempfile.TemporaryDirectory(prefix='coil-merge-review-') as tmp:
    wt = Path(tmp) / 'worktree'
    git('worktree', 'add', '--detach', str(wt), BASE)
    try:
        for number, head in HEADS.items():
            proc = subprocess.run(['git', '-C', str(wt), '-c', 'user.name=COIL review',
                '-c', 'user.email=review@example.invalid', 'merge', '--no-ff', '--no-commit', head],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            check(f'local_merge_PR{number}', proc.returncode == 0, proc.stdout.strip())
            if proc.returncode:
                subprocess.run(['git', '-C', str(wt), 'merge', '--abort'], check=True)
                break
            subprocess.run(['git', '-C', str(wt), '-c', 'user.name=COIL review',
                '-c', 'user.email=review@example.invalid', 'commit', '-m',
                f'Disposable review merge of PR {number}; not a publication'], check=True,
                stdout=subprocess.DEVNULL)
        else:
            merged = subprocess.check_output(['git', '-C', str(wt), 'rev-parse', 'HEAD']).decode().strip()
            print('INTEGRATED_TREE=' + git('rev-parse', merged + '^{tree}').decode().strip())
            for group, number in [('prereg', 7), ('run', 7), ('code', 8), ('audit', 8), ('outputs', 8)]:
                prefix = 'evidence/coil/' + group + '/'
                orig = {p: h for p, h in tree(HEADS[number]).items() if p.startswith(prefix)}
                now = {p: h for p, h in tree(merged).items() if p.startswith(prefix)}
                check('merged_group_preserved:' + group, orig == now)
            manifest = (wt / 'records/coil/COIL_SOURCE_MANIFEST.md').read_text()
            for n in [1, 2, 3, 4]:
                check('merged_manifest_batch:' + str(n), f'## Batch {n}' in manifest)
    finally:
        git('worktree', 'remove', '--force', str(wt))
check('review_worktree_clean', not git('status', '--porcelain').strip())
print('FINAL_BYTE_PLACEMENT_VERDICT=' + ('FAIL' if failures else 'PASS'))
print('FAILURES=' + json.dumps(failures))
print('LIMITS: no scientific replay, semantic translation proof, rights audit or adoption.')
sys.exit(bool(failures))
