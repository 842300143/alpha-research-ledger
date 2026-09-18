# Factor Timing Contract

## Primary rule

Every P0-8 signal using session `t` OHLC, volume, amount, turnover, trade-status, or adjustment information is considered available only after the official close of `t` and successful daily-batch ingestion. The earliest permitted portfolio entry is the next eligible session open, `t+1`. Same-close execution is prohibited.

This conservative contract applies even to formulas that could theoretically be known at `t` open (for example an overnight gap). `FREE_DAILY_V1` is a daily batch dataset and does not certify an intraday publication timestamp or actionable opening auction state.

## Derived-input timing

- Rolling windows end at and include `t`; they never include `t+1`.
- Adjusted OHLC uses only the adjustment-factor convention frozen in the dataset and must pass the action-path gate. Back-adjustment can encode later corporate-action knowledge if reconstructed carelessly; implementation must use the already frozen factor convention and deny unknown factor paths.
- Equal-weight market return, breadth, aggregate activity, and other market composites for `t` use only the eligible cross-section at `t` and become available after `t` close.
- Cross-sectional rank/z-score at `t` uses only eligible security observations from `t` and is available after `t` close.
- Training labels and model preprocessing may not cross fold boundaries. Outcome labels enter only after their full forward horizon has elapsed.

## Execution and label contract

- Primary outcome: unchanged 20-session cross-sectional-median-relative adjusted return from `t+1` eligible open to `t+20` adjusted close.
- Diagnostic decay horizons: 5, 20, and 60 sessions; each exit must remain inside its fold/tranche.
- Entry and exit require positive adjusted prices and the frozen tradability surrogate. Missing or unknown state is not silently eligible.
- T+1, daily limits, queue position, and authoritative historical suspension/ST state are not fully modeled. Portfolio evidence remains synthetic and research-only.

## Universe contract

- Eligibility uses the frozen action-aware subset and only historical effective-date evidence available under the dataset contract.
- Current-vs-future membership leakage must be denied where detectable. Current-capture lifecycle evidence remains a non-PIT surrogate and is never called certified PIT.
- Delisted and absent-history gaps remain a survivorship limitation. No factor may infer an unavailable security's value or backfill current membership.

## Factor-card timing values

| Value | Meaning |
| --- | --- |
| `AFTER_T_CLOSE; EARLIEST_T_PLUS_1_OPEN` | Default and primary contract |
| `THEORETICALLY_AT_T_OPEN; BATCH_CONTRACT_T_PLUS_1_OPEN` | Gap/open-only formula still delayed under V1 |
| `AFTER_T_CLOSE_DERIVED_MARKET; EARLIEST_T_PLUS_1_OPEN` | Uses eligible-universe composite at `t` |
| `P0_8D_ONLY_AFTER_STATE_FREEZE` | Conditional definition unavailable until structure/archetype state is frozen |

Any factor whose timing cannot be mapped to one of these is `LIMITED_TIMING_UNKNOWN` and cannot become `SURVIVED`.

## Prohibited timing shortcuts

- same-close fill from close/high/low/volume/amount/turnover;
- future-adjusted membership or later-known ST/suspension status;
- forward-filled future observation, label, or corporate-action factor;
- ranking with securities that were ineligible on the signal date;
- using 2026 values for warmup, coverage, normalization, regime thresholds, or any other purpose.
