# Current State

Last updated: 2026-09-20

| Field | Value |
| --- | --- |
| Research Controller Repository | `D:\alpha-research-ledger` |
| Execution Repository | `D:\alpha-factory` |
| Last completed execution task | `P0_8C_FACTOR_STRUCTURE_V1` / `P0_8C_PASS_WITH_WARNINGS` (Alpha Factory checkpoint) |
| Current research program | `P0-8 FACTOR ZOO & FACTOR STRUCTURE DISCOVERY V1` |
| Current research policy | `FREE FIRST`; Generation-2 canonical factor-space research allowed under ADR-0014 |
| RD-Agent | `PAUSED_CREDENTIAL_REQUIRED` |
| Old P0-7B Blind | `SUPERSEDED_UNCONSUMED` under ADR-0007 |
| Protected 2026 holdout | `SEALED / UNACCESSED / UNCONSUMED` |
| Generation-1 research anchor / strict pool | `P07C_ML_ENET_A010_L50` / one research-only member |
| Final Generation-1 constructor | `TOP20_EQUAL_WEIGHT` |
| P0-8 design | 103 definitions / 89 concepts / 89 parameterization groups |
| P0-8A/B/C | `COMPLETE_WITH_WARNINGS`; 103 built, 97 evaluated, 27 survivors, 16 archetypes, 12 frozen pair leads |
| P0-8D V1 | `UNEXECUTED`; zero executable definitions; activation exception `CLOSED_ABORTED` |
| P0-8D0 | `COMPLETE_WITH_ZERO_EXECUTABLE_INTERACTIONS`; 12 investigated, 4 simple combinations, 2 rejected for no mechanism, 6 deferred |
| P0-8D execution V2 | `NOT_READY_NO_EXECUTABLE_CARDS`; no activation directive |

## Generation-1 close

P0-7E completed all seven configurations and 35 fold attempts, 45 LowVol robustness cells, four ablations, Formula-span diagnostics, deterministic selection, and portfolio slots. All three new Formula candidates passed standalone evidence and failed the full anchor-relative incremental gate. No candidate was promoted. The buffer challenger was not promoted. The final strict pool and constructor remained unchanged.

Cumulative P0-7 predictive accounting is 34 configurations and 170 fold attempts, plus P0-7D's 136 pair decisions, 45 Formula-span checks, deterministic ordering, forward-addition, and leave-one-out choices. The 2019-2025 sample is heavily selection-contaminated.

## P0-8 design state

- Alpha Factory P0-8A froze 103 implemented/schema-checked definitions. P0-8B excluded two structural zero-sum definitions without replacement and evaluated 97 atomic/transformed factors across 291 WF1-WF3 attempts.
- P0-8C evaluated 351 pair relationships, froze 16 archetypes and a 12-pair P0-8D investigation handoff; its handoff hash is `2502ac870d0767db8839665ca664251e7652b7e493e7c6986719f993486ccb4c`.
- P0-8D0 used only frozen structure evidence and factor cards to investigate the 12 pairs. No candidate-specific form, direction, and feasible state rule passed the complete design gate; zero Interaction Cards were issued.
- Included space: canonical daily price, range, volume, amount, turnover, market-relative, and conditional price-volume constructs.
- Excluded space: Size, Value, Quality, industry, text/event, order book/tick, authoritative limits, and other unavailable inputs.
- Definition freeze: `YES` for P0-8A atomic factors; `NO` for any P0-8D interaction hypothesis.
- New predictive execution in this Ledger task: `NONE`.

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

P0-8D V1 was not activated. The proposed V2 execution spec has an empty executable population and is `NOT_READY_NO_EXECUTABLE_CARDS`. Alpha Factory remains direction-only. A new controller decision is required before any further hypothesis design, P0-8D execution, P0-8E, or protected data access. The 2026 holdout remains `SEALED / UNACCESSED / UNCONSUMED`.

## CAD01 active transition (2026-09-20)

The controller directive `EXECUTE_CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1` supersedes the earlier direction wait only for a separate exploratory CAD01 namespace under ADR-0016. The old P0-8D/P0-8D0 state remains 12 investigated, zero executable, and unrun. Alpha Factory completed the finite metadata repair at local commit `f4295368e43f6396a64307d4888140752a71ae56`; normal `worker_start` returned `READY:YES`. CAD01 pre-result code, manifest, real pilot, and final status are still pending. The 2024–2025 interval and 2026 holdout remain closed.
