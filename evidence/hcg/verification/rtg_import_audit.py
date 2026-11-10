"""HCG: targeted audit of the RTG imports of the v0.2 ledger (section 7) against rtg-corpus tags.
For each imported statement it finds the defining entry at the historical tag and at the latest tag,
reports the section heading it sits in and its leading grade tag, and says whether the entry text is
identical at both tags (RID markup and backticks ignored).
Scope: it compares the ONE selected defining line of each import. It does not check proofs, the entries
that line depends on, or the rest of the block. The OFN reference of R8 names no statement and is not covered.
Needs a local clone of MustafaAksu/rtg-corpus that holds the tags named below.
Usage: python3 rtg_import_audit.py /path/to/rtg-corpus
"""
import hashlib, re, subprocess, sys

DYAD = 'dsn/RTG_DYADIC_OSCILLATOR_DSN.md'
GEN = 'dsn/RTG_GENESIS_GEOMETRY_DSN.md'
PROG = 'dsn/RTG_PROGRAMME_OVERVIEW.md'
ITEMS = [  # label, file, historical tag, latest tag, regex that picks the defining entry line
    ('R1 A (DYAD-side: A = DT(P1) of order 6, in the Q-form entry)', DYAD, 'dyad-v6.4.19', 'dyad-v6.4.23', r'^`\[ALG\]` \[RID: DYAD-ALG-Q-INVARIANT-FORM\]'),
    ('R1 A^3 = -I, A^6 = I (GEN-THM-LIN-ORDER6)', GEN, 'gen-v2.8.9', 'gen-v2.10', r'^`\[THM\]` `\[RID: GEN-THM-LIN-ORDER6\]`'),
    ('R1 A (Genesis linearization)', GEN, 'gen-v2.8.9', 'gen-v2.10', r'Linearization: \$DT\(0,0\) = A'),
    ('R2 B, Q-invariant form (DYAD-ALG-Q-INVARIANT-FORM)', DYAD, 'dyad-v6.4.19', 'dyad-v6.4.23', r'^`\[ALG\]` \[RID: DYAD-ALG-Q-INVARIANT-FORM\]'),
    ('R3 J_Q (Genesis 6.6 display)', GEN, 'gen-v2.8.9', 'gen-v2.10', r'^\$\$J_Q = \\tfrac\{1\}\{\\sqrt\{3\}\}'),
    ('R4 c21 (DYAD-THM-C21 entry)', DYAD, 'dyad-v6.4.19', 'dyad-v6.4.23', r'^`\[THM\]` `\[RID: DYAD-THM-C21\]`'),
    ('R4 mu display (six-step cubic jet)', DYAD, 'dyad-v6.4.19', 'dyad-v6.4.23', r'^\$\$W_\{m\+1\}=W_m\+\\mu'),
    ('R4 mu and a05 in the conjugacy chart (DYAD-ALG-NF6 values)', DYAD, 'dyad-v6.4.19', 'dyad-v6.4.23', r'Confirmed exactly at \$p=6\$ in the conjugacy chart'),
    ('R5 DYAD-THM-SMOOTH-EMBEDDING entry', DYAD, 'dyad-v6.4.19', 'dyad-v6.4.23', r'^`\[THM\]` \[RID: DYAD-THM-SMOOTH-EMBEDDING\]'),
    ('R6(a) DYAD-THM-PRIM-CTR entry', DYAD, 'dyad-v6.4.19', 'dyad-v6.4.23', r'`\[RID: DYAD-THM-PRIM-CTR\]` \*\*Primitive contraction'),
    ('R8 SG-PROG-1', PROG, 'programme-v1.2', 'programme-v1.4', r'^\*\*\[SG-PROG-1\]'),
]


def show(repo, tag, path):
    return subprocess.run(['git', '-C', repo, 'show', f'{tag}:{path}'], check=True, capture_output=True).stdout


def norm(l):
    return re.sub(r'`?\[RID: ([A-Z0-9-]+)\]`?', r'\1', l).replace('`', '')


def find(text, rx):
    sec, hits = '', []
    for i, l in enumerate(text.split('\n'), 1):
        if re.match(r'^#{2,3} ', l):
            sec = re.sub(r'\s*\{#.*$', '', l).lstrip('# ')
        if re.search(rx, l):
            hits.append((i, sec, l))
    return hits


def main(repo):
    cache = {}
    for label, path, t0, t1, rx in ITEMS:
        out = []
        for t in (t0, t1):
            if (t, path) not in cache:
                raw = show(repo, t, path)
                cache[(t, path)] = (hashlib.sha256(raw).hexdigest(), raw.decode('utf-8'))
            h, text = cache[(t, path)]
            hits = find(text, rx)
            assert len(hits) == 1, (label, t, len(hits))
            out.append((t, h, hits[0]))
        (ta, ha, (ia, sa, la)), (tb, hb, (ib, sb, lb)) = out
        grade = re.match(r'^(`\[[A-Z]+\]`)', la)
        print(f'{label}')
        print(f'  {ta} (file {ha[:12]}) line {ia}, in "{sa}"')
        print(f'  {tb} (file {hb[:12]}) line {ib}, in "{sb}"')
        print(f'  leading grade tag: {grade.group(1) if grade else "none on the line"}; '
              f'entry text identical at both tags: {norm(la) == norm(lb)}')


if __name__ == '__main__':
    main(sys.argv[1])
