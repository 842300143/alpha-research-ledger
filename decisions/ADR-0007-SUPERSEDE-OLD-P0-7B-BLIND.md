# ADR-0007: Supersede the Old P0-7B Blind Without Consuming It

- Status: Accepted
- Date: 2026-09-17

## Context

The old protected P0-7B Blind interval is 2024-12-27 through 2025-03-31 and is bound to the prior Alpha V0 dataset, split, candidates, code, configurations, and result hashes. Alpha Factory evidence confirms that it was never accessed or consumed and that no execution manifest exists.

`FREE_DAILY_V1` spans 2019-01-02 through 2026-09-15. Ordinary long-horizon research on this new dataset necessarily includes the old calendar interval in development or walk-forward evidence, so the old interval can no longer serve as the final protected holdout for the new research generation.

## Decision

Classify the old P0-7B protected Blind as `SUPERSEDED_UNCONSUMED` for research planning.

- It was never executed.
- `BLIND_CONSUMED` remains `FALSE` for the historical P0-7B artifact.
- Preserve every old approval, candidate, dataset, split, code, configuration, result-hash, and access-log artifact in Alpha Factory.
- Never execute it now and never report it retroactively as a valid Blind result.
- P0-7C uses multi-year walk-forward OOS through 2025 and reserves the observed 2026 trading-calendar segment as a new, separately governed protected holdout.

## Reason

A holdout protects against choices made before it is observed. Once the new research protocol uses a dataset spanning the old interval, that interval cannot provide an independent final test for the new generation. Preserving the unconsumed old artifacts retains historical integrity without pretending that an obsolete boundary still supplies valid protection.

## Consequences

- No old P0-7B Blind execution manifest may be created.
- Old P0-7B evidence remains historical and immutable, not deleted or rewritten.
- P0-7C must deny ordinary research access to all 2026 observations, including labels, returns, portfolio outcomes, and regime results.
- A later P0-7D-style task may consume the new holdout only after candidates, dataset/subset, feature code, model settings, comparison set, portfolio rules, and cost assumptions are frozen and a one-run manifest is created.
- The available 2026 holdout is partial through 2026-09-15 (171 sessions); its adequacy for final promotion must be assessed before consumption, never repaired by peeking or repeated testing.
