# P0_8A_FACTOR_ZOO_BUILD_V1

- Task ID: `P0_8A_FACTOR_ZOO_BUILD_V1`
- Status: `DESIGN_READY` / `NOT_YET_EXECUTED`
- Intended execution repository: `D:\alpha-factory`
- Research repository: `D:\alpha-research-ledger`
- Dataset: `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`
- Evidence mode: implementation and no-result correctness only
- Protected holdout access: zero

## 1. Goal

Implement, validate, and freeze the canonical P0-8 Factor Zoo without computing predictive evidence. Convert the 103 design cards into deterministic code: 99 atomic/transformed definitions eligible for later P0-8B evaluation and four conditional prototypes reserved for P0-8D.

P0-8A succeeds by proving definition correctness, field compatibility, timing safety, budget accounting, and protected-data isolation. It does not rank factors, compute IC, inspect returns, run a portfolio, or select survivors.

## 2. Required source binding

Before mutation, verify and bind:

- Alpha Factory P0-7E result commit `27793d974110758ccf83848aed3d9354341b7e3f` and completion checkpoint `c37ab3caf0c50c100906503d17d05fd5f78e2e24` in linear ancestry;
- `FREE_DAILY_V1` manifest and feature-readiness hashes;
- price and adjustment Parquet schemas;
- P0-7C split, subset, feature, timing, and cost artifacts for inheritance only;
- P0-7E final-freeze hash `7399a25d212caa7b1a6c68c8f7ac8a362fbffeefd6d92f9168ca0b902f9364b8`;
- exact ledger Factor Registry, Card Schema, Timing Contract, Preprocessing Policy, and ADR-0014 content hashes.

Deny on mismatch. Do not repair a mismatch by changing a factor definition.

## 3. Permitted inputs

Raw inputs are limited to the documented `FREE_DAILY_V1` fields:

`trade_date`, `symbol`, `open`, `high`, `low`, `close`, `preclose`, `volume`, `amount`, `turnover`, `trade_status`, `st_status`, `suspension_status`, provenance fields, and `adj_factor`/action metadata.

Derived inputs may include adjusted OHLC, backward returns, rolling statistics, equal-weight eligible-universe market composites, breadth, and cross-sectional ranks defined by the cards. Size, market cap, PE/PB, fundamentals, industry, news/text, order book, tick data, authoritative limit prices, or any undeclared source is prohibited.

## 4. Protected-data deny rule

All ordinary loaders must predicate-filter at `trade_date <= 2025-12-31` before conversion or materialization and fail if any 2026 row reaches memory. P0-8A does not need 2024-2025 outcomes, but it may use through-2025 feature rows for no-label formula correctness only.

Prohibited for 2026: feature values, factor coverage, missingness, score distributions, ranks, labels, returns, regimes, portfolio behavior, universe comparisons, or any candidate-specific information. Calendar dates alone may be used to verify exclusion.

## 5. Build requirements

- Implement every factor as a pure deterministic function with stable factor ID.
- Separate raw factor calculation from common preprocessing.
- Enforce full lookback and declared endpoint requirements.
- Implement adjusted OHLC consistently; never substitute provider `pct_change` for the card return definition.
- Implement equal-weight market composites only from the eligible same-date universe.
- Produce explicit missing values on denied inputs; no silent imputation.
- Tag each output with definition hash, code hash, raw-field list, lookback, availability time, readiness, and abstraction.
- Conditional definitions compile and validate schema but cannot emit evaluated scores before P0-8C/P0-8D activation.

## 6. Allowed correctness evidence

Allowed:

- unit tests on synthetic miniature panels;
- property tests for lag direction, scale invariance where expected, sign, full lookback, missingness, and deterministic ties;
- hand-calculated fixtures containing no protected data;
- schema-only inspection of committed Parquet metadata;
- bounded through-2025 spot checks that emit only PASS/FAIL and no candidate values, coverage, rankings, or outcomes;
- exact reproduction tests for already frozen P0-7 formulas, without new performance computation.

Forbidden:

- IC, RankIC, labels, future returns, NAV, return spread, Sharpe, drawdown, turnover portfolio results, candidate ordering, correlation map, or survivor selection;
- changing a formula because a value “looks wrong” absent a specification violation;
- any predictive backtest or Stage-1 evaluation.

## 7. Parameterization and budget audit

The manifest must report:

- 103 definitions total;
- 99 atomic/transformed P0-8B definitions;
- four conditional P0-8D prototypes;
- unique concept count and every `parameterization_group`;
- variants per concept and the mechanism justification for each;
- zero continuous/neighboring sweeps;
- zero predictive configurations executed in P0-8A.

Any duplicate formula, unexplained adjacent horizon, missing field, or undeclared transform is a hard stop. Do not add replacement factors merely to retain the count.

## 8. Freeze artifacts

Before P0-8A completion, emit immutable:

- `FACTOR_REGISTRY_V1.json` normalized payload and hash;
- factor-card bundle hash and per-card hashes;
- implementation code and configuration hashes;
- field/schema audit;
- parameterization audit;
- timing/PIT audit;
- preprocessing implementation audit;
- synthetic correctness-test report;
- holdout deny-before-load audit;
- build registry with one terminal build status for every definition;
- `P0_8A_FACTOR_ZOO_FREEZE.json` binding all inputs and outputs.

Definitions become `FROZEN_P0_8A` only after all hard gates pass. A definition that cannot be implemented remains retained as `DENIED_NOT_READY` and is excluded from P0-8B; its slot is not replaced.

## 9. Validation gates

Independent Validator must verify:

- source hashes and schema;
- exact factor counts and unique IDs;
- formula/card/code traceability;
- absence of undeclared raw fields;
- no future shift or same-close execution assumption;
- full-window requirements;
- common preprocessing behavior;
- conditional-factor execution denial;
- no predictive metrics/results;
- protected 2026 not accessed or materialized;
- no secrets, large raw-data commits, payment, broker, or trade action.

## 10. Outputs and next state

On PASS, close as `P0_8A_PASS_WITH_WARNINGS` if only inherited data limitations remain and prepare a separate P0-8B activation directive. The P0-8B spec must bind the P0-8A freeze, exact 99-or-fewer eligible definitions, 297-or-fewer Stage-1 fold attempts, shared empirical-null permutations, and lifecycle gates.

On implementation or integrity failure, stop with the exact factor IDs and gates. Correct only specification violations under additive correction records; do not inspect results or substitute new definitions.

## 11. Prohibited actions

Do not access 2026; run a predictive evaluation; compute candidate coverage for 2026; change P0-7 evidence; tune definitions; add fields/families; call RD-Agent/LLMs; purchase data; bind a broker; trade; make production claims; or push any change to Alpha Factory without the exact P0-8A controller directive.

## 12. Execution readiness

Design readiness: `YES`.

Execution readiness requires a clean Alpha Factory worktree, exact source/hash reproduction, a new exact controller directive `EXECUTE_P0_8A_FACTOR_ZOO_BUILD_V1`, and a pre-build manifest created before formula implementation or correctness evidence. This ledger design does not execute P0-8A.
