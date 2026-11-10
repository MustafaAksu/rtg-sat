# HCG — Character-data replay and all-dimensional symplectic-type exclusion

**Date:** 30 October 2026  
**Reviewer:** ChatGPT  
**Provenance:** SESSION, independent exact replay and proof review. INTERNAL. No PI adoption, no canonical RTG/HCG file changes. Severn A/B/C remain CLAIMED.  
**Review disposition:** The remaining exact character-data checks now pass in this runtime. The 25 <= d <= 42 exclusion is CHECKED within the previously specified complex-primitive, factorwise tensor-indecomposable, not tensor-induced branch, subject to its named external classification/Weil inputs. Claude's all-dimensional symplectic-type exclusion is also proof-checked below.

## 1. Received objects and actual review extent

The complete new report and all supplied scripts were read before execution.

- Source ZIP: `H3_D42_PRIMITIVE_DATA_REPLAY_CLAUDE_v0_1.zip`, SHA-256 `8af11b4911f1a9f1eae1ccdabec1d951b022118eb88e0368f21034ab6e8c1418`.
- Source report: SHA-256 `eb306f413f79adbb3772d67672df7525ad789e606b8d59fec160f624890a9885`. The standalone and archived report bytes coincide.
- Raw CTblLib JSON: `78030350699ee7ccce0db8b5d78ec2f1db564d0080dbe815a6d8f417c58b63e3`.
- GAP exporter: `7051ea808e2e03d156dc8399944c8edb41da25aaa25c295451f0b2a4e3c49698`; identical to the previous ChatGPT package copy.
- Original ChatGPT Python verifier, recovered unchanged from the prior package: `6397d15ab0f962a6b212dfcef40dfb6d9e3652bdf1bdf49f0a24a476850a8f4a`.

All **8/8** source-manifest entries validate. The source archive was preserved; computations used an extracted copy. No GAP code was executed in this ChatGPT session. No network operation is performed by the included replay scripts.

This is a targeted completion of the previous review, not a repeated survey of 459 character tables or a reproof of Hiss–Malle classification. The previous classification, no-junior, self-dual, normal-subgroup and Weil arguments remain distinct dependencies.

## 2. Exact character replay

Ran the unchanged `verify_character_export.py` on the supplied raw JSON. It independently reconstructs each cyclic restriction by cyclotomic Fourier inversion using rational polynomial arithmetic in Q[z]/Phi_m(z). Neither GAP's previously computed moving ranks nor the target summary values are used to generate eigenvalue multiplicities.

**20/20 characters pass.** The complete output is byte-identical to Claude's `verify_out.json`, with SHA-256 `b587e3a58e10c201a2f810598e35044ec584def545d7219a13d75be35e27f9cf`.

| Group | Degree | Characters | Min moving rank | Min projective moving rank |
|---|---:|---:|---:|---:|
| 3.O7(3) | 27 | 2 | 6 | 6 |
| 3.G2(3) | 27 | 4 | 12 | 12 |
| U4(2) | 30 | 2 | 12 | 12 |
| 2.U4(2) | 36 | 2 | 18 | 18 |
| 3_2.U4(3) | 36 | 2 | 16 | 16 |
| 6.A7 | 36 | 2 | 24 | 18 |
| 6.L3(4) | 36 | 2 | 16 | 16 |
| U4(2) | 40 | 2 | 20 | 16 |
| S8(3) | 41 | 2 | 16 | 13 |

For both 3.O7(3) characters, distinct source classes 1 and 2 **in zero-based indexing** fuse in the index-two extension but have different character values. Thus the extension's nontrivial outer action does not preserve either character. These are GAP classes 2 and 3, not classes 1 and 2 in GAP indexing. The previously reviewed normalizer argument therefore applies: scalar multiples of the normal-subgroup matrices have moving rank at least 6, so the branch budget would require 19*6=114 > 62.

The unavailable 2.S8(3) degree-40 character table is **not** among these 20 characters. Its exclusion remains the source-backed Weil trace bound, with the symmetric endpoint repair independently accepted by Claude. No statement that this missing table was exported is made.

### Additional checks made in this session

A separate raw-data audit checked:

- all 9 table/degree records, unique character rows and all nonreal K-valued character vectors;
- all **9,872** power-map entries, including first-power identities and exact orders of powers;
- the scalar-class sets against `|chi(g)|^2=d^2`, and faithfulness against `chi(g)=d`;
- complex-conjugate closure of the selected character sets;
- **1,408** cyclic restrictions including central classes, comprising **20,860** eigenvalue multiplicities;
- four negative controls: corrupted degree, corrupted power map, omitted genuine scalar class, and an artificially injective outer fusion. All were rejected.

These consistency checks do not establish CTblLib data from a group presentation. Both implementations share CTblLib as input. The independence is computational: the prior GAP moving-rank calculation and this exact Python character-to-spectrum calculation are different algorithms. Running the same Python checker in two environments is a replay, not a third independent implementation.

