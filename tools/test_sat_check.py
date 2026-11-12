#!/usr/bin/env python3
"""Tests for sat_check.py: a clean fixture passes, and each planted defect is reported at the
intended level. Every test builds its own throw-away git repository.

usage: python3 tools/test_sat_check.py
"""
import contextlib
import datetime
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sat_check  # noqa: E402

TODAY = datetime.date(2026, 11, 20)

REGISTRY = """# Registry

| Key | Study | Owners | Layout | Governing edition | RTG inputs (pinned tags) | LIT consumer | Transfer rule |
|---|---|---|---|---|---|---|---|
| `coil` / COIL | a study | owners | layout | `coil-v0.9` — adopted; previous: `coil-v0.8` | `dyad-v6.4.23` | admitted | — |
| `abc` / ABC | another study | owners | layout | `abc-v0.10` — adopted; inputs pinned at `coil-v0.8` | none | admitted | — |
"""

ITEM = """---
from: COIL
to: ABC
date: 2026-11-10
kind: question
object: something in abc/ABC.md
tags: [coil-v0.9]
state: open
---
A short question.
"""


def git(repo, *args):
    env = dict(os.environ, GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@example.invalid',
               GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@example.invalid',
               GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)
    return subprocess.run(['git', '-C', repo] + list(args), check=True, env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode().strip()


def write(repo, path, text):
    full = os.path.join(repo, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


class Fixture:
    """A small rtg-sat look-alike: study `coil` with legacy tags v0.8 and v0.9, study `abc`
    with template tags v0.9 and v0.10 (0.10 must sort after 0.9)."""

    def __init__(self):
        self.repo = tempfile.mkdtemp(prefix='satcheck-')
        git(self.repo, 'init', '-q', '-b', 'main')
        write(self.repo, 'REGISTRY.md', REGISTRY)
        write(self.repo, 'pipes/ABC/20261110-COIL-a-question.md', ITEM)
        self.commit('base')
        self.release('coil', '0.8', '# COIL v0.8 — release record: RM-04 design draft\n', template=False, with_hash=True)
        self.release('coil', '0.9', '# COIL v0.9 — release record\n', template=False, with_hash=False)
        self.release('abc', '0.9', '# ABC v0.9 — release record\n')
        self.release('abc', '0.10', '# ABC v0.10 — release record\n')

    def commit(self, message):
        git(self.repo, 'add', '-A')
        git(self.repo, 'commit', '-q', '--allow-empty', '-m', message)
        return git(self.repo, 'rev-parse', 'HEAD')

    def release(self, key, version, record_text, template=True, with_hash=True, stated_hash=None, drop=None, payload=None):
        path = 'records/%s/%s_v%s_RELEASE_RECORD.md' % (key, key.upper(), version)
        write(self.repo, path, record_text)
        payload_commit = self.commit('%s v%s payload' % (key, version))
        merge_commit = self.commit('%s v%s publication' % (key, version))
        h = stated_hash or sha(record_text)
        if template:
            lines = [
                'Release record: %s' % path,
                'Release record SHA-256: %s' % h,
                'Approved payload commit: %s' % (payload or payload_commit),
                'Publication merge commit: %s' % merge_commit,
                'PI adoption: 2026-11-12, release record §1',
            ]
            if drop:
                lines = [l for l in lines if not l.startswith(drop + ':')]
            message = '%s v%s\n\n%s\n' % (key, version, '\n'.join(lines))
        elif with_hash:
            message = '%s v%s\n\nRelease record: %s\nRelease record SHA-256: %s\n' % (key, version, path, h)
        else:
            message = '%s v%s. Adoption record: %s\n' % (key, version, path)
        git(self.repo, 'tag', '-a', '%s-v%s' % (key, version), '-m', message)

    def run(self, corpus=None):
        return sat_check.run(self.repo, corpus, TODAY)

    def close(self):
        shutil.rmtree(self.repo, ignore_errors=True)


def rows(rep, level, check=None):
    return [r for r in rep.rows if r[0] == level and (check is None or r[1] == check)]


def has(rep, level, check, fragment):
    return any(fragment in r[2] + ': ' + r[3] for r in rows(rep, level, check))


class SatCheckTests(unittest.TestCase):
    def setUp(self):
        self.fx = Fixture()
        self.addCleanup(self.fx.close)

    def test_clean_fixture_has_no_errors_or_warnings(self):
        rep = self.fx.run()
        self.assertEqual(rows(rep, 'ERROR'), [])
        self.assertEqual(rows(rep, 'WARN'), [])
        self.assertTrue(has(rep, 'INFO', 'registry', 'abc: governing tag abc-v0.10'))

    def test_version_order_is_numeric_not_textual(self):
        tags = sat_check.tags_by_study(self.fx.repo)
        self.assertEqual(tags['abc'][-1][1], 'abc-v0.10')

    def test_check_is_read_only(self):
        before = git(self.fx.repo, 'status', '--porcelain'), git(self.fx.repo, 'for-each-ref')
        self.fx.run()
        after = git(self.fx.repo, 'status', '--porcelain'), git(self.fx.repo, 'for-each-ref')
        self.assertEqual(before, after)

    # --- registry ---
    def test_registry_lagging_behind_newest_tag_is_error(self):
        write(self.fx.repo, 'REGISTRY.md', REGISTRY.replace('`abc-v0.10` — adopted', '`abc-v0.9` — adopted'))
        self.assertTrue(has(self.fx.run(), 'ERROR', 'registry', 'newest published tag is abc-v0.10'))

    def test_registry_ahead_of_publication_is_warning_only(self):
        write(self.fx.repo, 'REGISTRY.md', REGISTRY.replace('`abc-v0.10` — adopted', '`abc-v0.11` — adopted'))
        rep = self.fx.run()
        self.assertTrue(has(rep, 'WARN', 'registry', 'abc-v0.11, which is not published yet'))
        self.assertEqual(rows(rep, 'ERROR', 'registry'), [])

    def test_tagged_study_without_registry_row_is_error(self):
        self.fx.release('zzz', '0.1', '# ZZZ v0.1 — release record\n')
        self.assertTrue(has(self.fx.run(), 'ERROR', 'registry', 'zzz: tags exist'))

    # --- tags ---
    def test_wrong_record_hash_in_tag_message_is_error(self):
        self.fx.release('abc', '0.11', '# ABC v0.11 — release record\n', stated_hash='0' * 64)
        self.assertTrue(has(self.fx.run(), 'ERROR', 'tag', 'abc-v0.11: tag message states record SHA-256'))

    def test_new_tag_missing_a_template_line_is_error(self):
        self.fx.release('abc', '0.11', '# ABC v0.11 — release record\n', drop='PI adoption')
        self.assertTrue(has(self.fx.run(), 'ERROR', 'tag', 'abc-v0.11: tag message lacks the line(s): PI adoption'))

    def test_new_tag_with_unknown_payload_commit_is_error(self):
        self.fx.release('abc', '0.11', '# ABC v0.11 — release record\n', payload='1' * 40)
        self.assertTrue(has(self.fx.run(), 'ERROR', 'tag', 'Approved payload commit'))

    def test_legacy_tag_without_hash_is_info_not_error(self):
        rep = self.fx.run()
        self.assertTrue(has(rep, 'INFO', 'tag', 'coil-v0.9: legacy tag'))
        self.assertEqual(rows(rep, 'ERROR', 'tag'), [])

    def test_legacy_tag_with_wrong_stated_hash_is_still_error(self):
        git(self.fx.repo, 'tag', '-d', 'coil-v0.8')
        git(self.fx.repo, 'tag', '-a', 'coil-v0.8', '-m',
            'coil v0.8\n\nRelease record: records/coil/COIL_v0.8_RELEASE_RECORD.md\nRelease record SHA-256: %s\n' % ('0' * 64))
        self.assertTrue(has(self.fx.run(), 'ERROR', 'tag', 'coil-v0.8: tag message states record SHA-256'))

    def test_lightweight_tag_is_error(self):
        write(self.fx.repo, 'records/abc/ABC_v0.11_RELEASE_RECORD.md', '# ABC v0.11 — release record\n')
        self.fx.commit('abc v0.11')
        git(self.fx.repo, 'tag', 'abc-v0.11')
        self.assertTrue(has(self.fx.run(), 'ERROR', 'tag', 'abc-v0.11: not an annotated tag'))

    def test_missing_release_record_at_tag_is_error(self):
        self.fx.commit('no record')
        git(self.fx.repo, 'tag', '-a', 'coil-v0.7', '-m', 'coil v0.7')
        self.assertTrue(has(self.fx.run(), 'ERROR', 'tag', 'coil-v0.7: release record'))

    # --- pipes ---
    def item(self, name='20261110-COIL-x.md', inbox='ABC', **changes):
        text = ITEM
        for old, new in changes.items():
            text = text.replace(*new) if isinstance(new, tuple) else text
        write(self.fx.repo, 'pipes/%s/%s' % (inbox, name), text)

    def test_bad_kind_is_error(self):
        self.item(a=('kind: question', 'kind: memo'))
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pipes', "kind='memo'"))

    def test_item_in_wrong_inbox_is_error(self):
        self.item(inbox='COIL')
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pipes', 'filed under COIL/ but to=ABC'))

    def test_filename_sender_mismatch_is_error(self):
        self.item(name='20261110-ABC-x.md')
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pipes', 'filename FROM differs'))

    def test_filename_date_mismatch_is_error(self):
        self.item(name='20261111-COIL-x.md')
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pipes', 'filename date differs'))

    def test_closed_without_disposition_is_error(self):
        self.item(a=('state: open', 'state: closed'))
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pipes', 'state closed needs a disposition'))

    def test_disposition_on_open_item_is_error(self):
        self.item(a=('state: open', 'state: open\ndisposition: 2026-11-11 · accept · records/abc/X.md'))
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pipes', 'a disposition is present but state is open'))

    def test_valid_disposition_passes(self):
        self.item(a=('state: open', 'state: closed\ndisposition: 2026-11-11 · accept with change · records/abc/X.md'))
        self.assertEqual(rows(self.fx.run(), 'ERROR', 'pipes'), [])

    def test_unknown_sat_tag_is_error(self):
        self.item(a=('tags: [coil-v0.9]', 'tags: [coil-v0.99]'))
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pipes', 'tag coil-v0.99 does not exist'))

    def test_rtg_tag_and_rtg_sender_are_accepted(self):
        text = ITEM.replace('from: COIL', 'from: DYAD').replace('tags: [coil-v0.9]', 'tags: [dyad-v6.4.24]')
        write(self.fx.repo, 'pipes/ABC/20261110-DYAD-new-tag.md', text)
        self.assertEqual(rows(self.fx.run(), 'ERROR', 'pipes'), [])

    def test_unknown_sender_is_error(self):
        text = ITEM.replace('from: COIL', 'from: NOBODY')
        write(self.fx.repo, 'pipes/ABC/20261110-NOBODY-x.md', text)
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pipes', "from='NOBODY'"))

    def test_open_item_age_is_info(self):
        self.assertTrue(has(self.fx.run(), 'INFO', 'pipes', 'open for 10 day(s)'))

    # --- record titles ---
    def test_draft_status_in_adopted_title_is_warning(self):
        write(self.fx.repo, 'records/coil/COIL_v0.9_RELEASE_RECORD.md', '# COIL v0.9 — release record (DRAFT, maintenance)\n')
        rep = self.fx.run()
        self.assertTrue(has(rep, 'WARN', 'record', 'COIL_v0.9_RELEASE_RECORD.md'))
        self.assertEqual(rows(rep, 'ERROR', 'record'), [])

    def test_design_draft_in_title_is_not_a_status_warning(self):
        # coil-v0.8 in the fixture is titled "… RM-04 design draft"
        self.assertFalse(has(self.fx.run(), 'WARN', 'record', 'COIL_v0.8'))

    # --- pins ---
    def test_older_satellite_pin_is_info_only(self):
        rep = self.fx.run()
        self.assertTrue(has(rep, 'INFO', 'pin', 'abc: pinned at coil-v0.8; newer source tag available: coil-v0.9'))
        self.assertEqual(rows(rep, 'ERROR', 'pin') + rows(rep, 'WARN', 'pin'), [])

    def test_pin_on_unpublished_tag_is_error(self):
        write(self.fx.repo, 'REGISTRY.md', REGISTRY.replace('pinned at `coil-v0.8`', 'pinned at `coil-v0.3`'))
        self.assertTrue(has(self.fx.run(), 'ERROR', 'pin', 'coil-v0.3, which is not a published tag'))

    def test_rtg_pins_without_corpus_are_reported_as_not_checked(self):
        self.assertTrue(has(self.fx.run(), 'INFO', 'pin', 'RTG pins not checked'))

    def test_rtg_pins_against_a_corpus_clone(self):
        corpus = tempfile.mkdtemp(prefix='satcheck-corpus-')
        self.addCleanup(shutil.rmtree, corpus, True)
        git(corpus, 'init', '-q', '-b', 'main')
        git(corpus, 'commit', '-q', '--allow-empty', '-m', 'c')
        git(corpus, 'tag', '-a', 'dyad-v6.4.23', '-m', 'x')
        self.assertTrue(has(self.fx.run(corpus), 'INFO', 'pin', 'dyad-v6.4.23 is the newest tag'))
        git(corpus, 'tag', '-a', 'dyad-v6.4.24', '-m', 'x')
        rep = self.fx.run(corpus)
        self.assertTrue(has(rep, 'INFO', 'pin', 'newer source tag available: dyad-v6.4.24'))
        self.assertEqual(rows(rep, 'ERROR', 'pin'), [])

    def test_rtg_pin_unknown_to_corpus_is_error(self):
        corpus = tempfile.mkdtemp(prefix='satcheck-corpus-')
        self.addCleanup(shutil.rmtree, corpus, True)
        git(corpus, 'init', '-q', '-b', 'main')
        git(corpus, 'commit', '-q', '--allow-empty', '-m', 'c')
        git(corpus, 'tag', '-a', 'dyad-v6.4.20', '-m', 'x')
        self.assertTrue(has(self.fx.run(corpus), 'ERROR', 'pin', 'RTG pin dyad-v6.4.23 is not a tag'))

    # --- exit status ---
    def test_exit_status(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(sat_check.main(['--repo', self.fx.repo, '--today', '2026-11-20']), 0)
            write(self.fx.repo, 'REGISTRY.md', REGISTRY.replace('`abc-v0.10` — adopted', '`abc-v0.9` — adopted'))
            self.assertEqual(sat_check.main(['--repo', self.fx.repo, '--today', '2026-11-20']), 1)


if __name__ == '__main__':
    unittest.main(verbosity=1)
