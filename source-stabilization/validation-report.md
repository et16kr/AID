# English Source Stabilization Final Report

Report date: 2026-05-16

Workspace: `/home/et16/AID`

Phase 2 job: `E009` - Final Stabilization Report

## Final Decision

`READY_FOR_LLM_CONSOLIDATION`

The user may run `.codex-jobs/llm-reference-consolidation/run-all.sh` next. Phase 3 was not run by this job, and `llm-reference/` was not created.

## Handoff Gate

The required handoff check was run from the repository root before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: pass. The command produced no output, so no project handoff files outside `.codex-jobs` blocked E009.

## Phase 1 Gate

`KO_EN_SEMANTIC_COVERAGE_REPORT.md` was read directly. It records the Phase 1 decision as `COMPLETE`, with zero final `missing`, `unverified`, or recheck rows, completed manifest metadata, and preserved URL-backed document attachments.

This satisfies the Phase 2 prerequisite that Korean-to-English semantic coverage is complete before LLM reference consolidation.

## E001-E008 Evidence Summary

| Job | Evidence | Result | Blocker status |
| --- | --- | --- | --- |
| E001 | `source-stabilization/README.md` | Phase 1 decision recorded as `COMPLETE`; baseline counts recorded as `DOCK/Home=51`, `faq/Home=115`, `arch/Home=181`, `FAQE/Home=241`; evidence files initialized. | No blocker |
| E002 | `source-stabilization/residual-korean-classification.tsv` | 24 live Hangul hits classified: 17 intentional attachment filenames and 7 intentional sample-data hits. | No untranslated or recheck rows |
| E003 | `source-stabilization/markdown-artifacts.tsv` | One `clean_no_match` evidence row records a passing artifact scan. | No live Markdown artifact blocker |
| E004 | `source-stabilization/legacy-attachments.tsv` | 21 legacy labels inventoried: 19 technical source limitations, 1 FAQ source limitation, and 1 legacy attachment-label row. | No blocker; all are source limitations with no downloadable source URL |
| E005 | `source-stabilization/url-backed-attachments.tsv` technical rows | 56 technical rows: 42 preserved URLs, 6 legacy no-downloadable-URL rows, and 8 non-document-format rows. | No technical URL-backed omission |
| E006 | `source-stabilization/url-backed-attachments.tsv` FAQ rows | 21 FAQ rows: 7 preserved URLs, 2 legacy no-downloadable-URL rows, and 12 non-document-format rows. | No FAQ URL-backed omission |
| E007 | `source-stabilization/source-classification.tsv` | 241 FAQE paths classified: 108 Korean-source-verified, 7 link-validated Korean-source-verified, and 126 English-only source rows. | No English-only source is presented as Korean-source-verified |
| E008 | `source-stabilization/manifest-metadata.tsv` | 588 manifest page entries checked, with 0 path mismatches, 0 metadata mismatches, and 0 manifest fixes required. | No manifest blocker |

## Source-Stability Checks

Residual Korean text is intentionally classified. The remaining live hits are attachment filenames, encoded/downloadable filenames, legacy filename placeholders, or sample data used in character-set examples.

Markdown artifact checks are clean. The artifact scan returned no matches; exit code 1 is expected and passing for an `rg` no-match scan.

Legacy attachment labels are inventoried and treated as source limitations. No synthetic URL was introduced for labels where the Korean source has no downloadable URL.

Technical and FAQ attachment checks have zero URL-backed document-format omissions. Rows marked `legacy_no_downloadable_url` are source limitations, not unresolved URL omissions. Rows marked `not_document_format` are outside the document-format attachment gate.

English-only FAQE material is classified separately. The `ALTIBASE HDB*` and `Altibase Error Messages` areas are auxiliary Phase 3 sources and must be labeled as English-only if used in consolidation.

Manifest metadata matches the current Markdown source files. No source document changed in E009, so no `manifest.json` update was required.

## Commands Run

### Required reading and evidence review

