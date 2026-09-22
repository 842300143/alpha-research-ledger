# ADR-0034: PORTFOLIO02 PIT-corrected sizing evaluation

- Status: Accepted research disposition on isolated branch.
- Task: `PORTFOLIO02_PIT_CORRECTED_SIZING_EVALUATION_V1`
- Controller directive: `ALPHA-PORTFOLIO02-PIT-CORRECTED-SIZING-EVALUATION-V1`
- Alpha Factory base: `a1bee7a5d07dd69c28eb8ba5892bc58db42aefb4`
- Alpha Factory pre-result commit: `d43daca43956331b9f9ab781d5f2424df0ad5957`
- Alpha Factory result commit: `c4d49d782cc34c5666fc5f581f9d45ca45096ab8`
- Research Ledger base: `ef1f1d1ca1ae51231816101ab519099dd7549870`
- Outcome: `RANK_WEIGHT_PROVISIONAL`
- Evidence: `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` for the bounded historical comparison; `SYNTHETIC` for research-account costs and execution assumptions; production behavior `UNKNOWN`.

## Decision

Retain canonical `RANK_WEIGHT_V1` as the provisional sizing policy for the corrected `REQUAL01_RIDGE_F1_S123_V2` ordered Top20 under `ALWAYS_INVEST`. Selection is solely by the preregistered RMB 50,000, 1x-cost, full-calendar terminal-wealth metric using the primary `INTEGER_TARGET_APPROXIMATION_V1` allocator. Terminal wealth is RMB 59,600.99 for RankWeight, RMB 57,445.71 for EqualWeight and RMB 56,813.97 for ScoreTilt.

Greedy allocation, RMB 1,000,000 capital, 2x costs, fractional weights, drawdown, bimonthly and concentration outputs remain diagnostics and cannot select a policy. EqualWeight narrowly leads RankWeight by RMB 42.41 in the 50k/2x-cost sensitivity, so the RankWeight result is cost-sensitive and remains provisional. ScoreTilt retains only relative within-date cross-sectional meaning; it is not an absolute-return forecast or profit probability.

## Integrity basis

The pre-result manifest froze the allocator roles and 15-attempt queue before wealth. All 15 attempts completed with no retry or slot recycling. All three policies consumed the same 36 ordered Top20 decisions, account start, execution rules, costs and corporate-action semantics. Every replay passed `HOLDING_PATH_EVENT_COVERAGE_GATE=EXACT_FOR_THIS_REPLAY`. The Alpha Factory independent validator reports 16 PASS / 0 FAIL, and the full repository suite reports 259 PASS / 0 FAIL / 0 ERROR with one unchanged pandas warning.

No EXPOSURE02 result or Cash Gate was consumed. No joint exposure-sizing optimization occurred. No 2024–2025 or 2026 market row was accessed. No broker order, credential action or production deployment occurred.

## Artifacts

- Report: `reports/PORTFOLIO02_PIT_CORRECTED_SIZING_EVALUATION_V1.md`
- Checkpoint: `state/checkpoints/PORTFOLIO02_PIT_CORRECTED_SIZING_EVALUATION_V1.json`
- Result bundle: `research/portfolio02/results/RESULT_BUNDLE.json`, SHA-256 `29ee4e917c89367fb73f6bd35d91379e243a62d05707ebad09b900b0413a8528`
- Diagnostics: `research/portfolio02/results/DIAGNOSTICS.json`, SHA-256 `6b9c275575b7f4290a795d35e6b3d5fdfc428d71cc638b828a394397bec341df`
- Validator: `research/portfolio02/VALIDATOR_RESULT.json`, SHA-256 `d256d328ba699ff311c0bc7735fe16bac285083e4e0278106e9fb8a1fad730e8`

ADR numbers 0032 and 0033 are reserved by the independent parallel EXPOSURE02 lineage; this record uses ADR-0034 solely to avoid a merge collision and does not consume that task's result substance.

## Next

Wait for `CONTROLLER_JOINT_DIRECTION`. This ADR does not authorize a joint replay, parameter scan, later-period test, broker action or deployment.
