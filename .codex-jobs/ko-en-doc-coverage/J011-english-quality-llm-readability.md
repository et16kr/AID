# J011 English Quality and LLM-Readability Review Note

Date: 2026-05-15

## Scope

J011 reviewed updated English documents from the J002-J010 coverage work for technical English quality, terminology consistency, LLM searchability, and preservation of non-translatable identifiers. This job did not re-compare full Korean-English content coverage, delete Korean documents, move source documents, or perform broad rewrites that would weaken source traceability.

## Design Note

This pass changes wording and local Markdown structure only. It keeps source URLs and original file paths intact, including source-export typos inside `docs.altibase.com` URLs and image paths, because those strings preserve traceability to the original pages. Search-facing titles, section headings, prose, and nearby table-of-contents links were improved where the meaning was clear from the corresponding Korean source or from the existing English context.

Non-translatable identifiers were preserved or made more explicit with code formatting, including `SYS_*`, `V$*`, `$ALTIBASE_HOME`, `$DOMAIN_HOME`, `TIMED_STATISTICS`, `DROP TABLESPACE`, `Altibase.jar`, `Altibase5.jar`, `altiProfile`, and JDBC/ODBC command terms.

## Documents Updated

- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/1. Main meta table and performance views related to session, query, transaction, lock, service thread, and memory DB GC__14058240.md`
- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/4. Main Metal Tables and Performance Views Related to Replication__14058248.md`
- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/5. Whether Users can Access the Tablespace, System_Object Privileges, PSM, View related Meta Tables and Peformance Views__14058250.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/2. Starting and Shutdown the WebLogic Server Instance__14058329.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/How to make a basic Makefile__15630382.md`
- `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md`
- `arch/Home/JAVA Developer's Guide__16875544.md`
- `arch/Home/Altibase GeoServer Integration Guide__22643004.md`
- `FAQE/Home/08. Monitoring/How to log queries performed in Altibase (altiProfile)__22642959.md`
- `FAQE/Home/02. Operation and Management/What is MEM_MAX_DB_SIZE__16875991.md`
- `manifest.json`

## Review Result

- Improved monitoring guide section titles, local TOC links, and prose for meta tables and performance views.
- Restored or clarified exact identifiers such as `SYS_USERS_`, `SYS_TABLES_`, `SYS_REPL_HOSTS_`, and `V$REPRECEIVER_TRANSTBL`.
- Clarified WebLogic start/shutdown and JDBC driver setup wording while preserving command names, paths, and jar names.
- Fixed obvious English typos and awkward exported phrasing in APRE, Java, GeoServer, altiProfile, and `MEM_MAX_DB_SIZE` pages.
- Split several image-heavy GeoServer steps onto separate lines so the procedural text is searchable and not hidden in a long image line.

## Remaining Risk

This job was a scoped quality pass over changed and high-risk English documents, not a complete sentence-level rewrite of every English page. Source URLs and image paths that contain legacy source-page misspellings, such as `Registeration` or `Peformance`, were intentionally preserved.

## Verification

- `python3 -m json.tool manifest.json > /tmp/aid_manifest_j011.json` passed.
- `git diff --check` passed.
- Changed-file consistency check passed for 10 English Markdown files:
  - `manifest.json` metadata matched file length, word count, and frontmatter title.
  - No removed URLs were detected compared with `HEAD`.
  - No Korean text remained in the changed English files.
  - No empty Markdown links were detected.
  - Scoped stale-pattern checks for fixed wording passed.
- Document counts remained unchanged:
  - `DOCK`: 51 Markdown files
  - `faq`: 115 Markdown files
  - `arch`: 181 Markdown files
  - `FAQE`: 241 Markdown files
  - `DOCK/Home`: 51 Markdown files
  - `arch/Home`: 181 Markdown files
  - `faq/Home`: 115 Markdown files
  - `FAQE/Home`: 241 Markdown files
