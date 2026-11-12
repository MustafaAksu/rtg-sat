"""Replay of the three frozen check scripts behind section 6.25 of the HCG ledger, from repository files.

  g34_rank2_plane_census_claude.py   census of root pairs and planes of G34            (6.25 a)
  block_cycle_local_factor_claude.py the local identity in its norm-ratio form, 60 cases (6.25 c)
  nonsplit8_budget_screen_claude.py  arithmetic of the budget bounds                    (6.25 d)

Two of the frozen scripts carry an absolute path of the session in which they were written. This wrapper does not
edit them: it writes temporary copies in which those paths point to the repository copies of the same files, runs
each, and compares the output byte for byte with the frozen output. Every input is pinned by its full SHA-256.
The scripts support the proofs; they are not the proofs. Standard library only. Runtime about one minute.
Usage (repository root): python3 evidence/hcg/verification/replay_d27_reflection_checks.py
"""
import hashlib
import os
import subprocess
import sys
import tempfile

E = 'evidence/hcg/'
ENGINE_DIR = E + 'h4sel/p2p3'
ROOTS = E + 'h4sel/severnlink/W5_BASELINE_ROOTS.json'   # same bytes as the session's roots_alt_5.json (NAME_ALIASES.tsv)
INPUTS = {
    ENGINE_DIR + '/generic_engine.py': '66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505',
    ROOTS: '480cd6dc95f1a802943a621df632693eeb9aa7e8a9057ff5099e444950c9e35a',
}
JOBS = [
    (E + 'nonsplit8/g34_rank2_plane_census_claude.py', 'd394eb1aa9bcc06798aae7d7b362381f71afa5fdcd4e71deb09bf71a6d72c854',
     E + 'nonsplit8/g34_rank2_plane_census_claude_out.txt', '746e8a4db0fd0f46ed06cd22ec916b810bfff038baa86b9850d3e193c225c744',
     [("'/home/claude/g34/roots_alt_5.json'", repr(os.path.abspath(ROOTS)))]),
    (E + 'nonsplit8/block_cycle_local_factor_claude.py', '78845d73c7157b3409568878c987df18d9f295b104596496f7cdb4fe41b60059',
     E + 'nonsplit8/block_cycle_local_factor_claude_out.txt', '6ceda59c73e8655aac79a73f5ffd33fd52197d9abdecac17ac954ffc99e4d090',
     [("'/home/claude/g34/h4sel/p2p3'", repr(os.path.abspath(ENGINE_DIR)))]),
    (E + 'nonsplit8/nonsplit8_budget_screen_claude.py', 'da9cebe3f2b5b9dcbb6a65a829f64adbb6cd7b3203b7f43112ea38f866df9263',
     E + 'nonsplit8/nonsplit8_budget_screen_claude_out.txt', '62c42a074245ad28e611f73b84f87d3aba92070f7d93fc1df7b064ea0ae34058',
     []),
]


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


for p, h in INPUTS.items():
    assert sha(p) == h, ('hash mismatch', p)
ok = True
for script, s_sha, frozen, f_sha, mapping in JOBS:
    assert sha(script) == s_sha and sha(frozen) == f_sha, ('hash mismatch', script)
    src = open(script, encoding='utf-8').read()
    for old, new in mapping:
        assert src.count(old) == 1, ('path anchor', script, old)
        src = src.replace(old, new)
    with tempfile.TemporaryDirectory() as d:
        t = os.path.join(d, 'check.py')
        open(t, 'w', encoding='utf-8').write(src)
        out = subprocess.run([sys.executable, t], cwd=d, capture_output=True, timeout=900)
    same = out.returncode == 0 and out.stdout == open(frozen, 'rb').read()
    ok = ok and same
    print(os.path.basename(script), '| exit', out.returncode, '| output byte-identical to the frozen output:', same)
assert ok
print('PASS: 3/3')
