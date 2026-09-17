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

P0-7C produced 17 broad OOS survivors but zero strict pool members. P0-7D evaluates their pairwise redundancy, ML Formula-span, and fixed-order marginal contribution with zero new predictive configurations. Because it reuses OOS evidence, any resulting `ALPHA_POOL_V1` remains research-only rather than independent confirmation.
