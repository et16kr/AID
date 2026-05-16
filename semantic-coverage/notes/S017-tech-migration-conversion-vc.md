# S017 Tech Migration Conversion VC

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S017 performs a semantic-unit audit for Oracle conversion, MSSQL conversion, Altibase version migration, Migration Center, VC 2008, and VC 2010 technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/38. Altibase VC 2008 개발가이드__19333567.md` -> `arch/Home/Altibase VC 2008 Development Guide__19333567.md`
- `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md` -> `arch/Home/ORACLE to ALTIBASE Conversion Guide__22643038.md`
- `DOCK/Home/46. Altibase 버전 간 마이그레이션 가이드__19333688.md` -> `arch/Home/Altibase Data Migration Process Guide__22642994.md`
- `DOCK/Home/61. Altibase VC 2010 개발가이드__19334121.md` -> `arch/Home/Altibase VC 2010 Development Guide__19334121.md`
- `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md` -> `arch/Home/MSSQL to ALTIBASE Conversion Guide__22643024.md`
- `DOCK/Home/70. Migration Center 사용자 가이드__19955861.md` -> `arch/Home/Migration Center User Guide__19955861.md`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S017.md`
- `semantic-coverage/doc-mapping.tsv`
- The six Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S017-tech-migration-conversion-vc.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow runtime area as `S017` was already in `Progress`.
- No uncommitted project files outside the workflow runtime area were present before S017 edits.

## Design Note

S017 adds semantic evidence only:

- Adds `semantic-coverage/matrices/S017-tech-migration-conversion-vc.tsv`
- Adds `semantic-coverage/notes/S017-tech-migration-conversion-vc.md`
- Updates S017 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

The product documentation structure is unchanged. No English `arch/` page required edits in this job, so `manifest.json` metadata was not changed.

The matrix records 1,699 semantic units: 1,652 `covered`, 44 `not_applicable`, and 3 `source_limitation`. It includes headings, paragraphs, support routes, command and SQL blocks, table rows, image references, document-format attachment references, and legacy placeholder rows.

## Audit Summary

### VC 2008 And VC 2010

The English VC 2008 and VC 2010 targets preserve the Korean-source overview, support route, support center number, Altibase v5 basis, and original downloadable document links:

- `ALTIBASE_VC_2008_개발가이드.zip`
- `ALTIBASE_VC_2010_개발가이드.pdf`

The Korean filenames are intentionally preserved in the English attachment labels.

### Oracle To Altibase Conversion

The English Oracle conversion guide preserves the Korean-source migration process, system analysis, supported-version scope, preliminary checklist, data type conversion table, object conversion tables, SQL conversion function tables, stored procedure/function conversion notes, exception table, database migration procedure, MigrationCenter workflow, support portal/product-download links, and Migration Center manual link.

The matrix records Oracle conversion table rows at row level, including conversion examples for `CREATE TABLESPACE`, `CREATE TABLE`, `CREATE INDEX`, AUTOCOMMIT procedure behavior, `WHERE CURRENT OF`, `DBMS_RANDOM`, exception mappings, data integrity verification, and MigrationCenter usage.

The two old Oracle conversion PDF entries are Korean-source legacy `#` placeholders and are recorded as `source_limitation`; the English target preserves the exact filenames without inventing URLs:

- `ALTIBASE_Oracle_변환_가이드.pdf`
- `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf`

### Altibase Version Migration

The English Altibase data migration guide preserves the Korean-source full migration flow: service stop, working directory and disk space, source counts, `DBMS_METADATA`, `ALTIBASE_NLS_USE`, `aexport.properties`, `run_aexport.sh`, DDL pre-checks, `iloader` extraction, `.fmt` and `.dat` checks, character-set conversion with `iconv`, target database creation and configuration, object creation, data loading, `.bad` and `.log` verification, performance options `-array` and `-commit`, and follow-up validation.

Standalone command blocks and the process table were checked directly against the English target. No English source edit was required.

### MSSQL To Altibase Conversion

The English MSSQL conversion guide preserves SQL Server 2016 and Altibase 7.1 or later scope, schema-to-user conversion, object conversion, datatype/function/object tables, `CREATE TABLESPACE`, `CREATE TABLE`, `CREATE USER`, `CREATE INDEX`, SQL conversion, procedure conversion, cursor usage, and exception-code mappings.

