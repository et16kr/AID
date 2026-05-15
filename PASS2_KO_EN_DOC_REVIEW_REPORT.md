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

## P213 Tech audit: migration conversion and VC guides

### Scope

P213 audited the Korean Oracle conversion, MSSQL conversion, Altibase version migration, Migration Center, VC 2008, and VC 2010 documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/38. Altibase VC 2008 개발가이드__19333567.md` | `arch/Home/Altibase VC 2008 Development Guide__19333567.md` |
| `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md` | `arch/Home/ORACLE to ALTIBASE Conversion Guide__22643038.md` |
| `DOCK/Home/46. Altibase 버전 간 마이그레이션 가이드__19333688.md` | `arch/Home/Altibase Data Migration Process Guide__22642994.md` |
| `DOCK/Home/61. Altibase VC 2010 개발가이드__19334121.md` | `arch/Home/Altibase VC 2010 Development Guide__19334121.md` |
| `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md` | `arch/Home/MSSQL to ALTIBASE Conversion Guide__22643024.md` |
| `DOCK/Home/70. Migration Center 사용자 가이드__19955861.md` | `arch/Home/Migration Center User Guide__19955861.md` |

### Findings And Updates

- Restored Korean-source support route, support center, legal/disclaimer text, and intellectual-property notice in the Oracle conversion and Altibase data migration guides.
- Restored the support route and support center in the MSSQL conversion guide, and added the `Technical Knowledge > Q&A` support route to the VC 2008, VC 2010, and Migration Center guides.
- Preserved exact Korean-source document filenames in English attachment labels and legacy placeholder notes: `ALTIBASE_VC_2008_개발가이드.zip`, `ALTIBASE_VC_2010_개발가이드.pdf`, `ALTIBASE_Oracle_변환_가이드.pdf`, `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf`, `ALTIBASE_MSSQL_변환가이드.pdf`, and `Migration_Center_사용자가이드.pdf`.
- Restored the Korean-source `iloader` performance-options link in the Altibase data migration guide and preserved the exact options `-array` and `-commit`.
- Corrected the Altibase data migration `.bad` file verification wording so users are told to confirm `.bad` file sizes are 0, and clarified the sample error-log reference as `SYS_ORDERS.log`.
- Removed an exported stray `1.` marker before the Oracle conversion `MigrationCenter` advantages subsection.
- Updated `manifest.json` metadata for all 6 edited English Markdown pages.

### Attachment And Link Evidence

- Scoped Korean source pages contain 6 document-format references, and all 6 exact filenames are preserved in the scoped English target set.
- VC 2008, VC 2010, and Migration Center document-format references preserve their original `docs.altibase.com` download URLs.
- Oracle and MSSQL conversion legacy PDF entries remain filename-only notes because the Korean source uses `#` placeholders with no downloadable URL.
- Oracle and MSSQL conversion table counts match the Korean sources at contiguous-table level.
- Scoped checks found no empty links, Confluence macro errors, malformed support links, invalid `http://altibase_env.mk` links, stale English replacement attachment names, or the checked stray marker pattern.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p213-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 6 edited English pages |
| Scoped document-format attachment preservation script | Passed, 6 Korean source filenames preserved |
| Scoped grep/Python stale-pattern check | Passed |
| Oracle and MSSQL contiguous table-count comparison | Passed |

### Remaining Risk

- External HTTP availability was not tested; P213 used grep-based source-link and attachment preservation checks.
- The Oracle and MSSQL Korean sources contain legacy `#` placeholders for old PDF files. The English targets preserve exact filenames but cannot add download URLs that the Korean sources do not provide.
- The Migration Center English target remains a condensed text guide rather than a screenshot-by-screenshot reproduction. The procedure, field, option, and supported-object semantics were audited, and the original downloadable PDF link is preserved; broad embedded image/export-link revalidation remains in later P223 scope.

## P214 Tech audit: Docker GeoServer and SQuirrel tools

### Scope

P214 audited the Korean Docker, GeoServer, and SQuirrel SQL Client documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/67. Altibase 도커 가이드__14057660.md` | `arch/Home/Altibase Docker Guide__14647741.md`; `arch/Home/Altibase Docker Guide/1. Overview of Docker__14647745.md`; `arch/Home/Altibase Docker Guide/2. Docker Installation__14647748.md`; `arch/Home/Altibase Docker Guide/3. Altibase Docker Image__14647754.md`; `arch/Home/Altibase Docker Guide/4. Creating Altibase Service Container__14647760.md`; `arch/Home/Altibase Docker Guide/5. Stopping_Deleting Altibase Service Container__14909445.md` |
| `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md` | `arch/Home/Altibase GeoServer Integration Guide__22643004.md` |
| `DOCK/Home/69. Altibase를 위한 SQuirrel SQL Client Quick 가이드__12255259.md` | `arch/Home/SQuirrel SQL Client Quick Guide for Altibase__14647622.md`; `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/1. SQuirrel SQL Client Installation__14647626.md`; `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/2. Altibase JDBC Driver Registeration__14647628.md`; `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/3. Integration with Altibase__14647630.md` |

### Findings And Updates

- Restored Korean-source support route, support center, disclaimer, release-timing notice, and intellectual-property notice in the Docker, GeoServer, and SQuirrel overview pages.
- Restored exact Korean-source Docker reference URLs for `https://www.docker.com/resources/what-container`, `https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#container-and-layers`, and `https://docs.docker.com/install/`.
- Corrected remaining Docker export damage in the `docker version` output, `docker-entrypoint.sh` example, and `set_altibase.env` example.
- Corrected Docker service-container prose for data volumes, Docker network creation, network inspection, and additional-node replication option descriptions.
- Restored the Korean-source SQuirrel note that version `3.9.1` requires Java `1.8` or later and that the guide therefore links version `3.7.1`.
- Corrected SQuirrel exported wording and structure for JDBC driver file selection and the `2.1 How to register` table-of-contents line.
- Corrected the GeoServer layer verification note so it preserves the Altibase product name and clearly states that table and column names are case-sensitive.
- Updated `manifest.json` metadata for all 9 edited English Markdown pages.

