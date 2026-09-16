# ADR-0005: Simple ML Before Deep Models

- Status: Accepted
- Date: 2026-09-16

## Context

Nonlinear factor interactions are a priority, but flexible models increase overfitting risk, infrastructure demands, and interpretation difficulty.

## Decision

Begin ML research with transparent linear and simple nonlinear baselines before deep models. Increase model complexity only when controlled out-of-sample, post-cost evidence demonstrates incremental value.

## Evidence / rationale

- `DOCUMENTED`: ML should first study nonlinear factor interactions.
- Simpler baselines make leakage, feature contribution, stability, and failure analysis easier to inspect.
- `UNKNOWN`: no current empirical evidence justifies a specific deep architecture.

## Alternatives

- Begin with deep learning.
- Restrict all research to linear models.
- Select models solely by validation performance.

## Consequences

Experiments require baseline ladders and matched data/splits. Model complexity becomes an explicit treatment, not an assumed improvement.

## Future revisit condition

Revisit after simple models establish a stable baseline and a predefined deep-model experiment shows reproducible incremental value after costs and multiple-testing treatment.
