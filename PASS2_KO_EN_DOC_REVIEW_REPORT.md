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

## P207 Tech audit: replication configuration and constraints

### Scope

P207 audited Korean replication configuration and replication constraints guides against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/27. Altibase 이중화 구성 가이드__13828098.md` | `arch/Home/Altibase Replication Configuration Guide__14647672.md` |
| `DOCK/Home/49. Altibase 이중화 제약사항 가이드__19333729.md` | `arch/Home/Altibase Replication Constraints Guide__22643008.md` |

### Findings And Updates

- Corrected replication configuration wording for disk sharing, Sender/Receiver behavior, network-failure retransmission, Update Conflict before-value comparison, `REPLICATION_UPDATE_REPLACE`, Off-Line Replicator, HA switchover, Lazy/Eager session use, `REPLICATION_MAX_LOGFILE`, bulk changes, Parallel Applier, sequence replication, DDL constraints, and memory/disk replication object separation.
- Normalized exported table headers and split the conflict-function table so high-availability methods, xLog contents, sender logs, conflict examples, HA layout, Lazy/Eager mode, service separation, Master / Slave conflict rules, and summary requirements are searchable and unambiguous.
- Corrected malformed support portal handling in the replication configuration guide and added Korean-source support portal and technical support center references to the replication constraints guide.
- Preserved non-translatable identifiers and values including `REPLICATION_UPDATE_REPLACE`, `REPLICATION_MAX_LOGFILE`, `ALTER SESSION SET REPLICATION = FALSE;`, `RP_MSGLOG_FLAG`, `$ALTIBASE_HOME/trc/altibase_rp_conflict.log`, `ERR-61035`, `Replication_ddl_enable`, `xLog`, `PK`, Lazy, Eager, and Off-Line Replicator.

### Attachment And Link Evidence

- The replication configuration Korean source contains embedded image links but no URL-backed document-format attachments.
- The replication constraints Korean source contains one URL-backed PDF attachment, and that URL remains preserved in the English constraints guide.
- Scoped grep found no residual Korean text in the edited English pages and no empty links, Confluence macro error markers, malformed support links, or stale typo patterns checked for this job.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p207-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for residual Korean text, empty links, Confluence macro errors, malformed support links, and stale typo patterns | Passed, no matches |
| Scoped document-format attachment preservation grep | Passed, 1 Korean source PDF URL preserved |
| Scoped Markdown table pipe-count check | Passed |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for both edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P207 used grep-based source-link and attachment preservation checks.
- Legal boilerplate beyond the technical support contact remained outside the content changes because this job focused on technical replication configuration, constraints, commands, settings, warnings, attachments, and links.

## P208 Tech audit: backup recovery and failure recovery

### Scope

P208 audited Korean backup policy, failure response recovery sections, and startup/shutdown recovery-related sections against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` | `arch/Home/Responding to Failures Guide for Altibase__15138818.md`; `arch/Home/Responding to Failures Guide for Altibase/1. Classification by type of failure__15138822.md`; `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md`; `arch/Home/Responding to Failures Guide for Altibase/3. References__15138869.md` |
| `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` | `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/2. Shutting Altibase Down__14909483.md` |
| `DOCK/Home/50. Altibase 백업정책 결정을 위한 고려사항__14057586.md` | `arch/Home/Considerations for Altibase Backup Policy__14647709.md`; `arch/Home/Considerations for Altibase Backup Policy/1. Backup Types__14647714.md`; `arch/Home/Considerations for Altibase Backup Policy/2. Considerations for Determining Backup Policy__14647722.md`; `arch/Home/Considerations for Altibase Backup Policy/3. Summary (Considerations for Altibase Backup Policy)__14647728.md` |

### Findings And Updates

- Corrected the backup-policy parent support portal link so it no longer renders as a broken concatenated `/en/` link and preserves the Korean-source support portal route.
- Normalized backup-policy tables so `aexport` and `iLoader` are clearly logical backup methods, online/offline backup are clearly physical backup methods, and level 1 differential/cumulative incremental backup methods remain under incremental backup.
- Corrected online-backup recovery wording to state that recovery is performed during the Altibase server startup process, not while the server is in normal service.
- Clarified the summary table recovery state for online and incremental backups as `Started to CONTROL stage`.
- Clarified the failure-response warning that arbitrary deletion of Altibase online log files makes the database unrecoverable.
- Preserved the exact `Remove Online Log File at LFG [0]: File[11252 ~ 11253]` `altibase_sm.log` checkpoint/log-deletion monitoring message as a code literal.
- Audited startup/shutdown recovery sections covering CONTROL-stage recovery, incomplete recovery online-log reset guidance, META restart recovery, `SHUTDOWN IMMEDIATE`, and `ABORT`; no additional English edits were needed there after earlier pass2 corrections.

