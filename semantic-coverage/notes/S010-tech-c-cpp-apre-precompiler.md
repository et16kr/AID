# S010 Tech C C++ APRE Precompiler

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S010 performs a semantic-unit audit for the developer training, Precompiler, APRE Makefile, and APRE C/C++ New Features and Upgrade technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/33. Altibase 개발자교육__19333461.md` -> `arch/Home/Altibase Developer Training__22642996.md`
- `DOCK/Home/34. Altibase Precompiler 가이드__11698385.md` -> `arch/Home/Altibase Precompiler Guide__14647438.md`; `arch/Home/Altibase Precompiler Guide/1. Considerations for ALTIBASE Development__14647447.md`; `arch/Home/Altibase Precompiler Guide/2. How to use APRE__14647451.md`; `arch/Home/Altibase Precompiler Guide/3. APRE Sample Program__14647488.md`; `arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md`; `arch/Home/Altibase Precompiler Guide/5. Considerations when converting from other DBMSs__14647506.md`
- `DOCK/Home/35. Altibase APRE(SES) _C_C++ Makefile__11698493.md` -> `arch/Home/Altibase APRE(SES) _C_C++ Makefile__15630378.md`; `arch/Home/Altibase APRE(SES) _C_C++ Makefile/How to make a basic Makefile__15630382.md`; `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Makefile for AIX xlc__16252935.md`; `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Makefile for HP acc__16449546.md`; `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Makefile for Linux gcc__15630400.md`; `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Makefile for SUN(Solaris) cc__16678920.md`; `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Notes_Considerations__16678933.md`
- `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md` -> `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents. Direct semantic-unit comparison found no English source change was required, so `manifest.json` metadata was not changed.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S010.md`
- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- The four Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S010-tech-c-cpp-apre-precompiler.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S010 ToDo` to `S010 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area before S010 edits.

## Design Note

S010 adds semantic evidence only:

- `semantic-coverage/matrices/S010-tech-c-cpp-apre-precompiler.tsv`
- `semantic-coverage/notes/S010-tech-c-cpp-apre-precompiler.md`

The product documentation structure is unchanged. The matrix records the four Korean source documents as semantic units for metadata, overview/support information, prerequisite links, version conditions, APRE usage, C/C++ precompile and Makefile examples, library/link options, platform-specific compiler options, failover options, error causes and remedies, upgrade procedure, and attachment/link evidence.

Dense code examples are grouped as code-example units when the code block demonstrates one workflow. Error-message headings are split by cause/remedy group so error code evidence remains searchable. The Korean Makefile source line that says library notation is `-I` is recorded as covered by the English target using the technically correct `-l` option because the surrounding Korean commands and library examples (`-lapre`, `-lodbccli`, `libapre.a`, `libapre_sl.so`) establish the intended library-option semantics.

## Audit Summary

### D033 Developer Training

The English developer training page preserves:

- the basic programming guide purpose for Altibase developers;
- technical support portal and support center contact details;
- the Korean-source note that the original document was based on Altibase v5;
- the legacy Altibase v5 PDF URL from the Korean source;
- the Korean-source Altibase v7-or-later PPTX URL under a Korean source attachments section.

Legal boilerplate was intentionally excluded from technical coverage.

### D034 Precompiler Guide

The split English precompiler guide preserves the Korean source semantics for:

- APRE*C/C++ purpose, prerequisite documents, Altibase version 6-or-later Linux test environment, and support contacts;
- performance considerations, `EXPLAIN PLAN`, `iSQL`, Orange for Altibase, DBeaver, plan output, and index/CPU tuning guidance;
- thread safety limits for connection objects and the listed communication/connection errors;
- host-variable sizing, `-n`, `?` parameter marker, and colon usage;
- SQLCA error checks, predefined SQL status values, `$ALTIBASE_HOME/msg/manual.txt`, Auto-Commit/NonAuto-Commit behavior, LOB restrictions, and `SIGPIPE` handling;
- unsupported precompiler items: Dynamic Method 4, Context syntax, Procedure typeset, Ref-Cursor, array-form result sets, and system signal safety;
- APRE executable usage, `.sc` sources, basic Makefile content, `-lapre -lodbccli`, `altibase_env.mk`, host variables, SQLCA, connect/disconnect, connection types, commit/rollback, DML, cursor, FAC, dynamic SQL, function/procedure calls, `WHENEVER`, failover, and sample programs;
- frequently occurring APRE errors and remedies, including `SQLCODE=-4164`, `FETCH_TIMEOUT`, `UTRANS_TIMEOUT`, `SQL_SUCCESS_WITH_INFO`, `ERR-4103C`, and `ERR-410D2`;
- conversion considerations from other DBMSs.

No URL-backed document-format attachments were present in this Korean source.

### D035 APRE Makefile

The split English APRE Makefile pages preserve the Korean source semantics for:

- Unix APRE/SESC C/C++ precompile purpose and Linux/gcc basis with HP, SUN/Solaris, and AIX additions;
- basic Makefile rules, source examples, `gmake` recommendation, precompile and compile stages, header/library path failures, `ulpLibInterface.h`, `ulpGetSqlca`, and APRE library naming;
- system library discovery through `$ALTIBASE_HOME/install/altibase_env.mk`, `ldd`, `nm`, and `man 3 cos`;
- 32-bit/64-bit APRE client tooling, `file libapre_sl.so`, and compiler bit-option tables;
- legacy C++ library requirements for SESC up to Altibase 5.3.3 and APRE 5.5.1 C-source rewrite;
- Linux gcc, AIX xlc, HP-UX acc, and SUN/Solaris cc library tables, compile options, simple Makefile examples, and 32-bit examples;
- AIX APRE shared-library examples and warning to link `apre_sl`/`odbccli_sl` only when building the executable when multiple shared libraries are used;
- final compile-problem checklist.

No URL-backed document-format attachments were present in this Korean source.

### D044 APRE C/C++ New Features And Upgrade

The English APRE New Features and Upgrade page preserves:

- Altibase 7.3 basis, related APRE Makefile and Precompiler Guide links, and support contacts;
- definitions for Embedded SQL precompiler, SES*C/C++, and APRE*C/C++;
- feature summary for Partial C Preprocessor, C Parser, host-variable library rewrite, `DECLARE STATEMENT`, `WHENEVER`, option changes, error-message output changes, `RETURNING INTO`, and `DISCONNECT` replacing `FREE`;
- detailed examples for macro processing, C Parser, host-variable initialization/struct/array/pointer/SELECT INTO/FOR/union support, `DECLARE STATEMENT`, and `WHENEVER`;
- `-I`, `-D`, `-keyword`, and `-parse` option semantics, including the `none`, `partial`, and `full` parsing-mode table;
- `-parse none` duplicate-declaration example with `ERR-51011` and `ERR-204E`;
- upgrade precautions for semicolon syntax (`ERR-302L`), C++ source with `-parse full`, `-D`/`-I`, binary type renames, changes table, and SESC-to-APRE upgrade procedure;
- warning that direct use of internal precompiler library interfaces is prohibited.

The Korean source includes `APRE_New_Features_업그레이드_가이드.pdf` as a `#` legacy placeholder. The English page preserves the filename and placeholder label because no downloadable source URL exists.

