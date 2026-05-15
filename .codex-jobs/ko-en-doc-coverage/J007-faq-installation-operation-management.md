# J007 FAQ Installation, Operation, and Management Review Note

Date: 2026-05-15

## Scope

J007 compared Korean FAQ categories `01. 설치, 패치, 업그레이드` and `02. 운영 및 관리` against the corresponding English FAQE core categories. Korean source FAQ pages remained authoritative and were not edited.

## Boundary

- Updated only scoped English FAQ Markdown documents, `manifest.json`, the review report, and workflow job tracking.
- Preserved the existing FAQE category and file structure.
- Did not enter FAQ replication, backup, SQL, stored procedure, development/API, monitoring, error-message, utility, attachment-wide coverage, or final LLM consolidation work.

## Documentation Structure Impact

No product behavior or architecture change was introduced. The documentation-structure changes were limited to restoring Korean-source technical details in searchable English text and converting broken table-exported shell examples into fenced code blocks where the Korean FAQ source clearly described script contents.

## Main Updates

- Rechecked the 4 Korean installation/patch/upgrade FAQ pages and 28 Korean operation/management FAQ pages against their FAQE counterparts.
- Restored or corrected Korean-source details for Linux automatic startup on Red Hat family v6, `MEM_MAX_DB_SIZE` restart/error handling, `TRANSACTION_TABLE_SIZE` memory usage, JOB interval guidance, IPC configuration, log/data file path changes, and startup scripts for Solaris and HP-UX.
- Removed residual Korean text from scoped English FAQE pages and corrected broken or misleading technical text such as swapped Solaris/HP-UX setup links, duplicated `IPC_FILEPATH` in a query, incorrect log-directory property names, and malformed support/manual links.
- Preserved scoped document-format attachment links already present in English counterparts; no missing URL-backed `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` links were found in this scope.

## Verification

Verification is recorded in `KO_EN_DOC_REVIEW_REPORT.md` for this job.
