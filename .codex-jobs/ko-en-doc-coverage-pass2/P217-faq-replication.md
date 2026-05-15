# P217 FAQ Replication Audit

Date: 2026-05-16

## Scope

P217 audited Korean FAQ category `03. 이중화` against the corresponding English `FAQE/Home/03. Replication` targets. Korean FAQ pages remained authoritative and were not edited.

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

## Boundary And Design Note

This job did not change product behavior, architecture, or the documentation hierarchy. The existing FAQE page structure was preserved. Documentation edits were limited to Korean-source semantic corrections, exact attachment filename preservation, and cleanup of unclear export artifacts inside existing English pages.

## Findings And Updates

- No English change was needed for the same-IP replication object, DDL operation, replication object IP change, or replication target table add/delete FAQ pages; their commands, SQL, version conditions, links, and semantic steps already matched the Korean sources.
- Clarified replication conflict wording for `altibase_rp.log`, `REPLICATION_INSERT_REPLACE`, `REPLICATION_UPDATE_REPLACE`, before-image wording, and conflict-error output while preserving the Korean-source conflict policy semantics.
- Restored the Korean-source technical document references near the overview of the replication object create/delete FAQ and preserved exact attachment filenames: `D24_ALTIBASE_효율적인_이중화_가이드.pdf` and `D67_ALTIBASE_이중화_제약사항_가이드.pdf`.
- Corrected a malformed SQL comment in the `REPLICATION_PORT_NO` verification example and restored the delete-object command comment as `-- Delete the replication object.`.
- Clarified sender/receiver thread wording in the replication start procedure.
- Removed a duplicated replication-gap checklist that appeared under the Altibase versions earlier than 7 section and kept the Korean-source checklist after the Altibase 7 or later `REP_GAP_SIZE` explanation.
- Removed exported bold markup around the replication give-up table of contents.
- Updated `manifest.json` metadata for all 4 edited English Markdown pages.

## Attachment And Link Evidence

- The scoped Korean source set contains 2 URL-backed document-format PDF attachments, both in `03-06. 이중화 객체 생성 및 삭제 방법__13008990.md`.
- Both attachment URLs and exact Korean-source filenames are preserved in the scoped English target set.
- English-specific manual/GitHub links were retained where they do not conflict with Korean-source meaning.

## Self-Review

- Rechecked commands, SQL, properties, file paths, versions, error messages, attachment filenames, and URLs against the Korean source pages.
- Rechecked the edited English pages for stale export artifacts and terminology problems: empty Markdown links, `Error rendering macro`, `Unknown macro`, malformed `-- #` comments, deleted-command bullet markers inside code blocks, `receive thread`, `sending thread`, translated attachment filenames, and common typo patterns.
- Rechecked edited-page `manifest.json` metadata against current file length and whitespace token counts.

## Verification

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
| Scoped stale-pattern grep | Passed, no matches |

## Remaining Risk

- External HTTP availability was not tested; P217 used source-link preservation and grep-based checks.
- The Korean conflict FAQ lists `Insert conflict` twice under the Slave processing method. Because Korean source is authoritative, the English page preserves that label rather than inferring a source correction.
