# Alpha Research Ledger Agent Policy

## Source of truth

- This repository is the research, controller, knowledge, and history source of truth.
- Chat history, prior sessions, and remembered context are not sources of truth.
- `alpha-factory` remains the execution, code, data pipeline, and experiment-result source of truth.
- Begin work by reading `state/CURRENT.md`, `state/NEXT.md`, relevant decisions, and the active task specification.

## Repository boundary

- Do not execute market experiments, data pipelines, backtests, Shadow runs, or broker operations in this repository.
- Put important Codex task specifications in `tasks/` and execute them in `alpha-factory`.
- Link Alpha Factory results by exact commit SHA and report or artifact path.
- Preserve research lineage from idea or paper through hypothesis, experiment, task, result, review, and decision.

## Historical integrity

- Preserve failed ideas, negative results, superseded hypotheses, and abandoned approaches.
- Add new decisions or superseding ADRs instead of rewriting old decisions to look current.
- Do not invent empirical evidence, commit SHAs, dataset hashes, or results. Use `UNKNOWN / TO_BACKFILL` when needed.
- Label evidence as `EMPIRICAL`, `DOCUMENTED`, `SYNTHETIC`, or `UNKNOWN`.
- Do not alter frozen or protected evaluation records except through an explicitly authorized additive correction.

## Security and storage

- Never store secrets, credentials, API keys, tokens, or `.env` contents.
- Do not commit raw market datasets, large generated caches, virtual environments, or Docker artifacts.
- Prefer Markdown metadata and notes for papers; do not commit large PDF collections to ordinary Git history.
- Consider Git LFS only after a specific need is documented and approved.

## Traceability

Use stable identifiers and record, where applicable:

- task ID and experiment ID
- research decision ID
- Alpha Factory start and end commit SHA
- report and artifact paths
- dataset ID and immutable hash
- result classification and review outcome

## CAD01 resume

For `ALPHA-CAD-RESUME` with both repository paths, read `state/CURRENT.md`, `state/NEXT.md`, ADR-0016, the CAD01 contract and task, then recover Alpha Factory through its five state files and `python scripts/worker_start.py`. Verify its pre-execution manifest, append-only attempt and cost ledgers, cumulative budget, checkpoint, and exact next queue position. Never infer progress from chat memory, reset a consumed slot, or open the locked 2024–2025 or 2026 intervals.
