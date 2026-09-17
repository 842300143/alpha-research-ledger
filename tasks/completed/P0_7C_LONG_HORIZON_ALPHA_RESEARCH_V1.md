# P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1

- Task ID: `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1`
- Status: `P0_7C_PASS_WITH_WARNINGS` / `COMPLETE`
- Intended execution repository: `D:\alpha-factory`
- Research repository: `D:\alpha-research-ledger`
- Protocol commit: `95dc8e3c5b895fe7bf47135536e0ed4843b73471`
- Result commit: `a881bd956c70088100f85999e7f0f4f965777a25`
- Completion checkpoint commit: `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138`
- Evidence classification: design is `DOCUMENTED`; results are `EMPIRICAL_RESEARCH_ONLY`; costs and adjusted-unit execution are `SYNTHETIC`; production properties remain `UNKNOWN`

## 1. Goal

Execute a bounded, reproducible long-horizon research program that compares transparent Formula Alpha, simple ML Alpha, and a minimal Portfolio Layer under one temporal discipline. Produce an Alpha Pool evidence table rather than select one magic winner.

This specification was activated by an exact Alpha Factory controller directive. Its frozen manifests and bounds governed the completed execution summarized in section 17.

## 2. Frozen dataset binding

- Dataset ID: `FREE_DAILY_V1`
- Dataset hash: `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`
- Dataset period: 2019-01-02 through 2026-09-15
- Sessions: 1,870
- Priced securities: 3,207
- Classification: `RESEARCH_ONLY_CURRENT_HISTORICAL_CAPTURE_NON_PIT`
- Authoritative manifest: `research/free_daily_v1/DATASET_MANIFEST.json` in Alpha Factory commit `52c6a7eb506bb8848f1a643c469978d28804738c`

Before execution, verify the dataset hash and all component artifact hashes from the P0-6E checkpoint. Deny on mismatch. Create a new P0-7C dataset/split/subset manifest; never alter P0-7A or P0-7B manifests.

## 3. Data limitations and eligibility gates

### Executable in V1

- Liquidity and raw volume/amount features with missing-day and suspension controls.
- Momentum, reversal, trend, and volatility only on a frozen action-aware/factor-covered subset.
- Predeclared multi-factor combinations using only eligible inputs.
- Formula, ML, and portfolio evaluation only where action-clean forward-return labels exist.

### Zero budget in V1

- Size: `NOT_READY`; market-cap history is absent.
- Value: `NOT_READY`; PE/PB history is absent.
- Quality: `NOT_READY`; point-in-time financial statements and revision history are absent.
- Text/event, Transformer, reinforcement learning, large deep networks, and RD-Agent: out of scope.

### Mandatory pre-execution subset gate

Construct `P0_7C_ACTION_AWARE_UNIVERSE_V1` from development-period metadata only. Require non-null, valid adjustment factors for every used feature and label observation, lifecycle eligibility, and a reproducible symbol/date inclusion rule. Freeze the symbol/date rule and its hash before any candidate run. The expected source population is the factor-covered BaoStock subset, but its exact membership must be empirically derived and recorded rather than assumed.

If the action-aware subset cannot support at least 60 eligible securities in each OOS fold after warmup and label purging, stop with `DATA_GATE_FAILED`; do not silently broaden to raw-return labels. The threshold is a research-design minimum, not evidence of statistical power.

## 4. Trading calendar and temporal protocol

The dates below were checked against the actual `FREE_DAILY_V1` trading calendar, not a civil-calendar assumption.

| Segment | First session | Last session | Sessions | Role |
| --- | --- | --- | ---: | --- |
| 2019 | 2019-01-02 | 2019-12-31 | 244 | warmup and initial training |
| 2020 | 2020-01-02 | 2020-12-31 | 243 | initial training |
| 2021 | 2021-01-04 | 2021-12-31 | 243 | walk-forward OOS fold 1 |
| 2022 | 2022-01-04 | 2022-12-30 | 242 | walk-forward OOS fold 2 |
| 2023 | 2023-01-03 | 2023-12-29 | 242 | walk-forward OOS fold 3 |
| 2024 | 2024-01-02 | 2024-12-31 | 242 | walk-forward OOS fold 4 |
| 2025 | 2025-01-02 | 2025-12-31 | 243 | walk-forward OOS fold 5 |
| 2026 protected | 2026-01-05 | 2026-09-15 | 171 | new protected holdout; excluded from P0-7C |

