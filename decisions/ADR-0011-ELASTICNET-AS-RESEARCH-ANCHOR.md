# ADR-0011: Treat the P0-7D ElasticNet Member as a Research Anchor

- Status: Accepted
- Date: 2026-09-17

## Context

P0-7D applied the independently predeclared qualification procedure to the exact 17 P0-7C survivors. It retained one member, `P07C_ML_ENET_A010_L50`, after nine additions failed and the singleton passed leave-one-out. Qualification reused selected 2021-2025 OOS evidence.

## Decision

Treat `P07C_ML_ENET_A010_L50` as the current **research anchor** and the sole member of research-only `ALPHA_POOL_V1`. It is the fixed comparator for P0-7E. Do not describe it as independently confirmed, production-proven, or ready for real trading.

## Evidence

- `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`: five fold RankIC values were `0.0802 / 0.0955 / 0.1675 / 0.0951 / 0.1337`; mean was `0.1144`; Formula-relative incremental RankIC was `+0.0165`.
- `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`: frozen-cost net return was `1.0098`, 2x-cost net return was `0.9369`, maximum drawdown was `-14.58%`, and the 60/20 decay ratio was `1.4253`.
- `EMPIRICAL`: P0-7D Validator recorded 16 PASS / 4 UNKNOWN / 0 FAIL and exact reproduction.
- `UNKNOWN`: independent-holdout, PIT, full-survivorship, empirical market-impact, capacity, and production performance.

## Consequences

P0-7E asks whether a mechanism adds information relative to the anchor, not merely whether it has a positive standalone result. Anchor decomposition may explain the result but may not tune `alpha` or `l1_ratio`. A later protected evaluation must test one fully frozen final pool under a separate directive.

## Revisit condition

Revisit only after a new candidate passes the frozen P0-7E incremental gate or a single-run protected evaluation supplies independent evidence.
