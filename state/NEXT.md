# Next Research Work

## Controller direction

`P0_7E_ALPHA_RESEARCH_V2`

Status: `DESIGN_READY` / `NOT_YET_EXECUTED`

The exact execution specification is `tasks/planned/P0_7E_ALPHA_RESEARCH_V2.md`. A later controller may direct Alpha Factory to activate that design. This ledger commit records governance and does not execute research or authorize protected-holdout access.

## Required activation gates

- Verify Alpha Factory commits `76568528ed1a7c70d6b0a93b76924d7cb943dc94`, `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63`, and `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0` in one linear ancestry chain.
- Bind the exact dataset, subset, split, feature, cost, P0-7C result, P0-7D result, and matched-panel hashes in the task specification.
- Reproduce the exact P0-7D anchor and pool payload before any P0-7E result.
- Freeze code, configuration, registry, formulas, seven configurations, 35 fold attempts, robustness views, orthogonality rules, ordering, constructor, thresholds, and output schemas before results.
- Create a deny-before-load audit proving all materialized research data end no later than 2025-12-31.

## Bounds

- New Formula candidates: exactly 3.
- ElasticNet family ablations: exactly 4; no hyperparameter change.
- Total new predictive configurations: exactly 7.
- Fold attempts: exactly 35; failures consume budget; no recycling.
- LowVol: 45 fixed robustness cells; no new window or formula.
- LightGBM, deep models, Size, Value, Quality, RD-Agent/LLM, paid data: zero budget.
- Portfolio: Top-20 equal weight baseline plus one `15/25` equal-weight membership-buffer challenger; seven reserved evaluations.
- Protected 2026 holdout access: `0`.

## Required output

Produce a fully accounted P0-7E result, one final research-only pool freeze (which may remain the singleton anchor), a complete negative-evidence ledger, and a protected-holdout adequacy/go-no-go handoff without accessing the holdout.

## Post-task stop rule

P0-7E is the last major candidate-generation iteration on 2019-2025. After it closes, freeze the final pool and decide separately whether the partial 2026 holdout is adequate for one confirmatory run. If it is not adequate, leave it sealed and defer. Do not start open-ended P0-7F research on the same years.

## If activation or integrity gates fail

Stop with the exact failed gate. Repair only the named integrity defect under the unchanged preregistration. Do not substitute candidates, change formulas or thresholds, broaden the budget, or access 2026.