### Fold logic

| Fold | Training sessions | Test sessions |
| --- | --- | --- |
| WF1 | 2019-01-02 through 2020-12-31 | 2021-01-04 through 2021-12-31 |
| WF2 | 2019-01-02 through 2021-12-31 | 2022-01-04 through 2022-12-30 |
| WF3 | 2020-01-02 through 2022-12-30 | 2023-01-03 through 2023-12-29 |
| WF4 | 2021-01-04 through 2023-12-29 | 2024-01-02 through 2024-12-31 |
| WF5 | 2022-01-04 through 2024-12-31 | 2025-01-02 through 2025-12-31 |

- WF1 uses a two-year training window; later folds use the latest three complete calendar years.
- Maximum feature lookback is 252 trading sessions. A row is ineligible until its full backward-only warmup exists.
- Primary holding/label horizon is 20 trading sessions.
- Purge the final 20 training-session signal rows from model fitting before each test boundary so no training label crosses into the following test year. The 20-session horizon purge is the boundary embargo; record the exact excluded sessions in the split manifest.
- Features are calculated with information available at or before session `t`. Signals formed after `t` close may first enter at `t+1`; no same-close execution is allowed.
- A test-fold label must enter and exit inside that same fold. The last label-eligible signal sessions are 2021-12-03, 2022-12-02, 2023-12-01, 2024-12-03, and 2025-12-03 respectively. Later sessions may support within-year portfolio marking but cannot create a forward label that crosses a fold boundary; 2025 processing must never read 2026 outcomes.
- Cross-sectional clipping, imputation, scaling, thresholds, hyperparameters, and ensemble weights are fit on training data only, then frozen for the following OOS fold.
- No random time split, shuffled cross-validation, future-filled missing value, or use of later lifecycle status is permitted.
- Fold OOS outputs are appended once. Failed, aborted, and invalid runs remain in the registry.

## 5. New protected holdout policy

All 171 sessions from 2026-01-05 through 2026-09-15 are `P0_7C_PROTECTED_RECENT_HOLDOUT_V1`.

P0-7C ordinary research must not load or compute 2026 features, labels, IC, returns, portfolio results, coverage comparisons, regime performance, or candidate rankings. Calendar/date and non-outcome integrity metadata may be used only to construct and verify the deny-before-load boundary.

The old 2024-12-27 through 2025-03-31 P0-7B Blind is `SUPERSEDED_UNCONSUMED` under ADR-0007. Preserve it; never execute or portray it as a Blind result.

Protected-holdout consumption is a separate future task. Before access it must freeze candidates, action-aware subset, feature code, model parameters, portfolio rules, costs, comparison set, and hashes; create a pre-access one-run manifest; and deny on any mismatch. No tuning or rerun follows consumption.

## 6. Common outcome, costs, and evaluation rules

### Prediction target

Primary target for both Formula and ML tracks: the 20-session forward, corporate-action-adjusted return from the next tradable session's open through the close of the 20th trading session after signal formation, minus the eligible-universe cross-sectional median return for that entry date. Its cross-sectional percentile rank is used for rank-based metrics.

- Missing or non-tradable entry/exit observations produce an unavailable label; they are not zero-filled.
- Adjustment factors must be valid at both endpoints and through any action transition used by the return calculation.
- The execution worker must document the exact adjusted-price equation and verify it with fixtures before candidate execution.
- Optional 5- and 60-session horizons are decay diagnostics only. They do not create new selection metrics or candidate slots.

### Common costs and China-market rules

Use one frozen V1 cost specification for every candidate and constructor: commissions, sell tax, slippage, 100-share lots, T+1, no same-day sell, missing/suspended-day controls, and fail-closed handling when authoritative tradability is unknown. The execution worker must either reuse a validated Alpha Factory research-only cost model or stop and define one before experiments. Do not claim production executability because authoritative historical limits, full suspension state, and market impact are unavailable.

### Primary metrics

- Prediction: mean IC and RankIC where meaningful, information-ratio analogues, hit rate, fold stability, subperiod consistency, and alpha decay.
- Portfolio: gross/net return, annualized volatility, Sharpe with stated sampling assumptions, max drawdown, turnover, fees/slippage, concentration, and active exposures available from the eligible inputs.
- Robustness: per-fold results, leave-one-fold-out aggregation, regime descriptions, and sensitivity to the predeclared cost stress.
- Pool contribution: signal correlation, portfolio overlap, incremental post-cost return/risk contribution, and redundancy.

