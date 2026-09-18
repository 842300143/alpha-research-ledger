# FZ1_COND_002 — Momentum conditional on low-volatility state

- Family: `CONDITIONAL_REGIME`
- Concept: `VOLATILITY_STATE_X_MOMENTUM`
- Parameterization group: `FZ1_COND_002` / `SINGLE`
- Abstraction: `CONDITIONAL`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8D`
- Lifecycle: `DISCOVERED`

## Formula

`rank_cs(ret60) active only when archetype_volatility_state is LOW`

Lookback/input horizon: parent lookbacks plus training-fitted state.

## Inputs and timing

Raw fields:

- `close`
- `adj_factor`

Derived inputs:

- `adjusted OHLC/returns and rolling statistics exactly as referenced`

Availability: `P0_8D_ONLY_AFTER_STATE_FREEZE`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

Momentum may persist more reliably when stock-specific or market volatility is subdued.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `MEDIUM`
- Execution sensitivity: Daily-batch delay, next-open gap, and synthetic cost assumptions.
- Data readiness: `DEFERRED_TO_P0_8D`

Likely related/redundant factors:

- `PG_MOM_TOTAL_RETURN`
- `VOLATILITY_ARCHETYPE_TBD`

PIT/lookahead risks:

- `PARTIAL_ACTION_FACTOR_COVERAGE_ACTION_AWARE_SUBSET_ONLY`
- `CURRENT_CAPTURE_NON_PIT_UNIVERSE`
- `T_PLUS_1_EXECUTION_ONLY`
- `DERIVED_EQUAL_WEIGHT_MARKET_INHERITS_UNIVERSE_BIAS`

Provenance:

- `P0_8_CONDITIONAL_PROTOTYPE`

## Planned tests

- `P0_8A_SYNTHETIC_FORMULA_AND_LAG_FIXTURE`
- `P0_8A_FULL_WINDOW_MISSINGNESS_AND_TIMING_CHECK`
- `P0_8D_PARENT_AND_PARENT_COMBINATION_RESIDUAL_TEST`
- `P0_8D_INCREMENTAL_COST_STABILITY_AND_REGIME_TEST`
