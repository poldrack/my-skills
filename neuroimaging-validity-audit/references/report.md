# Audit report structure

Adapt length to scope; retain the distinctions below even in a compact report.

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
