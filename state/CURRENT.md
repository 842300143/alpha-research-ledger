# Current State

## INTEGRATION02 complete (2026-09-22)

ADR-0031 accepts the unified corrected-research and corporate-action engineering baseline at Alpha Factory work commit `c5235189d866aa05c52f7e6802ae482b4a1b9972`, integration state commit `df5f374eefb7204a2705282dd8b4445d6ee9859e`, and normal master merge `b17b33bbaec09573e8b14af710830340a9aba392`. The Research Ledger normal main merge is `70ca84a11f6dc1dea7dbadec04ed13c0cf775315`. Current system is corrected Ridge F1/S123 V2 / `PROVISIONAL_RESEARCH_SYSTEM`; the pre-PIT system is `SUPERSEDED`; production champion is `NONE`; confirmed Alpha is `NO`. The 14 REQUAL impact warnings are explanation-only, not corrected-semantic blockers. CAQUAL02 leaves no event-data gap, and ELECTION01 supplies the frozen self-financing policy. Generic capability is `EXACT_EVENT_AWARE_UNDER_FROZEN_ELECTION_POLICY`; exact replay requires `HOLDING_PATH_EVENT_COVERAGE_GATE=EXACT_FOR_THIS_REPLAY`. Capital is RMB 50,000 primary and RMB 1,000,000 diagnostic. Alpha Factory passes 250 tests and 13 independent checks. No wealth replay, new Alpha research, 2024–2025 or 2026 access occurred.

## REQUAL01 complete (2026-09-21)

ADR-0026 closes `REQUAL01_PIT_CORRECTED_RESEARCH_REPLAY_V1` as `PASS_WITH_WARNINGS` at Alpha Factory work commit `9eb913ac4bff3739c063a9b3f782bf68c74b98f8`. `FREE_DAILY_PIT_V2` contains 87,408 rows for 72 symbols from 2019-01-02 through 2023-12-29. The frozen 97-factor / 291-attempt protocol retained 27 survivors with zero lifecycle changes; corrected structure retained 16 archetypes and 10 estimated dimensions; CAD retained three candidates and `S123`; MODEL01 retained `RIDGE_F1` / `F1`. The corrected system is system-equivalent to the old provisional system, but the old artifact is superseded for forward selection. Validator: 18 PASS / 3 warnings / 0 fail; 184 Alpha Factory tests pass. Evidence remains selection contaminated. No interaction, Exposure, Portfolio selection, 2024–2025 or 2026 access occurred. CAQUAL01 remains separate.

## INTEGRATION01 complete (2026-09-21)

Controller directive `ALPHA-INTEGRATION01-PITPRICE-PIPELINE-PORTFOLIO-V1` integrated PITPRICE01 correctness contracts with PIPELINE01 incremental runtime and PORTFOLIO01 sizing. Execution work commit `62daaa7319eb06de8333f150049377286450da36` was merged normally to master at `e4758907dd246e812a2e56f35ff41defc3c7f116`; the Research Ledger integration was merged normally to main at `5e8d4b48ff55c162d1f7ed248e5d2b86ea00214e`. Independent review passed with a source-drift cache warning; 57 owner tests passed. ADR-0024 records the accepted baseline; ADR-0021 and frozen PITPRICE01 evidence remain authoritative. `UPSTREAM_MODEL_INVARIANT=NO`. Old Ridge F1/S123 is a superseded research fixture pending REQUAL01; there is no current production champion. EXPOSURE01 V1 remains invalid for selection. Primary capital is RMB 50,000, scaling diagnostic RMB 1,000,000. Corporate-action capability is `TOTAL_RETURN_APPROX_ONLY`; exact executable wealth and real-market portfolio evaluation await CAQUAL01. PIPELINE01 is `ENGINE_READY_WITH_PERF_WARNING` on synthetic evidence. The 2024–2025 and 2026 market intervals remained sealed for this task. No Alpha research, exposure replay or portfolio return evaluation occurred.

## PITPRICE01 completed at upstream hard gate (2026-09-21)

ADR-0021 records `UPSTREAM_RESEARCH_REQUALIFICATION_REQUIRED` at Alpha Factory work commit `e622bae101329a4b4f365d3354ff11e115ccc046`. The capital audit found that the project charter's RMB 50,000 initial model was not propagated into EXPOSURE01 V1's explicit RMB 1m continuous account; `STATE_PROPAGATION_FAILURE` is primary. A bounded 2019–2023 causal-price comparison changed frozen Ridge F1 inputs and five of 36 fixed exposure-signal Top20 choices, so `UPSTREAM_MODEL_INVARIANT=NO`. No V2 replay or policy selection occurred. BaoStock price-return links do not supply exact cash/share entitlements. See `research/price-basis/PITPRICE01_RESULT_SUMMARY.md` and the exact Alpha Factory report/checkpoint. V1, CAD01/CAD02/MODEL01 remain frozen; 2024–2025 and 2026 market rows remain unopened by PITPRICE01. Next is controller direction on upstream requalification and event data.

## EXPOSURE01 controller authorization history

