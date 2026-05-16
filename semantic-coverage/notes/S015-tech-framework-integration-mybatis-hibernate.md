# S015 Tech Framework Integration MyBatis Hibernate

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S015 performs a semantic-unit audit for the Hibernate and MyBatis framework integration technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/58. Altibase Hibernate 연동가이드__14057878.md` -> `arch/Home/Hibernate Integration Guide for Altibase__14058388.md`
- `DOCK/Home/64. Altibase MyBatis 연동 가이드__7340818.md` -> `arch/Home/MyBatis Integration Guide for Altibase__14058349.md`; `arch/Home/MyBatis Integration Guide for Altibase/**`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S015.md`
- `semantic-coverage/doc-mapping.tsv`
- The two Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S015-tech-framework-integration-mybatis-hibernate.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow area as `S015` moved to `Progress`.
- No uncommitted project files outside the workflow runtime area were present before S015 product-document edits.

## Design Note

S015 adds semantic evidence and makes scoped English source corrections:

- Adds `semantic-coverage/matrices/S015-tech-framework-integration-mybatis-hibernate.tsv`
- Adds `semantic-coverage/notes/S015-tech-framework-integration-mybatis-hibernate.md`
- Updates one scoped Hibernate English page
- Updates six scoped MyBatis English pages
- Updates edited page metadata in `manifest.json`

The product documentation structure is unchanged. The matrix records 70 semantic units covering Hibernate overview, mapping/configuration, AltibaseDialect porting, JDBC driver setup, FailOver, multi-version driver loading, Spring integration, connection pool behavior, transactions, LOB handling, stored procedure/function calls, NativeSQL, appendices, MyBatis/iBatis differences, Mapper/Configuration files, Altibase integration, Spring-MyBatis integration, transaction management, LOB and duplicate insert issues, and attachment evidence.

## Audit Summary

### D058 Hibernate

The English Hibernate guide preserves:

- Hibernate/Hibernate+Spring integration scope, support contacts, Hibernate ORM concept, architecture reference, and Hibernate 5.4.8 download basis;
- hibernate-mapping and hibernate-configuration examples, including `Person.hbm.xml`, `Hibernate.cfg.xml`, `PERSON_SEQ`, `sequence_name`, connection properties, and `org.hibernate.dialect.AltibaseDialect`;
- application DML flow using `SessionFactory`, `Session`, `Transaction`, `session.save()`, `session.update()`, `session.delete()`, `session.get()`, and `session.createCriteria()`;
- AltibaseDialect porting through `ALTIBASE_DIALECT_PORTING.md`, `AltibaseDialect.java`, `AltibaseLimitHandler.java`, `SequenceInformationExtractorAltibaseDatabaseImpl.java`, `javac`, and `jar -cvfm`;
- Altibase JDBC driver location, `Altibase.jar`, `Altibase5.jar`, `$ALTIBASE_HOME/lib`, CM/CMP compatibility commands, and Eclipse classpath setup;
- FailOver URL properties, STF/CTF behavior, and multi-version driver load order with `Altibase5.jdbc.driver.AltibaseDriver`;
- Hibernate+Spring dataSource and Hibernate property configuration, connection pool limitation, transaction handling, LOB handling, CallableStatement procedure/function calls, NativeSQL `MOVE`, appendix Java/XML examples, and legacy PDF attachment.

S015 corrected the English Hibernate source for:

- `Person.hbm.xml` sample labeling;
- malformed/misleading property prose such as `connection.driver_driver_class`, `mapping-resource`, and `hibernate Properties`;
- sample titles and file names including `Person.java`, `NativeSQLApp.java`, and `examples.domain`;
- LOB type mapping prose, `java.sql.SQLException` casing, and required-jar references;
- the related Spring guide wording and connection pool narrative.

The Korean Hibernate source has one internal class-name inconsistency: prose names `AltibaseConnectionPoolDataSource`, while the sample code uses `Altibase.jdbc.driver.ABConnectionPoolDataSource`. The English target now preserves both source identifiers and records the risk in the matrix rather than inventing a single corrected class.

### D064 MyBatis

The split English MyBatis guide preserves:

- MyBatis 3.2.8, Altibase 6.3.1, Eclipse, Maven, support contacts, related guide references, and the Korean-source PDF attachment URL;
- MyBatis concept and architecture, official MyBatis sites, the Korean MyBatis reference page, dependency snippet for `org.mybatis:mybatis:3.2.8`, and Maven appendix reference;
- iBatis/MyBatis differences including JDK requirements, package names, `parameterMap` deprecation, terminology changes, and namespace requirements;
- Mapper XML CRUD examples, `mybatis-config.xml`, `db.properties`, `typeAliases`, `transactionManager`, `dataSource`, `mappers`, multiple-DB configuration, `SqlSessionFactory`, `openSession(false)`, and Mapper id usage;
- Altibase JDBC driver setup, compatibility commands, DataSource configuration, FailOver properties including `Healthcheckduration` and `Failover_source`, multi-version `Altibase5.jar` setup, stored procedure/function calls with `statementType="CALLABLE"`, and required MyBatis jars;
- Spring-MyBatis integration setup, `mybatis-spring-1.x.x.jar` compatibility table, `SqlSessionFactoryBean`, `DataSourceTransactionManager`, connection pool examples, transaction management, LOB handling, `useGeneratedKeys` duplicate insert issue, and both appendices.

S015 corrected the English MyBatis source for:

- missing `iBatis Integration Guide for Altibase` in the related document list;
- the Korean MyBatis reference page link;
- `CRUB` typo and missing delete wording in the sample application explanation;
- required MyBatis jar references in FailOver, Procedure, Function, and multi-version sections;
- unclear MyBatis LOB transaction wording around `<transactionManager>`;
- Appendix 2 capitalization and procedure text, including `UserServiceImpl.java`.

The Korean MyBatis source names `MyBatis-3-User-Guide_ko.pdf` three times without a downloadable URL. S015 records those rows as `source_limitation` and does not invent a URL. The source also uses `ibatis-2.3.4.x.jar` and `mybatis.3.2.8.jar` in a few MyBatis required-jar sentences; S015 corrected the English target to the intended `mybatis-3.2.8.jar`, consistent with the rest of the scoped Korean document and the MyBatis dependency section.

## Attachment And Link Evidence

URL-backed document-format attachments in this scope:

- `ALTIBASE_Hibernate_연동가이드.pdf`: Korean-source URL preserved in `arch/Home/Hibernate Integration Guide for Altibase__14058388.md`
- `ALTIBASE_MyBatis_연동가이드.pdf`: Korean-source URL preserved in `arch/Home/MyBatis Integration Guide for Altibase__14058349.md`

Source-limited filename-only references:

- `MyBatis-3-User-Guide_ko.pdf`: named in the Korean MyBatis source without a downloadable URL in the Markdown export.

Embedded screenshots were reviewed as source-exported illustrations. The audit matrix records the surrounding semantic unit rather than treating every screenshot URL as independent technical prose.

## Self-Review

- Scope checked: S015 changed only scoped English Hibernate/MyBatis pages, `manifest.json`, S015 evidence files, and S015 workflow status.
- Korean authority checked: both scoped Korean source files were inspected directly with line-numbered reads.
- English target checked: all mapped English parent and split pages were inspected directly.
- Matrix checked: the S015 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `Altibase.jar`, `Altibase5.jar`, `Altibase5.jdbc.driver.AltibaseDriver`, `Altibase.jdbc.driver.AltibaseDriver`, `AltibaseDialect`, `AltibaseConnectionPoolDataSource`, `ABConnectionPoolDataSource`, `SqlSessionFactory`, `SqlSessionFactoryBean`, `DataSourceTransactionManager`, `SessionFailOver=off`, `Healthcheckduration`, `Failover_source`, `V$SESSION`, `jdbcType=BLOB`, `jdbcType=CLOB`, `setAutoCommit(false)`, `openSession(false)`, `LobLocator can not span the transaction 101858625`, and exact PDF attachment URLs are preserved.
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
| S015 TSV header and column-count check | Passed: 70 data rows, 15 columns each |
| S015 coverage status check | Passed: 40 `covered`, 23 `added`, 4 `not_applicable`, 3 `source_limitation` |
| S015 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped English empty-link and macro-artifact scan | Passed with exit code 1, meaning no matches |
| Scoped stale-pattern scan for corrected Hibernate/MyBatis issues | Passed with exit code 1, meaning no matches |
| Scoped residual Korean scan in English targets | Passed with exit code 1, meaning no visible Korean text remains in scoped English pages |
| Scoped document-format attachment preservation grep | Passed: 2 Korean-source PDF attachment URLs are preserved in the scoped English parent targets |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |

## Decision

S015 final decision: `COMPLETE`.