The matrix records MSSQL conversion table rows at row level, including SQL Server schema behavior, `IDENTITY` to sequence conversion, procedure parameter and variable conversion, assignment, control flow, `REF CURSOR`, `NO_DATA_FOUND`, function substitutions, DB link and JOIN update limitations, and cursor examples.

The old MSSQL PDF entry is a Korean-source legacy `#` placeholder and is recorded as `source_limitation`; the English target preserves the exact filename without inventing a URL:

- `ALTIBASE_MSSQL_변환가이드.pdf`

### Migration Center

The English Migration Center target remains a condensed text guide, but it preserves the actionable Korean-source semantics: overview, benefits, requirements, compatible DBMS matrix, JDBC driver rules and URLs, precautions, installation/removal/run commands, project and process concepts, menus, utilities, GUI flow, DBMS connection fields, project creation/open/connect behavior, migration options, Build/Reconcile/Run/Data Validation flow, CLI run command, and supported conversion object matrices.

Screenshot-only embedded image rows in the Korean source are recorded as `not_applicable` where the English condensed guide intentionally omits screenshots. Rows with procedural or field semantics are marked `covered` and mapped to the corresponding English prose or table. The original downloadable PDF link is preserved:

- `Migration_Center_사용자가이드.pdf`

## Attachment And Link Evidence

URL-backed document-format attachments in this scope:

- `ALTIBASE_VC_2008_개발가이드.zip`: Korean-source URL preserved in `arch/Home/Altibase VC 2008 Development Guide__19333567.md`
- `ALTIBASE_VC_2010_개발가이드.pdf`: Korean-source URL preserved in `arch/Home/Altibase VC 2010 Development Guide__19334121.md`
- `Migration_Center_사용자가이드.pdf`: Korean-source URL preserved in `arch/Home/Migration Center User Guide__19955861.md`

Source-limited filename-only references:

- `ALTIBASE_Oracle_변환_가이드.pdf`: Korean source uses a legacy `#` placeholder with no downloadable URL.
- `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf`: Korean source uses a legacy `#` placeholder with no downloadable URL.
- `ALTIBASE_MSSQL_변환가이드.pdf`: Korean source uses a legacy `#` placeholder with no downloadable URL.

Important non-document links checked in scope include `support.altibase.com`, `support.altibase.com/en/product`, Microsoft JDBC driver URLs, PostgreSQL JDBC download URL, and the Migration Center manual URL.

## Self-Review

- Scope checked: S017 changed only S017 evidence files and S017 workflow status.
- Korean authority checked: all six scoped Korean source files were inspected directly.
- English target checked: all six mapped English target files were inspected directly.
- Matrix checked: the S017 matrix uses the exact required TSV header, one physical row per semantic unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `MigrationCenter`, `Migration Center`, `aexport`, `iloader`, `iLoader`, `iSQL`, `DBMS_METADATA`, `ALTIBASE_NLS_USE`, `JAVA_HOME`, `FILESYNC`, `Build`, `Reconcile`, `Run`, `Data Validation`, `DB to DB`, `DB to File`, `PSM`, `REF CURSOR`, `IDENTITY`, `DBMS_RANDOM`, and exact attachment filenames/URLs are preserved.
- Product docs checked: no scoped English `arch/` Markdown page changed, so no manifest metadata refresh was required.

## Verification

Verification results after drafting and self-review:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| S017 TSV header and column-count check | Passed: 1,699 data rows, 15 columns each |
| S017 coverage status check | Passed: 1,652 `covered`, 44 `not_applicable`, 3 `source_limitation` |
| S017 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped English empty-link and macro-artifact scan, including S017 evidence files | Passed with exit code 1, meaning no matches |
| Scoped document-format attachment preservation check | Passed: 3 URL-backed source attachments and 3 legacy placeholders preserved |
| D040/D046/D065 table-row count comparison | Passed: Oracle 562/562, version migration 8/8, MSSQL 296/296 |

## Final Decision

S017 final decision: `COMPLETE`.
