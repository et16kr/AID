# P216 FAQ Operation Storage Logs Jobs and Resources Audit

Date: 2026-05-16

## Scope

P216 audited the remaining Korean FAQ category `02. 운영 및 관리` pages for automatic startup, log/datafile paths, tablespace files, operational file changes, JOB objects, `MEM_MAX_DB_SIZE`, capacity/resource limits, character-set changes, and related operation topics against the corresponding English `FAQE` targets. Korean FAQ pages remained authoritative and were not edited.

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

## Boundary And Design Note

This job did not change product behavior, architecture, or the documentation hierarchy. The existing FAQE page structure was preserved. Documentation-structure edits were limited to clarifying Korean-source semantic units inside existing English pages and restoring Korean test data in the character-set change procedure where the sample verifies Hangul data handling.

## Findings And Updates

- No English change was needed for the Linux automatic startup, Solaris automatic startup, or maximum-capacity FAQ pages; their scoped semantic units already matched the Korean sources closely enough after earlier work.
- Corrected column-modify wording for the `ALTER TABLE ~ MODIFY COLUMN ~` version boundary, data-loss/load warning, and SQL Reference Manual link.
- Clarified datafile history logging around `V$DATAFILES`, `QP_MSGLOG_FLAG`, `$ALTIBASE_HOME/trc/altibase_qp.log`, and `ALTER TABLESPACE ~ ADD DATAFILE`.
- Fixed the floating-point FAQ where English incorrectly said double/float decimal values "may not be truncated"; the Korean source and examples state that values after the decimal point may be truncated in iSQL or iloader output.
- Clarified HP-UX automatic startup wording, `altibase_conf` handling, startup/shutdown terminology, and symbolic-link step text.
- Clarified `MEM_MAX_DB_SIZE` guidance for MVCC record replicas, disk-space requirements, `max memory size / virtual memory`, and the `V$PROPERTY`/`V$DATABASE` verification queries.
- Corrected PUBLIC SYNONYM wording so the reason not to drop it is tied to common queries such as dual table lookups and procedures such as print and println.
- Corrected the disk-table/index FAQ so it refers to the same tablespace type, matching the Korean source and `ERR-311EC`.
- Corrected log-disk-full guidance for replication gap wording, `[None]`/`skip` checkpoint interpretation, symbolic-link handling, and `$ALTIBASE_HOME/logs`.
- Restored the missing JOB concurrency note: when two or more JOBs may run concurrently, set `JOB_THREAD_COUNT` to at least the number of JOBs to prevent execution delay. Also corrected JOB query comments, `altierr`, and `JOB_THREAD_*` property wording.
- Restored the Korean Hangul sample data in the character-set change procedure so the example actually verifies Korean-character export/import behavior, and fixed the fused `$ sh formout.sh` step.
- Corrected tablespace datafile path wording for default-path changes, memory checkpoint path checks, error handling, double write file recovery, and CONTROL-stage DDL guidance.
- Corrected log anchor/online log/archive log/double write path wording, preserving `logfile*#*`, `LOGANCHOR_DIR`, `LOG_DIR`, `ARCHIVE_DIR`, and `DOUBLE_WRITE_DIRECTORY`.
- Updated `manifest.json` metadata for all 12 edited English Markdown pages.

## Attachment And Link Evidence

- The scoped Korean source set contains 0 URL-backed document-format attachments with `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` extensions.
- The scoped English target set also contains 0 URL-backed document-format attachments with those extensions.
- `total_memory_tablespaces_usage.txt` remains a legacy `#` attachment placeholder in the Korean source. There is no URL-backed document-format attachment to preserve.
- The character-set FAQ now intentionally contains Korean sample data from the Korean source; this is not residual untranslated prose.

## Self-Review

- Rechecked commands, SQL, properties, file paths, versions, error messages, and file name formats against Korean source meaning.
- Verified that the Korean Hangul strings restored in the English character-set page match the Korean source examples.
- Ran scoped grep checks for empty Markdown links, export artifacts, stale typo patterns, stale semantic phrases, and known bad command text.
- Rechecked edited-page `manifest.json` metadata against current file length and whitespace token counts.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p216-manifest.json` | Passed |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 12 edited English pages |
| Scoped grep for empty links, export artifacts, stale typo patterns, stale semantic phrases, and known bad command text | Passed, no matches |
| Scoped document-format attachment grep in Korean and English scoped sets | Passed, 0 URL-backed document-format attachments |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |

## Remaining Risk

- External HTTP availability was not tested; this job used source-link preservation and grep-based link checks.
- Some legacy FAQE pages in this scope still preserve Confluence-exported one-line command output blocks where the Korean source has the same export shape. P216 corrected semantic drift without broadly reformatting every legacy output block.
