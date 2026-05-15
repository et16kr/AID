# P203 OS Platform and Disk I/O Setup Audit

Date: 2026-05-16

## Scope

P203 performed a sentence-level Korean-to-English audit for the disk I/O volume configuration guide and OS platform setup guides for Solaris, HPUX, AIX, and Linux.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/21. Altibase 디스크I_O 병목을 고려한 볼륨구성 가이드__11698408.md` | `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md` |
| `DOCK/Home/22. Altibase 운영을 위한 Solaris 설정 가이드__11698415.md` | `arch/Home/Solaris Setup Guide for Altibase__14058290.md`; `arch/Home/Solaris Setup Guide for Altibase/1. Kernel Parameters__22643040.md`; `arch/Home/Solaris Setup Guide for Altibase/2. User Settings__14058294.md`; `arch/Home/Solaris Setup Guide for Altibase/3. Summary__14058296.md` |
| `DOCK/Home/23. Altibase 운영을 위한 HPUX 설정 가이드__14057733.md` | `arch/Home/HPUX Setup Guide for Altibase__14058288.md` |
| `DOCK/Home/24. Altibase 운영을 위한 AIX 설정 가이드__13436846.md` | `arch/Home/AIX Setup Guide for Altibase__14058298.md` |
| `DOCK/Home/57. Altibase 운영을 위한 Linux 설정 가이드__13436485.md` | `arch/Home/Linux Setup Guide for Altibase__22643022.md` |

## Boundary

- Korean `DOCK/Home` source documents were read only.
- No final LLM consolidation was performed.
- Changes were limited to scoped English `arch/Home` documents, `manifest.json`, pass2 workflow/report files, and this note.
- The pre-existing pass2 `jobs.tsv` status change from `P203 ToDo` to `P203 Progress` was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior or architecture changed. Documentation structure changed only where Korean-source semantic tables had been flattened incorrectly during export. The English Linux, Solaris, AIX, and disk I/O tables were normalized into explicit rows so LLM and human readers can identify the OS, kernel parameter, filesystem, recommended value, and check command without relying on lost Confluence row spans.

## Audit Method

The audit compared semantic units rather than line numbers. Checked units included headings, bullets, table rows, command blocks, kernel parameters, environment variables, warning and note text, version conditions, attachment links, and external references.

## Findings And Changes

- Corrected disk I/O guide semantics:
  - Changed the version basis to `Altibase 6.5 or later`.
  - Restored the checkpoint reference note from the Korean source.
  - Corrected undo tablespace recovery wording so original data is copied back to its original location.
  - Rebuilt supported filesystem and Direct I/O action tables to preserve row-span meaning.
  - Preserved disk I/O PDF attachment filenames, version labels, and URLs.
- Corrected Solaris setup guide details:
  - Clarified `STARTUP_SHM_CHUNK_SIZE`, `EXPAND_CHUNK_PAGE_COUNT * 32K`, and `shmmni` startup/shared-memory guidance.
  - Corrected semaphore synchronization wording and rebuilt the summary kernel-parameter table.
  - Clarified `PATH`, `LD_LIBRARY_PATH`, and `LD_LIBRARY_PATH_64` descriptions.
- Corrected HPUX setup guide details:
  - Clarified semaphore, `maxdsiz_64bit`, `maxfiles`, resource limit, `SHLIB_PATH`, and multi-thread environment-variable descriptions.
  - Preserved Korean-source version conditions for `PERF_ENABLE`, `PTHREAD_FORCE_SCOPE_SYSTEM`, `PTHREAD_DISABLE_HANDOFF`, and `PTHREAD_SHARED_MUTEX_OLDSPIN`.
- Corrected AIX setup guide details:
  - Restored the reference to the Altibase Configuration File Guide.
  - Clarified AIX 5.2 ML03 and AIX 6.1 file-cache applicability.
  - Restored the long-resident process swap-out explanation from the Korean source.
  - Added the missing `PTHREAD_FORCE_SCOPE_SYSTEM` MxN thread-model note.
  - Corrected `file size (fsize)`, file-cache summary rows, AIX patch wording, and IPC channel version wording.
- Corrected Linux setup guide details:
  - Rebuilt the glibc compatibility table and summary table so row-span semantics are explicit and searchable.
  - Corrected `max_map_count`, RHEL 7-or-later CPUfreq wording, swappiness typo, THP `[vm]` section wording, and remaining Korean text in the RHEL 6 GRUB example.
  - Preserved Linux PDF attachment filenames and URLs.

## Attachment And Link Evidence

- Disk I/O Korean source PDF attachments preserved in the English target: 3.
- Linux Korean source PDF attachments preserved in the English target: 2.
- Solaris, HPUX, and AIX scoped Korean pages did not contain URL-backed document-format attachments.
- The AIX IBM IV28577 reference URL remains preserved.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p203-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, `Error rendering macro`, `Unknown macro`, malformed support links, invalid `http://altibase_env.mk`, stale typo patterns, and residual Korean text outside preserved attachment filenames | Passed, no matches |
| Scoped attachment preservation grep for disk I/O and Linux PDF filenames/URLs | Passed, 5 preserved links |
| Scoped Markdown table pipe-count check | Passed |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P203 used grep-based source-link and attachment preservation checks.
- The AIX Korean source states that `PTHREAD_FORCE_SCOPE_SYSTEM` must be set but does not provide a value in the AIX example. The English guide now preserves the requirement, but a platform owner may still want to confirm the exact AIX setting value.
