# P0_7D_ALPHA_POOL_QUALIFICATION_V1

- Task ID: `P0_7D_ALPHA_POOL_QUALIFICATION_V1`
- Status: `COMPLETE` / `P0_7D_PASS_WITH_WARNINGS`
- Intended execution repository: `D:\alpha-factory`
- Research repository: `D:\alpha-research-ledger`
- Evidence classification: design is `DOCUMENTED`; reused P0-7C results are `EMPIRICAL_RESEARCH_ONLY`; any P0-7D pool result remains research-only and selection-contaminated until separately tested

## 1. Goal

Use only the exact frozen P0-7C OOS survivors and their 2021-2025 score/result evidence to determine which signals provide distinct and additive information. Produce `ALPHA_POOL_V1`, including a justified empty pool when appropriate, without creating a predictive configuration or accessing the protected 2026 holdout.

P0-7D is qualification and research governance, not Generation-2 discovery and not protected-holdout confirmation.

## 2. Frozen source binding

Alpha Factory commits must resolve in this ancestry order:

1. Protocol: `95dc8e3c5b895fe7bf47135536e0ed4843b73471`.
2. Result: `a881bd956c70088100f85999e7f0f4f965777a25`.
3. Completion checkpoint: `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138`.

Bind before execution:

- Dataset: `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`.
- Canonical result-bundle hash: `30f0879579906af2d341a9053f9090b19616fbd3facd7415461b5ae247329444`.
- Pool-audit hash: `9121c1984a237f7555171fea15bca882febfc4284e26a44c1527456ab4878f62`.
- Candidate results: `research/alpha_v1/results/CANDIDATE_RESULTS.json`.
- Portfolio results: `research/alpha_v1/results/PORTFOLIO_RESULTS.json`.
- Signal correlation: `research/alpha_v1/diagnostics/SIGNAL_CORRELATION.json`.
- Portfolio overlap and descriptive incremental audit: `research/alpha_v1/diagnostics/POOL_OVERLAP_INCREMENTAL_AUDIT.json`.
- ML comparison: `research/alpha_v1/diagnostics/ML_INCREMENTAL.json`.
- Lifecycle history: `research/alpha_v1/registry/ALPHA_POOL.json` and `research/alpha_v1/registry/POOL_QUALIFICATION.json`.
- Validator: `research/alpha_v1/VALIDATOR_RESULT.json`.

The historical `ALPHA_POOL.json` file contains a nine-name provisional correlation/decay shortlist. It is input evidence, not prior final membership, and must not be rewritten.

## 3. Exact input population

The input is exactly these 17 `OOS_SURVIVED` candidates, verified against the frozen registry and candidate result bundle:

### Formula survivors

1. `P07C_BASE_LIQ_TURN20` — Liquidity.
2. `P07C_LIQ_SHOCK20` — Liquidity.
3. `P07C_LIQ_TURN_PERSIST60` — Liquidity.
4. `P07C_REV5` — Reversal.
5. `P07C_REV20` — Reversal.
6. `P07C_DOWNSIDE_VOL60` — Volatility.
7. `P07C_LOWVOL120` — Volatility.
8. `P07C_BASE_LOWVOL20` — Volatility.

### ML survivors

9. `P07C_ML_LINEAR`.
10. `P07C_ML_ENET_A001_L10`.
11. `P07C_ML_ENET_A001_L50`.
12. `P07C_ML_ENET_A010_L10`.
13. `P07C_ML_ENET_A010_L50`.
14. `P07C_ML_LGB_D2_L7`.
15. `P07C_ML_LGB_D3_L7`.
16. `P07C_ML_LGB_D3_L15`.
17. `P07C_ML_LGB_D4_L15`.

No rejected, decaying, replacement, regenerated, or newly proposed candidate may enter. Candidate count other than 17 is a hard stop.

## 4. Zero-search rule

P0-7D permits:

