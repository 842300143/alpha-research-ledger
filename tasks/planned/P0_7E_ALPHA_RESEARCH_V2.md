# P0_7E_ALPHA_RESEARCH_V2

- Task ID: `P0_7E_ALPHA_RESEARCH_V2`
- Status: `DESIGN_READY` / `NOT_YET_EXECUTED`
- Intended execution repository: `D:\alpha-factory`
- Research repository: `D:\alpha-research-ledger`
- Positioning: `MECHANISM_REFINEMENT_AND_ORTHOGONAL_ALPHA_DISCOVERY`
- Evidence classification: design is `DOCUMENTED`; all 2019-2025 results will be `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`; costs remain `SYNTHETIC`; independent confirmation remains `UNKNOWN`

## 1. Goal and research questions

P0-7E is the last major research iteration on 2019-2025 before a freeze and protected-holdout decision. Its goal is not to find another standalone survivor. Its goal is to explain why the ElasticNet anchor worked and to test a very small number of economically specified signals for information incremental to that anchor.

The frozen questions are:

1. Does signed abnormal turnover contain a different mechanism from absolute liquidity shock, turnover level, or persistence?
2. Does medium-horizon reversal remain after excluding the most recent five sessions?
3. Is very-short reversal stronger specifically after abnormal-turnover events?
4. Does LowVol survive stricter action, holding-path tradability, and historical-universe/PIT-surrogate views?
5. Which feature families make the anchor work, and is its residual information stable across folds?
6. Can one turnover-control change improve Top-20 equal weight without changing the score, weighting objective, or cost assumptions?

## 2. Frozen source bindings

Alpha Factory commits must resolve in this linear ancestry order:

1. P0-7D protocol: `76568528ed1a7c70d6b0a93b76924d7cb943dc94`.
2. P0-7D result: `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63`.
3. P0-7D completion checkpoint: `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0`.

Bind before execution:

- Dataset: `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`.
- P0-7C split hash: `398aaa7bb3d4c5a6c4c1ae59d282c86231612808bfe7d78313e780940bbe2046`.
- P0-7C action-aware subset hash: `450584eca061808f92fbd34fe07dcc0f0354d4136ba5530dd04c6cb4a3669e9f`.
- P0-7C feature-spec hash: `1f8d0e68829fbf077b091a4ad53728e6a5c2d847e084cde21f466433ad305d13`.
- P0-7C cost-spec hash: `650aaba318a5ea8898440e9c3b5846e00c71cd19c6c40c9d05d307a2ca284560`.
- P0-7C canonical result-bundle hash: `30f0879579906af2d341a9053f9090b19616fbd3facd7415461b5ae247329444`.
- P0-7D qualification result hash: `d06b21fe5bcea2b394be0d6b7a09006a2518aaf37d04933631b4a5b49fbcb360`.
- P0-7D matched-panel hash: `68f1aee1a3f099f0167392bc4cbc3f5ab9b6494bca98170b54e4e46516c22538`.
- Research anchor: `P07C_ML_ENET_A010_L50` with `alpha=0.01`, `l1_ratio=0.5`, cyclic selection, and the frozen P0-7C seed/training procedure.
- Current research pool: `ALPHA_POOL_V1`, exactly one member, the anchor above.
- Portfolio Baseline V1: `TOP20_EQUAL_WEIGHT` under the P0-7C cost and execution spec.

The implementation must first reproduce the anchor's five fold RankIC values and the P0-7D pool payload. Any mismatch is a hard stop; it cannot be repaired by retraining with different settings.

## 3. Research period and protected isolation

- Permitted load period: `2019-01-02` through `2025-12-31` only.
- OOS folds: the exact five P0-7C annual walk-forward folds covering 2021-2025, with the same purge and label rules.
- Label: the unchanged 20-session cross-sectional-median-relative return using next-session entry.
- Protected holdout: `2026-01-05` through `2026-09-15`, `SEALED / UNACCESSED / UNCONSUMED`.
- All ordinary feature, label, score, coverage, regime, portfolio, eligibility, and ranking loaders must deny 2026 before materialization.
- Calendar-only metadata may establish exclusion and later adequacy inputs; it may not reveal coverage by candidate, features, performance, labels, rankings, or outcomes.

The old P0-7B Blind remains `SUPERSEDED_UNCONSUMED` and must never be executed.

## 4. Pre-registration and experiment registry

