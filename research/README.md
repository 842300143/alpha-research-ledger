# Paper-to-Experiment Workflow

```text
INBOX
  -> PAPER / IDEA
  -> HYPOTHESIS
  -> EXPERIMENT
  -> TASK
  -> alpha-factory execution
  -> RESULT
  -> REVIEW
  -> DECISION
  -> next hypothesis
```

## Stage contract

- **Inbox:** capture a source without treating it as validated.
- **Paper / Idea:** summarize the claim, limitations, and relevance.
- **Hypothesis:** state an economic mechanism, measurable signal, expected direction, confounders, and falsification criteria.
- **Experiment:** predefine data, split, controls, costs, metrics, and multiple-testing treatment.
- **Task:** specify bounded implementation and validation work for `alpha-factory`.
- **Result:** record exact commits, reports, artifacts, dataset identifiers, and evidence class.
- **Review:** interpret limitations, robustness, and lineage without changing raw results.
- **Decision:** accept, reject, revise, defer, or create the next hypothesis.

Every important experiment must answer both:

1. Why does this experiment exist?
2. What decision did its evidence change?

Use the templates in `templates/`. Preserve negative results and never convert a paper or vendor claim into an empirical result.

## Factor Zoo V1

The Generation-2 canonical factor-space design lives in `research/factor-zoo/`. Start with `FACTOR_ZOO_RESEARCH_CHARTER.md`, `FACTOR_TAXONOMY_V1.md`, and `FACTOR_REGISTRY_V1.md`. The registry is design-draft evidence until P0-8A binds implementation and hashes; it contains no predictive result.
