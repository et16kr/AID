# Pass2 Korean-English Documentation Review Report

Review start date: 2026-05-16

Workspace: `/home/et16/AID`

## Summary

This report tracks the second-pass Korean-to-English documentation audit after J013. The pass2 goal is to make the English source set safer before GPTs, Codex, and other LLM reference packaging begins.

The second pass uses Korean `DOCK/Home` and `faq/Home` documents as authoritative sources. Later scoped jobs compare Korean and English content at sentence, bullet, table-row, command, SQL, configuration, warning, version, attachment, and link level, using semantic units when document structures differ.

P201 establishes the baseline and includes the newly generated pass2 workflow scaffold. It does not edit product documentation.

## P201 Baseline after J013

### Scope

P201 confirmed J013 completion, current git state, first-pass completion status, document counts, manifest validity, and pass2 audit boundaries before any pass2 product documentation editing.

### Evidence

- Current branch before P201 edits: `combine`.
- Initial dirty state: only untracked `.codex-jobs/ko-en-doc-coverage-pass2/` scaffold files.
- Latest first-pass commit before P201 edits: `dbac1de docs: complete J013 LLM handoff plan`.
- `.codex-jobs/ko-en-doc-coverage/jobs.tsv` showed `J001` through `J013` as `Done`.
- First-pass report and handoff evidence reviewed:
  - `KO_EN_DOC_REVIEW_REPORT.md`
  - `LLM_REFERENCE_REVIEW_PLAN.md`
  - `.codex-jobs/ko-en-doc-coverage/J012-final-coverage-validation.md`
  - `.codex-jobs/ko-en-doc-coverage/J013-llm-reference-handoff-package-plan.md`

### Baseline Counts

| Area | Count |
| --- | ---: |
| `DOCK/Home` Markdown files | 51 |
| `faq/Home` Markdown files | 115 |
| `arch/Home` Markdown files | 181 |
| `FAQE/Home` Markdown files | 241 |

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run_all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run-all.sh` | Passed |

The required baseline export-pattern scan was run:

```bash
rg -n "\[\]\(|Error rendering macro|Unknown macro" arch/Home FAQE/Home
```

It found four pre-existing `Unknown macro: {gliffy}` markers in `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md` at lines 29, 39, 55, and 101.

P201 did not edit that product documentation page because P201 is a baseline-only job. The finding is English-only `FAQE` material outside the Korean-core FAQ verification boundary and is recorded for later scoped export/link revalidation work.

### Changes Made

- Added `.codex-jobs/ko-en-doc-coverage-pass2/` workflow scaffold to version control.
- Added `.codex-jobs/ko-en-doc-coverage-pass2/P201-baseline-after-j013.md`.
- Added this `PASS2_KO_EN_DOC_REVIEW_REPORT.md`.
- Marked P201 as `Done` in pass2 workflow control files.

No product documentation files under `DOCK/`, `arch/`, `faq/`, or `FAQE/` were edited. `manifest.json` was not changed.

### Remaining Risk

- P201 is not a sentence-level product documentation audit; that work starts with later scoped jobs.
- The English-only `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md` page still contains four `Unknown macro: {gliffy}` markers.
- English-only `FAQE` extras remain outside Korean-source core verification unless later pass2 jobs explicitly classify and review them.

## P202 Tech audit: installation core and database creation

### Scope

P202 audited Korean installation, quick install, troubleshooting, database creation, and configuration core documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` | `arch/Home/Altibase Configuration File Guide__22642991.md` |
| `DOCK/Home/25. Altibase 데이터베이스 생성 가이드__13436812.md` | `arch/Home/Creating ALTIBASE Database__22643020.md` |
| `DOCK/Home/31. Altibase 설치가이드__11698403.md` | `arch/Home/Altibase Installation Guide__14647632.md`; `arch/Home/Altibase Installation Guide/1. Altibase HDB package installer__14647639.md`; `arch/Home/Altibase Installation Guide/2. Product Installation using the Package Installer__14647653.md`; `arch/Home/Altibase Installation Guide/3. License Key Request__14647666.md` |
| `DOCK/Home/41. Altibase Quick Install & Start for UNIX__13436834.md` | `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md` |
| `DOCK/Home/42. Altibase 설치 시 발생할 수 있는 문제상황과 조치__13437056.md` | `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md` |

