# ADR-0002: Adopt the Five-Layer Architecture

- Status: Accepted
- Date: 2026-09-16

## Context

Alpha research fails when data, discovery, evaluation, portfolio construction, and execution assumptions are mixed together. The project needs clear ownership and interfaces without losing end-to-end lineage.

## Decision

Organize the system as L1 Data, L2 Alpha Discovery, L3 Alpha Evaluation, L4 Portfolio, and L5 Execution.

## Evidence / rationale

- `DOCUMENTED`: this architecture is the current controller direction.
- It separates distinct failure modes while retaining a traceable path from source data to feasible fills.
- Current weakness can be stated precisely: L2 and L4 need the most research attention.

## Alternatives

- Treat each strategy as an end-to-end standalone stack.
- Use a three-layer data/model/execution split.
- Organize only around software services rather than research responsibilities.

## Consequences

Interfaces and artifacts need layer ownership. Downstream performance cannot excuse weak upstream integrity. Research plans should name the affected layer and cross-layer dependencies.

## Future revisit condition

Revisit if recurring work does not fit a layer, layer boundaries cause duplicated evidence, or operational experience supports a clearer decomposition.