Before any result is computed, create an immutable P0-7E execution manifest containing source hashes, code/config hashes, the exact seven configurations, all formulas below, fold/split/subset bindings, cost and portfolio rules, output schemas, ordering, thresholds, and reserved evaluation slots.

Registry rules:

- Each configuration is registered once in a hash-chained registry before results.
- Every configuration receives exactly five fold-attempt records, including `FAILED`, `DENIED`, or `NOT_RUN_BY_DESIGN`.
- A failure consumes its configuration and fold budget. No replacement or budget recycling is allowed.
- Unused conditional diagnostic or portfolio slots are retained as consumed `NOT_RUN_BY_DESIGN`; they cannot be reassigned.
- No formula, sign, lookback, feature family, threshold, ordering, seed, cost, or constructor may change after registration.
- Exact reproduction runs do not add a configuration; any non-identical refit does.

## 5. Exact experiment budget

| Track | Registered predictive configurations | Fold attempts | Other fixed accounting |
| --- | ---: | ---: | --- |
| A. Liquidity refinement | 1 | 5 | one mechanism, one sign, one 5-vs-prior-60 definition |
| B. Reversal refinement | 1 | 5 | one medium-ex-five definition |
| C. LowVol robustness | 0 | 0 | 3 frozen LowVol scores x 3 robustness views x 5 folds = 45 cells |
| D. ElasticNet decomposition | 4 | 20 | 5 coefficient snapshots; 5 Formula-span residual checks |
| E. Cross-family interaction | 1 | 5 | one fixed very-short-reversal x abnormal-turnover interaction |
| F. Portfolio V2 | 0 | 0 | one challenger; 7 reserved constructor/score-stream evaluations |
| **P0-7E total** | **7** | **35** | no recycling |

Cumulative accounting after full execution will be exactly:

- predictive configurations: `27 + 7 = 34`;
- predictive configuration-fold attempts: `135 + 35 = 170`;
- prior P0-7D qualification: 136 pair decisions, 45 Formula-span checks, 10 anchor/forward decisions, one leave-one-out decision, one ordering, one score combiner, and one constructor;
- P0-7E selection degrees are additive and may not reset the history.

## 6. Track A — Liquidity mechanism refinement

Register exactly one new Formula candidate:

### `P07E_LIQ_SIGNED_ABTURN_5V60`

For security `i` on signal date `t`:

```text
recent_turn_i,t = mean(turnover_i,t-4:t)
prior_turn_i,t  = mean(turnover_i,t-64:t-5)
innovation_i,t  = ln((recent_turn_i,t + 1e-12) / (prior_turn_i,t + 1e-12))
score_i,t       = -innovation_i,t
```

Require all 65 observations, positive `prior_turn`, and no imputation. A higher score means recent turnover contracted relative to the security's own lagged baseline. The mechanism is a signed attention/liquidity innovation, unlike P0-7C's level (`-turnover20`), absolute amount shock, and absolute persistence deviation. Do not run the opposite sign, another window, winsorization choice, or alternative normalization.

Hypothesis: unusually high recent attention/turnover contains a transitory component, while low-attention contraction earns a positive subsequent relative return. Falsification: weak standalone OOS evidence, anchor redundancy, non-positive residual RankIC, or failure of the matched incremental gate.

## 7. Track B — Reversal mechanism refinement

Register exactly one new Formula candidate:

### `P07E_REV_MEDIUM_EX5_20`

Using adjusted closes:

```text
medium_return_ex5_i,t = adjusted_close_i,t-5 / adjusted_close_i,t-20 - 1
score_i,t              = -medium_return_ex5_i,t
```

Require valid adjusted closes at both endpoints. This isolates the 15-session move preceding the most recent five sessions, rather than scanning a horizon between 5 and 20. `P07C_REV5` and `P07C_REV20` remain frozen comparators; they are not rerun as new configurations.

Hypothesis: medium reversal reflects slower inventory or behavioral correction distinct from the very-short microstructure effect. Falsification: redundancy with the anchor or existing reversal, non-positive residual information, or failure of cost/stability gates.

## 8. Track C — LowVol robustness, not window search

Do not create a LowVol formula. Reuse the frozen score streams for:

- `P07C_BASE_LOWVOL20`;
- `P07C_DOWNSIDE_VOL60`;
- `P07C_LOWVOL120`.

Evaluate each across the five folds under three fixed views:

