# Roadmap

## Current bounded exposure research

`EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1` is active under ADR-0019. It tests continuous-account terminal wealth for the frozen Ridge F1/S123 signal and cash choices on the 72-security 2019–2023 research subset. At most two gates, no new model and no later tranche. After its report and independent review, next step is controller direction, with no automatic test or production transition.

## Completed Generation 1

1. `P0_6E_FREE_DATA_EXPANSION_V1`: `COMPLETE` / `P0_6E_PASS_WITH_WARNINGS`.
2. `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1`: `COMPLETE` / `P0_7C_PASS_WITH_WARNINGS`.
3. `P0_7D_ALPHA_POOL_QUALIFICATION_V1`: `COMPLETE` / `P0_7D_PASS_WITH_WARNINGS`; one research-only anchor.
4. `P0_7E_ALPHA_RESEARCH_V2`: `COMPLETE` / `P0_7E_PASS_WITH_WARNINGS`; zero new promotions, unchanged singleton strict pool, unchanged top-20 equal-weight constructor.

Generation-1 predictive accounting closed at 34 configurations and 170 fold attempts. Its 2019-2025 evidence is selection-contaminated. The 2026 holdout remains sealed.

## Generation 2 — P0-8

1. `P0_8A_FACTOR_ZOO_BUILD_V1`: completed with warnings; froze 103 definitions without predictive results.
2. `P0_8B_FACTOR_EVALUATION_V1`: completed with warnings; evaluated 97 eligible factors across 291 WF1-WF3 attempts, retaining failures.
3. `P0_8C_FACTOR_STRUCTURE_V1`: completed with warnings; 27 survivors, 351 pairs, 16 archetypes, 12 frozen interaction-investigation leads.
4. `P0_8D0_INTERACTION_HYPOTHESIS_DESIGN_V1`: completed as no-result design; investigated 12 exact pairs, froze zero executable Interaction Cards, retained all rejection/deferral reasons.
5. `P0_8D_FACTOR_INTERACTION_EXECUTION_V2`: `NOT_READY_NO_EXECUTABLE_CARDS`; no activation or predictive attempts. Requires a later, separately reviewed nonempty preregistration and exact controller directive.
6. `P0_8E_ALPHA_POOL_V2`: not authorized; possible one-pass WF4-WF5 internal reuse validation only after a separate controller decision on frozen inputs.
7. `P0_8F_SPARSE_MULTIFACTOR`: later structured-representative comparison, at most one Ridge and two ElasticNet configurations; LightGBM/deep/RL budget zero.
8. `P0_8G_FINAL_RESEARCH_POOL_V2`: later final research entity and separate holdout-decision handoff.

Detailed stage contracts are in `research/factor-zoo/P0_8_ROADMAP.md`.

## Protected boundary

The old P0-7B interval remains `SUPERSEDED_UNCONSUMED`. The 2026-01-05 through 2026-09-15 holdout remains `SEALED / UNACCESSED / UNCONSUMED`. P0-8A through P0-8G may not access it. Any later evaluation requires an exact frozen entity, one primary endpoint, an immutable pre-access one-run manifest, and no tuning or rerun.

## Later

- Revisit paid-data validation only when a quantified PIT, survivorship, or execution-evidence gap blocks a named decision and free evidence cannot resolve it.
- Use Shadow execution before any broker integration.
- Paper trading and real trading remain separate later phases with explicit risk and external-action controls.