No single metric is a sufficient promotion gate.

## 7. Track A — Formula Alpha

### Families and bounded candidate budget

| Family | New candidates | Scope |
| --- | ---: | --- |
| Liquidity | 3 | amount/volume illiquidity, turnover persistence/change, and a liquidity shock definition |
| Volume | 2 | volume activity and volume-price confirmation using raw volume/amount controls |
| Momentum | 2 | medium and long horizon on the action-aware subset |
| Reversal | 2 | short and medium horizon on the action-aware subset |
| Trend | 2 | moving-average/trend-strength variants on the action-aware subset |
| Volatility | 2 | low-volatility and downside-volatility variants on the action-aware subset |
| Multi-factor | 1 | one predeclared price-volume/liquidity combination |
| Size / Value / Quality | 0 | `NOT_READY`; registration as an executed candidate is forbidden |

Up to four existing P0-7A formulas may be ported as historical baselines: `LIQ_TURN20`, `MOM_LOWVOL`, `LOWVOL`, and `TREND_MA20`. They count toward the Track A total and are not presumed winners.

Track A budget: **18 registered candidate definitions total** (14 new + at most 4 historical baselines), each evaluated once across the five walk-forward folds. Maximum four definitions in Liquidity and three in any other family, including baselines. Failed or aborted definitions consume budget; post hoc replacements are forbidden. Lookbacks must come from the predeclared set `{5, 20, 60, 120, 252}` and each definition uses one fixed specification, not a grid.

Liquidity/turnover remains a hypothesis motivated by P0-7A, not established evidence. It receives no special promotion rule.

## 8. Track B — ML Alpha

### Models

1. Linear baseline: one fixed regularized linear regression configuration.
2. ElasticNet: four predeclared `(alpha, l1_ratio)` configurations.
3. LightGBM: four shallow, regularized configurations with fixed depth/leaves, learning rate, estimators, feature subsampling, and seed.

Track B budget: **9 registered model configurations total**. The five outer folds are repeated evaluations of each registered configuration, not five new hypotheses. An optional shallow MLP has budget zero in V1 and requires a future design amendment justified by simple-model evidence. Transformers, RL, and large deep networks are forbidden.

### Features

- Backward-only returns, trend, volatility, liquidity, and volume features allowed by the feature-readiness contract.
- Calendar features only if known at prediction time.
- No Size, Value, Quality, text, event, future membership, or unadjusted return label.
- Missingness indicators are explicit; imputation and scaling are training-fit.
- Feature list, formulas, lookbacks, and monotonic transforms are frozen before the first model run.

### Training and retraining

- Use the common 20-session target and outer folds.
- Retrain once at the start of each annual OOS fold using only that fold's training window.
- Hyperparameters are fixed per registered configuration; the outer test fold never chooses or changes them. If a training-only diagnostic is required, use at most three chronological inner blocks wholly inside the training window; no random CV.
- LightGBM early stopping, if used, consumes only the final chronological training block and its rule is frozen. It cannot select among the four registered configurations using outer-fold results.
- Primary ML comparison is against the linear baseline and the best matched Formula candidate on identical rows; unmatched coverage cannot be treated as superiority.

## 9. Track C — Portfolio Layer

### Constructors

1. Baseline: top-20 equal weight, 5% target per name, rebalanced every 20 sessions at the next eligible open.
2. Alternative: rank-score weights with inverse trailing-volatility scaling, 8% single-name cap, a no-trade buffer around the current target, and a fixed turnover penalty. This is a deterministic constrained rule, not a high-dimensional optimizer.

Track C budget: **two constructors and at most 12 portfolio evaluations** (two constructors applied to at most six frozen shortlisted score streams). Constructor settings are frozen before comparison. No optimizer sweep or candidate-specific constructor tuning is allowed.

### Independent evaluation

Alpha prediction quality and portfolio construction are reported separately. First freeze each score stream and its IC/RankIC evidence. Then feed the identical dated scores into both constructors with identical entry, cost, T+1, and missing-tradability rules. Attribute differences in return, volatility, drawdown, turnover, cost, and concentration to the constructor. A stronger portfolio result cannot rewrite a weak predictive score as a strong Alpha, and vice versa.

## 10. Alpha Pool schema and lifecycle

Each candidate record must include:

