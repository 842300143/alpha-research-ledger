# Roadmap

## Completed Generation 1

1. `P0_6E_FREE_DATA_EXPANSION_V1`: `COMPLETE` / `P0_6E_PASS_WITH_WARNINGS`.
2. `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1`: `COMPLETE` / `P0_7C_PASS_WITH_WARNINGS`.
3. `P0_7D_ALPHA_POOL_QUALIFICATION_V1`: `COMPLETE` / `P0_7D_PASS_WITH_WARNINGS`; one research-only anchor.
4. `P0_7E_ALPHA_RESEARCH_V2`: `COMPLETE` / `P0_7E_PASS_WITH_WARNINGS`; zero new promotions, unchanged singleton strict pool, unchanged top-20 equal-weight constructor.

Generation-1 predictive accounting closed at 34 configurations and 170 fold attempts. Its 2019-2025 evidence is selection-contaminated. The 2026 holdout remains sealed.

## Generation 2 — P0-8

1. `P0_8A_FACTOR_ZOO_BUILD_V1`: `DESIGN_READY`; implement, correctness-test, and freeze 103 definitions without predictive results.
2. `P0_8B_FACTOR_EVALUATION`: evaluate up to 99 frozen atomic/transformed definitions on WF1-WF3 with global FDR and retained failures.
3. `P0_8C_FACTOR_STRUCTURE`: signal correlation, IC-series correlation, Top-20 overlap, clustering, residual information, archetypes, and Factor Graph.
4. `P0_8D_FACTOR_INTERACTION`: at most 12 hypothesis-led archetype interactions; no brute-force pairs.
5. `P0_8E_ALPHA_POOL_V2`: open WF4-WF5 once for frozen representatives/interactions and qualify incremental dimensions against the Generation-1 anchor.
6. `P0_8F_SPARSE_MULTIFACTOR`: structured representatives into at most one Ridge and two ElasticNet configurations; LightGBM/deep/RL budget zero.
7. `P0_8G_FINAL_RESEARCH_POOL_V2`: freeze the next final research entity and prepare a separate holdout-decision handoff.

Detailed stage contracts are in `research/factor-zoo/P0_8_ROADMAP.md`.

## Protected boundary

The old P0-7B interval remains `SUPERSEDED_UNCONSUMED`. The 2026-01-05 through 2026-09-15 holdout remains `SEALED / UNACCESSED / UNCONSUMED`. P0-8A through P0-8G may not access it. Any later evaluation requires an exact frozen entity, one primary endpoint, an immutable pre-access one-run manifest, and no tuning or rerun.

## Later

- Revisit paid-data validation only when a quantified PIT, survivorship, or execution-evidence gap blocks a named decision and free evidence cannot resolve it.
- Use Shadow execution before any broker integration.
- Paper trading and real trading remain separate later phases with explicit risk and external-action controls.
