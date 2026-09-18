# FZ1_VOLM_005 — Volume autocorrelation 60

- Family: `RAW_RELATIVE_VOLUME`
- Concept: `VOLUME_PERSISTENCE`
- Parameterization group: `FZ1_VOLM_005` / `SINGLE`
- Abstraction: `TRANSFORMED`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8B`
- Lifecycle: `DISCOVERED`

## Formula

`corr(log1p(volume[s]),log1p(volume[s-1])) over s=t-58:t`

Lookback/input horizon: 60 sessions.

## Inputs and timing

Raw fields:

- `volume`

Derived inputs:

- `lagged log-volume series`

Availability: `AFTER_T_CLOSE; EARLIEST_T_PLUS_1_OPEN`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

Persistent activity may distinguish stable investor participation from isolated bursts.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `LOW`
- Execution sensitivity: Daily-batch delay, next-open gap, and synthetic cost assumptions.
- Data readiness: `READY_WITH_WARNINGS`

Likely related/redundant factors:

- `FZ1_TOV_002`
- `FZ1_VOLM_004`

PIT/lookahead risks:

- `RAW_VOLUME_SPLIT_AND_PROVIDER_SEMANTICS`
- `PARTIAL_HISTORICAL_TRADABILITY_STATE`
- `CURRENT_CAPTURE_NON_PIT_UNIVERSE`

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
