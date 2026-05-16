# S018 Tech Docker GeoServer SQuirrel

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S018 performs a semantic-unit audit for the Docker, GeoServer, and SQuirrel SQL Client technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/67. Altibase 도커 가이드__14057660.md` -> `arch/Home/Altibase Docker Guide__14647741.md`; `arch/Home/Altibase Docker Guide/**`
- `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md` -> `arch/Home/Altibase GeoServer Integration Guide__22643004.md`
- `DOCK/Home/69. Altibase를 위한 SQuirrel SQL Client Quick 가이드__12255259.md` -> `arch/Home/SQuirrel SQL Client Quick Guide for Altibase__14647622.md`; `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/**`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S018.md`
- `semantic-coverage/doc-mapping.tsv`
- The three Korean source documents and mapped English target documents listed above

Previous J/P reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S018-tech-docker-geoserver-squirrel.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow area as `S018` was already in `Progress`.
- No uncommitted project files outside the workflow area were present before S018 edits.

## Design Note

S018 adds semantic evidence only:

- Adds `semantic-coverage/matrices/S018-tech-docker-geoserver-squirrel.tsv`
- Adds `semantic-coverage/notes/S018-tech-docker-geoserver-squirrel.md`
- Updates S018 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

The product documentation structure is unchanged. No English `arch/` page required edits in this job, so `manifest.json` metadata was not changed.

The matrix records 140 semantic units: 124 `covered`, 15 `not_applicable`, and 1 `source_limitation`. It covers metadata, overview/support/legal blocks, headings, procedures, command blocks, command-output transcripts, configuration blocks, table rows, screenshots, URL-backed ZIP evidence, external references, and the known GeoServer source-link limitation. Long Docker shell/output examples are summarized by functional unit while preserving exact commands, paths, environment variables, ports, property names, URLs, version values, and output identifiers.

## Audit Summary

### Docker

The English split Docker guide preserves the Korean-source overview, version basis, support contacts, Docker concepts, Docker installation commands, `docker version` output, Docker Hub and `docker pull` workflow, Dockerfile example, `docker-entrypoint.sh`, `set_altibase.env`, `docker build`, `docker run`, data-volume examples, replication-network workflow, `isql` connection procedures, container stop/delete commands, and Docker reference links.

The matrix records command and output blocks by operational purpose rather than by every output line. Key identifiers include `Docker 19.03.2`, `Altibase 7.1.1`, `ubuntu:18.04`, `vm.swappiness`, `kernel.sem`, `ALTIBASE_HOME`, `ALTIBASE_NLS_USE`, `ALTIBASE_PORT_NO`, `DB_CHARSET`, `MODE=daemon`, `MODE=isql`, `MODE=shell`, `MODE=replication`, `MASTER_REP_PORT`, `SLAVE_REP_PORT`, `isolated_network`, `172.18.0.0/16`, `172.17.0.3`, `docker stop`, and `docker rm`.

### GeoServer

The English GeoServer guide preserves the Korean-source version scope, installation assumptions, JRE requirements, GeoServer 2.16.2 setup, required libraries, Altibase Spatial setup, `spatial_ref_sys` insert SQL, GeoServer login, Altibase data-store fields, layer registration workflow, shapefile import workflow, registered-layer verification SQL, case-sensitive table/column-name note, and OGC/OSGeo links.

The GeoServer importer plug-in ZIP is the only URL-backed document-format link in the S018 Korean sources and is preserved exactly in the English target:

- `https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/extensions/geoserver-2.16.2-importer-plugin.zip/download`

The Korean source has one known source-link limitation: its `GeoServer Documentation` label points to a Red Hat Enterprise Linux CPU governor URL. This mismatch was already recorded in `KO_EN_DOC_REVIEW_REPORT.md` and `PASS2_KO_EN_DOC_REVIEW_REPORT.md`; S018 records it as `source_limitation` and does not propagate the incorrect URL into the English target.

### SQuirrel SQL Client

The English SQuirrel split guide preserves the Korean-source overview, test environment, support contacts, installation procedure, SQuirrel 3.9.1/Java 1.8 note, 3.7.1 installer JAR link, JDBC driver registration steps, `jdbc:Altibase://<host>:<port>/<database>` URL pattern, `Altibase.jdbc.driver.AltibaseDriver`, alias/connection setup, Test button validation, database connection, Objects tab behavior, and SQL tab behavior.

Screenshot URLs differ by Confluence English export path, but the surrounding procedural units and screenshot filenames are represented.

## Attachment And Link Evidence

- URL-backed document-format links in scope: 1 Korean source link, preserved once in the English target.
- Scoped tracked links preserved in English targets include support portal, Docker concept/install/build/run/reference URLs, Docker Hub, SourceForge driver/JTS/SQuirrel URLs, GeoServer importer ZIP, `altibase_spatial_ref_sys.sql`, OGC, OSGeo, and OSGeo Korean chapter.
- English-specific manual links that point to English counterparts are retained where they do not conflict with Korean-source procedure semantics.
- The Korean GeoServer `GeoServer Documentation` label/URL mismatch is recorded as `source_limitation`.

## Self-Review

- Scope checked: S018 changed only S018 evidence files and S018 workflow status.
- Korean authority checked: all three scoped Korean source files were inspected directly.
- English target checked: all mapped English target files were inspected directly.
- Matrix checked: the S018 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `Docker`, `GeoServer`, `SQuirrel SQL Client`, `Altibase`, `isql`, `docker-entrypoint.sh`, `set_altibase.env`, `Altibase.jar`, `gt-jdbc-altibase-21-SNAPSHOT.jar`, `jts-1.14.jar`, `spatial_ref_sys`, `ASTEXT`, `SEOUL_43260`, `Altibase.jdbc.driver.AltibaseDriver`, exact port numbers, paths, and URLs are preserved.
- Product docs checked: no scoped English `arch/` Markdown page changed, so no manifest metadata refresh was required.

## Verification

Verification results after drafting and self-review:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| S018 TSV header and column-count check | Passed: 140 data rows, 15 columns each |
| S018 coverage status check | Passed: 124 `covered`, 15 `not_applicable`, 1 `source_limitation` |
| S018 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped English empty-link and macro-artifact scan, including S018 evidence file | Passed with exit code 1, meaning no matches |
| Scoped document-format attachment preservation check | Passed: 1 URL-backed source ZIP link preserved in English |
| GeoServer source-link limitation check | Passed: source mismatch recorded in S018 matrix and not propagated into English target |

## Final Decision

S018 final decision: `COMPLETE`.
