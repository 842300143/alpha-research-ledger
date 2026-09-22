# ADR-0039: Accept Exposure02 canonical V1 fail-closed disposition

- Status: ACCEPTED
- Date: 2026-09-22
- Task: `EXPOSURE02_CANONICAL_BASELINE_REPLAY_V1`
- Supersedes: ADR-0038 active execution state only

## Decision

Accept `EXPOSURE02_CANONICAL_BASELINE_REPLAY_V1` as `INCONCLUSIVE_IMPLEMENTATION_PREFLIGHT_GATE / FAIL_CLOSED`. Preserve the mandatory first P0 / RMB 50,000 / 1x slot as `FAILED_NO_RETRY`. Do not recycle that slot or execute the remaining eleven V1 slots. No terminal wealth, P0 canonical reproduction, P2 comparison, or Exposure policy selection exists.

Portfolio02 remains valid and unchanged under ADR-0037. The RMB 57,445.71 canonical artifact is not invalidated: the V1 child stopped before the account loop because the canonical task configuration was used to rebuild a V2-identity grid contract, producing `FROZEN_GRID_CONTRACT_DRIFT` in task identity, four historical V1 source bindings, and the derived payload hash.

Any further replay requires a separately versioned controller directive, corrected preflight coverage, a new additive namespace and manifest, and a new one-use attempt roster. An in-place V1 repair or retry is forbidden.

## Evidence

- Alpha Factory failure-evidence work commit: `b010422812cb707109548854e6855c004900682c`.
- Alpha Factory formal close commit: `edc89dba143f8e412fa1b6ffc38b793c72fe3a3e`.
- Report: `D:/alpha-factory-exposure02-canonical-v1/reports/EXPOSURE02_CANONICAL_BASELINE_REPLAY_V1.md`.
- Checkpoint: `D:/alpha-factory-exposure02-canonical-v1/state/checkpoints/EXPOSURE02_CANONICAL_BASELINE_REPLAY_V1.json`.
- Focused tests: 10 PASS / 0 FAIL.
- Fail-closed closure validator: 10 PASS / 0 FAIL.
- Full isolated-worktree suite: 278 PASS / 18 FAIL / 1 WARNING; the nonpasses retain the EVALRECON01 external-fixture/frozen-hash classification.

Evidence is `EMPIRICAL_EXECUTION_RECORD` for the attempt/failure only. Market wealth and a policy winner are `UNKNOWN_NOT_PRODUCED` / `UNKNOWN_NOT_SELECTED`.

## Boundaries

The 2024-2025 and 2026 intervals remained sealed. EVALRECON01, Exposure02 V1/V2, and Portfolio02 remain unchanged. No Alpha research, broker order, payment, credential action, production action, destructive Git, force push, or history rewrite occurred.

