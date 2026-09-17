# P0-6E Sync and P0-7C Design Session — 2026-09-17

## Scope

Synchronize completed P0-6E evidence from Alpha Factory into the research ledger and design `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1`. This was research governance and design only. No Alpha experiment, data pipeline, protected holdout evaluation, RD-Agent/LLM call, broker action, or trade was executed.

## P0-6E changes the research capability

P0-6E created `FREE_DAILY_V1`, a reproducible 5,587,828-row dataset covering 3,207 priced securities and 1,870 trading sessions from 2019-01-02 through 2026-09-15. All 3,195 current securities have price coverage and 12 historical-delisted histories were recovered. The dataset passed its hard data-quality gates and is fast enough for ordinary multi-year research queries.

This materially changes the project from a 120-stock, 299-session diagnostic arena to a multi-year research substrate capable of annual walk-forward evaluation. It does not create production readiness or full feature readiness. Adjustment, ST, and suspension evidence remains concentrated in 83 symbols; 280 historical-delisted master records lack prices; point-in-time certification, authoritative historical limits, complete corporate actions, and fundamentals remain unavailable.

## Why broad data repair is not the default next action

The P0-6E checkpoint states `FREE_DATA_SUFFICIENT_FOR_NEXT_ALPHA_ITERATION = YES` and `PAID_DATA_REQUIRED_NOW = NO`. Liquidity and raw volume/amount features are available, and a frozen action-aware subset provides a bounded path for return-based labels and price-derived features. The next task therefore tests whether this constrained evidence can support durable Alpha research before spending another phase on broad repair.

This is not a claim that repair is unnecessary. P0-7C stops fail-closed if the action-aware universe falls below its minimum cross-section, action-clean labels cannot be proven, or the holdout/data gates fail. Any later repair should target the measured failure rather than expand data speculatively.

## Why the old 60-session Blind is superseded

The old P0-7B Blind interval, 2024-12-27 through 2025-03-31, was never executed or consumed. `FREE_DAILY_V1` now spans that interval, and P0-7C requires multi-year research through 2025. The old interval therefore cannot remain an independent final holdout for the new research generation.

ADR-0007 classifies it as `SUPERSEDED_UNCONSUMED`. All old artifacts and hashes remain historical evidence; no execution manifest is created, and the interval must never be described as a valid Blind result. The actual 2026 sessions in the dataset become a new, separately governed protected holdout.

## Why multi-year walk-forward is adopted

One short split cannot reveal whether a candidate persists across years and market conditions. P0-7C uses five annual OOS folds from 2021 through 2025. Each training window precedes its test year, transformations and model settings are training-only, and feature warmup plus label purging prevent boundary leakage. The 171 sessions from 2026-01-05 through 2026-09-15 are excluded from ordinary research.

This protocol increases the number of genuinely out-of-sample periods while retaining an untouched recent test. It does not make the folds independent or erase survivorship/PIT limitations; those warnings remain part of every result.

## Why Formula, ML, and Portfolio are developed together

Formula Alpha provides transparent mechanisms and strong diagnostics. Simple ML tests whether controlled nonlinear interactions add value beyond those formulas. The Portfolio Layer tests whether a fixed predictive score translates into a feasible, cost-aware holding process. Evaluating the three under the same folds, labels, costs, and universe makes their differences attributable and prevents a portfolio improvement from being mistaken for better prediction.

The scope remains bounded: 18 Formula candidates, 9 ML configurations, and two portfolio constructors with at most 12 comparisons. Simple models come before deep models; Size, Value, and Quality receive no V1 experiment budget.

## Why the Alpha Pool replaces single-strategy selection

The durable objective is a set of stable, low-correlated, post-cost usable signals. P0-7C therefore records predictive power, OOS behavior, stability, turnover, costs, drawdown, decay, correlation, overlap, regimes, complexity, data dependency, and lifecycle status for every candidate. A strong isolated backtest is insufficient if the signal is unstable, redundant, or unusable after costs.

Failed, aborted, negative, redundant, and decaying candidates remain in the immutable registry. Promotion depends on multi-fold evidence and incremental pool contribution, not a single leaderboard winner.

## Evidence and resulting state

- `EMPIRICAL`: P0-6E dataset, coverage, quality, survivorship, resource, and test results from Alpha Factory result commit `69be29e41ddfdf815685f64d697465032c4a9891` and checkpoint commit `52c6a7eb506bb8848f1a643c469978d28804738c`.
- `DOCUMENTED`: P0-7C folds, budgets, label, holdout, Alpha Pool, and overfitting policy.
- `UNKNOWN`: predictive power, profitability, portfolio superiority, regime robustness, and production suitability of every future candidate.

P0-6E is complete. P0-7C is design-ready and not executed. The next state is `CONTROLLER_DIRECTION`.
