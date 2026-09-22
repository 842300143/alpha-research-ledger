# EXPOSURE02 canonical-baseline replay V1

Status: `ACTIVE`  
Directive: `ALPHA-EXPOSURE02-CANONICAL-BASELINE-REPLAY-V1`  
Mode: `CORRECTNESS_EQUIVALENT_POLICY_REPLAY`

## Goal

Replay the exact frozen Exposure02 V2 policies P0 AlwaysInvest, P1 AlwaysCash, and P2 Trend60 through the canonical EVALRECON01 account path, reproduce the P0 RMB 50,000 / 1x anchor at RMB 57,445.71, and apply only the preregistered terminal-wealth selection rule.

## Exact scope

- 12 one-use paths: 3 policies × 2 capitals × 2 cost multipliers.
- Primary: RMB 50,000 / 1x cost / full-calendar post-cost compounded terminal wealth.
- Diagnostics: RMB 1,000,000 and 2x cost only.
- Scheduled strategic allocations: exactly 36; no off-grid redistribution after rejected, partial, unavailable, or unfilled orders.
- Allocator regression: 2021-07-05, `000008.SZ`, canonical target 1,100 shares and never 1,200.
- Holding-path gate: `EXACT_FOR_THIS_REPLAY` for every market replay.
- Frozen selection outcomes: `ALWAYS_INVEST_RETAINED`, `SELECTIVE_INVEST_P2_PROVISIONAL`, or `INCONCLUSIVE`.

## Boundaries

Preserve EVALRECON01, Exposure02 V1/V2, and Portfolio02 byte-for-byte. Do not change model, factor, prediction, Top20, EqualWeight, Trend60, grid, allocator objective, costs, event/election policy, capital classification, or selection threshold. Do not access 2024-2025 or 2026 market rows. Do not run new Alpha research or perform broker, payment, credential, production, destructive Git, force-push, or history-rewrite actions.

## Required outputs

Create an additive Alpha Factory namespace, freeze code/config/protocol/attempt queue before results, add the focused canonical-path regressions, execute at most the exact 12 slots once, publish diagnostics and an independent validator, classify full-suite nonpasses, write a formal report/checkpoint, and return a deterministic `CONTROLLER_INTEGRATION_DIRECTION` handoff.

## Bindings

- Alpha Factory EVALRECON01 base: `f58eff5e643cfdd740383197c7ed1bc029b69470`.
- Research Ledger base: `12a56ef0eb6cda8b4b4b1e4ef29ce73c173eb0d0`.
- Alpha Factory activation: `81a0b09cb3b94000a32af4a637caeca9ee1d4338`.
- Canonical artifact committed SHA-256: `019370314303618dcee4c8cd8b72e7527f55c6777fc1fa15d502e0280cec92fd`.
- Decision: ADR-0038.
