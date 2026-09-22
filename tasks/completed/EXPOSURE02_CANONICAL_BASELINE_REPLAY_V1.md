# EXPOSURE02 canonical-baseline replay V1

Status: `COMPLETE / INCONCLUSIVE_IMPLEMENTATION_PREFLIGHT_GATE / FAIL_CLOSED`  
Directive: `ALPHA-EXPOSURE02-CANONICAL-BASELINE-REPLAY-V1`  
Mode: `CORRECTNESS_EQUIVALENT_POLICY_REPLAY`

The exact 12-slot task stopped on its mandatory first slot. `P0_ALWAYS_INVEST / RMB 50,000 / 1x` was consumed once and ended `FAILED_NO_RETRY` on `FROZEN_GRID_CONTRACT_DRIFT` before the account loop or any wealth result. The remaining eleven slots were not started. P0 reproduction, P2 evaluation and Exposure policy selection are `NOT_EXECUTED`, `NOT_EXECUTED`, and `NONE`.

The frozen task protocol forbids retrying a terminal slot. V1 therefore remains closed; any future replay must be a separately versioned controller task with a corrected preflight and new one-use roster. Portfolio02 remains valid and unchanged.

Alpha Factory failure-evidence work commit: `b010422812cb707109548854e6855c004900682c`. Formal close commit: `edc89dba143f8e412fa1b6ffc38b793c72fe3a3e`. Decision: ADR-0039.

No later market interval or external irreversible action was accessed.

