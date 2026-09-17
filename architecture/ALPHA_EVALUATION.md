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

The old P0-7B Blind is `SUPERSEDED_UNCONSUMED` under ADR-0007; `BLIND_CONSUMED = FALSE`. Preserve it but never execute it. P0-7C ordinary research uses five annual walk-forward OOS folds through 2025 and excludes a new protected 2026 holdout from all candidate selection.
