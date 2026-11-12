# SAT branch inventory — 12 Nov 2026

**Purpose:** machine-verified list of the remote branches of `MustafaAksu/rtg-sat`, made before any branch clean-up. It deletes nothing and authorizes nothing. Deleting branches needs the PI's explicit authorization, given separately.

**Taken at:** `main` = `bbd3ddec625bc565a7df2dca340856ddf1637a97`; 62 pull requests read from the GitHub API; 64 branches besides `main`.

**Classes.**
- **candidate** — the branch has a merged pull request, no open one, and its head commit is an ancestor of `main`. Deleting it loses no commit: every commit is reachable from `main`, and the pull request page stays.
- **review by hand** — none of the other classes applies; check before doing anything.
- **closed unmerged PR (keep)** — its commits are not on `main`. Deleting the branch would leave them reachable only through the pull request ref.
- **open PR (keep)** and **upload (keep)** — out of scope of the first clean-up.

| Class | Count |
|---|---|
| candidate | 54 |
| closed unmerged PR (keep) | 1 |
| open PR (keep) | 4 |
| upload (keep) | 5 |
| **Total** | **64** |

**Before deleting a candidate**, re-check at that moment that its head is still the SHA listed here and is still an ancestor of `main`. A branch that has moved since this inventory is not a candidate.

