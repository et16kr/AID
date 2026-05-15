# J006 SQL, Tuning, Migration, Conversion, and Tools Review Note

Date: 2026-05-15

## Scope

J006 compared Korean DOCK documents for the Altibase Development Guide, SQL tuning, Oracle and MSSQL conversion, Altibase version-to-version migration, Docker, GeoServer, SQuirrel SQL Client, VC 2008 and VC 2010 guides, and Migration Center against their English arch counterparts. Korean source documents remained authoritative and were not edited.

## Boundary

- Updated only scoped English technical Markdown documents, `manifest.json`, the review report, and workflow job tracking.
- Preserved the existing English split-page structure for the Development Guide, Docker Guide, and SQuirrel SQL Client guide.
- Did not enter FAQ, final attachment-wide coverage, or final LLM consolidation work.

## Documentation Structure Impact

No product behavior or architecture change was introduced. The documentation-structure change was limited to making exported command/output blocks searchable and readable, correcting residual Korean text in English pages, and recording Korean-source legacy document placeholders where the Korean page has no downloadable URL.

## Main Updates

- Rechecked J006 mappings for Development Guide, SQL Tuning, VC 2008, Altibase/Oracle Comparison, Oracle conversion, Altibase data migration, VC 2010, MSSQL conversion, Docker, GeoServer, SQuirrel SQL Client, and Migration Center documents.
- Preserved J006 Korean source document-format attachment links in English counterparts; no missing URL-backed `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` links remained.
- Restored missing Oracle conversion support/manual references and recorded legacy Korean-source placeholder PDF labels without creating broken download URLs.
- Corrected residual Korean in Oracle conversion, MSSQL conversion, data migration, GeoServer, and Development Guide pages.
- Repaired flattened Docker command and output blocks for `docker build`, `docker run`, `docker network`, `docker ps`, and `isql` examples.

## Verification

Verification is recorded in `KO_EN_DOC_REVIEW_REPORT.md` for this job.
