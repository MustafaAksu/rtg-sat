"""Place the uploaded HCG originals under evidence/hcg/ as unchanged copies (run from the repository root).
Every source hash is checked against upload/hcg/SHA256SUMS before the copy and every copy is re-hashed after it.
Working folders are kept whole, so files that refer to their neighbours stay together.
Writes evidence/hcg/PLACEMENT_MAP.tsv and evidence/hcg/SHA256SUMS.
Usage: python3 evidence/hcg/verification/place_evidence.py
"""
import hashlib, os, shutil

UP, EV = 'upload/hcg', 'evidence/hcg'
C = 'owner-session-outputs/claude/'
RULES = [                                   # first match wins: upload prefix -> evidence folder
    (C + 'g34/dsn/', 'ledger-history/'),
    (C + 'hodge_session/', 'session-start/'),
    (C + 'g34/h4sel/', 'h4sel/'),
    (C + 'g34/nonsplit8/', 'nonsplit8/'),
    (C + 'g34/severn_v2/', 'severn-v2/'),
    (C + 'g34/positive/', 'positive/'),
    (C + 'g34/deliver18/', 'positive/deliver18/'),
    (C + 'g34/hho/', 'hho-track/'),
    (C + 'g34/deliver17/', 'hho-track/deliver17/'),
    (C + 'g34/research_next/', 'research-next/'),
    (C + 'g34/', 'g34/'),
    (C + 'litrev/', 'literature-reviews/'),
    (C + 'scratch/', 'scratch/'),
    ('pi-uploads-received/', 'received/'),
]


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    rows = []
    for line in open(os.path.join(UP, 'SHA256SUMS'), encoding='utf-8'):
        h, rel = line.rstrip('\n').split('  ./', 1)
        dst = next(t + rel[len(s):] for s, t in RULES if rel.startswith(s))
        src = os.path.join(UP, rel)
        assert sha(src) == h, rel
        out = os.path.join(EV, dst)
        assert not os.path.exists(out) or sha(out) == h, out
        os.makedirs(os.path.dirname(out), exist_ok=True)
        shutil.copyfile(src, out)
        assert sha(out) == h, out
        rows.append((dst, h, rel))
    assert len({r[0] for r in rows}) == len(rows)
    rows.sort()
    with open(os.path.join(EV, 'PLACEMENT_MAP.tsv'), 'w', encoding='utf-8') as f:
        f.write('evidence_path\tsha256\tupload_path\n')
        for d, h, r in rows:
            f.write(f'{d}\t{h}\t{r}\n')
    with open(os.path.join(EV, 'SHA256SUMS'), 'w', encoding='utf-8') as f:
        for d, h, r in rows:
            f.write(f'{h}  ./{d}\n')
    print(len(rows), 'files placed; every copy re-hashed and equal to its upload hash')


if __name__ == '__main__':
    main()