### Findings And Updates

- Added missing Korean-source configuration semantics to the English configuration guide:
  - `?` in `altibase.properties` means `$ALTIBASE_HOME`.
  - `AUTO_COMMIT` session settings take precedence over `altibase.properties`.
  - Changing DB-creation-time immutable properties requires migration and DB recreation.
  - `altibase_boot.log`, `LF_PREPARE_WAIT_COUNT`, and `v$lfg` were corrected for exact searchable identifiers.
- Corrected EOS wording in both database creation and quick install documents. The Korean source says versions earlier than `Altibase ver. 6` are EOS targets; the English database creation document incorrectly included `Altibase ver. 6`.
- Fixed malformed support portal/manual links and an invalid `altibase_env.mk` URL in scoped English documents.
- Corrected installation guide details:
  - test environment version `Altibase v7.1.0`.
  - `Windows 7, 8` support table wording.
  - property-configuration step explanation.
  - post-install list of two shell scripts plus one SQL script.
  - malformed MAC address lookup table export.
- Corrected Quick Install and troubleshooting wording where Korean-source semantics or identifiers were unclear in English, including `PATH`, `altibase_boot.log`, shutdown wait behavior, iSQL utility wording, license reissue, and listener/replication port bind resolutions.
- No English change was needed for `arch/Home/Altibase Installation Guide/1. Altibase HDB package installer__14647639.md`; its APatch, patchinfo, backup, rollback, and command examples already matched the Korean source semantically.

### Attachment And Link Evidence

- Configuration, database creation, quick install, and troubleshooting PDF attachment links from Korean source pages remain preserved in the English targets.
- The scoped installation guide uses embedded image links rather than document-format attachments.
- Grep checks found no scoped `[]()`, `Error rendering macro`, `Unknown macro`, malformed `support.altibase.com/en/)]`, or invalid `http://altibase_env.mk` references after edits.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p202-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for malformed support links, invalid `http://altibase_env.mk`, export artifacts, and corrected typo patterns | Passed, no matches |
| Scoped PDF attachment preservation grep | Passed, 5 preserved links |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |

### Remaining Risk

- P202 did not add broad Korean legal boilerplate to split English installation pages because the job focused on technical installation, database creation, configuration, command, warning, version, attachment, and link semantics.
- External HTTP availability was not tested; P202 used grep-based source-link and attachment preservation checks.

## P203 Tech audit: OS platform and disk I/O setup

### Scope

