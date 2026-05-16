# Exhaustive LLM Reference Consolidation Workflow Requirements

## Purpose

Create a reviewed English reference package that GPTs, Codex, and other LLMs can use as the canonical Altibase knowledge base. This workflow is not a FAQ-only pass and not a high-level summary pass.

The final `llm-reference/` package must preserve enough information from every original English source document under `arch/Home` and `FAQE/Home` for an LLM to answer questions about the procedures, commands, SQL, settings, version conditions, cautions, errors, attachments, and operational edge cases found in those sources.

The package may reorganize and deduplicate content by topic, but it must not drop unique technical meaning. If a source item is not carried into a topic document, the coverage evidence must explicitly say why, for example duplicate canonical coverage, legacy attachment label only, diagram unavailable, English-only auxiliary risk, or recheck required.

## Output Directory

All final package files are created under `llm-reference/`. Do not delete, move, or rename original source documents under `DOCK/`, `faq/`, `arch/`, or `FAQE/`.

Expected top-level outputs:

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

Expected coverage outputs:

- `llm-reference/coverage/README.md`
- `llm-reference/coverage/interrupted-run-summary.md`
- `llm-reference/coverage/source-inventory.tsv`
- `llm-reference/coverage/source-to-topic-map.tsv`
- `llm-reference/coverage/semantic-unit-coverage.tsv`
- `llm-reference/coverage/attachment-diagram-register.tsv`
- `llm-reference/coverage/answerability-backtest.tsv`
- `llm-reference/coverage/omissions-and-risks.tsv`

## Completeness Policy

The final package must be answerable from the consolidated documents alone, with source paths retained for review. Use the original English source set stabilized in Phase 2 as the input corpus.

A "semantic unit" is any source item that may affect an Altibase answer:

- Procedure step, prerequisite, validation step, rollback step, warning, restriction, exception, or version/platform condition.
- SQL statement, system view, performance view, utility command, shell command, property, environment variable, file path, class name, driver name, JDBC URL, DSN, error code, or message text.
- Troubleshooting symptom, cause, resolution, diagnostic evidence, or operational decision point.
- Attachment label, downloadable URL, unavailable diagram notice, external reference, or legacy source limitation.

Every semantic unit must be represented in `llm-reference/coverage/semantic-unit-coverage.tsv` with one of these statuses:

- `covered`: the unit is represented in a topic document.
- `covered_by_canonical_duplicate`: the unit is duplicated in sources and the canonical topic section is named.
- `source_index_only`: the unit is only source metadata and does not contain answerable technical content.
- `legacy_attachment_label_only`: the source has only a legacy attachment label with no downloadable URL.
- `diagram_unavailable`: source evidence says diagram content is unavailable and must not be reconstructed.
- `not_document_format`: attachment is outside the document-format preservation gate.
- `english_only_auxiliary`: material is useful auxiliary English source and is labeled as such.
- `recheck_required`: coverage cannot be verified.

Final acceptance requires zero `recheck_required` rows. It also requires that every `arch/Home/**/*.md` and `FAQE/Home/**/*.md` source file appears in both `source-inventory.tsv` and `source-to-topic-map.tsv`.

## Coverage Evidence Formats

All TSV files must be tab-separated. Escape literal tabs or newlines in field values as `\t` and `\n`.

`llm-reference/coverage/source-inventory.tsv`:

```text
source_path	source_class	owner_job	title	heading_count	code_block_count	attachment_count	primary_topic	coverage_status	notes
```

Allowed `coverage_status` values: `pending`, `covered`, `covered_with_risk`, `source_index_only`, `recheck_required`.

`llm-reference/coverage/source-to-topic-map.tsv`:

```text
source_path	source_class	primary_topic	secondary_topics	owner_job	mapped_status	notes
```

Allowed `mapped_status` values: `mapped`, `mapped_with_risk`, `source_index_only`, `recheck_required`.

`llm-reference/coverage/semantic-unit-coverage.tsv`:

```text
source_path	source_heading	unit_id	unit_type	source_excerpt_or_identifier	coverage_status	target_doc	target_section	target_anchor	preservation_note	risk
```

Allowed `unit_type` values: `concept`, `procedure`, `command`, `sql`, `configuration`, `path`, `version_condition`, `warning`, `error`, `troubleshooting`, `attachment`, `external_reference`, `sample_code`, `source_metadata`.

`llm-reference/coverage/attachment-diagram-register.tsv`:

```text
source_path	label_or_url	kind	extension	source_class	target_doc	preservation_status	risk	notes
```

