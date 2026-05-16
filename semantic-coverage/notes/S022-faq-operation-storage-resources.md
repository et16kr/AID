# S022 - FAQ operation storage resources

## Requirement and boundary

S022 performs a semantic-unit audit for FAQ category `02. 운영 및 관리` storage/resource/log/JOB/charset operation topics. The Korean source documents are authoritative, and the English targets are the Korean-core `FAQE` pages assigned to S022 in `semantic-coverage/doc-mapping.tsv`.

Scoped Korean sources and English targets:

- `faq/Home/02. 운영 및 관리/02-02. column modify 하는 방법__8454851.md` -> `FAQE/Home/02. Operation and Management/How to modify column__16875952.md`
- `faq/Home/02. 운영 및 관리/02-05. Datafile 을 추가한 이력 확인 방법__8454956.md` -> `FAQE/Home/02. Operation and Management/How to check the history of adding datafiles__16875969.md`
- `faq/Home/02. 운영 및 관리/02-07. floating point 형 data type (double, float) 사용 시 주의사항__8454981.md` -> `FAQE/Home/02. Operation and Management/Notes on using floating point data type (double, float)__16875974.md`
- `faq/Home/02. 운영 및 관리/02-11. Maximum Capacity Specifications for Altibase__9110717.md` -> `FAQE/Home/02. Operation and Management/Maximum Capacity Specifications for Altibase__16875989.md`
- `faq/Home/02. 운영 및 관리/02-12. MEM_MAX_DB_SIZE 프로퍼티 설정 변경__8454891.md` -> `FAQE/Home/02. Operation and Management/What is MEM_MAX_DB_SIZE__16875991.md`
- `faq/Home/02. 운영 및 관리/02-16. Table 데이터는 Disk 에 저장하고 인덱스만 Memory 에 생성이 가능한가요__8454455.md` -> `FAQE/Home/02. Operation and Management/Can table data be saved on disk and only indexes can be created in memory__16876008.md`
- `faq/Home/02. 운영 및 관리/02-17. TRANSACTION_TABLE_SIZE 변경 시 고려사항__7341337.md` -> `FAQE/Home/02. Operation and Management/Notes_Considerations when changing TRANSACTION_TABLE_SIZE__16876013.md`
- `faq/Home/02. 운영 및 관리/02-20. 로그디스크 FULL이 발생하는 경우와 대처 방법__9110748.md` -> `FAQE/Home/02. Operation and Management/When log disk is FULL and its countermeasures__16876034.md`
- `faq/Home/02. 운영 및 관리/02-23. 작업(Job)객체 생성 및 실행 방법__9109696.md` -> `FAQE/Home/02. Operation and Management/How to create and execute Job objects__16876042.md`
- `faq/Home/02. 운영 및 관리/02-24. 캐릭터셋 변경 방법 상세 절차__8454470.md` -> `FAQE/Home/02. Operation and Management/Detailed procedure for changing character set__16876045.md`
- `faq/Home/02. 운영 및 관리/02-25. 테이블스페이스 데이터 파일 경로 변경 방법__9109934.md` -> `FAQE/Home/02. Operation and Management/How to change the tablespace data file path__16876049.md`
- `faq/Home/02. 운영 및 관리/02-26. 로그앵커, 온라인 로그파일, 아카이브 로그파일, 더블 라이트(Double Write)파일 경로 변경 방법__14057689.md` -> `FAQE/Home/02. Operation and Management/How to change the path of log anchor, online log file, archive log file, and double write file__16876052.md`

This job does not audit S021 operation-core topics, does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required reading and direct inspection

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`
- `semantic-coverage/doc-mapping.tsv`
- `semantic-coverage/notes/S021-faq-operation-core.md`
- The 12 Korean source documents and 12 mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S022-faq-operation-storage-resources.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-edit state

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified as `S022` was already in `Progress`.
- No uncommitted project files outside the active workflow state were present before S022 edits.

## Design note

S022 adds semantic evidence only:

- Adds `semantic-coverage/matrices/S022-faq-operation-storage-resources.tsv`
- Adds `semantic-coverage/notes/S022-faq-operation-storage-resources.md`
- Updates S022 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

No English source Markdown page required a content edit, so `manifest.json` did not require metadata updates for this job. The documentation structure is unchanged.

## Audit summary

Matrix file: `semantic-coverage/matrices/S022-faq-operation-storage-resources.tsv`

Rows by coverage status:

- `covered`: 110
- `not_applicable`: 12
- `source_limitation`: 2

Rows by source:

- F02-02 column modify: 9 rows
- F02-05 datafile history: 8 rows
- F02-07 floating point data type cautions: 8 rows
- F02-11B maximum capacity: 5 rows
- F02-12 `MEM_MAX_DB_SIZE`: 15 rows
- F02-16 disk table and memory index: 4 rows
- F02-17 `TRANSACTION_TABLE_SIZE`: 15 rows
- F02-20 log disk full: 9 rows
- F02-23 Job objects: 14 rows
- F02-24 character-set change: 8 rows
- F02-25 tablespace datafile path change: 18 rows
- F02-26 log anchor/online log/archive log/double write path change: 11 rows

### Storage and datafile operations

The English targets preserve the Korean-source semantics for column modification, `TOLERATE DATA LOSS`, `DEFAULT_DATE_FORMATE`, replication DDL caution, copy-table space requirements, and `iloader` backup guidance. The datafile-history FAQ preserves the fact that `V$DATAFILES` does not record change timestamps, the `QP_MSGLOG_FLAG=2` setup paths, the `altibase_qp.log` examples, and the grep/awk limitation for old deleted trace logs.

The tablespace datafile path procedure preserves the disk and memory current-path queries, `MEM_DB_DIR`, `DEFAULT_DISK_DB_DIR`, file-copy and verification commands, `STARTUP CONTROL`, `ALTER DATABASE RENAME DATAFILE`, `ALTER TABLESPACE ... RENAME CHECKPOINT PATH`, service startup, and the error handling for missing datafiles, invalid headers, double write files, and `CANNOT IDENTIFY DATAFILE`.

### Resource and limit topics

The maximum-capacity FAQ preserves identifier length, tablespace/datafile limits, object limits, partition/constraint limits, and replication limits including the `REPLICATION_MAX_COUNT` condition.

The `MEM_MAX_DB_SIZE` FAQ preserves the total-memory-table-space definition, exclusions for memory-table index size, MVCC old-version inclusion, increase/decrease guidance, physical memory and disk-space considerations, ulimit/kernel checks, checkpoint image file sizing SQL, `TOTAL(M)` explanation, restart requirement, error message, verification queries, and related references. The Korean `total_memory_tablespaces_usage.txt` link is a legacy `#` placeholder with no downloadable URL, so the matrix records it as `source_limitation`.

