# ADR-0018: MODEL01 fixed model-capacity bakeoff

- Status: Accepted for `MODEL01_MODEL_CAPACITY_BAKEOFF_V1`
- Controller directive: `EXECUTE_MODEL01_MODEL_CAPACITY_BAKEOFF_V1`
- Execution source: Alpha Factory CAD02 `research/cad02/SYSTEM_FREEZE.json`, SHA-256 `b9b999327cedbddc18da568f1c2c7c3953a9e8c8bd50da0c59b8fcb859bac986`

The controller authorizes one fixed model-capacity comparison on the 2019–2023 discovery panel. It crosses CAD02's 16 baseline representatives (F0) and those same inputs plus frozen C1/C2/C3 (F1) with Ridge, ElasticNet, additive GAM, fixed-pair GA2M, and shallow LightGBM. The exact roster, one configuration per family, fixed GA2M pairs, fold accounting, cost comparisons, selection premium, hard-wall enforcement, and fail-closed boundaries are in Alpha Factory `research/model01/PROTOCOL.md` and `CONFIG.json`, to be committed and hash-bound before real MODEL01 results.

CAD02's incomplete calibration remains 15/20 complete with one retained incomplete run and a 2,297.160-second wall-cap deviation. The historical runner and results are immutable. MODEL01 implements a killable child-process wall cap for successor experiments and must validate it independently. No new expression, CAD01 search, CAD02 rerun, 2024–2025 access, 2026 access, external LLM/API, or real order is authorized.

All resulting comparisons are `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`; costs and synthetic sanity checks are `SYNTHETIC`; independent forward validity and production capability remain `UNKNOWN`. A selected complete system is provisional. Any later 2024–2025 test requires a separate exact directive and pre-access manifest.
