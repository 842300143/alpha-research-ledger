# Next Research Work

## Status

`WAIT_FOR_CONTROLLER_DIRECTION`

## Task

`CONTROLLER_INTEGRATION_DIRECTION`

## Decision needed

Choose whether to integrate the fail-closed Exposure02 canonical V1 negative result as-is or authorize a separately versioned corrected replay.

V1's first one-use slot is terminal and cannot be retried. No wealth result, P0 anchor reproduction, P2 evaluation or policy winner exists. Portfolio02 remains valid and unchanged under ADR-0037.

Any replay must use a new task version, additive namespace, corrected grid preflight, committed pre-result manifest and new one-use attempt roster. Keep 2024-2025 and 2026 sealed and all broker, payment, credential, production, destructive Git, force-push and history-rewrite actions forbidden.

## Inputs

- ADR-0039.
- `tasks/completed/EXPOSURE02_CANONICAL_BASELINE_REPLAY_V1.md`.
- `research/exposure/EXPOSURE02_CANONICAL_V1_RESULT_SUMMARY.md`.
- Alpha Factory formal close commit `edc89dba143f8e412fa1b6ffc38b793c72fe3a3e`.

## Stop

Stop pending exact controller direction.
