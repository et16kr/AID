# S023 - FAQ replication

## Requirement and boundary

S023 performs a semantic-unit audit for FAQ category `03. 이중화` against the Korean-core English targets under `FAQE/Home/03. Replication`. The Korean source documents are authoritative.

Scoped Korean sources and English targets:

- `faq/Home/03. 이중화/03-01. replication conflict 발생원인과 해결방법__9110676.md` -> `FAQE/Home/03. Replication/Causes and Solutions of Replication Conflicts__16876059.md`
- `faq/Home/03. 이중화/03-02. 동일 IP로 여러 개의 이중화 객체를 생성하는 방법__12517469.md` -> `FAQE/Home/03. Replication/How to create multiple replication objects with the same IP__16876063.md`
- `faq/Home/03. 이중화/03-03. 알티베이스 이중화 대상 테이블에 대한 DDL 작업__8454667.md` -> `FAQE/Home/03. Replication/DDL operation on the table for Altibase replication__22642943.md`
- `faq/Home/03. 이중화/03-04. 이중화 give-up에 대해__9110761.md` -> `FAQE/Home/03. Replication/Replication give-up__22642945.md`
- `faq/Home/03. 이중화/03-05. 이중화 객체 IP 변경 방법__12517463.md` -> `FAQE/Home/03. Replication/How to change replication object IP__16876079.md`
- `faq/Home/03. 이중화/03-06. 이중화 객체 생성 및 삭제 방법__13008990.md` -> `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md`
- `faq/Home/03. 이중화/03-07. 이중화 대상 테이블 추가_삭제 방법__13008994.md` -> `FAQE/Home/03. Replication/How to add_delete replication target table__16876094.md`
- `faq/Home/03. 이중화/03-08. 이중화 모니터링 쿼리__9110681.md` -> `FAQE/Home/03. Replication/Replication monitoring query__22642947.md`

This job does not audit technical replication guides under `DOCK/Home`, other FAQ categories, English-only `FAQE` material, or the `llm-reference` consolidation workflow. Korean source files were not edited, and no English source document was deleted or moved.

## Required reading and direct inspection

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`
- `semantic-coverage/doc-mapping.tsv`
- `semantic-coverage/notes/S022-faq-operation-storage-resources.md`
- The 8 Korean source documents and 8 mapped English target documents listed above

Previous J/P reports were used only for orientation. Coverage decisions in `semantic-coverage/matrices/S023-faq-replication.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-edit state

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified.
- The existing `jobs.tsv` change was within the active workflow area and marked `S023` as `Progress`; no uncommitted project files outside the workflow runtime area were present before S023 edits.

## Design note

S023 adds semantic evidence only:

- Adds `semantic-coverage/matrices/S023-faq-replication.tsv`
- Adds `semantic-coverage/notes/S023-faq-replication.md`
- Updates S023 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

No English Markdown source file required a content edit, so `manifest.json` metadata did not require updates for this job. The documentation structure is unchanged.

## Audit summary

Matrix file: `semantic-coverage/matrices/S023-faq-replication.tsv`

Rows by coverage status:

- `covered`: 114
- `not_applicable`: 8
- `source_limitation`: 2

Rows by source:

- F03-01 replication conflict causes and solutions: 16 rows
- F03-02 multiple replication objects with the same IP: 9 rows
- F03-03 DDL operation on replicated tables: 10 rows
- F03-04 replication give-up: 16 rows
- F03-05 replication object IP change: 7 rows
- F03-06 replication object create/delete: 41 rows
- F03-07 add/delete replication target table: 11 rows
- F03-08 replication monitoring query: 14 rows

### Conflict handling and duplicate-host replication

The English conflict FAQ preserves the Korean-source semantics for insert, update, and delete conflicts, the `altibase_rp.log` path, `REPLICATION_INSERT_REPLACE`, `REPLICATION_UPDATE_REPLACE`, the same-key insert example, prevention guidance, User-Oriented Scheme, Master-slave Scheme, Timestamp-based Scheme, and the `ERR-11058`, `ERR-610f7`, and `ERR-61000` examples.

The duplicate-host FAQ preserves the Altibase 6.5.1 version condition, `REPLICATION_ALLOW_DUPLICATE_HOSTS`, default value `0`, `ALTER SYSTEM SET REPLICATION_ALLOW_DUPLICATE_HOSTS = 1`, `altibase.properties` persistence, successful `REP1`/`REP2` examples, `SYSTEM_.SYS_REPL_HOSTS_`, and English manual links.

