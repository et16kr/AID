#!/usr/bin/env python3
"""Validate Altibase GPTs Knowledge upload artifacts.

Use --mode preflight before bundles exist, --mode full after bundle generation,
and --mode final as the automated gate before human review starts.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
LLM_REF = REPO_ROOT / "llm-reference"
UPLOAD_DIR = LLM_REF / "gpts-upload"
ENCYCLOPEDIA = UPLOAD_DIR / "Altibase_GPT_Knowledge_Encyclopedia.md"
AUDIT_BUNDLE = UPLOAD_DIR / "Altibase_GPT_Knowledge_Audit.md"
UPLOAD_MANIFEST = UPLOAD_DIR / "UPLOAD_MANIFEST.tsv"
GPTS_INSTRUCTIONS = UPLOAD_DIR / "GPTS_INSTRUCTIONS.txt"
READINESS_REPORT = UPLOAD_DIR / "GPTS_READINESS_REPORT.md"
HUMAN_REVIEW_CHECKLIST = UPLOAD_DIR / "HUMAN_REVIEW_CHECKLIST.html"

MAX_GPTS_FILE_BYTES = 512 * 1024 * 1024
ROUGH_MAX_TEXT_TOKENS = 2_000_000
ROUGH_CHARS_PER_TOKEN = 4

CORE_FULL_INCLUDE_PATHS = [
    "llm-reference/README.md",
    "llm-reference/source-index.md",
    "llm-reference/00-source-classification.md",
]

TOPIC_PATHS = [
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
    "llm-reference/GPTS_KNOWLEDGE_PACKAGING_RECOMMENDATIONS.md",
]

REQUIRED_SOURCE_PATHS = CORE_FULL_INCLUDE_PATHS + TOPIC_PATHS + SUPPORTING_SOURCE_PATHS
FULL_TEXT_REQUIRED_PATHS = CORE_FULL_INCLUDE_PATHS + TOPIC_PATHS

ARTIFACT_PATTERNS = [
    r"\[\]\(",
    r"Error rendering macro",
    r"Unknown macro",
    r"unknown-macro",
    r"\]\(#\)",
]

REQUIRED_LIMITATION_LABELS = [
    "English-only source",
    "english_only_auxiliary",
    "legacy_no_downloadable_url",
    "legacy_attachment_label_only",
    "diagram_unavailable",
    "not_document_format",
    "accepted_source_limitation",
    "accepted_english_only_auxiliary",
]

ROUTING_TERMS = [
    "installation",
    "platform",
    "architecture",
    "administration",
    "backup",
    "replication",
    "monitoring",
    "troubleshooting",
    "sql",
    "performance",
    "development",
    "framework",
    "migration",
    "terminology",
]

REQUIRED_TOP_MATTER = [
    "# Altibase GPT Knowledge Encyclopedia",
    "## How To Use This Knowledge File",
    "## Answering Rules For GPTs",
    "## Source Package Status",
    "COMPLETE_REFERENCE_PACKAGE",
]

NO_RUNTIME_DEPENDENCY_PATTERNS = [
    r"original source (?:trees|files) are not (?:GPT )?(?:answer-time )?(?:runtime )?dependencies",
    r"Do not require access to original arch, FAQE, DOCK, or faq source files",
]

FORBIDDEN_RUNTIME_DEPENDENCY_PATTERNS = [
    r"GPT[^.\n]{0,80}must[^.\n]{0,80}(?:open|read|inspect)[^.\n]{0,80}(?:arch|FAQE|DOCK|faq)",
    r"cannot answer[^.\n]{0,80}without[^.\n]{0,80}(?:arch|FAQE|DOCK|faq)",
    r"requires? original source files at GPT answer time",
]

COVERAGE_LEDGER_RULES = {
    "llm-reference/coverage/source-inventory.tsv": (8, {"pending", "recheck_required"}),
    "llm-reference/coverage/source-to-topic-map.tsv": (5, {"pending", "recheck_required"}),
    "llm-reference/coverage/semantic-unit-coverage.tsv": (5, {"pending", "recheck_required"}),
    "llm-reference/coverage/attachment-diagram-register.tsv": (6, {"recheck_required"}),
    "llm-reference/coverage/answerability-backtest.tsv": (6, {"recheck_required", "not_answerable"}),
    "llm-reference/coverage/omissions-and-risks.tsv": (5, {"recheck_required"}),
}


@dataclass
class CheckResult:
    name: str
    status: str
    detail: str


class Validator:
    def __init__(self, mode: str) -> None:
        self.mode = mode
        self.results: list[CheckResult] = []

    def pass_(self, name: str, detail: str = "") -> None:
        self.results.append(CheckResult(name, "PASS", detail))

    def fail(self, name: str, detail: str) -> None:
        self.results.append(CheckResult(name, "FAIL", detail))

    def warn(self, name: str, detail: str) -> None:
        self.results.append(CheckResult(name, "WARN", detail))

    def repo_path(self, rel_path: str) -> Path:
        return REPO_ROOT / rel_path

    def read_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def check_source_files_exist(self) -> None:
        missing = [p for p in REQUIRED_SOURCE_PATHS if not self.repo_path(p).is_file()]
        if missing:
            self.fail("source-files-exist", "missing: " + ", ".join(missing))
        else:
            self.pass_("source-files-exist", f"{len(REQUIRED_SOURCE_PATHS)} required source files present")

    def check_coverage_blockers(self) -> None:
        blockers: list[str] = []
        for rel_path, (index, bad_values) in COVERAGE_LEDGER_RULES.items():
            path = self.repo_path(rel_path)
            if not path.is_file():
                blockers.append(f"{rel_path}: missing")
                continue
            with path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.reader(handle, delimiter="\t")
                header = next(reader, None)
                if not header:
                    blockers.append(f"{rel_path}: empty")
                    continue
                for line_no, row in enumerate(reader, start=2):
                    if len(row) <= index:
                        blockers.append(f"{rel_path}:{line_no}: too few columns")
                    elif row[index] in bad_values:
                        blockers.append(f"{rel_path}:{line_no}: {row[index]}")
        if blockers:
            self.fail("coverage-blocking-statuses", "\n".join(blockers[:40]))
        else:
            self.pass_("coverage-blocking-statuses", "no recheck_required or not_answerable status-field blockers")

    def check_generated_outputs_exist(self) -> None:
        required = [
            UPLOAD_DIR / "build-gpts-knowledge-bundles.py",
            UPLOAD_DIR / "validate-gpts-knowledge.py",
            UPLOAD_DIR / "VALIDATION_PROCESS.md",
            HUMAN_REVIEW_CHECKLIST,
            ENCYCLOPEDIA,
            UPLOAD_DIR / "README.md",
            GPTS_INSTRUCTIONS,
            UPLOAD_MANIFEST,
        ]
        missing = [str(p.relative_to(REPO_ROOT)) for p in required if not p.is_file()]
        if missing:
            self.fail("generated-outputs-exist", "missing: " + ", ".join(missing))
        else:
            self.pass_("generated-outputs-exist", f"{len(required)} required generated outputs present")

    def check_upload_file_count(self) -> None:
        if not UPLOAD_DIR.is_dir():
            self.fail("upload-file-count", "llm-reference/gpts-upload does not exist")
            return
        upload_files = sorted(UPLOAD_DIR.glob("Altibase_GPT_Knowledge_*.md"))
        if len(upload_files) > 2:
            files = ", ".join(str(p.relative_to(REPO_ROOT)) for p in upload_files)
            self.fail("upload-file-count", f"expected at most 2 Altibase GPT upload files, found {len(upload_files)}: {files}")
        elif not ENCYCLOPEDIA.is_file():
            self.fail("upload-file-count", "required encyclopedia upload file is missing")
        else:
            detail = ", ".join(str(p.relative_to(REPO_ROOT)) for p in upload_files)
            self.pass_("upload-file-count", detail)

    def extract_included_document(self, bundle: str, rel_path: str) -> str | None:
        pattern = re.compile(
            rf"^BEGIN INCLUDED DOCUMENT: {re.escape(rel_path)}\n(.*?)\nEND INCLUDED DOCUMENT: {re.escape(rel_path)}$",
            re.MULTILINE | re.DOTALL,
        )
        matches = pattern.findall(bundle)
        if len(matches) != 1:
            return None
        content = matches[0]
        if content.startswith("\n"):
            content = content[1:]
        return content

    def count_boundary(self, bundle: str, rel_path: str) -> int:
        return len(re.findall(rf"^BEGIN INCLUDED DOCUMENT: {re.escape(rel_path)}$", bundle, re.MULTILINE))

    def check_full_text_includes(self, bundle: str) -> None:
        problems: list[str] = []
        for rel_path in FULL_TEXT_REQUIRED_PATHS:
            count = self.count_boundary(bundle, rel_path)
            if count != 1:
                problems.append(f"{rel_path}: boundary count {count}, expected 1")
                continue
            included = self.extract_included_document(bundle, rel_path)
            source = self.read_text(self.repo_path(rel_path))
            if included is None:
                problems.append(f"{rel_path}: could not extract included document")
            elif included.rstrip("\n") != source.rstrip("\n"):
                problems.append(f"{rel_path}: included text differs from source")
        if problems:
            self.fail("full-text-required-documents", "\n".join(problems))
        else:
            self.pass_("full-text-required-documents", f"{len(FULL_TEXT_REQUIRED_PATHS)} full-text documents match source")

    def check_topic_documents_once(self, bundle: str) -> None:
        problems = []
        for rel_path in TOPIC_PATHS:
            count = self.count_boundary(bundle, rel_path)
            if count != 1:
                problems.append(f"{rel_path}: {count}")
        if problems:
            self.fail("topic-boundary-counts", "topic boundary counts not exactly one: " + ", ".join(problems))
        else:
            self.pass_("topic-boundary-counts", "all 12 topic documents included exactly once")

    def check_top_matter(self, bundle: str) -> None:
        missing = [term for term in REQUIRED_TOP_MATTER if term not in bundle]
        if missing:
            self.fail("required-top-matter", "missing: " + ", ".join(missing))
        else:
            self.pass_("required-top-matter", "required GPTs front matter and package status found")

    def check_routing_terms(self, bundle: str) -> None:
        head = bundle[:25000].lower()
        missing = [term for term in ROUTING_TERMS if term not in head]
        if missing:
            self.fail("routing-index-coverage", "missing near top: " + ", ".join(missing))
        else:
            self.pass_("routing-index-coverage", "routing terms found near top of bundle")

    def check_limitation_labels(self, bundle: str) -> None:
        missing = [label for label in REQUIRED_LIMITATION_LABELS if label not in bundle]
        if missing:
            self.fail("limitation-labels", "missing: " + ", ".join(missing))
        else:
            self.pass_("limitation-labels", "accepted limitation labels present")

    def check_no_runtime_dependency(self, bundle: str) -> None:
        required_found = any(re.search(pattern, bundle, flags=re.IGNORECASE) for pattern in NO_RUNTIME_DEPENDENCY_PATTERNS)
        forbidden = []
        for pattern in FORBIDDEN_RUNTIME_DEPENDENCY_PATTERNS:
            forbidden.extend(re.findall(pattern, bundle, flags=re.IGNORECASE))
        if forbidden:
            self.fail("no-original-runtime-dependency", "forbidden dependency wording found: " + "; ".join(forbidden[:10]))
        elif not required_found:
            self.fail("no-original-runtime-dependency", "missing explicit no-runtime-dependency rule")
        else:
            self.pass_("no-original-runtime-dependency", "explicit no-runtime-dependency rule found")

    def check_source_traceability(self, bundle: str) -> None:
        source_paths_count = len(re.findall(r"^## Source paths$", bundle, flags=re.MULTILINE))
        source_refs_count = len(re.findall(r"(?:arch/Home|FAQE/Home)/", bundle))
        if source_paths_count < 12:
            self.fail("source-path-traceability", f"expected at least 12 Source paths sections, found {source_paths_count}")
        elif source_refs_count < 100:
            self.fail("source-path-traceability", f"expected substantial source path references, found {source_refs_count}")
        else:
            self.pass_("source-path-traceability", f"{source_paths_count} Source paths sections, {source_refs_count} source references")

    def check_artifact_patterns(self, bundle: str) -> None:
        matches = [pattern for pattern in ARTIFACT_PATTERNS if re.search(pattern, bundle)]
        if matches:
            self.fail("artifact-patterns", "matched patterns: " + ", ".join(matches))
        else:
            self.pass_("artifact-patterns", "no export artifact patterns found")

    def check_no_raw_tsv_in_customer_bundle(self, bundle: str) -> None:
        raw_tsv_boundary = re.findall(r"^BEGIN INCLUDED DOCUMENT: llm-reference/coverage/.*\.tsv$", bundle, flags=re.MULTILINE)
        if raw_tsv_boundary:
            self.fail("no-raw-tsv-in-customer-bundle", "raw TSV files included: " + ", ".join(raw_tsv_boundary))
        else:
            self.pass_("no-raw-tsv-in-customer-bundle", "no raw coverage TSV boundary found in encyclopedia")

    def check_file_size(self, path: Path) -> None:
        size = path.stat().st_size
        rough_tokens = size // ROUGH_CHARS_PER_TOKEN
        if size > MAX_GPTS_FILE_BYTES:
            self.fail("file-size-limit", f"{path.name} is {size} bytes, exceeds 512 MB")
        elif rough_tokens > ROUGH_MAX_TEXT_TOKENS:
            self.fail("rough-token-limit", f"{path.name} rough token estimate {rough_tokens} exceeds {ROUGH_MAX_TEXT_TOKENS}")
        else:
            self.pass_("file-size-limit", f"{path.name}: {size} bytes, rough token estimate {rough_tokens}")

    def check_upload_manifest(self) -> None:
        if not UPLOAD_MANIFEST.is_file():
            self.fail("upload-manifest", "UPLOAD_MANIFEST.tsv missing")
            return
        with UPLOAD_MANIFEST.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            required_cols = {
                "file_path",
                "upload_priority",
                "audience",
                "required_for_customer_answers",
                "purpose",
                "notes",
            }
            if reader.fieldnames is None:
                self.fail("upload-manifest", "manifest has no header")
                return
            missing_cols = required_cols - set(reader.fieldnames)
            if missing_cols:
                self.fail("upload-manifest", "missing columns: " + ", ".join(sorted(missing_cols)))
                return
            rows = list(reader)
        required_rows = [
            row
            for row in rows
            if row["required_for_customer_answers"].strip().lower() in {"yes", "true", "required"}
        ]
        encyclopedia_rows = [
            row for row in rows if row["file_path"].strip().endswith("Altibase_GPT_Knowledge_Encyclopedia.md")
        ]
        if len(required_rows) != 1:
            self.fail("upload-manifest", f"expected exactly 1 customer-required upload row, found {len(required_rows)}")
        elif not encyclopedia_rows:
            self.fail("upload-manifest", "encyclopedia row missing")
        else:
            self.pass_("upload-manifest", f"{len(rows)} rows, 1 required customer upload")

    def check_gpts_instructions(self) -> None:
        if not GPTS_INSTRUCTIONS.is_file():
            self.fail("gpts-instructions", "GPTS_INSTRUCTIONS.txt missing")
            return
        text = self.read_text(GPTS_INSTRUCTIONS)
        required_terms = [
            "Altibase_GPT_Knowledge_Encyclopedia.md",
            "Answer from the uploaded knowledge file",
            "Do not require access to original",
            "Do not invent",
        ]
        missing = [term for term in required_terms if term not in text]
        if missing:
            self.fail("gpts-instructions", "missing: " + ", ".join(missing))
        else:
            self.pass_("gpts-instructions", "copy-paste GPT instructions contain required rules")

    def check_readiness_report(self, required: bool) -> None:
        if not READINESS_REPORT.is_file():
            if required:
                self.fail("readiness-report", "GPTS_READINESS_REPORT.md is required for final validation")
            else:
                self.warn("readiness-report", "GPTS_READINESS_REPORT.md is not present yet")
            return
        text = self.read_text(READINESS_REPORT)
        ready_decision = bool(
            re.search(r"final decision\s*:?\s*`?GPTS_UPLOAD_READY`?", text, flags=re.IGNORECASE)
            or re.search(r"^`GPTS_UPLOAD_READY`$", text, flags=re.MULTILINE)
        )
        recheck_decision = bool(
            re.search(r"final decision\s*:?\s*`?GPTS_RECHECK_REQUIRED`?", text, flags=re.IGNORECASE)
            or re.search(r"^`GPTS_RECHECK_REQUIRED`$", text, flags=re.MULTILINE)
        )
        if recheck_decision:
            self.fail("readiness-report", "report final decision is GPTS_RECHECK_REQUIRED")
        elif not ready_decision:
            self.fail("readiness-report", "report has no GPTS_UPLOAD_READY final decision")
        elif required and "GPTS_AUTOMATED_PASS" not in text:
            self.fail("readiness-report", "final report does not reference GPTS_AUTOMATED_PASS")
        elif required and not re.search(r"human review.*GPTS_AUTOMATED_PASS", text, flags=re.IGNORECASE | re.DOTALL):
            self.fail("readiness-report", "final report does not state the human review gate")
        else:
            self.pass_("readiness-report", "report contains GPTS_UPLOAD_READY and automated gate evidence")

    def validate_preflight(self) -> None:
        self.check_source_files_exist()
        self.check_coverage_blockers()

    def validate_full(self, *, require_readiness_report: bool = False) -> None:
        self.validate_preflight()
        self.check_generated_outputs_exist()
        self.check_upload_file_count()
        if ENCYCLOPEDIA.is_file():
            bundle = self.read_text(ENCYCLOPEDIA)
            self.check_topic_documents_once(bundle)
            self.check_full_text_includes(bundle)
            self.check_top_matter(bundle)
            self.check_routing_terms(bundle)
            self.check_limitation_labels(bundle)
            self.check_no_runtime_dependency(bundle)
            self.check_source_traceability(bundle)
            self.check_artifact_patterns(bundle)
            self.check_no_raw_tsv_in_customer_bundle(bundle)
            self.check_file_size(ENCYCLOPEDIA)
        self.check_upload_manifest()
        self.check_gpts_instructions()
        if AUDIT_BUNDLE.is_file():
            self.check_file_size(AUDIT_BUNDLE)
        self.check_readiness_report(required=require_readiness_report)

    def has_failures(self) -> bool:
        return any(result.status == "FAIL" for result in self.results)

    def print_results(self) -> None:
        for result in self.results:
            detail = f" - {result.detail}" if result.detail else ""
            print(f"[{result.status}] {result.name}{detail}")
        print()
        if self.has_failures():
            print("Final automated decision: GPTS_AUTOMATED_RECHECK_REQUIRED")
        else:
            print("Final automated decision: GPTS_AUTOMATED_PASS")

    def write_report(self, output: Path) -> None:
        output.parent.mkdir(parents=True, exist_ok=True)
        decision = "GPTS_AUTOMATED_RECHECK_REQUIRED" if self.has_failures() else "GPTS_AUTOMATED_PASS"
        lines = [
            "# GPTs Knowledge Automated Validation Report",
            "",
            f"Generated at: {datetime.now(timezone.utc).isoformat()}",
            f"Mode: `{self.mode}`",
            f"Decision: `{decision}`",
            "",
            "## Automated Checks",
            "",
            "| Status | Check | Detail |",
            "| --- | --- | --- |",
        ]
        for result in self.results:
            detail = result.detail.replace("|", "\\|").replace("\n", "<br>")
            lines.append(f"| `{result.status}` | `{result.name}` | {detail} |")
        lines.extend(
            [
                "",
                "## Human Review Boundary",
                "",
                "Start human review only when the automated decision is `GPTS_AUTOMATED_PASS`.",
                "Human review must still check customer-facing clarity, representative answer quality, and GPTs UI behavior.",
                "",
            ]
        )
        output.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Altibase GPTs Knowledge upload artifacts.")
    parser.add_argument(
        "--mode",
        choices=["preflight", "full", "final"],
        default="full",
        help="preflight checks source corpus only; full checks generated artifacts; final also requires readiness report",
    )
    parser.add_argument(
        "--write-report",
        metavar="PATH",
        help="write a Markdown automated validation report to PATH",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validator = Validator(mode=args.mode)
    if args.mode == "preflight":
        validator.validate_preflight()
    elif args.mode == "final":
        validator.validate_full(require_readiness_report=True)
    else:
        validator.validate_full()
    validator.print_results()
    if args.write_report:
        validator.write_report(REPO_ROOT / args.write_report)
    return 1 if validator.has_failures() else 0


if __name__ == "__main__":
    sys.exit(main())