- stable candidate and experiment IDs; parent hypothesis and family;
- formula/model version, code/config hash, dataset/subset/split hashes, and dependencies;
- prediction target, horizon, feature lookback, retraining cadence, and coverage;
- IC/RankIC distribution and stability where meaningful;
- gross and net OOS return, volatility, Sharpe, max drawdown, turnover, and costs;
- fold/subperiod consistency, alpha decay, and descriptive regime behavior;
- signal correlation, portfolio overlap, and incremental pool contribution;
- complexity, data dependency, known limitations, and evidence classification;
- experiment-count inclusion, failure/abort reason, review note, and lifecycle status.

Lifecycle values:

`DISCOVERED -> RESEARCHING -> OOS_SURVIVED -> ALPHA_POOL`

Terminal or side paths: `REDUNDANT`, `DECAYING`, `REJECTED`, `RETIRED`.

Promotion to `OOS_SURVIVED` requires valid results in all five folds, positive aggregate evidence after costs, no catastrophic fold dependency, and no unresolved leakage or data-quality failure. Promotion to `ALPHA_POOL` additionally requires non-redundant incremental contribution. Threshold values must be frozen in the execution manifest before candidate results are inspected.

## 11. Multiple-testing and overfitting policy

- Pre-register all 18 Formula and 9 ML configurations. The primary predictive search budget is 27 configurations.
- Count every materially distinct formula, feature set, target, horizon used for selection, model configuration, seed used for selection, and post hoc rule as an experiment. Failed and aborted attempts remain counted.
- Outer folds do not multiply the hypothesis count, but every fold result is retained. Portfolio construction has a separate maximum of 12 comparisons.
- No budget recycling, winner replacement, silent parameter tweak, or deletion of negative results.
- Rank candidates on a predeclared composite of predictive stability and post-cost usability; report the full comparison set and correlations, not only winners.
- Primary defenses are the fixed budget, chronological walk-forward OOS, immutable registry, retained failures, and untouched protected holdout.

Deflated Sharpe Ratio is a secondary diagnostic only if the candidate has at least 36 non-overlapping 20-session OOS portfolio observations and the calculation uses the full attempted-configuration count plus non-normality/autocorrelation treatment. Otherwise record `NOT_JUSTIFIED`.

PBO is not a V1 promotion gate. It may be reported descriptively only if at least eight sufficiently populated chronological subperiod blocks support a documented, time-order-preserving implementation. Ordinary CSCV permutations that destroy chronology are forbidden; otherwise record `NOT_JUSTIFIED`.

## 12. Regime analysis

Regime analysis is descriptive, not a parameter-selection loop. Using only lagged information and training-frozen thresholds, report candidate results by:

- market direction: positive versus negative trailing market trend;
- market volatility: low, middle, high trailing-volatility terciles;
- liquidity: low, middle, high cross-sectional market liquidity terciles;
- breadth: proportion of eligible names above a trailing trend threshold.

Use the action-aware eligible universe, state the proxy definitions, and report sample counts. Do not optimize separate strategy parameters per regime. Cells below a predeclared minimum observation count are `INSUFFICIENT`, not merged after inspection.

## 13. Deliverables

The later Alpha Factory execution task must produce at minimum:

- dataset/subset/split manifests and deny-before-load 2026 holdout guard;
- immutable experiment registry containing all attempts;
- feature and label specifications with code/config hashes;
- Formula, ML, and Portfolio reports with per-fold and aggregate tables;
- Alpha Pool registry and correlation/overlap matrices;
- multiple-testing/accounting report;
- regime diagnostic report;
- cost/execution-assumption report;
- leakage, PIT, survivorship, and protected-holdout audit;
- resource/reproducibility report, checkpoint, and exact test results;
- recommended next decision without accessing the protected holdout.

## 14. Success gates

P0-7C passes with appropriate warnings only if:

1. dataset and artifact hashes match P0-6E;
2. the action-aware subset and all five folds pass eligibility and leakage gates;
3. no 2026 outcome data is loaded or derived;
4. all attempts stay within the 18 Formula, 9 ML, and 12 portfolio-comparison budgets;
5. all five OOS folds are complete for any surviving candidate;
6. Formula, ML, and portfolio effects are separately reported;
7. costs, turnover, T+1, missingness, and known tradability uncertainty are explicit;
8. failed, negative, redundant, and aborted results remain registered;
9. exact reproduction and test suites pass;
10. no production, paid-data, or performance-generalization claim exceeds the evidence.

