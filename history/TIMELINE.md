# Project Timeline

## Recent verified events

| Date | Event | Exact evidence |
| --- | --- | --- |
| 2026-09-22 | INTEGRATION03 froze `CURRENT_20D_RESEARCH_BASELINE_V1`: provisional RankWeight, retained AlwaysInvest, separate canonical EqualWeight comparator, documented non-empirical 20-session horizon provenance, and preserved failure lineage. | ADR-0042; `research/integration/INTEGRATION03_RESULT_SUMMARY.md`; Alpha Factory Integration03 report/checkpoint. |
| 2026-09-22 | EVALRECON01 reconciled the Exposure02/Portfolio02 common path at RMB 57,445.71; first cause allocator-reserve drift, second cause non-grid rejected-exit reallocation; Validator V2 21/21. | Alpha Factory formal work commit `7189c2201e6bf1d6350eb5f67820a8f29128f61b`; ADR-0037; `research/exposure/EVALRECON01_RESULT_SUMMARY.md`. |
| 2026-09-21 | MODEL01 completed `COMPLETE_NO_MODEL_UPGRADE`: Ridge F1/S123 retained; 10 systems/30 folds; 16 PASS/0 FAIL. | Alpha Factory result commit `7565127615202c3edbc6d43458ac941d7a217282`; `reports/MODEL01_MODEL_CAPACITY_BAKEOFF_V1.md`; freeze SHA-256 `d7dcd4a2ebf930e805fc14fc9e059b4bd126b2c7b0054f4451ef8e559893deb7`. |
| 2026-09-21 | EXPOSURE01 bounded controller directive activated. | ADR-0019; `tasks/completed/EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1.md`; execution start HEAD `aeebb5493e2805d1fcaea81cfb6fdc64f3014b90`. |
| 2026-09-21 | EXPOSURE01 V1 closed inconclusive: six replays retained, adjustment-factor future normalization caused one hard validator FAIL; no policy selected. | Alpha Factory work commit `87b4bbe2f87081b46182ffb1c2dd18a8aa78b198`; `reports/EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1.md`; `state/checkpoints/EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1.json`; ADR-0020. |

Evidence note: phase names and sequence below are `DOCUMENTED` by the bootstrap controller directive. Exact dates, commits, reports, and empirical outcomes must be verified in `D:\alpha-factory`; unknown references are not inferred.

