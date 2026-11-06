# Translation rules for frozen COIL files (evidence/coil)

Applies to every `<name>.en.md` written beside a frozen Turkish original in `evidence/coil/prereg/` and `evidence/coil/run/`.

1. **The frozen original governs.** The first lines of every translation are exactly:
   ```
   > **Translation; the frozen original governs.** Original: `<name>.md`, SHA-256 `<hash from SHA256SUMS>`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.
   ```
2. **Faithful, complete, sentence-level.** Translate everything: headings, tables, footnotes, code blocks' comments. Do not summarise, reorder, merge or drop sentences, rows or cells. Keep all numbers, symbols, formulas, file names, identifiers, labels (`[NUM]`, `[EXPLORE]`, `D2`, `P-κ`, …) and version strings exactly as in the original. Keep LaTeX as is. Keep strike-through, bold and emphasis where the original has them.
3. **Never correct the original.** If a statement is known (or looks) wrong, superseded or later retracted, translate it as written. Do not soften, strengthen or update a claim, a grade or a status. Do not add qualifiers the original does not have.
4. **Translator's notes** are the only addition allowed. Form: a separate paragraph `> *Translator's note:* …` immediately after the passage. Use one only when a later COIL document corrects or supersedes the passage, and only to **point** to the live document (`coil/COIL_INDEX.md`, `coil/COIL_CHARTER.md`, `coil/records/RM-02.md`, `coil/MM-1.md`, `coil/IDEALOG_COIL_RCSJ.md`) or to the later frozen file (an addendum, a later RUN). State what the later document says in one sentence; do not argue, do not evaluate. Never put a note where you are not certain a later correction exists.
5. **Fixed English terms** (from the glossary): ön-kayıt → preregistration (prereg); koşu raporu → run report; sertifika → certificate; karar ağacı → decision tree; kilitli → LOCKED/locked; kırılma → fracture; spark stays spark; basamak → rung; dil → tongue; yürütme/tahmin hatası → execution/prediction failure; hat → line; Pair A/B/C, κ, β_c, γdt, a as in the original; YANLIŞLANDI → FALSIFIED; ÇÖZÜLDÜ → RESOLVED; TAMAM → DONE; KAPANDI → CLOSED; AÇIK (gate) → OPEN; yok → none/absent as fits; ölçülmedi → unmeasured; tested-scope language stays as in the original.
6. **Turkish-specific tokens** in file names, column headers or labels that are themselves identifiers (e.g. `CLI-N3-kalan-kosular.md`, `kayit`) stay unchanged.
7. Markdown structure identical to the original (same heading levels, same table columns, same bullet nesting).
8. Output is UTF-8, LF line endings, no trailing whitespace changes beyond what translation needs.