Allowed `preservation_status` values: `preserved_url`, `legacy_no_downloadable_url`, `not_document_format`, `diagram_unavailable`, `recheck_required`.

`llm-reference/coverage/answerability-backtest.tsv`:

```text
source_path	unit_id	question	expected_answer_basis	target_doc	target_section	result	risk	notes
```

Allowed `result` values: `answerable`, `answerable_with_source_label`, `not_answerable`, `recheck_required`.

`llm-reference/coverage/omissions-and-risks.tsv`:

```text
source_path	unit_id	issue_type	description	action	final_status	notes
```

Allowed `final_status` values: `resolved`, `accepted_source_limitation`, `accepted_english_only_auxiliary`, `recheck_required`.

## Source Classification

Use Phase 2 evidence from `source-stabilization/`:

- `Korean-source-verified`: `arch/Home` and Korean-core `FAQE/Home` material reviewed in Phase 1 and Phase 2.
- `Link-validated Korean-source-verified`: Korean-source-verified material whose attachments and links were checked.
- `English-only source`: `FAQE/Home/ALTIBASE HDB*`, `FAQE/Home/Altibase Error Messages/**`, and `FAQE/Home/Altibase Error Messages__6979655.md` unless later explicitly audited against Korean sources.
- `Legacy attachment label only`: source has a `#` attachment label with no downloadable URL.
- `Diagram unavailable`: Gliffy or other exported diagram content is unavailable and must not be reconstructed from guesswork.

## Standard Consolidated Document Shape

Use this structure unless the job-specific topic needs a small adjustment:

```markdown
# <Topic title>

## Source paths

## Source coverage notes

## Scope and audience

## Key facts

## Procedures

## SQL, commands, and configuration

## Validation and troubleshooting

## Version-specific notes

## Related errors

## Attachments and external references

## Terminology
```

Topic documents must include exact identifiers and enough procedural detail for answer generation. Do not replace a procedure with a vague summary when the source contains concrete steps.

## Job Details

### R001 - Interrupted run summary and phase gates

Output: `llm-reference/coverage/interrupted-run-summary.md`

Goal: Preserve what happened before this workflow was restructured and confirm Phase 2 readiness remains valid.

Acceptance:

- Summarize the interrupted L001 state: `PASS2_KO_EN_DOC_REVIEW_REPORT.md` was updated with a source-readiness note, `llm-reference/` topic files were not created, and the old L001 status was not a complete Phase 3 package.
- Confirm `source-stabilization/validation-report.md` has decision `READY_FOR_LLM_CONSOLIDATION`.
- Confirm `llm-reference/` contains only outputs created by the restarted exhaustive workflow.
- Standard verification passes.

### R002 - Package scaffold and exhaustive coverage ledgers

Outputs:

- `llm-reference/README.md`
- `llm-reference/source-index.md`
- `llm-reference/00-source-classification.md`
- `llm-reference/coverage/README.md`
- coverage TSV files initialized with headers

Acceptance:

- The package states that it is exhaustive reference material, not a FAQ-only or summary-only package.
- Coverage TSV headers exactly match this requirements file.
- Every active job and expected output is listed.

### R003 - Full source inventory and source-to-topic map

Goal: Inventory every Markdown source under `arch/Home` and `FAQE/Home` and map every source path to a primary topic document and owner job.

Acceptance:

- `source-inventory.tsv` has exactly one row for every `arch/Home/**/*.md` and `FAQE/Home/**/*.md` source file.
- `source-to-topic-map.tsv` has exactly one row for every same source file.
- Inventory records heading count, code block count, attachment count, source class, owner job, and primary topic.
- No source path is unmapped.

### R004 - Installation, patch, upgrade, and database creation

Output: `llm-reference/01-installation-upgrade-platform.md`

Primary sources:

- `arch/Home/Altibase Installation Guide__14647632.md`
- `arch/Home/Altibase Installation Guide/**`
- `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md`
- `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md`
- `arch/Home/Creating ALTIBASE Database__22643020.md`
- `FAQE/Home/01. Installation, Patch, Upgrade/**`

Acceptance:

- Installation prerequisites, package layout, license handling, installation steps, patch/upgrade flow, database creation, startup validation, and installation failure handling are covered.
- All commands, paths, properties, version conditions, and FAQ variants from the primary sources have semantic-unit rows.

### R005 - Platform setup, OS prerequisites, and Docker

Output: `llm-reference/01-installation-upgrade-platform.md`

Primary sources:

