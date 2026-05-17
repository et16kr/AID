#!/usr/bin/env python3
"""Build GPTs Knowledge bundle files from the generated llm-reference corpus."""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
UPLOAD_DIR = SCRIPT_PATH.parent
ENCYCLOPEDIA = UPLOAD_DIR / "Altibase_GPT_Knowledge_Encyclopedia.md"
AUDIT_BUNDLE = UPLOAD_DIR / "Altibase_GPT_Knowledge_Audit.md"
SCRIPT_REL_PATH = "llm-reference/gpts-upload/build-gpts-knowledge-bundles.py"

FULL_INCLUDE_SOURCE_PATHS = [
    "llm-reference/README.md",
    "llm-reference/source-index.md",
    "llm-reference/00-source-classification.md",
    "llm-reference/01-installation-upgrade-platform.md",
    "llm-reference/02-architecture-storage-concepts.md",
    "llm-reference/03-operation-administration-security.md",
    "llm-reference/04-backup-recovery.md",
    "llm-reference/05-replication-ha.md",
    "llm-reference/06-monitoring-diagnostics.md",
    "llm-reference/07-troubleshooting-error-messages.md",
    "llm-reference/08-sql-performance-tuning.md",
    "llm-reference/09-development-client-api.md",
    "llm-reference/10-application-framework-integration.md",
    "llm-reference/11-migration-conversion-tools.md",
    "llm-reference/12-terminology-multilingual-preservation.md",
]

SUPPORTING_SOURCE_PATHS = [
    "llm-reference/HANDOFF.md",
    "llm-reference/LLM_REFERENCE_BUILD_REPORT.md",
    "llm-reference/coverage/README.md",
]

ENCYCLOPEDIA_SOURCE_PATHS = FULL_INCLUDE_SOURCE_PATHS + SUPPORTING_SOURCE_PATHS

AUDIT_INCLUDE_SOURCE_PATHS = [
    "llm-reference/LLM_REFERENCE_BUILD_REPORT.md",
    "llm-reference/HANDOFF.md",
    "llm-reference/coverage/README.md",
    "llm-reference/GPTS_KNOWLEDGE_PACKAGING_RECOMMENDATIONS.md",
]

REQUIRED_SOURCE_PATHS = list(dict.fromkeys(ENCYCLOPEDIA_SOURCE_PATHS + AUDIT_INCLUDE_SOURCE_PATHS))

ANSWERING_RULES = """Use Altibase_GPT_Knowledge_Encyclopedia.md as the primary source for Altibase answers.
Answer from the uploaded knowledge file before relying on general knowledge.
Do not require access to original arch, FAQE, DOCK, or faq source files.
Prefer exact commands, SQL, file paths, configuration properties, system views, error codes, class names, driver names, package filenames, URLs, and version strings from the knowledge file.
Answer in the user's language, but keep product names, SQL, commands, paths, properties, error codes, class names, filenames, URLs, and version strings exactly as written.
When source confidence matters, preserve labels such as English-only source, english_only_auxiliary, legacy_no_downloadable_url, legacy_attachment_label_only, diagram_unavailable, not_document_format, accepted_source_limitation, and accepted_english_only_auxiliary.
Do not invent content from unavailable diagrams, missing attachments, or legacy attachment labels with no downloadable URL.
If the knowledge file does not contain enough information to answer safely, say that the available Altibase GPT knowledge does not contain the required detail."""