### Attachment And Link Evidence

- The scoped Korean source pages contain one URL-backed document-format ZIP link, the GeoServer importer plug-in ZIP, and it is preserved exactly in the English target.
- A scoped tracked-link check confirmed that Korean-source support, Docker, SourceForge, GeoServer importer ZIP, SQuirrel installer JAR, Docker Hub, and Docker command-reference URLs are preserved in the scoped English target set.
- English-specific manual links that point to English counterparts were retained where they do not conflict with Korean-source meaning.
- Scoped grep found no remaining `versionClient`, `bash. ./`, `occured.export`, `Create Docker network Docker network`, `created work`, `data column`, `Atlibase`, `drive file`, malformed SQuirrel TOC marker, or malformed support `/en/` link patterns in the scoped English target set.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p214-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 9 edited English pages |
| Scoped tracked-link preservation script | Passed, 16 tracked Korean-source URLs preserved |
| Scoped stale-pattern grep | Passed |

### Remaining Risk

- External HTTP availability was not tested; P214 used grep-based source-link and attachment preservation checks.
- Broad embedded-image URL revalidation was not part of P214. The scoped text audit preserved existing image references and left broader image/export checks for later workflow scope.
- The Korean GeoServer source still contains a mislabeled `GeoServer Documentation` link that points to a Red Hat CPU governor page. As in the first pass, that mismatched Korean source link was not propagated into the English target.

## P215 FAQ audit: installation and operation core

### Scope

