# ADR-0014: Permit a Pre-Registered Generation-2 Factor Zoo

- Status: Accepted
- Date: 2026-09-18
- Scope relationship: narrows the interpretation of ADR-0013 without changing its historical P0-7E stop decision

## Context

P0-7E completed the final major **Generation-1** iteration on the repeatedly used 2019-2025 sample. Its three new Formula candidates passed standalone gates but failed the complete anchor-relative incremental gate, the buffer constructor was not promoted, and the strict pool remained the singleton `P07C_ML_ENET_A010_L50`.

ADR-0013 correctly stopped result-driven continuation of the P0-7 family and prohibited treating disappointing P0-7E results as permission for another neighboring parameter search. It did not establish that the canonical factor space available from `FREE_DAILY_V1` had been systematically enumerated. P0-7A through P0-7E covered a small set of Formula concepts and simple models, not a controlled factor taxonomy, factor graph, or archetype discovery program.

## Decision

Authorize the design of `P0-8 FACTOR ZOO & FACTOR STRUCTURE DISCOVERY V1` as a new Generation-2 research program, subject to all of the following:

- P0-8 asks how many independent, repeatable predictive dimensions exist in the available canonical daily price-volume space; it does not optimize for the highest-return strategy.
- Factor concepts, formulas, canonical parameterizations, preprocessing, timing, budgets, lifecycle states, and evaluation rules are pre-registered before results.
- Neighboring-window sweeps, result-driven variants, budget recycling, brute-force interactions, and deleting failures are prohibited.
- P0-8 uses only fields empirically present in `FREE_DAILY_V1`. Size, Value, Quality, industry neutralization, and any other unavailable family receive zero budget.
- All 2019-2025 evidence remains `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`. P0-8 cannot create independent confirmation from reused years.
- The 2026-01-05 through 2026-09-15 protected holdout remains `SEALED / UNACCESSED / UNCONSUMED`. No P0-8 design or execution may inspect its features, labels, candidate coverage, rankings, regimes, NAV, IC, or outcomes.
- The Generation-1 anchor remains a comparator. It does not constrain taxonomy construction or automatically promote or reject a factor.

## Interpretation of ADR-0013

The operative reading is:

> P0-7E was the last major Generation-1 iteration on 2019-2025 and closed the P0-7 candidate-refinement path. It is not a permanent ban on a materially different, explicitly pre-registered canonical factor-space program.

ADR-0013 still prohibits reopening P0-7F, tuning the frozen P0-7E candidates, changing the singleton freeze, or using another P0-7-style search to avoid the holdout decision. This ADR authorizes a new research question and governance structure; it does not alter any frozen P0-7 result.

## Evidence and limits

- `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`: P0-7A through P0-7E results and retained failures.
- `EMPIRICAL`: `FREE_DAILY_V1` field coverage, data-quality checks, feature-readiness contract, and P0-7E completion/checkpoint artifacts.
- `DOCUMENTED`: P0-8 taxonomy, registry, evaluation, structure, interaction, and multiple-testing policies.
- `SYNTHETIC`: transaction costs and execution assumptions used in later evaluation.
- `UNKNOWN`: number of genuinely independent dimensions, independent-holdout behavior, complete PIT/survivorship, market impact, capacity, production readiness, and real-trading behavior.

## Consequences

P0-8A may implement and freeze the canonical library without running predictive results. P0-8B onward requires a separate exact Alpha Factory controller directive and phase manifest. Each stage must retain failures and cumulative experiment accounting. No stage may consume the protected holdout.

## Revisit condition

Revisit only if the field contract changes, a frozen P0-8 stage exposes an implementation defect, or materially new external evidence changes the available factor space. Poor results do not authorize neighboring variants or reset the search history.