ANSWER_ROUTING_INDEX = """Use this routing index to choose the best included document boundary inside this same encyclopedia before answering. The `llm-reference/...` paths below are included-document labels in this file and source-traceability labels for maintenance; they are not external runtime dependencies.

| User question area | Primary route inside this file | Retrieval anchors |
| --- | --- | --- |
| Installation, patch, upgrade, database creation, license setup, startup/shutdown basics, Docker, OS and platform setup | Included topic `llm-reference/01-installation-upgrade-platform.md` | install, patch, upgrade, database creation, license, `server create`, `server start`, `server stop`, `altibase.properties`, platform, Linux, AIX, HPUX, Solaris, Docker |
| Architecture, storage, checkpoints, transaction logs, WAL, Direct I/O, tablespaces, memory/disk concepts | Included topic `llm-reference/02-architecture-storage-concepts.md` | architecture, memory table, disk table, WAL, redo log, checkpoint, buffer, tablespace, Direct I/O, page, datafile |
| Operation, administration, configuration, security, users, passwords, sessions, locks, charset, capacity, startup stages | Included topic `llm-reference/03-operation-administration-security.md` | administration, operation, security, user, password, session, lock, charset, configuration, `ACCESS_LIST`, `DB_NAME`, `IPC_CHANNEL_COUNT` |
| Backup, recovery, failure response, export/import utilities, archive/noarchive, media recovery | Included topic `llm-reference/04-backup-recovery.md` | backup, recovery, failure response, archive, noarchive, media recovery, `aexport`, `iloader`, backup policy, restore |
| Replication and high availability | Included topic `llm-reference/05-replication-ha.md` | replication, HA, Sender, Receiver, replication gap, `REPLICATION_PORT_NO`, failover, active-standby |
| Monitoring, diagnostics, CPU, memory, OS evidence, locks, system views, performance views | Included topic `llm-reference/06-monitoring-diagnostics.md` | monitoring, diagnostics, CPU, memory, lock wait, system view, performance view, `V$`, `altimon`, query evidence |
| Troubleshooting and error messages | Included topic `llm-reference/07-troubleshooting-error-messages.md` | troubleshooting, error, `ERR-`, SQLCODE, SQLSTATE, cause, action, failure symptom |
| SQL, stored procedures, optimizer, indexes, partitioning, query behavior, tuning, performance | Included topic `llm-reference/08-sql-performance-tuning.md` | SQL, stored procedure, function, optimizer, index, partition, plan, statistics, performance tuning |
| Development, APRE, JDBC, ODBC, ADO.NET, PHP, SQLCLI, client APIs, drivers | Included topic `llm-reference/09-development-client-api.md` | APRE, JDBC, ODBC, ADO.NET, PHP, SQLCLI, driver, client API, connection string, `Altibase.jar` |
| WAS and framework integration | Included topic `llm-reference/10-application-framework-integration.md` | WebLogic, Tomcat, JEUS, JBoss, Spring, iBATIS, MyBatis, Hibernate, datasource, connection pool |
| Migration, conversion, compatibility tooling, Migration Center, Oracle/MS-SQL conversion, GeoServer | Included topic `llm-reference/11-migration-conversion-tools.md` | migration, conversion, Migration Center, Oracle, MS-SQL, DBMS compatibility, GeoServer, schema conversion |
| Terminology, multilingual answer preservation, exact identifier rules, source labels | Included topic `llm-reference/12-terminology-multilingual-preservation.md` | terminology, multilingual, translation, exact identifier, source label, product name, limitation label |
| Source classification, package status, accepted risks, coverage status | Included support docs `llm-reference/00-source-classification.md`, `llm-reference/HANDOFF.md`, `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`, and `llm-reference/coverage/README.md` | `Korean-source-verified`, `English-only source`, `COMPLETE_REFERENCE_PACKAGE`, coverage, answerability, risk labels |"""

