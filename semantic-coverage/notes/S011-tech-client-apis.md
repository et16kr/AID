# S011 Tech Client APIs

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S011 performs a semantic-unit audit for the Java, unixODBC, Windows ODBC, ADO.NET, and PHP client API technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/32. Altibase와 unixODBC 연동 가이드__11698379.md` -> `arch/Home/Altibase and unixODBC Integration Guide__14647413.md`; `arch/Home/Altibase and unixODBC Integration Guide/1. unixODBC Manager Installation__14647417.md`; `arch/Home/Altibase and unixODBC Integration Guide/2. Integrating unixODBC Manager__14647432.md`
- `DOCK/Home/51. Altibase window ADO.NET 개발 가이드__11698513.md` -> `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md`; `arch/Home/Altibase Window ADO.NET Development Guide/1. ADO.NET Settings__14647569.md`; `arch/Home/Altibase Window ADO.NET Development Guide/2. ADO.NET Development Guide__14647573.md`; `arch/Home/Altibase Window ADO.NET Development Guide/3. Frequent Error Messages__14647579.md`
- `DOCK/Home/53. Windows 환경의 Altibase ODBC 개발 가이드__13436856.md` -> `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md`
- `DOCK/Home/56. JAVA 개발 가이드__14057500.md` -> `arch/Home/JAVA Developer's Guide__16875544.md`
- `DOCK/Home/66. Altibase PHP 연동가이드__7341461.md` -> `arch/Home/PHP Integration Guide for Altibase__14647305.md`; `arch/Home/PHP Integration Guide for Altibase/1. ALTIBASE HDB PHP Module Reference__14647310.md`; `arch/Home/PHP Integration Guide for Altibase/2. ODBC Manger Installation for PHP Integration__14647312.md`; `arch/Home/PHP Integration Guide for Altibase/3. PHP Functions for ODBC Connection__14647314.md`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `semantic-coverage/doc-mapping.tsv`
- The five Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S011-tech-client-apis.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S011 ToDo` to `S011 Progress`.
- No uncommitted project files outside the workflow runtime area were present before S011 product-document edits.

## Design Note

S011 adds semantic evidence and makes one source-preservation correction:

- Adds `semantic-coverage/matrices/S011-tech-client-apis.tsv`
- Adds `semantic-coverage/notes/S011-tech-client-apis.md`
- Updates `arch/Home/PHP Integration Guide for Altibase/2. ODBC Manger Installation for PHP Integration__14647312.md`
- Updates the edited page metadata in `manifest.json`

The product documentation structure is unchanged. The matrix records 110 semantic units covering overview/support information, prerequisites, version conditions, installation/configuration commands, connection strings, code examples, property tables, failover/XA/LOB behavior, error causes and remedies, and attachment/link evidence.

The only English source change preserves the Korean PHP source command spelling for the unixODBC `./configure` example. The Korean source uses `-prefix`, `-enable-gui=no`, and `-–enable-drivers=no`. Because this workflow treats source command text as authoritative, the English target now preserves those option spellings and records `source_command_spelling_review` in the matrix. The option spelling may still merit source-owner review, but this S011 job does not infer a corrected command.

## Audit Summary

### D032 unixODBC

The split English unixODBC guide preserves:

- integration purpose, unixODBC source URL, native compiler assumption, user responsibility for unixODBC setup, test environment, and support contacts;
- download path and `unixODBC-2.3.2.tar.gz`;
- source decompression, driver bit check, `ul32`/`ul64` SQLLEN meaning, and bit matching between unixODBC and the Altibase ODBC driver;
- `BUILD_LEGACY_64_BIT_MODE=1`, SQLLEN/SQLULEN warnings, PHP/Python `SQLColAttribute`, `SQLfetch()`, and `SQLMoreResult()` behavior;
- AIX, HP-UX, and SUN compiler variables plus Linux 64-bit to 32-bit compile examples;
- configure, make, make install, `dltest`, `ODBCINI`, `odbc.ini`, `odbcinst -j`, `isql`, AIX `libodbcinst.so.1`, SUN `LD_LIBRARY_PATH_64`, and trace-log setup.

No URL-backed document-format attachments were present in the Korean unixODBC source.

### D051 ADO.NET

The split English ADO.NET guide preserves:

- Windows ADO.NET development purpose, prerequisite API manual, Altibase v6.5.1/Windows 7/Visual Studio 2010 C# basis, and support contacts;
- ADO.NET component and class tables;
- .NET Framework, ADO.NET-provider, Altibase CLI library, and DTC/XA requirements;
- support-site download route, `altiadonetX.X.X_32/64bit.zip`, older-version Q&A route, and latest `altiadonet6.5.1.2_64/32.zip` note;
- Windows Client installation, `Altibase.Data.AltibaseClient.dll`, `odbccli_sl.dll`, Visual Studio reference setup, executable-folder/PATH dependency handling, and bit-type warning;
- `AltibaseConnection`, `AltibaseDataReader`, `AltibaseCommand`, `AltibaseDataAdapter`, and `AltibaseTransaction` examples;
- `System.BadImageFormatException` and `System.DllNotFoundException` causes, messages, and remedies.

The Korean-source ADO.NET PDF URL is preserved in the English parent page.

### D053 Windows ODBC

The English Windows ODBC guide preserves:

- Windows ODBC purpose, Altibase v6.5.1/Windows 10 basis, and the Korean-source condition that Windows ODBC is provided only through Altibase v6.5.1 and not from Altibase v7.1.0;
- support/download route, support email for old versions, Windows Client installation, and Control Panel registration procedure;
- DSN settings table, `Test Connection` validation, ODBC connection string, and `LongDataCompat`;
- Visual C++, Visual C#, and Visual Basic examples;
- LOB Non-AutoCommit warning, exact autocommit LOB error text, BLOB insert example, and BLOB select example.

The Korean-source Windows ODBC PDF URL is preserved in the English page.

### D056 Java

The English Java guide preserves:

- Java development purpose, Altibase v6.5.1/JRE or JDK 1.5/Eclipse basis, reference documents, and support contacts;
- `Altibase.jar`, `Altibase6_5.jar`, JDBC/server compatibility through CMP and cm protocol version, and the recommendation to use the same-or-later latest JDBC driver;
- CLASSPATH, JRE ext directory, runtime classpath, and Eclipse setup procedures;
- `Altibase.jdbc.driver.AltibaseDriver`, general JDBC URL syntax, connection examples, `SELECT DB_NAME FROM V$DATABASE`, and connection property table;
- connection pool classes for 6.3.1 or later and 6.1.1, XA classes for 6.3.1 or later and 6.1.1, and connection pool properties;
- failover URL properties, CTF/STF semantics, simultaneous different-version connection behavior, and IBM Java 1.6 cm-version URL condition;
- stored procedure/function syntax and examples, `PreparedStatement`, `executeBatch()`, `setFetchSize()`, resource closing, NULL handling, LOB autocommit behavior, REF CURSOR example, and common error causes/remedies.

The Korean-source Java PDF URL is preserved in the English page.

### D066 PHP

The split English PHP guide preserves:

- PHP ODBC integration purpose and support contacts;
- PHP supported data types and `db.php` port-number alignment requirement;
- ODBC Manager prerequisite for Unix/Linux and Windows;
- unixODBC download URL, configure/make/install command sequence, `ODBCSYSINI`, library path variables, `odbc.ini`, `odbcinst.ini`, and Windows automatic registration behavior;
- PHP standard ODBC function reference URL and sample code using `odbc_connect`, `odbc_exec`, `odbc_prepare`, `odbc_execute`, `odbc_do`, `odbc_fetch_row`, `odbc_result`, and `odbc_close`.

S011 changed the English unixODBC configure command in the PHP ODBC Manager page from normalized double-dash syntax to the Korean-source option spelling.

## Attachment Evidence

URL-backed document-format attachments in this scope:

- `ALTIBASE_Windows_AOD.NET_개발가이드.pdf`: Korean-source URL preserved in `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md`
- `ALTIBASE_Windows_ODBC_개발가이드.pdf`: Korean-source URL preserved in `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md`
- `JAVA_개발가이드.pdf`: Korean-source URL preserved in `arch/Home/JAVA Developer's Guide__16875544.md`

