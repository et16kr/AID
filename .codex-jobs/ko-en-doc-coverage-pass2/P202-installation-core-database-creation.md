# P202 Installation Core and Database Creation Audit

Date: 2026-05-16

## Scope

P202 performed a sentence-level Korean-to-English audit for the installation core, quick install, troubleshooting, database creation, and configuration core documents.

Korean source documents audited:

| Korean source | English target |
| --- | --- |
| `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` | `arch/Home/Altibase Configuration File Guide__22642991.md` |
| `DOCK/Home/25. Altibase 데이터베이스 생성 가이드__13436812.md` | `arch/Home/Creating ALTIBASE Database__22643020.md` |
| `DOCK/Home/31. Altibase 설치가이드__11698403.md` | `arch/Home/Altibase Installation Guide__14647632.md`; `arch/Home/Altibase Installation Guide/1. Altibase HDB package installer__14647639.md`; `arch/Home/Altibase Installation Guide/2. Product Installation using the Package Installer__14647653.md`; `arch/Home/Altibase Installation Guide/3. License Key Request__14647666.md` |
| `DOCK/Home/41. Altibase Quick Install & Start for UNIX__13436834.md` | `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md` |
| `DOCK/Home/42. Altibase 설치 시 발생할 수 있는 문제상황과 조치__13437056.md` | `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md` |

## Boundary

- Korean `DOCK/Home` source documents were read only.
- No final LLM consolidation was performed.
- Changes were limited to scoped English `arch/Home` documents, `manifest.json`, pass2 workflow/report files, and this note.
- The pre-existing pass2 `jobs.tsv` status change from `P202 ToDo` to `P202 Progress` was inside the workflow runtime area, so it did not block the audit; the final workflow status is `Done`.

## Design Note

No product behavior, architecture, or source-document ownership changed. Documentation structure changes were limited to correcting the malformed MAC address lookup table in the English installation guide and updating manifest metadata for edited English pages.

## Audit Method

The audit compared semantic units rather than line numbers because the installation guide is split across several English `arch` pages. Checked units included headings, bullets, table rows, command blocks, SQL examples, configuration names, warning and note text, version conditions, attachment links, and support/manual links.

## Findings And Changes

- Restored Korean-source configuration semantics in `Altibase Configuration File Guide`:
  - Documented that `?` in `altibase.properties` means the path defined by `$ALTIBASE_HOME`.
  - Added the missing `AUTO_COMMIT` session-precedence note.
  - Added the missing warning that immutable DB creation properties require data migration and DB recreation to change.
  - Corrected `altibase_boot.log`, `LF_PREPARE_WAIT_COUNT`, `v$lfg`, and wording that affected searchability.
- Corrected database creation EOS wording:
  - Korean says versions earlier than `Altibase ver. 6` are EOS targets; the English document incorrectly said `Altibase ver 6 or below`.
- Corrected installation-guide core content:
  - Fixed malformed support portal links.
  - Restored `Altibase v7.1.0` in the test environment.
  - Corrected the Windows support row and clarified the property-configuration step and post-install script list.
  - Rebuilt the MAC address lookup table so the header and OS rows are searchable and no longer exported as a broken table.
- Corrected Quick Install and troubleshooting text:
  - Aligned EOS wording with the Korean source.
  - Replaced the invalid `altibase_env.mk` URL with a file-name reference.
  - Corrected `PATH`, `altibase_boot.log`, manual portal, shutdown wait behavior, and iSQL utility wording.
  - Fixed malformed support portal/license links and unclear port-bind troubleshooting language.
- No English change was needed for `arch/Home/Altibase Installation Guide/1. Altibase HDB package installer__14647639.md`; its APatch, patchinfo, backup, rollback, and command examples already matched the Korean source semantically.

## Attachment And Link Evidence

- Preserved Korean-source PDF attachment references for:
  - configuration guide: 2 PDF links.
  - database creation guide: 1 PDF link.
  - quick install guide: 1 PDF link.
  - troubleshooting guide: 1 PDF link.
- The scoped installation guide uses embedded image links rather than document-format attachments.
- Grep checks found no scoped `[]()`, `Error rendering macro`, `Unknown macro`, malformed `support.altibase.com/en/)]`, or invalid `http://altibase_env.mk` links after the edit.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p202-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for `[]()`, `Error rendering macro`, `Unknown macro`, malformed support links, invalid `http://altibase_env.mk`, and corrected typo patterns | Passed, no matches |
| Scoped PDF attachment preservation grep for `13437165`, `13436812`, `13436834`, and `13437056` download URLs | Passed, 5 preserved links |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |

## Remaining Risk

- The Korean installation and troubleshooting pages include broad legal boilerplate that is not consistently present in the split English pages. P202 did not add that boilerplate because this job focused on technical installation, database creation, configuration, command, warning, version, attachment, and link semantics.
- External HTTP availability was not tested; P202 used grep-based link and attachment preservation checks only.
