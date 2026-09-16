# ADR-0003: Defer the RD-Agent LLM API Pilot

- Status: Accepted / Deferred
- Date: 2026-09-16

## Context

The RD-Agent environment is installed, but an LLM-backed pilot requires an API credential and likely paid usage. The free research path has not yet demonstrated the specific incremental value needed to justify that cost.

## Decision

Keep the RD-Agent LLM pilot at `PAUSED_CREDENTIAL_REQUIRED`. Do not obtain credentials or incur API cost solely to resume it.

## Evidence / rationale

- `DOCUMENTED`: RD-Agent installation is complete.
- `DOCUMENTED`: the LLM-backed pilot is paused because no credential is available.
- `UNKNOWN`: incremental research productivity or alpha value from this pilot has not been empirically established.

## Alternatives

- Purchase API access now.
- Remove RD-Agent from the roadmap.
- Limit current work to environment preparation and non-LLM evaluation.

## Consequences

The environment remains available, while current resources focus on free data, explicit hypotheses, and controlled experiments. No claim is made about RD-Agent effectiveness.

## Future revisit condition

Revisit when a well-scoped pilot has success metrics, a bounded budget, a comparison baseline, and a specific bottleneck that an LLM could plausibly remove.