### Attachment And Link Evidence

- Scoped Korean source pages contain 2 unique URL-backed document-format attachments, and both Korean source PDF URLs are preserved in the scoped English target set.
- Scoped grep found no empty links, Confluence macro error markers, malformed support links, residual Korean text, stale recovery wording, or known Korean-source typo artifacts checked for this job after edits.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p208-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, malformed support links, stale recovery wording, known Korean-source typos, and residual Korean text | Passed, no matches |
| Scoped document-format attachment preservation grep | Passed, 2 Korean source PDF URLs preserved |
| Scoped Markdown table pipe-count check | Passed |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 6 edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P208 used grep-based source-link and attachment preservation checks.
- Legal boilerplate beyond the technical support contact remained outside the content changes because this job focused on backup, recovery, failure response, startup recovery, archive log, online/offline/logical/incremental backup, warnings, attachments, and links.

## P209 Tech audit: C C++ precompiler APRE developer basics

### Scope

P209 audited Korean developer training, precompiler, APRE Makefile, and APRE C/C++ upgrade documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/33. Altibase 개발자교육__19333461.md` | `arch/Home/Altibase Developer Training__22642996.md` |
| `DOCK/Home/34. Altibase Precompiler 가이드__11698385.md` | `arch/Home/Altibase Precompiler Guide__14647438.md`; `arch/Home/Altibase Precompiler Guide/**` |
| `DOCK/Home/35. Altibase APRE(SES) _C_C++ Makefile__11698493.md` | `arch/Home/Altibase APRE(SES) _C_C++ Makefile__15630378.md`; `arch/Home/Altibase APRE(SES) _C_C++ Makefile/**` |
| `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md` | `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md` |

### Findings And Updates

- Clarified developer training version coverage, preserving both the Altibase v7-or-later training attachment and the Korean-source legacy Altibase v5 training document.
- Corrected malformed support portal links in the scoped parent pages.
- Corrected precompiler split-page details for DBeaver, `iSQL>`, APRE Makefile references, `-lapre -lodbccli`, dynamic SQL, `CTF`, failover `DSN`, timeout checks, date functions, trace collection, `UTrans`, and `CONNECT`/`DISCONNECT` conversion references.
- Corrected APRE Makefile pages for `altibase_env.mk`, compile/link option tables, OS-specific libraries, 32-bit examples, shared-library examples, APRE shared-library build restrictions on AIX, and final checklist wording.
- Replaced fake exported local links with code literals or fenced code blocks for APRE and Makefile examples.
- Restored APRE C/C++ New Features details for Embedded SQL terminology, SES/APRE version conditions, Partial C Preprocessor, C Parser, host variables, `DECLARE STATEMENT`, `WHENEVER`, upgrade steps, `-parse none`, direct precompiler-library-use warning, and the legacy PDF placeholder.
- Updated `manifest.json` metadata for all 15 edited English Markdown pages.

### Attachment And Link Evidence

- Scoped Korean source pages contain 2 URL-backed document-format attachments, and both Korean-source developer training attachment URLs are preserved in the scoped English target set.
- The Korean APRE New Features source contains the legacy placeholder `APRE_New_Features_업그레이드_가이드.pdf` with `#`; the English target records the same placeholder because no downloadable source URL is present.
- Scoped grep found no empty links, Confluence macro error markers, malformed support links, fake APRE local links, stale typo patterns, or residual visible Korean text after excluding the preserved legacy placeholder filename.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p209-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, malformed support links, fake APRE local links, stale typo patterns, and residual Korean text | Passed |
| Scoped document-format attachment preservation script | Passed, 2 Korean source URLs preserved |
| Scoped fenced-code balance check | Passed for all scoped English files |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 15 edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P209 used grep-based source-link and attachment preservation checks.
- The Korean APRE New Features legacy PDF is a `#` placeholder, so the English target can preserve the filename but cannot provide a real download URL.
- Some source-exported image URLs retain URL-encoded Korean image filenames; the visible English prose was checked separately.

## P210 Tech audit: Java ODBC ADO.NET PHP client APIs

### Scope

P210 audited Korean Java, unixODBC, Windows ODBC, ADO.NET, and PHP client API documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/32. Altibase와 unixODBC 연동 가이드__11698379.md` | `arch/Home/Altibase and unixODBC Integration Guide__14647413.md`; `arch/Home/Altibase and unixODBC Integration Guide/**` |
| `DOCK/Home/51. Altibase window ADO.NET 개발 가이드__11698513.md` | `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md`; `arch/Home/Altibase Window ADO.NET Development Guide/**` |
| `DOCK/Home/53. Windows 환경의 Altibase ODBC 개발 가이드__13436856.md` | `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md` |
| `DOCK/Home/56. JAVA 개발 가이드__14057500.md` | `arch/Home/JAVA Developer's Guide__16875544.md` |
| `DOCK/Home/66. Altibase PHP 연동가이드__7341461.md` | `arch/Home/PHP Integration Guide for Altibase__14647305.md`; `arch/Home/PHP Integration Guide for Altibase/**` |

### Findings And Updates

- Corrected malformed technical-support links in scoped parent pages while preserving the Korean-source support portal route.
- Corrected unixODBC compile and integration content for native compiler assumptions, `SQLLEN`/`SQLULEN`, `BUILD_LEGACY_64_BIT_MODE=1`, `./configure --prefix=/home/unixODBC --disable-gui --enable-threads=yes`, driver selection by `SQLLEN`, `odbcinst -j`, AIX `libodbcinst.so.1`, and `[ODBC]` trace settings.
- Replaced fake exported local-library links for unixODBC driver and manager library filenames with code literals.
- Corrected ADO.NET setup and error details for `Altibase.Data.AltibaseClient.dll`, Windows terminology, provider requirements, Q&A link, `odbccli_sl.dll`, bit-specific `altiadonetX.X.X.X_32bit.zip`/`altiadonetX.X.X.X_64bit.zip`, and DLL error causes.
- Corrected the Windows ODBC guide for the Altibase `7.1.0` Windows ODBC cutoff, support/download links, Windows Client wording, ODBC setting table order, C# section wording, and flattened BLOB code comments.
- Corrected the Java guide for connection pool and XA class names, failover CTF/STF wording, missing simultaneous-version heading, stored procedure filename, `PreparedStatement`, `executeBatch()`, `setFetchSize()` memory warning, LOB autocommit error text, LOB sample paths, and timeout error table messages.
- Corrected PHP pages for Altibase product naming, `db.php`, ODBC Manager wording, `--prefix` configure option, library-path variables, `odbc.ini`, and standard ODBC function wording.
- Updated `manifest.json` metadata for all 12 edited English Markdown pages.

### Attachment And Link Evidence

- Scoped Korean source pages contain 3 URL-backed PDF attachments, and all 3 URLs are preserved in the scoped English target set.
- Scoped grep found no empty links, Confluence macro error markers, malformed support links, fake unixODBC local links, stale typo patterns checked for this job, or residual visible Korean text.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p210-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, malformed support links, fake unixODBC local links, stale typo patterns, and residual Korean text | Passed |
| Scoped document-format attachment preservation script | Passed, 3 Korean source URLs preserved |
| Scoped fenced-code balance check | Passed for all scoped English files |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 12 edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P210 used grep-based source-link and attachment preservation checks.
- The PHP Korean source configure command appears to use single-dash options; the English page now uses standard unixODBC `./configure --prefix=... --enable-...` option spelling consistent with the scoped unixODBC guide.
- The PHP split page path and source URL still contain the pre-existing `ODBC Manger` spelling because P210 did not rename source-exported files or alter page identity metadata.

## P211 Tech audit: WAS and framework integrations

### Scope

P211 audited Korean TOMCAT, JEUS, JBoss, WebLogic, WebSphere, Spring, iBATIS, MyBatis, and Hibernate integration documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

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

### Findings And Updates

- Corrected malformed technical-support links in scoped parent pages while preserving the Korean-source support route.
- Corrected TOMCAT content for JDBC placement, resource and connection-pool wording, Korean-source TOMCAT failover limitation, Altibase v5.3.3 wording, `SessionFailOver=off`, `testOnBorrow`, `poolPrepareStatements`, and connection-pool leak cautions.
- Corrected JEUS installation and data-source content for directory structure readability, XA/local-XA wording, data-source class names, connection-pool management semantics, complete JDBC class names, and `initialPoolSize` deadlock caution.
- Corrected JBoss content for JDK requirements, package-extraction detail, broken image placeholders, `JBOSS_HOME`, JBoss startup wording, DBMS-in-use wording, and `SessionFailOver=off`.
- Corrected WebSphere content for version wording, IBM Installation Manager, Internet Explorer download note, installer execution, `$ALTIBASE_HOME`, and application URL spelling.
- Corrected Spring content for data-source file names, URL literals, class names, failover `ConnectionRetryDelay`, CTF/STF semantics, `$ALTIBASE_HOME`, transaction manager names, `AltibaseXADataSource`, JOTM URL, LOB error wording, and HelloSpring sample names.
- Corrected iBATIS content for download URLs, `ibatis-2.3.4.*` filenames, JDBC driver selection, Eclipse setup text, URL literals, `SessionFailOver=off`, multi-version labels, Spring jar names, and LOB error text.
- Corrected MyBatis and Hibernate details for support text, JDBC class-name wording, exact LOB error text, and Hibernate `SessionFailOver=off`.
- Corrected WebLogic content for unsupported JDBC specification warnings, `WL_HOME`, `$DOMAIN_HOME/autodeploy`, UI label artifacts, JDBC URL literal, deployment heading, multi-version driver table and `Altibase5.jdbc.driver.AltibaseDriver`, Altibase v5.3.3 failover/load-balancing note, and ALTIBASE 4 connection target wording.
- Updated `manifest.json` metadata for all 33 edited English Markdown pages.

### Attachment And Link Evidence

- Scoped Korean source pages contain 12 URL-backed document-format attachment filenames, and all 12 filenames are preserved in the scoped English target set.
- Scoped grep found no empty links, Confluence macro errors, broken image placeholders, malformed support links, stale typo patterns checked for this job, or residual visible Korean text.

### Verification

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

### Remaining Risk

- External HTTP availability was not tested; P211 used grep-based source-link and attachment preservation checks.
- Source-exported attachment and image URLs may retain URL-encoded Korean filenames; visible English prose was checked separately.
- Legacy WAS/framework versions and examples were kept where the Korean source kept them.

## P212 Tech audit: SQL tuning development and Oracle comparison

### Scope

P212 audited the Korean Altibase Development Guide, SQL Tuning Guide, and Altibase/Oracle Comparison documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/36. Altibase 개발가이드__7341274.md` | `arch/Home/Altibase Development Guide__14058519.md`; `arch/Home/Altibase Development Guide/**` |
| `DOCK/Home/37. Altibase SQL 튜닝 가이드__19333563.md` | `arch/Home/Altibase SQL Tuning Guide__22643010.md` |
| `DOCK/Home/39. Altibase, Oracle 비교 자료__14058137.md` | `arch/Home/Altibase_Oracle Comparison__16875638.md` |

### Findings And Updates

- Restored Korean-source overview, support route, support center, legal/disclaimer text, related technical document links, SQL Tuning Guide version wording, and exact scoped attachment filenames or URLs.
- Corrected Development Guide design/development content for Lazy/Eager replication, Off-Line replicator conditions, backup method semantics, table design and HPT wording, redo log capacity planning, `CONNTYPE`, `AUTO_COMMIT`, `ALTER SYSTEM`, threaded protocol sequence, timeout examples, `altibase_cli.ini`, prepared statement examples, execution-plan examples, and bulk-change cautions.
- Corrected Development Guide trace/error content for trace log names, `$ALTIBASE_HOME/trc`, `$ALTIBASE_HOME/msg/`, `DB` property logging, the missing `altibase_rp_conflict.log` section, replication conflict meanings, abnormal termination support guidance, `Conversion not applicable`, cursor errors, `TRX_UPDATE_MAX_LOGSIZE`, and `09-18. ERR-11118`.
- Corrected Altibase/Oracle comparison tables for support/legal overview text, deadlock detection, Altibase tablespace count `65,536`, DBMS Watcher, partition operation tables, recovery labels, `CONNECT_BY_ISCYCLE`, `CREATE TABLE AS SELECT`, `Parallel Select`, binary type row alignment, `CLI`, and Built-In Function identifier/table-row structure.
- Rebuilt the Built-In Function table at identifier level so 262 Korean data rows match 262 English data rows, including `REPLACE2`, `REGEXP_COUNT`, `BASE64_DECODE_STR`, `BASE64_ENCODE`, `ROWIDTONCHAR`, `TO_BINARY_DOUBLE`, `LAST_VALUE`, `LEAD`, `PREDICTION_PROBABILITY`, `XMLCOLATTVAL`, and `PERCENTILE_DISC`.
- Preserved non-conflicting English-only clarification where useful, including the `REP1` example-name note and the English-only `Invalid character in use` client error section.
- Updated `manifest.json` metadata for all 7 edited English Markdown pages.

### Attachment And Link Evidence

- Scoped Korean source pages contain 4 document-format references, and all 4 filenames or source URLs are preserved in the scoped English target set.
- The Development Guide PDF entries are Korean-source legacy placeholders without downloadable URLs; the English target now records the exact Korean filenames.
- Scoped grep found no empty links, Confluence macro errors, malformed support links, invalid `http://altibase_env.mk` links, or checked stale export typo patterns.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p212-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, malformed support links, invalid local links, and stale typo patterns | Passed |
| Scoped document-format attachment preservation script | Passed, 4 Korean source references preserved |
| Altibase/Oracle Built-In Function identifier/table-row comparison | Passed, 262 Korean data rows matched 262 English data rows |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |

### Remaining Risk

- External HTTP availability was not tested; P212 used grep-based source-link and attachment preservation checks.
- The Korean source contains legacy `#` placeholders for Development Guide PDFs; the English target preserves exact filenames but cannot add download URLs that the Korean source does not provide.
- The Altibase/Oracle comparison document remains a feature comparison against Oracle 12c and keeps legacy product/version context where the Korean source keeps it.
