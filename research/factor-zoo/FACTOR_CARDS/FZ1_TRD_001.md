# FZ1_TRD_001 — Price above SMA 20

- Family: `TREND`
- Concept: `PRICE_TO_MOVING_AVERAGE`
- Parameterization group: `PG_TREND_PRICE_SMA` / `SHORT`
- Abstraction: `ATOMIC`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8B`
- Lifecycle: `DISCOVERED`

## Formula

`adj_close[t] / mean(adj_close[t-19:t]) - 1`

Lookback/input horizon: 20 sessions.

## Inputs and timing

Raw fields:

- `close`
- `adj_factor`

Derived inputs:

- `adjusted OHLC/returns and rolling statistics exactly as referenced`

Availability: `AFTER_T_CLOSE; EARLIEST_T_PLUS_1_OPEN`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

A price above its trailing equilibrium may indicate a persistent trend.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `HIGH`
- Execution sensitivity: Daily-batch delay, next-open gap, and synthetic cost assumptions.
- Data readiness: `LIMITED`

Likely related/redundant factors:

- `PG_MOM_TOTAL_RETURN`
- `FZ1_POS_005`

PIT/lookahead risks:

- `PARTIAL_ACTION_FACTOR_COVERAGE_ACTION_AWARE_SUBSET_ONLY`
- `CURRENT_CAPTURE_NON_PIT_UNIVERSE`
- `T_PLUS_1_EXECUTION_ONLY`

Provenance:

- `STANDARD_TREND`
- `P0_7C_TREND_LINEAGE`

## Planned tests

- `P0_8A_SYNTHETIC_FORMULA_AND_LAG_FIXTURE`
- `P0_8A_FULL_WINDOW_MISSINGNESS_AND_TIMING_CHECK`
- `P0_8B_PRIMARY_AND_FIXED_NORMALIZATION_IC_RANKIC`
- `P0_8B_FOLD_SIGN_STABILITY_AND_DECAY_5_20_60`
- `P0_8B_TOP20_TURNOVER_COST_2X_COST_AND_DRAWDOWN`
- `P0_8B_COVERAGE_MISSINGNESS_REGIME_AND_FDR`
- `P0_8C_CORRELATION_OVERLAP_CLUSTER_AND_RESIDUAL_INFORMATION`
