## Pass2 Sentence-Level Audit Contract

Before editing, read:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-doc-coverage/jobs.tsv`
- `.codex-jobs/ko-en-doc-coverage-pass2/workflow-requirements.md`

Follow the section of `workflow-requirements.md` matching this job id.

The generated workflow files under `.codex-jobs/ko-en-doc-coverage-pass2/` are control files for this pass. If this is P201 and the workflow scaffold is still untracked, include the scaffold in the P201 commit together with the baseline note and pass2 report. Do not treat the freshly generated scaffold as previous-job product documentation output.

Audit at sentence, bullet, table-row, command, SQL, configuration, warning, version, attachment, and link level. If Korean and English structures differ, compare by semantic unit rather than line number.

Korean `DOCK/Home` and `faq/Home` documents are authoritative. Do not edit Korean source documents. Update English `arch/Home` or Korean-core `FAQE/Home` documents only when Korean-source meaning, commands, SQL, settings, warnings, version conditions, attachments, or links are missing, outdated, incorrect, or unclear in English.

Preserve product names, commands, SQL, system views, properties, file paths, environment variables, error codes, versions, attachment filenames, and URLs exactly. Write surrounding explanations in natural technical English.

Each job must create or update:

- A job note under `.codex-jobs/ko-en-doc-coverage-pass2/`, named with this job id and a short slug.
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`, with a section for this job.

If no English documentation change is needed, still record checked documents, evidence, a no-change conclusion, verification, and remaining risks in the job note and pass2 report.

If English Markdown documents are edited, update `manifest.json` metadata for those changed pages using the repository's existing format.

Run appropriate verification, including at minimum:

```bash
python3 -m json.tool manifest.json
git diff --check
```

Review the final diff, then create a focused commit. A successful job must leave project files clean.
