"""Replay of the frozen check script behind section 6.24 (a) of the HCG ledger, from repository files.

The frozen script evidence/hcg/nonsplit8/disc_locality_proof_check_claude.py carries two absolute paths of the
session in which it was written. This wrapper does not edit it: it writes a temporary copy in which the two paths
point to the repository copies of the same files (hashes checked), runs it, and compares the output byte for byte
with the frozen output. Runtime about one minute. Standard library only.
Usage (repository root): python3 evidence/hcg/verification/replay_d27_core_checks.py
"""
import hashlib
import os
import subprocess
import sys
import tempfile

E = 'evidence/hcg/'
SCRIPT = E + 'nonsplit8/disc_locality_proof_check_claude.py'
FROZEN_OUT = E + 'nonsplit8/disc_locality_proof_check_claude_out.txt'
ENGINE_DIR = E + 'h4sel/p2p3'
ROOTS = E + 'h4sel/severnlink/W5_BASELINE_ROOTS.json'   # same bytes as the session's roots_alt_5.json (NAME_ALIASES.tsv)
SHA = {
    SCRIPT: 'f538ce4deac12d32c16296b3d27f99a80450a8d94a0882fb51e73783d71d94dc',
    FROZEN_OUT: '985138c194851db60714c1700ede95978a2f4cf7539c394c8b3955d993f09dd4',
    ENGINE_DIR + '/generic_engine.py': '66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505',
    ROOTS: '480cd6dc95f1a802943a621df632693eeb9aa7e8a9057ff5099e444950c9e35a',
}
MAP = [("'/home/claude/g34/h4sel/p2p3'", repr(os.path.abspath(ENGINE_DIR))),
       ("'/home/claude/g34/roots_alt_5.json'", repr(os.path.abspath(ROOTS)))]


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


for p, h in SHA.items():
    assert len(h) == 64 and sha(p) == h, ('hash mismatch', p)
src = open(SCRIPT, encoding='utf-8').read()
for old, new in MAP:
    assert src.count(old) == 1, ('path anchor', old)
    src = src.replace(old, new)
with tempfile.TemporaryDirectory() as d:
    t = os.path.join(d, 'check.py')
    open(t, 'w', encoding='utf-8').write(src)
    out = subprocess.run([sys.executable, t], cwd=d, capture_output=True, timeout=900)
assert out.returncode == 0, out.stderr.decode()[-500:]
same = out.stdout == open(FROZEN_OUT, 'rb').read()
print('exit code 0; lines:', out.stdout.count(b'\n'), '; PASS lines:', out.stdout.count(b'PASS'))
print('output byte-identical to the frozen output:', same)
assert same
