# Conventions — how a satellite study works in `rtg-sat`

A satellite study is inspired by RTG or related to it but is not part of the RTG programme. This page sets how such studies are kept and how they relate to `rtg-corpus` (RTG) and `rtg-lit` (LIT).

**Base rules.** Unless this page says otherwise, a satellite study follows `rtg-corpus/CONVENTIONS.md` and the DSN Methodology it points to, read at the tag `methodology-v1.4`. That covers the live file, release making, evidence and who writes where. A study may adopt a lighter layout than a DSN (for example a session ledger), stated in its `REGISTRY.md` row. Where this page and those rules differ, this page governs inside `rtg-sat`.

*Status: draft (bootstrap). In force from the merge of the pull request that introduced it, after PI adoption.*

## 1. Where things are

| What | Where | Rule |
|---|---|---|
| A study's live document(s) | `<study>/` | fixed filenames, no version in the name |
| Release records, reviews, session records | `records/<study>/` | release records are frozen at adoption |
| Scripts, outputs, evidence packages | `evidence/<study>/` | stored once; external packages kept as received |
| Files arriving from outside | `upload/<topic>` branch | unchanged, hash-checked, placed by a follow-up commit |
| Inboxes | `pipes/<KEY>/` | see §5 |
| Studies, owners, states, governing editions | `REGISTRY.md` | |

Study keys (tags and records): see `REGISTRY.md`. Keys are lowercase and do not reuse an `rtg-corpus` study key.

## 2. Which edition governs

The governing edition of a satellite study is its latest **adopted, tagged** release `<study>-v<version>` in this repository, with its release record. Order: decision → release record → merge → tag. A merge, a tag or a passing check is not an adoption. Branches: Claude sessions push only to `claude/*`; the PI merges into `main` with a merge commit and creates annotated tags. Nobody force-pushes, moves a tag or rewrites published history.

A study whose current state is only adopted at chat level, with no file in this repository, is listed in `REGISTRY.md` as such. Its first repository edition is created by bringing the files in on an `upload/<topic>` branch.

## 3. Using RTG

- A satellite study consumes RTG **only at an adopted `rtg-corpus` tag** (for example `triad-v1.6`), never at `main`. Every use names the tag, the section or RID, and the RTG grade as stated there.
- RTG grades travel unchanged. A satellite study does not upgrade an RTG result, and its own grades are not RTG grades.
- When a newer RTG edition is adopted, a satellite study keeps its pinned tag until its owners re-pin it in a release.

## 4. Flow back to RTG

- Nothing in `rtg-sat` is an RTG result. A satellite finding enters RTG only as a pipe item in the receiving stream's inbox in `rtg-corpus` (`pipes/<STREAM>/`), and only the receiver's Import Ledger row or release record makes it adopted use there.
- **Disclosure.** `rtg-corpus` and `rtg-sat` are both public (PI decision, 4 Nov 2026). Open science applies to a satellite study's own work: its research, computations, code, negative results and scientific records may be public. Source rights still apply: third-party publications, licence-restricted documents and content without permission to share are not placed in `rtg-sat`; their bibliographic identity and permitted derived analyses may be. Such material stays in `rtg-lit`, which remains private. A pipe item filed into `rtg-corpus` still states only what the satellite study's owners agree to make public, and the PI checks disclosure before relaying it; confidential information and third-party copyrighted content are not published in either repository.
- A satellite study may also have a transfer rule of its own (for example HHO → HCG); it is stated in its `REGISTRY.md` row and applies on top of this section.

## 5. Pipes inside `rtg-sat`

Items between satellite studies, and from LIT to a satellite study, go to `pipes/<KEY>/` with the item schema, states and rules of `rtg-corpus/pipes/README.md`. Keys are the uppercase study keys in `REGISTRY.md` plus the service key `LIT`. An item carries no scientific authority; the receiver decides.

## 6. Literature (LIT)

LIT (`MustafaAksu/rtg-lit`) serves the programme's own studies only: the RTG streams in `rtg-corpus` and the satellite studies registered in `REGISTRY.md`. It is not a public or community service. A study uses LIT only once it is listed in `REGISTRY.md` and LIT's own rules admit `rtg-sat` consumers.

- A source is taken into LIT once and shared. A validation or adoption by one consumer does not pass to another.
- A report of use records: consumer · source `LIT-ID@version:label` · rtg-lit commit · verification scope · owner decision.
- LIT's disclosure rules (`rtg-lit/CONVENTIONS.md`) apply to anything a satellite study publishes, as for an RTG stream.

## 7. Leaving `rtg-sat`

A study that grows its own publication line may move to its own repository with its history (`git subtree split` or `git filter-repo`), by PI decision. Its tags are recreated there with the same names. Commit and tag object hashes change under `git subtree split` or `git filter-repo`, so identity is carried by content: each release record states the SHA-256 of the files it adopts, and the moved study's first release record in the new repository lists the old tag names with their original tag object hashes next to the new ones. Its `REGISTRY.md` row then points to the new repository.
