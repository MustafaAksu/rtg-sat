#!/usr/bin/env python3
"""Read-only consistency check for the rtg-sat repository.

usage: sat_check.py [--repo PATH] [--corpus PATH] [--today YYYY-MM-DD]

  --repo PATH     the rtg-sat working tree to check (default: the repository this file is in)
  --corpus PATH   a local clone of rtg-corpus; when given, the RTG pins in REGISTRY.md are
                  compared with the newest tag of the same study there. Without it the RTG
                  pins are reported as "not checked".
  --today DATE    date used for the age of open pipe items (default: today)

The check reads REGISTRY.md, records/ and pipes/ from the working tree and reads tags
with `git`. It never writes, fetches, tags or re-pins anything.

What it checks
  1. registry   REGISTRY.md names, for every study, the newest published tag of that study.
  2. tag        every tag is annotated; its release record exists at the tag; a release
                record SHA-256 stated in the tag message equals the file at the tag. Tags
                created after the tag-message rule (CONVENTIONS.md §2) must carry its five
                lines. The tags in LEGACY_TAGS predate that rule: a missing hash line there
                is reported as INFO, never as an error.
  3. pipes      every pipe item follows the item schema of rtg-corpus/pipes/README.md, with
                the rtg-sat keys. Open items are listed with their age (INFO).
  4. record     an adopted release record whose title carries the status word DRAFT in
                parentheses is reported (WARN). The record is frozen, so this is a note for
                the next release, not something to repair.
  5. pin        a tag pinned by a study that is older than the newest tag of its source is
                reported as INFO ("newer source tag available"). Keeping an older pin is the
                owners' decision; this tool never treats it as an error.

Levels: ERROR (exit status 1), WARN, INFO. A passing check authorizes nothing.
"""
import argparse
import datetime
import os
import re
import subprocess
import sys

# Tags published before the tag-message rule of CONVENTIONS.md §2. They are not changed and
# are not judged by that rule.
LEGACY_TAGS = frozenset(
    ['coil-v0.%d' % i for i in range(1, 10)]
    + ['hcg-v0.%d' % i for i in range(2, 6)]
    + ['hho-v0.%d' % i for i in range(1, 4)]
)

TEMPLATE_FIELDS = [
    'Release record',
    'Release record SHA-256',
    'Approved payload commit',
    'Publication merge commit',
    'PI adoption',
]

# Keys that may appear as `from` in an rtg-sat pipe item besides the registered study keys.
SERVICE_KEYS = ['LIT', 'SAT']
RTG_STREAM_KEYS = ['METH', 'PROG', 'OFN', 'RRF', 'LEGACY', 'PREL', 'NUMGEN', 'DYAD', 'TRIAD', 'GEN',
                   'UVM', 'RECOG', 'DZT', 'TDRG', 'AZ', 'RER', 'FMS', 'ER2B', 'ATLAS']
KINDS = ['request', 'offer', 'finding', 'question', 'notice']
STATES = ['open', 'acknowledged', 'dispositioned', 'closed']
REQUIRED = ['from', 'to', 'date', 'kind', 'object', 'tags', 'state']
OPTIONAL = ['blocks', 'disposition', 'filed_by']
DISP_RE = re.compile(r'^(\d{4}-\d{2}-\d{2}) · (accept with change|accept|reject|defer|no action) · (.+)$')
NAME_RE = re.compile(r'^(\d{8})-([A-Z0-9]+)-[a-z0-9][a-z0-9.-]*\.md$')
POINTER_RE = re.compile(r'(records/|pipes/|evidence/|REGISTRY\.md|CONVENTIONS\.md|[a-z0-9]+/[A-Za-z0-9_.-]+\.md|[A-Z]{2,}-[A-Z0-9-]{3,})')
TAG_RE = re.compile(r'^([a-z][a-z0-9]*)-v(\d+(?:\.\d+)*)$')
BACKTICK_TAG_RE = re.compile(r'`([a-z][a-z0-9]*-v\d+(?:\.\d+)*)`')
SHA256_LINE_RE = re.compile(r'^\s*(?:Release record|Record) SHA-256:\s*([0-9a-f]{64})\s*$', re.M)
RECORD_LINE_RE = re.compile(r'^\s*(?:Release record|Record|Adoption record):\s*(\S+)\s*$', re.M)
DRAFT_TITLE_RE = re.compile(r'\([^)]*\bDRAFT\b[^)]*\)')
MAX_BODY_LINES = 40


