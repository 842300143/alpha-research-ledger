# Next Research Work

## Status

`WAIT_FOR_CONTROLLER_DIRECTION`

## Task

`EXPOSURE02_PORTFOLIO02_INTEGRATION_DIRECTION`

## Decision needed

Choose whether and how to bind the corrected Exposure02 `ALWAYS_INVEST_RETAINED` result with the already-valid Portfolio02 sizing result. Decide whether metadata-only integration is sufficient or whether any new combined replay is justified. No replay or integration is authorized by this direction state.

## Inputs

- ADR-0041 and `research/exposure/EXPOSURE02_CANONICAL_V2_RESULT_SUMMARY.md`.
- Alpha Factory result work commit `489a37206674813c6b56983a88702a485dc99776`.
- Alpha Factory report and checkpoint for `EXPOSURE02_CANONICAL_COMPOSITION_REPLAY_V2`.
- Frozen valid Portfolio02 result and its exact commit bindings.

## Stop

Stop pending an exact controller directive. Do not rerun Exposure02 or Portfolio02, create a new policy or sizing candidate, access later market intervals or promote a production system.
