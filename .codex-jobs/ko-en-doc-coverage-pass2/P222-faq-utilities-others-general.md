# P222 FAQ Utilities, Others, and General Audit

Date: 2026-05-16

## Scope

P222 audited Korean FAQ categories `11. 유틸리티`, `12. 기타`, and `13. 일반` against the corresponding English `FAQE` targets. Korean FAQ pages remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/11. 유틸리티/11-01. AdminCenter2 실행 파일__8454900.md` | `FAQE/Home/11. Utilities/AdminCenter2 execution file__16876465.md` |
| `faq/Home/11. 유틸리티/11-02. iLoader/11-02-01. 도스 형식 데이터 파일을 iloader로 업로드 할 때 에러가 발생 합니다__8454513.md` | `FAQE/Home/11. Utilities/iLoader/An error occurs when uploading a DOS format data file to iloader__16876469.md` |
| `faq/Home/12. 기타/12-01. Thread process debugging방법__9109859.md` | `FAQE/Home/12. Others/Thread process debugging method__16876474.md` |
| `faq/Home/12. 기타/12-02. 대용량 DRDB Index 구축__20873218.md` | `FAQE/Home/12. Others/Building a Large-Scale DRDB Index__22642978.md` |
| `faq/Home/13. 일반/13-01. Altibase는 어떤 인터페이스를 제공하나요__9110631.md` | `FAQE/Home/13. General/What interface does Altibase provide__22642982.md` |
| `faq/Home/13. 일반/13-02. Altibase와 디스크 기반 DBMS의 가장 큰 차이점은 무엇인가요__9110635.md` | `FAQE/Home/13. General/What is the biggest difference between Altibase and disk-based DBMS__16876485.md` |
| `faq/Home/13. 일반/13-03. 메모리에 전체 데이터베이스가 존재하는데 데이터의 안전성에는 문제가 없나요__9110752.md` | `FAQE/Home/13. General/The entire database exists in memory. Is there any problem with the safety of the data__22642980.md` |

## Boundary And Design Note

This job did not change product behavior, architecture, or the documentation hierarchy. Documentation-structure edits were limited to existing FAQE pages: clearer headings, corrected inline TOC labels, fenced command examples, and Korean-source semantic wording fixes. `manifest.json` metadata was updated for every edited English page.

## Findings And Updates

- Restored the Korean-source AdminCenter2 manual note that no separate Korean version is provided, clarified that AdminCenter2 maintenance has ended, and formatted `$ALTIBASE_HOME/lib/Altibase.jar`.
- Clarified the DOS-format `iloader` upload FAQ by preserving `ERR-9102B`, `%n`, `%r%n`, `dos2unix`, `sed`, `^M`, and the upload example while correcting unclear English around row terminators and file conversion.
- Corrected the thread process debugging FAQ wording for Unix CPU overuse, hangs, `pstack`, `dbx`, and `gdb`, and fenced the exported `dbx` and `gdb` example output blocks without changing command text.
- Clarified large DRDB index guidance by formatting `SORT_AREA_SIZE`, `BUFFER_AREA_SIZE`, `DISK_INDEX_BUILD_SORT_AREA_SIZE`, and memory-multiplication expressions as searchable technical text.
- Improved the Altibase interface FAQ wording while preserving the Korean-source version conditions for JDBC, ADO.NET, PDO, and Hibernate support.
- Restored the missing overview and exact `ALTIBASE HDB` all-version wording in the in-memory versus disk-based DBMS FAQ.
- Clarified the memory safety FAQ heading and backup/recovery explanation while preserving WAL, checkpoint, backup, complete recovery, incomplete recovery, and failure-management semantics.

## Attachment And Link Evidence

- The scoped Korean source set contains 1 URL-backed document-format attachment: `AdminCenter2.zip`.
- The exact `AdminCenter2.zip` URL is preserved in the scoped English target.
- The Korean source disk-vs-memory page contains image links; the English target already contains corresponding FAQE embedded image links, and P222 did not replace those localized image references.
- Scoped Korean and English pages contain no empty Markdown links, `Error rendering macro`, or `Unknown macro` markers.

## Self-Review

- Rechecked all 7 Korean/English pairs by semantic unit, including headings, bullets, commands, configuration identifiers, version conditions, attachments, and links.
- Rechecked edited English pages for stale wording found during audit, including `procesd`, `Tthe`, `releasedby`, `over-occupies`, `DB Hang`, `unixtype`, `the iloader`, `All the versions`, `logical/physical`, and remaining Korean text.
- Rechecked code-fence balance for all 7 edited English pages.
- Rechecked `manifest.json` `body_chars` and `word_count` against the edited English page contents.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p222-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |
| Scoped document-format attachment preservation script | Passed, 1 Korean source ZIP link preserved |
| Scoped empty-link/export-artifact grep | Passed, no matches |
| Scoped stale-pattern and Korean-residue grep in English targets | Passed, no matches |
| Scoped code-fence balance check | Passed |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run_all.sh` and `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run-all.sh` | Passed |

## Remaining Risk

- External HTTP availability was not tested; P222 used source-link preservation and grep-based checks.
- The Korean source exports for the `dbx` and `gdb` examples are single-line, collapsed command/output blocks. P222 fenced them for readability but did not infer line breaks beyond the source export.
