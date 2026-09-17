# ADR-0009: Qualify the Alpha Pool Before Further Broad Search

- Status: Accepted
- Date: 2026-09-17

## Context

P0-7C produced 17 broad OOS survivors but also 18 signal-correlation pairs above 0.80, five Top-20 overlap pairs above 0.80, and a mixed fixed-order additive audit. No explicit pooled incremental threshold had been frozen, so strict pool membership remained empty.

## Decision

Run `P0_7D_ALPHA_POOL_QUALIFICATION_V1` on the exact 17 frozen survivors before authorizing broad Generation-2 candidate search. Freeze deterministic redundancy, ML-composite, forward-addition, and leave-one-out rules first. Zero pool members is a valid result.

## Evidence / rationale

- `EMPIRICAL_RESEARCH_ONLY`: individual OOS survival did not imply distinct or additive information.
- `EMPIRICAL_RESEARCH_ONLY`: the non-selective nine-name audit contained additions that reduced net return, Sharpe, or both.
- `DOCUMENTED`: controlling selection degrees of freedom is more valuable than adding configurations before the existing evidence is resolved.
- Maximum DSR probability was only `0.4228853062141328`, so statistical-certainty claims are unsupported.

## Alternatives

- Treat all 17 survivors as independent Alphas.
- Promote the nine-name provisional shortlist as final.
- Begin a broad Generation-2 parameter grid immediately.
- Abandon all survivors without qualification.

## Consequences

P0-7D adds no predictive configurations and preserves all negative additions. Generation-2 directions must be justified by residual mechanisms or gaps found during qualification. Pool output remains research-only because it reuses P0-7C OOS evidence.

## Future revisit condition

Revisit after P0-7D produces `ALPHA_POOL_V1` or a justified empty result and identifies a narrow, predeclared research question that cannot be answered by the frozen population.
