# S012 Tech WAS Integration Tomcat JEUS JBoss

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S012 performs a semantic-unit audit for the TOMCAT, JEUS, and JBoss WAS integration technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/28. Altibase TOMCAT 연동가이드__7341030.md` -> `arch/Home/TOMCAT Integration Guide for Altibase__14058489.md`; `arch/Home/TOMCAT Integration Guide for Altibase/**`
- `DOCK/Home/29. Altibase JEUS 연동가이드__7341028.md` -> `arch/Home/JEUS Integration Guide for Altibase__14058459.md`; `arch/Home/JEUS Integration Guide for Altibase/**`
- `DOCK/Home/30. Altibase JBoss 연동가이드__13437492.md` -> `arch/Home/JBOSS Integration Guide for Altibase__14647358.md`; `arch/Home/JBOSS Integration Guide for Altibase/**`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `semantic-coverage/doc-mapping.tsv`
- The three Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S012-tech-was-integration-tomcat-jeus-jboss.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow runtime area.
- No uncommitted project files outside the workflow runtime area were present before S012 product-document edits.

## Design Note

S012 adds semantic evidence and makes scoped source-preservation/document-quality corrections:

- Adds `semantic-coverage/matrices/S012-tech-was-integration-tomcat-jeus-jboss.tsv`
- Adds `semantic-coverage/notes/S012-tech-was-integration-tomcat-jeus-jboss.md`
- Updates six scoped English `arch/Home` pages
- Updates the edited page metadata in `manifest.json`

The product documentation structure is unchanged. The matrix records 73 semantic units covering overview/support information, installation prerequisites, environment variables, JDBC driver placement and compatibility, JNDI/DataSource configuration, connection pool settings, failover behavior, warnings, error remedies, sample JSP code, deployment procedures, and attachment evidence.

## Audit Summary

### D028 TOMCAT

The split English TOMCAT guide preserves:

- Altibase v6.3 or later and TOMCAT v7.0 test scope, support contacts, TOMCAT 7 installation prerequisites, startup/shutdown commands, and environment variables;
- `Altibase.jar` and `Altibase5.jar` guidance, JDBC/CMP compatibility checks, and driver placement through `CLASSPATH` or `$CATALINA_HOME/lib`;
- JNDI DataSource `context.xml`, `WEB-INF/web.xml`, resource attribute table, JNDI lookup examples, JNDI JSP example, and general JDBC JSP example;
- Altibase FailOver version condition (`Altibase v5.3.3`), `AlternateServers`, `ConnectionRetryCount`, `ConnectionRetryDelay`, `SessionFailOver=off`, `LoadBalance=off`, CTF/STF semantics, and Replication Manual reference;
- TOMCAT DBCP warnings, access-log check procedure, `testOnBorrow`, `poolPrepareStatements`, explicit resource close guidance, connection-pool leak handling, and common error remedies.

S012 corrected the TOMCAT binary filename to `apache-tomcat-7.0.56.tar.gz`, restored the Korean-source list of three integration approaches, and restored `NONE` plus `READ COMMITTED` in `defaultTransactionIsolation`.

### D029 JEUS

The split English JEUS guide preserves:

- Altibase v6.3.1 and JEUS6.0 scope, JEUS install modes, JDK 5.0 Update 4 requirement, console install sequence, environment variable table, and JEUS startup/shutdown validation;
- JEUS home directory descriptions, wrong-OS installation error, GLIBC lower-than-2.4 installation error, and Linux-only applicability;
- `Altibase.jar` and `Altibase5.jar` guidance, `$JEUS_HOME/lib/datasource` driver placement, connection pooling benefits, and four data-source types;
- JEUSMain.xml data-source tag table, `ABConnectionPoolDataSource`, `AltibaseConnectionPoolDataSource`, `BlackboxConnectionPoolDataSource`, ClassNotFoundException warning, and XML/WebAdmin setup methods;
- Blackbox and AltibaseConnectionPoolDataSource XML/WebAdmin examples, URL/Url case warning, `initialPoolSize` deadlock caution, check-query settings, `dsinfo`, `dsconinfo`, `testdsconfig`, sample JSPs, and WebAdmin deployment steps.

S012 restored the `Sessiondb` first-boot creation condition, corrected `GLIBC`, corrected the `ALTIBASE 6.1.1 or lower` class-version condition, fixed the DBMS/DataSource selection order, and corrected the `Usecount` description.

### D030 JBoss

The split English JBoss guide preserves:

- Altibase 6.5.1 and JBoss 6.1.0.Final scope, JDK 1.6-or-later requirement, JDK 1.7 test environment, package download/unzip procedure, `JBOSS_HOME`, and Windows/Unix JDK setup;
- JBoss directory structure, startup/shutdown commands, expected `Started` output, web-console/admin-console access, and port-conflict error/remedy;
- JDBC driver location and `JBOSS_HOME/common/lib` restart requirement, DataSource parameter table, local and distributed transaction examples, and `JBOSS_HOME/docs/jca` reference;
- JBoss and Altibase failover methods, CTF-only JBoss syntax, Altibase v5.3.3-or-later FailOver syntax, `AlternateServers`, `ConnectionRetryCount`, `ConnectionRetryDelay`, `LoadBalance=off`, and `SessionFailOver=off`;
- JSP sample, existing-WAR test path, Eclipse WAR creation, JBoss web-console upload, automatic deploy, and run URL examples.

S012 corrected `run.bat`, converted malformed server URL examples to literal URL templates, restored the existing-WAR directory to `JBOSS_HOME/server/default/deploy`, and fixed unclear WAR execution wording.

## Attachment Evidence

URL-backed document-format attachments in this scope:

- `ALTIBASE_TOMCAT연동_가이드.pdf`: Korean-source URL preserved in `arch/Home/TOMCAT Integration Guide for Altibase__14058489.md`
- `ALTIBASE_TOMCAT_연동_가이드_5.5.pdf`: Korean-source URL preserved in `arch/Home/TOMCAT Integration Guide for Altibase__14058489.md`
- `ALTIBASE_JEUS_연동_가이드.pdf`: Korean-source URL preserved in `arch/Home/JEUS Integration Guide for Altibase__14058459.md`
- `ALTIBASE_JEUS_연동_가이드_6.0.pdf`: Korean-source URL preserved in `arch/Home/JEUS Integration Guide for Altibase__14058459.md`

The JBoss Korean source has embedded images but no URL-backed document-format attachments in the scoped extensions. Embedded images were reviewed as source-exported illustrations.

## Self-Review

- Scope checked: S012 changed only scoped English pages, `manifest.json`, S012 evidence files, and S012 workflow status.
- Korean authority checked: all three scoped Korean source files were inspected directly with line-numbered reads.
- English target checked: all mapped English parent and split pages were inspected directly.
- Matrix checked: the S012 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `Altibase.jar`, `Altibase5.jar`, `Altibase.jdbc.driver.AltibaseDriver`, `ABConnectionPoolDataSource`, `AltibaseConnectionPoolDataSource`, `BlackboxConnectionPoolDataSource`, `SessionFailOver=off`, `AlternateServers`, CTF/STF, `JBOSS_HOME`, `JEUS_BASSPORT`, `testOnBorrow`, `poolPrepareStatements`, and exact PDF attachment URLs are preserved.
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
| S012 TSV header and column-count check | Passed: 73 data rows, 15 columns each |
| S012 coverage status check | Passed: 56 `covered`, 11 `added`, 6 `not_applicable` |
| S012 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped English empty-link and macro-artifact scan | Passed with exit code 1, meaning no matches |
| Scoped stale-pattern scan for fixed TOMCAT/JEUS/JBoss issues | Passed with exit code 1, meaning no matches in scoped English targets |
| Scoped residual Korean scan in English targets | Passed with exit code 1, meaning no matches |
| Scoped document-format attachment preservation script | Passed: 4 Korean-source PDF attachment URLs are preserved in the scoped English parent targets |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 6 edited English pages |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |

## Decision

S012 final decision: `COMPLETE`.
