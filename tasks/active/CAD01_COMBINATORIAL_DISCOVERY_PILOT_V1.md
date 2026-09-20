# CAD01 Combinatorial Discovery Pilot V1

- Task ID: `CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1`
- Directive: `EXECUTE_CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1`
- Scope: new `EXPLORATORY_SEARCH` only, separate from P0-8D/P0-8D0
- Research repository: `D:\alpha-research-ledger`
- Execution repository: `D:\alpha-factory`
- Source P0-8C result payload hash: `995efd57f952c9ddfb5527f992225764bb7ce22814f7a28478492f66e04e9c12`
- Source P0-8C handoff payload hash: `2502ac870d0767db8839665ca664251e7652b7e493e7c6986719f993486ccb4c`
- Source FREE_DAILY_V1 dataset ID hash: `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`

Read `research/combinatorial-discovery/{CAD_RESEARCH_CONTRACT_V1,EVIDENCE_AUDIT,PRIOR_ART_MAP}.md`, ADR-0016, the execution `state/NEXT_TASK.md`, config, pre-execution manifest, attempt ledger, and checkpoint. Follow exact hash and chronology checks. No 2024–2025 or 2026 market row access, no RD-Agent/LLM/API, no paid data, broker, or trading.

Required conclusion: engine readiness, pilot status, evidence level, budget used and stop reason, all proposal/duplicate/invalid/failed counts, matched delta and cost checks, source hashes, local commit SHAs, and honest remote sync state. Zero candidates is acceptable. On technical failure, retain attempts and close with a safe resumable status; do not silently repair an exposed run.

For a later worker, `ALPHA-CAD-RESUME` with both repository paths means recover the five execution state files, run `worker_start`, verify the manifest and ledger, inherit the cumulative budget and queue position, and perform only the recorded next action.
