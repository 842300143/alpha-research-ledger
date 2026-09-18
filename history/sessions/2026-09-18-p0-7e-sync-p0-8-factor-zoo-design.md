# P0-7E Sync and P0-8 Factor Zoo Design Session — 2026-09-18

## Scope

Synchronize completed P0-7E evidence from Alpha Factory and design `P0-8 FACTOR ZOO & FACTOR STRUCTURE DISCOVERY V1`. This session changed only the Research Ledger. It executed no market experiment, data pipeline, backtest, factor value, label, ranking, IC, portfolio, Shadow run, protected-holdout evaluation, RD-Agent/LLM call, payment, broker action, or trade.

## Verified execution lineage

- P0-7E protocol commit: `f3523ac72ed6995f3d0342d6b28d25fb5f78fb4b`.
- Result commit: `27793d974110758ccf83848aed3d9354341b7e3f`.
- Completion checkpoint: `c37ab3caf0c50c100906503d17d05fd5f78e2e24`.
- Result payload hash: `bd2b6bc841ed948237ddac98777d43d38f89a28e27d9d5de99bee4d9031746d4`.
- Final-freeze hash: `7399a25d212caa7b1a6c68c8f7ac8a362fbffeefd6d92f9168ca0b902f9364b8`.
- Validator hash: `fa7ef94392d1b9b440247baa93dcd48b07526d6f7b5229ccc8d9c5eb12f13275`.

Alpha Factory was inspected read-only and remained clean and unchanged.

## P0-7E synchronization

P0-7E closed Generation 1. It completed seven configurations, 35 attempts, 45 LowVol robustness cells, four fixed family ablations, Formula-span residual checks, deterministic selection, and portfolio slots. All three new Formula candidates passed standalone gates and failed the full anchor-relative gate. No new member was promoted. The strict pool remained `P07C_ML_ENET_A010_L50`; the constructor remained `TOP20_EQUAL_WEIGHT`. The 2026 holdout remained sealed and unconsumed.

## Data capability review

The actual price schema contains daily OHLC, preclose, volume, amount, turnover, provider pct_change, trade/suspension/ST status and provenance fields. The adjustment schema contains adj_factor and action metadata. Price-return families remain limited to the action-aware subset. Liquidity/activity inputs are ready with warnings. Market composites can be derived only from the eligible universe. Size, Value, Quality, industry, authoritative historical limits, and certified PIT/survivorship remain unavailable or not ready.

## Policy change

ADR-0014 clarifies that ADR-0013 ended the P0-7/Generation-1 refinement path; it did not prove the canonical factor space exhausted or permanently prohibit new preregistered research. P0-8 is permitted because it asks a materially different structure question and imposes a canonical registry, fixed budgets, FDR, retained failures, factor clustering, and continued holdout isolation.

## P0-8 design

- 103 draft definitions across 20 families.
- 99 atomic/transformed definitions for P0-8B.
- Four conditional prototypes reserved for P0-8D.
- 89 concepts and 89 parameterization groups.
- Common rank and fixed winsorized-zscore views.
- 2021-2023 Stage-1 structure research; 2024-2025 one-pass internal reuse validation only after structure and interactions freeze.
- Global BH-FDR at q=0.10 using 1,000 shared within-date label permutations.
- Four-layer factor map: signal correlation, IC-series correlation, Top-20 overlap, and cross-fitted residual information.
- Maximum 12 hypothesis-led interactions; brute-force pairs prohibited.
- Sparse model budget: one Ridge and two ElasticNet configurations maximum; LightGBM/deep/RL zero.

## Resulting state

- P0-7E: `COMPLETE` / `P0_7E_PASS_WITH_WARNINGS`.
- Generation-1 anchor: `P07C_ML_ENET_A010_L50` / research-only.
- P0-8A: `DESIGN_READY` / `NOT_YET_EXECUTED`.
- Registry definitions frozen: `NO`; P0-8A no-result code/hash freeze required.
- Protected 2026 holdout: `SEALED / UNACCESSED / UNCONSUMED`.
- Next durable state: `CONTROLLER_DIRECTION` for exact P0-8A activation.
