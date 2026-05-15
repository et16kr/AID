# Workflow Requirements: Korean-to-English Sentence-Level Documentation Audit Pass 2

## Purpose

This workflow performs a second-pass Korean-to-English documentation audit after J013. The first pass found and applied many Korean-source updates to English documents. This pass is intentionally stricter: it asks each job to audit its scoped Korean source material against the corresponding English material at sentence, bullet, table-row, command, SQL, configuration, warning, version, attachment, and link level.

The goal is not to create final consolidated LLM documents yet. The goal is to make the English source set safer before GPTs, Codex, and other LLM reference packaging begins.

## Authority And Boundaries

- Korean `DOCK/Home` and `faq/Home` documents are authoritative.
- English `arch/Home` and Korean-core `FAQE/Home` documents are update targets.
- Do not edit, delete, move, or rename Korean source documents under `DOCK/` or `faq/`.
- Do not modify the existing first-pass workflow under `.codex-jobs/ko-en-doc-coverage/`.
- Preserve existing user changes. Stop if uncommitted project files outside this workflow block safe execution.
- Keep original English documents in place. Do not perform final LLM consolidation in this pass.
- If English-only `FAQE` material is reviewed, label it as English-only and do not describe it as Korean-source verified.

## Required Inputs

Every job must read these files before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-doc-coverage/jobs.tsv`
- `.codex-jobs/ko-en-doc-coverage-pass2/workflow-requirements.md`

Jobs should also inspect the corresponding first-pass job note under `.codex-jobs/ko-en-doc-coverage/` when the scope maps to J002-J013.

## Sentence-Level Audit Method

For each scoped Korean source document:

1. Identify the corresponding English target path from `KO_EN_DOC_REVIEW_REPORT.md`, first-pass job notes, `manifest.json`, and nearby file names.
2. Compare the Korean source to the English target at sentence, bullet, table-row, command, SQL, configuration, warning, note, attachment, and link level.
3. Treat Korean as authoritative when meaning differs.
4. Update English with natural technical English when Korean content is missing, newer, clearer, or semantically different.
5. Preserve non-translatable identifiers exactly, including product names, commands, SQL, system views, properties, file paths, environment variables, error codes, versions, URLs, and attachment filenames.
6. Do not remove valid English-only clarification unless it conflicts with Korean-source meaning. If retained English-only content matters for LLM packaging, record it as English-only.
7. Record both changes and no-change findings in a pass2 audit note.

If the Korean and English documents are structured differently, compare by semantic unit instead of line number. A semantic unit may be a sentence, bullet, table row, code block, warning paragraph, procedure step, or attachment reference.

## Required Output Per Job

Each job must create or update:

- A job note under `.codex-jobs/ko-en-doc-coverage-pass2/`, named with the job id and a short slug.
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`, with a section for the job.

If no English documentation change is needed, still update the job note and pass2 report with the checked document list, evidence, and no-change conclusion. This ensures each successful job has a focused commit.

If English `arch` or `FAQE` documents are edited, update `manifest.json` metadata for the changed Markdown pages using the repository's existing manifest format.

## Required Verification

Use checks appropriate to the job scope. At minimum, every job must run:

```bash
python3 -m json.tool manifest.json
git diff --check
```

Baseline and final validation jobs must also run:

```bash
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
rg -n "\\[\\]\\(|Error rendering macro|Unknown macro" arch/Home FAQE/Home
```

Attachment/link jobs must revalidate URL-backed document-format links for these extensions:

```text
.pdf .ppt .pptx .doc .docx .xls .xlsx .zip
```

## Commit Requirement

Every successful job must:

- Review the final diff.
- Leave project files clean after the commit.
- Create a focused commit.

Suggested commit format:

```text
docs: complete P20x pass2 <short scope>
```

## Job Scope Matrix

### P201 Baseline after J013

Confirm J013 is complete and record the second-pass starting point. Do not edit product documentation.

When this workflow is first generated, `.codex-jobs/ko-en-doc-coverage-pass2/` may be untracked. P201 may include the pass2 workflow scaffold in its focused commit together with the P201 baseline note and `PASS2_KO_EN_DOC_REVIEW_REPORT.md`. Do not treat the newly generated pass2 workflow scaffold as previous-job product documentation output.

Required evidence:

- `git status --short --branch --untracked-files=all`
- `git log --oneline -15`
- first-pass `.codex-jobs/ko-en-doc-coverage/jobs.tsv` shows J001-J013 as `Done`
- document counts for `DOCK/Home`, `faq/Home`, `arch/Home`, `FAQE/Home`
- `python3 -m json.tool manifest.json`
- `git diff --check`

### P202 Tech audit: installation core and database creation

