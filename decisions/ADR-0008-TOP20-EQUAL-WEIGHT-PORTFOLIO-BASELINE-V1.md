# ADR-0008: Adopt Top-20 Equal Weight as Portfolio Baseline V1

- Status: Accepted
- Date: 2026-09-17

## Context

P0-7C applied top-20 equal weight and a rank/inverse-volatility buffered alternative to the same six frozen score streams under matched entry, costs, and execution assumptions.

## Decision

Adopt top-20 equal weight as Portfolio Baseline V1. Future portfolio constructors must demonstrate incremental value against it on identical frozen score streams and costs before promotion.

## Evidence / rationale

- `EMPIRICAL_RESEARCH_ONLY`: top-20 equal weight beat the alternative on frozen-cost net return in all six matched comparisons.
- Mean frozen-cost net return was 0.7595 for equal weight and 0.6352 for the alternative.
- The alternative incurred greater average cost drag and did not improve the observed return/risk tradeoff sufficiently.
- `SYNTHETIC`: costs, slippage, adjusted-unit lots, and fills do not establish production executability or capacity.

## Alternatives

- Keep both constructors co-equal.
- Promote the more complex constructor because it includes risk and turnover controls.
- Search additional constructor settings after seeing P0-7C results.

## Consequences

P0-7D uses only top-20 equal weight for matched portfolio qualification. Complexity receives no presumption of superiority. This baseline is research-only and may be superseded by a predeclared matched comparison.

## Future revisit condition

Revisit when one fixed constructor, frozen before comparison, improves matched post-cost return/risk, drawdown, and implementation efficiency without weakening predictive or data-integrity controls.