P203 audited Korean disk I/O volume configuration and OS platform setup documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/21. Altibase 디스크I_O 병목을 고려한 볼륨구성 가이드__11698408.md` | `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md` |
| `DOCK/Home/22. Altibase 운영을 위한 Solaris 설정 가이드__11698415.md` | `arch/Home/Solaris Setup Guide for Altibase__14058290.md`; `arch/Home/Solaris Setup Guide for Altibase/1. Kernel Parameters__22643040.md`; `arch/Home/Solaris Setup Guide for Altibase/2. User Settings__14058294.md`; `arch/Home/Solaris Setup Guide for Altibase/3. Summary__14058296.md` |
| `DOCK/Home/23. Altibase 운영을 위한 HPUX 설정 가이드__14057733.md` | `arch/Home/HPUX Setup Guide for Altibase__14058288.md` |
| `DOCK/Home/24. Altibase 운영을 위한 AIX 설정 가이드__13436846.md` | `arch/Home/AIX Setup Guide for Altibase__14058298.md` |
| `DOCK/Home/57. Altibase 운영을 위한 Linux 설정 가이드__13436485.md` | `arch/Home/Linux Setup Guide for Altibase__22643022.md` |

### Findings And Updates

- Corrected disk I/O guide semantics:
  - version basis is now `Altibase 6.5 or later`;
  - checkpoint reference note restored;
  - undo tablespace recovery wording corrected so original data is copied back to its original location;
  - supported filesystem and Direct I/O action tables rebuilt so lost row-span semantics are explicit;
  - PDF attachment filenames, version labels, and URLs preserved.
- Corrected Solaris setup guide details:
  - `STARTUP_SHM_CHUNK_SIZE`, `EXPAND_CHUNK_PAGE_COUNT * 32K`, and `shmmni` shared-memory guidance clarified;
  - semaphore synchronization wording corrected;
  - summary kernel-parameter table rebuilt;
  - `PATH`, `LD_LIBRARY_PATH`, and `LD_LIBRARY_PATH_64` descriptions clarified.
- Corrected HPUX setup guide details:
  - semaphore, `maxdsiz_64bit`, `maxfiles`, resource limit, `SHLIB_PATH`, and multi-thread environment-variable descriptions clarified;
  - Korean-source version conditions for HPUX multi-thread settings preserved.
- Corrected AIX setup guide details:
  - missing Altibase Configuration File Guide reference restored;
  - AIX 5.2 ML03 and AIX 6.1 file-cache applicability clarified;
  - long-resident process swap-out explanation restored;
  - missing `PTHREAD_FORCE_SCOPE_SYSTEM` MxN thread-model note added;
  - `file size (fsize)`, file-cache summary rows, patch wording, and IPC channel version wording corrected.
- Corrected Linux setup guide details:
  - glibc compatibility table and summary table rebuilt so row-span semantics are explicit and searchable;
  - `max_map_count`, RHEL 7-or-later CPUfreq wording, swappiness typo, THP `[vm]` section wording, and remaining Korean text in the RHEL 6 GRUB example corrected;
  - Linux PDF attachment filenames and URLs preserved.

### Attachment And Link Evidence

- Disk I/O Korean source PDF attachments preserved in the English target: 3.
- Linux Korean source PDF attachments preserved in the English target: 2.
- Solaris, HPUX, and AIX scoped Korean pages did not contain URL-backed document-format attachments.
- The AIX IBM IV28577 reference URL remains preserved.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p203-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, export artifacts, malformed support links, invalid `http://altibase_env.mk`, stale typo patterns, and residual Korean text outside preserved attachment filenames | Passed, no matches |
| Scoped PDF attachment preservation grep | Passed, 5 preserved links |
| Scoped Markdown table pipe-count check | Passed |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P203 used grep-based source-link and attachment preservation checks.
- The AIX Korean source states that `PTHREAD_FORCE_SCOPE_SYSTEM` must be set but does not provide a value in the AIX example. The English guide now preserves the requirement, but a platform owner may still want to confirm the exact AIX setting value.

## P204 Tech audit: operations failure startup resource utilities

### Scope

