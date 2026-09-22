# ADR-0036: EVALRECON01 common-baseline reconciliation

- Status: ACTIVE
- Date: 2026-09-22
- Directive: `ALPHA-EVALRECON01-COMMON-BASELINE-RECONCILIATION-V1`
- Mode: `CORRECTNESS_RECONCILIATION_ONLY`

## Decision

Authorize one additive reconciliation of the committed Exposure02 V2 P0 AlwaysInvest + EqualWeight path and Portfolio02 EqualWeight + AlwaysInvest path. The authority order is PIT correctness contracts, Integration02 contracts, `SIGNAL_GRID_CONTRACT_V2`, then the frozen Exposure02/Portfolio02 protocols.

The execution repository may create `CANONICAL_COMMON_BASELINE_V1` and replay only the necessary common baseline to prove exact deterministic equality. It must not modify either frozen result, select an implementation by return, rerun challenger policies, revise a winner, tune parameters, or access 2024-2025/2026 market rows.

## Evidence status

The two historical terminal values are `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` under modeled execution assumptions. Until reconciliation completes, the cause and joint usability are `UNKNOWN`.

## Boundaries

No model, factor, Top20, EqualWeight, capital, actual cost assumption, corporate-action policy, or rights-election change. No new Alpha, broker action, payment, credential action, production action, destructive Git action, or history rewrite.
