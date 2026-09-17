# P0-7C Sync and P0-7D Design Session — 2026-09-17

## Scope

Synchronize completed P0-7C evidence from Alpha Factory into the research ledger and design `P0_7D_ALPHA_POOL_QUALIFICATION_V1`. This session changed only the research ledger. It ran no experiment, backtest, qualification, data pipeline, protected-holdout evaluation, RD-Agent/LLM call, broker action, or trade.

## Verified execution lineage

- Protocol commit: `95dc8e3c5b895fe7bf47135536e0ed4843b73471`.
- Result commit: `a881bd956c70088100f85999e7f0f4f965777a25`.
- Completion checkpoint: `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138`.
- Result-bundle hash: `30f0879579906af2d341a9053f9090b19616fbd3facd7415461b5ae247329444`.
- Pool-audit hash: `9121c1984a237f7555171fea15bca882febfc4284e26a44c1527456ab4878f62`.

The three commits resolve in a linear ancestry chain. The Alpha Factory worktree was clean during evidence review and was not modified.

## P0-7C outcome

P0-7C completed all 18 Formula and 9 ML configurations across five 2021-2025 OOS folds, retaining 135 configuration-fold attempts. Eight Formula candidates survived from Liquidity, Reversal, and Volatility. All nine ML configurations met the broad survivor gate, but matched incremental RankIC was positive only for three ElasticNet variants; all four LightGBM variants underperformed the best matched Formula stream.

Top-20 equal weight beat the more complex constructor in all six matched comparisons. Seventeen configurations survived predictively, but material correlation and overlap meant they could not be interpreted as 17 independent Alphas. The nine-name historical correlation/decay shortlist was not a strict pool because pooled incremental thresholds were not frozen and the additive audit was mixed. Strict membership therefore remained empty.

The maximum DSR probability was 0.4229 and PBO was not justified. These results leave material selection-bias and multiple-testing risk. The protected 2026 holdout remained unaccessed and unconsumed.

## Research interpretation

- Liquidity, Reversal, and Volatility are priority hypotheses, not proven production Alphas.
- ElasticNet merits decomposition because it showed selective incremental RankIC.
- LightGBM receives no larger budget merely because it is more complex.
- Top-20 equal weight becomes Portfolio Baseline V1.
- The 17 survivors require redundancy and incremental-contribution qualification before broad new search.
- Weak DSR evidence forbids statistical-certainty claims.

## Why P0-7D comes next

The main unresolved P0-7C question is not whether another candidate can be generated. It is whether any of the existing survivors adds genuinely distinct information to a small pool. P0-7D therefore freezes the exact 17 survivors, evaluates every pair, decomposes ML composites against Formula scores, uses one deterministic preference order, performs one forward-addition pass, and performs one reverse-order leave-one-out pass.

The procedure uses one unweighted score combiner and top-20 equal weight. It permits no alternate ordering, threshold, weight, constructor, or candidate subset. Every negative addition remains evidence. A zero-member pool is a successful outcome when justified.

## Multiple testing and holdout discipline

The frozen P0-7C history remains 27 predictive configurations and 135 fold attempts. P0-7D adds zero predictive experiments, but it explicitly counts pairwise, Formula-span, forward-addition, and leave-one-out selection degrees. Because qualification reuses OOS data, `ALPHA_POOL_V1` will remain research-only until a separate independent evaluation.

The 2026 holdout remains sealed throughout P0-7D and Generation-2 research. No protected performance, NAV, ranking, or selection information is available to the pool design.

## Resulting state

- P0-7C: `P0_7C_PASS_WITH_WARNINGS` / `COMPLETE`.
- P0-7D: `DESIGN_READY` / `NOT_YET_EXECUTED`.
- Strict Alpha Pool before P0-7D: 0 members.
- New predictive configurations authorized by P0-7D design: 0.
- Protected 2026 holdout: `UNACCESSED / UNCONSUMED`.
- Next durable state: `CONTROLLER_DIRECTION`.
