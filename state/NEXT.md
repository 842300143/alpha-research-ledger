# Next Research Work

## Controller direction

`P0_7D_ALPHA_POOL_QUALIFICATION_V1`

Status: `DESIGN_READY` / `NOT_YET_EXECUTED`

The exact execution specification is `tasks/planned/P0_7D_ALPHA_POOL_QUALIFICATION_V1.md`. A later controller may direct Alpha Factory to activate that design. This ledger commit records governance and does not execute qualification or authorize protected-holdout access.

## Required activation gates

- Verify Alpha Factory commits `95dc8e3c5b895fe7bf47135536e0ed4843b73471`, `a881bd956c70088100f85999e7f0f4f965777a25`, and `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138` in one linear ancestry chain.
- Bind `FREE_DAILY_V1` hash `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`, P0-7C result-bundle hash `30f0879579906af2d341a9053f9090b19616fbd3facd7415461b5ae247329444`, and pool-audit hash `9121c1984a237f7555171fea15bca882febfc4284e26a44c1527456ab4878f62`.
- Freeze the exact 17-candidate input list and verify each record is `OOS_SURVIVED` with all five folds in the immutable P0-7C registry.
- Create a P0-7D execution manifest before qualification and prove that every loaded or reproduced score and outcome ends no later than 2025-12-31.
- Reproduce the frozen P0-7C score/result identities before computing any new qualification diagnostic; deny on any mismatch.
- Freeze output schemas, metric definitions, pairwise thresholds, ordering, forward-addition rules, and leave-one-out rules exactly as specified.

## Bounds

- Input candidates: exactly 17; substitutions and regeneration are forbidden.
- New predictive configurations, features, targets, horizons, parameters, seeds, or models: `0`.
- Pairwise redundancy assessments: exactly 136 unordered pairs.
- ML formula-span diagnostics: at most 9 frozen ML candidates across five leave-one-fold-out score-reconstruction checks each; these are explanatory, not predictive-return experiments.
- Pool construction: one fixed ordering, one forward pass of at most 17 additions, and one reverse-order leave-one-out pass of at most 17 removals.
- Pool weights: equal weights over within-date percentile-ranked scores; no weighting search.
- Portfolio constructor: top-20 equal weight only; no constructor comparison.
- Protected 2026 holdout access: `0`.

## Required output

Produce `ALPHA_POOL_V1`, including a justified empty pool if no candidate passes. Retain every negative addition, redundancy edge, rejected candidate, and selection-degree count. Produce bounded Generation-2 research questions, not experiments.

## If activation or integrity gates fail

Stop with the exact failed gate. Do not repair, substitute, rerun, broaden the candidate set, alter thresholds, or access the protected holdout under P0-7D.
