# H3 — G34 W6/W7 Independent Exact Cross-Review v0.1

**22 October 2026 · SESSION-ALG · ChatGPT independent numerical/symbolic recomputation, not PI adoption**

## Input manifest
- `G34_W6_W7_PACKET_v0_1.zip` and `H3_G34_W6_W7_WITNESS_ADDENDUM_CLAUDE_v0_1.md` read. Two certificate JSONs, root lists, and accompanying research scripts were inspected. The Claude main calculation engine was **not imported or executed**.
- Common inputs from the submitted certificates: generating roots and their 8 parabolic cocycle coordinates. Independent reconstruction uses exact rational pairs in K=Q(ω), ω²+ω+1=0.
- Reused independent ChatGPT algorithms developed for W5: fraction-based K arithmetic, elementary Hurwitz/Artin braid update, paired-relative-cup formula, Hermitian principal-minor criteria. This constitutes independent implementation but shares the certificate's root and chosen basis inputs; not a second geometric principle for identifying the cup pairing.

## Verification results

| Check | W6 | W7 |
|---|---:|---:|
| All 17 T_j recomputed from individual elementary braid moves (not closed interval formula) | 17/17 exact | 17/17 exact |
| All N_j = T_j-I | PASS | PASS |
| N_j N_k = 0 for all 289 ordered pairs | PASS | PASS |
| dim_K(sum im N_j) | 4 | 4 |
| I isotropic for S and N_j(I)=0 | PASS | PASS |
| 17 Hermitian β_j individually negative semidefinite, all principal minors exact | PASS | PASS |
| sum β_j negative definite, leading principal minors | (-57, 2871, -121824, 3746331) | (-234, 10008, -306774, 12331116) |
| dim_Q span of 17 N_j (real/rational flattening) | 16 | 16 |
| Direct paired-cocycle cup construction = claimed Gram S | 64/64 | 64/64 |
| Cup descends across coboundary radical (both slots) | PASS | PASS |
| h=(1+2ω)S: exact signature | (4,4) | (4,4) |
| det h | 531441/4 = (729/2)^2 | 531441 = 729² |
| Norm class | [1] | [1] |

Every interval has odd left endpoint and even right endpoint and k=1; every such interval product of paired involutions is the identity. This certifies the asserted combinatorial H0 pants case at the level of the paired tuple; full geometric realization belongs to G34-D.

## Qualification
- The scripts use **the supplied cocycle quotient basis**, but compute its coboundary complement/gauge from scratch and reconstruct all 17 T matrices from root reflections and elementary braid moves. Their matches are exact equality of all 8×8 entries.
- The cup construction is algorithmically independent of Claude's engine, **not principle-independent** of the paired relative-cup calculation. W5's separate Dettweiler–Wewers cross-check supports the method, but this report does not repeat the DW primary-source derivation for W6/W7.
- Verified H2/H3 are from independently recomputed certificate matrices and exact Hermitian inequalities; geometric positive plumbing directions remain unverified.
- No Hurwitz braid orbit equivalence/non-equivalence test was completed. W5, W6, W7 being from distinct searches does **not** prove distinct Hurwitz components.
- The statement that H4 depends on the boundary decomposition is supported by Claude's balanced-versus-comb scan, **not independently reproduced** in this review (only the two comb certificates were supplied as exact witnesses).
- This is a finite algebraic witness check; it is not an independent proof of G34-D or of Severn Theorem 6.2.

## Proposed status
- `G34-C-W6-ALG`: CHECKED (exact certificate and direct braid reconstruction).
- `G34-C-W7-ALG`: CHECKED (same scope).
- `G34-C-COMPONENT`: OPEN.
- `G34-D`: EXPERT-SIGNOFF-PENDING, unchanged.
- `H3-PO-5`: CONDITIONAL-HOLD, unchanged.
- `H3-THM6.2`: CLAIMED, not ESTABLISHED, unchanged.
- PI ACCEPTED column remains blank.
