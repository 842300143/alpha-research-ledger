# Current State

Last updated: 2026-09-18

| Field | Value |
| --- | --- |
| Research Controller Repository | `D:\alpha-research-ledger` |
| Execution Repository | `D:\alpha-factory` |
| Last completed execution task | `P0_7E_ALPHA_RESEARCH_V2` / `P0_7E_PASS_WITH_WARNINGS` |
| Current research program | `P0-8 FACTOR ZOO & FACTOR STRUCTURE DISCOVERY V1` |
| Current research policy | `FREE FIRST`; Generation-2 canonical factor-space research allowed under ADR-0014 |
| RD-Agent | `PAUSED_CREDENTIAL_REQUIRED` |
| Old P0-7B Blind | `SUPERSEDED_UNCONSUMED` under ADR-0007 |
| Protected 2026 holdout | `SEALED / UNACCESSED / UNCONSUMED` |
| Generation-1 research anchor / strict pool | `P07C_ML_ENET_A010_L50` / one research-only member |
| Final Generation-1 constructor | `TOP20_EQUAL_WEIGHT` |
| P0-8 design | 103 definitions / 89 concepts / 89 parameterization groups |
| P0-8A | `DESIGN_READY` / `NOT_YET_EXECUTED` / no-result implementation and freeze |

## Generation-1 close

P0-7E completed all seven configurations and 35 fold attempts, 45 LowVol robustness cells, four ablations, Formula-span diagnostics, deterministic selection, and portfolio slots. All three new Formula candidates passed standalone evidence and failed the full anchor-relative incremental gate. No candidate was promoted. The buffer challenger was not promoted. The final strict pool and constructor remained unchanged.

Cumulative P0-7 predictive accounting is 34 configurations and 170 fold attempts, plus P0-7D's 136 pair decisions, 45 Formula-span checks, deterministic ordering, forward-addition, and leave-one-out choices. The 2019-2025 sample is heavily selection-contaminated.

## P0-8 design state

- Registry: `research/factor-zoo/FACTOR_REGISTRY_V1.json` / `DRAFT_DESIGN`.
- Definitions: 99 atomic/transformed candidates for P0-8B plus four conditional prototypes reserved for P0-8D.
- Included space: canonical daily price, range, volume, amount, turnover, market-relative, and conditional price-volume constructs.
- Excluded space: Size, Value, Quality, industry, text/event, order book/tick, authoritative limits, and other unavailable inputs.
- Definition freeze: `NO`; P0-8A must bind implementation/code/config/card hashes after no-label correctness tests.
- Predictive execution in this ledger session: `NONE`.

## Architecture health

- L1 Data: `FREE_DAILY_V1` supports bounded factor research on the action-aware subset. Full PIT, survivorship, authoritative tradability, corporate actions, and historical-delisted completeness remain unresolved.
- L2 Alpha Discovery: a structured 103-definition factor taxonomy now replaces ad hoc neighboring-candidate search. Definitions remain draft until P0-8A.
- L3 Alpha Evaluation: P0-8B/P0-8C protocols separate atomic evaluation from factor structure, add global FDR and shared empirical-null controls, and retain failures.
- L4 Portfolio: Top-20 equal weight remains the research diagnostic baseline. No new constructor is authorized.
- L5 Execution: costs and fills remain synthetic. Production and real-trading readiness remain `NO`.

## Evidence status

- `EMPIRICAL`: committed FREE_DAILY_V1 schema/coverage/quality evidence and P0-7A through P0-7E result artifacts.
- `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`: all 2019-2025 factor/pool evidence.
- `DOCUMENTED`: P0-8 charter, taxonomy, registry design, preprocessing, timing, evaluation, structure, interaction, multiple-testing, and roadmap.
- `SYNTHETIC`: transaction costs, slippage, adjusted-unit execution, and portfolio fills.
- `UNKNOWN`: independent-holdout performance, full PIT/survivorship, empirical impact, capacity, production, and real-trading behavior.

## Current boundary

Only `P0_8A_FACTOR_ZOO_BUILD_V1` is design-ready. It may implement and correctness-test the factor library in Alpha Factory after an exact controller directive. It may not compute labels, IC, rankings, coverage comparisons for 2026, portfolios, or predictive results. P0-8B and later stages are not authorized. Alpha Factory remained read-only during this ledger design session.