- `arch/Home/Linux Setup Guide for Altibase__22643022.md`
- `arch/Home/Solaris Setup Guide for Altibase__14058290.md`
- `arch/Home/Solaris Setup Guide for Altibase/**`
- `arch/Home/HPUX Setup Guide for Altibase__14058288.md`
- `arch/Home/AIX Setup Guide for Altibase__14058298.md`
- `arch/Home/Altibase Docker Guide__14647741.md`
- `arch/Home/Altibase Docker Guide/**`

Acceptance:

- OS settings, kernel/resource settings, user/environment setup, filesystem notes, platform-specific cautions, and Docker commands are covered without merging incompatible platform variants.
- Semantic-unit coverage rows are added for every concrete setting, command, path, and warning.

### R006 - Architecture, storage, and disk concepts

Output: `llm-reference/02-architecture-storage-concepts.md`

Primary sources:

- `arch/Home/Home/**`
- `arch/Home/Disk Configuration Guide for Altibase__14647508.md`
- `arch/Home/Disk Configuration Guide for Altibase/**`
- `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md`
- `FAQE/Home/13. General/**`

Acceptance:

- Memory DBMS, disk DBMS, WAL, checkpoints, storage files, Direct I/O, disk contention, volume configuration, and architecture FAQ concepts are covered.
- Diagram-unavailable cases are recorded without reconstructing missing diagrams.

### R007 - Configuration, startup, shutdown, capacity, and OS utilities

Output: `llm-reference/03-operation-administration-security.md`

Primary sources:

- `arch/Home/Altibase Configuration File Guide__22642991.md`
- `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`
- `arch/Home/Understanding the Altibase Start_Shut down Process/**`
- `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md`
- `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md`
- `arch/Home/UNIX Memory Management__16875572.md`

Acceptance:

- Properties, startup/shutdown process, capacity calculations, OS utilities, memory management, paths, and operational commands are covered with exact identifiers.

### R008 - Administration, security, sessions, charset, and operational FAQ

Output: `llm-reference/03-operation-administration-security.md`

Primary sources:

- `FAQE/Home/02. Operation and Management/**`
- Korean-source-verified operational rows from `source-stabilization/source-classification.tsv`

Acceptance:

- User/password/access control, sessions, clients, character set, JOBs, data/log movement, operational procedures, and every operation FAQ variant are represented.
- Korean sample data remains exact where it is part of charset examples.

### R009 - Backup, recovery, and failure response

Output: `llm-reference/04-backup-recovery.md`

Primary sources:

- `arch/Home/Considerations for Altibase Backup Policy__14647709.md`
- `arch/Home/Considerations for Altibase Backup Policy/**`
- `arch/Home/Responding to Failures Guide for Altibase__15138818.md`
- `arch/Home/Responding to Failures Guide for Altibase/**`
- `FAQE/Home/04. Backup and Recovery/**`

Acceptance:

- Cold backup, online backup, logical backup, incremental backup, archive/noarchive mode, time-based recovery, log anchor risks, failure response, aexport/iloader backup usage, and validation steps are covered.

### R010 - Replication and HA

Output: `llm-reference/05-replication-ha.md`

Primary sources:

- `arch/Home/Altibase Replication Configuration Guide__14647672.md`
- `arch/Home/Altibase Replication Constraints Guide__22643008.md`
- `FAQE/Home/03. Replication/**`

Acceptance:

- Replication setup, Sender/Receiver behavior, constraints, conflict handling, gap monitoring, GIVE-UP, DDL constraints, parallel applier, HA cautions, and every replication FAQ variant are covered.

### R011 - Monitoring queries and diagnostics

Output: `llm-reference/06-monitoring-diagnostics.md`

Primary sources:

- `arch/Home/Altibase Monitoring Queries Guide__14058229.md`
- `arch/Home/Altibase Monitoring Queries Guide/**`
- `FAQE/Home/08. Monitoring/**`

Acceptance:

- Monitoring query IDs, system views, performance views, session/lock/tablespace/replication checks, and every monitoring FAQ variant are covered with exact SQL.

### R012 - CPU, memory, OS evidence, and failure diagnostics

Output: `llm-reference/06-monitoring-diagnostics.md`

Primary sources:

- `arch/Home/Altibase CPU Overload Analysis Guide__14647581.md`
- `arch/Home/Altibase CPU Overload Analysis Guide/**`
- `arch/Home/Altibase Memory Usage Increase Analysis Guide__14647388.md`
- `arch/Home/Altibase Memory Usage Increase Analysis Guide/**`
- relevant diagnostic sections from `arch/Home/Responding to Failures Guide for Altibase/**`

