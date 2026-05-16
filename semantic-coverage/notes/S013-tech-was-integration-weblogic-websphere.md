# S013 Tech WAS Integration WebLogic WebSphere

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S013 performs a semantic-unit audit for the WebLogic and WebSphere WAS integration technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/52. Altibase WebSphere 연동 가이드__13435602.md` -> `arch/Home/WebSphere Integration Guide for Altibase__14058343.md`
- `DOCK/Home/60. Altibase WebLogic 연동가이드__7340101.md` -> `arch/Home/WEBLOGIC Integration Guide for Altibase__14058319.md`; `arch/Home/WEBLOGIC Integration Guide for Altibase/**`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `semantic-coverage/doc-mapping.tsv`
- The two Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S013-tech-was-integration-weblogic-websphere.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow area as `S013` moved to `Progress`.
- No uncommitted project files outside the workflow runtime area were present before S013 product-document edits.

## Design Note

S013 adds semantic evidence and makes scoped source-preservation/document-quality corrections:

- Adds `semantic-coverage/matrices/S013-tech-was-integration-weblogic-websphere.tsv`
- Adds `semantic-coverage/notes/S013-tech-was-integration-weblogic-websphere.md`
- Updates four scoped English `arch/Home` pages
- Updates the edited page metadata in `manifest.json`

The product documentation structure is unchanged. The matrix records 76 semantic units covering overview/support information, WebSphere installation, WebLogic glossary and prerequisites, startup/shutdown scripts, JDBC driver acquisition/version checks/classpath setup, JDBC data-source creation, connection pool settings, sample web applications, FailOver/Load-Balancing behavior, error remedies, and attachment evidence.

## Audit Summary

### D052 WebSphere

The English WebSphere guide preserves:

- Altibase v7.1.0 and WebSphere v9.0 scope, support contacts, IBM Installation Manager 1.8.5, IBM repository URLs, Java and Internet Explorer download notes, WebSphere Customization Toolbox 9.0, profile creation, and management-security behavior;
- `WAS_INSTALL_ROOT`, `C:\IBM\WebSphere\AppServer`, Profile semantics, the profile directory table, `Resource.xml`, `cell`, `node`, and `server` configuration scope;
- `startServer.bat`, `stopServer.bat`, `server1`, admin console URL `http://SERVER_IP:9060/ibm/console`, management port 9060, and application port 9080;
- `Altibase.jar`, `$ALTIBASE_HOME/lib`, JDBC driver CMP checks, `Altibase -v`, `${WAS_INSTALL_ROOT}\universalDriver\lib`, `Altibase.jdbc.driver.AltibaseConnectionPoolDataSource`, and `Altibase.jdbc.driver.ABConnectionPoolDataSource` for Altibase 6.1.1 and earlier;
- `altitest`, `jdbc/altitest`, required data-source properties, connection testing, WAR registration, Eclipse WAR creation, `select * from dual`, and WebSphere FailOver testing with `jdbc/Altibase`.

S013 corrected the WebSphere English source for the `tranlog` transaction-log description, unclear JDBC provider completion wording, prose accidentally fenced as code, the `WARD` typo, WAR URL parameter wording, the Altibase v5.3.3 FailOver sentence, the FailOver URL literal, and the seconds unit for `ConnectionRetryDelay`.

### D060 WebLogic

The split English WebLogic guide preserves:

- Windows WebLogic 12.1.3.0 scope, Oracle documentation link, related development guide references, support contacts, WebLogic glossary, WebLogic 8.1.6.0 minimum recommendation, JDBC 3.0/JDK 1.4 basis, JDBC 4.0 warning, and API Manual warning;
- WebLogic download/install/domain creation flow, `WL_HOME`, `DOMAIN_HOME`, development mode, `$DOMAIN_HOME/autodeploy`, default port 7001, `startWebLogic.cmd`, `stopWebLogic.cmd`, `startManagedWebLogic.cmd`, and `stopManagedWebLogic.cmd`;
- `Altibase.jar`, `Altibase5.jar`, `$ALTIBASE_HOME/lib`, support download, `altibase -v`, `java -jar Altibase.jar`, CM/CMP compatibility, `$DOMAIN_HOME/lib`, `CLASSPATH`, and `startWebLogic.cmd` classpath setup;
- WebLogic data-source creation, `Altibase.jdbc.driver.AltibaseDriver`, `Altibase#.jdbc.driver.AltibaseDriver`, `jdbc:Altibase://127.0.0.1:20300/mydb`, Altibase 4 `user=sys`, `dual`, configuration testing, connection-pool `Initial Capacity`, and `v$session` verification;
- `web.xml`, `$DOMAIN_HOME/autodeploy`, `welcome.html`, `singleVersion.jsp`, `multiVersion.jsp`, `altibase`, `altibase5`, `altibase6`, renamed driver table, WebLogic multi-data-source FailOver/Load-Balancing, Altibase v5.3.3 FailOver/Load-Balancing, and integration error remedies.

S013 corrected WebLogic English source for the domain-definition second case, `Managed Server` terminology, the shutdown warning meaning, the single-version verification wording (`without error`), and the multi-version JDBC driver setup sentence so it includes the current ALTIBASE driver as well as ALTIBASE 5 and ALTIBASE 6.

## Attachment Evidence

URL-backed document-format attachments in this scope:

- `ALTIBASE_Websphere_연동가이드.pdf`: Korean-source URL preserved in `arch/Home/WebSphere Integration Guide for Altibase__14058343.md`
- `ALTIBASE_WebLogic_연동_가이드_12c.pdf`: Korean-source URL preserved in `arch/Home/WEBLOGIC Integration Guide for Altibase__14058319.md`
- `ALTIBASE_WebLogic_연동_가이드_10.3.pdf`: Korean-source URL preserved in `arch/Home/WEBLOGIC Integration Guide for Altibase__14058319.md`

Embedded screenshots were reviewed as source-exported illustrations. The audit matrix records the surrounding semantic unit rather than treating every screenshot URL as independent technical prose.

## Self-Review

- Scope checked: S013 changed only scoped English pages, `manifest.json`, S013 evidence files, and S013 workflow status.
- Korean authority checked: both scoped Korean source files were inspected directly with line-numbered reads.
- English target checked: the WebSphere target page and all mapped WebLogic parent/child pages were inspected directly.
- Matrix checked: the S013 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `WAS_INSTALL_ROOT`, `Altibase.jar`, `Altibase5.jar`, `$ALTIBASE_HOME`, `$DOMAIN_HOME`, `WL_HOME`, `CLASSPATH`, `Altibase.jdbc.driver.AltibaseDriver`, `Altibase.jdbc.driver.AltibaseConnectionPoolDataSource`, `Altibase.jdbc.driver.ABConnectionPoolDataSource`, `Altibase5.jdbc.driver.AltibaseDriver`, `AlternateServers`, `ConnectionRetryCount`, `ConnectionRetryDelay`, `SessionFailOver=off`, CTF/STF, and exact PDF attachment URLs are preserved.
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
| S013 TSV header and column-count check | Passed: 76 data rows, 15 columns each |
| S013 coverage status check | Passed: 60 `covered`, 12 `added`, 4 `not_applicable` |
| S013 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped English empty-link and macro-artifact scan | Passed with exit code 1, meaning no matches |
| Scoped stale-pattern scan for fixed WebLogic/WebSphere issues | Passed with exit code 1, meaning no matches |
| Scoped residual Korean scan in English targets | Passed with exit code 1, meaning no visible Korean text remains in scoped English pages |
| Scoped document-format attachment preservation script | Passed: 3 Korean-source PDF attachment URLs are preserved in the scoped English parent targets |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 4 edited English pages |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |

## Decision

S013 final decision: `COMPLETE`.
