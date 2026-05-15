# Workflow Requirements: Korean-to-English Complete Documentation Coverage

## User Goal

When the user runs `run_all.sh`, the workflow must drive a sequence of Codex jobs that checks all Korean documentation against the English documentation and updates English documents so they include the Korean-source content.

The authoritative rule is:

- Korean documents are the source of truth.
- If Korean and English differ, update the English document from the Korean document unless the Korean source is clearly outside the job scope or the difference requires user confirmation.
- Do not delete Korean documents.
- Preserve user changes and do not revert unrelated work.
- Each successful job must commit its own result and leave the project handoff clean.

## Source Requirement Documents

Every job must read these files before making edits:

- `AGENTS.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `.codex-jobs/ko-en-doc-coverage/jobs.md`
- `.codex-jobs/ko-en-doc-coverage/workflow-requirements.md`

## Documentation Sets

| Korean source | English target | Purpose |
| --- | --- | --- |
| `DOCK/Home` | `arch/Home` | Technical documents |
| `faq/Home` | `FAQE/Home` | FAQ documents |

English-only `FAQE` extras may remain, but they do not replace the Korean-source FAQ coverage requirement.

## General Job Rules

- Read the Korean source documents and corresponding English target documents before editing.
- If an English document is split into child pages, compare the Korean source against the parent page and child pages together.
- When Korean content is missing in English, add it in English at the closest corresponding location.
- Preserve technical identifiers exactly where appropriate:
  - Product names
  - SQL
  - Commands
  - File paths
  - Environment variables
  - Property names
  - Error codes
  - Version numbers
- Prefer natural technical English over literal machine translation.
- Update `manifest.json` metadata for any Markdown file whose body changes.
- Update the relevant review report or job note with what was checked, what changed, and what remains risky.

## Required Validation

Each job must run checks proportional to its scope. At minimum, run:

```bash
python3 -m json.tool manifest.json
git diff --check
```

Jobs that compare mappings or attachments must also check:

```bash
find DOCK/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

If a job updates attachment references, it must verify `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.zip` links from Korean sources are present in the matching English targets.

## Job Scope Matrix

### J001 Baseline inventory and mapping

- Confirm document counts.
- Confirm Korean-English technical mappings.
- Confirm FAQ category mappings.
- Confirm attachment inventory.
- Produce or update a baseline note under `.codex-jobs/ko-en-doc-coverage/`.

### J002 Technical docs: installation and platform setup

Review Korean `DOCK` technical documents related to:

- Configuration file guide
- Disk I/O and volume configuration
- Solaris, HPUX, AIX, Linux setup
- Database creation
- Installation guide
- Quick install and start
- Installation troubleshooting

Update corresponding English `arch` documents where Korean content is missing or newer.

### J003 Technical docs: operations and administration

Review Korean `DOCK` technical documents related to:

- Failure response
- Startup and shutdown
- System resource sizing
- OS utilities for problem analysis
- UNIX memory management
- CPU overload
- Memory usage increase
- Monitoring query guide
- Operational administration content

Update corresponding English `arch` documents where Korean content is missing or newer.

### J004 Technical docs: replication, backup, and recovery

Review Korean `DOCK` technical documents related to:

- Replication configuration
- Replication constraints
- Backup policy
- Failure response and recovery-related procedures

Update corresponding English `arch` documents where Korean content is missing or newer.

### J005 Technical docs: development and API integrations

Review Korean `DOCK` technical documents related to:

- Developer training
- Precompiler
- APRE and C/C++ Makefile
- Java
- Windows ODBC
- ADO.NET
- Spring
- iBATIS
- MyBatis
- Hibernate
- PHP
- TOMCAT, JEUS, JBoss, WebSphere, WebLogic integrations

Update corresponding English `arch` documents where Korean content is missing or newer.

### J006 Technical docs: SQL, tuning, migration, conversion, and tools

Review Korean `DOCK` technical documents related to:

- Altibase Development Guide
- SQL tuning
- Altibase and Oracle comparison
- Oracle to Altibase conversion
- MSSQL to Altibase conversion
- Altibase version-to-version migration
- Docker
- GeoServer
- SQuirrel SQL Client
- VC 2008 and VC 2010 guides
- Migration Center user guide

Update corresponding English `arch` documents where Korean content is missing or newer.

### J007 FAQ docs: installation, operation, and management

Review Korean `faq` categories:

- `01. 설치, 패치, 업그레이드`
- `02. 운영 및 관리`

Update corresponding English `FAQE` core documents where Korean content is missing or newer.

### J008 FAQ docs: replication, backup, SQL, stored procedures, and development API

Review Korean `faq` categories:

- `03. 이중화`
- `04. 백업 및 복구`
- `05. SQL`
- `06. Stored Procedures`
- `07. 개발 및 API`

Update corresponding English `FAQE` core documents where Korean content is missing or newer.

### J009 FAQ docs: monitoring, error messages, utilities, others, and general

Review Korean `faq` categories:

- `08. 모니터링`
- `09. 에러메시지`
- `11. 유틸리티`
- `12. 기타`
- `13. 일반`

Update corresponding English `FAQE` core documents where Korean content is missing or newer.

### J010 Attachment and source-link coverage

- Recheck document-format attachments in all Korean technical and FAQ documents.
- Ensure matching English documents preserve the Korean source attachment URLs when needed.
- Update English references and `manifest.json` if documents change.

### J011 English quality and LLM-readability pass

- Review changed and high-risk English documents for natural technical English.
- Preserve meaning from Korean sources.
- Improve section names, terminology consistency, and LLM searchability where safe.
- Do not perform broad rewrites that weaken traceability.

### J012 Final coverage validation and review report

- Run final coverage checks.
- Run JSON and diff validation.
- Update `KO_EN_DOC_REVIEW_REPORT.md` with final evidence and remaining risks.
- The report must state whether Korean-source content is fully represented in English within the checked scope.

### J013 LLM reference handoff package plan

- Update `LLM_REFERENCE_REVIEW_PLAN.md` or create a handoff note for the next phase.
- Define topic groups for consolidated English reference documents.
- Include source-path traceability and multilingual terminology preservation rules.

## Stop Conditions

Stop and explain the blocker instead of guessing if:

- The Korean source and English target conflict and neither source is clearly authoritative.
- The Korean source appears incorrect and changing English from it would likely introduce a technical error.
- A required English counterpart cannot be found.
- A change requires deleting, moving, or replacing original source documents.
- Validation fails and cannot be fixed within the job boundary.