1. `ACTION_PATH_STRICT`: positive, present adjustment factors on signal date and every session through the 20-session exit; any factor or endpoint gap denies the observation.
2. `TRADABILITY_PATH_STRICT`: `trade_status=1`, positive volume, and positive amount on signal date, entry, every intervening session, and exit; endpoint-only eligibility is insufficient.
3. `HISTORICAL_UNIVERSE_PIT_SURROGATE`: require the committed historical-as-of membership/lifecycle evidence available in `FREE_DAILY_V1`; current-master-only backfill rows and unknown membership are excluded, never treated as eligible.

Each of the 45 cells records rows, securities, dates, mean RankIC, net spread, and coverage. A view is `UNKNOWN_INSUFFICIENT_COVERAGE` if it retains fewer than 60 securities in a fold or less than 60% of the corresponding reference rows. Otherwise a LowVol score is `ROBUST_ON_AVAILABLE_SURROGATE` only if every sufficiently covered view has positive mean RankIC, at least four of five positive folds in aggregate, pooled mean RankIC at least 50% of its reference value, positive frozen-cost net, and positive 2x-cost net. It is `FRAGILE` on any sufficiently covered hard failure. This is not PIT certification; full PIT and survivorship remain `UNKNOWN`.

## 9. Track D — ElasticNet anchor decomposition

Hyperparameters remain exactly `alpha=0.01`, `l1_ratio=0.5`. No alternate penalty, l1 ratio, seed, solver, scaling, feature selection, or tuning run is allowed.

### 9.1 Coefficient and support stability

Refit the exact anchor once per original fold solely to reproduce its OOS score and extract standardized coefficients. For every base feature and corresponding missingness indicator, retain coefficient, sign, absolute magnitude, and support. Support means `abs(coefficient) > 1e-12`. Stable support means supported in at least four of five folds with the same non-zero sign in at least four folds. Report all ten pairwise fold support Jaccard values.

Group normalized absolute coefficient exposure into:

- Return/Reversal: `ret5`, `ret20`, `ret60`, `ret120` and their indicators.
- Trend: `trend20`, `trend60` and indicators.
- Volatility: `vol20`, `vol60`, `downvol20` and indicators.
- Liquidity/Activity: `amount20`, `volume20`, `volume_ratio20`, `illiq20`, `turnover20` and indicators.
- Data-quality control: `missing20` and its indicator where present.

### 9.2 Four fixed family ablations

Register exactly four predictive configurations, each using the anchor settings and removing one economic family plus its missingness indicators:

- `P07E_ENET_ABL_RETURN_REVERSAL`;
- `P07E_ENET_ABL_TREND`;
- `P07E_ENET_ABL_VOLATILITY`;
- `P07E_ENET_ABL_LIQUIDITY_ACTIVITY`.

No ablation is a promotion candidate. A family is `MATERIAL` only when the full anchor minus ablation has matched mean RankIC delta at least `0.005`, at least three of five fold deltas are positive, and the full anchor has strictly higher frozen-cost net return on matched observations. Otherwise classify it `NON_MATERIAL_AT_THIS_BUDGET` or `AMBIGUOUS` when coverage/integrity is insufficient.

### 9.3 Formula exposure and residual information

Repeat only the exact P0-7D non-negative Formula-span reconstruction with the eight frozen Formula survivors and five leave-one-fold-out checks. Evaluate the held-out residual score against the unchanged target. Stable residual information requires mean residual RankIC at least `0.005` and positive residual RankIC in at least four of five folds. This diagnostic cannot change the anchor or create a new ML configuration.

## 10. Track E — one cross-family interaction

Register exactly one new Formula candidate:

### `P07E_INT_REV5_X_ABTURN`

Let `RANK_t(x)` be average-tie within-date percentile rank and `CENTER(x)=x-0.5`. Use the Track-A turnover innovation and the frozen P0-7C adjusted five-session return:

```text
reversal_component_i,t = CENTER(RANK_t(-ret5_i,t))
shock_intensity_i,t    = RANK_t(abs(innovation_i,t))
raw_interaction_i,t    = reversal_component_i,t * shock_intensity_i,t
score_i,t              = RANK_t(raw_interaction_i,t)
```

The mechanism is very-short reversal amplified by an abnormal-attention event. Do not try another interaction, sign, transform, horizon, or weight. In addition to the ordinary anchor-relative gate, this candidate must show residual mean RankIC at least `0.005` with at least three positive folds relative to both frozen parent components (`P07C_REV5` and `P07E_LIQ_SIGNED_ABTURN_5V60`). Otherwise it is a repackaging and cannot be promoted.

