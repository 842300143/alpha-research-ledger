# Current State

Last updated: 2026-09-17

| Field | Value |
| --- | --- |
| Research Controller Repository | `D:\alpha-research-ledger` |
| Execution Repository | `D:\alpha-factory` |
| Last completed execution task | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` / `P0_7D_PASS_WITH_WARNINGS` |
| Current research policy | `FREE FIRST` |
| RD-Agent | `PAUSED_CREDENTIAL_REQUIRED` |
| Old P0-7B Blind | `SUPERSEDED_UNCONSUMED` under ADR-0007 |
| Protected 2026 holdout | `UNACCESSED / UNCONSUMED` |
| Research anchor / `ALPHA_POOL_V1` | `P07C_ML_ENET_A010_L50` / one research-only member |
| Next research design | `P0_7E_ALPHA_RESEARCH_V2` / `DESIGN_READY` / `NOT_YET_EXECUTED` |
| P0-7E budget | 7 predictive configurations / 35 fold attempts / no recycling |
| Post-P0-7E rule | freeze one final pool, then protected-holdout adequacy/go-no-go; no open-ended P0-7F on 2019-2025 |

## Architecture health

- L1 Data: `FREE_DAILY_V1` supports bounded research; full PIT, survivorship, authoritative tradability, and historical-delisted completeness remain unknown.
- L2 Alpha Discovery: the problem is now independent information relative to the ElasticNet anchor, not another broad survivor. P0-7E allows three mechanism-driven Formula candidates and no model sweep.
- L3 Alpha Evaluation: P0-7D established one research-only member on reused selected OOS evidence. Independent confirmation remains absent; the 2026 holdout is sealed.
- L4 Portfolio: Top-20 equal weight remains Portfolio Baseline V1. P0-7E allows one equal-weight membership-buffer challenger only.
- L5 Execution: costs, slippage, lots, and fills remain synthetic research assumptions. Production and real-trading readiness remain `NO`.

## P0-7D empirical result

- 17 frozen P0-7C survivors, zero new predictive experiments.
- 78,091 matched rows, 1,112 dates, 72 symbols, five folds, and 60 non-overlapping observations.
- 136 pair assessments, 16 redundancy edges, seven redundant variants, and 10 candidates after deterministic de-duplication.
- One accepted anchor and nine rejected additions; one retained singleton leave-one-out decision.
- Final `ALPHA_POOL_V1`: `P07C_ML_ENET_A010_L50` only.
- Anchor fold RankIC: `0.0802 / 0.0955 / 0.1675 / 0.0951 / 0.1337`; mean `0.1144`; 5/5 positive.
- Formula-relative incremental RankIC: `+0.0165`; frozen-cost net `1.0098`; 2x-cost net `0.9369`; MDD `-14.58%`; decay ratio `1.4253`.
- Three ElasticNet variants had independent Formula-relative increments. Ridge and all LightGBM variants failed incremental classification.
- Maximum prior DSR probability remains `0.4228853062141328`; PBO remains `NOT_JUSTIFIED`.
- Validator 16 PASS / 4 UNKNOWN / 0 FAIL; repository tests 107/107.
- Protected holdout accessed `FALSE`; consumed `FALSE`.

## Evidence status

- `EMPIRICAL`: P0-7D protocol `76568528ed1a7c70d6b0a93b76924d7cb943dc94`, result `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63`, and checkpoint `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0` form a verified linear chain.
- `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`: the anchor and one-member pool were selected using reused 2021-2025 OOS evidence.
- `DOCUMENTED`: P0-7E is mechanism/orthogonality-first, LightGBM stays frozen, and P0-7E is the last major 2019-2025 iteration before a holdout decision.
- `SYNTHETIC`: transaction costs, slippage, adjusted-unit execution, and portfolio fills.
- `UNKNOWN`: independent-holdout performance, full PIT/survivorship, empirical market impact, capacity, production, and real-trading behavior.

## Current boundary

P0-7E may execute only after an exact Alpha Factory controller directive and pre-result manifest. It permits exactly three new Formula candidates, four fixed anchor family ablations, fixed LowVol robustness views, deterministic anchor-relative qualification, and one portfolio challenger. It may not access 2026, tune ElasticNet, run LightGBM/deep models, add Size/Value/Quality, use RD-Agent/LLMs, buy data, trade, or make production claims.
