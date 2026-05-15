# P206 CPU and Memory Analysis Audit

Date: 2026-05-16

## Scope

P206 audited the Korean CPU overload and memory usage increase analysis guides against their English `arch` targets.

| Korean source | English targets |
| --- | --- |
| `DOCK/Home/62. Altibase CPU 과부하 현상에 대한 분석가이드__11698396.md` | `arch/Home/Altibase CPU Overload Analysis Guide__14647581.md`; `arch/Home/Altibase CPU Overload Analysis Guide/**` |
| `DOCK/Home/63. Altibase Memory 사용량 증가 분석가이드__11698518.md` | `arch/Home/Altibase Memory Usage Increase Analysis Guide__14647388.md`; `arch/Home/Altibase Memory Usage Increase Analysis Guide/**` |

The Korean source was treated as authoritative. No Korean source documents were edited.

## Design Note

This job does not change product behavior, architecture, or the documentation hierarchy. The existing English split-page structure was preserved. The job updates English content inside existing pages, fixes Korean-source semantic drift and export-format damage, and refreshes `manifest.json` metadata for the edited pages.

## Findings And Updates

- Corrected the CPU routine checklist so the collection table follows the Korean-source order, the `V$SYSSTAT` SQL is searchable, the shell output is a fenced code block, and the sample history table is in chronological order.
- Clarified CPU analysis procedure wording for normal transaction growth, newly added services, long-running query detection, `V$PLANTEXT`, optimizer statistics collection, and data-growth/query-plan causes.
- Corrected CPU query-processing explanations for PVO cost, repeated `PREPARE`, `V$SESSTAT`/`V$SESSION`, memory-table index behavior, Buffered I/O vs Direct I/O, and the impossibility of low CPU use with high query throughput.
- Corrected CPU "other cases" wording for `NLS_USE`, `Dedicated Thread`, `MULTIPLEXING_POLL_TIMEOUT`, OS environment variables, repeated connect/disconnect, `QUERY_PROF_FLAG`, `*.prof`, and `altiProfile`.
- Corrected the CPU summary numbering and wording for data collection, old-version statistics collection, `select-poll`, repeated DB connections, and the OS utility reference.
- Restored missing Korean-source memory overview details in the English parent page, including reference documents, the `Altibase version 7 or later` test basis, Linux OS version, support contact, and the Korean-source PDF attachment.
- Corrected the memory routine page for OS memory/swap checks, Linux available-memory calculations, routine collection wording, `V$MEMSTAT`, and the `V$MEMSTAT` table. The bogus exported `Internal Module | Description` table row was removed.
- Corrected the memory cause/resolution page for memory table compaction, restart behavior, query object close handling, similar SQL patterns, MVCC copy semantics, `LIMIT`, `V$MEMGC`, `ADD_OID_CNT`, `GC_OID_CNT`, and GC aging delay cleanup.

## Attachment And Link Evidence

- The CPU guide Korean-source PDF attachment URL is preserved in the English target set.
- The memory guide Korean-source PDF attachment URL is preserved in the English target set.
- Scoped grep found no residual Korean text in the scoped English target set and no empty links, Confluence macro error markers, malformed support links, or stale typo patterns checked for this job.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p206-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for residual Korean text, empty links, Confluence macro errors, malformed support links, and stale typo patterns | Passed, no matches |
| Scoped attachment preservation script | Passed, 2 Korean source document-format URLs preserved |
| Scoped fenced-code balance check | Passed for all 9 scoped English files |
| Scoped table pipe-count check | Passed for edited CPU and memory routine tables |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 9 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P206 used grep-based source-link and attachment preservation checks.
- The Korean CPU source has internally inconsistent optimizer-statistics version wording: one section names `6.1.1.6.1` or later, while the summary names `6.1.1` or earlier. The English guide preserves the scoped meanings in their respective sections.
- The Korean memory routine checklist pairs a transaction-throughput row with a `v$memstat` SQL example. The English guide clarifies the row around the SQL example and `V$MEMSTAT` because the scoped page is the memory usage guide.
