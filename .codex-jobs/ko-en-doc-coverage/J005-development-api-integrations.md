# J005 Development and API Integrations Review Note

Date: 2026-05-15

## Scope

J005 compared Korean DOCK development and API integration documents against their English arch counterparts. Korean source documents remained authoritative and were not edited.

## Boundary

- Updated only scoped English technical Markdown documents, `manifest.json`, the review report, and workflow job tracking.
- Preserved the existing English split-page structure for APRE, ADO.NET, WAS, Spring, iBATIS, MyBatis, and PHP documents.
- Did not enter SQL tuning, migration/conversion, Docker, GeoServer, SQuirrel, VC guide, FAQ, final attachment-wide coverage, or final LLM consolidation work.

## Documentation Structure Impact

No product behavior or architecture change was introduced. The documentation-structure change was limited to restoring Korean-source command/code examples as searchable fenced code blocks in the APRE new-features and ADO.NET development pages, while keeping the original screenshots and split-page layout.

## Main Updates

- Rechecked J005 mappings for TOMCAT, JEUS, JBoss, unixODBC, Developer Training, Precompiler, APRE Makefile, APRE new features, ADO.NET, WebSphere, Windows ODBC, Spring, iBATIS, Java, Hibernate, WebLogic, MyBatis, and PHP integration documents.
- Preserved J005 Korean source document-format attachment links in English counterparts; no missing `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` links remained.
- Restored APRE `-I`, `-D`, `-keyword`, `-parse`, and `ERR-302L` examples as text/code so LLM consumers can retrieve them without relying on embedded screenshots.
- Reformatted ADO.NET C# examples as fenced code blocks and corrected `AltibaseDataAdapter`/`AltibaseTransaction` wording.
- Removed residual Korean text from scoped English pages, especially MyBatis comments/tables, JBoss WAR creation steps, APRE notes, Java JDBC URL description, and WebLogic example timestamps.
- Corrected typo-level terms in scoped pages, including `ODBC Manager`, `JDBC driver file`, `Altibase ADO.NET`, `APRE*C/C++`, and `$ALTIBASE_HOME`.

## Verification

Verification is recorded in `KO_EN_DOC_REVIEW_REPORT.md` for this job.
