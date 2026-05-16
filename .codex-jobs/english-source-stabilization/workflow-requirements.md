# English Source Stabilization Workflow Requirements

## Purpose

This workflow is Phase 2 of the Altibase documentation cleanup. Phase 1 already completed Korean-to-English semantic coverage with final decision `COMPLETE` in `KO_EN_SEMANTIC_COVERAGE_REPORT.md`. Phase 2 stabilizes the English source documents before the LLM reference consolidation workflow runs.

Phase 2 must make `arch/Home` and `FAQE/Home` safe as source material for GPTs, Codex, and other LLM references. It checks residual Korean text, Markdown artifacts, attachment evidence, English-only FAQ classification, manifest metadata, and final readiness.

Do not create `llm-reference/` in this workflow. The existing `.codex-jobs/llm-reference-consolidation/` workflow is Phase 3 and must not be run from Phase 2.

## Authority And Boundaries

- Korean documents under `DOCK/Home` and `faq/Home` remain authoritative.
- English documents under `arch/Home` and Korean-core `FAQE/Home` are the stabilization targets.
- Do not delete, move, or rewrite Korean source documents.
- Do not delete, move, or rename original English source documents.
- English source files may be edited only to fix real source-stability defects found by the current job.
- Update `manifest.json` metadata only when Markdown source file contents change or when validation proves existing metadata is stale.
- Preserve exact product names, commands, SQL, properties, paths, error codes, class names, attachment filenames, and source URLs.

## Phase 2 Evidence Outputs

Jobs write evidence under `source-stabilization/`:

- `source-stabilization/README.md`
- `source-stabilization/residual-korean-classification.tsv`
- `source-stabilization/markdown-artifacts.tsv`
- `source-stabilization/legacy-attachments.tsv`
- `source-stabilization/url-backed-attachments.tsv`
- `source-stabilization/source-classification.tsv`
- `source-stabilization/manifest-metadata.tsv`
- `source-stabilization/validation-report.md`

Each TSV file must use tab-separated rows with the exact header below. Escape literal tabs or newlines inside field values as `\t` and `\n`.

`source-stabilization/residual-korean-classification.tsv`:

```text
path	line	class	excerpt	action	evidence	risk	notes
```

Allowed `class` values: `intentional_attachment_filename`, `intentional_url_or_encoded_filename`, `intentional_sample_data`, `real_untranslated_text`, `needs_recheck`.

`source-stabilization/markdown-artifacts.tsv`:

```text
path	line	pattern_class	excerpt	action	evidence	risk	notes
```

Allowed `pattern_class` values: `empty_markdown_link`, `macro_rendering_artifact`, `unknown_macro`, `hash_only_attachment_link`, `historical_evidence_reference`, `clean_no_match`.

`source-stabilization/legacy-attachments.tsv`:

```text
source_path	label	related_evidence_path	source_class	action	risk	notes
```

Allowed `source_class` values: `technical_source_limitation`, `faq_source_limitation`, `legacy_attachment_label_only`.

`source-stabilization/url-backed-attachments.tsv`:

```text
scope	ko_path	en_target_paths	attachment_label	extension	ko_url	en_url	status	action	risk	notes
```

Allowed `scope` values: `technical`, `faq`. Allowed `status` values: `preserved_url`, `legacy_no_downloadable_url`, `not_document_format`, `needs_recheck`.

`source-stabilization/source-classification.tsv`:

```text
path	source_class	evidence_path	allowed_phase3_use	risk	notes
```

Allowed `source_class` values: `Korean-source-verified`, `Link-validated Korean-source-verified`, `English-only source`, `Legacy attachment label only`, `Diagram unavailable`.

`source-stabilization/manifest-metadata.tsv`:

```text
path	manifest_entry_id	checked_fields	status	action	body_chars_manifest	body_chars_actual	word_count_manifest	word_count_actual	risk	notes
```

Allowed `status` values: `matched`, `normalized`, `missing_path`, `needs_recheck`.

## Evidence Update Policy

- Jobs must be idempotent. Re-running a job must not duplicate evidence rows.
- E001 initializes evidence files only when they do not exist; if a later rerun finds existing evidence, preserve later job rows unless explicitly reinitializing E001 from a clean Phase 2 start.
- E002, E003, E004, E007, and E008 own one evidence file each and may regenerate that file from the header down.
- E005 owns only `technical` rows in `source-stabilization/url-backed-attachments.tsv`; on rerun, replace existing `technical` rows and preserve `faq` rows.
- E006 owns only `faq` rows in `source-stabilization/url-backed-attachments.tsv`; on rerun, replace existing `faq` rows and preserve `technical` rows.
- E009 owns `source-stabilization/validation-report.md` and may regenerate it.

## Final Decision

The final Phase 2 report must use exactly one decision:

- `READY_FOR_LLM_CONSOLIDATION`: Phase 1 decision is `COMPLETE`; English source defects are fixed or intentionally classified; URL-backed attachment omissions are zero; English-only FAQE sources are not mislabeled as Korean-source-verified; `manifest.json` and standard checks pass.
- `RECHECK_REQUIRED`: any source defect, classification gap, attachment uncertainty, metadata mismatch, or validation failure remains unresolved.

## Standard Checks

Run these checks in every job unless the job explains why a narrower check is sufficient:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

Use these targeted scans where relevant:

```bash
rg -n "[가-힣]" arch/Home FAQE/Home
rg -n "\[\]\(|Error rendering macro|Unknown macro|unknown-macro|\]\(#\)" arch/Home FAQE/Home semantic-coverage source-stabilization
```