P204 audited Korean failure response, startup/shutdown, system resource sizing, OS utility, UNIX memory, and operation-related configuration documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` | `arch/Home/Altibase Configuration File Guide__22642991.md` |
| `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` | `arch/Home/Responding to Failures Guide for Altibase__15138818.md`; `arch/Home/Responding to Failures Guide for Altibase/1. Classification by type of failure__15138822.md`; `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md`; `arch/Home/Responding to Failures Guide for Altibase/3. References__15138869.md` |
| `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` | `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/2. Shutting Altibase Down__14909483.md` |
| `DOCK/Home/45. Altibase 운영을 위한 시스템 리소스 용량산정 가이드__14057887.md` | `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md` |
| `DOCK/Home/47. 문제분석을 위한 OS별 유틸리티 사용 가이드__13436866.md` | `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md` |
| `DOCK/Home/48. UNIX Memory Management__13436842.md` | `arch/Home/UNIX Memory Management__16875572.md` |

### Findings And Updates

- No English documentation change was needed in `arch/Home/Altibase Configuration File Guide__22642991.md`; operation-related configuration sections already matched the Korean source after earlier pass2 updates.
- Corrected system resource sizing guide table structure and identifiers:
  - Restored Korean-source table headers for memory DB sizing and memory capacity examples.
  - Preserved the exact `SQL_CACHE` identifier.
  - Restored the `iloader` delimiter example line break.
- Corrected OS utility guide details:
  - `vmstat 1 5` now means 5 outputs at 1-second intervals.
  - The Linux `pstack` low-kernel warning is restored.
  - Function identifiers such as `mmtServiceThread::execute`, `qmx::executeInsertSelect`, `qmnINST::doItNext`, and `smrLogMgr::updateTransLSNInfo` were corrected.
  - `c++filt`, SUN `/var/adm/messages.*`, AIX `-n`, and PA-RISC wording were corrected.
- Corrected UNIX memory management guide details:
  - Solaris `lotsfree` is restored to `1/64` of total memory, with the Korean-source `5.7` or earlier version condition.
  - The allocation example now uses `*(p+i) = 1`.
  - `svmon -G`, `ps v [process id]`, `pmap`, `mmap`, `top`/`pmap`, and Red Hat wording were corrected.
- Corrected failure-response guide details:
  - Collapsed restart and connection commands were split into code blocks.
  - Hang-information commands and 30-second interval wording were normalized.
  - Insufficient disk space, tablespace emergency response wording, MVCC Garbage Data conditions, and temporary network-failure wording were clarified.
  - Korean-source ATC/support website references and the `altibase_sm.log` checkpoint/tablespace note were restored.
- Corrected startup/shutdown guide details:
  - Stage terminology and `altibase_boot.log` references were normalized.
  - `STARTUP CONTROL`, `STARTUP META`, `STARTUP SERVICE`, and `STARTUP` transition wording was clarified.
  - "SHUTDOWN IMMEDIATE" internal-operation wording now preserves dirty page flush and checkpoint wait-time semantics.

### Attachment And Link Evidence

- Scoped Korean source pages contain 6 unique URL-backed document-format attachments, and all 6 are preserved in the scoped English target set.
- The startup/shutdown PDF remains preserved in both the parent English page and the split starting page, matching the existing split-page pattern.
- Scoped grep found no empty links, `Error rendering macro`, `Unknown macro`, invalid `http://altibase_env.mk`, or malformed `support.altibase.com/)[/en/]` links after edits.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p204-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for stale mistranslations, malformed support links, invalid utility names, and corrected command typo patterns | Passed, no matches |
| Scoped attachment preservation script | Passed, 6 Korean source URLs preserved |
| Scoped fenced-code balance check | Passed for 11 scoped English files |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 10 edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P204 used grep-based source-link and attachment preservation checks.
- Some English split startup/shutdown pages contain valid English-only detail from the existing English structure where the current Korean export only has placeholder images. P204 preserved that material when it did not conflict with Korean-source meaning.

## P205 Tech audit: monitoring queries

### Scope

P205 audited the Korean Altibase monitoring queries guide against the English `arch` split guide targets. The Korean source remained authoritative and was not edited.

| Korean source | English targets |
| --- | --- |
| `DOCK/Home/59. Altibase 모니터링 쿼리 가이드__10060431.md` | `arch/Home/Altibase Monitoring Queries Guide__14058229.md`; `arch/Home/Altibase Monitoring Queries Guide/**` |

### Findings And Updates

- Preserved the existing English split-page structure; this job changed documentation content only.
- Confirmed semantic coverage of all 72 monitoring query IDs from the Korean source in the English guide.
- Restored missing Korean-source version-specific SQL and labels for service thread, tablespace, object, privilege, constraint, and replication monitoring sections.
- Restored major missing query variants, including `SV01` Altibase v4, `TS01` Altibase v5.5.1+/v5.3.3/v4, `TS03` Altibase v5.5.1+/v5.3.3-v5.3.5/v5.1.5/v4, `OB01`/`OB03` older memory-table queries, `OB05`/`OB06` disk table/index queries, and the `OB09` Altibase v4.3.9 synonym query.
- Corrected or clarified meta-table and performance-view references such as `SYSTEM_.SYS_TABLES_`, `TABLE_OID`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `INDEX_SEG_PID`, `LF_PREPARE_WAIT_COUNT`, `PREPARE_LOG_FILE_COUNT`, and `V$REPGAP`.
- Restored version warnings and usage caveats for `CLIENT_APP_INFO`, `TIMED_STATISTICS`, `REPL_MODE`, `START_FLAG`, role filters, object timestamp/access columns, package/job columns, `CHECK_CONDITION`, tablespace queries, redo log queries, GC queries, and disk buffer queries.
- Preserved source SQL identifiers where the Korean document contains them, including the `RP01` `STAUS` alias.

### Attachment And Link Evidence