P215 audited Korean FAQ category `01. 설치, 패치, 업그레이드` and core category `02. 운영 및 관리` operation/security/user/session/client-configuration documents against English `FAQE` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/01. 설치, 패치, 업그레이드/*` | `FAQE/Home/01. Installation, Patch, Upgrade/*` |
| `faq/Home/02. 운영 및 관리/02-03. Database 를 stop 하고 start 하는 방법__9764972.md` | `FAQE/Home/02. Operation and Management/How to start and stop the database__22642937.md` |
| `faq/Home/02. 운영 및 관리/02-04. Database 의 db name을 바꾸는 방법__10059840.md` | `FAQE/Home/02. Operation and Management/How to change the database's db name__16875966.md` |
| `faq/Home/02. 운영 및 관리/02-06. DB 이름 변경 후 server create 오류발생시__8454421.md` | `FAQE/Home/02. Operation and Management/When server create errors occur after DB name change__16875972.md` |
| `faq/Home/02. 운영 및 관리/02-09. IPC 통신을 위한 알티베이스 서버 설정__9110665.md` | `FAQE/Home/02. Operation and Management/Altibase Server Configuration for IPC Communication__22642933.md` |
| `faq/Home/02. 운영 및 관리/02-10. LOCK TIMEOUT 발생 시 조치 방법__9110702.md` | `FAQE/Home/02. Operation and Management/How to resolve when LOCK TIMEOUT occurs__16875984.md` |
| `faq/Home/02. 운영 및 관리/02-11. Lock 잡고 있는 세션을 강제로 종료하는 방법__9110706.md` | `FAQE/Home/02. Operation and Management/How to forcefully close a session that is being locked__16875986.md` |
| `faq/Home/02. 운영 및 관리/02-15. sys 유저 패스워드 변경 방법__6521708.md` | `FAQE/Home/02. Operation and Management/How to change sys user password__16876004.md` |
| `faq/Home/02. 운영 및 관리/02-17. TRANSACTION_TABLE_SIZE 변경 시 고려사항__7341337.md` | `FAQE/Home/02. Operation and Management/Notes_Considerations when changing TRANSACTION_TABLE_SIZE__16876013.md` |
| `faq/Home/02. 운영 및 관리/02-18. 데이터베이스 보안 점검 체크리스트__6521702.md` | `FAQE/Home/02. Operation and Management/Database Security Checklist__22642935.md` |
| `faq/Home/02. 운영 및 관리/02-19. 동시 접속 세션 수(MAX_CLIENT) 증가 시 고려사항__7341076.md` | `FAQE/Home/02. Operation and Management/Notes_Considerations when increasing the number of concurrent connection sessions (MAX_CLIENT)__16876028.md` |
| `faq/Home/02. 운영 및 관리/02-21. 사용자 생성(CREATE USER) 및 패스워드 변경(ALTER USER) 방법__9110757.md` | `FAQE/Home/02. Operation and Management/How to create a user (CREATE USER) and change a password (ALTER USER)__16876036.md` |
| `faq/Home/02. 운영 및 관리/02-22. 사용자 패스워드 길이 제약 - 버전 별 차이__7341322.md` | `FAQE/Home/02. Operation and Management/User password length limitation - Differences by version__22642941.md` |
| `faq/Home/02. 운영 및 관리/02-27. OS시간과 DB시간이 맞질 않습니다__22642857.md` | `FAQE/Home/02. Operation and Management/The OS time and the DB time do not match__22642939.md` |

### Findings And Updates

- No English change was needed for the platform support, `CREATE USER`/`ALTER USER`, or OS/DB time FAQ pages.
- Corrected the Unix/Linux patch FAQ for minor-version patch semantics, version boundary wording, `$ALTIBASE_HOME`, replication gap wording, step references, `CHECK_LOGFILE = 0`, and SQL/comment formatting.
- Restored the missing Altibase client installation directory listing and clarified installer prompt, shell initialization, and connection-test wording.
- Corrected Windows registry cleanup wording, DB start/stop output examples, DB-name recreation risk, and server-create error guidance.
- Corrected IPC, LOCK TIMEOUT, lock-holder session close, SYS password, `TRANSACTION_TABLE_SIZE`, and `MAX_CLIENT` wording where English was unclear or semantically different from Korean source.
- Updated the database security checklist for the Korean-source `sys`/`manager` defaults, `ALTER USER sys`, shell-history permission command, `ACCESS_LIST` example, version conditions, audit wording, and patch-note link.
- Corrected password-length wording from "digits" to "characters" and clarified the older-version first-8-character storage behavior.
- Updated `manifest.json` metadata for all 14 edited English Markdown pages.

### Attachment And Link Evidence

- The scoped Korean source set contains 0 URL-backed document-format attachments with `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` extensions.
- The scoped English target set also contains 0 URL-backed document-format attachments with those extensions.
- Scoped stale-pattern checks found no empty Markdown links, `Error rendering macro`, `Unknown macro`, stale typo patterns, stale command-output patterns, or residual Korean text in edited English pages.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p215-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`, and lock-session title) | Passed for all 14 edited English pages |
| Scoped document-format attachment grep | Passed, 0 URL-backed document-format attachments |
| Scoped stale-pattern grep | Passed |

### Remaining Risk

- External HTTP availability was not tested; P215 used source-link preservation and grep-based checks.
- Some legacy FAQE pages in this scope still preserve Confluence-exported one-line command output blocks where the Korean source has the same export shape. P215 corrected semantic drift without broadly reformatting every legacy output block.

## P216 FAQ audit: operation storage logs jobs and resources

### Scope

P216 audited the remaining Korean FAQ category `02. 운영 및 관리` pages for automatic startup, log/datafile paths, tablespace files, operational file changes, JOB objects, `MEM_MAX_DB_SIZE`, capacity/resource limits, character-set changes, and related operation topics against English `FAQE` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/02. 운영 및 관리/02-01. [Linux] Altibase 서버 프로세스 자동 시작 스크립트 등록 방법__12517478.md` | `FAQE/Home/02. Operation and Management/[Linux] How to register Altibase server process auto start script__16875947.md` |
| `faq/Home/02. 운영 및 관리/02-02. column modify 하는 방법__8454851.md` | `FAQE/Home/02. Operation and Management/How to modify column__16875952.md` |
| `faq/Home/02. 운영 및 관리/02-05. Datafile 을 추가한 이력 확인 방법__8454956.md` | `FAQE/Home/02. Operation and Management/How to check the history of adding datafiles__16875969.md` |
| `faq/Home/02. 운영 및 관리/02-07. floating point 형 data type (double, float) 사용 시 주의사항__8454981.md` | `FAQE/Home/02. Operation and Management/Notes on using floating point data type (double, float)__16875974.md` |
| `faq/Home/02. 운영 및 관리/02-08. HP-UX에서 부팅 시 알티베이스를 자동으로 시작(startup)하는 방법__9110724.md` | `FAQE/Home/02. Operation and Management/How to startup Altibase automatically when booting from HP-UX__16875976.md` |
| `faq/Home/02. 운영 및 관리/02-11. Maximum Capacity Specifications for Altibase__9110717.md` | `FAQE/Home/02. Operation and Management/Maximum Capacity Specifications for Altibase__16875989.md` |
| `faq/Home/02. 운영 및 관리/02-12. MEM_MAX_DB_SIZE 프로퍼티 설정 변경__8454891.md` | `FAQE/Home/02. Operation and Management/What is MEM_MAX_DB_SIZE__16875991.md` |
| `faq/Home/02. 운영 및 관리/02-13. PUBLIC SYNONYM 을 삭제해도 되나요__6520939.md` | `FAQE/Home/02. Operation and Management/Can PUBLIC SYNONYM be dropped__16875993.md` |
| `faq/Home/02. 운영 및 관리/02-14. Solaris에서 OS booting 시 자동 altibase startup__9110643.md` | `FAQE/Home/02. Operation and Management/Automatic altibase startup during OS booting in Solaris__16875996.md` |
| `faq/Home/02. 운영 및 관리/02-16. Table 데이터는 Disk 에 저장하고 인덱스만 Memory 에 생성이 가능한가요__8454455.md` | `FAQE/Home/02. Operation and Management/Can table data be saved on disk and only indexes can be created in memory__16876008.md` |
| `faq/Home/02. 운영 및 관리/02-20. 로그디스크 FULL이 발생하는 경우와 대처 방법__9110748.md` | `FAQE/Home/02. Operation and Management/When log disk is FULL and its countermeasures__16876034.md` |
| `faq/Home/02. 운영 및 관리/02-23. 작업(Job)객체 생성 및 실행 방법__9109696.md` | `FAQE/Home/02. Operation and Management/How to create and execute Job objects__16876042.md` |
| `faq/Home/02. 운영 및 관리/02-24. 캐릭터셋 변경 방법 상세 절차__8454470.md` | `FAQE/Home/02. Operation and Management/Detailed procedure for changing character set__16876045.md` |
| `faq/Home/02. 운영 및 관리/02-25. 테이블스페이스 데이터 파일 경로 변경 방법__9109934.md` | `FAQE/Home/02. Operation and Management/How to change the tablespace data file path__16876049.md` |
| `faq/Home/02. 운영 및 관리/02-26. 로그앵커, 온라인 로그파일, 아카이브 로그파일, 더블 라이트(Double Write)파일 경로 변경 방법__14057689.md` | `FAQE/Home/02. Operation and Management/How to change the path of log anchor, online log file, archive log file, and double write file__16876052.md` |

### Findings And Updates

- No English change was needed for the Linux automatic startup, Solaris automatic startup, or maximum-capacity FAQ pages.
- Corrected column-modify, datafile-history, floating-point, HP-UX auto-start, `MEM_MAX_DB_SIZE`, PUBLIC SYNONYM, disk-table/index, log-disk-full, JOB object, character-set, tablespace datafile path, and log/double-write path English pages where Korean-source semantics or wording were missing, unclear, or incorrect.
- Restored the JOB concurrency note that `JOB_THREAD_COUNT` should be at least the number of concurrently running JOBs to avoid execution delay.
- Restored Korean Hangul sample data in the character-set procedure so the English example verifies the same Korean-character export/import behavior as the Korean source.
- Preserved and clarified key identifiers including `V$DATAFILES`, `QP_MSGLOG_FLAG`, `$ALTIBASE_HOME/trc/altibase_qp.log`, `ALTER TABLESPACE ~ ADD DATAFILE`, `MEM_MAX_DB_SIZE`, `V$PROPERTY`, `V$DATABASE`, `ERR-311EC`, `V$REPGAP`, `[CHECKPOINT-step9] Remove Online Log File`, `JOB_THREAD_COUNT`, `LOGANCHOR_DIR`, `LOG_DIR`, `ARCHIVE_DIR`, `DOUBLE_WRITE_DIRECTORY`, and `logfile*#*`.
- Updated `manifest.json` metadata for all 12 edited English Markdown pages.

### Attachment And Link Evidence

- The scoped Korean source set contains 0 URL-backed document-format attachments with `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` extensions.
- The scoped English target set also contains 0 URL-backed document-format attachments with those extensions.
- `total_memory_tablespaces_usage.txt` remains a legacy `#` attachment placeholder in the Korean source with no URL-backed document-format attachment to preserve.
- The character-set FAQ intentionally contains Korean sample data from the Korean source; this is not residual untranslated prose.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p216-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 12 edited English pages |
| Scoped document-format attachment grep | Passed, 0 URL-backed document-format attachments |
| Scoped stale-pattern grep | Passed |

### Remaining Risk

- External HTTP availability was not tested; P216 used source-link preservation and grep-based checks.
- Some legacy FAQE pages in this scope still preserve Confluence-exported one-line command output blocks where the Korean source has the same export shape. P216 corrected semantic drift without broadly reformatting every legacy output block.

## P217 FAQ audit: replication

### Scope

P217 audited Korean FAQ category `03. 이중화` against English `FAQE/Home/03. Replication` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/03. 이중화/03-01. replication conflict 발생원인과 해결방법__9110676.md` | `FAQE/Home/03. Replication/Causes and Solutions of Replication Conflicts__16876059.md` |
| `faq/Home/03. 이중화/03-02. 동일 IP로 여러 개의 이중화 객체를 생성하는 방법__12517469.md` | `FAQE/Home/03. Replication/How to create multiple replication objects with the same IP__16876063.md` |
| `faq/Home/03. 이중화/03-03. 알티베이스 이중화 대상 테이블에 대한 DDL 작업__8454667.md` | `FAQE/Home/03. Replication/DDL operation on the table for Altibase replication__22642943.md` |
| `faq/Home/03. 이중화/03-04. 이중화 give-up에 대해__9110761.md` | `FAQE/Home/03. Replication/Replication give-up__22642945.md` |
| `faq/Home/03. 이중화/03-05. 이중화 객체 IP 변경 방법__12517463.md` | `FAQE/Home/03. Replication/How to change replication object IP__16876079.md` |
| `faq/Home/03. 이중화/03-06. 이중화 객체 생성 및 삭제 방법__13008990.md` | `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md` |
| `faq/Home/03. 이중화/03-07. 이중화 대상 테이블 추가_삭제 방법__13008994.md` | `FAQE/Home/03. Replication/How to add_delete replication target table__16876094.md` |
| `faq/Home/03. 이중화/03-08. 이중화 모니터링 쿼리__9110681.md` | `FAQE/Home/03. Replication/Replication monitoring query__22642947.md` |

### Findings And Updates

- No English change was needed for the same-IP replication object, DDL operation, replication object IP change, or replication target table add/delete FAQ pages.
- Clarified the replication conflict FAQ wording for `altibase_rp.log`, `REPLICATION_INSERT_REPLACE`, `REPLICATION_UPDATE_REPLACE`, before-image wording, and conflict-error output.
- Restored Korean-source technical document references near the replication object create/delete overview and preserved exact PDF filenames: `D24_ALTIBASE_효율적인_이중화_가이드.pdf` and `D67_ALTIBASE_이중화_제약사항_가이드.pdf`.
- Corrected the malformed `-- #` SQL comment in the `REPLICATION_PORT_NO` verification example and restored the delete-object command comment as a SQL comment.
- Clarified sender/receiver thread wording in the replication start procedure.
- Removed a duplicated replication-gap checklist from the pre-Altibase 7 section while retaining the Korean-source checklist after the Altibase 7 or later `REP_GAP_SIZE` explanation.
- Removed exported bold markup around the replication give-up table of contents.
- Updated `manifest.json` metadata for all 4 edited English Markdown pages.

### Attachment And Link Evidence

- The scoped Korean source set contains 2 URL-backed document-format PDF attachments, both in `03-06. 이중화 객체 생성 및 삭제 방법__13008990.md`.
- Both attachment URLs and exact Korean-source filenames are preserved in the scoped English target set.
- Scoped stale-pattern checks found no empty Markdown links, `Error rendering macro`, `Unknown macro`, malformed `-- #` comments, translated attachment filename labels, or checked typo patterns in `FAQE/Home/03. Replication`.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p217-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 4 edited English pages |
| Scoped document-format attachment preservation script | Passed, 2 Korean source PDF links preserved |
| Scoped stale-pattern grep | Passed |

### Remaining Risk

- External HTTP availability was not tested; P217 used source-link preservation and grep-based checks.
- The Korean conflict FAQ lists `Insert conflict` twice under the Slave processing method. Because Korean source is authoritative, the English page preserves that label rather than inferring a source correction.

## P218 FAQ audit: backup SQL and stored procedures

### Scope

P218 audited Korean FAQ categories `04. 백업 및 복구`, `05. SQL`, and `06. Stored Procedures` against English `FAQE` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용__7341694.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader__16876103.md` |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-01. aexport, iloader 란__7341696.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/What is aexport, iloader__16876105.md` |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-02. aexport 를 이용한 데이터베이스 객체 백업__7341698.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Database object backup using aexport__22642949.md` |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-03. iloader 를 이용한 데이터 다운로드__7341700.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Data download using iloader__16876147.md` |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-04. 데이터베이스 객체 생성 및 데이터 업로드__7341702.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Create database object and upload data__16876145.md` |
| `faq/Home/04. 백업 및 복구/04-02. Cold Backup한 것을 Directory 경로변경 하여 복구하는 방법__9110699.md` | `FAQE/Home/04. Backup and Recovery/How to recover cold backup by changing directory path__16876133.md` |
| `faq/Home/04. 백업 및 복구/04-03. Online Backup 및 Time Based Recovery 방법__9110695.md` | `FAQE/Home/04. Backup and Recovery/Online Backup and Time Based Recovery__16876135.md` |
| `faq/Home/05. SQL/05-01. varchar, char 타입 비교__9110650.md` | `FAQE/Home/05. SQL/Comparison between VARCHAR and CHAR types__16876151.md` |
| `faq/Home/05. SQL/05-02. 객체에 부여된 권한을 확인하는 방법__8454634.md` | `FAQE/Home/05. SQL/How to check the privileges granted to an object__16876153.md` |
| `faq/Home/06. Stored Procedures/06-01. Stored Procedure 내에서 DML 로 영향 받은 레코드 수 확인 방법__8454526.md` | `FAQE/Home/06. Stored Procedure/How to check the number of records affected by DML within the stored procedure__16876157.md` |
| `faq/Home/06. Stored Procedures/06-02. 저장 프로시저 내용 확인 방법__9110656.md` | `FAQE/Home/06. Stored Procedure/How to check the contents of stored procedure__16876159.md` |

### Findings And Updates

- No English change was needed for the `Using aexport and iloader` parent page or the `What is aexport, iloader?` definition page.
- Corrected the `aexport` database-object backup page so `.sql` files and `.sh` files are described with their Korean-source roles.
- Restored the Korean-source `ALTIBASE HDB version 5` availability condition for checking `NLS_USE` and `NLS_CHARACTERSET` in the `iloader` data download page.
- Clarified `run_il_out.sh`, `run_il_in.sh`, foreground/background execution, table-specific extraction, log checking, and generated-file naming explanations while preserving Korean-source commands.
- Clarified cold-backup path-change and online backup/time-based recovery wording for `$ALTIBASE_HOME/conf/altibase.properties`, `CONTROL`, `ALTER SYSTEM SWITCH LOGFILE`, Archivelog Mode prerequisites, `SYS_TBS_DISK_TEMP`, `RESETLOGS`, and related recovery steps.
- Rewrote the `VARCHAR`/`CHAR` comparison explanation so `0x20` padding and `0x00` valid-data comparison rules are explicit.
- Clarified object-privilege query comments without changing SQL, aliases, or system table names.
- Added code formatting and clearer wording for `SQL%ROWCOUNT`, `SYSTEM_.SYS_PROCEDURES_`, `SYSTEM_.SYS_PROC_PARSE_`, `ALL_CRT_PROC.sql`, and `aexport` stored-procedure extraction options.
- Updated `manifest.json` metadata for all 9 edited English Markdown pages.

### Attachment And Link Evidence

- The scoped Korean source set contains 1 URL-backed attachment/reference with a document or text-file extension: `SP_DML_RECORD_COUNT.txt`.
- The exact `SP_DML_RECORD_COUNT.txt` URL is preserved in the scoped English target.
- Scoped stale-pattern checks found no empty Markdown links, `Error rendering macro`, `Unknown macro`, residual Korean prose, or checked stale wording in `FAQE/Home/04. Backup and Recovery`, `FAQE/Home/05. SQL`, or `FAQE/Home/06. Stored Procedure`.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p218-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 9 edited English pages |
| Scoped document/text attachment preservation script | Passed, 1 Korean source attachment URL preserved |
| Scoped stale-pattern grep | Passed |

### Remaining Risk

- External HTTP availability was not tested; P218 used source-link preservation and grep-based checks.
- The Korean source preserves probable command/output typos such as `ls --l run_il_out.sh` and `tail -f download.d.out`. Because Korean source command text is authoritative for this audit, the English target preserves those commands and records this as a source-review risk rather than inferring corrections.

## P219 FAQ audit: development API

### Scope

P219 audited Korean FAQ category `07. 개발 및 API` against English `FAQE` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/07. 개발 및 API/07-01. Connection 연결이 끊어지는 경우와 각 경우의 에러 코드 및 에러 메세지(APRE_C_C++, SQLCLI)__9110022.md` | `FAQE/Home/07. Development and API/Connection disconnection, error codes, and error messages in each case (APRE_C_C++, SQLCLI)__16876167.md` |
| `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-01. Altibase JDBC에서 Fail-Over 사용하는 방법은__9110740.md` | `FAQE/Home/07. Development and API/JDBC/How to use Fail-Over in Altibase JDBC__16876173.md` |
| `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-02. jdbc.trc 파일 생성 위치 변경 방법__8454703.md` | `FAQE/Home/07. Development and API/JDBC/How to change the jdbc.trc file creation location__16876175.md` |
| `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-03. JDBC를 통한 서로 다른 Altibase 버전 동시 접속__22642863.md` | `FAQE/Home/07. Development and API/JDBC/Simultaneous connections to different Altibase versions via JDBC__22642951.md` |
| `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-01. 64-bit Windows에서 32-bit ODBC 설치__9110670.md` | `FAQE/Home/07. Development and API/ODBC/32-bit ODBC installation on 64-bit Windows__22642957.md` |
| `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-02. ODBC 함수, SQLFreeStmt__9110024.md` | `FAQE/Home/07. Development and API/ODBC/ODBC function, SQLFreeStmt__16876183.md` |
| `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-03. unix_odbc와 연동하기__9110646.md` | `FAQE/Home/07. Development and API/ODBC/Integrating with unix_odbc__16876187.md` |
| `faq/Home/07. 개발 및 API/07-04. PHP/07-04-01. php 사용중인데 한글이 깨집니다__8454801.md` | `FAQE/Home/07. Development and API/PHP/Hangul is broken when using php__16876191.md` |
| `faq/Home/07. 개발 및 API/07-05. Spring+iBatis 트랜잭션 관리 방법__9109742.md` | `FAQE/Home/07. Development and API/How to manage Spring+iBatis transaction__16876194.md` |

### Findings And Updates

- No English change was needed for the connection-disconnection, JDBC Fail-Over, `jdbc.trc`, multi-version JDBC, 32-bit ODBC on 64-bit Windows, `SQLFreeStmt`, or PHP Hangul troubleshooting pages; their version conditions, commands, SQL, configuration names, error codes, and procedure semantics already matched the Korean sources.
- Corrected the unixODBC page to preserve the Korean-source `http://www.unixodbc.org/` download URL and the Korean-source configure command `./configure -prefix=/home/wonsik/ODBC_HOME --enable-gui=no --enable-threads=yes`.
- Corrected the Spring+iBatis page from `SetAutoCommit(false)` to the exact Java method `setAutoCommit(false)`.
- Updated `manifest.json` metadata for both edited English Markdown pages.

### Attachment And Link Evidence

- The scoped Korean source set contains 1 URL-backed document-format attachment: `LobSpringIbatisSample.zip`.
- The exact `LobSpringIbatisSample.zip` URL is preserved in the scoped English target.
- Scoped Korean and English development/API pages contain no empty Markdown links, `Error rendering macro`, or `Unknown macro` markers.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p219-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for both edited English pages |
| Scoped document-format attachment preservation script | Passed, 1 Korean source ZIP link preserved |
| Scoped stale-pattern grep | Passed, no matches |

### Remaining Risk

- External HTTP availability was not tested; P219 used source-link preservation and grep-based checks.
- The Korean source uses `-prefix` in the unixODBC configure command. Because Korean source command text is authoritative for this audit, the English target preserves that spelling; a source owner may still want to validate whether the command should be `--prefix`.

## P220 FAQ audit: monitoring

### Scope

P220 audited Korean FAQ category `08. 모니터링` against English `FAQE` monitoring targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/08. 모니터링/08-01. Altibase에서 수행된 쿼리 로그 남기는 방법(altiProfile)은__9110730.md` | `FAQE/Home/08. Monitoring/How to log queries performed in Altibase (altiProfile)__22642959.md` |
| `faq/Home/08. 모니터링/08-02. Lock 관련 정보 조회__9109812.md` | `FAQE/Home/08. Monitoring/Lock related properties__16876204.md` |
| `faq/Home/08. 모니터링/08-03. OS별 시스템 정보 보기__9110801.md` | `FAQE/Home/08. Monitoring/System information by OS__16876206.md` |
| `faq/Home/08. 모니터링/08-04. Windows 용 모니터링 툴__7340488.md` | `FAQE/Home/08. Monitoring/Monitoring Tools for Windows__16876220.md` |
| `faq/Home/08. 모니터링/08-05. 디스크 테이블 및 인덱스 사용량__7342015.md` | `FAQE/Home/08. Monitoring/Disk table and index usage__16876226.md` |
| `faq/Home/08. 모니터링/08-05. 디스크 테이블 및 인덱스 사용량/08-05-01. ALTIBASE HDB 4.3.9.x__7342017.md` | `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 4.3.9.x__16876229.md` |
| `faq/Home/08. 모니터링/08-05. 디스크 테이블 및 인덱스 사용량/08-05-02. ALTIBASE HDB 5.1.5.x__7342019.md` | `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 5.1.5.x__16876234.md` |
| `faq/Home/08. 모니터링/08-05. 디스크 테이블 및 인덱스 사용량/08-05-03. ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1__7342021.md` | `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1__16876240.md` |
| `faq/Home/08. 모니터링/08-06. 디스크 테이블스페이스 사용량/08-06-01. ALTIBASE HDB 4.3.9__7342007.md` | `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 4.3.9__16876249.md` |
| `faq/Home/08. 모니터링/08-06. 디스크 테이블스페이스 사용량/08-06-02. ALTIBASE HDB 5.1.5__7342009.md` | `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.1.5__16876251.md` |
| `faq/Home/08. 모니터링/08-06. 디스크 테이블스페이스 사용량/08-06-03. ALTIBASE HDB 5.3.3, 5.3.5__7342011.md` | `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.3.3, 5.3.5__16876253.md` |
| `faq/Home/08. 모니터링/08-06. 디스크 테이블스페이스 사용량/08-06-04. ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__7342013.md` | `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__16876255.md` |
| `faq/Home/08. 모니터링/08-07. 롤백(rollback) 중인 쿼리를 확인하는 방법__8454580.md` | `FAQE/Home/08. Monitoring/How to determine which queries are being rolled back__16876296.md` |
| `faq/Home/08. 모니터링/08-08. 메모리 테이블 및 인덱스 사용량__8454613.md` | `FAQE/Home/08. Monitoring/Memory table and index usage__16876259.md` |
| `faq/Home/08. 모니터링/08-09. 메모리 테이블스페이스 사용량/08-09-01. ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__8454645.md` | `FAQE/Home/08. Monitoring/Memory tablespace usage/ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__16876263.md` |
| `faq/Home/08. 모니터링/08-10. 알티몬(altimon) 설정 및 실행 방법__6979592.md` | `FAQE/Home/08. Monitoring/How to set up and execute altimon__16876266.md` |
| `faq/Home/08. 모니터링/08-11. 언두 테이블스페이스(UNDO TABLESPACE)/08-11-01. 언두 테이블스페이스 사용량__7341970.md` | `FAQE/Home/08. Monitoring/Undo Tablespace/Undo tablespace usage__22642965.md` |
| `faq/Home/08. 모니터링/08-11. 언두 테이블스페이스(UNDO TABLESPACE)/08-11-02. 언두 테이블스페이스 사용량 증가 시 모니터링 방법__8455098.md` | `FAQE/Home/08. Monitoring/Undo Tablespace/Monitoring method when undo tablespace usage increases__22642963.md` |
| `faq/Home/08. 모니터링/08-12. 테이블_컬럼 정의서__12517434.md` | `FAQE/Home/08. Monitoring/Table_Column Definition__22642961.md` |

### Findings And Updates

- No English change was needed for the OS system information, ALTIBASE HDB 4.3.9.x disk table/index usage, ALTIBASE HDB 4.3.9 and 5.1.5 disk tablespace usage, rollback-query monitoring, or table/column definition pages; their command, SQL, version, warning, and link semantics already matched the Korean sources.
- Corrected `altiProfile` startup and shutdown steps so `TIMED_STATISTICS` and `QUERY_PROF_FLAG` are set in the Korean-source order.
- Corrected lock monitoring text, including `v$lock`, `v$lock_statement`, SELECT `IS_LOCK`, and DML `IX_LOCK` semantics.
- Restored the Windows altimon foreground execution command block and corrected the monitoring-query column rule to `sysdate` followed by `_MON_` aliases.
- Restored the disk table/index overview `Reference` heading from the Korean source.
- Corrected disk table/index usage SQL comments and version-specific details, including `Tablespace`, partitioned/non-partitioned comments, `SEGMENT_TYPE` comments, missing `set linesize 1024` and `set colsize 20`, LOB segment version wording, and aging warnings.
- Replaced the duplicated ALTIBASE HDB 5.1.5 disk index count SQL with the Korean-source `SYSTEM_.SYS_INDICES_` and `SYSTEM_.SYS_INDEX_PARTITIONS_` query.
- Corrected disk tablespace version notes, including `5.3.3` wording and the BUG-39985 note that no reflected tag had been released yet for ALTIBASE HDB version 6.3.1.
- Corrected memory table/index usage version scope and typos, memory tablespace `V$VOL_TABLESPACES` spelling, query heading, and tablespace state comment for state `4`.
- Corrected altimon guide cross-reference text while preserving the `ALTIMON_USER_GUIDE.pdf` attachment URL.
- Corrected undo tablespace overview wording and undo monitoring SQL alias `UNDO_PAGE_COUNT`.
- Updated `manifest.json` metadata for the 13 edited English Markdown pages.

### Attachment And Link Evidence

- The scoped Korean source set contains 2 URL-backed document-format attachments: `altimon_for_windows.zip` and `ALTIMON_USER_GUIDE.pdf`.
- The exact `altimon_for_windows.zip` and `ALTIMON_USER_GUIDE.pdf` URLs are preserved in the scoped English targets.
- Scoped Korean and English monitoring pages contain no empty Markdown links, `Error rendering macro`, or `Unknown macro` markers.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p220-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for 13 edited English pages |
| Scoped document-format attachment preservation script | Passed, 2 Korean source document links preserved |
| Scoped stale-pattern grep | Passed, no matches |
| Scoped Korean-residue grep in English targets | Passed, no matches |
| Scoped code-fence balance check | Passed |

### Remaining Risk

- External HTTP availability was not tested; P220 used source-link preservation and grep-based checks.
- The Korean FAQ source contains some terse or legacy phrasing in monitoring SQL comments. English was corrected only where the Korean-source meaning, identifier spelling, command, SQL, version condition, warning, attachment, or link was missing, outdated, incorrect, or unclear.

## P221 FAQ Error Messages Audit

### Scope

P221 audited Korean FAQ category `09. 에러메시지` against the corresponding English `FAQE/Home/09. Error Messages` targets. Korean FAQ pages remained authoritative and were not edited.

### Checked Documents

The audit covered 29 Korean FAQ source documents and 29 English targets:

| Korean source category | English target category |
| --- | --- |
| `faq/Home/09. 에러메시지/**` | `FAQE/Home/09. Error Messages/**` |

### Findings And Updates

- No English change was needed for `09-05`, `09-06`, `09-09`, `09-12`, `09-15`, `09-20`, `09-21`, `09-22`, or `09-23`; their error-code, command, SQL, version, and link semantics already matched the Korean sources.
- Corrected fetch-timeout, cursor, and fetch-across-commit explanations, including `FETCH_TIMEOUT`, COMMIT/ROLLBACK-after-cursor-open causes, solution summaries, and the version-specific communication buffer wording.
- Restored malformed V$MUTEX message and `desc v$mutex` examples into fenced code blocks and removed duplicated cause text.
- Corrected invalid or unclear technical wording for memory allocation, 8-digit `altibase_qp.log` error codes, disk temporary tablespace record size, `AUTOEXTEND` data file max size, `MEM_MAX_DB_SIZE`, `DDL_LOCK_TIMEOUT = -1`, `TRX_UPDATE_MAX_LOGSIZE`, `TEMP_MAX_PAGE_COUNT`, and task-pool overflow causes.
- Updated client/server compatibility and connection-failure wording, including `ERR-4109C`, `ERR-7101D`, `ERR-71018`, `ERR-71019`, and `ERR-91015`.
- Added the Korean-source ODBC driver screenshot URL to the English `ERR-4109C Invalid session property` page.
- Corrected replication terminology in `ERR-11075` and `ERR-71018`, preserving `altibase_rp.log`, Sender, Receiver, and `REPLICATION_LOCK_TIMEOUT` terms.
- Corrected the `tablespace does not have enough free space` `ALTER TABLESPACE ... add datafile` example and version-specific lock/wait notes.
- Updated `manifest.json` metadata for all 20 edited English Markdown pages.

### Attachment And Link Evidence

- The scoped Korean source set contains 1 URL-backed document-format attachment: `ALTIBASE_운영을_위한_HPUX_설정_가이드.pdf`.
- The exact PDF URL is preserved in the scoped English target `[Warning] Memory allocation failed`.
- The Korean-source ODBC screenshot image for `ERR-4109C Invalid session property` is now preserved in the English target.
- Scoped Korean and English error-message pages contain no empty Markdown links, `Error rendering macro`, or `Unknown macro` markers.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p221-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 20 edited English pages |
| Scoped document-format attachment preservation script | Passed, 1 Korean source document link preserved |
| Scoped stale-pattern grep | Passed, no matches |
| Scoped Korean-residue grep in English targets | Passed, no matches |
| Scoped code-fence balance check | Passed |

### Remaining Risk

- External HTTP availability was not tested; P221 used source-link preservation and grep-based checks.
- The Korean source includes a duplicated `ALTER SESSION SET` phrase in one APRE example. Because the same command text already existed in English and was outside a Korean/English discrepancy, it was left unchanged and recorded as a source-review risk.