- integrity verification and exact reproduction of frozen P0-7C scores through 2025;
- deterministic re-expression of those scores for matched comparison;
- predeclared correlation, overlap, regime, formula-span, equal-weight pool, forward-addition, and leave-one-out calculations;
- one top-20 equal-weight portfolio evaluation per frozen candidate or fixed pool state when needed for qualification.

P0-7D permits zero new predictive configurations, features, targets, horizons, formulas, model fits to returns, hyperparameters, seeds, portfolio constructors, candidate-specific costs, weighting schemes, or parameter searches. A score/result mismatch must stop the task; it cannot be repaired by retraining or substitution.

If persisted dated scores are insufficient, the worker may run the exact frozen P0-7C code/configuration solely to reproduce the canonical through-2025 score streams. Reproduction must match the frozen candidate results before qualification begins. This is a reproducibility gate, not a new experiment.

## 5. Protected holdout

The interval 2026-01-05 through 2026-09-15 remains sealed.

- `HOLDOUT_ACCESSED = FALSE` is mandatory.
- `HOLDOUT_CONSUMED = FALSE` is mandatory.
- Loaders must deny before materialization and cap all score, label, outcome, IC, portfolio, regime, coverage, and ranking data at 2025-12-31.
- Calendar metadata may verify the exclusion boundary but may not reveal performance, NAV, ranking, or candidate-selection information.
- No P0-7D execution manifest may reserve or consume a protected-holdout run.

Any 2026 outcome row in memory, cache, output, or log is a hard failure.

## 6. Matched comparison panel

Before viewing P0-7D qualification output, freeze one matched panel:

- daily predictive comparisons use only dates and symbol-date rows available for every candidate being compared;
- pairwise correlation and overlap use the exact matched pair rows/dates;
- pool construction uses the intersection of eligible signal dates and symbols across all 17 candidates;
- portfolio evaluation uses non-overlapping 20-session observations and the exact P0-7C label, next-session entry, T+1, 100-share lot, missing/tradability, cost, and 2x-cost-stress rules;
- all pool scores are formed by converting each member to its within-date percentile rank centered at zero and then taking an unweighted arithmetic mean.

Record the row, date, symbol, fold, and non-overlapping-observation counts before qualification. Do not change the panel because a candidate performs poorly.

## 7. Qualification dimensions

Every candidate must receive a complete evidence row. Missing evidence is `UNKNOWN`, never silently favorable.

| Dimension | Frozen measures |
| --- | --- |
| Predictive power | Mean IC, mean RankIC, median daily RankIC, RankIC hit rate, and net predictive spread. |
| OOS fold consistency | Five fold results, positive-fold count, minimum fold RankIC, fold dispersion, and leave-one-fold-out aggregate range. |
| Post-cost behavior | Top-20 equal-weight gross, frozen-cost net, cost drag, and 2x-cost net on the matched panel. |
| Turnover | Total and per-rebalance turnover under the baseline constructor. |
| Drawdown | Maximum drawdown and worst fold drawdown. |
| Cost sensitivity | Change from zero cost to frozen cost and from frozen cost to 2x cost. |
| Alpha decay | Frozen 5-, 20-, and 60-session RankIC plus the existing 60-to-20 decay ratio. |
| Signal correlation | P0-7C signal-correlation definition on matched OOS rows. |
| Top-N overlap | Mean Top-20 Jaccard overlap on matched signal dates. |
| Regime coverage | Positive and negative sufficient cells, minimum sufficient-cell RankIC, and coverage across direction, volatility, liquidity, and breadth regimes. |
| Complexity | Formula = 0, linear = 1, ElasticNet = 2, shallow LightGBM = 3. Lower is simpler. |
| Data dependency | Exact fields, lookbacks, action-factor dependency, model dependency, and known PIT/survivorship/tradability limitations from frozen manifests. |
| Incremental contribution | Fixed-order forward-addition and reverse-order leave-one-out results under sections 11 and 12. |

The 2021 fold weakness, non-PIT data, partial historical-delisted coverage, synthetic costs, and unavailable market impact remain attached to every output.

## 8. Deterministic redundancy rules

Evaluate all 136 unordered candidate pairs. Create a redundancy edge when any rule below is true:

