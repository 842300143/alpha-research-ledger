# Factor Taxonomy V1

## Field capability

Verified against Alpha Factory commit `c37ab3caf0c50c100906503d17d05fd5f78e2e24` and the `FREE_DAILY_V1` Parquet schemas.

| Capability | Actual fields | Status | Boundary |
| --- | --- | --- | --- |
| Daily price/bar | open, high, low, close, preclose | `LIMITED` | action-aware adjusted-price work only on the factor-covered subset |
| Activity | volume, amount, turnover | `READY_WITH_WARNINGS` | raw/relative research allowed; split adjustment and provider semantics remain limited |
| Tradability surrogate | trade_status, suspension_status, st_status | `LIMITED_NON_PIT` | partial empirical coverage; not authoritative historical pre-open state |
| Corporate-action adjustment | adj_factor, event_ratio, factor_change_event | `LIMITED` | complete for the 72-name action-aware research subset, partial for the full dataset |
| Historical universe | listing/delisting current capture | `LIMITED_NON_PIT` | 12 delisted histories recovered; 280 known historical gaps |
| Market composites | equal-weight returns, breadth, aggregate activity derived from the eligible universe | `LIMITED_DERIVED` | not an external market index and inherits universe bias |
| Industry | none | `UNAVAILABLE` | no industry-neutral factors or neutralization |
| Size | total_mv/circ_mv effectively absent | `NOT_READY` | one retained daily_basic row; zero factor budget |
| Value | PE/PB effectively absent | `NOT_READY` | one retained daily_basic row; zero factor budget |
| Quality/fundamentals | no PIT statements/revisions | `UNAVAILABLE` | zero factor budget |
| Authoritative limits/actions | incomplete | `UNAVAILABLE_FOR_PRODUCTION` | research cannot claim executable limit handling or full PIT |

## Included taxonomy

| Family | Subfamilies | Draft definitions | Readiness |
| --- | --- | ---: | --- |
| Momentum | total return, skip-recent, acceleration | 5 | `LIMITED` |
| Reversal | short/medium reversal, shock reversal, run-up exhaustion | 5 | `LIMITED` |
| Trend | moving-average distance, dual-MA, regression, trend significance, persistence | 6 | `LIMITED` |
| Volatility | realized, EWMA, vol-of-vol, idiosyncratic, intraday | 6 | `LIMITED` |
| Downside / Tail Risk | downside deviation, semivariance, drawdown, tail loss | 5 | `LIMITED` |
| Range / ATR / Compression | ATR, range estimators, bandwidth, compression/expansion | 6 | `LIMITED` |
| Liquidity | Amihud, amount level, zero activity, dispersion, return-per-turnover | 6 | `READY_WITH_WARNINGS` |
| Turnover Dynamics | level, persistence, abnormal turnover, slope, variability | 5 | `READY_WITH_WARNINGS` |
| Raw / Relative Volume | level, relative activity, trend, variability, persistence | 5 | `READY_WITH_WARNINGS` |
| Price-Volume Relation | correlation, OBV, confirmation, divergence, money flow | 6 | `LIMITED` |
| Gap / Open-Close Structure | overnight gap, gap persistence/reversal, gap-vs-intraday | 5 | `LIMITED` |
| Intraday Daily-Bar Structure | close location, body, upper/lower shadow | 5 | `LIMITED` |
| Price / N-day Range Position | range position, long position, VWAP position | 5 | `LIMITED` |
| High/Low / Breakout | high and low distance, breakout events, new-high frequency | 5 | `LIMITED` |
| Distribution Shape | skew, kurtosis, sign balance, median deviation, tail asymmetry | 5 | `LIMITED` |
| Market/Beta/Residual Return | beta, residual momentum/reversal, idiosyncratic risk, downside beta | 6 | `LIMITED_DERIVED_MARKET` |
| Rolling Correlation | security return vs equal-weight market/breadth | 4 | `LIMITED_DERIVED_MARKET` |
| Price Efficiency / Trend-to-Noise | efficiency ratio, path efficiency, variance ratio, sign autocorrelation | 5 | `LIMITED` |
| Volatility-Return Relation | volatility momentum, risk-adjusted return, asymmetry, return-vol correlation | 4 | `LIMITED` |
| Conditional / Regime Descriptive | state-conditioned momentum, reversal, breakout, low-vol | 4 | `DEFERRED_TO_P0_8D` |
| **Total** | 20 families | **103** | 99 atomic/transformed + 4 conditional |

## Explicit exclusions

- Size, Value, Quality, Profitability, Investment, Accruals, analyst, text, event, options, short interest, order-book, tick/microstructure, ownership, and industry factors are `UNAVAILABLE` or `NOT_READY`.
- Daily-bar data cannot support genuine intraday timing, order imbalance, spread, queue, or trade-sign factors.
- `amount / volume` may be used only as a research VWAP proxy after unit validation; it is not a certified exchange VWAP.
- Current-capture listing/ST/suspension facts are eligibility warnings, not predictive factor inputs.

## Count discipline

The 103 definitions contain approximately 90 concepts. Repeated definitions occur only for declared short/medium/long mechanisms such as return horizon, realized volatility horizon, or range position. The registry records a `parameterization_group` so variant count and concept count remain separate. No 5,6,7...60 sweep is present.
