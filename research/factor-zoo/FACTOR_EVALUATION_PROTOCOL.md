# P0-8B Factor Evaluation Protocol

## Scope

Evaluate the 99 P0-8A-frozen atomic/transformed definitions. The four conditional prototypes remain sealed until P0-8D. P0-8B does not add formulas, change signs, create neighboring horizons, tune portfolio parameters, or access 2026.

## Staged sample

- Stage 1 `R1_STRUCTURE_RESEARCH`: WF1-WF3, test years 2021-2023.
- Stage 2 `R2_INTERNAL_REUSE_VALIDATION`: WF4-WF5, test years 2024-2025, opened once only after P0-8C archetype rules and P0-8D interaction registry are frozen.
- Both stages are selection-contaminated research evidence. Stage 2 is not independent confirmation.

P0-8B computes Stage-1 atomic evidence. It reserves exactly 99 x 3 = 297 factor-fold attempts. A failed, denied, invalid, or insufficient-coverage attempt consumes its slot. The later Stage-2 registry count is `number_of_frozen_survivors x 2`; no rejected definition is replaced.

## Required factor-level outputs

For the primary rank view and fixed robustness view retain:

- daily Pearson IC and Spearman RankIC;
- mean and median daily IC/RankIC;
- RankIC standard deviation and ICIR/RankICIR where observation assumptions are stated;
- sign hit rate, year/fold values, minimum fold, dispersion, and leave-one-fold-out range;
- 5-, 20-, and 60-session decay profiles;
- gross and modeled-cost top-20 equal-weight behavior;
- 2x-cost stress, turnover, cost drag, Sharpe, maximum drawdown, and worst-fold drawdown;
- breadth/coverage, missingness, security/date counts, and concentration;
- descriptive market-direction, volatility, liquidity, and breadth regime cells;
- timing/PIT/data-readiness verdict and Validator output.

Standalone return is one dimension and never the sole screen.

## Primary lifecycle gates

All thresholds are applied on Stage 1 and are frozen before results:

1. three terminal fold records and no integrity/Validator failure;
2. at least 60 securities and 60% reference-row coverage per sufficient fold;
3. mean RankIC >= 0.005 in the predeclared direction;
4. at least two of three positive fold RankIC values;
5. moving-block-bootstrap 95% interval for mean daily RankIC does not have an upper bound <= 0;
6. positive frozen-cost top-20 net return and positive 2x-cost net return;
7. no fold frozen-cost net return below -0.20;
8. primary and fixed robustness-view RankIC signs agree;
9. no unresolved timing, leakage, or protected-data violation.

Passing these gates yields `EVALUATED_CANDIDATE`, not final survival. Multiple-testing, stability, cost, and structure disposition are then applied.

## Lifecycle disposition

- `SURVIVED`: primary gates, multiplicity control, cost, and stability pass; not yet proven independent.
- `UNSTABLE`: direction or fold/normalization stability fails.
- `REDUNDANT`: P0-8C finds no material residual information relative to its cluster representative.
- `COST_KILLED`: predictive gate passes but frozen-cost or 2x-cost behavior fails.
- `REGIME_SPECIFIC`: aggregate gate fails or is weak, but a predeclared sufficient regime is stable; cannot enter the atomic main pool without P0-8D treatment.
- `REJECTED`: predictive/multiplicity gate fails without a narrower predeclared status.
- `UNKNOWN_INSUFFICIENT_COVERAGE`, `DENIED_DATA_GATE`, or `INVALID_IMPLEMENTATION`: retained terminal attempt state; no budget recycling.

## Regime diagnostics

Regimes are descriptive in P0-8B and cannot select a factor or threshold. Thresholds are fit on training history only. A cell needs at least 20 daily observations and the factor's minimum breadth. A regime result cannot rescue a rejected aggregate factor except to nominate a predeclared P0-8D conditional hypothesis under the separate interaction budget.

## Portfolio diagnostic

Use only `TOP20_EQUAL_WEIGHT`, 20-session rebalance/holding, and the frozen Generation-1 synthetic cost model for comparability. Portfolio behavior is diagnostic of implementability; it does not convert a weak IC result into survival. No constructor search is permitted.

## Decay

The 20-session outcome is primary. Five- and 60-session results are fixed diagnostics. No factor may change its claimed horizon after observing decay. Monotonic or persistent decay is descriptive; sign reversal must be retained and may produce `UNSTABLE`.

## Outputs

- immutable evaluation manifest and registry;
- 297 Stage-1 attempt records;
- factor metric table, fold table, decay table, cost table, regime table, and missingness table;
- multiple-testing artifact with shared-null permutation identifiers;
- complete lifecycle registry including failures;
- P0-8C handoff containing score streams and daily IC series, not rankings from protected data.
