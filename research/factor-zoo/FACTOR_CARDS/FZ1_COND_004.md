# FZ1_COND_004 — Low-volatility factor conditional on market drawdown

- Family: `CONDITIONAL_REGIME`
- Concept: `MARKET_DRAWDOWN_X_LOW_VOL`
- Parameterization group: `FZ1_COND_004` / `SINGLE`
- Abstraction: `CONDITIONAL`
- Definition status: `DRAFT_DESIGN`
- Evaluation stage: `P0_8D`
- Lifecycle: `DISCOVERED`

## Formula

`rank_cs(-vol60) active only when lagged equal_weight_market_drawdown60 is HIGH`

Lookback/input horizon: 60 sessions plus market state.

## Inputs and timing

Raw fields:

- `close`
- `adj_factor`

Derived inputs:

- `adjusted OHLC/returns and rolling statistics exactly as referenced`

Availability: `P0_8D_ONLY_AFTER_STATE_FREEZE`.

## Hypothesis

Direction: `HIGHER_EXPECTED_BETTER`.

The defensive low-volatility dimension may be strongest during broad market stress.

Common-use note: Common daily-bar factor construct; common usage is not empirical validation here.

## Implementation profile

- Expected turnover: `MEDIUM`
- Execution sensitivity: Daily-batch delay, next-open gap, and synthetic cost assumptions.
- Data readiness: `DEFERRED_TO_P0_8D`

Likely related/redundant factors:

- `PG_VOL_REALIZED`
- `FZ1_DTR_004`

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
