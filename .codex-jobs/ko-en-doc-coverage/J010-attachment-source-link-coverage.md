# J010 Attachment and Source-Link Coverage Review Note

Date: 2026-05-15

## Scope

J010 rechecked document-format attachment links and important source/reference links across all Korean technical documents in `DOCK/Home` and all Korean FAQ documents in `faq/Home` against their English counterparts in `arch/Home` and the Korean-source core `FAQE/Home` categories. Korean source documents remained authoritative and were not edited.

## Boundary

- Updated only scoped English Markdown documents, `manifest.json`, the review report, and workflow job tracking.
- Preserved the existing English document hierarchy and split-page structure.
- Did not enter broad English-quality rewriting, final workflow validation, or LLM consolidation work.

## Documentation Structure Impact

No product behavior, architecture, or documentation hierarchy changed. The documentation changes were limited to restoring or correcting source/reference links and preserving Korean-source link coverage in the existing English pages.

## Main Updates

- Rechecked 49 URL-backed document-format links: 41 Korean technical `docs.altibase.com/download/attachments` links, 1 Korean technical GeoServer importer ZIP link, and 7 Korean FAQ attachment links. No missing English coverage remained.
- Restored missing GeoServer source links for OpenJDK, Oracle JRE, GeoServer downloads, the Altibase spatial driver, JTS, the coordinate-system reference SQL script, and Open Geospatial references.
- Corrected a malformed IBM Installation Manager source URL in the WebSphere integration guide.
- Corrected English support/manual/product links in APRE Makefile, Windows ODBC, failure-response references, replication DDL FAQ, Oracle conversion, and Migration Center pages.
- Added the missing 64-bit client development tool download note in the APRE Makefile page where the Korean source referenced the same product-download source.

## Review Notes

- The Korean GeoServer page contains a link labeled `GeoServer Documentation` whose URL points to a Red Hat Enterprise Linux CPU governor page. This was treated as a source-link mismatch in the Korean source and was not propagated into the English GeoServer reference list.
- Six legacy Korean technical document labels still use `#` instead of a downloadable URL. They remain documented as placeholders and are not counted as missing URL-backed attachments.

## Verification

Verification is recorded in `KO_EN_DOC_REVIEW_REPORT.md` for this job.
