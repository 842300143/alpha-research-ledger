# ADR-0010: Keep the 2026 Protected Holdout Sealed During Generation-2 Research

- Status: Accepted
- Date: 2026-09-17

## Context

The protected interval 2026-01-05 through 2026-09-15 contains 171 sessions and remained unaccessed and unconsumed throughout P0-7C. P0-7D qualifies candidates on reused 2021-2025 OOS evidence, and future Generation-2 work may create new hypotheses.

## Decision

Keep the 2026 protected holdout sealed throughout P0-7D and Generation-2 research. No performance, NAV, feature, label, regime, coverage, ranking, candidate selection, or pool selection may use the interval.

Holdout consumption requires a later, separate exact controller directive; frozen candidates and pool; frozen dataset, subset, code, configuration, costs, and comparison set; a pre-access one-run manifest; and a determination made without peeking that the partial interval is adequate for the intended decision.

## Evidence / rationale

- `EMPIRICAL`: P0-7C loader and audit recorded `HOLDOUT_ACCESSED = FALSE` and `HOLDOUT_CONSUMED = FALSE`.
- `DOCUMENTED`: using the holdout during pool design or Generation-2 discovery would turn it into development data and remove its independent value.
- The old P0-7B Blind is already `SUPERSEDED_UNCONSUMED`; consuming another holdout casually would further reduce scarce independent evidence.

## Alternatives

- Use 2026 to choose P0-7D members.
- Consume 2026 after each Generation-2 iteration.
- Discard the partial holdout without a future adequacy review.

## Consequences

P0-7D and P0-7E must deny 2026 before load. Qualification and Generation-2 results remain research evidence, not final confirmation. No repeat, tuning, or replacement follows any later authorized one-run consumption.

## Future revisit condition

Revisit only through a separate protected-holdout task after all decision inputs are frozen and repository gates prove no prior access or consumption.
