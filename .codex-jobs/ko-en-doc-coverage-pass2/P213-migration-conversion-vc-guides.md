# P213 Migration, Conversion, and VC Guides Audit

Date: 2026-05-16

## Scope

P213 audited the Korean Oracle conversion, MSSQL conversion, Altibase version migration, Migration Center, VC 2008, and VC 2010 documents against their English `arch` targets.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/38. Altibase VC 2008 개발가이드__19333567.md` | `arch/Home/Altibase VC 2008 Development Guide__19333567.md` |
| `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md` | `arch/Home/ORACLE to ALTIBASE Conversion Guide__22643038.md` |
| `DOCK/Home/46. Altibase 버전 간 마이그레이션 가이드__19333688.md` | `arch/Home/Altibase Data Migration Process Guide__22642994.md` |
| `DOCK/Home/61. Altibase VC 2010 개발가이드__19334121.md` | `arch/Home/Altibase VC 2010 Development Guide__19334121.md` |
| `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md` | `arch/Home/MSSQL to ALTIBASE Conversion Guide__22643024.md` |
| `DOCK/Home/70. Migration Center 사용자 가이드__19955861.md` | `arch/Home/Migration Center User Guide__19955861.md` |

The Korean sources were treated as authoritative. No Korean source documents were edited.

## Boundary

- Completed only P213.
- Did not enter Docker, GeoServer, SQuirrel, FAQ, attachment-wide revalidation, or final LLM consolidation jobs.
- The pre-existing pass2 `jobs.tsv` status change for P213 was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior or repository architecture changed. Documentation structure changes were limited to restoring Korean-source overview support/legal text in existing overview sections, preserving exact Korean-source document filenames in English attachment labels and legacy placeholder notes, and correcting unclear validation prose in the Altibase migration guide.

## Findings And Updates

- Restored Korean-source support route, support center, legal/disclaimer text, and intellectual-property notice in the Oracle conversion and Altibase data migration guides; restored the support route and support center in the MSSQL conversion guide.
- Added the Korean-source support portal route `Technical Knowledge > Q&A` to the VC 2008, VC 2010, and Migration Center guides.
- Preserved exact Korean-source attachment filenames in the English targets:
  - `ALTIBASE_VC_2008_개발가이드.zip`
  - `ALTIBASE_VC_2010_개발가이드.pdf`
  - `ALTIBASE_Oracle_변환_가이드.pdf`
  - `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf`
  - `ALTIBASE_MSSQL_변환가이드.pdf`
  - `Migration_Center_사용자가이드.pdf`
- Restored the Korean-source `iloader` performance-options link in the Altibase data migration guide while preserving the exact options `-array` and `-commit`.
- Corrected the Altibase data migration `.bad` file verification text so it instructs users to confirm `.bad` file sizes are 0.
- Clarified the data-load error example to point to the corresponding failed log file, `SYS_ORDERS.log`, matching the sample output.
- Removed an exported stray `1.` marker before the Oracle conversion `MigrationCenter` advantages subsection.
- Updated `manifest.json` metadata for all 6 edited English Markdown pages.

## Attachment And Link Evidence

- Scoped Korean source pages contain 6 document-format references, and all 6 exact filenames are preserved in the scoped English target set.
- The VC 2008, VC 2010, and Migration Center document-format references preserve their original `docs.altibase.com` download URLs.
- The Oracle and MSSQL conversion pages keep Korean-source legacy `#` document placeholders as filename-only notes because the Korean source does not provide downloadable URLs.
- Oracle and MSSQL conversion table counts match their Korean sources at contiguous-table level after the audit.
- Scoped checks found no empty links, Confluence macro errors, malformed support links, invalid `http://altibase_env.mk` links, stale English replacement attachment names, or the checked stray marker pattern.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p213-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 6 edited English pages |
| Scoped document-format attachment preservation script | Passed, 6 Korean source filenames preserved |
| Scoped grep/Python stale-pattern check | Passed |
| Oracle and MSSQL contiguous table-count comparison | Passed |

## Remaining Risk

- External HTTP availability was not tested; P213 used grep-based source-link and attachment preservation checks.
- The Oracle and MSSQL Korean sources contain legacy `#` placeholders for old PDF files. The English targets preserve exact filenames but cannot add download URLs that the Korean sources do not provide.
- The Migration Center English target remains a condensed text guide rather than a screenshot-by-screenshot reproduction. The procedure, field, option, and supported-object semantics were audited, and the original downloadable PDF link is preserved; broad embedded image/export-link revalidation remains in the later P223 scope.
