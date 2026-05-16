# KO to EN Semantic Coverage Evidence

This directory stores the semantic-unit evidence for the strict Korean-to-English source coverage audit. The audit happens before source stabilization and before any `llm-reference/` consolidation work.

## Scope

- Korean source authority: `DOCK/Home` and `faq/Home`.
- English update targets: Korean-core documents under `arch/Home` and `FAQE/Home`.
- Previous J/P reports are orientation only. They can provide mappings, prior fixes, and risk context, but they do not prove that a current semantic unit is covered.
- Each scoped audit job must inspect its assigned Korean source and English target files directly.
- Korean source documents and original English source documents are not deleted, moved, or rewritten as part of this workflow.
- `llm-reference/` is not created by this workflow.

## Evidence Layout

- `semantic-coverage/README.md`: this method and evidence structure note.
- `semantic-coverage/doc-mapping.tsv`: KO-to-EN mapping inventory, created or updated by S002.
- `semantic-coverage/matrices/<job-id>-<slug>.tsv`: per-job semantic-unit coverage matrix.
- `semantic-coverage/notes/<job-id>-<slug>.md`: per-job audit note, decisions, verification, and review evidence.
- `KO_EN_SEMANTIC_COVERAGE_REPORT.md`: workflow-level report and final decision record.

## Semantic Unit Method

Audit by semantic unit, not visual line number. A semantic unit is the smallest independently meaningful item that must be represented, rejected with a reason, or recorded as a source limitation.

Semantic units include:

- heading or subheading
- paragraph
- bullet or numbered step
- table row
- procedure step
- command block
- SQL block
- configuration item or property description
- warning, caution, note, limitation, exception, or version condition
- error code, cause, and action item
- attachment, source URL, or external reference

Do not collapse content-bearing units to reduce matrix size. If a table row carries multiple independent facts, split it when needed. If a command or SQL block contains commands with different meanings, split it when needed.

Use Korean line ranges only as locators. Coverage is decided by the semantic meaning of the unit, not by whether the English document has the same line structure.

## Matrix Schema

Every matrix file uses this exact TSV header:

```text
job_id	ko_path	ko_start_line	ko_end_line	ko_unit_id	unit_type	ko_excerpt	required_identifiers	en_target_paths	en_start_line	coverage_status	action	evidence_excerpt	risk	notes
```

Rules:

- One physical line per semantic unit.
- Replace tabs inside field values with `\t`.
- Replace newlines inside field values with `\n`.
- Keep code, SQL, and long table excerpts short in the matrix; put detailed excerpts in the matching note.
- Use `; ` to separate multiple English target paths in `en_target_paths`.
- Use stable unit IDs that include the job and source context, for example `S003-D020-U001` or `S020-F01-U001`.

Allowed `coverage_status` values:

- `covered`: English already represents the Korean unit with preserved meaning.
- `added`: English was updated in the current job to represent the Korean unit.
- `not_applicable`: the Korean unit is intentionally not carried into English, with a defensible reason.
- `source_limitation`: the source has a placeholder, broken export, legacy non-downloadable attachment label, or no downloadable URL.
- `missing`: English does not represent the Korean unit yet. This must be fixed before a successful job completes unless blocked.
- `unverified`: the job could not verify coverage. This must become `covered`, `added`, or `recheck_required` before a successful job completes.
- `recheck_required`: correctness cannot be established safely and a human or later job must review it.

Successful scoped jobs must not leave `missing` or `unverified` rows. `recheck_required` rows are allowed only when the job records a concrete blocker and the workflow-level decision remains `RECHECK_REQUIRED`.

## Duplicate Source Ownership

When the same Korean source appears in more than one scope, the first listed owner audits the whole source. Later jobs add only topic-specific cross-reference rows and name the primary owner in `notes`.

The workflow requirements define the current duplicate ownership list:

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md`: primary owner S003.
- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md`: primary owner S005.
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md`: primary owner S005.

## Decision Criteria

The final workflow decision must be exactly one of:

- `COMPLETE`: all in-scope Korean semantic units are `covered`, `added`, `not_applicable`, or `source_limitation`; no `missing`, `unverified`, or `recheck_required` rows remain; English source fixes and `manifest.json` metadata are complete; validation passes.
- `RECHECK_REQUIRED`: any semantic unit remains uncertain, disputed, technically unsafe to translate, or blocked by insufficient source evidence.

Until all source audit, closure, stabilization, and independent challenge jobs are complete, the workflow-level decision remains `RECHECK_REQUIRED`.

## Standard Verification

Every job records scope-appropriate checks in its note. The baseline checks are:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

For expected-no-match `rg` checks, exit code 1 is a passing result because it means no matching defect was found. Exit code 2 or higher is a command error.
