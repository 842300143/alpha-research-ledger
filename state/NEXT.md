# Next Research Work

## Active controller directive

`MODEL01_MODEL_CAPACITY_BAKEOFF_V1` is authorized under ADR-0018 for a pre-registered 2019–2023 five-model, two-representation comparison. The 2024–2025 test and 2026 holdout remain closed. Await the Alpha Factory checkpoint and a separate later controller decision before any future test.

## Completed task

`CAD02_SYNERGY_CALIBRATION_AND_SYSTEM_FREEZE_V1` is complete under ADR-0017 with a technically frozen S123 provisional research system and an incomplete synthetic calibration. The calibration exceeded its six-hour wall cap by 2,297.160 seconds, which is retained as a protocol deviation. The exact result, limits, and work commit are in `research/combinatorial-discovery/CAD02_RESULT_SUMMARY.md` and the Alpha Factory report/checkpoint. CAD01 remains complete and immutable. Old P0-8D/P0-8D0 remains 12 investigated, zero executable, unrun.

## Recommended next routine task

`CAD03_ONE_SYSTEM_TEST_DIRECTION` is the matching Alpha Factory `state/NEXT_TASK.md` direction request. The controller may review whether the exact technically frozen S123-versus-S0 system should enter one separately specified 2024–2025 research test, given the incomplete calibration and selection-contaminated evidence. This direction request does not authorize data access. A later exact directive, immutable bindings and pre-access manifest are required; 2026 remains sealed.

## Resume

`ALPHA-CAD-RESUME` with both repository paths means recover repository state through Alpha Factory `worker_start`, its five mandatory state files, the frozen CAD01 contract and completion artifacts, and the active Alpha Factory task/checkpoint. CAD01 and CAD02 are complete; do not restart either, reset a consumed slot, or infer progress from chat memory. Keep 2024–2025 and 2026 unopened absent a new exact directive and manifest.
