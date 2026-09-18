# FZ1_COND_001 — Reversal conditional on high-liquidity state

- Family: `CONDITIONAL_REGIME`
- Concept: `LIQUIDITY_STATE_X_REVERSAL`
- Parameterization group: `FZ1_COND_001` / `SINGLE`
- Abstraction: `CONDITIONAL`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8D`
- Lifecycle: `DISCOVERED`

## Formula

`rank_cs(-ret20) active only when archetype_liquidity_state is HIGH`

Lookback/input horizon: parent lookbacks plus training-fitted state.

## Inputs and timing

Raw fields:

- `close`
- `amount`
- `volume`
- `turnover`
- `adj_factor`

Derived inputs:

- `adjusted OHLC/returns and rolling statistics exactly as referenced`

Availability: `P0_8D_ONLY_AFTER_STATE_FREEZE`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

Reversal may be more executable and less distress-driven in high-liquidity states.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `HIGH`
- Execution sensitivity: Daily-batch delay, next-open gap, and synthetic cost assumptions.
- Data readiness: `DEFERRED_TO_P0_8D`

Likely related/redundant factors:

- `PG_REV_TOTAL_RETURN`
- `LIQUIDITY_ARCHETYPE_TBD`

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