Acceptance:

- CPU overload analysis, memory growth analysis, OS evidence collection, logs, dumps, and diagnostic decision points are covered.

### R013 - Troubleshooting and Korean-source error messages

Output: `llm-reference/07-troubleshooting-error-messages.md`

Primary sources:

- `FAQE/Home/09. Error Messages/**`
- `arch/Home/Altibase Development Guide/4. CLIENT APPLICATION Error Messages__14058547.md`
- `arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md`
- relevant troubleshooting sections from Korean-source-verified technical guides

Acceptance:

- Error entries use symptom, cause, resolution, related SQL/commands, exact error codes/messages, and source labels.

### R014 - English-only error catalog and troubleshooting auxiliary sources

Output: `llm-reference/07-troubleshooting-error-messages.md`

Primary sources:

- `FAQE/Home/Altibase Error Messages__6979655.md` as `English-only source`
- `FAQE/Home/Altibase Error Messages/**` as `English-only source`
- `FAQE/Home/ALTIBASE HDB Troubleshooting/**` as `English-only source`

Acceptance:

- English-only error and troubleshooting entries are integrated or indexed with explicit `English-only source` labels.
- No English-only entry is described as Korean-source-verified.

### R015 - SQL, stored procedures, and query behavior

Output: `llm-reference/08-sql-performance-tuning.md`

Primary sources:

- SQL and stored procedure portions of `arch/Home/Altibase Development Guide__14058519.md`
- `arch/Home/Altibase Development Guide/**`
- `FAQE/Home/05. SQL/**`
- `FAQE/Home/06. Stored Procedure/**`
- `FAQE/Home/12. Others/**`

Acceptance:

- SQL syntax, stored procedure behavior, examples, limits, FAQ variants, and version-specific behavior are covered with exact SQL and object names.

### R016 - Performance tuning, optimizer, indexes, and partitioning

Output: `llm-reference/08-sql-performance-tuning.md`

Primary sources:

- `arch/Home/Altibase SQL Tuning Guide__22643010.md`
- performance portions of `arch/Home/Altibase Development Guide/**`
- `FAQE/Home/ALTIBASE HDB Performance Tuning/**` as `English-only source`

Acceptance:

- Optimizer, indexes, partitioning, HPT, DRDB index build settings, tuning SQL, diagnostic SQL, and exact caveats are covered.

### R017 - APRE, precompiler, and C/C++ development

Output: `llm-reference/09-development-client-api.md`

Primary sources:

- `arch/Home/Altibase Developer Training__22642996.md`
- `arch/Home/Altibase Precompiler Guide__14647438.md`
- `arch/Home/Altibase Precompiler Guide/**`
- `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile__15630378.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/**`

Acceptance:

- APRE, SES, precompiler, C/C++ build options, Makefiles, client errors, sample code cautions, and attachments are covered.

### R018 - Java, JDBC, ODBC, ADO.NET, PHP, and client API FAQ

Output: `llm-reference/09-development-client-api.md`

Primary sources:

- `arch/Home/JAVA Developer's Guide__16875544.md`
- `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md`
- `arch/Home/Altibase and unixODBC Integration Guide__14647413.md`
- `arch/Home/Altibase and unixODBC Integration Guide/**`
- `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md`
- `arch/Home/Altibase Window ADO.NET Development Guide/**`
- `arch/Home/PHP Integration Guide for Altibase__14647305.md`
- `arch/Home/PHP Integration Guide for Altibase/**`
- `FAQE/Home/07. Development and API/**`

Acceptance:

- JDBC, ODBC, unixODBC, ADO.NET, PHP, connection strings, driver versions, examples, and every development/API FAQ variant are covered.

### R019 - WAS and framework integration

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

Acceptance:

- WAS/framework setup, driver files, datasource settings, JDBC URL forms, version conditions, failover/load-balancing notes, and sample caveats are covered for every framework source.

### R020 - Migration, conversion, and tools

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
- `FAQE/Home/11. Utilities/**`

Acceptance:

- Altibase version migration, Oracle/MSSQL conversion, Migration Center, VC guides, GeoServer, SQuirrel, iLoader/utilities, support/manual links, and legacy attachment limitations are covered.

### R021 - English-only auxiliary corpus integration

Outputs: relevant topic documents plus coverage rows

Primary sources:

