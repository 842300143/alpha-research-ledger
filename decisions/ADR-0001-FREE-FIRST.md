# ADR-0001: Free First

- Status: Accepted
- Date: 2026-09-16

## Context

The project can currently progress through free data sources, open tools, and local computation. Paid data and LLM APIs create recurring cost before their incremental research value is established.

## Decision

Use free research paths first. Do not pay for data or LLM APIs until work identifies a specific bottleneck and credible evidence shows that paying is worth removing it.

## Evidence / rationale

- `DOCUMENTED`: controller policy is `FREE FIRST`.
- `DOCUMENTED`: the RD-Agent environment is installed, while its LLM-backed pilot is paused because no credential is available.
- No empirical claim is made that free sources are sufficient for every future phase.

## Alternatives

- Buy premium data immediately.
- Fund an LLM API pilot immediately.
- Avoid all paid services permanently.

## Consequences

Near-term work emphasizes free-data coverage, provenance, and robust baselines. Some capabilities may remain deferred. The policy is a sequencing rule, not a permanent ban.

## Future revisit condition

Revisit when a documented research objective is blocked by a measurable data or model limitation, free alternatives have been tested, and the expected incremental value and budget are explicit.
