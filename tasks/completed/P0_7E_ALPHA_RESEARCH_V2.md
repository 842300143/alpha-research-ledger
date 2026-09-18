# P0_7E_ALPHA_RESEARCH_V2

- Task ID: `P0_7E_ALPHA_RESEARCH_V2`
- Status: `P0_7E_PASS_WITH_WARNINGS` / `COMPLETE`
- Execution repository: `D:\alpha-factory`
- Protocol commit: `f3523ac72ed6995f3d0342d6b28d25fb5f78fb4b`
- Result commit: `27793d974110758ccf83848aed3d9354341b7e3f`
- Completion checkpoint commit: `c37ab3caf0c50c100906503d17d05fd5f78e2e24`
- Result payload hash: `bd2b6bc841ed948237ddac98777d43d38f89a28e27d9d5de99bee4d9031746d4`
- Final-freeze hash: `7399a25d212caa7b1a6c68c8f7ac8a362fbffeefd6d92f9168ca0b902f9364b8`
- Validator hash: `fa7ef94392d1b9b440247baa93dcd48b07526d6f7b5229ccc8d9c5eb12f13275`
- Evidence classification: `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`

## Frozen scope completed

- Seven preregistered predictive configurations and 35 terminal fold attempts; no budget recycling.
- Three new Formula candidates, 45 fixed LowVol robustness cells, five anchor coefficient snapshots, four family ablations, and five Formula-span residual checks.
- One deterministic candidate order, one forward pass, one reverse leave-one-out procedure, and seven reserved portfolio slots.
- Repository tests: 110 passed. Independent Validator: `PASS`. Artifact verification: `PASS`.

## Result

All three new Formula candidates passed their standalone evidence gates and failed the complete anchor-relative promotion gate:

- `P07E_LIQ_SIGNED_ABTURN_5V60`: rejected.
- `P07E_REV_MEDIUM_EX5_20`: rejected.
- `P07E_INT_REV5_X_ABTURN`: rejected.

The four ablations were diagnostic only. Return/Reversal, Trend, and Volatility were `NON_MATERIAL_AT_THIS_BUDGET`; Liquidity/Activity was `AMBIGUOUS` because one fold produced an undefined RankIC from a constant score. The three frozen LowVol scores were robust only on available non-PIT surrogates, not PIT-certified. Formula-span analysis retained stable residual anchor information.

The final strict research pool did not change:

- member: `P07C_ML_ENET_A010_L50`;
- constructor: `TOP20_EQUAL_WEIGHT`;
- new promotions: zero;
- buffer challenger: not promoted because there was no distinct final-pool stream.

## Cumulative selection record

P0-7C and P0-7E together account for 34 predictive configurations and 170 configuration-fold attempts. P0-7D additionally contributed 136 pair decisions, 45 Formula-span held-out reconstructions, deterministic ordering, forward-addition, and leave-one-out choices. None of this history is reset by P0-8.

## Retained limits

- 2019-2025 is heavily selection-contaminated and supplies no independent confirmation.
- Security-master lifecycle evidence is a current capture of historical effective dates, not certified PIT evidence.
- Historical survivorship is incomplete; costs and fills are synthetic; market impact, capacity, production readiness, and real-trading behavior remain `UNKNOWN`.
- The 2026 protected holdout remained `SEALED / UNACCESSED / UNCONSUMED`.

## Authoritative Alpha Factory evidence

- `reports/P0_7E_ALPHA_RESEARCH_V2_FINAL.md`
- `research/alpha_v2/results/RESULT_BUNDLE.json`
- `research/alpha_v2/results/P0_7E_FINAL_POOL_FREEZE.json`
- `research/alpha_v2/VALIDATOR_RESULT.json`
- `state/checkpoints/P0_7E_ALPHA_RESEARCH_V2.json`

## Decision changed

Generation-1 Alpha Research is complete. P0-7E does not prove that the available canonical factor space is exhausted. ADR-0014 permits a separately governed Generation-2 Factor Zoo program while preserving every P0-7 result and keeping the protected holdout sealed.
