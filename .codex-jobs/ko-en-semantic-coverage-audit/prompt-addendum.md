# Shared Semantic Coverage Audit Requirements

Every job in this workflow must follow `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.

## Required Reading

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- The Korean source and English target documents in the current job scope

## Critical Rule

Previous J/P workflow reports are useful orientation, but they are not sufficient proof for this workflow. Each audit job must inspect the scoped Korean source and English target files directly and create semantic-unit matrix evidence.

## Semantic Unit Requirement

Audit by semantic unit, not by visual line number. A semantic unit is the smallest independently meaningful content item, including:

- heading or subheading
- paragraph
- bullet or numbered step
- table row
- SQL block
- command block
- configuration item
- warning, note, exception, version condition, or limitation
- error code and resolution item
- attachment or external reference link

Do not collapse content-bearing units merely to reduce matrix size. If a Korean unit is nontechnical boilerplate or a source limitation, record it explicitly with a reason.

## Coverage Status Values

Use only these status values in matrix rows:

- `covered`: English already represents the Korean unit with preserved meaning.
- `added`: English was updated in this job to represent the Korean unit.
- `not_applicable`: The Korean unit is intentionally not carried into English, with a defensible reason.
- `source_limitation`: The source has a placeholder, broken export, or no downloadable URL; no English content can be inferred.
- `missing`: English does not represent the Korean unit yet. This must be fixed before the job completes unless blocked.
- `unverified`: The job could not verify coverage. This must become `covered`, `added`, or `recheck_required` before the job completes.
- `recheck_required`: A human or later job must review this unit because correctness cannot be established safely.

`missing` and `unverified` are not allowed in a successful committed job. If they remain, either fix the English document or stop with a clear failure. `recheck_required` is allowed only if the job records the blocker and the final decision will become `RECHECK_REQUIRED`.

## Matrix Columns

Use TSV files under `semantic-coverage/matrices/` with this header:

```text
job_id	ko_path	ko_start_line	ko_end_line	ko_unit_id	unit_type	ko_excerpt	required_identifiers	en_target_paths	en_start_line	coverage_status	action	evidence_excerpt	risk	notes
```

Keep excerpts short enough to review, but include exact identifiers, commands, SQL, version numbers, paths, property names, error codes, and attachment filenames.

## Required Outputs

- Per-job matrix: `semantic-coverage/matrices/<job-id>-<slug>.tsv`
- Per-job note: `semantic-coverage/notes/<job-id>-<slug>.md`
- Final report updated by final jobs: `KO_EN_SEMANTIC_COVERAGE_REPORT.md`

If English `arch/` or `FAQE/` files change, update `manifest.json` metadata for changed Markdown pages.

## Standard Verification

Run scope-appropriate checks and record results in the per-job note:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

For final or stabilization jobs, also check:

```bash
rg -n "\[\]\(|Error rendering macro|Unknown macro|unknown-macro|\]\(#\)" arch/Home FAQE/Home semantic-coverage
rg -n $'\t(missing|unverified)\t' semantic-coverage/matrices
```

The final decision must be exactly one of:

- `COMPLETE`: all in-scope Korean semantic units are `covered`, `added`, `not_applicable`, or `source_limitation`; no `missing`, `unverified`, or `recheck_required` rows remain; validation passes.
- `RECHECK_REQUIRED`: any semantic unit remains uncertain, disputed, technically unsafe to translate, or blocked by insufficient source evidence.