Success means a trustworthy evidence set and bounded shortlist, not necessarily a profitable candidate.

## 15. Stop conditions

Stop fail-closed before candidate execution if any dataset/component hash mismatches, the protected-holdout guard cannot prove deny-before-load, the action-aware subset falls below 60 eligible names in a fold, label construction cannot exclude corporate-action contamination, or split leakage is found.

Stop the affected track if its experiment budget is exhausted, reproducibility fails, or a shared data defect invalidates comparisons. Preserve partial and failed records. Do not repair data, broaden the universe, access P0-7B/P0-7C holdouts, call RD-Agent/LLMs, buy data, bind a broker, or trade under this task.

## 16. Completion state

Design readiness: `YES`.

Execution completed as `P0_7C_PASS_WITH_WARNINGS`. The empirical result did not establish a strict Alpha Pool, statistical certainty, production readiness, or real-trading readiness.

## 17. Completed empirical result

- 27 predictive configurations: 18 Formula and 9 ML.
- Five annual OOS folds from 2021 through 2025; 135 configuration-fold attempts; no failed attempts or budget recycling.
- Formula survivors: 8, from Liquidity, Reversal, and Volatility.
- ML survivors under the broad gate: 9. ElasticNet showed selective matched incremental RankIC; LightGBM showed no matched incremental value.
- Predictive survivors: 17.
- Top-20 equal weight beat the alternative constructor in all six matched comparisons and becomes Portfolio Baseline V1 under ADR-0008.
- Material signal and portfolio redundancy remained.
- Strict Alpha Pool members: 0. The historical nine-name correlation/decay shortlist is provisional and must not be relabeled as a final pool.
- Maximum DSR probability: `0.4228853062141328`; PBO: `NOT_JUSTIFIED`.
- Exact reproduction passed; 97/97 repository tests passed; Independent Validator recorded 23 PASS / 7 UNKNOWN / 0 FAIL.
- Protected 2026 holdout: `UNACCESSED / UNCONSUMED`.

## 18. Research interpretation

- Liquidity, Reversal, and Volatility are priority hypotheses, not proven production Alphas.
- ElasticNet merits decomposition and bounded follow-up because three configurations showed positive matched incremental RankIC.
- LightGBM receives no larger tuning budget merely because it is more complex.
- The 17 survivors are correlated configurations, not 17 independent Alphas.
- Weak DSR evidence leaves material multiple-testing and selection-bias risk.
- P0-7D must qualify the exact frozen survivors before any broad Generation-2 search; it may validly return an empty pool.

## 19. Authoritative Alpha Factory evidence

- `reports/P0_7C_LONG_HORIZON_ALPHA_RESEARCH_REPORT.md`
- `reports/P0_7C_CHECKPOINT.json`
- `reports/P0_7C_FORMULA_REPORT.md`
- `reports/P0_7C_ML_REPORT.md`
- `reports/P0_7C_PORTFOLIO_REPORT.md`
- `reports/P0_7C_ALPHA_POOL_REPORT.md`
- `reports/P0_7C_POOL_OVERLAP_INCREMENTAL_AUDIT.md`
- `reports/P0_7C_MULTIPLE_TESTING_REPORT.md`
- `reports/P0_7C_REGIME_DIAGNOSTICS.md`
- `reports/P0_7C_LEAKAGE_PIT_HOLDOUT_AUDIT.md`
- `research/alpha_v1/results/RESULT_BUNDLE.json`
- `research/alpha_v1/results/CANDIDATE_RESULTS.json`
- `research/alpha_v1/results/PORTFOLIO_RESULTS.json`
- `research/alpha_v1/registry/ALPHA_POOL.json`
- `research/alpha_v1/registry/POOL_QUALIFICATION.json`
- `research/alpha_v1/diagnostics/SIGNAL_CORRELATION.json`
- `research/alpha_v1/diagnostics/POOL_OVERLAP_INCREMENTAL_AUDIT.json`
- `research/alpha_v1/diagnostics/ML_INCREMENTAL.json`
- `research/alpha_v1/VALIDATOR_RESULT.json`

Result-bundle hash: `30f0879579906af2d341a9053f9090b19616fbd3facd7415461b5ae247329444`.

Pool-audit hash: `9121c1984a237f7555171fea15bca882febfc4284e26a44c1527456ab4878f62`.
