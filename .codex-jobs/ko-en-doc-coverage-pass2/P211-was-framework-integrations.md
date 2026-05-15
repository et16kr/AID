# P211 WAS and Framework Integrations Audit

Date: 2026-05-16

## Scope

P211 audited Korean TOMCAT, JEUS, JBoss, WebLogic, WebSphere, Spring, iBATIS, MyBatis, and Hibernate integration documents against their English `arch` targets.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/28. Altibase TOMCAT 연동가이드__7341030.md` | `arch/Home/TOMCAT Integration Guide for Altibase__14058489.md`; `arch/Home/TOMCAT Integration Guide for Altibase/**` |
| `DOCK/Home/29. Altibase JEUS 연동가이드__7341028.md` | `arch/Home/JEUS Integration Guide for Altibase__14058459.md`; `arch/Home/JEUS Integration Guide for Altibase/**` |
| `DOCK/Home/30. Altibase JBoss 연동가이드__13437492.md` | `arch/Home/JBOSS Integration Guide for Altibase__14647358.md`; `arch/Home/JBOSS Integration Guide for Altibase/**` |
| `DOCK/Home/52. Altibase WebSphere 연동 가이드__13435602.md` | `arch/Home/WebSphere Integration Guide for Altibase__14058343.md` |
| `DOCK/Home/54. Altibase Spring 연동 가이드__7340945.md` | `arch/Home/Spring Integration Guide for Altibase__14058410.md`; `arch/Home/Spring Integration Guide for Altibase/**` |
| `DOCK/Home/55. Altibase iBATIS 연동가이드__7340053.md` | `arch/Home/iBatis Integration Guide for Altibase__14058303.md`; `arch/Home/iBatis Integration Guide for Altibase/**` |
| `DOCK/Home/58. Altibase Hibernate 연동가이드__14057878.md` | `arch/Home/Hibernate Integration Guide for Altibase__14058388.md` |
| `DOCK/Home/60. Altibase WebLogic 연동가이드__7340101.md` | `arch/Home/WEBLOGIC Integration Guide for Altibase__14058319.md`; `arch/Home/WEBLOGIC Integration Guide for Altibase/**` |
| `DOCK/Home/64. Altibase MyBatis 연동 가이드__7340818.md` | `arch/Home/MyBatis Integration Guide for Altibase__14058349.md`; `arch/Home/MyBatis Integration Guide for Altibase/**` |

The Korean sources were treated as authoritative. No Korean source documents were edited.

## Boundary

- Completed only P211.
- Preserved existing English parent and split-page hierarchy.
- Did not enter SQL tuning, migration/conversion, FAQ, attachment-wide revalidation, or final LLM consolidation jobs.
- The pre-existing pass2 `jobs.tsv` status change for P211 was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior or repository architecture changed. Documentation structure changes were limited to making a flattened JEUS directory paragraph into searchable bullets and renaming the mistranslated WebLogic `Arrangement` heading to `Deploying`. Existing source-page identities, file paths, and Korean sources were preserved.

## Findings And Updates

- Corrected malformed technical-support links in TOMCAT, JEUS, JBoss, Spring, iBATIS, MyBatis, Hibernate, WebLogic, and WebSphere parent pages while preserving the Korean-source support route.
- Corrected TOMCAT integration wording for JDBC driver placement, `ConnectionPool`/`Resource`, JNDI DataSource wording, Korean-source TOMCAT failover limitation, Altibase v5.3.3 wording, `context.xml`, `SessionFailOver=off`, `testOnBorrow`, `poolPrepareStatements`, and connection-pool leak/GC cautions.
- Corrected JEUS installation and data-source content for directory structure readability, XA/local-XA wording, `ABConnectionPoolDataSource`/`AltibaseConnectionPoolDataSource`/`BlackboxConnectionPoolDataSource`, complete JDBC data source class names, and `initialPoolSize` deadlock caution.
- Corrected JBoss installation and failover content for JDK requirements, missing package-extraction detail, broken image placeholders from the Korean source, `JBOSS_HOME`, JBoss startup wording, DBMS-in-use wording, and `SessionFailOver=off`.
- Corrected WebSphere wording for Altibase/WebSphere versions, IBM Installation Manager, Internet Explorer download note, installer execution, `$ALTIBASE_HOME`, and application URL spelling.
- Corrected Spring data source, failover, multi-version, transaction, LOB, and HelloSpring content for exact file names, URLs, class names, `ConnectionRetryDelay`, CTF/STF semantics, `$ALTIBASE_HOME`, `TransactionProxyFactoryBean`, `AltibaseXADataSource`, JOTM URL, and sample class/file names.
- Corrected iBATIS content for download URLs, `ibatis-2.3.4.726.zip`, `ibatis-2.3.4.726.jar`, `ibatis-2.3.4.x.jar`, JDBC driver selection, Eclipse setup text, connection URL literals, `SessionFailOver=off`, multi-version filenames, Spring jar names, and LOB error text.
- Corrected MyBatis and Hibernate details for support text, JDBC driver class-name wording, exact LOB error text, and Hibernate `SessionFailOver=off`.
- Corrected WebLogic prerequisites, setup, JDBC data-source, deployment, multi-version, failover/load-balancing, and error pages for unsupported JDBC specifications, `WL_HOME`, `$DOMAIN_HOME/autodeploy`, UI label artifacts, URL literal, renamed driver class `Altibase5.jdbc.driver.AltibaseDriver`, Altibase v5.3.3 library-layer failover/load-balancing note, and ALTIBASE 4 connection target wording.
- Updated `manifest.json` metadata for all 33 edited English Markdown pages.

## Attachment And Link Evidence

- Scoped Korean source pages contain 12 URL-backed document-format attachment filenames.
- All 12 Korean-source document-format attachment filenames are preserved in the scoped English target set:
  - `ALTIBASE_TOMCAT_연동_가이드_5.5.pdf`
  - `ALTIBASE_TOMCAT연동_가이드.pdf`
  - `ALTIBASE_JEUS_연동_가이드.pdf`
  - `ALTIBASE_JEUS_연동_가이드_6.0.pdf`
  - `ALTIBASE_Websphere_연동가이드.pdf`
  - `ALTIBASE_Spring_연동가이드.pdf`
  - `ALTIBASE_Spring_연동가이드_2.5.pdf`
  - `ALTIBASE_iBATIS_연동가이드.pdf`
  - `ALTIBASE_Hibernate_연동가이드.pdf`
  - `ALTIBASE_WebLogic_연동_가이드_10.3.pdf`
  - `ALTIBASE_WebLogic_연동_가이드_12c.pdf`
  - `ALTIBASE_MyBatis_연동가이드.pdf`
- Scoped grep found no empty links, Confluence macro errors, broken image placeholders, malformed support links, stale typo patterns checked for this job, or residual visible Korean text.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p211-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, broken image placeholders, malformed support links, stale typo patterns, and residual Korean text | Passed |
| Scoped document-format attachment preservation script | Passed, 12 Korean source filenames preserved |
| Scoped fenced-code balance check | Passed for all 51 scoped English files |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 33 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P211 used grep-based source-link and attachment preservation checks.
- Source-exported attachment and image URLs may retain URL-encoded Korean filenames; visible English prose was checked separately.
- Some legacy WAS/framework examples retain old framework or product versions because the Korean source does so and this job did not modernize beyond Korean-source parity.
