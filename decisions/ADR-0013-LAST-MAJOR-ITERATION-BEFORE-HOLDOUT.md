# ADR-0013: Make P0-7E the Last Major 2019-2025 Research Iteration Before a Holdout Decision

- Status: Accepted
- Date: 2026-09-17

## Context

The 2019-2025 sample has supported 27 predictive configurations, 135 fold attempts, P0-7D qualification choices, and repeated interpretation. Continuing Generation N on the same period would compound researcher overfitting. The 2026-01-05 through 2026-09-15 protected interval remains sealed and contains only a partial year.

## Decision

P0-7E is the final major candidate-generation iteration on 2019-2025. After it closes, freeze exactly one final research pool—possibly the unchanged singleton anchor—and move to a separate `freeze -> protected-holdout adequacy/go-no-go` decision. Do not authorize P0-7F candidate generation on the same sample.

If P0-7E integrity or reproduction fails, repair only that named defect and rerun the unchanged preregistered protocol. If the partial holdout is inadequate, leave it sealed and defer; do not return to open-ended Generation N. A known free-data PIT or survivorship limitation may block a claim or holdout consumption, but it does not justify additional search on 2019-2025.

## Evidence

- `EMPIRICAL`: the cumulative pre-P0-7E history is 27 configurations and 135 fold attempts; maximum DSR probability is only `0.4228853062141328`.
- `EMPIRICAL`: P0-7D added 136 pair decisions, 45 Formula-span checks, 10 anchor/forward decisions, and one leave-one-out decision on reused evidence.
- `DOCUMENTED`: repeated use of the same years increases researcher-overfitting risk even when walk-forward folds are retained.
- `UNKNOWN`: whether the partial 2026 interval is adequate for the eventual primary confirmatory endpoint.

## Consequences

P0-7E must emit a final freeze manifest and a holdout-decision handoff. Holdout access remains zero under this ADR. Consumption requires its own exact directive, one-run manifest, frozen entity, code, data, cost and endpoint rules, and an adequacy finding made without performance access.

## Revisit condition

Revisit only if new external data with materially different PIT/survivorship properties becomes available or an independent result reveals a named defect. Do not revisit because P0-7E results are disappointing.
