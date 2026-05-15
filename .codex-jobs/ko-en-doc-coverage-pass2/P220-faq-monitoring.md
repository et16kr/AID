# P220 FAQ Monitoring Audit

Date: 2026-05-16

## Scope

P220 audited Korean FAQ category `08. 모니터링` against the corresponding English `FAQE` monitoring targets. Korean FAQ pages remained authoritative and were not edited.

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

## Boundary And Design Note

This job did not change product behavior, architecture, or the documentation hierarchy. The existing FAQE monitoring category and child-page structure was preserved. Documentation edits were limited to Korean-source semantic corrections in existing English pages plus required manifest metadata.

## Findings And Updates

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

## Attachment And Link Evidence

- The scoped Korean source set contains 2 URL-backed document-format attachments: `altimon_for_windows.zip` and `ALTIMON_USER_GUIDE.pdf`.
- The exact `altimon_for_windows.zip` and `ALTIMON_USER_GUIDE.pdf` URLs are preserved in the scoped English targets.
- Scoped Korean and English monitoring pages contain no empty Markdown links, `Error rendering macro`, or `Unknown macro` markers.

## Self-Review

- Rechecked all scoped Korean/English pairs by semantic unit, including headings, bullets, table rows, commands, SQL, configuration identifiers, version conditions, warnings, attachments, and links.
- Rechecked edited English pages for stale identifiers and typos found during audit, including `v$loc`, `UNDO_PAGE_COUNT_COUNT`, `AGINING`, `AGAING`, `Tablesapce`, `usercan`, `V$VOL_TABLESpACES`, and incorrect `HDB 7` wording.
- Rechecked `manifest.json` `body_chars` and `word_count` against the edited English page contents.

## Verification

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

## Remaining Risk

- External HTTP availability was not tested; P220 uses source-link preservation and grep-based checks.
- The Korean FAQ source contains some terse or legacy phrasing in monitoring SQL comments. English was corrected only where the Korean-source meaning, identifier spelling, command, SQL, version condition, warning, attachment, or link was missing, outdated, incorrect, or unclear.