## 11. Standalone, orthogonality, and incremental gates

Use one all-candidate matched panel fixed before results. Scores are converted to centered within-date percentile ranks. Missing evidence is `UNKNOWN`, never favorable.

Each of the three new Formula candidates must first satisfy:

1. five completed OOS folds;
2. mean RankIC at least `0.005`;
3. at least four of five positive fold RankIC values;
4. positive net predictive spread;
5. no fold frozen-cost net return below `-0.20`;
6. no leakage, integrity, or Validator failure.

Then compare it with the anchor:

- signed signal correlation must be below `0.80`;
- mean Top-20 Jaccard must be below `0.80`;
- cross-fold residualize the candidate rank score on the anchor rank score using ordinary least squares on the other four folds, with one intercept, one slope, no penalty, and no return labels; held-out residual mean RankIC must be at least `0.005` with at least three positive folds;
- the equal-weight arithmetic mean of centered within-date anchor and candidate ranks must have strictly higher frozen-cost net return and Sharpe than the anchor on identical observations; strict comparisons use a numerical equality tolerance of `1e-12` only;
- mean RankIC may not fall by more than `0.002`, and positive RankIC folds must remain at least four;
- absolute maximum drawdown may not worsen by more than 5% relative;
- turnover and cost drag may not increase by more than 10% relative;
- positive sufficient regime-cell share may not fall by more than 5 percentage points;
- 2x-cost net return must remain positive;
- at least one of mean RankIC, minimum-fold RankIC, maximum drawdown, or positive regime-cell share must strictly improve.

Passing standalone evidence cannot override a failed orthogonality or incremental gate.

## 12. Deterministic final-pool procedure

Order the three candidates once by:

1. higher anchor-residual mean RankIC;
2. higher minimum residual-fold RankIC;
3. lower anchor signal correlation;
4. lower turnover;
5. ascending experiment ID.

Traverse once from the frozen anchor. Every pool score is the unweighted arithmetic mean of its members' centered within-date percentile ranks. Apply the section-11 matched incremental gate to the current pool and each candidate in this fixed order. Reject failures permanently. Do not backtrack, reorder, enumerate subsets, alter weights, or rerun after seeing results. Run one reverse-order leave-one-out pass over any accepted additions using the same hard limits. The final pool may remain the singleton anchor and can contain at most four members.

The final output is research-only and selected on reused 2019-2025 evidence.

## 13. Track F — Portfolio Baseline V1 and one challenger

Baseline remains the exact `TOP20_EQUAL_WEIGHT` constructor, 20-session rebalance, 5% target weight, and frozen P0-7C cost/execution rules.

The only challenger is `TOP20_EQUAL_WEIGHT_BUFFER_15_25`:

Rank 1 means the highest score; break exact score ties by ascending symbol before applying membership rules.

1. At each rebalance, retain an incumbent while its current score rank is at most 25.
2. Add non-incumbents with rank at most 15 in ascending-rank order until 20 names are held.
3. If fewer than 20 are held, fill from remaining non-incumbents in ascending-rank order.
4. Rebalance all selected names to equal 5% target weights.

This changes only membership hysteresis. No inverse-volatility weight, optimizer, turnover penalty, candidate-specific setting, or alternate buffer is allowed.

Reserve seven evaluations:

1. baseline anchor reproduction;
2-4. baseline anchor-plus-each-new-candidate streams;
5. baseline final pool when distinct from 1-4;
6. challenger anchor;
7. challenger final pool.

Duplicate or inapplicable slots are recorded `NOT_RUN_BY_DESIGN` and remain consumed. The challenger is promoted only if, on both the anchor and a distinct final-pool stream, it strictly improves frozen-cost net return and Sharpe, reduces turnover and cost drag by at least 10%, keeps 2x-cost net positive, and does not worsen absolute maximum drawdown by more than 5%. If no distinct final-pool stream exists, the challenger cannot be promoted from a single stream.

## 14. Regime, stability, decay, and cost metrics

For every promotable candidate and pool state retain:

- mean IC and RankIC, median daily RankIC, hit rate, five fold results, minimum fold, dispersion, and leave-one-fold-out range;
- 5-, 20-, and 60-session RankIC and 60/20 decay ratio;
- gross, frozen-cost, and 2x-cost portfolio outcomes;
- turnover, cost drag, modeled RMB costs, Sharpe, maximum drawdown, worst-fold drawdown, and positive net-return folds;
- direction, volatility, liquidity, and breadth regime cells with counts and sufficient-cell rules unchanged from P0-7D;
- anchor correlation, Top-20 overlap, residual RankIC, incremental pool deltas, complexity, fields, lookbacks, and data limitations.

The cost model remains `SYNTHETIC`; market impact and capacity remain `UNKNOWN`.

## 15. Multiple testing

Do not compute DSR or PBO unless their frozen prerequisites are satisfied. DSR, if valid, remains secondary and must use the cumulative 34-configuration search count plus declared selection degrees. PBO remains `NOT_JUSTIFIED` unless there are at least eight legitimate chronological blocks without destroying chronology.

The primary defenses are fixed budget, pre-registration, retained failures, unchanged walk-forward folds, deterministic selection, cumulative accounting, and the sealed 2026 holdout. Repeated use of 2019-2025 means no P0-7E PASS is independent confirmation.

## 16. Success, rejection, and stop gates

P0-7E succeeds as a research task when all seven configurations and all 35 fold attempts have terminal records, all fixed diagnostics are retained, the deterministic pool procedure closes, the final entity is frozen, and 2026 remains sealed. A singleton final pool and zero new promotions are valid successful outcomes.

Reject a candidate on any failed section-11 gate. Reject the interaction on either parent-residual failure. Do not replace a rejected candidate or reuse its budget.

Stop fail-closed on any source/hash mismatch, anchor reproduction mismatch, ambiguous implementation rule, registry or budget inconsistency, fold/subset change, unregistered result, 2026 materialization, or need for a new choice. Repair may address only the named integrity defect and must rerun the unchanged manifest; it may not change research content.

## 17. Final freeze and next-phase rule

At completion, emit one immutable `P0_7E_FINAL_POOL_FREEZE.json` containing the exact final member list, score combiner, constructor, code/config/data/subset/split/cost hashes, research-result hash, Validator hash, and cumulative experiment count.

Then stop major research on 2019-2025:

- If integrity passes, freeze the final pool and prepare a separate protected-holdout adequacy/go-no-go design. Do not access 2026 under P0-7E.
- If the partial 2026 interval is later judged inadequate without performance access, keep it sealed and defer; do not open P0-7F on the same years.
- If P0-7E identifies a hard PIT/survivorship limitation, record it as a blocker to the claim or to holdout consumption. Additional candidate search does not resolve it.
- Only a materially new external dataset with different evidence properties or an independent result exposing a named defect can justify reopening research scope.

Any later holdout task must evaluate exactly one frozen final pool, use one predeclared primary endpoint, create a pre-access one-run manifest, and forbid tuning or rerun after consumption.

## 18. Required deliverables

- pre-execution manifest and hash-chained seven-configuration registry;
- source, anchor, dataset, subset, split, and holdout-deny audits;
- complete fold-attempt ledger with retained failures;
- three new Formula candidate definitions and results;
- 45-cell LowVol robustness matrix and report;
- fold coefficient/support stability and feature-family exposure report;
- four ablation results and five Formula-span residual checks;
- anchor/candidate orthogonality, correlation, overlap, and residual table;
- one fixed forward-addition ledger and one reverse leave-one-out ledger;
- Portfolio Baseline V1/challenger report with all seven reserved slots;
- cumulative multiple-testing and researcher-degree accounting;
- final research-only pool, full disposition table, and `P0_7E_FINAL_POOL_FREEZE.json`;
- Independent Validator, reproducibility artifact, tests, final report, and checkpoint;
- protected-holdout adequacy/go-no-go handoff without holdout access.

## 19. Prohibited actions

Do not access 2026, execute old P0-7B, broaden the candidate list, scan horizons or parameters, tune ElasticNet, run LightGBM or deeper models, add Size/Value/Quality, call RD-Agent/LLMs, buy data or credits, bind a broker, trade, alter frozen P0-7C/P0-7D evidence, or make production-readiness claims.

## 20. Execution readiness

Design readiness: `YES`.

Execution readiness in Alpha Factory requires a new exact controller directive, a clean and consistent worktree, successful source/hash reproduction, and creation of the pre-execution manifest before results. This ledger commit does not execute P0-7E and does not authorize protected-holdout access.