| Order | Phase | Durable note | Alpha Factory evidence |
| ---: | --- | --- | --- |
| 1 | Environment / bootstrap | Initial project environment and control foundations. | `UNKNOWN / TO_BACKFILL` |
| 2 | BigQuant baseline | BigQuant baseline work was performed. | `UNKNOWN / TO_BACKFILL` |
| 3 | WorldQuant | Blocked by account eligibility. | `UNKNOWN / TO_BACKFILL` |
| 4 | Qlib baseline | Qlib baseline work was performed. | `UNKNOWN / TO_BACKFILL` |
| 5 | RD-Agent environment preparation | Prepared the RD-Agent environment. | `UNKNOWN / TO_BACKFILL` |
| 6 | JoinQuant evaluation | Evaluated JoinQuant. | `UNKNOWN / TO_BACKFILL` |
| 7 | MyQuant evaluation | Encountered a current-product limitation. | `UNKNOWN / TO_BACKFILL` |
| 8 | Production Data Foundation | Established a production-data foundation phase. | `UNKNOWN / TO_BACKFILL` |
| 9 | Free Data Sandbox | Developed the free-data sandbox path. | `UNKNOWN / TO_BACKFILL` |
| 10 | Free Execution Bridge | Connected free data to the execution path. | `UNKNOWN / TO_BACKFILL` |
| 11 | Free Data Hardening | Hardened the free-data workflow. | `UNKNOWN / TO_BACKFILL` |
| 12 | Alpha Discovery V0 | Ran the initial controlled Alpha Discovery phase. | `UNKNOWN / TO_BACKFILL` |
| 13 | RD-Agent installation | Installed the RD-Agent environment. | `UNKNOWN / TO_BACKFILL` |
| 14 | RD-Agent LLM pilot | Paused for credentials under `FREE FIRST`. | `UNKNOWN / TO_BACKFILL` |
| 15 | Autonomous Workflow V3 | Advanced the autonomous workflow design. | `UNKNOWN / TO_BACKFILL` |
| 16 | Free Data Expansion V1 | Completed a 5,587,828-row, 3,207-security, 1,870-session research dataset with zero hard quality failures and explicit feature-readiness limits. | `P0_6E_PASS_WITH_WARNINGS`; result `69be29e41ddfdf815685f64d697465032c4a9891`; checkpoint `52c6a7eb506bb8848f1a643c469978d28804738c` |
| 17 | Long-Horizon Alpha Research V1 | Completed 27 frozen predictive configurations across five annual OOS folds. Eight Formula and nine ML configurations survived the broad gate; ElasticNet showed selective matched incremental value, LightGBM did not, top-20 equal weight won all six constructor comparisons, strict Alpha Pool membership remained empty, and the 2026 holdout remained sealed. | `P0_7C_PASS_WITH_WARNINGS`; protocol `95dc8e3c5b895fe7bf47135536e0ed4843b73471`; result `a881bd956c70088100f85999e7f0f4f965777a25`; checkpoint `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138` |
| 18 | Alpha Pool Qualification V1 | Qualified the exact 17 frozen survivors with zero new predictive experiments. Deterministic de-duplication left 10 candidates; one anchor was accepted, nine additions were rejected, and `ALPHA_POOL_V1` contains only `P07C_ML_ENET_A010_L50` as a research-only, selection-contaminated member. The 2026 holdout remained sealed. | `P0_7D_PASS_WITH_WARNINGS`; protocol `76568528ed1a7c70d6b0a93b76924d7cb943dc94`; result `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63`; checkpoint `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0` |
| 19 | Alpha Research V2 design | Froze a seven-configuration, 35-fold-attempt mechanism/orthogonality design: three Formula candidates, four ElasticNet family ablations, fixed LowVol robustness, deterministic anchor-relative selection, and one portfolio challenger. Declared P0-7E the last major 2019-2025 iteration before a freeze and holdout adequacy decision. No research was executed. | Ledger task `P0_7E_ALPHA_RESEARCH_V2`; `DESIGN_READY` / `NOT_YET_EXECUTED` |
| 20 | Alpha Research V2 execution | Completed all seven configurations and 35 fold attempts. All three Formula candidates passed standalone gates and failed the complete anchor-relative incremental gate. No new member or buffer constructor was promoted; the strict pool remained the singleton `P07C_ML_ENET_A010_L50` under `TOP20_EQUAL_WEIGHT`. | `P0_7E_PASS_WITH_WARNINGS`; protocol `f3523ac72ed6995f3d0342d6b28d25fb5f78fb4b`; result `27793d974110758ccf83848aed3d9354341b7e3f`; checkpoint `c37ab3caf0c50c100906503d17d05fd5f78e2e24` |
| 21 | Factor Zoo and Structure Discovery V1 design | Synchronized P0-7E, clarified ADR-0013 through ADR-0014, and designed a 103-definition canonical daily price-volume Factor Zoo: 99 atomic/transformed definitions plus four conditional prototypes, common preprocessing/timing, FDR, factor-map, residual, interaction, staged-sample, and sparse-model policies. No Alpha result or factory mutation occurred. | Ledger task `P0_8A_FACTOR_ZOO_BUILD_V1`; `DESIGN_READY` / `NOT_YET_EXECUTED` |
| 22 | Factor Zoo build, evaluation, and structure | Alpha Factory completed P0-8A/B/C with warnings: 103 definitions built, 97 evaluated through 291 WF1-WF3 attempts, 27 survivors, 351 structure pairs, 16 archetypes, and 12 frozen pair leads. P0-8D interactions remained unexecuted. | `state/checkpoints/P0_8A_FACTOR_ZOO_BUILD_V1.json`, `P0_8B_FACTOR_EVALUATION_V1.json`, `P0_8C_FACTOR_STRUCTURE_V1.json`; P0-8C completion work commit `02851c4620c9bbb9a904c842437496d9d6527c05` |
| 23 | P0-8D0 interaction-hypothesis design | Investigated the exact 12 P0-8C pairs from frozen evidence only. Four were simple combinations, two lacked a defensible interaction mechanism, and six were ambiguous/deferred; zero executable Interaction Cards and zero new predictive results. Old P0-8D V1 activation was aborted. | Ledger `tasks/completed/P0_8D0_INTERACTION_HYPOTHESIS_DESIGN_V1.md`; Alpha Factory governance audit commit `ce2b776a2f17b492a7be3d40a08a0ba863d8019b` |

## Protected Blind

The old 2024-12-27 through 2025-03-31 P0-7B protected Blind is `SUPERSEDED_UNCONSUMED` under ADR-0007. It was never executed and remains historical evidence: `BLIND_CONSUMED = FALSE`. The 2026-01-05 through 2026-09-15 protected recent holdout was not accessed or consumed by P0-7C, P0-7D, or P0-7E and remains sealed throughout P0-8 under ADR-0010, ADR-0013, and ADR-0014.
