"""Build records/hcg/HCG_SOURCE_MANIFEST.md from upload/hcg/SHA256SUMS (run from the repository root).
The 'reported origin' of a received file is read from its file name only; it is not a verification of authorship.
Usage: python3 evidence/hcg/verification/make_source_manifest.py
"""
import hashlib, os, re

UP = 'upload/hcg'
LEDGER = 'owner-session-outputs/claude/g34/dsn/adopted_v0_2/HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md'
HHO_COPIES = {
    'owner-session-outputs/claude/g34/h4sel/p2p3/generic_engine.py':
        'upload/hho/pi-uploads-received/55ff2cd3-generic_engine.py',
    'owner-session-outputs/claude/g34/nonsplit8/cyclic_disc_claude.py':
        'upload/hho/pi-uploads-received/eb26092d-cyclic_disc_claude.py',
}
HHO_TRACK = ('owner-session-outputs/claude/g34/hho/', 'owner-session-outputs/claude/g34/deliver17/hho/')
AUDITOR = ('GEOMETRIC_REPORT', 'ROUND2_FINAL_REPORT', 'REPLAY.md', 'SHA256SUMS__5_', 'G34D_W5_ROUND2_BLIND_AUDIT')


def origin(rel):
    n = os.path.basename(rel)
    if rel.startswith('owner-session-outputs/claude/g34/cg_replay/'):
        return 'Claude owner session; path-adapted replay copy of a ChatGPT script, or its output'
    if rel.startswith('owner-session-outputs/claude/scratch/'):
        return 'Claude owner session (scratch area)'
    if rel.startswith('owner-session-outputs/'):
        return 'Claude owner session'
    if rel.startswith('pi-uploads-received/session-start/'):
        return 'PI upload at session start (21 Oct 2026)'
    if re.search(r'-attachment\.txt$', n):
        return 'PI relay of a chat message'
    if any(a in n for a in AUDITOR):
        return 'PI-received; third-family auditor (by file name)'
    if 'CHATGPT' in n.upper() or n[9:].startswith('HCG_'):
        return 'PI-received; ChatGPT (by file name)'
    return 'PI-received; origin not stated in the file name'


def main():
    rows = []
    for line in open(os.path.join(UP, 'SHA256SUMS'), encoding='utf-8'):
        h, rel = line.rstrip('\n').split('  ./', 1)
        got = hashlib.sha256(open(os.path.join(UP, rel), 'rb').read()).hexdigest()
        assert got == h, rel
        note = ''
        if rel == LEDGER:
            note = 'placed byte-identical as `hcg/HCG_STUDY_LEDGER.md`'
        elif rel in HHO_COPIES:
            note = 'HHO consumer copy, byte-identical: `%s`' % HHO_COPIES[rel]
        elif rel.startswith(HHO_TRACK):
            note = 'HHO-track source evidence; custody HHO'
        rows.append((rel, h, origin(rel), note))
    head = open('records/hcg/HCG_SOURCE_MANIFEST_HEAD.md', encoding='utf-8').read()
    with open('records/hcg/HCG_SOURCE_MANIFEST.md', 'w', encoding='utf-8') as f:
        f.write(head)
        f.write('\n## 5. File table (%d files)\n\n' % len(rows))
        f.write('Paths are relative to `upload/hcg/`. An empty placement cell means "not placed yet".\n\n')
        f.write('| Upload path | SHA-256 | Origin | Placement / consumer copies |\n|---|---|---|---|\n')
        for rel, h, o, note in rows:
            f.write('| `%s` | `%s` | %s | %s |\n' % (rel, h, o, note))
    print(len(rows), 'rows; all hashes recomputed and equal')


if __name__ == '__main__':
    main()