- `FAQE/Home/ALTIBASE HDB Architecture/**`
- `FAQE/Home/ALTIBASE HDB Administration/**`
- `FAQE/Home/ALTIBASE HDB Performance Tuning/**`
- `FAQE/Home/ALTIBASE HDB Replication/**`
- `FAQE/Home/ALTIBASE HDB Troubleshooting/**`

Acceptance:

- All English-only auxiliary sources are either integrated into topic documents or indexed as auxiliary references.
- Every row uses `English-only source` or `english_only_auxiliary` classification.

### R022 - FAQ exhaustive reconciliation

Outputs: all relevant topic documents and coverage TSVs

Goal: Reconcile every Korean-source-verified FAQE file against the topic documents. This is not a "where useful" pass; every FAQ must be answerable or explicitly classified.

Acceptance:

- Every Korean-source-verified FAQE source has semantic-unit coverage rows.
- No FAQ is dropped because it appears repetitive unless a canonical duplicate target is named.
- Version, OS, license, restart, backup/recovery mode, output, and failure-condition variants are preserved.

### R023 - Attachments, diagrams, and external references register

Output: `llm-reference/coverage/attachment-diagram-register.tsv`

Primary sources:

- `source-stabilization/legacy-attachments.tsv`
- `source-stabilization/url-backed-attachments.tsv`
- all attachment references in `arch/Home` and `FAQE/Home`

Acceptance:

- Every document-format URL-backed attachment remains preserved.
- Every legacy label is marked `legacy_no_downloadable_url`.
- Every unavailable diagram is marked `diagram_unavailable`.
- No synthetic URL or guessed diagram content is introduced.

### R024 - Terminology and multilingual preservation guide

Output: `llm-reference/12-terminology-multilingual-preservation.md`

Primary sources:

- all topic documents created so far
- source classification and risk reports

Acceptance:

- Glossary includes product names, commands, SQL/system objects, properties, paths, error codes, roles/internal terms, Java/.NET/C/C++ identifiers, version conditions, and attachment/URL rules.
- The guide states which identifiers must remain untranslated in multilingual answers.

### R025 - Source and semantic-unit coverage reconciliation

Outputs: updated coverage TSVs and topic fixes

Acceptance:

- Source inventory count equals `find arch/Home FAQE/Home -type f -name '*.md' | wc -l`.
- Every source in inventory has `mapped` or accepted source-limitation status.
- Every semantic-unit row has a non-empty target or accepted limitation.
- There are zero `recheck_required` rows unless final decision is `RECHECK_REQUIRED`.

### R026 - Source-derived answerability backtest

Output: `llm-reference/coverage/answerability-backtest.tsv`

Acceptance:

- Generate representative source-derived questions from headings, procedures, commands, SQL, errors, and attachments.
- At least one backtest row exists for every source file with answerable technical content, and high-density sources have multiple rows.
- Every backtest row is `answerable` or `answerable_with_source_label`; otherwise fix the topic document or record `recheck_required`.

### R027 - Cross-reference consistency and unsupported-claim review

Outputs: updated `llm-reference/*.md`

Acceptance:

- Source path sections, terminology sections, source labels, attachment wording, and related links are consistent.
- Empty Markdown links, stale export artifacts, and unsupported claims are absent.
- `English-only source` material is never described as Korean-source-verified.

### R028 - Final validation, build report, and handoff

Outputs:

- `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
- `llm-reference/HANDOFF.md`

Acceptance:

- Verify every expected output exists.
- Verify all source paths in coverage files exist or are documented source limitations.
- Verify final document counts, manifest JSON, diff whitespace, artifact scans, coverage counts, attachment preservation, and answerability backtest results.
- Final decision is exactly one of `COMPLETE_REFERENCE_PACKAGE` or `RECHECK_REQUIRED`.
- Create a concise handoff explaining how to use the files in GPTs/Codex and what risk labels remain.

## Standard Verification

Run the checks that match the job scope and record results in the job's final message before committing:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
rg -n "\[\]\(|Error rendering macro|Unknown macro|unknown-macro|\]\(#\)" llm-reference arch/Home FAQE/Home
```

For expected-no-match scans, `rg` exit code 1 is a passing no-match result. Exit code 2 or higher is a command error. If a scan intentionally finds legacy source labels, explain each hit and use a narrower follow-up scan for live defects.

## Commit Expectations

Each successful job must create one focused commit when practical. If a job cannot safely create a commit because it only verifies existing committed material, it must create or update a small evidence file under `llm-reference/coverage/` so the job result is reviewable and committable.

If a job discovers that a previous job left unrelated changes, stop instead of sweeping those changes into the current commit.
