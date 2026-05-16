# KO to EN Semantic Coverage Audit Workflow Requirements

## Purpose

This workflow performs the strictest pre-consolidation audit: verify whether English source documents fully represent the Korean source documents at semantic-unit level. If Korean content is missing from English, update the English source document first. The final report must decide exactly one outcome:

- `COMPLETE`: English source documents are ready for the source-stabilization phase and later LLM consolidation.
- `RECHECK_REQUIRED`: at least one item still needs another human/Codex review before source stabilization or LLM consolidation.

This workflow is intentionally stricter than the previous J/P workflows. The previous workflows performed broad and pass2 sentence-level audits, but they did not leave a complete semantic-unit coverage matrix for every content unit. This workflow creates that matrix.

## Relationship To Existing Work

Previous work is valuable but not a substitute for this audit.

- Use `KO_EN_DOC_REVIEW_REPORT.md` and `PASS2_KO_EN_DOC_REVIEW_REPORT.md` for mappings, known findings, previous fixes, and risk context.
- Use `LLM_REFERENCE_REVIEW_PLAN.md` for source classification and later handoff rules.
- Do not treat previous report statements as proof that a specific Korean semantic unit is covered. Each current job must inspect its scoped Korean and English files directly.
- Do not run `.codex-jobs/llm-reference-consolidation/` in this workflow.

## Authority And Boundaries

- Korean documents under `DOCK/Home` and `faq/Home` are authoritative.
- English documents under `arch/Home` and Korean-core `FAQE/Home` are update targets.
- Korean source documents are never deleted, moved, or rewritten.
- Original English source documents are not deleted or moved.
- English-only `FAQE` material may help context, but it cannot prove Korean-source coverage unless the Korean unit is also represented in a Korean-core English target.
- Preserve user changes and stop if uncommitted project files outside workflow runtime areas block safe execution.

## Semantic Unit Definition

Audit by semantic unit rather than visual line number. A semantic unit is the smallest independently meaningful content item:

- heading or subheading
- paragraph
- bullet or numbered list item
- table row
- procedure step
- command block
- SQL block
- configuration item or property description
- warning, caution, note, limitation, exception, or version condition
- error code, cause, and action item
- attachment, source URL, or external reference

If a table row has multiple independent facts, split it into multiple units when needed. If a command block contains multiple commands with different meanings, split those commands when needed.

## Duplicate Source Ownership

Some Korean sources appear in more than one topical area. To prevent duplicate or conflicting matrix rows:

- The first listed job for a Korean source is the primary owner and must cover the whole source document.
- Later jobs that mention the same Korean source must add only topic-specific cross-reference rows, with `notes` naming the primary owner job.
- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` primary owner: S003. S005 may add operation-specific cross-reference rows only.
- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` primary owner: S005. S009 may add backup/recovery-specific cross-reference rows only.
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` primary owner: S005. S009 may add recovery-specific cross-reference rows only.

## Required Evidence

Each scoped audit job must produce:

- `semantic-coverage/matrices/<job-id>-<slug>.tsv`
- `semantic-coverage/notes/<job-id>-<slug>.md`

The matrix header must be exactly:

```text
job_id	ko_path	ko_start_line	ko_end_line	ko_unit_id	unit_type	ko_excerpt	required_identifiers	en_target_paths	en_start_line	coverage_status	action	evidence_excerpt	risk	notes
```

## Worktree Handoff Check

The orchestrator updates workflow state while a job is running. Audit jobs must not treat those runtime/status files as project handoff changes.

Use this command from the repository root when checking for blocking uncommitted files:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Stop only if that command prints output. Changes under `.codex-jobs/ko-en-semantic-coverage-audit/`, including `jobs.tsv`, logs, rollbacks, and `.runtime`, are expected workflow runtime state.

Allowed `coverage_status` values:

- `covered`
- `added`
- `not_applicable`
- `source_limitation`
- `missing`
- `unverified`
- `recheck_required`

Successful audit jobs must not leave `missing` or `unverified` rows. If a unit cannot be safely resolved, record `recheck_required` with a concrete reason.

TSV escaping rules:

- Matrix rows must be one physical line per semantic unit.
- Replace tabs inside field values with `\t`.
- Replace newlines inside field values with `\n`.
- Keep code and SQL excerpts short in the matrix; put longer excerpts in the per-job Markdown note and reference that note in `notes`.
- Do not use Markdown tables for matrices because command, SQL, and path values often contain pipe characters.

## Final Decision Rule

`COMPLETE` is allowed only when all of these are true:

- Every Korean source file in `DOCK/Home` and `faq/Home` has corresponding matrix coverage.
- Every matrix row is one of `covered`, `added`, `not_applicable`, or `source_limitation`.
- There are zero `missing`, `unverified`, and `recheck_required` rows.
- All English source fixes have been applied to `arch/` or `FAQE/`.
- `manifest.json` metadata is updated for edited Markdown pages.
- URL-backed document attachments from Korean sources are preserved in the relevant English targets.
- Final validation checks pass.
- S029 independent challenge review finds no false positive coverage evidence.

If any condition fails, S030 must report `RECHECK_REQUIRED`, not `COMPLETE`.

## Standard Checks

Every job runs at least:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
```