1. Signal correlation is greater than or equal to `0.80`.
2. Mean Top-20 Jaccard overlap is greater than or equal to `0.80`.
3. The pair belongs to the same Formula family or the same ML model class and either signal correlation or Top-20 overlap is greater than or equal to `0.70`.

Correlation is signed, not absolute: a negatively correlated, correctly oriented survivor is not redundant merely because the magnitude is large. Record which rule or rules created every edge.

Family membership is fixed by the P0-7C registry. The ML classes are linear, ElasticNet, and LightGBM. Multiple variants do not survive merely because each passed standalone gates.

## 9. ML composite decomposition

Use the eight Formula survivor score streams as a fixed explanatory basis. This diagnostic uses no return labels.

For each of the nine ML candidates:

1. Center and scale every score cross-section using the frozen within-date rank transform.
2. For each outer fold, fit non-negative least squares with an intercept to reconstruct the ML score from the eight Formula scores using the other four OOS folds.
3. Evaluate reconstruction `R²` on the held-out fold.
4. Use no penalty, feature selection, threshold search, or alternate basis.

An ML candidate is `REDUNDANT_COMPOSITE` when median held-out `R² >= 0.80` and at least four of five held-out folds have `R² >= 0.70`. It is also `REDUNDANT_COMPOSITE` if it has a section-8 redundancy edge to a Formula candidate and fails to show positive matched incremental RankIC over the best matched Formula stream.

Standalone strength cannot override this classification. Retain the five reconstruction results and exact Formula contributions for interpretation.

## 10. Deterministic preference and de-duplication

Sort candidates once by the following lexicographic key:

1. More positive RankIC folds.
2. Higher minimum fold RankIC.
3. Larger share of positive sufficient regime cells.
4. Lower complexity tier.
5. Lower turnover.
6. Lower frozen-cost drag.
7. Higher mean RankIC.
8. Ascending experiment ID.

Before this sort, remove candidates classified `REDUNDANT_COMPOSITE`. Then traverse the sorted list once. Retain a candidate only if it has no redundancy edge to an already retained candidate. Otherwise mark it `REDUNDANT` or `REDUNDANT_FAMILY_VARIANT` and record the preferred candidate and decisive comparison key.

This produces one deterministic maximal independent set. Do not try another sort, reorder after observing additions, or search graph subsets.

## 11. Fixed forward-addition procedure

Process the de-duplicated candidates in the unchanged section-10 order. There is no backtracking and a rejected addition is never reconsidered.

### First member

Traverse the fixed section-10 order until a candidate satisfies all anchor conditions. Candidates that fail are recorded as `NEGATIVE_ADDITION` and the traversal continues; their failure does not change the order. The first passing candidate becomes the provisional anchor only if all are true:

- mean RankIC is positive;
- at least four of five fold RankIC values are positive;
- top-20 equal-weight frozen-cost net return is positive;
- top-20 equal-weight 2x-cost net return is positive;
- no leakage, integrity, data-quality, or validator failure applies.

If no candidate meets the anchor gate, output an empty `ALPHA_POOL_V1`.

### Later additions

For each later candidate, compare the current pool with the pool after adding that candidate on the same matched observations. Compute changes in:

- combined mean and minimum-fold RankIC;
- frozen-cost net return and Sharpe;
- positive net-return folds and fold RankIC dispersion;
- maximum drawdown;
- turnover, cost drag, and 2x-cost net return;
- positive sufficient regime-cell share and minimum sufficient-cell RankIC.

Accept the addition only when all conditions hold:

1. Frozen-cost net return and Sharpe both strictly increase, using a numerical equality tolerance of `1e-12` only.
2. Mean RankIC does not fall by more than `0.002`, and the count of positive RankIC folds does not fall below four.
3. Absolute maximum drawdown does not worsen by more than 5% relative to the current pool.
4. Turnover and cost drag each do not increase by more than 10% relative to the current pool.
5. The share of positive sufficient regime cells does not fall by more than 5 percentage points.
6. The after-addition pool remains positive under 2x cost.
7. At least one of these also strictly improves: mean RankIC, minimum-fold RankIC, maximum drawdown, or positive regime-cell share.

