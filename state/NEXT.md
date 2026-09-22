# Next Research Work

## Status

`ACTIVE`

## Task

`EXPOSURE02_CANONICAL_COMPOSITION_REPLAY_V2`

## Decision needed

Execute ADR-0040's exact contract-composition replay in a new additive namespace.

V1's first one-use slot remains terminal and is not retried. V2 receives a new roster only after immutable strategy and execution parents, the authority matrix, implementation, protected guards, and independent pre-result review are frozen.

Run P0 / RMB 50,000 / 1x first. Stop on any grid, parent, authority, canonical baseline, holding-path, or protected-boundary failure. On PASS, complete the other eleven exact matrix slots and select only from the frozen legal outcomes.

## Inputs

- ADR-0040.
- ADR-0039 and `tasks/completed/EXPOSURE02_CANONICAL_BASELINE_REPLAY_V1.md`.
- Alpha Factory V1 close `5d716551f59dcce41dd16419efe763031863136e`.
- EVALRECON01 commits `f58eff5e643cfdd740383197c7ed1bc029b69470` and `12a56ef0eb6cda8b4b4b1e4ef29ce73c173eb0d0`.

## Stop

Stop on a named fail-closed gate or after committed result, validation, checkpoint, and handoff.
