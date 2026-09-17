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

Portfolio construction remains a weak layer. P0-7C found that top-20 equal weight beat the rank/inverse-volatility buffered alternative in all six matched comparisons. Under ADR-0008, top-20 equal weight is Portfolio Baseline V1 until a more complex constructor proves incremental value.

## Design principle

Prefer diversified contributions from low-correlated signals. Explicitly record cases where individually predictive signals become redundant or destructive in combination.

P0-7D uses equal-weight combinations of within-date percentile-ranked scores and one fixed top-20 equal-weight constructor. It searches neither pool weights nor constructor settings.