| Class | Branch | Head SHA | Pull request(s) | Head is ancestor of `main` | Commits not on `main` | Head = merged PR head |
|---|---|---|---|---|---|---|
| candidate | `chatgpt/coil-adoption-20261109` | `9884fcec7cb7cc9bf98c99e54819364d41adcc21` | #11 merged | yes | 0 | yes |
| candidate | `chatgpt/coil-intake-pr3` | `6fd37ab66dc8f17e4557dff7be9e6741f96676a7` | #4 merged | yes | 0 | yes |
| candidate | `chatgpt/coil-migration-review-20261109` | `47a90f316965399db9ca8942a66f215bcb572b95` | #9 merged | yes | 0 | yes |
| candidate | `chatgpt/hho-b1-o1-o2-proof-20261112` | `aef96ec2c77415aa8d51bfbc053993647090b0e3` | #49 merged | yes | 0 | yes |
| candidate | `chatgpt/hho-c6-mod2-independent-20261112` | `8d747b2bc62dd0c966f01994d0f3a6b11d7738bb` | #59 merged | yes | 0 | yes |
| candidate | `chatgpt/hho-p1-original-review-20261111` | `c913912a484acb4be46f9b7f847ab16e90d9bfaf` | #46 merged | yes | 0 | yes |
| candidate | `chatgpt/hho-posdefect-projector-gluing-20261112` | `1d9a59031f8585ca8ac1a9d5cd85fa7e6ca87ebe` | #56 merged | yes | 0 | yes |
| candidate | `chatgpt/hho-pr35-scoped-fixes-20261111` | `cb0b8a74460c427e7a9d8386d2e4766d9ad2224a` | #38 merged | yes | 0 | yes |
| candidate | `claude/coil-batch0-plan` | `d5c3c51162b4e51331d82b9094802e52d5b76c7c` | #2 merged | yes | 0 | yes |
| candidate | `claude/coil-batch1-index-charter` | `5f98540515ed74ee05bac83afb65df53982a3b53` | #5 merged | yes | 0 | yes |
| candidate | `claude/coil-batch2-rmt-records` | `899e75f5dc46794176313975dda664a5f2308d14` | #6 merged | yes | 0 | yes |
| candidate | `claude/coil-batch3-prereg-run` | `1be8cf587a9d19b378326fcc15f797f3baf19146` | #7 merged | yes | 0 | yes |
| candidate | `claude/coil-batch4-audits-code` | `f4058ab3f5c93503959febe966ffb7edd3add560` | #8 merged | yes | 0 | yes |
| candidate | `claude/coil-clusteroffset-v1.0-lock` | `6c634b9fc0fe728bc895409e95b223e9d4a6fb4a` | #42 merged | yes | 0 | yes |
| candidate | `claude/coil-clusteroffset-v1.0-run` | `148227eed14516e5e92c8b9810e598ef479d5e88` | #48 merged | yes | 0 | yes |
| candidate | `claude/coil-followup-markers-manifests` | `91c5c4fc961fac806300be85a7d82a2cf89b88ae` | #10 merged | yes | 0 | yes |
| candidate | `claude/coil-icid-v1.0-lock` | `4d2e67764865a183a04df31091a1cfb84eac64e7` | #22 merged | yes | 0 | yes |
| candidate | `claude/coil-icid-v1.0-run` | `41eed4da2fb822aa52c2f2109d590a7fd86470dd` | #30 merged | yes | 0 | yes |
| candidate | `claude/coil-rm04-analytic-start` | `cfeb02ac2ae7318ebbc3060cf5857cd3b45c898a` | #32 merged | yes | 0 | yes |
| candidate | `claude/coil-synthesis-source-package` | `58ee41077e8b0b1071aee98e38827dce0dec1ae7` | #39 merged | yes | 0 | yes |
| candidate | `claude/coil-v0.4-maintenance` | `a00824d695a0b36b9d7b4066d534055b411d3b90` | #13 merged | yes | 0 | yes |
| candidate | `claude/coil-v0.5-pairbc-scope-spectrum` | `9350e8d0794e71b081b51d2473dd3c9f9510447a` | #19 merged | yes | 0 | yes |
| candidate | `claude/coil-v0.7-adoption` | `fddc83efbe388c4f5608faf2cf5005ee0a2a8af8` | #37 merged | yes | 0 | yes |
| candidate | `claude/hcg-batch2-charter-ledger-manifest` | `526b50e3139c5a413f1d6cf440f8ace358228030` | #21 merged | yes | 0 | yes |
| candidate | `claude/hcg-batch3-evidence-placement` | `48d5de0d94872ee573125fa9c30e50bdd8636912` | #23 merged | yes | 0 | yes |
| candidate | `claude/hcg-batch4-v0.2-release-record` | `5d365c156c2fc0a94763c519fe70e55e507f0d7e` | #24 merged | yes | 0 | yes |
| candidate | `claude/hcg-d27-core-matrix` | `d74f6cc023c594181360b83ae1bd5abcadb45322` | #36 merged | yes | 0 | yes |
| candidate | `claude/hcg-d27-d6-matrix` | `63f973154352849d7840c3e3aab2005ef10b5f92` | #44 merged | yes | 0 | yes |
| candidate | `claude/hcg-d27-lemma-e-matrix` | `b0f48491a60f0489b55bf07c9a61190344293551` | #47 merged | yes | 0 | yes |
| candidate | `claude/hcg-d27-reflection-dichotomy-matrix` | `623003d74baaccd35e7ee5cacc61d425bff22a6d` | #50 merged | yes | 0 | yes |
| candidate | `claude/hcg-hho-interface-items` | `75daabfb7114d7bbf518bcd6a5d8a5a9d7b6a897` | #25 merged | yes | 0 | yes |
| candidate | `claude/hcg-rtg-import-audit` | `16203e2afb0aeb80274fa33fafc7eb7eff2b9485` | #29 merged | yes | 0 | yes |
| candidate | `claude/hcg-v0.3-d24-d26-matrix` | `7c4bacd4c60249f948f15ecc5cd497b6137687ec` | #27 merged | yes | 0 | yes |
| candidate | `claude/hcg-v0.3-ledger-draft` | `5c97019914a2c2fabd89adc3987b6f65a2c81064` | #31 merged | yes | 0 | yes |
| candidate | `claude/hcg-v0.3-notice-maintenance` | `e2fd0dfd4806b2217e06e41067c8bd9b500cf251` | #34 merged | yes | 0 | yes |
| candidate | `claude/hcg-v0.4-ledger-draft` | `3f2f7528abbd731b27e886fa1125c6dcc4e763e9` | #40 merged | yes | 0 | yes |
| candidate | `claude/hcg-v0.4-notice-maintenance` | `e2afcfa0046b11ea4d01a9d1b0c9e15376fcb5e8` | #43 merged | yes | 0 | yes |
| candidate | `claude/hcg-v0.5-ledger-draft` | `88771833beb00e3ac085278b38f4067d583dabca` | #53 merged | yes | 0 | yes |
| candidate | `claude/hcg-v0.5-notice` | `ac6f0d6e17df9f9f8014266c7ea50c03e58149cf` | #57 merged | yes | 0 | yes |
| candidate | `claude/hho-b1-o1-o2-review` | `9cbd59583c1fa88e9a99b6726c7f48442176af31` | #51 merged | yes | 0 | yes |
| candidate | `claude/hho-batch0-plan` | `eeb2822fb595e985368262c2095c3bb6b2cf908f` | #15 merged | yes | 0 | yes |
| candidate | `claude/hho-batch1-charter` | `e117f753b3753fe39cb29a17efb0f2dee5148a93` | #26 merged | yes | 0 | yes |
| candidate | `claude/hho-batch2-evidence` | `d0e90c4d5b29a1ffac6cfe65f5a2e83cf9b628c5` | #33 merged | yes | 0 | yes |
| candidate | `claude/hho-batch3-live` | `7156ca15fcde70f6bd79d46f7be747b38b6fd071` | #35 merged | yes | 0 | yes |
| candidate | `claude/hho-migration-note` | `e92e5051f58dd3720bf9b27399a56387c2991758` | #14 merged | yes | 0 | yes |
| candidate | `claude/hho-p1-source-review` | `49745d0843d1f63580d701886ba88416d81fa038` | #45 merged | yes | 0 | yes |
| candidate | `claude/hho-pipe-b2-question` | `a17da7ef1a50a094f2d3cb438e825877ab7cd5d7` | #54 merged | yes | 0 | yes |
| candidate | `claude/hho-posdefect-review` | `93b5ca9374474992525018a6099a97872ad99e38` | #58 merged | yes | 0 | yes |
| candidate | `claude/hho-v0.1-release` | `a02fd5a462f3c55804397454ceb624d92de2ff25` | #28 merged | yes | 0 | yes |
| candidate | `claude/hho-v0.2-release` | `b7f2b45555c4ce41b954ae7ad81361e3934b8b51` | #41 merged | yes | 0 | yes |
| candidate | `claude/hho-v0.3-b1` | `d796f1943cb949374091bb8fddbb1c3dd69edb60` | #55 merged | yes | 0 | yes |
| candidate | `claude/lit-consumer-admission-reply` | `cb564b17986c116933a8b6d2d974b950e6d0381b` | #17 merged | yes | 0 | yes |
| candidate | `claude/sat-bootstrap` | `39e0a7411d693caa832de0bb842af14ead0f150e` | #1 merged | yes | 0 | yes |
| candidate | `claude/sat-conventions-v1` | `1ee6edf25eae6ad18db386e7dd14ce2c8bc6e044` | #12 merged | yes | 0 | yes |
| closed unmerged PR (keep) | `chatgpt/hcg-migration-preparation-20261110` | `1366c58d4af8abf4246ca5fe97f0175434a0fecf` | #18 closed | no | 6 | n/a |
| open PR (keep) | `claude/coil-phase25-preconditions` | `dbc3a190f204be8ff008c2c49c7d5aa9c4d5bb66` | #62 open | no | 1 | n/a |
| open PR (keep) | `claude/coil-synthesis-signature-plan` | `853aab713caa0e8e2f170abbf02a9b80692c2cec` | #52 open | no | 7 | n/a |
| open PR (keep) | `claude/hcg-open8-line-review` | `0f7034920fcdf9441c947dcb3246ce1eb1d1ebe7` | #61 open | no | 1 | n/a |
| open PR (keep) | `claude/hho-posdefect-f20` | `51c51b78afb9595aadae6ab47a3b21fcc7c59ae9` | #60 open | no | 1 | n/a |
| upload (keep) | `upload/coil-clusteroffset-results` | `b3fa72c6da02bc19f3e2e30e3558c53b6a1e810a` | none | yes | 0 | n/a |
| upload (keep) | `upload/coil-icid-results` | `e2ccc9b1a357d5704051ff10ac5ca8153f21ec70` | none | yes | 0 | n/a |
| upload (keep) | `upload/coil-sources` | `01a262e3b1039ae394a3aca5891076cc511f22d5` | #3 merged | yes | 0 | yes |
| upload (keep) | `upload/hcg-sources` | `802a34651676800c2a6fe3b9bd178aac6c07bd6d` | #20 merged | yes | 0 | yes |
| upload (keep) | `upload/hho-sources` | `516400de9d0a8e6184e858306178713f9b6ab1e1` | #16 merged | yes | 0 | yes |
