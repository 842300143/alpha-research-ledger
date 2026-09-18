# FZ1_GAP_001 — Negative overnight gap 1

- Family: `GAP_OPEN_CLOSE`
- Concept: `OVERNIGHT_GAP_REVERSAL`
- Parameterization group: `FZ1_GAP_001` / `SINGLE`
- Abstraction: `ATOMIC`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8B`
- Lifecycle: `DISCOVERED`

## Formula

`-(adj_open[t]/adj_close[t-1]-1)`

Lookback/input horizon: 2 sessions.

## Inputs and timing

Raw fields:

- `open`
- `close`
- `adj_factor`

Derived inputs:

- `adjusted OHLC/returns and rolling statistics exactly as referenced`

Availability: `THEORETICALLY_AT_T_OPEN; BATCH_CONTRACT_T_PLUS_1_OPEN`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

Overnight price pressure may partially reverse after the open.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `VERY_HIGH`
- Execution sensitivity: Opening auction gap and t+1 batch delay; cannot trade the observed t open in V1.
- Data readiness: `LIMITED`

Likely related/redundant factors:

- `FZ1_GAP_003`
- `FZ1_REV_001`

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