Baseline, closure, and final jobs also run:

```bash
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

Stabilization and final jobs also run:

```bash
rg -n "\[\]\(|Error rendering macro|Unknown macro|unknown-macro|\]\(#\)" arch/Home FAQE/Home semantic-coverage
rg -n $'\t(missing|unverified|recheck_required)\t' semantic-coverage/matrices
```

For expected-no-match checks, exit code 1 from `rg` is a passing result because no defect rows were found. Exit code 2 or higher is a command error.

Attachment jobs must check URL-backed document-format links for:

```text
.pdf .ppt .pptx .doc .docx .xls .xlsx .zip
```

## Outputs

- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- `semantic-coverage/matrices/*.tsv`
- `semantic-coverage/notes/*.md`
- `KO_EN_SEMANTIC_COVERAGE_REPORT.md`

Do not create `llm-reference/` in this workflow.

## Job Scope

### S001 - Audit method and baseline

Create `semantic-coverage/README.md` and the initial `KO_EN_SEMANTIC_COVERAGE_REPORT.md`. Record the semantic-unit method, final decision rule, current git state, document counts, previous J/P workflow relationship, and the fact that previous reports are orientation only.

### S002 - Mapping inventory and unit matrix scaffold

Create or update `semantic-coverage/doc-mapping.tsv` with Korean source paths, English target paths, source type, previous evidence references, and assigned audit job. Validate path existence and count coverage.

### S003 - Tech installation configuration database

Audit:

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md`
- `DOCK/Home/25. Altibase 데이터베이스 생성 가이드__13436812.md`
- `DOCK/Home/31. Altibase 설치가이드__11698403.md`
- `DOCK/Home/41. Altibase Quick Install & Start for UNIX__13436834.md`
- `DOCK/Home/42. Altibase 설치 시 발생할 수 있는 문제상황과 조치__13437056.md`

### S004 - Tech platform disk IO

Audit:

- `DOCK/Home/21. Altibase 디스크I_O 병목을 고려한 볼륨구성 가이드__11698408.md`
- `DOCK/Home/22. Altibase 운영을 위한 Solaris 설정 가이드__11698415.md`
- `DOCK/Home/23. Altibase 운영을 위한 HPUX 설정 가이드__14057733.md`
- `DOCK/Home/24. Altibase 운영을 위한 AIX 설정 가이드__13436846.md`
- `DOCK/Home/57. Altibase 운영을 위한 Linux 설정 가이드__13436485.md`

### S005 - Tech operations startup resources

Audit:

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md`
- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md`
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md`
- `DOCK/Home/45. Altibase 운영을 위한 시스템 리소스 용량산정 가이드__14057887.md`
- `DOCK/Home/47. 문제분석을 위한 OS별 유틸리티 사용 가이드__13436866.md`
- `DOCK/Home/48. UNIX Memory Management__13436842.md`

### S006 - Tech monitoring queries

Audit `DOCK/Home/59. Altibase 모니터링 쿼리 가이드__10060431.md` against the English monitoring guide parent and child pages. Preserve query IDs, SQL, meta tables, performance views, output examples, and warnings.

### S007 - Tech CPU memory diagnostics

Audit:

- `DOCK/Home/62. Altibase CPU 과부하 현상에 대한 분석가이드__11698396.md`
- `DOCK/Home/63. Altibase Memory 사용량 증가 분석가이드__11698518.md`

### S008 - Tech replication

Audit:

- `DOCK/Home/27. Altibase 이중화 구성 가이드__13828098.md`
- `DOCK/Home/49. Altibase 이중화 제약사항 가이드__19333729.md`

### S009 - Tech backup recovery

Audit:

- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md`
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md`
- `DOCK/Home/50. Altibase 백업정책 결정을 위한 고려사항__14057586.md`

Focus on backup, recovery, archive/noarchive modes, log anchors, online/offline/logical/incremental backup, time based recovery, and failure response.

### S010 - Tech C C++ APRE precompiler

Audit:

- `DOCK/Home/33. Altibase 개발자교육__19333461.md`
- `DOCK/Home/34. Altibase Precompiler 가이드__11698385.md`
- `DOCK/Home/35. Altibase APRE(SES) _C_C++ Makefile__11698493.md`
- `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md`

### S011 - Tech client APIs

Audit:

- `DOCK/Home/32. Altibase와 unixODBC 연동 가이드__11698379.md`
- `DOCK/Home/51. Altibase window ADO.NET 개발 가이드__11698513.md`
- `DOCK/Home/53. Windows 환경의 Altibase ODBC 개발 가이드__13436856.md`
- `DOCK/Home/56. JAVA 개발 가이드__14057500.md`
- `DOCK/Home/66. Altibase PHP 연동가이드__7341461.md`

### S012 - Tech WAS integration Tomcat JEUS JBoss

Audit:

- `DOCK/Home/28. Altibase TOMCAT 연동가이드__7341030.md`
- `DOCK/Home/29. Altibase JEUS 연동가이드__7341028.md`
- `DOCK/Home/30. Altibase JBoss 연동가이드__13437492.md`

### S013 - Tech WAS integration WebLogic WebSphere

Audit:

- `DOCK/Home/52. Altibase WebSphere 연동 가이드__13435602.md`
- `DOCK/Home/60. Altibase WebLogic 연동가이드__7340101.md`

### S014 - Tech framework integration Spring iBATIS

Audit:

- `DOCK/Home/54. Altibase Spring 연동 가이드__7340945.md`
- `DOCK/Home/55. Altibase iBATIS 연동가이드__7340053.md`

### S015 - Tech framework integration MyBatis Hibernate

Audit:

- `DOCK/Home/58. Altibase Hibernate 연동가이드__14057878.md`
- `DOCK/Home/64. Altibase MyBatis 연동 가이드__7340818.md`

### S016 - Tech development SQL tuning comparison

Audit:

- `DOCK/Home/36. Altibase 개발가이드__7341274.md`
- `DOCK/Home/37. Altibase SQL 튜닝 가이드__19333563.md`
- `DOCK/Home/39. Altibase, Oracle 비교 자료__14058137.md`

### S017 - Tech migration conversion VC

Audit:

- `DOCK/Home/38. Altibase VC 2008 개발가이드__19333567.md`
- `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md`
- `DOCK/Home/46. Altibase 버전 간 마이그레이션 가이드__19333688.md`
- `DOCK/Home/61. Altibase VC 2010 개발가이드__19334121.md`
- `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md`
- `DOCK/Home/70. Migration Center 사용자 가이드__19955861.md`

### S018 - Tech Docker GeoServer SQuirrel

Audit:

- `DOCK/Home/67. Altibase 도커 가이드__14057660.md`
- `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md`
- `DOCK/Home/69. Altibase를 위한 SQuirrel SQL Client Quick 가이드__12255259.md`

### S019 - Technical attachments and source links

Revalidate all technical document-format attachments and important external links from Korean technical sources against English targets. Legacy `#` labels must be recorded as `source_limitation`, not invented URLs.

### S020 - FAQ installation patch upgrade

Audit `faq/Home/01. 설치, 패치, 업그레이드/**` against `FAQE/Home/01. Installation, Patch, Upgrade/**`.

### S021 - FAQ operation core

Audit FAQ category `02. 운영 및 관리` operation core topics, including security, users, sessions, clients, startup, configuration, and administrative procedures.

### S022 - FAQ operation storage resources

Audit remaining FAQ category `02. 운영 및 관리` topics, including logs, tablespaces, file changes, JOBs, memory/resource limits, charset, and operational changes.

### S023 - FAQ replication

Audit `faq/Home/03. 이중화/**` against `FAQE/Home/03. Replication/**`.

### S024 - FAQ backup SQL stored procedures

Audit:

- `faq/Home/04. 백업 및 복구/**`
- `faq/Home/05. SQL/**`
- `faq/Home/06. Stored Procedures/**`

### S025 - FAQ development API

Audit `faq/Home/07. 개발 및 API/**` against `FAQE/Home/07. Development and API/**`.

### S026 - FAQ monitoring

Audit `faq/Home/08. 모니터링/**` against `FAQE/Home/08. Monitoring/**`.

### S027 - FAQ error messages 09-01 to 09-10

Audit Korean FAQ error message documents whose filename begins with `09-01.` through `09-10.` against `FAQE/Home/09. Error Messages/**`.

### S028 - FAQ error messages 09-11 to 09-20

Audit Korean FAQ error message documents whose filename begins with `09-11.` through `09-20.` against `FAQE/Home/09. Error Messages/**`.

### S029 - FAQ error messages 09-21 to 09-29

Audit Korean FAQ error message documents whose filename begins with `09-21.` through `09-29.`, including nested export paths such as `faq/Home/09. 에러메시지/Home/09. 에러메시지/**`, against `FAQE/Home/09. Error Messages/**`.

### S030 - FAQ utilities others general

Audit:

- `faq/Home/11. 유틸리티/**`
- `faq/Home/12. 기타/**`
- `faq/Home/13. 일반/**`

### S031 - FAQ attachments English-only classification

Revalidate FAQ attachments, legacy labels, source links, export artifacts, and English-only `FAQE` classification boundaries. English-only pages do not prove Korean-source coverage.

### S032 - Unresolved coverage closure

Merge matrix results. Fix remaining source coverage issues in English targets where safe. There must be zero `missing` and zero `unverified` rows after this job. Any `recheck_required` row must have an explicit blocker and owner note.

### S033 - Source stabilization after coverage fixes

Run source-stability checks after all coverage fixes. Verify manifest metadata, counts, residual Korean classification, links, macro artifacts, and known stale export patterns.

### S034 - Independent matrix challenge review

Challenge the matrix. Sample and inverse-search units marked `covered`, including high-risk documents and table/code-heavy pages. If false positives are found, fix the matrix and English source documents, then rerun relevant checks.

### S035 - Final semantic coverage decision

Create or finalize `KO_EN_SEMANTIC_COVERAGE_REPORT.md`. The final decision must be exactly `COMPLETE` or `RECHECK_REQUIRED`. Do not use softer wording such as "mostly complete".

## Commit Requirement

Every successful job must:

- Review the final diff.
- Commit with a focused message.
- Leave project files clean.

Suggested commit style:

```text
docs: complete S00x semantic coverage <scope>
```
