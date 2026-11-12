# evidence/hho — frozen evidence of the HHO study

The **54 originally placed files** in `frozen/`, `code/`, `outputs/` and `received/` are byte-identical copies from `upload/hho/` (PR #16); the root `SHA256SUMS` indexes **only those 54 files**. Their mapping is in `records/hho/HHO_SOURCE_MANIFEST.md` §6. New B1 session-native files live in `b1/`, outside the frozen upload and with a separate index supplied by the B1 receiving-review package.

Frozen files are never edited. They keep their wording, including statements that were later corrected or withdrawn. The current state of every claim is in `hho/HHO_CLAIM_REGISTER.md`.

| Folder | Content | Files |
|---|---|---|
| `frozen/` | the append-only review record `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` (952 lines; prefix-hash chain in `records/hho/HHO_MIGRATION_PLAN.md` §3.1) | 1 |
| `code/` | the Claude session's scripts | 11 |
| `outputs/` | outputs of those scripts | 8 |
| `outputs/pi/` | GAP output from the PI's machine, as relayed in the conversation | 1 |
| `received/chatgpt/` | ChatGPT's reviews, proof sketch, checkers and packages, as received through the PI. The attachment-ID prefix of each name is kept. | 21 |
| `received/relays/` | the PI's relays of ChatGPT's chat messages (Turkish) | 12 |
| `b1/` | session-native B1 O1/O2 source code, independent outputs and own SHA-256 index (not 54 original frozen files) | separate |

## Not placed here

- `generic_engine.py` and `cyclic_disc_claude.py`. They are HCG inputs and are cited at `hcg-v0.2`:
  - `evidence/hcg/h4sel/p2p3/generic_engine.py`
  - `evidence/hcg/nonsplit8/cyclic_disc_claude.py`
- The migration note as pasted into the conversation. The repository copy is `records/hho/HHO_MIGRATION_NOTE.md`.

## Reading the files with care

- `code/f20_faithful.py` and `outputs/f20_faithful_out.txt`: the printed "class" divides two determinants and is **not** the class of the rank-4 system (register, HHO-WD-F20-ALLSPLIT). The 40 tuples are valid input; the correct classes are in `outputs/a4_direct_out.txt`.
- `received/chatgpt/` packages may contain copies of HCG review notes named `SOURCE_*`. Those are HCG inputs.
- `received/relays/` are chat messages. They are provenance, not results.

## Replaying a script

The scripts load the two HCG engines from the current directory. Use a scratch directory:

```
mkdir scratch && cd scratch
cp ../evidence/hcg/h4sel/p2p3/generic_engine.py ../evidence/hcg/nonsplit8/cyclic_disc_claude.py .
python3 ../evidence/hho/code/f20_check.py
```

- `a4_direct.py` takes the path of `f20_faithful_out.txt` as its argument.
- `HHO_C6_LEAF_TEST_v0_1.py` takes no argument when the engines are in the current directory.
- `HHO_G34_BLOCKS_v0_1.g` needs GAP with CTblLib.

Replayed on 11 Nov 2026 from this layout with byte-identical output: `f20_check.py` and `g616.py`. The other scripts were not replayed for the placement.