### DDL, give-up, and IP change procedures

The DDL FAQ preserves the Korean-source explanation that DDL is not replicated through transaction-log based replication and must be performed on each node. The service-outage procedure preserves the session and statement checks, `V$REPGAP` gap verification, `ALTER REPLICATION ... STOP`, `DROP TABLE FROM ... TO ...`, DDL execution, `ADD TABLE FROM ... TO ...`, replication restart, and service restoration steps. The uninterrupted-service section remains represented as a cautionary, support-assisted workflow.

The replication give-up FAQ preserves the Redo-log lifecycle, checkpoint cleanup conditions, replication gap behavior, `REPLICATION_MAX_LOGFILE`, `$ALTIBASE_HOME/conf/altibase.properties`, `REPLICATION_SENDER_START_AFTER_GIVING_UP`, the `IS_STARTED` and `XSN` behavior for values `0` and `1`, checkpoint trigger timing, and `SYSTEM_.SYS_REPLICATIONS_` verification.

The IP-change FAQ preserves the full stop/add-host/drop-host/start/verify procedure using `ALTER REPLICATION replication_name STOP`, `ADD HOST`, `DROP HOST`, `START`, and `SYSTEM_.SYS_REPL_HOSTS_`.

### Replication object lifecycle and monitoring

The create/delete FAQ preserves the initial assumptions, dedicated IP and port preparation, primary-key requirement, `REPLICATION_PORT_NO` enablement flow, `netstat` port check, `altibase.properties` update, server restart, optional `ALTIBASE_PORT_NO` service-port isolation, verification queries, `CREATE REPLICATION` syntax, two-server and three-server examples, Sender/Receiver startup semantics, Sender and Receiver status queries, delete commands, and the `ERR-61023`, `ERR-61113`, and `ERR-6100D` handling guidance.

The add/delete replication-target-table FAQ preserves the stop/add/sync/start procedure, the need to run add/drop on each replication target server, `SYNC ONLY TABLE`, `SYSTEM_.SYS_REPL_ITEMS_`, and `SYSTEM_.SYS_REPLICATIONS_` status checks.

The monitoring FAQ preserves the overall replication status query, Sender query, Receiver query, pre-Altibase 7 `REP_GAP` semantics, Altibase 7 or later `REP_GAP_SIZE` and `REPLICATION_GAP_UNIT` semantics, and the network/remote-system/bulk-DML checklist for large gaps.

## Attachment and link evidence

The scoped S023 Korean source set contains 2 URL-backed document-format PDF attachments, both in `faq/Home/03. 이중화/03-06. 이중화 객체 생성 및 삭제 방법__13008990.md`:

- `D24_ALTIBASE_효율적인_이중화_가이드.pdf`
- `D67_ALTIBASE_이중화_제약사항_가이드.pdf`

Both exact filenames and `docs.altibase.com/download/attachments/13008990` URLs are preserved in `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md`.

Known source limitations:

- The Korean create/delete source contains two Gliffy diagram placeholders with no downloadable source content in the Korean Markdown export. The matrix records these as `source_limitation` with `diagram_unavailable`. The English page has embedded diagram images, but the Korean placeholder itself does not provide auditable technical text.

Non-document links were checked as source-link semantics:

- Korean support/manual links are represented by corresponding English support/manual links where available.
- Korean GitHub manual links embedded in source references are preserved or represented by matching English manual links.

## Self-review

- Scope checked: S023 changed only S023 evidence files and the S023 workflow status.
- Korean authority checked: all 8 scoped Korean source files were inspected directly.
- English target checked: all 8 mapped English target files were inspected directly.
- Matrix checked: the S023 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: product names, SQL, commands, properties, paths, version numbers, error codes, support URLs, system views, and attachment filenames are preserved.
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
| S023 TSV header, field-count, and status validation | Pass, 15 fields, 124 rows: `covered` 114, `not_applicable` 8, `source_limitation` 2 |
| S023 allowed-status validation | Pass |
| S023 scoped empty-link and macro-artifact grep | Pass, `rg` exit 1 expected no matches |
| S023 and full matrix unresolved-status grep | Pass, `rg` exit 1 expected no matches |
| Scoped document-format attachment preservation grep for `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` | Pass, 2 Korean PDF links preserved in the English target |

## Final decision

S023 final decision: `COMPLETE`.