The controller authorized `EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1` under ADR-0019 from Alpha Factory HEAD `aeebb5493e2805d1fcaea81cfb6fdc64f3014b90` and Ledger HEAD `e335d575e39d9cfd561bfa131fb17f0a7f5ef0c8`. MODEL01 is complete and unchanged: Ridge F1/S123, 16 base plus C1/C2/C3, 10 systems and 30 folds, 16 validator PASS, zero FAIL. The >0.005 RankIC complexity premium retained Ridge despite ElasticNet F1 leading mean RankIC by 0.003064. ElasticNet F0's approximately 0.000422 higher modeled net outcome is only an alternate clue; it does not revise MODEL01 selection. EXPOSURE01's objective is full-calendar, after-cost compounded terminal wealth, with cash allowed. Two-month windows are diagnostics, not independent samples. Evidence remains selection-contaminated, non-PIT and synthetic for execution. CAD02's 15/20 calibration, one incomplete run and 2,297.160-second overrun remain unchanged. The 2024–2025 interval was used in Generation-1 research but is unopened by EXPOSURE01; 2026 remains sealed. No test or live-trading authorization.

## EXPOSURE01 completed inconclusive

ADR-0020 closes V1 at Alpha Factory work commit `87b4bbe2f87081b46182ffb1c2dd18a8aa78b198`. Three policies and six account/cost paths were retained, but the validator found one hard as-of price failure: backward end-normalized adjustment factors encoded post-2023 events in 2019–2023 execution prices. The independent Reviewer agreed; 51/72 factors at 2023-12-29 were nonunit. Validator 71 PASS / one FAIL; no policy selected. The next work is controller direction on a separate causal-price correction, not a V1 rerun. See `research/exposure/EXPOSURE01_RESULT_SUMMARY.md` and the exact Alpha Factory report/checkpoint. No later data or trading access.

Last updated: 2026-09-22

| Field | Value |
| --- | --- |
| Research Controller Repository | `D:\alpha-research-ledger` |
| Execution Repository | `D:\alpha-factory` |
| Last completed execution task | `INTEGRATION02_REQUAL_CORPORATE_ACTION_V1` / `ENGINEERING_INTEGRATION_COMPLETE` at Alpha Factory work commit `c5235189d866aa05c52f7e6802ae482b4a1b9972` |
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

## Prior P0-8 boundary

P0-8D V1 was not activated. The proposed V2 execution spec has an empty executable population and is `NOT_READY_NO_EXECUTABLE_CARDS`. A new controller decision is required before any P0-8D execution, P0-8E, or protected data access. The 2026 holdout remains `SEALED / UNACCESSED / UNCONSUMED`.

## CAD01 completed exploratory pilot (2026-09-20)

The controller directive `EXECUTE_CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1` superseded the earlier direction wait only for a separate exploratory CAD01 namespace under ADR-0016. The old P0-8D/P0-8D0 state remains 12 investigated, zero executable, and unrun. Alpha Factory completed the finite metadata repair at `f4295368e43f6396a64307d4888140752a71ae56`, froze code and policy at `a9f1dbc74471df1d55fce06588d169dc14973940`, committed the exact manifest at `419dc0e0b35454934cef23f4c0536c10b6405d16`, and committed the real result at `df327bfbd653864368a817eef7e64006b6575022`. Normal `worker_start` after metadata repair returned `READY:YES`. The pilot evaluated 131 expressions plus three fixed controls, stopped under `STAGNATION_RULE`, and archived three `SELECTION_CONTAMINATED_RESEARCH` candidates after modeled cost checks. The 2024–2025 interval and 2026 holdout remain closed. See `research/combinatorial-discovery/CAD01_RESULT_SUMMARY.md` and the exact execution artifacts.

## CAD02 provisional system freeze (2026-09-20)

Under ADR-0017, Alpha Factory evaluated eight fixed systems on CAD01-selected 2019–2023 data and technically froze S123, the 16-feature Ridge baseline plus all three archived CAD01 ASTs, as a provisional research system. The work commit is `844f682373b40d6d1519838f0d90eb0dbb449ecc`. A synthetic N0/N1 calibration completed 15 of 20 runs, retained one incomplete run, and exceeded the six-hour wall cap by 2,297.160 seconds; no remaining seed is authorized. The two approximate diagnostic generators disagree, so no confirmatory Alpha claim follows. See `research/combinatorial-discovery/CAD02_RESULT_SUMMARY.md` and the Alpha Factory report/checkpoint. The 2024–2025 test and 2026 protected interval remain closed pending a new exact controller directive and pre-access manifest.

## MODEL01 pre-result authorization (2026-09-21)

ADR-0018 authorized a fixed five-family by two-representation model-capacity comparison on the CAD02-bound 2019–2023 panel. Alpha Factory completed all ten systems and 30 folds at work commit `7565127615202c3edbc6d43458ac941d7a217282`, with 16 PASS / 0 FAIL Independent Validator and no model upgrade. Ridge F1/CAD02 S123 remains the one provisional system. CAD01 and CAD02 frozen evidence stayed unchanged; successor hard-wall enforcement passed focused tests. No 2024–2025 or 2026 data was accessed by MODEL01, and no later test is authorized. See `research/model-capacity/MODEL01_RESULT_SUMMARY.md`.
