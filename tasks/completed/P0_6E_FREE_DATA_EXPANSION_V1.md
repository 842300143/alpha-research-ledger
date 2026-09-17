# P0_6E_FREE_DATA_EXPANSION_V1

- Task ID: `P0_6E_FREE_DATA_EXPANSION_V1`
- Status: `P0_6E_PASS_WITH_WARNINGS` / `COMPLETE`
- Execution repository: `D:\alpha-factory`
- Research repository: `D:\alpha-research-ledger`
- Controller authorization commit: `67591334d7289c6d6685b6538568241591512f2b`
- Execution start commit: `cf45be007afd168d8ad40746cfe1b16c3e0d2360`
- Result commit: `69be29e41ddfdf815685f64d697465032c4a9891`
- Completion checkpoint commit: `52c6a7eb506bb8848f1a643c469978d28804738c`

## Goal

Expand the free-data research foundation into a multi-year, historical-universe-aware dataset suitable for a bounded next Alpha iteration.

## Empirical result

`FREE_DAILY_V1` contains 5,587,828 daily price rows for 3,207 Shanghai/Shenzhen main-board securities over 1,870 trading sessions from 2019-01-02 through 2026-09-15. It covers all 3,195 current securities and 12 historical-delisted securities. Its immutable dataset hash is `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`.

- Hard data-quality failures: 0.
- Current-security price coverage: 100%.
- Known historical-only master records without recovered price history: 280.
- Survivorship-aware membership differences: 595,813 security-date candidates across 1,863 dates.
- Verification: 85/85 repository tests, 27/27 data probes, 16/16 Shadow probes, and 3/3 offline regressions passed.
- No Alpha experiment, protected Blind access, RD-Agent/LLM call, payment, broker action, or trade occurred.

## Feature-readiness review

| Family | Status | Evidence and permitted scope |
| --- | --- | --- |
| Momentum | `LIMITED` | Corporate-action-clean returns cover only the factor-covered subset. |
| Reversal | `LIMITED` | Raw ex-date jumps can mimic reversal; use only a frozen factor-covered subset. |
| Trend | `LIMITED` | Long raw series have unresolved action discontinuities; action-aware subset only. |
| Volatility | `LIMITED` | Unadjusted jumps inflate volatility; action-aware subset or predeclared robust diagnostics only. |
| Liquidity | `READY` | Raw amount/volume research is supported with missing-day and suspension controls. Forward-return evaluation still requires action-clean labels. |
| Volume | `READY` | Raw volume/amount activity features are supported with missing/suspension controls; adjusted or shares-outstanding-normalized volume remains limited. |
| Size | `NOT_READY` | Only one retained `daily_basic` row; no usable cross-sectional history. |
| Value | `NOT_READY` | Only one retained `daily_basic` row; no usable PE/PB history. |
| Quality | `NOT_READY` | No point-in-time financial-statement or revision history. |
| Multi-factor | `LIMITED` | Only predeclared combinations of eligible price-volume/liquidity inputs; Size, Value, and Quality cannot enter. |
| Machine Learning | `LIMITED` | Simple models are feasible only on the same eligible feature set and action-clean label universe; ML does not repair unavailable inputs. |

The statuses for Volume and Machine Learning are `DOCUMENTED` interpretations of the empirical field coverage and family-specific readiness contract; they are not claims of predictive performance.

## Warnings retained

- Dataset classification is `RESEARCH_ONLY_CURRENT_HISTORICAL_CAPTURE_NON_PIT`.
- Adjustment, ST, and suspension evidence covers 83 BaoStock-priced symbols and is unknown elsewhere.
- The historical master is a current capture, not proof that each fact was knowable at each historical open.
- Historical limits and complete corporate-action evidence are unavailable.
- Production readiness remains `NO`; paid data is not required now.

## Authoritative Alpha Factory evidence

- `reports/P0_6E_FREE_DATA_EXPANSION_REPORT.md`
- `reports/P0_6E_FREE_DATA_COVERAGE_MATRIX.md`
- `reports/P0_6E_SURVIVORSHIP_AUDIT.md`
- `reports/P0_6E_DATA_QUALITY_REPORT.md`
- `reports/P0_6E_RESOURCE_REPORT.md`
- `reports/P0_6E_CHECKPOINT.json`
- `research/free_daily_v1/DATASET_MANIFEST.json`
- `research/free_daily_v1/FEATURE_READINESS.json`
- `reports/P0_7C_LONG_HORIZON_ALPHA_V1_RECOMMENDATION.md`

## Decision changed

The data foundation is sufficient to design and later execute a bounded long-horizon Alpha protocol on a frozen action-aware subset. A broad data-repair phase is not the default next step. Full-universe action-clean research, fundamentals, and production claims remain blocked.