## Attachment Evidence

URL-backed document-format attachments in this scope:

- `Altibase_개발자교육_v1.pptx`: Korean-source URL preserved in `arch/Home/Altibase Developer Training__22642996.md` under Korean source attachments.
- `D33_ALTIBASE5_개발자교육.pdf`: Korean-source URL preserved in `arch/Home/Altibase Developer Training__22642996.md`.

Legacy non-downloadable attachment placeholder:

- `APRE_New_Features_업그레이드_가이드.pdf` appears in the Korean source with `#`; English records it as a legacy placeholder with `#`.

D034 and D035 have no URL-backed document-format attachments in the scoped Korean source. Embedded PNG image links were reviewed as source-exported illustrations; their associated technical meaning is represented in English text and corresponding embedded images where relevant.

## Self-Review

- Scope checked: only S010 evidence files and S010 workflow status files were changed.
- Korean authority checked: all four scoped Korean source files were inspected directly with line-numbered reads.
- English target checked: all mapped English parent and split pages were inspected directly.
- Matrix checked: the S010 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `APRE*C/C++`, `SES*C/C++`, `apre`, `sesc`, `SQLCA`, `SQLCODE`, `SQLSTATE`, `CTF`, `STF`, `altibase_env.mk`, `libapre_sl.so`, `libodbccli_sl.so`, `-parse none`, `-lapre`, `-lodbccli`, platform compile flags, error codes, and file paths are preserved as technical identifiers.
- Product docs checked: no English source change was needed, so `manifest.json` metadata remained valid and unchanged.

## Verification

Verification results after drafting and self-review:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| S010 TSV header and column-count check | Passed: 96 data rows, 15 columns each |
| S010 coverage status check | Passed: 87 `covered`, 8 `not_applicable`, 1 `source_limitation` |
| S010 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link and macro-artifact scan over S010 English targets and evidence | Passed with exit code 1, meaning no matches |
| Scoped stale fake-link scan over S010 English targets | Passed with exit code 1, meaning no fake exported local links remain |
| Scoped document-format attachment preservation grep | Passed: both Korean-source D033 document attachment URLs are preserved in the English target, and the D044 legacy `#` PDF placeholder is recorded in English |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |

## Decision

S010 final decision: `COMPLETE`.