- The Korean monitoring guide PDF attachment URL remains preserved in both the English parent guide page and the English overview split page.
- Scoped grep found no residual Korean text in the English monitoring guide, no empty links, and no Confluence macro error markers.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p205-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped query ID comparison | Passed, 72 Korean IDs and 72 English IDs |
| Scoped SQL/code block comparison | Passed, 88 Korean blocks and 88 English blocks |
| Scoped fenced-code balance check | Passed for all scoped English files |
| Scoped monitoring guide PDF attachment preservation grep | Passed, 2 preserved English links |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 18 edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P205 used grep-based source-link and attachment preservation checks.
- Apparent source-level typos in the Korean guide, including `STAUS` in `RP01`, were preserved because the Korean source is authoritative for this pass.

## P206 Tech audit: CPU and memory analysis

### Scope

P206 audited the Korean CPU overload and memory usage increase analysis guides against the English `arch` split guide targets. The Korean sources remained authoritative and were not edited.

| Korean source | English targets |
| --- | --- |
| `DOCK/Home/62. Altibase CPU 과부하 현상에 대한 분석가이드__11698396.md` | `arch/Home/Altibase CPU Overload Analysis Guide__14647581.md`; `arch/Home/Altibase CPU Overload Analysis Guide/**` |
| `DOCK/Home/63. Altibase Memory 사용량 증가 분석가이드__11698518.md` | `arch/Home/Altibase Memory Usage Increase Analysis Guide__14647388.md`; `arch/Home/Altibase Memory Usage Increase Analysis Guide/**` |

### Findings And Updates

- Preserved the existing English split-page structure; this job changed documentation content only.
- Corrected the CPU routine checklist so the Korean-source table order, `V$SYSSTAT` SQL, shell output block, and chronological sample history table are clear and searchable.
- Clarified CPU analysis procedure details for transaction growth, newly added services, long-running query detection, `V$PLANTEXT`, optimizer statistics collection, data growth, and query-plan changes.
- Corrected CPU query-processing and other-case explanations for PVO cost, repeated `PREPARE`, `V$SESSTAT`/`V$SESSION`, memory-table index behavior, Buffered I/O vs Direct I/O, `NLS_USE`, `Dedicated Thread`, `MULTIPLEXING_POLL_TIMEOUT`, `QUERY_PROF_FLAG`, `*.prof`, and `altiProfile`.
- Corrected the CPU summary numbering and wording for data collection, old-version statistics collection, `select-poll`, repeated DB connections, and the OS utility reference.
- Restored missing Korean-source memory overview details, including reference documents, `Altibase version 7 or later`, Linux test OS, support contact, and the Korean-source PDF attachment.
- Corrected the memory routine page for OS memory/swap checks, Linux available-memory calculations, routine collection wording, `V$MEMSTAT`, and the `V$MEMSTAT` table. Removed the bogus exported `Internal Module | Description` row.
- Corrected memory cause/resolution explanations for memory table compaction, restart behavior, query object close handling, similar SQL patterns, MVCC copy semantics, `LIMIT`, `V$MEMGC`, `ADD_OID_CNT`, `GC_OID_CNT`, and GC aging cleanup.

### Attachment And Link Evidence

- The CPU guide Korean-source PDF attachment URL is preserved in the English target set.
- The memory guide Korean-source PDF attachment URL is preserved in the English target set.
- Scoped grep found no residual Korean text in the scoped English target set and no empty links, Confluence macro error markers, malformed support links, or stale typo patterns checked for this job.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p206-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for residual Korean text, empty links, Confluence macro errors, malformed support links, and stale typo patterns | Passed, no matches |
| Scoped attachment preservation script | Passed, 2 Korean source document-format URLs preserved |
| Scoped fenced-code balance check | Passed for all 9 scoped English files |
| Scoped table pipe-count check | Passed for edited CPU and memory routine tables |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 9 edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P206 used grep-based source-link and attachment preservation checks.
- The Korean CPU source has internally inconsistent optimizer-statistics version wording: one section names `6.1.1.6.1` or later, while the summary names `6.1.1` or earlier. The English guide preserves the scoped meanings in their respective sections.
- The Korean memory routine checklist pairs a transaction-throughput row with a `v$memstat` SQL example. The English guide clarifies the row around the SQL example and `V$MEMSTAT` because the scoped page is the memory usage guide.
