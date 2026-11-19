# HHO — receipt and full-input rerun of the co-owner's W6/W7 and C₃ × F₂₀ replay (Claude)

**Date:** 19 Nov 2026. **Level:** `[SESSION]`. Receipt of outside files and a rerun by the scientific owner. It adopts nothing, creates no RID and changes no grade.

## 1. What was received

The PI attached the ChatGPT session package `HHO_WITT_REPLAY_W67_F20_CHATGPT_SESSION.zip` to the Claude HHO session on 19 Nov 2026.

**The ZIP.** SHA-256 `a0847e71ebe5b4c3a80bd51964e882809b50c4330634b902384868f69150e5f5`. This is the value the co-owner stated before sending the file. It has ten members.

**Placed in this branch unchanged (byte-identical to the ZIP members):**

| Path | SHA-256 |
|---|---|
| `records/hho/HHO_WITT_REPLAY_W67_F20_CHATGPT.md` | `4d84bcd09f94b18c2bbee35dc4b60ca8dae5b19ba70c041ea6906857fbf64007` |
| `evidence/hho/d-witt/hho_witt_w67_eisenstein_chatgpt.py` | `ca88a0d0df89686288fd08fcd01af62c0abdcfe4ff8e730a01f8566ca161d6d9` |
| `evidence/hho/d-witt/hho_witt_w67_eisenstein_chatgpt_out.txt` (the co-owner's run on extracted fixtures) | `0abda1f04101b30392e01df9fabb62ebbeeed79f556ca1815341b8abf53d40a5` |
| `evidence/hho/d-witt/hho_witt_f20_orbit_chatgpt.py` | `f1b9b2ee8e8c2384be7286518f602a33b39f5d5e0a9306d095a2bd486d9bc54b` |
| `evidence/hho/d-witt/hho_witt_f20_orbit_chatgpt_out.txt` | `8a765c0687f3848dee8334d1688a1d18343a2d20e96016229865afae989aeccc` |

**These four hashes agree with the co-owner's index** (`SHA256SUMS_CHATGPT_REPLAY.txt` in the ZIP, SHA-256 `3dca239457f4284fc16db92f27a3cabfae065132ddb1d1ddad545f35d3a27323`). Their rows are added to `evidence/hho/d-witt/SHA256SUMS`. The co-owner's index itself is not placed, because the folder index replaces it.

**Not placed:**
- `evidence/hcg/g34/g34_cert_W6_comb.json` and `…_W7_comb.json` from the ZIP. These are the extracted fixtures: 549 and 543 bytes, with SHA-256 `7c424151…` and `f4c0edc6…`, holding only `roots` and `curves`. They are **not** the HCG files of the same path (`ae904878…`, `45097b30…`). Placing them would overwrite HCG evidence.
- `evidence/hho/outputs/a4_direct_out.txt` and `evidence/hho/code/a4_direct.py` from the ZIP. They are byte-identical to the files on `main` (`8d54d662…`, `cd548934…`), so nothing changes.

## 2. Full-input rerun (closes the co-owner's open step)

The co-owner's record (§2) left one step open: the W6/W7 script had run only on the extracted fixtures, not on the original JSON files.

**The rerun.**
- **Setup:** a clone of `main` at `c5d1e9e`; Python 3.13.18; `python3 -I`; default mode, which enforces the full-file SHA-256 of both original certificates.
- **Commands:**
  - `python3 -I evidence/hho/d-witt/hho_witt_w67_eisenstein_chatgpt.py`: both input hashes PASS.
  - `python3 -I evidence/hho/d-witt/hho_witt_f20_orbit_chatgpt.py`.
- **W6 and W7:** certificate edges 102, vertices 98, w = 4; planar min/max 4/4; witnesses (76, 72); product one and V^G = 0 PASS.
- **Output.** `evidence/hho/d-witt/hho_witt_w67_eisenstein_chatgpt_fullinput_out.txt` (SHA-256 `a456beb9c26b0c00f248c9c585756443a0b134c2b57f80663022a169ef403cb8`).
  - It differs from the co-owner's fixture output **only in the header lines**: the mode line and the two "input SHA-256 PASS" lines.
  - Every numerical line is identical.
- **F₂₀:** the rerun reproduces `hho_witt_f20_orbit_chatgpt_out.txt` byte for byte.

**Independence check.**
- Both scripts import only the standard library.
- They read only these files: the two HCG certificates, `a4_direct_out.txt`, and `a4_direct.py`, which is read as text and not imported.
- Neither touches `witt_gate_planar_claude.py` or any HCG engine.
- The F₂₀ method (orbit and stabilizer counts in C₃ × AGL(1,5), checked by character averages) shares no step with Claude's matrix programme.

## 3. Consequence for the register (the PI decides)

`HHO-NUM-WITT-PLANAR-SINGLE` now has two implementations, both run on the original inputs, with no disagreement. **In `hho-v0.5` it stays PROPOSED.**

A change to CHECKED (two implementations) belongs to a later HHO edition and needs the PI's decision. It could be merged with `HHO-NUM-WITT-PLANAR`, since the two rows would then have the same state.

Unchanged:
- `HHO-COR-WITT-GATE` keeps its conditional grade.
- `HHO-OPEN-WITT-SOURCE` stays open; the LIT request is waiting.
