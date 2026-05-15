# J009 FAQ Monitoring, Error Messages, Utilities, Others, and General Review Note

Date: 2026-05-15

## Scope

J009 compared Korean FAQ categories `08. 모니터링`, `09. 에러메시지`, `11. 유틸리티`, `12. 기타`, and `13. 일반` against the corresponding English FAQE core categories. Korean source FAQ pages remained authoritative and were not edited.

## Boundary

- Updated only scoped English FAQ Markdown documents, `manifest.json`, the review report, and workflow job tracking.
- Preserved the existing FAQE category and split-page structure.
- Did not enter attachment-wide coverage, workflow-wide final validation, English quality beyond scoped Korean-source fixes, or LLM consolidation work.

## Documentation Structure Impact

No product behavior or architecture change was introduced. Documentation-structure changes were limited to restoring Korean-source headings and examples in searchable English text, correcting malformed exported content, and converting unclear Korean-source table rows into clear English tables.

## Main Updates

- Rechecked 55 Korean FAQ pages in categories 08, 09, 11, 12, and 13 against 55 corresponding FAQE pages.
- Removed residual Korean text from scoped monitoring, error-message, and general FAQE pages, including SQL comments, examples, cursor pseudocode, and table headings.
- Restored the missing disk table count query heading in the Altibase 5.3.x/5.5.1/6.1.1/6.3.1 disk table and index usage FAQ by replacing an exported macro error.
- Corrected malformed support/manual links and Korean-source attachment labels while preserving the original attachment URLs.
- Clarified the large DRDB index build guidance for versions 6.5.1 through 7.1.0 and 7.3.0 or later, preserving property names such as `BUFFER_AREA_SIZE`, `SORT_AREA_SIZE`, `DISK_INDEX_BUILD_SORT_AREA_SIZE`, and `DISK_INDEX_BUILD_MERGE_PAGE_COUNT`.
- Improved general FAQ wording for Altibase interfaces, in-memory versus disk-based DBMS differences, WAL, and failure management while preserving the Korean-source meaning.

## Verification

Verification is recorded in `KO_EN_DOC_REVIEW_REPORT.md` for this job.
