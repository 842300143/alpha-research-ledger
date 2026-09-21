# ADR-0022: PIPELINE01 isolated incremental runtime infrastructure

- Status: Isolated result preserved; functional assets integrated under ADR-0024. The original branch named this ADR-0020, which collided with main's EXPOSURE01 ADR-0020. Integration assigned the next available number without altering the branch record.
- Controller directive: `ALPHA-PIPELINE01-INCREMENTAL-RUNTIME-V1`.
- Source execution HEAD: `025f553d75ad83b395790efc2a7cb2f5aa6ea868`.
- Source Ledger HEAD: `ee0c1e283889b7f424a07c164020e8fdd5fb3a48`.
- Execution branch start: `c8b7eecae6338cc7f4843f18d59cf4344d7662c8` (latest state-only commit passing the mandatory worker readiness gate).
- Execution result work commit: `defa004c61a4d9dea098d7acf8f34883225a1311`; close commit: `6dc07aca922f0a710824422baae72a6865d1c940` (`SAFE_TO_CLOSE=YES`).

Decision: keep research search, daily scoring/paper intent, and exact-spec retraining as separate runtimes. Use a repo-native versioned canonical bar contract, provider adapters and overlap qualification, an explicit dependency planner, immutable exact-version local model artifacts, and a replaceable exposure-policy interface. Do not introduce DVC, MLflow, Feast, a hosted registry, or a new data provider during PIPELINE01. This is an engineering compatibility fixture, not a new Alpha test or production activation.

The isolated branch loaded the frozen MODEL01 Ridge F1/S123 artifact only after exact freeze and CAD02 fit-hash verification and labeled it `CURRENT_RESEARCH_FIXTURE`, never `champion`. PITPRICE01 subsequently proved it non-invariant; integration relabels it `SUPERSEDED_RESEARCH_FIXTURE` for explicit research use only. No financial gate is selected here.

Evidence: `SYNTHETIC` acceptance fixture and performance benchmark in Alpha Factory `tests/test_pipeline01.py` and `reports/PIPELINE01_PERFORMANCE.json`; `DOCUMENTED` prior art links and runbooks in `docs/PIPELINE01_INCREMENTAL_RUNTIME_V1.md`; `UNKNOWN` production PIT/tradability and real execution. The existing FREE_DAILY_V1 non-PIT and adjustment coverage limits remain. The one-day fixture path is logically incremental but has a performance warning on a tiny sample.

Merge policy: do not merge/rebase into either source branch while the controller continues source work. Comparing changed paths after the execution source advanced to `6f9fd81f31dcbc241a9a70102ee99a6863fad4f2` shows overlap in `state/CURRENT_STATE.md`, `state/DECISIONS.md`, and `state/NEXT_TASK.md`. Resolve after the source task closes, preserving both histories and frozen artifacts. No protected interval, broker action, purchase, or external LLM call is authorized by this ADR.
