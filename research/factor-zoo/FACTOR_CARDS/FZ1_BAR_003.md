# FZ1_BAR_003 — Body-to-range conviction 20

- Family: `INTRADAY_DAILY_BAR`
- Concept: `CANDLE_BODY_CONVICTION`
- Parameterization group: `FZ1_BAR_003` / `SINGLE`
- Abstraction: `ATOMIC`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8B`
- Lifecycle: `DISCOVERED`

## Formula

`mean((adj_close-adj_open)/(adj_high-adj_low) over 20)`

Lookback/input horizon: 20 sessions.

## Inputs and timing

Raw fields:

- `open`
- `high`
- `low`
- `close`
- `adj_factor`

Derived inputs:

- `adjusted OHLC/returns and rolling statistics exactly as referenced`

Availability: `AFTER_T_CLOSE; EARLIEST_T_PLUS_1_OPEN`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

Consistent signed candle bodies may indicate directional conviction rather than noisy ranges.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `HIGH`
- Execution sensitivity: Daily-batch delay, next-open gap, and synthetic cost assumptions.
- Data readiness: `LIMITED`

Likely related/redundant factors:

- `FZ1_BAR_001`
- `FZ1_TRD_006`

PIT/lookahead risks:

- `PARTIAL_ACTION_FACTOR_COVERAGE_ACTION_AWARE_SUBSET_ONLY`
- `CURRENT_CAPTURE_NON_PIT_UNIVERSE`
- `T_PLUS_1_EXECUTION_ONLY`

Provenance:

- `P0_8_CANONICAL_DAILY_BAR_TAXONOMY`

## Planned tests

- `P0_8A_SYNTHETIC_FORMULA_AND_LAG_FIXTURE`
- `P0_8A_FULL_WINDOW_MISSINGNESS_AND_TIMING_CHECK`
- `P0_8B_PRIMARY_AND_FIXED_NORMALIZATION_IC_RANKIC`
- `P0_8B_FOLD_SIGN_STABILITY_AND_DECAY_5_20_60`
- `P0_8B_TOP20_TURNOVER_COST_2X_COST_AND_DRAWDOWN`
- `P0_8B_COVERAGE_MISSINGNESS_REGIME_AND_FDR`
- `P0_8C_CORRELATION_OVERLAP_CLUSTER_AND_RESIDUAL_INFORMATION`