```bash
sed -n '1,260p' AGENTS.md
sed -n '1,260p' .codex-jobs/english-source-stabilization/workflow-requirements.md
sed -n '1,360p' KO_EN_SEMANTIC_COVERAGE_REPORT.md
sed -n '1,520p' LLM_REFERENCE_REVIEW_PLAN.md
sed -n '1,220p' semantic-coverage/README.md
sed -n '1,220p' source-stabilization/README.md
find source-stabilization -maxdepth 2 -type f | sort
```

Result: pass. Required Phase 1, Phase 2, and Phase 3 boundary documents were reviewed; existing Phase 2 evidence files were present.

### Evidence summaries and blocker scans

```bash
awk -F '\t' 'NR>1 {c[$3]++} END {for (k in c) print k, c[k]}' source-stabilization/residual-korean-classification.tsv
awk -F '\t' 'NR>1 {c[$3]++} END {for (k in c) print k, c[k]}' source-stabilization/markdown-artifacts.tsv
awk -F '\t' 'NR>1 {c[$4]++} END {for (k in c) print k, c[k]}' source-stabilization/legacy-attachments.tsv
awk -F '\t' 'NR>1 {c[$1 ":" $8]++} END {for (k in c) print k, c[k]}' source-stabilization/url-backed-attachments.tsv
awk -F '\t' 'NR>1 {c[$2]++} END {for (k in c) print k, c[k]}' source-stabilization/source-classification.tsv
awk -F '\t' 'NR>1 {c[$5]++} END {for (k in c) print k, c[k]}' source-stabilization/manifest-metadata.tsv
awk -F '\t' 'NR>1 && ($3=="real_untranslated_text" || $3=="needs_recheck" || $7!="none") {print}' source-stabilization/residual-korean-classification.tsv
awk -F '\t' 'NR>1 && ($3!="clean_no_match" || $7!="none") {print}' source-stabilization/markdown-artifacts.tsv
awk -F '\t' 'NR>1 && $8=="needs_recheck" {print}' source-stabilization/url-backed-attachments.tsv
awk -F '\t' 'NR>1 && $5=="needs_recheck" {print}' source-stabilization/manifest-metadata.tsv
test ! -e llm-reference
```

Result: pass. No unresolved blocker rows were found. `llm-reference/` does not exist.

### Standard verification

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

Results:

| Command | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Pass |
| `git diff --check` | Pass |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |

### Targeted source-stability scans

```bash
rg -n "[\x{AC00}-\x{D7A3}]" arch/Home FAQE/Home
```

Result: 24 matches. All 24 matches are represented in `source-stabilization/residual-korean-classification.tsv` as intentional attachment filenames or intentional sample data.

```bash
artifact_pattern="$(printf '%s|%s%s|%s%s|%s%s|%s' '\[\]\(' 'Error rendering' ' macro' 'Unknown' ' macro' 'unknown' '-macro' '\]\(#\)')"
rg -n "$artifact_pattern" arch/Home FAQE/Home semantic-coverage source-stabilization
```

Result: pass. The scan returned no matches with `rg` exit code 1, which is expected for a no-match defect scan.

## Remaining Risks

- Legacy attachment labels with no downloadable source URL remain source limitations. Phase 3 must keep them as labels and must not invent download URLs.
- English-only FAQE sources may be useful auxiliary references, but Phase 3 must label them as English-only and not describe them as Korean-source-verified.
- Residual Hangul in English source files is intentional and should be preserved when it is part of attachment filenames, encoded filenames, or sample data.

These risks are documented and bounded. None blocks Phase 3.

## Diff Review

The final report diff was reviewed with:

```bash
git diff --no-index -- /dev/null source-stabilization/validation-report.md
```

Result: reviewed. Exit code 1 is expected for this command because it displays a new-file diff.

## Phase 3 Boundary

E009 did not create `llm-reference/` and did not run `.codex-jobs/llm-reference-consolidation/run-all.sh`.

Because Phase 1 is `COMPLETE`, Phase 2 source-stability checks have no unresolved blockers, standard verification passes, and Phase 3 output was not created, the English source set is ready for the LLM reference consolidation workflow.
