# CAD01 source evidence audit

Classification: `DOCUMENTED` source reconciliation over frozen `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` P0-8A/B/C artifacts. No new label or outcome was loaded for this audit.

## Binding and actual universe

| Item | Verified value | Meaning |
| --- | --- | --- |
| `FREE_DAILY_V1` dataset hash | `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | Manifest dataset ID; its full 3,207 priced securities were **not** all used in P0-8B/C. |
| P0-8C result self-hash | `995efd57f952c9ddfb5527f992225764bb7ce22814f7a28478492f66e04e9c12` | Recomputed from canonical payload excluding self-hash. |
| P0-8D handoff self-hash | `2502ac870d0767db8839665ca664251e7652b7e493e7c6986719f993486ccb4c` | Recomputed from canonical payload excluding self-hash. |
| P0-8B actual subset | 72 symbols | Frozen action-aware subset; 69–71 minimum eligible per fold. |
| P0-8B evaluation signal panel | 52,344 symbol-date rows, 2021-01-04 through 2023-12-29 | Panel includes 97 factor columns; actual valid rows vary by factor. |
| P0-8B factor population | 97 evaluated atomic/transformed definitions | Two zero-sum definitions excluded before results. |
| P0-8C representative population | 16 representatives of 27 survivors | 16 archetypes from 351 pair decisions. |
| Sequential explanation set | first representative plus nine `DISTINCT_INCREMENT` cross-cluster tests = 10 | Historical, ordered regression diagnostic with the frozen 0.005/0.25/2-fold thresholds. It does **not** prove ten statistically independent or economic market dimensions. |

The P0-8B coverage artifact gives 15,380–15,967 valid rows per factor per fold in the 16-representative set. These are signal coverage counts before a new complete-case baseline, label-end purge, and matched candidate comparison; they must not be presented as CAD01 effective model sample sizes.

## Exact 16 representatives

Formulas below are the frozen registry's pseudocode, with its signed direction and raw-field dependencies. `adj_*` are adjustment-factor derived. `r1` is one-session adjusted return.

| Cluster | Factor | Frozen formula | Direction | Required raw fields |
| --- | --- | --- | --- | --- |
| C01 | `FZ1_BAR_004` | `-mean((adj_high-max(adj_open,adj_close))/(adj_high-adj_low) over 20)` | higher better | open, high, low, close, adj_factor |
| C02 | `FZ1_BAR_005` | `mean((min(adj_open,adj_close)-adj_low)/(adj_high-adj_low) over 20)` | higher better | open, high, low, close, adj_factor |
| C03 | `FZ1_COR_004` | `corr(r1, delta(equal_weight_positive_return_share) over 60)` | higher better, diagnostic | close, adj_factor |
| C04 | `FZ1_DST_001` | `-skew(r1[t-59:t])` | higher better | close, adj_factor |
| C05 | `FZ1_DTR_005` | `mean(worst ceil(0.05*120) r1 values over 120)` | higher better | close, adj_factor |
| C06 | `FZ1_GAP_004` | `sum(log(adj_open[s]/adj_close[s-1]) over 20)` | higher better | open, close, adj_factor |
| C07 | `FZ1_GAP_005` | `sum(overnight_log_return,20)-sum(log(adj_close/adj_open),20)` | higher better | open, close, adj_factor |
| C08 | `FZ1_LIQ_005` | `-std(amount,20)/(mean(amount,20)+1e-12)` | higher better | amount |
| C09 | `FZ1_MKT_002` | `-cov(r1,market_r1,252)/(var(market_r1,252)+1e-12)` | higher better | close, adj_factor |
| C10 | `FZ1_MKT_005` | `-std(OLS_residual(r1~market_r1) over 60)` | higher better | close, adj_factor |
| C11 | `FZ1_REV_003` | `-(adj_close[t-5] / adj_close[t-20] - 1)` | higher better | close, adj_factor |
| C12 | `FZ1_REV_004` | `-max(r1[t-19:t])` | higher better | close, adj_factor |
| C13 | `FZ1_TOV_001` | `-mean(turnover[t-19:t])` | higher better | turnover |
| C14 | `FZ1_TOV_003` | `-log((mean(turnover,t-4:t)+1e-12)/(mean(turnover,t-64:t-5)+1e-12))` | higher better | turnover |
| C15 | `FZ1_TOV_004` | `-OLS_slope(log1p(turnover[t-19:t]) ~ 0..19)` | higher better | turnover |
| C16 | `FZ1_VOL_004` | `-std(rolling_std_10(r1)[t-59:t])` | higher better | close, adj_factor |

## Ordered ten-item historical diagnostic

`FZ1_BAR_004` is the first representative. The nine subsequent cross-cluster `DISTINCT_INCREMENT` classifications are `R012 FZ1_BAR_005`, `R013 FZ1_COR_004`, `R014 FZ1_DST_001`, `R015 FZ1_DTR_005`, `R016 FZ1_GAP_004`, `R017 FZ1_GAP_005`, `R020 FZ1_MKT_005`, `R022 FZ1_REV_004`, and `R024 FZ1_TOV_003`. The other six later representative tests were `PARTIALLY_DISTINCT`; none was deleted. The 10 items are an explanatory set chosen by order and thresholds, not CAD01's terminal set and not a proof of independent dimensions.

## Interpretation corrections

- P0-8C's label-free residual OLS fitted WF2/WF3 to evaluate WF1 (and analogous other-fold fits). This is retrospective cross-fitting. CAD01 prediction fits and standardization must use data strictly available before each evaluation fold; none of those residual coefficients or series is a CAD01 terminal.
- `R004` is `FZ1_VOL_005` against identical `FZ1_MKT_005`: residual RankIC is exactly zero after the retained machine-noise repair, yet the old residual Top-20 portfolio net return is about 0.05999 decimal. The old portfolio helper accepts all-zero scores, `nlargest(20, keep="first")` takes the first rows in input order, and 20 selected securities can earn or lose market return while incurring costs. That outcome is order/tie and exposure dependent, not residual Alpha. CAD01 must classify zero and all-tie scores explicitly and calculate no candidate-attributable portfolio increment from them.
- `FZ1_MKT_005`/`FZ1_VOL_005` share a known definition-level identity; `FZ1_RNG_002`/`FZ1_VOL_006` were empirically equal on the observed panel. Mathematical equality, same-date rank equivalence under a monotone transform, and high correlation are separate tests. High correlation alone cannot cancel a paired incremental test.
- `PARTIALLY_DISTINCT` and `REDUNDANT` are classifications under the historical residual protocol. They are not unconditional information independence or causal findings.

Sources: `research/factor_structure_v1/results/{RESULT_BUNDLE,ARCHETYPE_REGISTRY,RESIDUAL_INFORMATION,FACTOR_GRAPH}.json`, `research/factor_structure_v1/handoff/P0_8D_HANDOFF.json`, `research/factor_zoo_v1/registry/FACTOR_REGISTRY_V1.json`, `research/factor_evaluation_v1/results/COVERAGE_MISSINGNESS.json`, and the frozen P0-8A/B manifests. The old 12-pair disposition remains 12 investigated, zero executable, unrun.
