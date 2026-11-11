# HHO — charter

**Study:** Hurwitz–Hodge Obstruction. **Key:** `hho`. **Tags:** `hho-v<version>`. **Inbox:** `pipes/HHO/`.

**Owners:** the Claude and ChatGPT sessions of the "HHO Hurwitz–Hodge obstruction research" conversation. **PI:** Mustafa Aksu, who decides adoption.

**Status of this file:** adopted by the PI on 11 Nov 2026 as the governance text of `hho-v0.1` (`records/hho/HHO_v0.1_RELEASE_RECORD.md`). It carries no scientific claim. **Governing edition:** `hho-v0.1`.

## 0. Scope guard

> HHO makes no statement that nonsplit Weil eightfolds exist or do not exist, and no statement about the Hodge conjecture. A failed gate excludes a datum or a class of data and nothing more.

This sentence applies to every HHO document and to every publication-facing text written about HHO by its owners or the PI.

- Severn's results (`hexagon:2610.00386`, `hexagon:2610.00387`) are **CLAIMED**. HHO does not change that.
- HHO is a satellite study (`REGISTRY.md`). It is not an RTG stream and not part of HCG. Nothing in it is an RTG result or an HCG result.

## 1. What HHO studies

**Object.** Severn-type genus-0 Hurwitz transfer data

  𝒟 = (K, Γ, σ, (g₁, …, g_N), h₀),

where K = ℚ(√−3); σ: G → GL_d(K) with image Γ; g₁⋯g_N = 1 is a generating product-one tuple; and h₀ is a positive K-Hermitian form preserved by Γ.

**Question.** Which necessary conditions must such a datum meet to give a **nonsplit, dominant Weil-eightfold family**? HHO turns those conditions into reproducible obstruction certificates.

**Three kinds of obstruction.**

| Kind | Examples |
|---|---|
| Arithmetic | local discriminant factors, Hilbert symbols, norm classes, lattice discriminants |
| Geometric | Riemann–Hurwitz, movement budget, period-map rank |
| Representation-theoretic | Clifford theory, Brauer blocks, reflection subgroups |

**Standing hypotheses (H).** HHO uses the list (H) of its opening note, §2 (source: §5.1). It has four parts: finiteness and absolute irreducibility over K with character field exactly K; dim_K H¹_par = 8 with signature (4,4); dominance (D); and the budget relations. **(L)** is a separate hypothesis and is not part of (H).

**Symbol warning.** HHO's "(H)" and Severn's boundary hypotheses "(H0)–(H4)" are different objects. `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md` records where each is stated.

**First target P1.**

> **P1 — Dominance versus the local class product.** Is there a dimension-independent obstruction to a nonsplit discriminant class under (H)?

History of this choice, kept in full:

1. The opening note (3 Nov 2026) proposed P1 in this form and left the PI-decision field blank.
2. On 10 Nov 2026 the PI accepted "(L)+(D) ⇒ [1] at d = 8" as the first target. The Claude owner session had proposed it without knowing the opening note's result R1 (`records/hho/HHO_MIGRATION_PLAN.md` §7, Q4).
3. Later on 10 Nov 2026 the PI replaced that target with P1 as quoted above. The decision is recorded in the co-owner checkpoint on PR #15 (comment of 2026-11-10T12:21:55Z) and was relayed by the PI in the HHO conversation. The PI's own wording is not held by the Claude session.

Choosing P1 is a research priority. It adopts no claim.

## 2. Documents and layout

| Place | Content |
|---|---|
| `hho/HHO_CHARTER.md` | this file |
| `hho/HHO_CLAIM_REGISTER.md` | every HHO claim: statement, hypotheses, dependencies, grade, review state, evidence |
| `hho/` (later batches) | live statements of the current results: support theorems, gates and bounds |
| `records/hho/` | migration note and plan, source manifest, reviews, release records |
| `evidence/hho/` | frozen files: append-only review records, scripts, outputs, received inputs |
| `upload/hho/` | the unchanged source upload with `SHA256SUMS` |

- Live files have fixed names, with no version and no author in the name.
- A frozen file is never edited. It keeps its wording, including statements that were later corrected or withdrawn. The live files state the current result.
- Until batch 2 and batch 4 place the frozen files in `evidence/hho/`, evidence pointers name the path in `upload/hho/`.

## 3. Editions

- The governing edition is the latest adopted tag `hho-v<version>` with its release record (`CONVENTIONS.md` §2). It is `hho-v0.1`.
- Order of a release: decision, release record, merge, tag. A merge, a tag or a passing check is not an adoption.
- The first release `hho-v0.1` contains this charter, the claim register and the source manifest. It is a register edition: it adopts no claim row.

## 4. Grades, review states, identifiers

HHO keeps two separate axes.

**Evidence grades.**

| Grade | Meaning |
|---|---|
| `[THM]` | proved statement with all hypotheses written |
| `[THM-cond: X]` | proved statement that depends on the named input X, which HHO has not itself established |
| `[ALG]` | exact algebraic computation or identity |
| `[NUM]` | exact finite computation on named data; it certifies those data only |
| `[CONJ]` | conjecture |
| `[OPEN]` | open question or open obligation |
| `[NEG]` | counterexample or negative control |

**Review states.**

| State | Meaning |
|---|---|
| `PROPOSED` | one AI has derived the claim |
| `CHECKED` | an independent check by a second AI is recorded |
| `THIRD-FAMILY CHECKED` | a reviewer outside the Claude and OpenAI model families has independently checked the claim |
| `ACCEPTED` | a PI decision |

