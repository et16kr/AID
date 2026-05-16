# Source Classification

## Source paths

- `source-stabilization/source-classification.tsv`
- `source-stabilization/legacy-attachments.tsv`
- `source-stabilization/url-backed-attachments.tsv`
- `source-stabilization/validation-report.md`
- `llm-reference/coverage/interrupted-run-summary.md`

## Source coverage notes

This file defines the source labels that later topic jobs must use. It does not replace source inventory rows, semantic-unit rows, attachment rows, or answerability rows.

Phase 2 classified `FAQE/Home` source material as follows:

| Source class | Count | Phase 3 use |
| --- | ---: | --- |
| `Korean-source-verified` | 108 | Primary Phase 3 source; may be described as Korean-source-verified. |
| `Link-validated Korean-source-verified` | 7 | Primary Phase 3 source; preserve recorded URL and attachment status. |
| `English-only source` | 126 | Auxiliary Phase 3 source only; label explicitly and do not present as Korean-source-verified. |

Technical `arch/Home` sources are classified from `PASS2_KO_EN_DOC_REVIEW_REPORT.md`, `KO_EN_DOC_REVIEW_REPORT.md`, and the attachment evidence files. R003 must record the per-file class in `source-inventory.tsv` and `source-to-topic-map.tsv` rather than relying on the `FAQE/Home` count table above.

Phase 2 attachment evidence recorded:

| Preservation class | Count | Phase 3 use |
| --- | ---: | --- |
| `preserved_url` | 49 | Preserve the original downloadable URL. |
| `legacy_no_downloadable_url` | 8 | Keep the label and record that no downloadable URL exists in the source. |
| `not_document_format` | 20 | Record only when the job scope needs non-document attachment context. |

## Scope and audience

Use this document when assigning `source_class`, `coverage_status`, `preservation_status`, `final_status`, and risk labels. It is written for later R-series jobs and final reviewers.

## Key facts

- Korean-source-verified English sources may be used as primary answer material.
- English-only auxiliary sources may be useful, but must be labeled as `English-only source` or `english_only_auxiliary`.
- A hash-only legacy label is not a downloadable attachment.
- URL-backed document-format attachments must preserve the original source URL.
- Diagram-unavailable cases must be recorded without reconstructing the missing diagram.
- Final acceptance requires zero `recheck_required` rows unless the final build decision is `RECHECK_REQUIRED`.

## Procedures

1. For a `FAQE/Home` source, first consult `source-stabilization/source-classification.tsv`.
2. For an attachment or external reference, consult `source-stabilization/url-backed-attachments.tsv` and `source-stabilization/legacy-attachments.tsv`.
3. Copy exact source URLs, filenames, labels, commands, SQL, properties, paths, and error codes into topic documents or coverage evidence.
4. If evidence is insufficient, write a risk row instead of guessing.
5. If source material is English-only, state that label in the topic section or coverage note where the material is used.

## SQL, commands, and configuration

Useful classification summaries:

```bash
awk -F '\t' 'NR>1 {c[$2]++} END {for (k in c) print k "\t" c[k]}' source-stabilization/source-classification.tsv
awk -F '\t' 'NR>1 {c[$8]++} END {for (k in c) print k "\t" c[k]}' source-stabilization/url-backed-attachments.tsv
```

## Validation and troubleshooting

If a source is mislabeled as Korean-source-verified, check whether it appears in the Korean-core mappings and Phase 2 reports. If not, relabel it as English-only auxiliary or record `recheck_required`.

If a source label looks like an attachment but the source has no downloadable URL, record `legacy_attachment_label_only` or `legacy_no_downloadable_url`; do not make a synthetic URL.

## Version-specific notes

Classification does not remove version-specific content. A source may be Korean-source-verified while still containing multiple distinct version variants that must be preserved in the topic document and semantic-unit rows.

## Related errors

English-only error catalog rows are useful auxiliary error references, but they must keep an explicit `English-only source` label. Korean-source-verified error FAQ rows are handled separately from the English-only error catalog.

## Attachments and external references

Document-format extensions in the preservation gate are:

- `.pdf`
- `.ppt`
- `.pptx`
- `.doc`
- `.docx`
- `.xls`
- `.xlsx`
- `.zip`

Other files may still be useful operational artifacts, but they are not document-format attachments for the Phase 2 preservation gate.

## Classification labels

| Label | Meaning | Required handling |
| --- | --- | --- |
| `Korean-source-verified` | English source audited against Korean source. | Use as primary answer source. |
| `Link-validated Korean-source-verified` | Korean-source-verified and attachment or link evidence validated. | Use as primary answer source and preserve URL status. |
| `English-only source` | English auxiliary material outside Korean-core verification. | Label explicitly; do not call it Korean-source-verified. |
| `legacy_attachment_label_only` | Legacy label exists without downloadable source URL. | Keep label; record no downloadable URL in source. |
| `diagram_unavailable` | Diagram content is unavailable. | Record limitation; do not reconstruct. |
| `not_document_format` | Attachment or reference is outside document-format preservation gate. | Record when useful; do not treat as URL-backed omission. |
| `recheck_required` | Coverage cannot be verified. | Treat as blocking until resolved or final decision accepts recheck. |

## Terminology

- `source_class`: Classification of a source path, usually from Phase 2 evidence.
- `coverage_status`: Semantic-unit or source inventory status showing whether material is covered or accepted as a limitation.
- `preservation_status`: Attachment and diagram register status.
- `final_status`: Risk-ledger resolution status.
- `english_only_auxiliary`: Semantic-unit status for useful English-only source material.