The `TRANSACTION_TABLE_SIZE` FAQ preserves the max simultaneous transaction semantics, TID caution, power-of-two/increase-only restrictions, replication sender mismatch error, version matrices, `ALTER SYSTEM` read-only behavior, migration/offline procedures, maximum values, memory usage examples, `V$MEMSTAT` rows, hang symptoms, `V$TRANSACTION_MGR`, error messages, and BUG references. The Korean source contains stray numeric export artifacts (`1`, `24`, `1`, `2`) between tables; the matrix records those as `source_limitation` and does not require carrying them into English.

### Logs, JOBs, and character set

The log-disk-full FAQ preserves the distinction between DB-file full and log-file full behavior, replication gap diagnosis with `V$REPGAP`, `ARCHIVE_FULL_ACTION` behavior, `altibase_sm.log` checkpoint evidence including `[CHECKPOINT-step9] Remove Online Log File`, the interpretation of `[None]` and `skip`, the move-and-symlink recovery script, and the `lsof` check for log files in use.

The Job-object FAQ preserves the 6.3.1+ scope, scheduler enablement properties, `JOB_THREAD_COUNT` concurrency guidance, setup procedure, procedure validation, `CREATE JOB`, 6.5.1 enable/disable semantics, `SYSTEM_.SYS_JOBS_` monitoring query, `altierr` example, and the related property descriptions for `JOB_SCHEDULER_ENABLE`, `JOB_THREAD_COUNT`, and `JOB_THREAD_QUEUE_SIZE`.

The character-set change FAQ preserves the rule that DB character set cannot be changed after creation, the delete/recreate and export/import workflow, `ALTIBASE_NLS_USE`, `V$NLS_PARAMETERS`, `aexport`, `run_il_out.sh`, `formout.sh`, `dataout.sh`, `run_is.sh`, `run_il_in.sh`, `DATA_NLS_USE`, and the Korean sample data used to validate Hangul preservation. The Korean sample strings in the English target are intentional data examples, not untranslated prose.

The log anchor, online log, archive log, and double write path-change FAQ preserves the service-downtime requirement, `V$PROPERTY` path check, file-copy/property-change instructions for `LOGANCHOR_DIR`, `LOG_DIR`, `ARCHIVE_DIR`, and `DOUBLE_WRITE_DIRECTORY`, file naming patterns, server restart, and final verification query.

## Attachment and link evidence

The scoped S022 Korean and English source files contain 0 URL-backed document-format attachments with `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` extensions.

Known legacy/source-limitation items:

- `faq/Home/02. 운영 및 관리/02-12. MEM_MAX_DB_SIZE 프로퍼티 설정 변경__8454891.md` has legacy attachment label `total_memory_tablespaces_usage.txt` with a `#` placeholder target and no downloadable URL in the source.
- `faq/Home/02. 운영 및 관리/02-17. TRANSACTION_TABLE_SIZE 변경 시 고려사항__7341337.md` has stray numeric export artifact lines around the ALTER SYSTEM/version-table section. These have no independent technical meaning and are not carried into English.

Non-document operational links and references were checked as source-link semantics:

- Korean support portal links are represented with corresponding English support/manual links where available.
- Korean cross-reference links to related FAQ pages are represented with corresponding English FAQE links.
- Legacy internal `nok.altibase.com`/`aid.altibase.com` reference links are preserved or represented by the corresponding English target link.

## Self-review

- Scope checked: S022 changed only the S022 evidence files and the S022 workflow status.
- Korean authority checked: all 12 scoped Korean source files were inspected directly.
- English target checked: all 12 mapped English target files were inspected directly.
- Matrix checked: the S022 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: product names, SQL, commands, properties, paths, version numbers, error codes, support URLs, and system views are preserved.
- Manifest checked: no English source Markdown was edited, so no `manifest.json` metadata update was required.

## Verification

Verification results after drafting, self-review, and fixes:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Pass |
| `git diff --check` | Pass |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | Pass, `51` |
| `find faq/Home -type f -name '*.md' \| wc -l` | Pass, `115` |
| `find arch/Home -type f -name '*.md' \| wc -l` | Pass, `181` |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | Pass, `241` |
| S022 TSV header, field-count, and status validation | Pass, 15 fields, 124 rows: `covered` 110, `not_applicable` 12, `source_limitation` 2 |
| S022 allowed-status validation | Pass |
| S022 scoped empty-link and macro-artifact grep | Pass after evidence-note fix, `rg` exit 1 expected no matches |
| S022 and full matrix unresolved-status grep | Pass, `rg` exit 1 expected no matches |
| Scoped document-format attachment grep for `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` | Pass, `rg` exit 1 expected no URL-backed document-format attachments |

## Final decision

S022 final decision: `COMPLETE`.
