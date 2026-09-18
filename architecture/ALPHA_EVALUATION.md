# L3 Alpha Evaluation

## Objective

Measure predictive usefulness and reject unstable, redundant, overfit, or post-cost unusable candidates.

## Core evidence

- IC and RankIC level, distribution, and stability.
- Cross-period, cross-regime, and cross-sectional robustness.
- Alpha decay and intended holding horizon.
- Correlation and incremental contribution relative to the Alpha Pool.
- Turnover, fees, slippage, and capacity-sensitive behavior.
- Multiple-testing and researcher-degrees-of-freedom treatment.

## Evaluation sequence

Use development and validation evidence before protected Blind. Freeze candidate, dataset, split, code, configuration, and comparison set before any approved Blind access.

## Protected Blind

The old P0-7B Blind is `SUPERSEDED_UNCONSUMED` under ADR-0007; `BLIND_CONSUMED = FALSE`. Preserve it but never execute it. P0-7C completed five annual walk-forward OOS folds through 2025 without accessing the protected 2026 holdout. P0-7D and Generation-2 research also exclude 2026 under ADR-0010.

## Current qualification boundary

P0-7D qualified the exact 17 P0-7C survivors and produced a one-member research-only `ALPHA_POOL_V1`: `P07C_ML_ENET_A010_L50`. Ten candidates remained after de-duplication, but nine forward additions failed. Because qualification reused selected OOS evidence, the member is a comparator and research anchor rather than independent confirmation.

P0-7E requires every new candidate to pass standalone stability, anchor-relative residual RankIC, correlation and overlap limits, matched post-cost incremental contribution, regime, drawdown, turnover, and 2x-cost gates. One deterministic order and one reverse leave-one-out pass produce the final pool. The cumulative search history is never reset.

ADR-0013 originally directed the post-P0-7E state to a separate protected-holdout adequacy/go-no-go decision. ADR-0014 preserves the frozen pool and holdout boundary while permitting a materially different, preregistered P0-8 factor-space program. No P0-7E or P0-8 result can authorize 2026 access.

## P0-8 evaluation and structure

P0-8 separates atomic evidence from structure and model combination. P0-8B evaluates frozen atomic/transformed definitions on 2021-2023 using common preprocessing, global BH-FDR over a shared empirical permutation null, stability, decay, missingness, cost, and regime diagnostics. P0-8C then builds a multiplex Factor Graph from signal correlation, daily IC-series correlation, Top-20 overlap, and cross-fitted residual information.

Only after clusters and representatives are frozen may P0-8D register at most 12 mechanism-led interactions. The 2024-2025 tranche is opened once in P0-8E as `INTERNAL_REUSE_VALIDATION`; those years were already used in Generation 1 and do not become independent confirmation. The 2026 holdout remains sealed through P0-8G.