- A review state is not a proof grade. Agreement among AIs is not human refereeing.
- Neither axis is an RTG grade or an HCG grade.
- A replay of the same engine is recorded as a replay, not as an independent check.

**Identifiers.** One namespace: `HHO-<KIND>-<NAME>`, with KIND ∈ {THM, LEM, COR, CONJ, OPEN, NUM, ALG, NEG, WD}. WD marks a withdrawn item.

- The session-local RIDs `HCG-HHO-…` of the opening note are renamed. The map is in `records/hho/HHO_SOURCE_MANIFEST.md` §5.
- RIDs of the form `HCG-…` without `HHO` belong to HCG and are cited unchanged.
- A withdrawn RID is never reused.

**Negative results** — refutations, retractions, failed routes, counterexamples — are kept with the same care as positive ones and are never dropped.

**Notation, fixed once.**

| Symbol | Meaning |
|---|---|
| K | ℚ(√−3) = ℚ(ω), ω² + ω + 1 = 0; δ = √−3 |
| [det h] | class of the determinant in ℚ^×/N_{K/ℚ}(K^×) |
| split | [det h] = [1] |
| inert prime | rational prime p ≡ 2 (mod 3) |
| c_j | rank(1 − g_j), the movement rank of the j-th local monodromy |
| E_j, a_j, b_j | E_j = im(1 − g_j); a_j = det(h₀\|E_j); b_j = det((1 − g_j)\|E_j) |
| Δ(g) | a/b, the local discriminant factor |
| (L), (D), (H0)–(H4) | as recorded in `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md` |

## 5. Interfaces

### 5.1 HCG

HCG has the adopted edition `hcg-v0.2`. Only its session ledger v0.2 is adopted (`records/hcg/HCG_v0.2_RELEASE_RECORD.md`).

- **How HHO cites HCG.** By tag, path and SHA-256, with the state the file has in HCG.
- **Pending material.** Everything in HCG's Δ24–Δ29 is "placed at `hcg-v0.2`, pending in HCG, not adopted". This includes the locality theorem, the induced-period bound, the dimension screens of Δ27 and the HHO opening note.
- **No upgrade by citation.** An HCG theorem, definition, engine or certificate does not gain HHO grade because HHO uses it. A result that depends on it is graded `[THM-cond: …]`.
- **The HHO track made in the HCG conversation.** The opening note and its founding documents are stored in `evidence/hcg/` as dated source evidence. Their scientific custody is with HHO (`hcg/HCG_CHARTER.md` §5). HHO cites them there and does not copy them.
- **HHO → HCG.** An HHO result enters HCG only with all three of: an explicit disposition by the HCG owners, PI adoption, and an HCG release that records the import.
- **Re-pinning** to a later HCG tag is an HHO decision, made in an HHO release.

### 5.2 RTG

HHO uses no RTG result. In `REGISTRY.md` the HHO field "RTG inputs" is `none` (set with `hho-v0.1`). If that changes, HHO cites an adopted `rtg-corpus` tag (`CONVENTIONS.md` §3). An HHO finding reaches RTG only as a pipe item in `rtg-corpus`.

### 5.3 LIT and third-party sources

- Third-party texts are cited bibliographically: identifier or URL, version, and SHA-256 where a copy is held. They are not stored in this repository.
- HHO claims no LIT-backed validation.
- Classification inputs (for example Shephard–Todd, Cohen 1976, Hiss–Malle, CTblLib data) are quoted, not re-proved. A result that uses one names it at every restatement.

## 6. Working rules

**Carried from the opening note (HHO-SG-1 to HHO-SG-6).**

| Rule | Content |
|---|---|
| HHO-SG-1 | A failed gate excludes that datum or class of data only. |
| HHO-SG-2 | A source-conditional result lists its external inputs every time it is restated. |
| HHO-SG-3 | (L), (D) and "split" are independent gates. None is inferred from another without a proof. |
| HHO-SG-4 | A parabolic-cup class is not a polarization discriminant without the cup–polarization identification. |
| HHO-SG-5 | A finite scan certifies only its stated range and model. Scans stay PROPOSED until replayed independently. |
| HHO-SG-6 | Witnesses that fail (D) are not counterexamples to any Severn theorem and say nothing about (H)-data. |

**Added from the HHO conversation.** Accepted by the PI on 10 Nov 2026, with the proviso that they are reconsidered if they prove too restrictive in practice.

| Rule | Content | Reason |
|---|---|---|
| HHO-SG-7 | When a coefficient representation is split into orthogonal summands, each summand carries the restricted coefficient form. A script that divides determinants asserts this. | the retracted "30/30 split" result (register, HHO-WD-F20-ALLSPLIT) |
| HHO-SG-8 | A package contains every file its manifest lists. | a package sent with two listed files missing |
| HHO-SG-9 | Before a result is recorded as new, it is compared with the HCG-side track (opening note and HCG Δ27). | Addenda 12–14 re-derived earlier results |

**General.**
- Two-AI protocol. Each owner reviews the other's work. No owner is the sole referee of its own claims.
- Hashes on every deliverable. Received archives are unpacked in their own directory and replayed with `python3 -I`.
- Hashes, approvals and file contents are never invented. A missing source is written "not available".
- Heavy computations run on the PI's machine. The library name and version that produced a stored output are recorded.
- Branches: `claude/hho-*` and `chatgpt/hho-*`; pull requests; the PI merges and tags.
