# ADR-0040: Authorize Exposure02 canonical contract-composition replay V2

- Status: ACTIVE
- Date: 2026-09-22
- Task: `EXPOSURE02_CANONICAL_COMPOSITION_REPLAY_V2`
- Directive: `ALPHA-EXPOSURE02-CANONICAL-COMPOSITION-REPLAY-V2`
- Supersedes: ADR-0039's pending replay direction only

## Decision

Authorize one additive V2 replay that composes, without rewriting either parent, the frozen Exposure02 V2 strategy contract with EVALRECON01's canonical execution contract. Strategy authority owns P0/P1/P2 identity, the exact 36-date `SIGNAL_GRID_CONTRACT_V2`, Top20 intent, and the unchanged strict-positive Trend60 rule. Execution authority owns allocator reserves, integer targets, orders, fills/rejections, residual cash, T+1, lots, fees/slippage, tradability, corporate actions, rights elections, holdings, NAV, and account boundaries.

The implementation must directly load the frozen grid artifact and prove the four V1 binding drifts before any replay. A new `EXPOSURE02_CANONICAL_COMPOSITION_V2` manifest must bind both immutable parents. Independent pre-result review is required before the first V2 slot.

The first slot is P0 / RMB 50,000 / 1x and must reproduce RMB 57,445.71, 14.89142%, the 2021-07-05 `000008.SZ` target of 1,100 shares, exactly 36 strategic allocations, zero off-grid strategic reallocations, and `HOLDING_PATH_EVENT_COVERAGE_GATE=EXACT_FOR_THIS_REPLAY`. Failure consumes that slot and stops the remaining eleven slots. On PASS, complete the exact P0/P1/P2 × RMB 50,000/RMB 1,000,000 × 1x/2x one-use matrix.

Primary selection uses only RMB 50,000 / 1x full-calendar post-cost terminal wealth and may return `ALWAYS_INVEST_RETAINED`, `SELECTIVE_INVEST_P2_PROVISIONAL`, or `INCONCLUSIVE`. P1 is cash reference; 2x and RMB 1,000,000 are diagnostics.

Portfolio02 remains valid, frozen, and read-only. Its current diagnostics are Equal RMB 57,445.71, Rank RMB 59,600.99, and Score RMB 56,813.97; RankWeight remains provisional.

## Provenance and boundaries

- Alpha Factory V1 close: `5d716551f59dcce41dd16419efe763031863136e`.
- Research Ledger V1 close: `462df798234784ab4b56a5118867c7c420d2c234`.
- EVALRECON01 Alpha Factory: `f58eff5e643cfdd740383197c7ed1bc029b69470`.
- EVALRECON01 Research Ledger: `12a56ef0eb6cda8b4b4b1e4ef29ce73c173eb0d0`.
- Frozen decision-grid SHA-256: `595998e5ef083f9d22da00975e9dbab1ea12b3653d08669e60a59a39974ecc93`.

All predecessor results remain immutable. Do not access 2024-2025 or 2026, create new Alpha research, mutate Portfolio02, place broker orders, purchase data, use credentials, deploy, force-push, or rewrite history.
