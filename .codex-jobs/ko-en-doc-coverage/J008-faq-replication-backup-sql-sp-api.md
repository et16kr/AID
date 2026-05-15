# J008 FAQ Replication, Backup, SQL, Stored Procedures, and Development API Review Note

Date: 2026-05-15

## Scope

J008 compared Korean FAQ categories `03. 이중화`, `04. 백업 및 복구`, `05. SQL`, `06. Stored Procedures`, and `07. 개발 및 API` against the corresponding English FAQE core categories. Korean source FAQ pages remained authoritative and were not edited.

## Boundary

- Updated only scoped English FAQ Markdown documents, `manifest.json`, the review report, and workflow job tracking.
- Preserved the existing FAQE category and split-page structure.
- Did not enter FAQ monitoring, error-message, utility, attachment-wide coverage, final validation, or LLM consolidation work.

## Documentation Structure Impact

No product behavior or architecture change was introduced. Documentation-structure changes were limited to restoring Korean-source technical content in searchable English text, correcting malformed exported command/code blocks, and adding the missing Fail-Over success-check subsection that exists in the Korean JDBC FAQ.

## Main Updates

- Rechecked 28 Korean FAQ pages in categories 03 through 07 against 28 corresponding FAQE pages.
- Restored the missing `ALTER REPLICATION ... ADD TABLE` statement and corrected `ALTER REPLICATION ... DROP TABLE FROM ... TO ...` in the replication target table FAQ.
- Restored the JDBC Fail-Over success-check guidance for `08F01` and `ES_08FO01`, and converted the flattened Java fail-over sample into a searchable code block.
- Preserved Korean-source attachment references in scope, including replication PDF links, the Spring+iBatis sample ZIP, and the stored procedure sample text file.
- Removed residual Korean comments and malformed export artifacts from replication monitoring, cold backup, stored procedure, JDBC, ODBC, and unixODBC pages.
- Corrected technical command/query text such as `SELECT DB_NAME FROM V$DATABASE`, `SELECT NLS_CHARACTERSET FROM V$NLS_PARAMETERS`, `run_il_in.sh`, `SQLFreeStmt`, `ALTIBASE_JDBC_TRCLOG_DISABLE`, and unixODBC library paths.

## Verification

Verification is recorded in `KO_EN_DOC_REVIEW_REPORT.md` for this job.
