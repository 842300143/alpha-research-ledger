# P0-7D Sync and P0-7E Design Session — 2026-09-17

## Scope

Synchronize completed P0-7D evidence from Alpha Factory into the Research Ledger and design `P0_7E_ALPHA_RESEARCH_V2`. This session changed only the Research Ledger. It ran no market experiment, backtest, Alpha, data pipeline, Shadow run, protected-holdout evaluation, RD-Agent/LLM call, broker action, or trade.

## Verified execution lineage

- Protocol commit: `76568528ed1a7c70d6b0a93b76924d7cb943dc94`.
- Result commit: `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63`.
- Completion checkpoint: `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0`.
- P0-7D qualification payload hash: `d06b21fe5bcea2b394be0d6b7a09006a2518aaf37d04933631b4a5b49fbcb360`.
- Matched-panel hash: `68f1aee1a3f099f0167392bc4cbc3f5ab9b6494bca98170b54e4e46516c22538`.

The commits resolve in one linear ancestry chain. The Alpha Factory worktree was clean during evidence review and remained unchanged.

## P0-7D outcome

P0-7D reproduced exactly 17 frozen P0-7C survivors and added zero predictive experiments. It evaluated 136 unordered pairs and 45 ML Formula-span held-out reconstructions. Deterministic de-duplication left 10 candidates. The fixed forward procedure accepted `P07C_ML_ENET_A010_L50` as anchor and rejected all nine additions; the singleton passed leave-one-out.

The anchor produced fold RankIC `0.0802 / 0.0955 / 0.1675 / 0.0951 / 0.1337`, mean `0.1144`, five positive folds, Formula-relative incremental RankIC `+0.0165`, frozen-cost net `1.0098`, 2x-cost net `0.9369`, MDD `-14.58%`, and a non-decaying 60/20 ratio of `1.4253`.

Seven variants were redundant. Three ElasticNet variants added Formula-relative RankIC; Ridge and all four LightGBM variants failed incremental classification. Maximum prior DSR probability remains `0.422885`. Validator recorded 16 PASS / 4 UNKNOWN / 0 FAIL and 107/107 repository tests passed.

## Research interpretation

The problem has shifted from finding a survivor to finding information independent of the anchor. The anchor is a research comparator, not independent confirmation. Liquidity and reversal merit mechanism separation; LowVol merits robustness testing rather than a window grid. ElasticNet merits explanation through coefficient stability, family exposure, ablations, and residual information. LightGBM receives no further budget. Top-20 equal weight remains Portfolio Baseline V1.

## P0-7E design

P0-7E registers exactly seven predictive configurations and 35 fold attempts:

- one signed abnormal-turnover candidate;
- one medium-reversal-excluding-five candidate;
- one very-short-reversal x abnormal-turnover interaction;
- four fixed ElasticNet feature-family ablations.

It adds 45 LowVol robustness cells, five anchor coefficient snapshots, five Formula-span residual checks, deterministic anchor-relative orthogonality and incremental gates, and one equal-weight membership-buffer portfolio challenger. Failures consume budget and no slot is recycled.

## Multiple testing and stop rule

The cumulative history becomes 34 predictive configurations and 170 fold attempts after full P0-7E execution, plus all P0-7D qualification degrees of freedom. Results remain research-only because 2019-2025 has been repeatedly used for research and selection.

P0-7E is the last major 2019-2025 research iteration. After it closes, freeze one final pool, possibly the unchanged singleton anchor, and make a separate protected-holdout adequacy/go-no-go decision. If the partial 2026 interval is inadequate, keep it sealed and defer; do not restart Generation N.

## Resulting state

- P0-7D: `P0_7D_PASS_WITH_WARNINGS` / `COMPLETE`.
- Research anchor: `P07C_ML_ENET_A010_L50` / research-only.
- P0-7E: `DESIGN_READY` / `NOT_YET_EXECUTED`.
- P0-7E budget: 7 configurations / 35 fold attempts / no recycling.
- Protected 2026 holdout: `UNACCESSED / UNCONSUMED`.
- Next durable state: `CONTROLLER_DIRECTION`.
