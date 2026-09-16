# L4 Portfolio Engine

## Objective

Translate accepted alphas into robust, feasible, cost-aware holdings.

## Components

- Alpha ensemble and dynamic weighting rules.
- Exposure and covariance risk model.
- Transaction-cost-aware optimization.
- Liquidity, turnover, concentration, industry, style, and position constraints.
- Regime allocation that is validated without hindsight leakage.

## Current weakness

Portfolio construction is a weak layer. Research must test whether a candidate adds incremental portfolio value rather than reward isolated backtest strength.

## Design principle

Prefer diversified contributions from low-correlated signals. Explicitly record cases where individually predictive signals become redundant or destructive in combination.
