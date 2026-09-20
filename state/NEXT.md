# Next Research Work

## Active controller directive

`EXECUTE_CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1` is active under ADR-0016 and `tasks/active/CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1.md`. The execution worker owns the finite readiness repair, evidence reconciliation, pre-result implementation and tests, exact manifest, bounded pilot, checkpoint, and local cross-repository close. This is a new exploratory namespace; it neither reactivates old P0-8D nor changes P0-8D0's 12 investigated / zero executable result.

## Required inputs

- `research/combinatorial-discovery/CAD_RESEARCH_CONTRACT_V1.md`
- `research/combinatorial-discovery/EVIDENCE_AUDIT.md`
- `research/combinatorial-discovery/PRIOR_ART_MAP.md`
- `decisions/ADR-0016-CAD01-EXPLORATORY-SEARCH.md`
- `tasks/completed/P0_8D0_PAIR_DISPOSITION.json`
- Execution `state/NEXT_TASK.md` and the exact P0-8C result/handoff and FREE_DAILY_V1 hashes named in the CAD01 task.

## Stop and continuation

Run only the 2019–2023 research scope, and stop on the frozen budget or any hash, time, leakage, numerical, implementation, or resource gate. Do not load 2024–2025 or 2026, call external LLM/API, or promote an exploratory candidate to Alpha Pool. The execution repository's `research/cad01/state/CHECKPOINT.json`, append-only attempt ledgers, and exact manifest are the resume state. `ALPHA-CAD-RESUME` plus both repository paths means follow those files and the five execution state files; do not restart counters or use chat memory. A future task is chosen after the pilot report, including a valid zero-candidate outcome.
