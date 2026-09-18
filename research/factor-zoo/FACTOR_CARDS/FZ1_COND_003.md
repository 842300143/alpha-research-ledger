# FZ1_COND_003 — Breakout conditional on volume expansion

- Family: `CONDITIONAL_REGIME`
- Concept: `VOLUME_CONFIRMATION_X_BREAKOUT`
- Parameterization group: `FZ1_COND_003` / `SINGLE`
- Abstraction: `CONDITIONAL`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8D`
- Lifecycle: `DISCOVERED`

## Formula

`rank_cs(distance_to_prior_high60) * rank_cs(relative_volume) after parent archetype freeze`

Lookback/input horizon: 65 sessions.

## Inputs and timing

Raw fields:

- `high`
- `close`
- `volume`
- `adj_factor`

Derived inputs:

- `adjusted OHLC/returns and rolling statistics exactly as referenced`

Availability: `P0_8D_ONLY_AFTER_STATE_FREEZE`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

A breakout with expanding activity may contain more information than either parent alone.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `VERY_HIGH`
- Execution sensitivity: Daily-batch delay, next-open gap, and synthetic cost assumptions.
- Data readiness: `DEFERRED_TO_P0_8D`

Likely related/redundant factors:

- `FZ1_BRK_002`
- `FZ1_VOLM_003`

PIT/lookahead risks:

- `PARTIAL_ACTION_FACTOR_COVERAGE_ACTION_AWARE_SUBSET_ONLY`
- `CURRENT_CAPTURE_NON_PIT_UNIVERSE`
- `T_PLUS_1_EXECUTION_ONLY`
- `RAW_VOLUME_SPLIT_AND_PROVIDER_SEMANTICS`
- `PARTIAL_HISTORICAL_TRADABILITY_STATE`
- `CURRENT_CAPTURE_NON_PIT_UNIVERSE`

Provenance:

- `P0_8_CONDITIONAL_PROTOTYPE`

## Planned tests

- `P0_8A_SYNTHETIC_FORMULA_AND_LAG_FIXTURE`
- `P0_8A_FULL_WINDOW_MISSINGNESS_AND_TIMING_CHECK`
- `P0_8D_PARENT_AND_PARENT_COMBINATION_RESIDUAL_TEST`
- `P0_8D_INCREMENTAL_COST_STABILITY_AND_REGIME_TEST`
