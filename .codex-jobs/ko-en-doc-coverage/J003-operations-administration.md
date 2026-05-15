# J003 Operations and Administration Review Note

Date: 2026-05-15

## Scope

J003 compared the Korean DOCK operations and administration documents against their English arch counterparts. Korean source documents remained authoritative and were not edited.

## Boundary

- Updated only scoped English technical Markdown documents, `manifest.json`, the review report, and workflow job tracking.
- Preserved the existing split-page structure of English documents.
- Did not enter FAQ coverage, replication-specific guide coverage, backup/recovery guide coverage, development/API coverage, migration, or final LLM consolidation work.

## Documentation Structure Impact

No architecture or product behavior change was introduced. The only documentation-structure improvement was adding Korean-source monitoring query IDs such as `[ST01]`, `[TS01]`, `[OB01]`, and `[RP01]` to the corresponding English monitoring query headings so the split English pages preserve the Korean source labels and remain searchable for LLM reference.

## Main Updates

- Rechecked the J003 Korean-to-English mappings for configuration, failure response, startup/shutdown, system resource sizing, OS utilities, UNIX memory management, monitoring queries, CPU overload analysis, and memory usage increase analysis.
- Preserved J003 Korean source document-format attachment links in English counterparts; no missing `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` links remained.
- Removed Korean residue from the English system resource sizing and monitoring query documents.
- Restored missing Korean-source monitoring query IDs to English monitoring query headings.
- Corrected operation-impacting mistranslations and stale terms, including `ulimit -n`, `$ALTIBASE_HOME/conf/altibase.properties`, duplicate Altibase startup prevention, `procstack`, replication-gap wording, `Garbage Data`, `TIMED_STATISTICS`/profiling wording, and several typo-level terms in startup, CPU, memory, and monitoring documents.

## Verification

Verification is recorded in `KO_EN_DOC_REVIEW_REPORT.md` for this job.
