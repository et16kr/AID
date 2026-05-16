# LLM Reference Consolidation Workflow Requirements

## Purpose

Create a reviewed English reference package that GPTs, Codex, and other LLMs can use as the canonical Altibase knowledge base. The package must preserve Korean-source meaning through the reviewed English source set, keep exact technical identifiers stable, and remain easy for humans to review.

## Output Directory

All final package files are created under `llm-reference/`. Do not delete, move, or rename original source documents under `DOCK/`, `faq/`, `arch/`, or `FAQE/`.

Expected outputs:

- `llm-reference/README.md`
- `llm-reference/source-index.md`
- `llm-reference/00-source-classification.md`
- `llm-reference/01-installation-upgrade-platform.md`
- `llm-reference/02-architecture-storage-concepts.md`
- `llm-reference/03-operation-administration-security.md`
- `llm-reference/04-backup-recovery.md`
- `llm-reference/05-replication-ha.md`
- `llm-reference/06-monitoring-diagnostics.md`
- `llm-reference/07-troubleshooting-error-messages.md`
- `llm-reference/08-sql-performance-tuning.md`
- `llm-reference/09-development-client-api.md`
- `llm-reference/10-application-framework-integration.md`
- `llm-reference/11-migration-conversion-tools.md`
- `llm-reference/12-terminology-multilingual-preservation.md`
- `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
- `llm-reference/HANDOFF.md`

## Source Classification

- `Korean-source-verified`: `arch/Home` and Korean-core `FAQE/Home` material reviewed in pass2.
- `Link-validated Korean-source-verified`: Korean-source-verified material whose attachments and links were checked in P223/P224.
- `English-only source`: `FAQE/Home/ALTIBASE HDB*`, `FAQE/Home/Altibase Error Messages/**`, and `FAQE/Home/Altibase Error Messages__6979655.md` unless later explicitly audited against Korean sources.
- `Legacy attachment label only`: source has a `#` attachment label with no downloadable URL.
- `Diagram unavailable`: Gliffy or other exported diagram content is unavailable and must not be reconstructed from guesswork.

## Job Details

### L001 - Source readiness cleanup

Goal: Fix known residual source issues before consolidation.

Scope:

- Correct real untranslated Korean residues in these English auxiliary files:
  - `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-2 SQL Conversion__14647324.md`
  - `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-3 Stored Procedure _ Function Conversion__14647326.md`
- Preserve intentional Korean attachment filenames and Korean sample data.
- Update `manifest.json` metadata for edited source documents if body length or word count changes.
- Add a short note to `PASS2_KO_EN_DOC_REVIEW_REPORT.md` or a new local validation note if the cleanup materially changes pass2 risk status.

Acceptance:

- `rg -n "[가-힣]" arch/Home FAQE/Home` has only intentional Korean filenames, URLs, or sample data.
- `python3 -m json.tool manifest.json` and `git diff --check` pass.

### L002 - Package scaffold and source index

Goal: Create the package skeleton and source policy used by later jobs.

Outputs:

- `llm-reference/README.md`
- `llm-reference/source-index.md`
- `llm-reference/00-source-classification.md`

Use:

- `LLM_REFERENCE_REVIEW_PLAN.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`

Acceptance:

- All expected topic output files are listed with owner job and source status.
- Source classification rules are explicit.
- No topic content is deeply drafted yet, except brief package-level guidance.

### L003 - Installation upgrade platform reference

Output: `llm-reference/01-installation-upgrade-platform.md`

Primary sources:

- `arch/Home/Altibase Installation Guide__14647632.md`
- `arch/Home/Altibase Installation Guide/**`
- `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md`
- `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md`
- `arch/Home/Creating ALTIBASE Database__22643020.md`
- `arch/Home/Linux Setup Guide for Altibase__22643022.md`
- `arch/Home/Solaris Setup Guide for Altibase__14058290.md`
- `arch/Home/Solaris Setup Guide for Altibase/**`
- `arch/Home/HPUX Setup Guide for Altibase__14058288.md`
- `arch/Home/AIX Setup Guide for Altibase__14058298.md`
- `arch/Home/Altibase Docker Guide__14647741.md`
- `arch/Home/Altibase Docker Guide/**`
- `FAQE/Home/01. Installation, Patch, Upgrade/**`

Acceptance: installation, license, database creation, startup validation, OS setup, package/patch flow, Docker, and installation failure notes are covered with source paths and exact commands.

### L004 - Architecture storage concepts reference

Output: `llm-reference/02-architecture-storage-concepts.md`

Primary sources:

- `arch/Home/Home/**`
- `arch/Home/Disk Configuration Guide for Altibase__14647508.md`
- `arch/Home/Disk Configuration Guide for Altibase/**`
- `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md`
- `FAQE/Home/13. General/**`
- `FAQE/Home/ALTIBASE HDB Architecture/**` as `English-only source`

Acceptance: memory DBMS, disk DBMS, WAL, checkpoints, storage files, Direct I/O, disk contention, and architecture FAQ concepts are consolidated without losing source labels.

### L005 - Operation administration security reference

Output: `llm-reference/03-operation-administration-security.md`

Primary sources:

- `arch/Home/Altibase Configuration File Guide__22642991.md`
- `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`
- `arch/Home/Understanding the Altibase Start_Shut down Process/**`
- `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md`
- `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md`
- `arch/Home/UNIX Memory Management__16875572.md`
- `FAQE/Home/02. Operation and Management/**`
- `FAQE/Home/ALTIBASE HDB Administration/**` as `English-only source`

Acceptance: properties, startup/shutdown, users, passwords, access control, session/client settings, charset, JOBs, paths, datafile/log movement, capacity sizing, and OS utilities are covered.

### L006 - Backup recovery reference

Output: `llm-reference/04-backup-recovery.md`

Primary sources:

- `arch/Home/Considerations for Altibase Backup Policy__14647709.md`
- `arch/Home/Considerations for Altibase Backup Policy/**`
- `arch/Home/Responding to Failures Guide for Altibase__15138818.md`
- `arch/Home/Responding to Failures Guide for Altibase/**`
- `FAQE/Home/04. Backup and Recovery/**`

Acceptance: cold backup, online backup, logical backup, incremental backup, archive/noarchive modes, time based recovery, log anchor considerations, validation steps, and recovery risks are covered.

### L007 - Replication HA reference

Output: `llm-reference/05-replication-ha.md`

Primary sources:

- `arch/Home/Altibase Replication Configuration Guide__14647672.md`
- `arch/Home/Altibase Replication Constraints Guide__22643008.md`
- `FAQE/Home/03. Replication/**`
- `FAQE/Home/ALTIBASE HDB Replication/**` as `English-only source`

Acceptance: replication setup, restrictions, Sender/Receiver behavior, conflict handling, gap monitoring, GIVE-UP, DDL/DDL constraints, parallel applier notes, and HA cautions are covered.

### L008 - Monitoring diagnostics reference

Output: `llm-reference/06-monitoring-diagnostics.md`

Primary sources:

- `arch/Home/Altibase Monitoring Queries Guide__14058229.md`
- `arch/Home/Altibase Monitoring Queries Guide/**`
- `arch/Home/Altibase CPU Overload Analysis Guide__14647581.md`
- `arch/Home/Altibase CPU Overload Analysis Guide/**`
- `arch/Home/Altibase Memory Usage Increase Analysis Guide__14647388.md`
- `arch/Home/Altibase Memory Usage Increase Analysis Guide/**`
- `arch/Home/Responding to Failures Guide for Altibase__15138818.md`
- `arch/Home/Responding to Failures Guide for Altibase/**`
- `FAQE/Home/08. Monitoring/**`
- `FAQE/Home/ALTIBASE HDB Troubleshooting/**` as `English-only source`

Acceptance: monitoring query IDs, system views, session/lock/tablespace/replication checks, CPU and memory diagnostics, OS collection commands, and failure evidence collection are covered.

### L009 - Troubleshooting error messages reference

Output: `llm-reference/07-troubleshooting-error-messages.md`

Primary sources:

- `FAQE/Home/09. Error Messages/**`
- `FAQE/Home/Altibase Error Messages__6979655.md` as `English-only source`
- `FAQE/Home/Altibase Error Messages/**` as `English-only source`
- `arch/Home/Altibase Development Guide/4. CLIENT APPLICATION Error Messages__14058547.md`
- `arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md`
- relevant sections from `arch/Home/Responding to Failures Guide for Altibase/**`

Acceptance: error entries use symptom, cause, resolution, related SQL/commands, and source labels. Exact error codes and messages are preserved.

### L010 - SQL performance tuning reference

Output: `llm-reference/08-sql-performance-tuning.md`

Primary sources:

- `arch/Home/Altibase Development Guide__14058519.md`
- `arch/Home/Altibase Development Guide/**`
- `arch/Home/Altibase SQL Tuning Guide__22643010.md`
- `FAQE/Home/05. SQL/**`
- `FAQE/Home/06. Stored Procedure/**`
- `FAQE/Home/12. Others/**`
- `FAQE/Home/ALTIBASE HDB Performance Tuning/**` as `English-only source`

Acceptance: SQL tuning, optimizer, indexes, partitioning, HPT, stored procedures, DRDB index build settings, query examples, and version-specific limits are covered.

### L011 - Development client API reference

Output: `llm-reference/09-development-client-api.md`

Primary sources:

- `arch/Home/Altibase Developer Training__22642996.md`
- `arch/Home/Altibase Precompiler Guide__14647438.md`
- `arch/Home/Altibase Precompiler Guide/**`
- `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile__15630378.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/**`
- `arch/Home/JAVA Developer's Guide__16875544.md`
- `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md`
- `arch/Home/Altibase and unixODBC Integration Guide__14647413.md`
- `arch/Home/Altibase and unixODBC Integration Guide/**`
- `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md`
- `arch/Home/Altibase Window ADO.NET Development Guide/**`
- `arch/Home/PHP Integration Guide for Altibase__14647305.md`
- `arch/Home/PHP Integration Guide for Altibase/**`
- `FAQE/Home/07. Development and API/**`

Acceptance: APRE, precompiler, C/C++, JDBC, ODBC, ADO.NET, PHP, driver versions, connection strings, client errors, sample code cautions, and attachments are covered.

### L012 - Application framework integration reference

Output: `llm-reference/10-application-framework-integration.md`

Primary sources:

- `arch/Home/TOMCAT Integration Guide for Altibase__14058489.md`
- `arch/Home/TOMCAT Integration Guide for Altibase/**`
- `arch/Home/JEUS Integration Guide for Altibase__14058459.md`
- `arch/Home/JEUS Integration Guide for Altibase/**`
- `arch/Home/JBOSS Integration Guide for Altibase__14647358.md`
- `arch/Home/JBOSS Integration Guide for Altibase/**`
- `arch/Home/WEBLOGIC Integration Guide for Altibase__14058319.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/**`
- `arch/Home/WebSphere Integration Guide for Altibase__14058343.md`
- `arch/Home/Spring Integration Guide for Altibase__14058410.md`
- `arch/Home/Spring Integration Guide for Altibase/**`
- `arch/Home/iBatis Integration Guide for Altibase__14058303.md`
- `arch/Home/iBatis Integration Guide for Altibase/**`
- `arch/Home/MyBatis Integration Guide for Altibase__14058349.md`
- `arch/Home/MyBatis Integration Guide for Altibase/**`
- `arch/Home/Hibernate Integration Guide for Altibase__14058388.md`

Acceptance: WAS/framework setup, driver files, datasource settings, JDBC URL forms, version conditions, failover/load-balancing notes, and sample caveats are covered.

### L013 - Migration conversion tools reference

Output: `llm-reference/11-migration-conversion-tools.md`

Primary sources:

- `arch/Home/Altibase Data Migration Process Guide__22642994.md`
- `arch/Home/Altibase_Oracle Comparison__16875638.md`
- `arch/Home/ORACLE to ALTIBASE Conversion Guide__22643038.md`
- `arch/Home/Altibase Oracle Conversion Guide__14647316.md`
- `arch/Home/Altibase Oracle Conversion Guide/**`
- `arch/Home/MSSQL to ALTIBASE Conversion Guide__22643024.md`
- `arch/Home/Migration Center User Guide__19955861.md`
- `arch/Home/Altibase VC 2008 Development Guide__19333567.md`
- `arch/Home/Altibase VC 2010 Development Guide__19334121.md`
- `arch/Home/Altibase GeoServer Integration Guide__22643004.md`
- `arch/Home/SQuirrel SQL Client Quick Guide for Altibase__14647622.md`
- `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/**`

Acceptance: Altibase version migration, Oracle/MSSQL conversion, Migration Center, VC guides, GeoServer, SQuirrel, support/manual links, and legacy attachment limitations are covered.

### L014 - FAQ integration and dedupe pass

Goal: Review topic documents against Korean-source verified FAQ content and remove unnecessary duplication.

Scope:

- Update `llm-reference/01-*` through `llm-reference/11-*`.
- Prefer technical guides for canonical explanations and FAQ for operational exceptions, examples, and troubleshooting.
- Do not collapse different version, OS, license, restart, backup/recovery mode, output, or failure-condition variants.

Acceptance:

- Each topic document has FAQ-derived operational notes where useful.
- Repeated commands or SQL are canonicalized unless conditions differ.
- Cross references to the error and terminology documents are added where useful.

### L015 - Terminology and multilingual preservation guide

Output: `llm-reference/12-terminology-multilingual-preservation.md`

Primary sources:

- `LLM_REFERENCE_REVIEW_PLAN.md`
- all `llm-reference/*.md` topic documents created so far
- pass2 reports for source classifications and risks

Acceptance: glossary includes product names, commands, SQL/system objects, properties, paths, error codes, roles/internal terms, Java/.NET/C/C++ identifiers, version conditions, and attachment/URL rules.

### L016 - Cross-reference consistency pass

Goal: Make the package consistent and searchable.

Scope:

- Update all `llm-reference/*.md` documents as needed.
- Normalize heading style, source path sections, terminology sections, related links, source classifications, and attachment wording.
- Check that no `English-only source` is described as Korean-source verified.

Acceptance:

- `rg -n "English-only source|Legacy attachment label only|Diagram unavailable" llm-reference` shows classifications where needed.
- Empty links and stale export artifacts are absent from `llm-reference/`.

### L017 - Final validation and report

Output: `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`

Acceptance:

- Run final checks for manifest JSON, diff whitespace, source path existence, document counts, empty links, stale export artifacts, Korean residue classification, and attachment URL preservation.
- Record checked commands, results, remaining risks, and manual review recommendations.

### L018 - Final packaging review

Output: `llm-reference/HANDOFF.md`

Acceptance:

- Verify every expected `llm-reference/` output exists.
- Summarize package contents, how to use the files in GPTs/Codex, remaining risk labels, and validation status.
- Review the final diff and create a focused final handoff commit.

## Commit Expectations

Each job must create exactly one focused commit when practical. Use messages like:

- `docs: clean source readiness for LLM package`
- `docs: add LLM reference package scaffold`
- `docs: add installation LLM reference`
- `docs: validate LLM reference package`

If a job discovers that a previous job left unrelated changes, stop instead of sweeping those changes into the current commit.