Sentence-level audit:

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md`
- `DOCK/Home/25. Altibase 데이터베이스 생성 가이드__13436812.md`
- `DOCK/Home/31. Altibase 설치가이드__11698403.md`
- `DOCK/Home/41. Altibase Quick Install & Start for UNIX__13436834.md`
- `DOCK/Home/42. Altibase 설치 시 발생할 수 있는 문제상황과 조치__13437056.md`

Use the first-pass J002 mapping for English targets.

### P203 Tech audit: OS platform and disk I/O setup

Sentence-level audit:

- `DOCK/Home/21. Altibase 디스크I_O 병목을 고려한 볼륨구성 가이드__11698408.md`
- `DOCK/Home/22. Altibase 운영을 위한 Solaris 설정 가이드__11698415.md`
- `DOCK/Home/23. Altibase 운영을 위한 HPUX 설정 가이드__14057733.md`
- `DOCK/Home/24. Altibase 운영을 위한 AIX 설정 가이드__13436846.md`
- `DOCK/Home/57. Altibase 운영을 위한 Linux 설정 가이드__13436485.md`

Use the first-pass J002 mapping for English targets.

### P204 Tech audit: operations failure startup resource utilities

Sentence-level audit:

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md`
- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md`
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md`
- `DOCK/Home/45. Altibase 운영을 위한 시스템 리소스 용량산정 가이드__14057887.md`
- `DOCK/Home/47. 문제분석을 위한 OS별 유틸리티 사용 가이드__13436866.md`
- `DOCK/Home/48. UNIX Memory Management__13436842.md`

Use the first-pass J003 mapping for English targets.

### P205 Tech audit: monitoring queries

Sentence-level audit:

- `DOCK/Home/59. Altibase 모니터링 쿼리 가이드__10060431.md`

This guide has many split English target files under `arch/Home/Altibase Monitoring Queries Guide/**`. Verify section IDs, SQL, meta tables, performance views, output examples, and warning text.

### P206 Tech audit: CPU and memory analysis

Sentence-level audit:

- `DOCK/Home/62. Altibase CPU 과부하 현상에 대한 분석가이드__11698396.md`
- `DOCK/Home/63. Altibase Memory 사용량 증가 분석가이드__11698518.md`

Use the first-pass J003 mapping for English targets.

### P207 Tech audit: replication configuration and constraints

Sentence-level audit:

- `DOCK/Home/27. Altibase 이중화 구성 가이드__13828098.md`
- `DOCK/Home/49. Altibase 이중화 제약사항 가이드__19333729.md`

Use the first-pass J004 mapping for English targets.

### P208 Tech audit: backup recovery and failure recovery

Sentence-level audit:

- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md`
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md`
- `DOCK/Home/50. Altibase 백업정책 결정을 위한 고려사항__14057586.md`

Focus on backup, recovery, failure response, startup recovery, archive log, online/offline/logical/incremental backup, and related warnings.

### P209 Tech audit: C C++ precompiler APRE developer basics

Sentence-level audit:

- `DOCK/Home/33. Altibase 개발자교육__19333461.md`
- `DOCK/Home/34. Altibase Precompiler 가이드__11698385.md`
- `DOCK/Home/35. Altibase APRE(SES) _C_C++ Makefile__11698493.md`
- `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md`

Use the first-pass J005 mapping for English targets.

### P210 Tech audit: Java ODBC ADO.NET PHP client APIs

Sentence-level audit:

- `DOCK/Home/32. Altibase와 unixODBC 연동 가이드__11698379.md`
- `DOCK/Home/51. Altibase window ADO.NET 개발 가이드__11698513.md`
- `DOCK/Home/53. Windows 환경의 Altibase ODBC 개발 가이드__13436856.md`
- `DOCK/Home/56. JAVA 개발 가이드__14057500.md`
- `DOCK/Home/66. Altibase PHP 연동가이드__7341461.md`

Use the first-pass J005 mapping for English targets.

### P211 Tech audit: WAS and framework integrations

Sentence-level audit:

- `DOCK/Home/28. Altibase TOMCAT 연동가이드__7341030.md`
- `DOCK/Home/29. Altibase JEUS 연동가이드__7341028.md`
- `DOCK/Home/30. Altibase JBoss 연동가이드__13437492.md`
- `DOCK/Home/52. Altibase WebSphere 연동 가이드__13435602.md`
- `DOCK/Home/54. Altibase Spring 연동 가이드__7340945.md`
- `DOCK/Home/55. Altibase iBATIS 연동가이드__7340053.md`
- `DOCK/Home/58. Altibase Hibernate 연동가이드__14057878.md`
- `DOCK/Home/60. Altibase WebLogic 연동가이드__7340101.md`
- `DOCK/Home/64. Altibase MyBatis 연동 가이드__7340818.md`

Use the first-pass J005 mapping for English targets.

