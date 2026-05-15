# P204 Operations Failure Startup Resource Utilities Audit

Date: 2026-05-16

## Scope

P204 performed a sentence-level Korean-to-English audit for failure response, startup/shutdown, system resource sizing, OS utility, UNIX memory, and operation-related configuration content.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` | `arch/Home/Altibase Configuration File Guide__22642991.md` |
| `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` | `arch/Home/Responding to Failures Guide for Altibase__15138818.md`; `arch/Home/Responding to Failures Guide for Altibase/1. Classification by type of failure__15138822.md`; `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md`; `arch/Home/Responding to Failures Guide for Altibase/3. References__15138869.md` |
| `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` | `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/2. Shutting Altibase Down__14909483.md` |
| `DOCK/Home/45. Altibase 운영을 위한 시스템 리소스 용량산정 가이드__14057887.md` | `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md` |
| `DOCK/Home/47. 문제분석을 위한 OS별 유틸리티 사용 가이드__13436866.md` | `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md` |
| `DOCK/Home/48. UNIX Memory Management__13436842.md` | `arch/Home/UNIX Memory Management__16875572.md` |

## Boundary

- Korean `DOCK/Home` source documents were read only.
- No final LLM consolidation was performed.
- Changes were limited to scoped English `arch/Home` documents, `manifest.json`, pass2 workflow/report files, and this note.
- The pre-existing pass2 `jobs.tsv` status change from `P204 ToDo` to `P204 Progress` was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior or architecture changed. Documentation structure changes were limited to restoring Korean-source table headers, separating collapsed command examples, normalizing support/reference links, and preserving exact technical identifiers for LLM and human searchability.

## Audit Method

The audit compared semantic units rather than line numbers because the failure-response and startup/shutdown guides are split across several English `arch` pages. Checked units included headings, paragraphs, bullets, table rows, commands, SQL, configuration identifiers, warning text, version conditions, source links, and document-format attachments.

## Findings And Changes

- No English documentation change was needed in `arch/Home/Altibase Configuration File Guide__22642991.md`; operation-related resource, session, disk I/O, and PBT property sections already matched the Korean source after earlier pass2 updates.
- Corrected system resource sizing content:
  - Restored Korean-source table headers in memory DB sizing examples.
  - Preserved the `SQL_CACHE` identifier instead of paraphrasing it as SQL Plan Cache.
  - Restored the delimiter example line break in the `iloader` backup sizing note.
- Corrected OS utility content:
  - Fixed the `vmstat 1 5` explanation to 5 outputs at 1-second intervals.
  - Restored the Linux `pstack` low-kernel warning.
  - Corrected function identifiers such as `mmtServiceThread::execute`, `qmx::executeInsertSelect`, `qmnINST::doItNext`, and `smrLogMgr::updateTransLSNInfo`.
  - Corrected `c++filt`, SUN `/var/adm/messages.*`, AIX `-n`, and PA-RISC wording.
- Corrected UNIX memory management content:
  - Restored Solaris `lotsfree` from `1/6` to `1/64` of total memory and the `5.7` or earlier version condition.
  - Corrected the Solaris allocation example from `*(p+1)` to `*(p+i)`.
  - Corrected `svmon -G`, `ps v [process id]`, `pmap`, `mmap`, `top`/`pmap`, and Red Hat wording.
- Corrected failure-response content:
  - Split collapsed restart and connection commands into code blocks.
  - Normalized hang-information collection commands and 30-second interval wording.
  - Clarified insufficient disk space, tablespace emergency response wording, MVCC Garbage Data conditions, and temporary network-failure wording.
  - Restored the Korean-source ATC/support website references and the `altibase_sm.log` checkpoint/tablespace note.
- Corrected startup/shutdown content:
  - Normalized stage terminology and `altibase_boot.log` references.
  - Clarified `STARTUP CONTROL`, `STARTUP META`, `STARTUP SERVICE`, and `STARTUP` stage-transition wording.
  - Corrected shutdown overview and "SHUTDOWN IMMEDIATE" internal-operation wording, including dirty page flush and checkpoint wait-time semantics.

## Attachment And Link Evidence

- Scoped Korean source pages contain 6 unique URL-backed document-format attachments.
- All 6 Korean source attachment URLs are preserved in the scoped English target set.
- The startup/shutdown PDF remains preserved in both the parent English page and the split starting page, matching the existing English split-page pattern.
- Scoped grep found no empty links, `Error rendering macro`, `Unknown macro`, invalid `http://altibase_env.mk`, or malformed `support.altibase.com/)[/en/]` links after edits.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p204-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for stale mistranslations, malformed support links, invalid utility names, and corrected command typo patterns | Passed, no matches |
| Scoped attachment preservation script for `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` URLs | Passed, 6 Korean source URLs preserved |
| Scoped fenced-code balance check | Passed for 11 scoped English files |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 10 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P204 used grep-based link and attachment preservation checks.
- Some English split startup/shutdown pages contain valid English-only detail from the existing English structure where the current Korean export only has placeholder images. P204 preserved that material when it did not conflict with Korean-source meaning.
