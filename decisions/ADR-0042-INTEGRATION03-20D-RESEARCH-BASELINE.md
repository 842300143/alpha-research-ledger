# ADR-0042: Accept the Integration03 20-session research baseline

- Status: ACCEPTED
- Date: 2026-09-22
- Task: `INTEGRATION03_20D_RESEARCH_BASELINE_FREEZE_V1`
- Supersedes: the Integration03 active integration state only

## Decision

Accept `CURRENT_20D_RESEARCH_BASELINE_V1` as a provisional, selection-contaminated research baseline with separately registered components:

- dataset: `FREE_DAILY_PIT_V2`;
- prediction model: `REQUAL01_RIDGE_F1_S123_V2`;
- target: 20-session relative return;
- rebalance: every 20 sessions;
- candidates: `TOP20_SELECTION_V1`;
- sizing: `RANK_WEIGHT_V1 / PROVISIONAL_RESEARCH_SIZING`;
- exposure: `P0_ALWAYS_INVEST`;
- execution/account: EVALRECON01 canonical modeled path, RMB 50,000 / 1x primary;
- corporate action: exact event-aware under the frozen election policy and per-replay exact gate.

Keep `20D_CANONICAL_EQUAL_WEIGHT_COMPARATOR_V1` separate and canonical. EqualWeight ends at RMB 57,445.71 (+14.89142%) on the primary path. RankWeight ends at RMB 59,600.99 (+19.20198%) but remains provisional and cost-sensitive: at 2x costs EqualWeight ends at RMB 52,155.30 versus RankWeight at RMB 52,112.89. ScoreTilt is not promoted.

Retain AlwaysInvest for the current frozen 20D system. The canonical exposure endpoints are P0 RMB 57,445.71, P1 RMB 50,000.00 and P2 Trend60 RMB 46,117.88. The Trend60 rejection is scope-limited to this system and is not a general rejection of cash gates or trend exposure.

## Horizon provenance

The repository documents P0-7A as a one-session forward target with weekly rebalance and P0-7C as the first confirmed 20-session target plus 20-session rebalance coupling. It does not document an empirical comparison selecting 20 sessions. Record the current horizon as `DIRECT_DESIGN_ASSUMPTION / NOT_EMPIRICALLY_SELECTED`.

The next task is `HORIZON01_MULTI_HORIZON_PREDICTION_RESEARCH_DESIGN`, design only. This ADR does not authorize its execution. `SHORTLIST01` remains a separate branch and is not part of the frozen baseline.

## Preserved evidence

Preserve without rewrite: the original Exposure02 pre-result failure, GridFix V2 and its superseded execution result, EVALRECON01, canonical replay V1's terminal `FAILED_NO_RETRY`, and canonical-composition V2's passing result. The integration used normal merges and no replay.

Alpha Factory validation is 18/18 independent checks and 8/8 focused tests. A selected combined source suite is 45 pass and one inherited Windows checkout-byte hash failure; no full-suite PASS is claimed.

The Alpha Factory work commit is `204bf7513e8baff852ef290734a548e4391ddb69` and its normal master merge is `5655926d199ed294028af8c37de22d451c17a46d`. The Research Ledger work commit is `930f1582ad7e8e349c029e8de4f49ecd4d8046d2` and its normal main merge is `64079e57c7e06c951b994a4dd739cb391cb651e1`.

## Boundaries

Production champion remains `NONE`; confirmed Alpha remains `NO`; evidence remains `SELECTION_CONTAMINATED_RESEARCH`. The task accessed neither 2024-2025 nor protected 2026 rows and performed no new Alpha research, replay, deployment, broker, payment or credential action.
