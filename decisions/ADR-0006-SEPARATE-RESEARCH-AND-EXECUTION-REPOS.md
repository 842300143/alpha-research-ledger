# ADR-0006: Separate Research Ledger and Execution Repositories

- Status: Accepted
- Date: 2026-09-16

## Context

Long-lived research reasoning and decision history have different storage and review needs from code, data pipelines, runtime artifacts, and experiment outputs.

## Decision

Use `alpha-research-ledger` for research, control, knowledge, and history. Keep `alpha-factory` as the execution, code, data pipeline, and experiment-result plane. Do not use Git submodules.

## Evidence / rationale

- `DOCUMENTED`: the controller requires this repository boundary.
- Stable cross-repository identifiers preserve lineage without coupling checkout state.
- Separating the planes reduces pressure to mix large data or mutable runtime artifacts into durable research history.

## Alternatives

- Keep everything in Alpha Factory.
- Use a monorepo with strict subdirectories.
- Link repositories with Git submodules.

## Consequences

Tasks and decisions must record Alpha Factory commit SHAs, report paths, artifact IDs, experiment IDs, and dataset IDs or hashes. Missing links remain explicitly `UNKNOWN / TO_BACKFILL`.

## Future revisit condition

Revisit if cross-repository traceability becomes unreliable despite the link indexes, or if operational evidence shows a monorepo would preserve history more safely.