D032 unixODBC and D066 PHP have no URL-backed document-format attachments in the scoped Korean source. Embedded image links were reviewed as source-exported illustrations.

## Self-Review

- Scope checked: S011 changed only the scoped PHP English page, `manifest.json`, S011 evidence files, and S011 workflow status files.
- Korean authority checked: all five scoped Korean source files were inspected directly with line-numbered reads.
- English target checked: all mapped English parent and split pages were inspected directly.
- Matrix checked: the S011 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `SQLLEN`, `SQLULEN`, `BUILD_LEGACY_64_BIT_MODE`, `ODBCINI`, `ODBCSYSINI`, `Altibase.Data.AltibaseClient.dll`, `odbccli_sl.dll`, `ALTIBASE_HDB_ODBC_64bit`, `Altibase.jar`, `Altibase6_5.jar`, `Altibase5.jar`, CTF/STF, XA classes, JDBC URL properties, LOB/autocommit text, and exact PDF attachment URLs are preserved.
- Product docs checked: the edited PHP page metadata in `manifest.json` matches the updated file.

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
| S011 TSV header and column-count check | Passed: 110 data rows, 15 columns each |
| S011 coverage status check | Passed: 99 `covered`, 1 `added`, 10 `not_applicable` |
| S011 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped English empty-link, macro-artifact, fake local-link, support-link, and residual Korean scan | Passed with exit code 1, meaning no matches |
| S011 matrix empty-link, macro-artifact, fake local-link, and malformed support-link scan | Passed with exit code 1, meaning no matches |
| Scoped PHP command spelling check | Passed: normalized double-dash command no longer appears in the PHP page; Korean-source `-prefix`, `-enable-gui=no`, and `-–enable-drivers=no` spelling is present |
| Scoped document-format attachment preservation script | Passed: 3 Korean-source PDF attachment URLs are preserved in the scoped English targets |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for the edited PHP page |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |

## Decision

S011 final decision: `COMPLETE`.