class Report:
    def __init__(self):
        self.rows = []

    def add(self, level, check, subject, message):
        self.rows.append((level, check, subject, message))

    def count(self, level):
        return sum(1 for r in self.rows if r[0] == level)

    def render(self):
        out = []
        for level in ('ERROR', 'WARN', 'INFO'):
            for r in self.rows:
                if r[0] == level:
                    out.append('%-5s  %-8s  %s: %s' % r)
        out.append('')
        out.append('sat_check: %d error(s), %d warning(s), %d info' % (
            self.count('ERROR'), self.count('WARN'), self.count('INFO')))
        return '\n'.join(out)


def git(repo, *args):
    """Run a read-only git command; return stdout, or None when git reports failure."""
    p = subprocess.run(['git', '-C', repo] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        return None
    return p.stdout.decode('utf-8', 'replace')


def version_key(version):
    return tuple(int(x) for x in version.split('.'))


def tags_by_study(repo):
    """{study key: [(version tuple, tag name), ...] sorted oldest first}."""
    out = git(repo, 'tag', '-l')
    if out is None:
        raise RuntimeError('cannot read the tag list of %s' % repo)
    studies = {}
    for name in out.split():
        m = TAG_RE.match(name)
        if m:
            studies.setdefault(m.group(1), []).append((version_key(m.group(2)), name))
    for key in studies:
        studies[key].sort()
    return studies


def parse_registry(text):
    """Rows of the study table: {key: {'cells': [...], 'governing': tag or None}}."""
    rows = {}
    for line in text.split('\n'):
        if not line.startswith('| `'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        m = re.match(r'^`([a-z][a-z0-9]*)`', cells[0])
        if not m or len(cells) < 6:
            continue
        key = m.group(1)
        governing = None
        for tag in BACKTICK_TAG_RE.findall(cells[4]):
            if tag.startswith(key + '-v'):
                governing = tag
                break
        rows[key] = {'cells': cells, 'governing': governing}
    return rows


def check_registry(rep, rows, sat_tags):
    for key, row in sorted(rows.items()):
        published = sat_tags.get(key, [])
        newest = published[-1][1] if published else None
        gov = row['governing']
        if gov is None and newest is None:
            rep.add('INFO', 'registry', key, 'no published tag and none named in REGISTRY.md')
        elif gov is None:
            rep.add('ERROR', 'registry', key, 'REGISTRY.md names no governing tag, but %s is published' % newest)
        elif newest is None or version_key(TAG_RE.match(gov).group(2)) > published[-1][0]:
            rep.add('WARN', 'registry', key, 'REGISTRY.md names %s, which is not published yet (newest tag: %s)' % (gov, newest or 'none'))
        elif gov != newest:
            rep.add('ERROR', 'registry', key, 'REGISTRY.md names %s, but the newest published tag is %s' % (gov, newest))
        else:
            rep.add('INFO', 'registry', key, 'governing tag %s is the newest published tag' % gov)
    for key in sorted(sat_tags):
        if key not in rows:
            rep.add('ERROR', 'registry', key, 'tags exist (%s …) but the study has no row in REGISTRY.md' % sat_tags[key][0][1])


def tag_message(repo, tag):
    """(object type, message) of a tag; message is None for a lightweight tag."""
    kind = git(repo, 'cat-file', '-t', 'refs/tags/' + tag)
    if kind is None:
        return None, None
    kind = kind.strip()
    if kind != 'tag':
        return kind, None
    raw = git(repo, 'cat-file', '-p', 'refs/tags/' + tag) or ''
    head, _, message = raw.partition('\n\n')
    return kind, message


def sha256_at(repo, tag, path):
    import hashlib
    p = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (tag, path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        return None
    return hashlib.sha256(p.stdout).hexdigest()


def default_record_path(tag):
    m = TAG_RE.match(tag)
    key, version = m.group(1), m.group(2)
    return 'records/%s/%s_v%s_RELEASE_RECORD.md' % (key, key.upper(), version)


def is_commit_in(repo, sha, tag):
    """True when sha names a commit that is the tagged commit or one of its ancestors."""
    if git(repo, 'cat-file', '-e', sha + '^{commit}') is None:
        return False
    return subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', sha, tag + '^{commit}'],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0


def check_tags(rep, repo, sat_tags):
    for key in sorted(sat_tags):
        for _, tag in sat_tags[key]:
            kind, message = tag_message(repo, tag)
            if kind != 'tag':
                rep.add('ERROR', 'tag', tag, 'not an annotated tag')
                continue
            legacy = tag in LEGACY_TAGS
            fields = {}
            for line in message.split('\n'):
                for name in TEMPLATE_FIELDS:
                    if line.startswith(name + ':'):
                        fields[name] = line[len(name) + 1:].strip()
            if not legacy:
                missing = [n for n in TEMPLATE_FIELDS if not fields.get(n)]
                if missing:
                    rep.add('ERROR', 'tag', tag, 'tag message lacks the line(s): %s (CONVENTIONS.md §2)' % ', '.join(missing))
                for name in ('Approved payload commit', 'Publication merge commit'):
                    sha = fields.get(name)
                    if sha and not is_commit_in(repo, sha.split()[0], tag):
                        rep.add('ERROR', 'tag', tag, '%s %s is not the tagged commit or an ancestor of it' % (name, sha.split()[0]))
            m = RECORD_LINE_RE.search(message)
            record = m.group(1) if m else default_record_path(tag)
            actual = sha256_at(repo, tag, record)
            if actual is None:
                rep.add('ERROR', 'tag', tag, 'release record %s does not exist at the tag' % record)
                continue
            stated = SHA256_LINE_RE.search(message)
            if stated:
                if stated.group(1) != actual:
                    rep.add('ERROR', 'tag', tag, 'tag message states record SHA-256 %s…, but %s at the tag is %s…' % (stated.group(1)[:12], record, actual[:12]))
                else:
                    rep.add('INFO', 'tag', tag, 'release record hash in the tag message matches %s' % record)
            elif actual in message:
                rep.add('INFO', 'tag', tag, 'release record hash appears in the tag message and matches %s' % record)
            elif legacy:
                rep.add('INFO', 'tag', tag, 'legacy tag: its message carries no release record SHA-256 (predates the rule; not a violation)')
            # a non-legacy tag without the hash line was already reported as ERROR above


def parse_item(text):
    if not text.startswith('---\n'):
        raise ValueError('no front matter')
    end = text.find('\n---\n', 4)
    if end < 0:
        raise ValueError('front matter not closed')
    data = {}
    for line in text[4:end].split('\n'):
        if not line.strip():
            continue
        if ':' not in line:
            raise ValueError('bad front-matter line: %r' % line)
        k, v = line.split(':', 1)
        k = k.strip()
        if k in data:
            raise ValueError('duplicate field %s' % k)
        data[k] = v.strip()
    return data, text[end + 5:]


def check_pipes(rep, repo, rows, sat_tags, today):
    root = os.path.join(repo, 'pipes')
    study_keys = [k.upper() for k in rows]
    inboxes = study_keys + ['SAT']
    senders = study_keys + SERVICE_KEYS + RTG_STREAM_KEYS
    all_sat_tags = set(t for tags in sat_tags.values() for _, t in tags)
    if not os.path.isdir(root):
        rep.add('INFO', 'pipes', 'pipes/', 'no pipes directory')
        return
    for inbox in sorted(os.listdir(root)):
        folder = os.path.join(root, inbox)
        if not os.path.isdir(folder):
            continue
        if inbox not in inboxes:
            rep.add('ERROR', 'pipes', 'pipes/%s/' % inbox, 'not an inbox key (registered study keys and SAT)')
        for name in sorted(os.listdir(folder)):
            if not name.endswith('.md') or name == 'INDEX.md':
                continue
            subject = 'pipes/%s/%s' % (inbox, name)
            with open(os.path.join(folder, name), encoding='utf-8') as f:
                text = f.read()
            errors = []
            m = NAME_RE.match(name)
            if not m:
                errors.append('filename must be YYYYMMDD-<FROM>-<slug>.md')
            try:
                data, body = parse_item(text)
            except ValueError as e:
                rep.add('ERROR', 'pipes', subject, str(e))
                continue
            for k in REQUIRED:
                if not data.get(k):
                    errors.append('missing %s' % k)
            for k in data:
                if k not in REQUIRED + OPTIONAL:
                    errors.append('unknown field %s' % k)
            if data.get('from') and data['from'] not in senders:
                errors.append('from=%r is not a study, service or RTG stream key' % data['from'])
            if data.get('to') and data['to'] != inbox:
                errors.append('filed under %s/ but to=%s' % (inbox, data['to']))
            if m and data.get('from') and m.group(2) != data['from']:
                errors.append('filename FROM differs from the from field')
            date = data.get('date', '')
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
                errors.append('date must be YYYY-MM-DD')
            elif m and m.group(1) != date.replace('-', ''):
                errors.append('filename date differs from the date field')
            if data.get('kind') and data['kind'] not in KINDS:
                errors.append('kind=%r' % data['kind'])
            if data.get('state') and data['state'] not in STATES:
                errors.append('state=%r' % data['state'])
            tl = data.get('tags', '')
            if tl:
                if not (tl.startswith('[') and tl.endswith(']')):
                    errors.append('tags must be [a, b]')
                else:
                    items = [x.strip() for x in tl[1:-1].split(',') if x.strip()]
                    if not items:
                        errors.append('tags must name at least one tag')
                    for t in items:
                        tm = TAG_RE.match(t)
                        if not tm:
                            errors.append('tag %r is not of the form <study>-v<version>' % t)
                        elif tm.group(1) in rows and t not in all_sat_tags:
                            errors.append('tag %s does not exist in this repository' % t)
            disp = data.get('disposition', '')
            state = data.get('state')
            if state in ('dispositioned', 'closed') and not disp:
                errors.append('state %s needs a disposition' % state)
            if disp:
                dm = DISP_RE.match(disp)
                if not dm:
                    errors.append('disposition must read "YYYY-MM-DD · <verdict> · <pointer>"')
                elif not POINTER_RE.search(dm.group(3)):
                    errors.append('disposition pointer must name a repository path or a RID')
                if state in ('open', 'acknowledged'):
                    errors.append('a disposition is present but state is %s' % state)
            if not body.strip():
                errors.append('empty body')
            if len(body.strip().split('\n')) > MAX_BODY_LINES:
                errors.append('body longer than %d lines' % MAX_BODY_LINES)
            for e in errors:
                rep.add('ERROR', 'pipes', subject, e)
            if state in ('open', 'acknowledged') and re.match(r'^\d{4}-\d{2}-\d{2}$', date):
                try:
                    age = (today - datetime.date.fromisoformat(date)).days
                    rep.add('INFO', 'pipes', subject, '%s for %d day(s); kind %s, from %s — the receiver decides' % (state, age, data.get('kind'), data.get('from')))
                except ValueError:
                    pass


def check_record_titles(rep, repo, sat_tags):
    for key in sorted(sat_tags):
        for _, tag in sat_tags[key]:
            path = default_record_path(tag)
            full = os.path.join(repo, path)
            if not os.path.isfile(full):
                continue
            with open(full, encoding='utf-8') as f:
                for line in f:
                    if line.startswith('# '):
                        if DRAFT_TITLE_RE.search(line):
                            rep.add('WARN', 'record', path, 'title of an adopted release record still carries the status word DRAFT: %s' % line.strip())
                        break


def check_pins(rep, repo, rows, sat_tags, corpus):
    # pins on other satellite studies: any tag of another registered study named in the row
    for key, row in sorted(rows.items()):
        seen = set()
        for cell in row['cells']:
            for tag in BACKTICK_TAG_RE.findall(cell):
                m = TAG_RE.match(tag)
                other = m.group(1)
                if other == key or other not in rows or tag in seen:
                    continue
                seen.add(tag)
                published = sat_tags.get(other, [])
                if not published:
                    rep.add('WARN', 'pin', key, 'names %s, but study %s has no published tag' % (tag, other))
                elif tag not in [t for _, t in published]:
                    rep.add('ERROR', 'pin', key, 'names %s, which is not a published tag' % tag)
                elif published[-1][1] != tag:
                    rep.add('INFO', 'pin', key, 'pinned at %s; newer source tag available: %s (re-pinning is the owners\' decision)' % (tag, published[-1][1]))
    # pins on RTG: the "RTG inputs" cell
    corpus_tags = None
    if corpus:
        try:
            corpus_tags = tags_by_study(corpus)
        except RuntimeError as e:
            rep.add('WARN', 'pin', 'rtg-corpus', str(e))
    for key, row in sorted(rows.items()):
        pins = BACKTICK_TAG_RE.findall(row['cells'][5])
        if not pins:
            continue
        if corpus_tags is None:
            rep.add('INFO', 'pin', key, 'RTG pins not checked (no --corpus): %s' % ', '.join(pins))
            continue
        for tag in pins:
            m = TAG_RE.match(tag)
            published = corpus_tags.get(m.group(1), [])
            if tag not in [t for _, t in published]:
                rep.add('ERROR', 'pin', key, 'RTG pin %s is not a tag of the rtg-corpus clone given' % tag)
            elif published[-1][1] != tag:
                rep.add('INFO', 'pin', key, 'RTG pin %s; newer source tag available: %s (re-pinning is the owners\' decision)' % (tag, published[-1][1]))
            else:
                rep.add('INFO', 'pin', key, 'RTG pin %s is the newest tag of its study' % tag)


def run(repo, corpus=None, today=None):
    rep = Report()
    today = today or datetime.date.today()
    registry_path = os.path.join(repo, 'REGISTRY.md')
    if not os.path.isfile(registry_path):
        rep.add('ERROR', 'registry', 'REGISTRY.md', 'file not found in %s' % repo)
        return rep
    with open(registry_path, encoding='utf-8') as f:
        rows = parse_registry(f.read())
    if not rows:
        rep.add('ERROR', 'registry', 'REGISTRY.md', 'no study rows found')
        return rep
    try:
        sat_tags = tags_by_study(repo)
    except RuntimeError as e:
        rep.add('ERROR', 'tag', 'repository', str(e))
        return rep
    check_registry(rep, rows, sat_tags)
    check_tags(rep, repo, sat_tags)
    check_pipes(rep, repo, rows, sat_tags, today)
    check_record_titles(rep, repo, sat_tags)
    check_pins(rep, repo, rows, sat_tags, corpus)
    return rep


def main(argv=None):
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser(description='Read-only consistency check for rtg-sat.')
    ap.add_argument('--repo', default=here)
    ap.add_argument('--corpus', default=None)
    ap.add_argument('--today', default=None)
    args = ap.parse_args(argv)
    today = datetime.date.fromisoformat(args.today) if args.today else None
    rep = run(args.repo, args.corpus, today)
    print(rep.render())
    return 1 if rep.count('ERROR') else 0


if __name__ == '__main__':
    sys.exit(main())
