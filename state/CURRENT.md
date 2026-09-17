# Current State

Last updated: 2026-09-17

| Field | Value |
| --- | --- |
| Research Controller Repository | `D:\alpha-research-ledger` |
| Execution Repository | `D:\alpha-factory` |
| Last completed execution task | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` / `P0_7C_PASS_WITH_WARNINGS` |
| Current research policy | `FREE FIRST` |
| RD-Agent | `PAUSED_CREDENTIAL_REQUIRED` |
| Old P0-7B Blind | `SUPERSEDED_UNCONSUMED` under ADR-0007 |
| `BLIND_CONSUMED` | `FALSE` |
| Next research design | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` / `DESIGN_READY` / `NOT_YET_EXECUTED` |
| P0-7D input population | Exact 17 frozen P0-7C OOS survivors |
| New predictive configurations in P0-7D | `0` |
| Protected holdout | 2026-01-05 through 2026-09-15 / `UNACCESSED` / `UNCONSUMED` |

## Architecture health

- L1 Data: `FREE_DAILY_V1` remains sufficient for bounded research use; non-PIT, corporate-action, tradability, and historical-delisted gaps remain.
- L2 Alpha Discovery: P0-7C completed 18 Formula and 9 simple-ML configurations. Liquidity, Reversal, and Volatility are priority hypotheses, not proven production Alphas.
- L3 Alpha Evaluation: 17 candidates passed the broad five-fold OOS gate, but weak DSR evidence and material redundancy prevent a statistical-certainty claim.
- L4 Portfolio: top-20 equal weight is Portfolio Baseline V1 after winning all six matched constructor comparisons. A strict Alpha Pool is not yet established.
- L5 Execution: research costs and adjusted-unit fills remain synthetic; production and real-trading readiness remain `NO`.

## P0-7C empirical result

- 27 frozen predictive configurations: 18 Formula and 9 ML.
- Five annual OOS folds covering 2021 through 2025; 135 configuration-fold attempts retained.
- Eight Formula survivors from Liquidity, Reversal, and Volatility.
- Nine ML survivors under the broad gate; three ElasticNet configurations showed positive matched incremental RankIC, while all four LightGBM configurations showed no matched incremental value.
- 17 predictive survivors, material signal/portfolio redundancy, and zero strict Alpha Pool members.
- Top-20 equal weight beat the alternative constructor in all six matched comparisons.
- Maximum DSR probability: `0.4228853062141328`; PBO remained `NOT_JUSTIFIED`.
- Exact reproduction, 97/97 repository tests, and Independent Validator 23 PASS / 7 UNKNOWN / 0 FAIL completed.
- The protected 2026 holdout was not loaded, accessed, or consumed.

## Evidence status

- `EMPIRICAL`: P0-7C results from Alpha Factory protocol commit `95dc8e3c5b895fe7bf47135536e0ed4843b73471`, result commit `a881bd956c70088100f85999e7f0f4f965777a25`, and checkpoint commit `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138`.
- `DOCUMENTED`: Liquidity, Reversal, Volatility, and ElasticNet are priority hypotheses; top-20 equal weight is the new portfolio baseline; P0-7D qualification rules are research-governance decisions.
- `SYNTHETIC`: transaction costs, slippage, adjusted-unit execution, and portfolio fills.
- `UNKNOWN`: production performance, point-in-time validity, full survivorship, authoritative tradability, capacity, and protected-holdout performance.

## Current boundary

P0-7D may qualify only the exact 17 frozen P0-7C survivors using frozen 2021-2025 evidence. It may compute deterministic correlation, overlap, formula-span, equal-weight pool, forward-addition, and leave-one-out diagnostics under its predeclared rules. It may not create a predictive configuration, change a parameter, search an ordering or weighting scheme, access 2026, call RD-Agent/LLMs, purchase data, bind a broker, trade, or make a production claim.