For expected-no-match scans, `rg` exit code 1 is a passing no-match result. Exit code 2 or higher is a command error.

Document-format attachment extensions:

```text
.pdf .ppt .pptx .doc .docx .xls .xlsx .zip
```

## Job Details

### E001 - Phase 1 completion gate and baseline

Create `source-stabilization/README.md` and initialize evidence files with headers. Confirm `KO_EN_SEMANTIC_COVERAGE_REPORT.md` records final decision `COMPLETE`. Record baseline document counts, current branch/HEAD, clean-start evidence, and the rule that stale status values in old Phase 1 job files do not override the final report.

Acceptance:

- Phase 1 final decision is recorded from `KO_EN_SEMANTIC_COVERAGE_REPORT.md`.
- Evidence directory and all planned evidence files exist with headers or initial content.
- Baseline counts are recorded.
- Standard checks pass.

### E002 - Residual Korean classification

Scan `arch/Home` and `FAQE/Home` for Hangul. Classify every live hit in `source-stabilization/residual-korean-classification.tsv` as one of: `intentional_attachment_filename`, `intentional_url_or_encoded_filename`, `intentional_sample_data`, `real_untranslated_text`, or `needs_recheck`.

Fix `real_untranslated_text` only when the English correction is safe from local source context. Preserve intentional Korean filenames and sample data.

Acceptance:

- Every Hangul hit from the scan is classified.
- No `real_untranslated_text` remains after safe fixes.
- No `needs_recheck` remains unless E009 must decide `RECHECK_REQUIRED`.
- `manifest.json` metadata is updated if Markdown files changed.

### E003 - Markdown artifact cleanup

Scan English sources and Phase 1/2 evidence for empty links, macro-rendering artifacts, unknown macro strings, and hash-only Markdown attachment links. Record findings in `source-stabilization/markdown-artifacts.tsv`.

Fix live English-source defects when the correct text is clear. Do not erase historical evidence meaning; rephrase evidence only if the literal artifact token creates false validation failures.

Acceptance:

- Live English sources have no unclassified artifact hits.
- Evidence files either avoid stale artifact tokens or explicitly mark intentional historical references.
- Standard artifact scan is clean or each intentional hit is documented with a narrower passing scan.

### E004 - Legacy attachment inventory

Build `source-stabilization/legacy-attachments.tsv` from English sources and Phase 1 evidence. Include every legacy attachment label that has no downloadable URL in the source and record `no downloadable URL in source`.

Acceptance:

- Legacy labels from `semantic-coverage` S019/S031 evidence are represented.
- No fake URL is introduced.
- Each row names source path, label, source class, related evidence path, and risk.

### E005 - Technical URL-backed attachment verification

Verify technical document-format attachment URLs in `DOCK/Home` sources are preserved in mapped `arch/Home` targets, using Phase 1 mapping and S019 evidence as the starting point. Write `technical` rows to `source-stabilization/url-backed-attachments.tsv`.

Acceptance:

- URL-backed technical document-format attachment omissions are zero, or E009 must decide `RECHECK_REQUIRED`.
- Rows distinguish `preserved_url`, `legacy_no_downloadable_url`, `not_document_format`, and `needs_recheck`.
- Existing `docs.altibase.com` URLs are not rewritten.

### E006 - FAQ URL-backed attachment verification

Verify FAQ document-format attachment URLs in `faq/Home` sources are preserved in mapped `FAQE/Home` targets, using Phase 1 mapping and S031 evidence as the starting point. Write `faq` rows to `source-stabilization/url-backed-attachments.tsv`.

Acceptance:

- URL-backed FAQ document-format attachment omissions are zero, or E009 must decide `RECHECK_REQUIRED`.
- Rows distinguish `preserved_url`, `legacy_no_downloadable_url`, `not_document_format`, and `needs_recheck`.
- Existing `docs.altibase.com` URLs are not rewritten.

### E007 - English-only FAQE classification

Classify FAQE sources that are not Korean-source-verified. Write `source-stabilization/source-classification.tsv`.

Acceptance:

- Korean-core FAQE paths mapped in `semantic-coverage/doc-mapping.tsv` are classified separately from English-only FAQE paths.
- `FAQE/Home/ALTIBASE HDB*`, `FAQE/Home/Altibase Error Messages/**`, and `FAQE/Home/Altibase Error Messages__6979655.md` are marked `English-only source` unless direct Korean-source evidence proves otherwise.
- Phase 3 instructions can rely on the classification without guessing source authority.

### E008 - Manifest and source metadata check

Validate `manifest.json` against current source files and record results in `source-stabilization/manifest-metadata.tsv`. If source Markdown files changed in E002-E007 or metadata is stale, normalize `body_chars` and `word_count` for affected entries.

Acceptance:

- `manifest.json` is valid JSON.
- Manifest paths resolve after repository-normalization rules used by Phase 1.
- `body_chars` and `word_count` match current Markdown files for checked entries.
- Source counts remain stable unless a prior job explicitly documented a safe reason.

### E009 - Final stabilization report

Create or update `source-stabilization/validation-report.md`. Merge the results from E001-E008 and decide exactly one of `READY_FOR_LLM_CONSOLIDATION` or `RECHECK_REQUIRED`.

Acceptance:

- Final decision is exactly one allowed value.
- Report includes Phase 1 completion evidence, residual Korean classification summary, artifact summary, attachment summary, English-only source classification summary, manifest summary, commands run, and remaining risks.
- If ready, the report explicitly states that Phase 3 `.codex-jobs/llm-reference-consolidation/` may be run next by the user.
- Standard checks pass.
