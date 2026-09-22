# ADR-0037: Accept the EVALRECON01 reconciled common baseline

- Status: ACCEPTED
- Date: 2026-09-22
- Task: `EVALRECON01_COMMON_BASELINE_RECONCILIATION_V1`
- Supersedes: ADR-0036 active execution state only

## Decision

Accept EVALRECON01 as `PASS_WITH_WARNINGS / COMMON_BASELINE_RECONCILED`. `CANONICAL_COMMON_BASELINE_V1` is the authority-bound AlwaysInvest + EqualWeight + RMB 50,000 + 1x modeled-cost path and ends at RMB 57,445.71.

The historical RMB 678.13 difference begins at the 2021-07-05 decision / 2021-07-06 account day. Exposure02 used allocator reserves `0 / 5 / 0.0018`; the authority-bound mapping is `100 / 5 / 0.0003`, producing 1,200 rather than 1,100 shares of `000008.SZ`. Exposure02 also dynamically reallocated after a rejected exit on 2021-09-01, creating 45 allocation invocations rather than the authorized 36.

Portfolio02's common path is valid and requires no correctness replay. Exposure02 V2's historical evidence remains frozen, but its winner cannot be carried forward until a separately versioned task replays the exact frozen policy roster under `CANONICAL_COMMON_BASELINE_V1`. This ADR does not authorize that replay or reselect a winner.

## Evidence

Alpha Factory formal work commit `7189c2201e6bf1d6350eb5f67820a8f29128f61b`; exact result publication commit `c403312bd8397b3999ec1e0505688ecb814b9571`. Primary report: `D:/alpha-factory-evalrecon01/reports/EVALRECON01_COMMON_BASELINE_RECONCILIATION_V1.md`. Formal checkpoint: `D:/alpha-factory-evalrecon01/state/checkpoints/EVALRECON01_COMMON_BASELINE_RECONCILIATION_V1.json`.

All 36 decisions, predictions, ordered Top20 candidates, canonical integer targets, 872 orders, 17 rejections, 855 fills, 287 event checks, and 727 daily rows reconcile. Terminal wealth is exact. The maximum numeric representation difference is `2.842170943040401e-14`, below the frozen `1e-8` account tolerance. Additive Independent Validator V2 passes 21/21 while preserving the earlier mechanical validator failure.

Evidence remains `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED_MODELED_EXECUTION`. It is not independent Alpha confirmation or production evidence.

## Boundaries

No predecessor result was modified. No Alpha, parameter, policy, capital, cost, model, factor, candidate, event, election, or winner change occurred. The 2024-2025 and 2026 market intervals remained sealed. No broker, payment, credential, production, destructive Git, or history-rewrite action is authorized.
