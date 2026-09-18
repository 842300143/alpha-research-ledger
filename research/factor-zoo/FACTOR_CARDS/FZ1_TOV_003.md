# FZ1_TOV_003 — Signed abnormal turnover contraction 5/prior60

- Family: `TURNOVER_DYNAMICS`
- Concept: `SIGNED_TURNOVER_INNOVATION`
- Parameterization group: `FZ1_TOV_003` / `SINGLE`
- Abstraction: `TRANSFORMED`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8B`
- Lifecycle: `DISCOVERED`

## Formula

`-log((mean(turnover,t-4:t)+1e-12)/(mean(turnover,t-64:t-5)+1e-12))`

Lookback/input horizon: 65 sessions.

## Inputs and timing

Raw fields:

- `turnover`

Derived inputs:

- `adjusted OHLC/returns and rolling statistics exactly as referenced`

Availability: `AFTER_T_CLOSE; EARLIEST_T_PLUS_1_OPEN`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

Recent attention contraction may be favorable if abnormal activity contains transitory demand.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `HIGH`
- Execution sensitivity: Daily-batch delay, next-open gap, and synthetic cost assumptions.
- Data readiness: `READY_WITH_WARNINGS`

Likely related/redundant factors:

- `FZ1_TOV_002`
- `FZ1_VOLM_003`

PIT/lookahead risks:

- `RAW_VOLUME_SPLIT_AND_PROVIDER_SEMANTICS`
- `PARTIAL_HISTORICAL_TRADABILITY_STATE`
- `CURRENT_CAPTURE_NON_PIT_UNIVERSE`

Provenance:

- `P07E_LIQ_SIGNED_ABTURN_5V60`

## Planned tests

- `P0_8A_SYNTHETIC_FORMULA_AND_LAG_FIXTURE`
- `P0_8A_FULL_WINDOW_MISSINGNESS_AND_TIMING_CHECK`
- `P0_8B_PRIMARY_AND_FIXED_NORMALIZATION_IC_RANKIC`
- `P0_8B_FOLD_SIGN_STABILITY_AND_DECAY_5_20_60`
- `P0_8B_TOP20_TURNOVER_COST_2X_COST_AND_DRAWDOWN`
- `P0_8B_COVERAGE_MISSINGNESS_REGIME_AND_FDR`
- `P0_8C_CORRELATION_OVERLAP_CLUSTER_AND_RESIDUAL_INFORMATION`
