# ADR-0038: Authorize Exposure02 canonical-baseline frozen-policy replay

- Status: ACTIVE
- Date: 2026-09-22
- Task: `EXPOSURE02_CANONICAL_BASELINE_REPLAY_V1`
- Directive: `ALPHA-EXPOSURE02-CANONICAL-BASELINE-REPLAY-V1`
- Supersedes: ADR-0037's pending Exposure02 replay direction only

## Decision

Authorize exactly one additive replay of the frozen Exposure02 V2 policy roster—P0 AlwaysInvest, P1 AlwaysCash, and P2 Trend60—through EVALRECON01's authority-bound `CANONICAL_COMMON_BASELINE_V1` account path.

The replay is exactly 12 one-use slots: two capitals (RMB 50,000 primary and RMB 1,000,000 diagnostic), two cost multipliers (1x primary and 2x sensitivity), and the three frozen policies. The canonical allocator reserve configuration, exact 36-date scheduled decision grid, prohibition on off-grid strategic redistribution, event/account semantics, rights election policy, model, prediction stream, Top20, EqualWeight, Trend60, costs, and selection rule are immutable. P0 RMB 50,000 / 1x must reproduce RMB 57,445.71 before P2 may enter policy selection.

Portfolio02 remains valid and frozen. It is not rerun, merged, or promoted by this task. No new policy, threshold, gate, Alpha research, 2024-2025/2026 access, production action, broker order, payment, credential action, destructive Git, or history rewrite is authorized.

## Provenance

- Alpha Factory EVALRECON01 base: `f58eff5e643cfdd740383197c7ed1bc029b69470`.
- Research Ledger EVALRECON01 base: `12a56ef0eb6cda8b4b4b1e4ef29ce73c173eb0d0`.
- Alpha Factory task activation: `81a0b09cb3b94000a32af4a637caeca9ee1d4338`.
- Canonical committed artifact SHA-256: `019370314303618dcee4c8cd8b72e7527f55c6777fc1fa15d502e0280cec92fd`.
- EVALRECON01 disposition authority: ADR-0037.

## Selection and stop gates

Selection uses only full-calendar post-cost compounded terminal wealth at RMB 50,000 / 1x under the original one-cent simplicity/tie rule. RMB 1,000,000 and 2x cost are diagnostics only. Every market path must pass `HOLDING_PATH_EVENT_COVERAGE_GATE=EXACT_FOR_THIS_REPLAY`.

If the P0 canonical anchor fails, stop with `CANONICAL_BASELINE_REPRODUCTION_FAILED` and do not evaluate P2 as a winner. A terminal replay slot is never recycled. Evidence remains `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED_MODELED_EXECUTION`, not independent Alpha confirmation or production evidence.