EXACT_IDENTIFIER_RULES = """Preserve exact identifiers as answer-critical technical evidence. Do not translate, paraphrase, normalize, singularize, pluralize, lowercase, uppercase, or reformat these identifiers unless the source text already does so:

- Product, component, and utility names such as `Altibase`, `ALTIBASE HDB`, `APRE`, `iSQL`, `aexport`, `iloader`, `altimon`, and `Migration Center`.
- SQL statements, SQL keywords, stored procedure names, system views, performance views, meta-table names, error codes, SQLCODE values, SQLSTATE values, and error message text.
- Commands, command options, environment variables, configuration properties, file paths, directory paths, package filenames, class names, driver names, JDBC URLs, DSNs, XML element names, property names, URLs, OS names, and version strings.
- Korean filenames, URL-encoded Korean path components, Korean sample data, attachment filenames, and source labels when they identify source evidence.

When answering in another language, translate only the explanatory prose. Keep the exact identifier spelling and code formatting from this knowledge file."""

SOURCE_CONFIDENCE_RULES = """Source paths in this encyclopedia are evidence labels and maintenance traceability labels. They may be mentioned to explain provenance, but answer generation uses this uploaded knowledge file itself; source labels do not create any access requirement for `arch/`, `FAQE/`, `DOCK/`, or `faq/` at GPT answer time.

When source confidence or limitations matter, preserve the accepted labels exactly: `English-only source`, `english_only_auxiliary`, `legacy_no_downloadable_url`, `legacy_attachment_label_only`, `diagram_unavailable`, `not_document_format`, `accepted_source_limitation`, and `accepted_english_only_auxiliary`.

Apply these limitation rules:

- If a claim comes only from material labeled `English-only source` or `english_only_auxiliary`, keep that label near the claim when confidence matters and do not present it as Korean-source-verified.
- If a diagram is labeled `diagram_unavailable`, say the diagram content is unavailable in the package and do not reconstruct it.
- If an attachment is labeled `legacy_no_downloadable_url` or `legacy_attachment_label_only`, say that no downloadable URL is available in the source and do not invent a URL.
- If material is labeled `not_document_format`, do not treat it as a preserved downloadable document-format attachment.
- If the knowledge file lacks the required detail, say that the available Altibase GPT knowledge does not contain the required detail; do not fill gaps from assumptions."""


def repo_path(rel_path: str) -> Path:
    return REPO_ROOT / rel_path


def read_source(rel_path: str) -> str:
    return repo_path(rel_path).read_text(encoding="utf-8")


def check_required_sources() -> None:
    missing = [rel_path for rel_path in REQUIRED_SOURCE_PATHS if not repo_path(rel_path).is_file()]
    if missing:
        missing_list = "\n".join(f"- {rel_path}" for rel_path in missing)
        raise FileNotFoundError(f"Missing required source file(s):\n{missing_list}")


def append_included_document(lines: list[str], rel_path: str) -> None:
    content = read_source(rel_path).rstrip("\n")
    lines.extend(
        [
            f"BEGIN INCLUDED DOCUMENT: {rel_path}",
            content,
            f"END INCLUDED DOCUMENT: {rel_path}",
            "",
        ]
    )


def demote_markdown_headings(markdown: str, levels: int) -> str:
    def replace(match: re.Match[str]) -> str:
        marker = "#" * min(6, len(match.group(1)) + levels)
        return f"{marker}{match.group(2)}"

    return re.sub(r"^(#{1,5})(\s)", replace, markdown, flags=re.MULTILINE)


