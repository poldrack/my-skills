# Audit report structure

Adapt length to scope; retain the distinctions below even in a compact report.

## Write, render, and verify the HTML report

Start from [audit_template.qmd](../templates/audit_template.qmd). Transfer the
reporting methods from reproducibility audits without implying that a validity
audit reproduced raw-image processing. The template needs no R or Python kernel
for a document-only audit; add executable chunks only for checks actually run.

Save `audit.qmd`, `audit.html`, `figures/`, and check outputs/run records in a
paper-specific folder in the user's workspace. For a corpus, use unique paper
IDs (e.g. author-year-short-title) and a corpus summary that identifies shared
dependencies. Use relative paths within each report folder. Preserve original
artifacts and retain figure files alongside the source for later rerendering.

1. Lead with a claim-level summary: what remains supported, what changes, and
   what is unresolved. Retain the two callouts identifying AI-generated content
   and preliminary analysis; accurately state human/independent review status.
2. Populate the sections below. Generate computed tables and prose numbers from
   the same saved results or inline expressions in the chosen execution engine.
   Distinguish paper-reported values from recomputations and approximate checks.
   Proposed checks have no computed result; missing evidence is not a clean pass.
3. Embed relevant figures from executed checks and source figures needed to
   substantiate findings. Use Markdown images with relative paths, captions,
   alt text, and unique figure IDs, or executable plotting chunks. For example:

   ```markdown
   ![Participant estimates for check K1.](figures/participant-estimates.png){#fig-k1}
   ```

   Each caption identifies the claim/check, input/version, units, uncertainty,
   and what the plot establishes. Label source reproductions, new derivative
   plots, sensitivity analyses, and illustrative simulations distinctly. Show
   original and alternative specifications together when informative; report
   all attempted specifications. For brain maps, include orientation, space,
   threshold, and color scale. Do not invent images or compute new analyses
   merely to fill a figure slot. State when no usable figures are available.
4. Keep `format.html.embed-resources: true`, the table of contents, and folded
   code. From the report folder, render with `uv run quarto render audit.qmd`.
   Check the exit status, `Output created` message, and actual HTML file. Record
   Quarto and analysis-tool versions, inputs, seeds where relevant, and commands.
   If Quarto or an execution dependency is unavailable, deliver the source and
   existing figures with the exact blocker; do not claim an HTML was rendered.
5. After every render, extract/read the HTML text and compare every numerical
   statement, status, and caption against displayed tables and saved outputs.
   Check evidence supporting claims as carefully as evidence against them.
   Inspect the rendered figures (or decode embedded base64 PNGs and view them)
   for empty panels, clipped labels, incorrect scales, and mismatched captions.
   Verify image resources are embedded as data URIs or inline SVG, with no local
   file or remote display dependencies. Open a copy of the HTML outside its
   report folder to confirm it works without the figure directory; inspect it
   offline when possible. Ordinary provenance hyperlinks may remain external.
6. Deliver links or attachments to the local HTML and `.qmd` source. Keep the
   report private; publication/upload requires an explicit user request. If
   visual inspection was unavailable, state that remaining verification limit.

The sections below define the content contract used by the template.

## Scope and evidence

Identify papers/versions, selected claims, available versus inspected artifacts,
budget, search scope/date when applicable, and unavailable evidence. Explain
selection of papers/claims. State which upstream processing is held fixed.

## Claim ledger and mechanism table

Use the two tables in SKILL.md. Include a defensible revised claim for each
central claim, including claims that survive unchanged.

## Findings

For every retained finding record:

- ID and affected claim ID.
- Status: verified error / sensitivity demonstrated / unresolved concern /
  reporting gap / no issue found in this check.
- Severity and confidence, separately; no severity required for a clean check.
- Mechanism and direction: false positive, false null, either, or interpretation
  overreach with the relevant direction explained.
- Evidence: verified quote or labeled paraphrase, exact source location, and
  relevant artifact/version. For calculations, inputs, method, output, and run
  record. Mark approximate calculations.
- Existing caveat/correction and strongest counterargument.
- Check status: executed / read-only / proposed; result or missing evidence.
- Consequence: what changes in the conclusion, and what remains supported.
- Cheapest discriminating next check and its decision rule.

## Check ledger

| Check | Inputs | Executed/read-only/proposed | Result | Limitations/upstream dependencies |
|---|---|---|---|---|

List rejected candidate criticisms with concise reasons. Distinguish inability
to check from passing. Summarize supported claims as well as weaknesses.

## Confidence update and next steps

Separate original justification from present-day confidence. For a corpus,
describe shared dependencies without treating repeated findings as independent.
Rank unresolved checks by likely consequence and cost; explain why a costly
rerun would be worth doing before proposing it. Avoid unsupported numerical
confidence scores or binary paper-wide verdicts.

End with specific coverage limits, such as unverified preprocessing or uncertain
sampling generalization, rather than a generic disclaimer. Identify the report
as AI-assisted and state which findings received human or independent review.
