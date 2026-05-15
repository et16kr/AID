# P209 C C++ Precompiler APRE Developer Basics Audit

Date: 2026-05-16

## Scope

P209 audited Korean developer training, precompiler, APRE Makefile, and APRE C/C++ upgrade documents against their English `arch` targets.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/33. Altibase 개발자교육__19333461.md` | `arch/Home/Altibase Developer Training__22642996.md` |
| `DOCK/Home/34. Altibase Precompiler 가이드__11698385.md` | `arch/Home/Altibase Precompiler Guide__14647438.md`; `arch/Home/Altibase Precompiler Guide/**` |
| `DOCK/Home/35. Altibase APRE(SES) _C_C++ Makefile__11698493.md` | `arch/Home/Altibase APRE(SES) _C_C++ Makefile__15630378.md`; `arch/Home/Altibase APRE(SES) _C_C++ Makefile/**` |
| `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md` | `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md` |

The Korean sources were treated as authoritative. No Korean source documents were edited.

## Boundary

- Completed only P209.
- Preserved the existing English parent and split-page hierarchy.
- Did not enter later Java/ODBC/API, WAS/framework, migration, FAQ, attachment-wide revalidation, or final LLM consolidation jobs.
- The pre-existing pass2 `jobs.tsv` status change from `P209 ToDo` to `P209 Progress` was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior or repository architecture changed. Documentation structure changes were limited to making existing APRE and Makefile examples searchable by restoring image-only or flattened command examples into fenced code blocks, while keeping the existing page hierarchy and source attachment placement.

## Findings And Updates

- Clarified the developer training page so the English target reflects both the Altibase v7-or-later training attachment and the Korean-source legacy Altibase v5 training document, and preserved the Korean-source support contact route.
- Corrected malformed support portal links in the precompiler, APRE Makefile, and APRE New Features parent pages.
- Updated the precompiler guide split pages for Korean-source semantics around Windows tools including DBeaver, `iSQL>` prompt output, APRE Makefile references, `-lapre -lodbccli`, dynamic SQL headings, `CTF`, failover `DSN` wording, and unsupported-item notes.
- Restored missing or unclear precompiler troubleshooting details for timeout checking, date function usage, trace collection, and `UTrans`/`QUERY_TIMEOUT` behavior.
- Updated conversion-consideration text for `CONNECT`/`DISCONNECT` references and `/absolute/path/` examples.
- Corrected APRE Makefile pages for `altibase_env.mk` references, compile/link option tables, `-lpthread`/`-lpthreads`, `-lrt`, `-brtl`, `-bexpall`, C++ compatibility libraries, 32-bit examples, shared-library examples, and APRE shared-library build restrictions on AIX.
- Replaced fake exported links such as `connect1.sc`, `libapre_sl.so`, `libconn_sl.so`, and `altibase_env.mk` with code literals or fenced Makefile examples.
- Restored APRE C/C++ New Features details from the Korean source, including Embedded SQL terminology, SES/APRE version conditions, Partial C Preprocessor and C Parser examples, host variable examples, `DECLARE STATEMENT`, `WHENEVER`, upgrade steps, `-parse none`, direct precompiler-library-use warning, and the legacy PDF placeholder.
- Updated `manifest.json` metadata for all 15 edited English Markdown pages.

## Attachment And Link Evidence

- Scoped Korean source pages contain 2 URL-backed document-format attachments, both from the developer training source.
- Both Korean-source developer training attachment URLs are preserved in the scoped English target set.
- The Korean APRE New Features source includes the legacy placeholder `APRE_New_Features_업그레이드_가이드.pdf` with `#`; the English target records the same placeholder because no downloadable source URL is present.
- Scoped grep found no empty links, Confluence macro error markers, malformed `support.altibase.com/)[/en/]` links, fake local-library/document links, or stale typo patterns checked for this job after edits.
- Residual visible Korean text check passed after excluding the preserved legacy placeholder filename.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p209-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, malformed support links, fake APRE local links, stale typo patterns, and residual Korean text | Passed |
| Scoped document-format attachment preservation script | Passed, 2 Korean source URLs preserved |
| Scoped fenced-code balance check | Passed for all scoped English files |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 15 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P209 used grep-based source-link and attachment preservation checks.
- The Korean APRE New Features legacy PDF is a `#` placeholder, so the English target can preserve the filename but cannot provide a real download URL.
- Some source-exported image URLs retain URL-encoded Korean image filenames; the visible English prose was checked separately.