### P212 Tech audit: SQL tuning development and Oracle comparison

Sentence-level audit:

- `DOCK/Home/36. Altibase 개발가이드__7341274.md`
- `DOCK/Home/37. Altibase SQL 튜닝 가이드__19333563.md`
- `DOCK/Home/39. Altibase, Oracle 비교 자료__14058137.md`

Use the first-pass J006 mapping for English targets.

### P213 Tech audit: migration conversion and VC guides

Sentence-level audit:

- `DOCK/Home/38. Altibase VC 2008 개발가이드__19333567.md`
- `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md`
- `DOCK/Home/46. Altibase 버전 간 마이그레이션 가이드__19333688.md`
- `DOCK/Home/61. Altibase VC 2010 개발가이드__19334121.md`
- `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md`
- `DOCK/Home/70. Migration Center 사용자 가이드__19955861.md`

Use the first-pass J006 mapping for English targets.

### P214 Tech audit: Docker GeoServer and SQuirrel tools

Sentence-level audit:

- `DOCK/Home/67. Altibase 도커 가이드__14057660.md`
- `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md`
- `DOCK/Home/69. Altibase를 위한 SQuirrel SQL Client Quick 가이드__12255259.md`

Use the first-pass J006 mapping for English targets.

### P215 FAQ audit: installation and operation core

Sentence-level audit:

- `faq/Home/01. 설치, 패치, 업그레이드/**`
- `faq/Home/02. 운영 및 관리/**` documents related to client installation, IPC, security checklist, user/password, database name, OS/DB time, `MAX_CLIENT`, `TRANSACTION_TABLE_SIZE`, and core connection/session settings.

Targets are corresponding English core documents under:

- `FAQE/Home/01. Installation, Patch, Upgrade/**`
- `FAQE/Home/02. Operation and Management/**`

### P216 FAQ audit: operation storage logs jobs and resources

Sentence-level audit remaining `faq/Home/02. 운영 및 관리/**` documents related to automatic startup, log anchor, online logs, archive logs, double write files, tablespace data files, column changes, job objects, `MEM_MAX_DB_SIZE`, resource properties, and operational file/path changes.

Target corresponding English core documents under `FAQE/Home/02. Operation and Management/**`.

### P217 FAQ audit: replication

Sentence-level audit:

- `faq/Home/03. 이중화/**`

Target corresponding English core documents under `FAQE/Home/03. Replication/**`.

### P218 FAQ audit: backup SQL and stored procedures

Sentence-level audit:

- `faq/Home/04. 백업 및 복구/**`
- `faq/Home/05. SQL/**`
- `faq/Home/06. Stored Procedures/**`

Targets are corresponding English core documents under:

- `FAQE/Home/04. Backup and Recovery/**`
- `FAQE/Home/05. SQL/**`
- `FAQE/Home/06. Stored Procedure/**`

### P219 FAQ audit: development API

Sentence-level audit:

- `faq/Home/07. 개발 및 API/**`

Target corresponding English core documents under `FAQE/Home/07. Development and API/**`.

### P220 FAQ audit: monitoring

Sentence-level audit:

- `faq/Home/08. 모니터링/**`

Target corresponding English core documents under `FAQE/Home/08. Monitoring/**`.

### P221 FAQ audit: error messages

Sentence-level audit:

- `faq/Home/09. 에러메시지/**`

Target corresponding English core documents under `FAQE/Home/09. Error Messages/**`.

### P222 FAQ audit: utilities others general

Sentence-level audit:

- `faq/Home/11. 유틸리티/**`
- `faq/Home/12. 기타/**`
- `faq/Home/13. 일반/**`

Targets are corresponding English core documents under:

- `FAQE/Home/11. Utilities/**`
- `FAQE/Home/12. Others/**`
- `FAQE/Home/13. General/**`

### P223 Technical attachment source and export revalidation

Revalidate document-format attachments and known export artifacts across Korean-source-verified `arch` documents. Preserve URL-backed attachments in English targets. Record legacy `#` attachment labels separately because there is no downloadable URL to preserve.

### P224 FAQ attachment source English-only and export revalidation

Revalidate document-format attachments, known export artifacts, and English-only `FAQE` classification candidates across FAQ targets. Preserve URL-backed attachments in English targets and record English-only candidates separately.

### P225 LLM readiness and multilingual terminology review

Review `LLM_REFERENCE_REVIEW_PLAN.md` and the J013 handoff section. Confirm that the proposed LLM package structure can use the pass2-reviewed English source set. Do not create final consolidated LLM reference documents in this workflow.

### P226 Final pass2 validation and report

Run final validation across the pass2 result, update `PASS2_KO_EN_DOC_REVIEW_REPORT.md`, and state whether the repository is ready for LLM reference document consolidation.