## 3. All-dimensional symplectic-type exclusion — proof checked

### Hypotheses

Let Gamma <= GL(V) be the finite monodromy image in the inherited genus-zero feasibility setting. Write d=dim_C V, c(g)=rank(1-g). We use only the following budget facts:

    N >= 19 effective branch generators,
    sum_j c(g_j) = 2d+8.

Assume Gamma normalizes a finite group P=Z(P)E of symplectic type, with E extraspecial of prime p, and P acts irreducibly on V. This is the finite symplectic-type alternative supplied by GT08 Proposition 2.8(iii); the irreducibility is explicit in its proof and Lemma 2.5. It is **not** the class of all finite symplectic groups.

P may be obtained in a scalar-normalized group H with C^*H=C^*Gamma. Scalar multiplication does not change conjugation or commutators, so Gamma still normalizes P and centralizes P exactly when the corresponding normalized matrix does. No assumption that the normalizing scalars are K-rational is needed below.

### Eigenvalue lower bound

For h in P\Z(P), there exists x in P such that x h x^{-1}=z h, where z is a primitive p-th-root scalar: use the nondegenerate commutator pairing of E/Z(E). Thus the eigenvalues of h occur in p-cycles of equal multiplicity, and

    c(h) >= d(1-1/p) >= d/2.                         (S1)

### A small noncentral commutator is forced

Choose a branch generator g with c(g)=c_min. Then

    c_min <= (2d+8)/19.

For d>=3, this is less than d, so g is nonscalar. Since P acts irreducibly, Schur's lemma gives C_GL(V)(P)=C^*; hence choose x in P with h=[g,x]!=1. Normality gives h in P. Rank subadditivity gives

    c(h) <= 2 c(g) <= (4d+16)/19.                   (S2)

For d>=3,

    (4d+16)/19 < d/2,                              (S3)

because 32<11d. In particular h cannot be a nonidentity scalar (which would have moving rank d). Thus h is noncentral in P, and (S1) contradicts (S2)–(S3).

This proves **symplectic type is impossible for all d>=3 in the stated budget**. The d=1,2 cases already have 2d+8<19 and cannot have N>=19 effective branch points.

### Relation to Claude's two inequalities

Claude's restrictions p=2 or 3 are valid in the K-model after retaining the scalar-normalization/commutator argument. They give 11d/2<=16 or 26d/3<=16, respectively, both impossible for d>=3.

The proof above is slightly stronger and simpler: **it works for every prime p** using 1-1/p>=1/2, so neither p in {2,3} nor a K-rationality assertion for all of P is needed. This is a strengthening of the proof scope, not a claim of literature novelty.

## 4. Scientific dispositions

1. The missing exact-data obligation in the prior primitive review is now closed. The complete 25<=d<=42 result may be recorded as **CHECKED (two implementations / two reviewers)**, with the Hiss–Malle completeness, GT08 reduction, inherited (H), and classical Weil formula kept as explicit external inputs.
2. The all-dimensional symplectic-type exclusion is **CHECKED** in the above inherited branch and budget. It does not exclude ordinary Sp_{2n}(q) groups merely because of their name.
3. The previously CHECKED global lower bound remains **d>=26**. At d<=41 the surviving degree list is unchanged at this point: 26,28,30,32,33,34,35,36,38,39,40, all in the complex-imprimitive, non-K-defined-block branch. At d=42 factorwise tensor and imprimitive cases have not been excluded by this review.
4. A separate, new **PROPOSED** note reduces the degree-26 two-block residual to rank-13 reflection groups and attempts its exclusion. It must not be merged into the checked lower bound before peer review.

## 5. Source reading and evidence boundary

- Claude current report: fully read; raw JSON and all included scripts inspected; exact Python verifier executed.
- Previous ChatGPT d<=42 cross-review: read, including the exact branch definition and the remaining-data qualification.
- GT08, *Symmetric powers and a problem of Kollár and Larsen*, arXiv:0810.0853v1: Lemma 2.5 and Proposition 2.8 plus the symplectic-type part of its proof, printed pp. 7–10, **targeted primary-text reading**. Web PDF screenshots failed with Cache miss; direct binary retrieval also failed. No visual verification or PDF-byte hash is claimed.
- Character-table completeness and the repaired Weil estimate were not re-proved or re-run from different underlying tables this turn. Their earlier external-source status is retained.

Primary reference: https://arxiv.org/pdf/0810.0853

## 6. Reproduction

The companion package includes the unchanged source ZIP, its eight manifest-listed files, the unchanged original exact verifier and exporter, the new raw-data/budget checker, frozen outputs and `replay.py`. The replay validates hashes, executes both Python checkers in a temporary directory, compares the complete results byte-for-byte, and rechecks source identity. It needs only Python's standard library. It does not run GAP or fetch web data.

No adopted HCG/RTG document was changed. No human refereeing or scientific adoption is inferred from successful execution.
