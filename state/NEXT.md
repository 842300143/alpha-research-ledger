# Next Research Work

## EXPOSURE01 authorization history (2026-09-21)

`EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1` was authorized under ADR-0019 and is archived at `tasks/completed/EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1.md`. The former MODEL01 direction wait was superseded only for this bounded 2019–2023 exposure comparison. Alpha Factory start HEAD was `aeebb5493e2805d1fcaea81cfb6fdc64f3014b90`; the Ridge F1 freeze SHA-256 is `d7dcd4a2ebf930e805fc14fc9e059b4bd126b2c7b0054f4451ef8e559893deb7`. Neither 2024–2025 nor 2026 test access was authorized.

## Current next direction after EXPOSURE01

Alpha Factory `EXPOSURE01_CAUSAL_PRICE_REPAIR_DIRECTION` is `WAIT_FOR_CONTROLLER_DIRECTION`. V1 closed `INCONCLUSIVE_CORRECTNESS_GATE` at work commit `87b4bbe2f87081b46182ffb1c2dd18a8aa78b198` under ADR-0020. Its six completed slots and failed validator are preserved. A controller may separately authorize a new, forward as-of adjusted-price/account experiment with fresh manifest and attempt accounting, or defer. The direction task itself authorizes no replay, 2024–2025 or 2026 access, future test, or trading.

## Active controller directive

`MODEL01_MODEL_CAPACITY_BAKEOFF_V1` is complete under ADR-0018. The matching Alpha Factory next task is `GEN2_LOCKED_ONE_SYSTEM_TEST_DIRECTION`, a controller direction request only. Review the one frozen Ridge F1 versus Ridge F0 system, CAD02's incomplete calibration and overrun, accumulated model-selection bias, PIT/survivorship gaps and synthetic costs. A possible 2024–2025 test needs a separate exact directive and pre-access manifest. The 2026 holdout remains sealed.

## Completed task

`CAD02_SYNERGY_CALIBRATION_AND_SYSTEM_FREEZE_V1` is complete under ADR-0017 with a technically frozen S123 provisional research system and an incomplete synthetic calibration. The calibration exceeded its six-hour wall cap by 2,297.160 seconds, which is retained as a protocol deviation. The exact result, limits, and work commit are in `research/combinatorial-discovery/CAD02_RESULT_SUMMARY.md` and the Alpha Factory report/checkpoint. CAD01 remains complete and immutable. Old P0-8D/P0-8D0 remains 12 investigated, zero executable, unrun.

## Recommended next routine task

`CAD03_ONE_SYSTEM_TEST_DIRECTION` is the matching Alpha Factory `state/NEXT_TASK.md` direction request. The controller may review whether the exact technically frozen S123-versus-S0 system should enter one separately specified 2024–2025 research test, given the incomplete calibration and selection-contaminated evidence. This direction request does not authorize data access. A later exact directive, immutable bindings and pre-access manifest are required; 2026 remains sealed.

## Resume

`ALPHA-CAD-RESUME` with both repository paths means recover repository state through Alpha Factory `worker_start`, its five mandatory state files, the frozen CAD01 contract and completion artifacts, and the active Alpha Factory task/checkpoint. CAD01 and CAD02 are complete; do not restart either, reset a consumed slot, or infer progress from chat memory. Keep 2024–2025 and 2026 unopened absent a new exact directive and manifest.
