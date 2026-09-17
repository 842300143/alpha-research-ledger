# L3 Alpha Evaluation

## Objective

Measure predictive usefulness and reject unstable, redundant, overfit, or post-cost unusable candidates.

## Core evidence

- IC and RankIC level, distribution, and stability.
- Cross-period, cross-regime, and cross-sectional robustness.
- Alpha decay and intended holding horizon.
- Correlation and incremental contribution relative to the Alpha Pool.
- Turnover, fees, slippage, and capacity-sensitive behavior.
- Multiple-testing and researcher-degrees-of-freedom treatment.

## Evaluation sequence

Use development and validation evidence before protected Blind. Freeze candidate, dataset, split, code, configuration, and comparison set before any approved Blind access.

## Protected Blind

The old P0-7B Blind is `SUPERSEDED_UNCONSUMED` under ADR-0007; `BLIND_CONSUMED = FALSE`. Preserve it but never execute it. P0-7C completed five annual walk-forward OOS folds through 2025 without accessing the protected 2026 holdout. P0-7D and Generation-2 research also exclude 2026 under ADR-0010.

## Current qualification boundary

P0-7D qualified the exact 17 P0-7C survivors and produced a one-member research-only `ALPHA_POOL_V1`: `P07C_ML_ENET_A010_L50`. Ten candidates remained after de-duplication, but nine forward additions failed. Because qualification reused selected OOS evidence, the member is a comparator and research anchor rather than independent confirmation.

P0-7E requires every new candidate to pass standalone stability, anchor-relative residual RankIC, correlation and overlap limits, matched post-cost incremental contribution, regime, drawdown, turnover, and 2x-cost gates. One deterministic order and one reverse leave-one-out pass produce the final pool. The cumulative search history is never reset.

After P0-7E, evaluation freezes one final pool and moves to a separate protected-holdout adequacy/go-no-go decision. No P0-7E result can authorize 2026 access.
