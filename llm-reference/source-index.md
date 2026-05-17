# Source Index

## Source paths

This scaffold uses these workflow and evidence paths:

- `.codex-jobs/llm-reference-consolidation/jobs.tsv`
- `.codex-jobs/llm-reference-consolidation/workflow-requirements.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `source-stabilization/source-classification.tsv`
- `source-stabilization/legacy-attachments.tsv`
- `source-stabilization/url-backed-attachments.tsv`

The source corpus to be indexed by R003 is:

- `arch/Home/**/*.md`
- `FAQE/Home/**/*.md`

## Source coverage notes

R002 created this index scaffold but did not claim per-source coverage. R003 populated exactly one `source-inventory.tsv` row and exactly one `source-to-topic-map.tsv` row for every Markdown source under `arch/Home` and `FAQE/Home`.

The Phase 2 validation report recorded these source counts:

| Source root | Markdown count |
| --- | ---: |
| `arch/Home` | 181 |
| `FAQE/Home` | 241 |

R003 inventory result:

| Ledger | Data rows | Expected source count | Status |
| --- | ---: | ---: | --- |
| `llm-reference/coverage/source-inventory.tsv` | 422 | 422 | Complete |
| `llm-reference/coverage/source-to-topic-map.tsv` | 422 | 422 | Complete |

R003 mapped all source files to a primary topic and owner job. Detailed answer-affecting semantic-unit extraction remains with the owning topic jobs listed below.

## Scope and audience

Use this file as the package-level route map. It lists topic destinations and job ownership so later jobs can add detailed source rows without changing the expected package shape.

## Key facts

- `arch/Home` technical guides and Korean-core `FAQE/Home` FAQ material are primary consolidated answer sources when classified as Korean-source-verified.
- `FAQE/Home/ALTIBASE HDB*`, `FAQE/Home/Altibase Error Messages/**`, and `FAQE/Home/Altibase Error Messages__6979655.md` are English-only auxiliary sources unless later audited differently.
- A source may be mapped to one primary topic and any needed secondary topics.
- Repeated content may be covered by a canonical duplicate target only when the coverage row names that target.

## Procedures

1. Add each source file to `coverage/source-inventory.tsv`.
2. Add each source file to `coverage/source-to-topic-map.tsv`.
3. Use the job ownership table below to assign `owner_job`.
4. Use `00-source-classification.md` to assign `source_class`.
5. Add semantic-unit rows in `coverage/semantic-unit-coverage.tsv` from the job that owns the relevant source units.

## SQL, commands, and configuration

R003 should use the same source boundary command:

```bash
find arch/Home FAQE/Home -type f -name '*.md' | sort
```

Final reconciliation should compare the source count with the inventory row count.

R025 reconciliation confirmed that the source tree count is 422 and that `source-inventory.tsv` and `source-to-topic-map.tsv` each contain exactly 422 unique source rows, matching every Markdown file under `arch/Home` and `FAQE/Home`.

## Validation and troubleshooting

If a file matches multiple topics, choose the primary topic by the dominant answer use and place other topics in `secondary_topics`. Do not drop a source because it looks repetitive; use `covered_by_canonical_duplicate` at semantic-unit level when appropriate.

## Version-specific notes

Topic routing must preserve version and platform differences. Do not route a source to a more general topic if that would hide a distinct version, OS, restart, license, backup mode, replication mode, or failure-condition variant.

## Related errors

Error-specific routing:

- Korean-source-verified FAQ errors and technical guide errors: `07-troubleshooting-error-messages.md`, owner job `R013`.
- English-only error catalog and troubleshooting auxiliary sources: `07-troubleshooting-error-messages.md`, owner job `R014` or `R021` depending on the path listed in `workflow-requirements.md`.

## Attachments and external references

Attachment routing belongs in `coverage/attachment-diagram-register.tsv`. Source rows should still note attachment count. R023 owns exhaustive attachment, diagram, and external-reference registration.

## Topic destinations

| Topic document | Primary scope | Owning jobs |
| --- | --- | --- |
| `01-installation-upgrade-platform.md` | Installation, patch, upgrade, database creation, platform setup, Docker | `R004`, `R005` |
| `02-architecture-storage-concepts.md` | Architecture, memory and disk DBMS concepts, WAL, checkpoints, disk configuration | `R006` |
| `03-operation-administration-security.md` | Configuration, startup, shutdown, capacity, OS utilities, administration, security, sessions, charset, JOBs | `R007`, `R008` |
| `04-backup-recovery.md` | Backup policy, cold and online backup, recovery, failure response, aexport, iloader | `R009` |
| `05-replication-ha.md` | Replication, HA, constraints, conflicts, gap monitoring, GIVE-UP | `R010` |
| `06-monitoring-diagnostics.md` | Monitoring SQL, system views, CPU, memory, OS evidence, logs, dumps | `R011`, `R012` |
| `07-troubleshooting-error-messages.md` | Error messages and troubleshooting, including English-only error catalog labels | `R013`, `R014` |
| `08-sql-performance-tuning.md` | SQL, stored procedures, query behavior, optimizer, indexes, partitioning, HPT | `R015`, `R016` |
| `09-development-client-api.md` | APRE, SES, precompiler, C/C++, Java, JDBC, ODBC, ADO.NET, PHP | `R017`, `R018` |
| `10-application-framework-integration.md` | Tomcat, JEUS, JBoss, WebLogic, WebSphere, Spring, iBATIS, MyBatis, Hibernate | `R019` |
| `11-migration-conversion-tools.md` | Altibase migration, Oracle and MSSQL conversion, Migration Center, VC guides, GeoServer, SQuirrel, utilities | `R020` |
| `12-terminology-multilingual-preservation.md` | Product terms, exact identifiers, translation boundaries, multilingual answer stability | `R024` |

## Job-to-source ownership

| Job | Source ownership summary |
| --- | --- |
| `R001` | Phase gate evidence only; no `arch/Home` or `FAQE/Home` semantic units |
| `R002` | Scaffold and ledger headers only; no `arch/Home` or `FAQE/Home` semantic units |
| `R003` | All `arch/Home` and `FAQE/Home` source inventory and source-to-topic map rows |
| `R004` | Installation, patch, upgrade, database creation, quick start, installation troubleshooting, installation FAQ sources |
| `R005` | Linux, Solaris, HPUX, AIX, platform prerequisite, and Docker sources |
| `R006` | Architecture, storage, disk, Direct I/O, disk contention, and general concept sources |
| `R007` | Configuration, startup, shutdown, capacity, OS utility, and memory management sources |
| `R008` | Operation and management FAQ sources plus Korean-source-verified operational rows |
| `R009` | Backup, recovery, failure response, aexport, iloader, and validation sources |
| `R010` | Replication, HA, constraints, conflict, gap, GIVE-UP, and replication FAQ sources |
| `R011` | Monitoring query and monitoring FAQ sources |
| `R012` | CPU, memory, OS evidence, dump, log, and diagnostic decision sources |
| `R013` | Korean-source-verified troubleshooting and error-message sources |
| `R014` | English-only error catalog and troubleshooting auxiliary sources |
| `R015` | SQL, stored procedure, query behavior, examples, limits, and FAQ sources |
| `R016` | Tuning, optimizer, index, partitioning, HPT, and performance diagnostic sources |
| `R017` | APRE, SES, precompiler, C/C++, Makefile, and sample-code sources |
| `R018` | Java, JDBC, ODBC, unixODBC, ADO.NET, PHP, driver, connection, and API FAQ sources |
| `R019` | WAS and framework integration sources |
| `R020` | Migration, conversion, Migration Center, VC, GeoServer, SQuirrel, and utility sources |
| `R021` | English-only architecture, administration, performance, replication, and troubleshooting auxiliary sources |
| `R022` | FAQ reconciliation across all Korean-source-verified FAQE sources |
| `R023` | Attachments, diagrams, and external references across all sources |
| `R024` | Terminology and multilingual preservation across completed topic documents |
| `R025` | Coverage reconciliation across source inventory, semantic units, and topics |
| `R026` | Source-derived answerability backtest rows and topic fixes |
| `R027` | Cross-reference, label, link, terminology, and unsupported-claim review |
| `R028` | Final validation, build report, and handoff |

## Terminology

- `primary_topic`: The main topic document where answerable content from a source should be consolidated.
- `secondary_topics`: Other topic documents that need cross-reference or partial coverage from the same source.
- `owner_job`: The R-series job responsible for extracting or reconciling the source content.
- `mapped`: The source has a primary topic and owner job.
- `mapped_with_risk`: The source has a primary topic and owner job, but a known limitation or classification risk remains.
