# P214 Docker, GeoServer, and SQuirrel Tools Audit

Date: 2026-05-16

## Scope

P214 audited the Korean Docker, GeoServer, and SQuirrel SQL Client documents against their English `arch` targets.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/67. Altibase 도커 가이드__14057660.md` | `arch/Home/Altibase Docker Guide__14647741.md`; `arch/Home/Altibase Docker Guide/1. Overview of Docker__14647745.md`; `arch/Home/Altibase Docker Guide/2. Docker Installation__14647748.md`; `arch/Home/Altibase Docker Guide/3. Altibase Docker Image__14647754.md`; `arch/Home/Altibase Docker Guide/4. Creating Altibase Service Container__14647760.md`; `arch/Home/Altibase Docker Guide/5. Stopping_Deleting Altibase Service Container__14909445.md` |
| `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md` | `arch/Home/Altibase GeoServer Integration Guide__22643004.md` |
| `DOCK/Home/69. Altibase를 위한 SQuirrel SQL Client Quick 가이드__12255259.md` | `arch/Home/SQuirrel SQL Client Quick Guide for Altibase__14647622.md`; `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/1. SQuirrel SQL Client Installation__14647626.md`; `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/2. Altibase JDBC Driver Registeration__14647628.md`; `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/3. Integration with Altibase__14647630.md` |

The Korean sources were treated as authoritative. No Korean source documents were edited.

## Boundary

- Completed only P214.
- Did not enter migration/conversion, FAQ, attachment-wide revalidation, embedded-image-wide revalidation, or final LLM consolidation jobs.
- The pre-existing pass2 `jobs.tsv` status change for P214 was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior, architecture, or documentation hierarchy changed. Documentation structure changes were limited to restoring Korean-source overview/support/legal text in existing overview pages, preserving exact Korean-source tool/source URLs where the English pages had drifted, and repairing exported command or table text inside existing English pages.

## Findings And Updates

- Restored Korean-source support route, support center, disclaimer, release-timing notice, and intellectual-property notice in the Docker, GeoServer, and SQuirrel overview pages.
- Restored exact Korean-source Docker reference URLs for `https://www.docker.com/resources/what-container`, `https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#container-and-layers`, and `https://docs.docker.com/install/`.
- Corrected remaining Docker export damage in the `docker version` output, `docker-entrypoint.sh` example, and `set_altibase.env` example so the commands and environment-variable lines are not merged.
- Corrected Docker service-container prose for data volumes, Docker network creation, network inspection, and additional-node replication option descriptions.
- Restored the Korean-source SQuirrel note that version `3.9.1` requires Java `1.8` or later and that the guide therefore links version `3.7.1`.
- Corrected SQuirrel exported wording and structure for the JDBC driver file selection step and the `2.1 How to register` table-of-contents line.
- Corrected the GeoServer layer verification note so it preserves the Altibase product name and clearly states that table and column names are case-sensitive.
- Updated `manifest.json` metadata for all 9 edited English Markdown pages.

## Attachment And Link Evidence

- The scoped Korean source pages contain one URL-backed document-format ZIP link, the GeoServer importer plug-in ZIP, and it is preserved exactly in the English target.
- A scoped tracked-link check confirmed that Korean-source support, Docker, SourceForge, GeoServer importer ZIP, SQuirrel installer JAR, Docker Hub, and Docker command-reference URLs are preserved in the scoped English target set.
- English-specific manual links that point to English counterparts were retained where they do not conflict with Korean-source meaning.
- Scoped grep found no remaining `versionClient`, `bash. ./`, `occured.export`, `Create Docker network Docker network`, `created work`, `data column`, `Atlibase`, `drive file`, malformed SQuirrel TOC marker, or malformed support `/en/` link patterns in the scoped English target set.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p214-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 9 edited English pages |
| Scoped tracked-link preservation script | Passed, 16 tracked Korean-source URLs preserved |
| Scoped stale-pattern grep | Passed |

## Remaining Risk

- External HTTP availability was not tested; P214 used grep-based source-link and attachment preservation checks.
- Broad embedded-image URL revalidation was not part of P214. The scoped text audit preserved existing image references and left broader image/export checks for later workflow scope.
- The Korean GeoServer source still contains a mislabeled `GeoServer Documentation` link that points to a Red Hat CPU governor page. As in the first pass, that mismatched Korean source link was not propagated into the English target.
