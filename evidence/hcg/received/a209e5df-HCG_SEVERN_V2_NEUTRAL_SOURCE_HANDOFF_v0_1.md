# HCG — Severn v2 primary-source handoff (neutral)

**Date:** 2026-10-27  
**Status:** SOURCE NAVIGATION / NOT A SCIENTIFIC REVIEW. Noncanonical, internal; no adopted HCG changes.

## Primary source

- Benjamin Severn, *Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(-3))*, `hexagon:2610.00387v2`.
- Official source page: https://hexagonmath.org/2610.00387v2
- Original PDF: https://hexagonmath.org/pdf/2610.00387v2
- Manuscript internal identity: **21 October 2026, version 1.5**, 31 PDF pages.
- Source browser: https://hexagonmath.org/src/2610.00387v2/files
- LaTeX root source: https://hexagonmath.org/api/v1/works/2610.00387v2/source?path=weil-qsqrt3-v1.5.tex

The original PDF was opened and read through the web research viewer, but a byte-for-byte local copy could not be materialized from this environment. Its SHA-256 is consequently **not verified locally**. Do not cite the handoff as if it were the deposited PDF.

## Independent successor review: target locations

1. `Lemma 4.4`, PDF pp. 9–10 (zero-based PDF pages 8–9): scope of Schoen's Theorem 2.0 when exponents are m/2 and 4 divides m. Verify the complete proof and its use of Schoen's Lemmas 2.5, 2.8 and Sublemma 2.9, independently of any ChatGPT proof assessment.
2. `Lemma 4.3`, `Proposition 4.6`, `Theorem 5.1`: the algebraic suppliers and character-lattice supply argument.
3. `Theorem 6.2`: spreading, especially the application to all members including special products.
4. `Proposition 8.5`: maximal boundary degeneration and the split discriminant scope.
5. `Section 9 / Remark 9.2`: G34 implementation, explicit supplier evidence and reliance on Lemma 4.4.
6. `Proposition 10.2`: compensation.
7. Match all substantive successor claims to v1 by hypotheses, not old theorem numbers.

## Existing certificate evidence (NOT a new Zenodo-version assertion)

The **previously user-uploaded** archive `/mnt/data/weil-sixfolds-qsqrt3-certificates.zip` exists locally with SHA-256 `3a39a346ed98f0ff11c6fcf4efdf72ad8e72ef4ff72cf983b5c4e4c46c684134`. Its entry `certificates/g34-d3/L/rebuild_rerun.log` (SHA-256 `7c824f4e2895d75a8e1c99e5f77fb1b73c6078b28932c6e47a9c1792935a2b21`) contains **84** supplier rows. Rows 42–44 report `m=12`, `s>0`, matching Severn v2 §4 / Remark 9.2. This checks presence of numerical supplier metadata, **not the proof of Lemma 4.4** and not the existence of a newer certificate version.

## Zenodo access / version caveat

Both the v1 and v2 Hexagon publication pages point to the same DOI `10.5281/zenodo.23422649`. The Zenodo record/API could not be opened from the research environment on 27 October 2026, so existence, version history, and file checksums of a **separate v2 certificate deposit** are **NOT VERIFIED**. Check the Zenodo version history and compare actual files/checksums before asserting a new release.

## Independence boundary

This is a source locator and a neutral examination scope, **not** a scientific verdict on Lemma 4.4 or the successor theorem. The second reviewer should perform their own reading and derivation before viewing any other review.
