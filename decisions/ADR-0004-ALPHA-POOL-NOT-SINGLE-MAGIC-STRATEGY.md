# ADR-0004: Build an Alpha Pool, Not One Magic Strategy

- Status: Accepted
- Date: 2026-09-16

## Context

Single strategies can be unstable, crowded, regime-dependent, or overfit. Portfolio construction benefits from signals whose errors and decay patterns are not identical.

## Decision

Build a pool of weak but predictive, stable, low-correlated, post-cost usable Alpha signals. Evaluate marginal contribution to the pool rather than celebrate isolated backtest performance.

## Evidence / rationale

- `DOCUMENTED`: this is the controller's long-term research principle.
- Finance and diversification reasoning favors complementary sources of return.
- No empirical claim is made that any current candidate satisfies the criteria.

## Alternatives

- Concentrate on the best single backtest.
- Combine every positive candidate without correlation or cost controls.
- Use only one factor family for interpretability.

## Consequences

Evaluation must measure correlation, stability, decay, turnover, and incremental portfolio value. Negative or redundant candidates remain valuable evidence.

## Future revisit condition

Revisit if robust empirical evidence shows concentration is structurally superior under the project's risk, cost, and capacity constraints.