def extract_section(content: str, heading: str, *, demote_levels: int = 0) -> str:
    pattern = re.compile(rf"^{re.escape(heading)}\n.*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(content)
    if not match:
        return f"{heading}\n\nSection not found in source report."
    section = match.group(0).rstrip()
    if demote_levels:
        section = demote_markdown_headings(section, demote_levels)
    return section


def build_front_matter(build_date: str) -> list[str]:
    return [
        "---",
        "generated_file: true",
        f"generator: {SCRIPT_REL_PATH}",
        f"build_date: {build_date}",
        "source_boundary: generated llm-reference corpus only; original source trees arch/, FAQE/, DOCK/, and faq/ are evidence labels and are not GPT answer-time dependencies",
        "gpts_purpose: self-contained Altibase GPTs Knowledge upload file for customer and support answers",
        "package_status: COMPLETE_REFERENCE_PACKAGE",
        "included_document_count: 18",
        "topic_document_count: 12",
        "answer_scope: answer from this file before general knowledge; original source trees are not required",
        "routing_index: top-of-file table maps common Altibase question areas to included llm-reference document boundaries",
        "exact_identifier_policy: preserve product names, SQL, commands, paths, properties, system views, error codes, class names, driver names, package filenames, URLs, and version strings exactly",
        "limitation_label_policy: preserve accepted limitation labels and do not invent unavailable diagrams, missing attachments, synthetic URLs, or absent source details",
        "---",
        "",
    ]


def build_audit_front_matter(build_date: str) -> list[str]:
    return [
        "---",
        "generated_file: true",
        f"generator: {SCRIPT_REL_PATH}",
        f"build_date: {build_date}",
        "source_boundary: generated llm-reference audit reports and coverage summary only; original source trees are evidence labels and are not GPT answer-time dependencies",
        "gpts_purpose: optional internal audit and technical support validation file",
        "required_for_customer_answers: false",
        "customer_required_file: llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md",
        "upload_policy: customer-facing GPTs require only the encyclopedia; this audit bundle is an optional second file for internal review",
        "included_document_count: 4",
        "raw_tsv_ledgers_included: false",
        "---",
        "",
    ]


def build_encyclopedia() -> str:
    build_date = datetime.now(timezone.utc).date().isoformat()
    lines: list[str] = []
    lines.extend(build_front_matter(build_date))
    lines.extend(
        [
            "# Altibase GPT Knowledge Encyclopedia",
            "",
            "Generated by `llm-reference/gpts-upload/build-gpts-knowledge-bundles.py` from the current generated `llm-reference/` corpus.",
            "",
            "This file is the required customer-facing GPTs Knowledge upload artifact for Altibase. Original source trees `arch/`, `FAQE/`, `DOCK/`, and `faq/` are not required at GPT answer time; source paths retained inside this file are evidence labels and maintenance traceability only.",
            "",
            "## How To Use This Knowledge File",
            "",
            "Use this encyclopedia as a self-contained `COMPLETE_REFERENCE_PACKAGE` for Altibase customer and support answers. It includes `llm-reference/README.md`, `source-index.md`, `00-source-classification.md`, all 12 topic documents in full, GPT usage guidance from `HANDOFF.md`, final validation evidence from `LLM_REFERENCE_BUILD_REPORT.md`, and accepted-risk and attachment-limitation guidance from `coverage/README.md`.",
            "",
            "The included topic corpus covers installation, upgrade, platform, architecture, storage, operation, administration, security, backup, recovery, replication, high availability, monitoring, diagnostics, troubleshooting, error messages, SQL, performance tuning, development, client API, application framework integration, migration, conversion tools, terminology, and multilingual preservation.",
            "",
            "## Answering Rules For GPTs",
            "",
            ANSWERING_RULES,
            "",
            "### Answer Routing Index",
            "",
            ANSWER_ROUTING_INDEX,
            "",
            "### Exact Identifier Preservation Rules",
            "",
            EXACT_IDENTIFIER_RULES,
            "",
            "### Source Confidence And Limitation Label Rules",
            "",
            SOURCE_CONFIDENCE_RULES,
            "",
            "## Source Package Status",
            "",
            "Final source package decision: `COMPLETE_REFERENCE_PACKAGE`.",
            "",
            "The generated `llm-reference/` corpus is the source boundary for this GPTs upload file. The original source trees are not GPT answer-time dependencies. Accepted limitation labels must remain visible when source confidence matters: `English-only source`, `english_only_auxiliary`, `legacy_no_downloadable_url`, `legacy_attachment_label_only`, `diagram_unavailable`, `not_document_format`, `accepted_source_limitation`, and `accepted_english_only_auxiliary`.",
            "",
            "Do not invent unavailable diagrams, missing attachments, synthetic URLs, or source content that is not present in this knowledge file.",
            "",
        ]
    )

    for rel_path in ENCYCLOPEDIA_SOURCE_PATHS:
        append_included_document(lines, rel_path)

    return "\n".join(lines).rstrip() + "\n"


def build_audit_bundle() -> str:
    build_date = datetime.now(timezone.utc).date().isoformat()
    build_report = read_source("llm-reference/LLM_REFERENCE_BUILD_REPORT.md")
    coverage_readme = read_source("llm-reference/coverage/README.md")

    lines: list[str] = []
    lines.extend(build_audit_front_matter(build_date))
    lines.extend(
        [
            "# Altibase GPT Knowledge Audit",
            "",
            "Generated by `llm-reference/gpts-upload/build-gpts-knowledge-bundles.py` from the current generated `llm-reference/` audit and packaging reports.",
            "",
            "This optional audit bundle is for internal validation, technical support traceability, and upload review. It is not required for normal customer answers. A customer-facing Altibase GPT requires only `Altibase_GPT_Knowledge_Encyclopedia.md` as the Altibase reference file.",
            "",
            "The original source trees `arch/`, `FAQE/`, `DOCK/`, and `faq/` are not GPT answer-time dependencies. Source paths retained in the included reports are evidence labels and maintenance traceability only.",
            "",
            "## Customer Upload Decision",
            "",
            "- Required customer-facing Altibase reference file: `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md`.",
            "- Optional internal audit file: `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md`.",
            "- Customer-facing upload requires no more than 1 Altibase reference file.",
            "- Internal upload requires no more than 2 Altibase reference files.",
            "- Do not describe this audit bundle as required for customer answers or as a runtime dependency.",
            "",
            "## Audit Summary",
            "",
            "Final source package decision: `COMPLETE_REFERENCE_PACKAGE`.",
            "",
            "This audit bundle includes full validation and packaging evidence, plus compact summary sections for reviewer orientation. It deliberately does not include full raw TSV ledgers; the repository copy of `llm-reference/coverage/` remains the row-level audit source.",
            "",
            "### Coverage Status Distributions",
            "",
            extract_section(build_report, "## Coverage ledger results", demote_levels=2),
            "",
            "### Answerability Status Distributions",
            "",
            extract_section(build_report, "## Answerability and risk results", demote_levels=2),
            "",
            "### Attachment And Diagram Preservation Summary",
            "",
            extract_section(build_report, "## Attachment and diagram preservation", demote_levels=2),
            "",
            "### Source Inventory And Source-To-Topic Reconciliation Summary",
            "",
            extract_section(coverage_readme, "## R025 source and semantic-unit coverage reconciliation", demote_levels=2),
            "",
            extract_section(coverage_readme, "## R026 source-derived answerability backtest", demote_levels=2),
            "",
            "### Attachment Register Reconciliation Summary",
            "",
            extract_section(coverage_readme, "## R023 attachment, diagram, and external reference register", demote_levels=2),
            "",
            "## Included Audit Documents",
            "",
            "The following source documents are included in full for internal review. They are evidence and configuration guidance, not additional required customer-answer content.",
            "",
        ]
    )

    for rel_path in AUDIT_INCLUDE_SOURCE_PATHS:
        append_included_document(lines, rel_path)

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    try:
        check_required_sources()
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        encyclopedia_content = build_encyclopedia()
        audit_content = build_audit_bundle()
        ENCYCLOPEDIA.write_text(encyclopedia_content, encoding="utf-8", newline="\n")
        AUDIT_BUNDLE.write_text(audit_content, encoding="utf-8", newline="\n")
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    for output_path in (ENCYCLOPEDIA, AUDIT_BUNDLE):
        size = output_path.stat().st_size
        print(f"Wrote {output_path.relative_to(REPO_ROOT)} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