Otherwise classify the candidate as `NEGATIVE_ADDITION` and retain every before/after metric. These tolerances are frozen materiality limits, not values to tune.

## 12. Reverse-order leave-one-out

After the single forward pass, inspect accepted members once in reverse addition order. Compare the current pool with that member removed on the same observations.

Treat the pool without the member as the section-11 "before" state and the pool with the member as the "after" state. Retain the member only if the with-member pool has both strictly higher frozen-cost net return and strictly higher Sharpe and satisfies every section-11 hard limit. Otherwise remove it as `REMOVED_LEAVE_ONE_OUT` and continue with the smaller pool.

Run one reverse pass only. Do not re-add removed members, rerun forward selection, test another order, or enumerate combinations.

## 13. `ALPHA_POOL_V1` output

The pool has no target size. Zero members is valid and preferable to unsupported inclusion.

For every final member record:

- candidate ID and lifecycle status;
- family and economic hypothesis copied from the frozen registry;
- OOS IC, RankIC, hit-rate, and predictive-spread metrics;
- all five fold results and stability diagnostics;
- gross, frozen-cost, and 2x-cost portfolio metrics;
- turnover, cost drag, and drawdown;
- 5/20/60-session decay status;
- signal-correlation and Top-20-overlap profile;
- regime profile and sample counts;
- complexity tier and data dependencies;
- ML Formula-span result where applicable;
- forward-addition and leave-one-out marginal contribution;
- evidence classification and retained limitations.

Also output the full disposition table for all 17 candidates using only: `ALPHA_POOL_V1`, `REDUNDANT`, `REDUNDANT_FAMILY_VARIANT`, `REDUNDANT_COMPOSITE`, `NEGATIVE_ADDITION`, `REMOVED_LEAVE_ONE_OUT`, or `INTEGRITY_FAILURE`.

## 14. Multiple testing and selection degrees of freedom

Preserve the P0-7C search history exactly:

- predictive configurations: 27;
- configuration-fold attempts: 135;
- Formula: 18;
- ML: 9;
- maximum observed DSR probability: `0.4228853062141328`;
- PBO: `NOT_JUSTIFIED`.

P0-7D adds zero predictive configurations and zero predictive fold attempts. It does add qualification degrees of freedom, which must be counted and reported:

- 136 pairwise redundancy decisions;
- at most 45 ML Formula-span held-out score-reconstruction checks;
- at most 17 anchor/forward-addition decisions;
- at most 17 leave-one-out decisions;
- one ordering rule, one equal-weight score combiner, and one portfolio constructor.

No alternate threshold, ordering, weight, constructor, candidate subset, or regime rule may be run. The pool result is selected on reused OOS evidence and therefore cannot be described as statistically independent confirmation. Weak DSR evidence remains a material warning.

## 15. Required artifacts

The later Alpha Factory execution must produce at minimum:

- pre-execution P0-7D manifest with all source hashes and the exact 17 candidates;
- holdout deny-before-load audit with `HOLDOUT_ACCESSED = FALSE`;
- matched-panel manifest and integrity/reproduction result;
- 17-row qualification table;
- 136-pair redundancy table and graph;
- ML Formula-span report;
- fixed-order forward-addition ledger with all negative additions;
- reverse-order leave-one-out ledger;
- `ALPHA_POOL_V1.json`, including a justified empty result when applicable;
- multiple-testing and selection-degree report;
- Generation-2 research-question handoff;
- Independent Validator result, tests, report, and completion checkpoint.

## 16. Generation-2 handoff questions

P0-7D must answer, without executing, which narrow questions deserve a future `P0_7E_ALPHA_RESEARCH_V2` design:

1. Liquidity: why did turnover persistence, liquidity shock, and low turnover differ from illiquidity and raw volume definitions?
2. Reversal: are 5- and 20-session effects distinct mechanisms or liquidity/microstructure variants?
3. LowVol: does the effect survive stronger action, PIT, survivorship, and tradability controls?
4. ElasticNet: which Formula exposures explain it, and what residual information remains?
5. Cross-family interactions: is there one economically motivated interaction suggested by residual rather than redundant information?
6. Portfolio: what single, predeclared change could plausibly beat top-20 equal weight after costs?

Do not turn these questions into a broad grid, execute them, or allocate a larger LightGBM budget under P0-7D.

## 17. Success gate

P0-7D succeeds when:

- all exact 17 survivors are evaluated;
- all 136 pairwise relationships are recorded;
- Formula-span redundancy is assessed for all nine ML survivors;
- the one fixed forward and leave-one-out procedure completes;
- negative and removed additions remain visible;
- `ALPHA_POOL_V1` members or a justified empty pool are produced;
- zero new predictive search occurs;
- the protected 2026 holdout remains sealed;
- qualification degrees of freedom and weak DSR evidence remain explicit;
- bounded Generation-2 research questions are produced.

Profitability and non-empty membership are not success requirements.

## 18. Stop conditions

Stop fail-closed if a source commit or hash mismatches, the input list is not exactly 17, any candidate lacks five frozen folds, exact P0-7C results cannot be reproduced, a 2026 outcome row is accessed, a rule is ambiguous in implementation, or the worker would need a new predictive configuration or parameter choice.

Do not repair data, replace a candidate, alter a threshold, access either protected holdout, call RD-Agent/LLMs, buy data, bind a broker, trade, or make a production claim under this task.

## 19. Execution result

Alpha Factory executed the frozen design without adding a predictive configuration. The exact 17 survivors were reproduced on a 78,091-row all-candidate matched panel, all 136 pairs and 45 ML Formula-span held-out reconstructions were evaluated, and deterministic de-duplication left 10 candidates. One forward pass accepted only `P07C_ML_ENET_A010_L50`; nine additions were rejected. The singleton anchor was retained in the one reverse leave-one-out decision.

`ALPHA_POOL_V1` therefore contains one **research-only anchor**, not an independently confirmed or production-proven Alpha. Its matched-panel evidence is:

- fold RankIC `0.0802 / 0.0955 / 0.1675 / 0.0951 / 0.1337`;
- mean RankIC `0.1144`, with 5/5 positive folds;
- Formula-relative incremental RankIC `+0.0165`;
- frozen-cost net return `1.0098` and 2x-cost net return `0.9369`;
- maximum drawdown `-14.58%`;
- 60/20 decay ratio `1.4253`, classified as not decaying;
- material singleton contribution under leave-one-out.

Seven candidates were redundant family variants. Three ElasticNet variants showed Formula-relative increments; the other six ML candidates, including every LightGBM candidate, failed incremental classification. The maximum prior DSR probability remains `0.4228853062141328`. Qualification reused selected OOS evidence and is not independent confirmation. The 2026 holdout remained unaccessed and unconsumed.

## 20. Execution trace

- Protocol commit: `76568528ed1a7c70d6b0a93b76924d7cb943dc94`.
- Result commit: `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63`.
- Completion checkpoint: `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0`.
- Result payload hash: `d06b21fe5bcea2b394be0d6b7a09006a2518aaf37d04933631b4a5b49fbcb360`.
- Matched-panel hash: `68f1aee1a3f099f0167392bc4cbc3f5ab9b6494bca98170b54e4e46516c22538`.
- Reports: `reports/P0_7D_ALPHA_POOL_QUALIFICATION_REPORT.md`; `reports/P0_7D_CHECKPOINT.json`; redundancy, Formula-span, multiple-testing, and Generation-2 handoff reports.
- Results: `research/alpha_pool_v1/results/RESULT_BUNDLE.json`; `ALPHA_POOL_V1.json`; `QUALIFICATION_TABLE.json`; `REDUNDANCY_TABLE.json`; `ML_FORMULA_SPAN.json`.
- Validator: 16 PASS / 4 UNKNOWN / 0 FAIL; repository tests 107/107.
