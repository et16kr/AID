# S014 Tech Framework Integration Spring iBATIS

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S014 performs a semantic-unit audit for the Spring and iBATIS framework integration technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/54. Altibase Spring 연동 가이드__7340945.md` -> `arch/Home/Spring Integration Guide for Altibase__14058410.md`; `arch/Home/Spring Integration Guide for Altibase/**`
- `DOCK/Home/55. Altibase iBATIS 연동가이드__7340053.md` -> `arch/Home/iBatis Integration Guide for Altibase__14058303.md`; `arch/Home/iBatis Integration Guide for Altibase/**`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S014.md`
- `semantic-coverage/doc-mapping.tsv`
- The two Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S014-tech-framework-integration-spring-ibatis.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow area as `S014` moved to `Progress`.
- No uncommitted project files outside the workflow runtime area were present before S014 product-document edits.

## Design Note

S014 adds semantic evidence and makes scoped English source corrections:

- Adds `semantic-coverage/matrices/S014-tech-framework-integration-spring-ibatis.tsv`
- Adds `semantic-coverage/notes/S014-tech-framework-integration-spring-ibatis.md`
- Updates five scoped English iBATIS `arch/Home` pages
- Updates the edited page metadata in `manifest.json`

The product documentation structure is unchanged. The matrix records 63 semantic units covering Spring setup, JDBC driver setup, DataSource configuration, FailOver, multi-version connection, transaction management, JOTM/XA transactions, LOB handling, HelloSpring, iBATIS SqlMap/SqlMapConfig, ODBC/iBATIS.Net, stored procedures/functions, Spring+iBATIS integration, transaction management, appendix examples, and attachment evidence.

## Audit Summary

### D054 Spring

The split English Spring guide preserves:

- Spring Framework 3.2.x, Altibase v6.3.1, Eclipse, support contacts, and related integration guide references;
- Spring concepts and features including lightweight container, POJO, IoC/DI, AOP, transaction handling, and APIs;
- STS/Maven setup, `spring-context` dependency example, `Altibase.jar`, `Altibase5.jar`, `$ALTIBASE_HOME/lib`, JDBC/CMP compatibility checks, and latest-driver guidance;
- Eclipse and web-application JDBC driver placement procedures;
- `DriverManagerDataSource`, Jakarta DBCP `BasicDataSource`, `AltibaseConnectionPoolDataSource`, all property tables, required jar lists, and `jdbc:Altibase://IP:port_no/db_name`;
- FailOver URL properties including `AlternateServers`, `ConnectionRetryCount`, `ConnectionRetryDelay`, `SessionFailOver=off`, `LoadBalance=off`, STF/CTF behavior, and multi-version `Altibase.jar`/`Altibase5.jar` usage;
- `DataSourceTransactionManager`, `TransactionProxyFactoryBean`, transaction attribute rows, JOTM/JTA distributed transaction setup, `AltibaseXADataSource`, required JOTM jars, and LOB transaction requirements;
- the HelloSpring appendix and both Korean-source PDF attachment URLs.

No Spring English source change was required after direct S014 comparison.

### D055 iBATIS

The split English iBATIS guide preserves:

- iBATIS 2.3.4, Spring Framework 2.5.6, Altibase v5.3.3, Eclipse, support contacts, related guide references, and the Korean-source PDF attachment URL;
- iBATIS ORM concepts, SqlMap/SqlMapConfig flow, iBATIS download URL, `ibatis-2.3.4.726.zip`, `ibatis-2.3.4.726.jar`, and `ibatis-2.3.4.x.jar`;
- Person.xml CRUD SqlMap examples, SqlMapConfig settings and pool properties, iBATIS.Net ODBC setup with `Odbc2.0`, `DSN=Altibase5`, and the Windows ODBC guide reference;
- `SqlMapClient` application flow, `Altibase.jar`/`Altibase5.jar` driver handling, `java -jar Altibase.jar`, `altibase -v`, CM/CMP compatibility, Eclipse setup, SqlMapConfig dataSource setup, FailOver properties, and multi-version driver loading order;
- stored procedure/function examples for `sum_proc`, `sum_func`, `ProcedureParam`, `FunctionParam`, and `<procedure>` calls;
- Spring+iBATIS `SqlMapClientFactoryBean` integration, Spring-side and iBATIS-side dataSource setup, `AltibaseConnectionPoolDataSource`, iBATIS/Spring transaction handling, and LOB handling with `CLOB`/`BLOB`, `setAutoCommit(false)`, propagation rules, and `LobLocator can not span the transaction 101858625`;
- the SimpleConnection appendix with `PERSON`, `PERSON_SEQ`, Person.xml, db.properties, SqlMapConfigExample.xml, Person.java, PersonApp.java, jar setup, and run procedure.

S014 corrected the English iBATIS source for:

- iBATIS 2.3.4 jar consolidation wording;
- CRUD tag explanation wording and the ODBC guide title;
- multi-version driver load-order wording and Procedure/Function introduction wording;
- a stray `spring-jdbc.jar, spring-orm.jar,` export artifact, `SpringIbatisConnection1` sample name, iBATIS-side `<transactionManager>` wording, `AltibaseConnectionPoolDataSource`, `setAutoCommit(false)`, transaction method names, and `TransactionSample`'s `PersonApp.java` filename;
- the appendix `Altibasein` fused-word typo.

## Attachment And Link Evidence

URL-backed document-format attachments in this scope:

- `ALTIBASE_Spring_연동가이드.pdf`: Korean-source URL preserved in `arch/Home/Spring Integration Guide for Altibase__14058410.md`
- `ALTIBASE_Spring_연동가이드_2.5.pdf`: Korean-source URL preserved in `arch/Home/Spring Integration Guide for Altibase__14058410.md`
- `ALTIBASE_iBATIS_연동가이드.pdf`: Korean-source URL preserved in `arch/Home/iBatis Integration Guide for Altibase__14058303.md`

The Korean iBATIS source also names `iBATIS-SqlMaps-2-ko.pdf` three times without a downloadable URL. S014 records those rows as `source_limitation` and does not invent a URL. The English target keeps the corresponding `iBATIS-SqlMaps-2-en.pdf` filename references.

Embedded screenshots were reviewed as source-exported illustrations. The audit matrix records the surrounding semantic unit rather than treating every screenshot URL as independent technical prose.

## Self-Review

- Scope checked: S014 changed only scoped English iBATIS pages, `manifest.json`, S014 evidence files, and S014 workflow status.
- Korean authority checked: both scoped Korean source files were inspected directly with line-numbered reads.
- English target checked: all mapped English parent and split pages were inspected directly.
- Matrix checked: the S014 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `Altibase.jar`, `Altibase5.jar`, `Altibase5.jdbc.driver.AltibaseDriver`, `Altibase.jdbc.driver.AltibaseDriver`, `AltibaseConnectionPoolDataSource`, `SqlMapClientFactoryBean`, `setAutoCommit(false)`, `startTransaction()`, `commitTransaction()`, `endTransaction()`, `SessionFailOver=off`, STF/CTF, `PROPAGATION_REQUIRED`, `PROPAGATION_REQUIRES_NEW`, `PROPAGATION_NESTED`, `LobLocator can not span the transaction 101858625`, and exact PDF attachment URLs are preserved.
- Product docs checked: edited page metadata in `manifest.json` matches the updated files.

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
| S014 TSV header and column-count check | Passed: 63 data rows, 15 columns each |
| S014 coverage status check | Passed: 45 `covered`, 10 `added`, 5 `not_applicable`, 3 `source_limitation` |
| S014 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped English empty-link and macro-artifact scan | Passed with exit code 1, meaning no matches |
| Scoped stale-pattern scan for fixed iBATIS issues | Passed with exit code 1, meaning no matches |
| Scoped residual Korean scan in English targets | Passed with exit code 1, meaning no visible Korean text remains in scoped English pages |
| Scoped document-format attachment preservation grep | Passed: 3 Korean-source PDF attachment URLs are preserved in the scoped English parent targets |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 5 edited English pages |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |

## Decision

S014 final decision: `COMPLETE`.
