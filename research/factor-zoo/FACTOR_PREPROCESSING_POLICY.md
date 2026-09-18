# Factor Preprocessing Policy

## Primary atomic-factor view

1. Compute the exact raw signed formula on the frozen eligible universe.
2. Replace positive/negative infinity with missing; do not impute atomic-factor values.
3. Require the full card lookback and all mandatory endpoints.
4. On each signal date, average-tie percentile-rank the available cross-section.
5. Center the rank as `rank_pct - 0.5`. Higher is the predeclared favorable direction.

This rank view is the primary comparison scale. It avoids factor-specific scaling choices and does not fit to outcomes.

## Fixed robustness view

One secondary normalization is allowed for every eligible atomic factor: within-date winsorize raw values at the 1st/99th percentiles, then cross-sectional z-score with population standard deviation. Require at least 30 non-missing names and nonzero dispersion. This is a robustness view, not a second hypothesis or a chance to choose the better presentation.

No factor may select its own winsorization, transform, rank method, or sign after results. Heavy-tailed formulas must encode their transform in the frozen definition itself.

## Missingness

- Atomic evaluation: missing factor values are excluded, never median-filled.
- Coverage, missing rate, missing-by-year, missing-by-symbol, and missing-by-regime are mandatory outputs.
- A date with fewer than 60 eligible securities or less than 60% of the reference eligible rows is `UNKNOWN_INSUFFICIENT_COVERAGE` for the primary research subset.
- ML stages may use training-only median imputation with an explicit missingness indicator, matching the established Generation-1 discipline. Imputation values are fit within each training fold only.

## Minimum history

Every definition requires its full declared lookback. No shortened rolling window or `min_periods` relaxation is allowed. The maximum V1 lookback is 252 sessions. Warmup rows have no signal and do not count as failed coverage.

## Eligibility

- Use the frozen action-aware P0-8 universe derived from development-period metadata only.
- Require positive adjustment factors for every adjusted-price observation used by the formula and label.
- Enforce listing/lifecycle, positive price, volume/amount requirements where declared, and the timing contract.
- Do not infer eligibility from future dates or the protected holdout.

## Scaling and adjustment

- Price factors use adjusted OHLC derived consistently from raw OHLC and `adj_factor`.
- Volume and amount remain raw activity measures under the feature-readiness warning. Relative-within-security transforms are preferred; split sensitivity must be recorded.
- Turnover may be used under provider-normalization warnings and must not be interpreted as shares-outstanding-neutral Size.
- `amount / volume` is a research VWAP proxy only after unit validation; zero volume denies the observation.

## Neutralization

- Industry neutralization: `UNAVAILABLE`, because no reliable historical industry classification is present.
- Size neutralization: `UNAVAILABLE`, because daily market-cap history is not ready.
- Market adjustment: `LIMITED_DERIVED_MARKET`; equal-weight eligible-universe returns may support beta/residual definitions, but the composite inherits current-capture and survivorship limitations.

No residual Size/industry claim may be made. Cross-sectional demeaning/ranking is not called neutralization.

## ML input policy

P0-8F may consume only P0-8C cluster representatives and separately accepted P0-8D interactions selected by frozen rules. It may not ingest all 103 raw definitions. Preprocessing, imputation, scaling, and input IDs must be bound before model results.
