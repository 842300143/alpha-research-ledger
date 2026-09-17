# Current State

Last updated: 2026-09-16

| Field | Value |
| --- | --- |
| Research Controller Repository | `D:\alpha-research-ledger` |
| Execution Repository | `D:\alpha-factory` |
| Last completed execution task | `P0_6E_FREE_DATA_EXPANSION_V1` / `P0_6E_PASS_WITH_WARNINGS` |
| Current research policy | `FREE FIRST` |
| RD-Agent | `PAUSED_CREDENTIAL_REQUIRED` |
| Old P0-7B Blind | `SUPERSEDED_UNCONSUMED` under ADR-0007 |
| `BLIND_CONSUMED` | `FALSE` |
| Next research design | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` / `DESIGN_READY` / `NOT_YET_EXECUTED` |
| P0-7C dataset | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` |
| P0-7C protected holdout | 2026-01-05 through 2026-09-15 / 171 sessions / `UNACCESSED_FOR_ALPHA_RESEARCH` |

## Architecture health

- L1 Data: P0-6E complete for bounded research use; non-PIT, corporate-action, and historical-delisted gaps remain.
- L2 Alpha Discovery: P0-7C Formula and simple-ML protocol is design-ready on a frozen action-aware subset.
- L3 Alpha Evaluation: five annual walk-forward OOS folds, immutable experiment accounting, and a new protected 2026 holdout are designed.
- L4 Portfolio: P0-7C compares top-20 equal weight with one simple cost/risk-aware constructor.
- L5 Execution: model China-market constraints and progress through Shadow before later broker integration.

## Evidence status

- P0-6E dataset, quality, coverage, survivorship, resource, and test claims are `EMPIRICAL` from Alpha Factory commits `69be29e41ddfdf815685f64d697465032c4a9891` and `52c6a7eb506bb8848f1a643c469978d28804738c`.
- Volume and ML readiness classifications are `DOCUMENTED` design interpretations of the empirical field coverage; no predictive result is claimed.
- P0-7C protocol, budgets, and holdout treatment are `DOCUMENTED` research-governance decisions. All future Alpha performance remains `UNKNOWN`.
- Production readiness remains `NO`; paid data is not required now.
