# Multiple-Testing Policy V2

## Inherited search history

P0-8 does not reset prior selection:

- P0-7C/P0-7E: 34 predictive configurations and 170 fold attempts.
- P0-7D: 136 pair decisions, 45 Formula-span held-out reconstructions, deterministic de-duplication/order, forward-addition, and leave-one-out decisions.
- P0-7A: 26 executed records (five controls and 21 bounded new records), including 17 retained failed executions and nine successful executions, plus 17 R2 registrations aborted before performance; this separate Alpha V0 dataset/split history remains explicit and is not arithmetically merged with the FREE_DAILY_V1 34-configuration count.

P0-8 records both `concept_count` and `configuration_count`. With 99 atomic/transformed definitions and three Stage-1 folds, 297 evaluations are processing volume, not 297 independent hypotheses. The 99 definitions are the primary multiplicity family; canonical variants remain distinct configurations linked to fewer concepts.

## Primary statistical control

For each signed atomic definition:

1. compute the Stage-1 daily RankIC series under the primary rank view;
2. generate a shared empirical null using 1,000 within-date label permutations with one frozen seed schedule applied to every factor, preserving cross-factor dependence for each permutation;
3. form a one-sided empirical p-value only when direction was predeclared; otherwise use two-sided p-values and prohibit directional promotion without a new budgeted preregistration;
4. apply Benjamini-Hochberg FDR at `q = 0.10` across all 99 primary definitions;
5. report adjusted q-values, never only nominal p-values.

Family-level FDR tables are supplementary and cannot rescue failure of the global family. Shared permutations, exact seed list, missingness policy, and attempt population must be frozen before results.

## Dependence and uncertainty

- Use moving-block bootstrap on daily IC series for intervals, with block length frozen from training-only autocorrelation diagnostics and capped before result access.
- Do not use naive iid t-tests as primary evidence.
- Retain effect sizes, fold signs, coverage, and cost behavior; statistical significance alone is insufficient.
- Factor clustering reduces interpretation duplication after testing; it does not retroactively reduce the tested-hypothesis count.

## Portfolio/model diagnostics

- White's Reality Check or Hansen SPA may be used only for a frozen, comparable strategy-return family with sufficient chronological observations and documented bootstrap validity.
- Deflated Sharpe is secondary and may be reported only when return observations, non-overlap, skew/kurtosis assumptions, and the full cumulative trial count are explicit.
- PBO remains `NOT_JUSTIFIED` unless at least eight legitimate chronological blocks exist without chronology-destroying resampling.
- None of these methods replaces preregistration, fixed budgets, retained failures, walk-forward evaluation, clustering, or the protected holdout.

## Accounting ledger

Every stage records:

- concepts, formula definitions, canonical variants, predictive configurations, folds, robustness views, structure pair decisions, residual fits, interactions, model settings, and portfolio constructors;
- terminal failures and unused reserved slots;
- whether a computation is a new hypothesis, fixed diagnostic, reproduction, or mechanical view;
- cumulative P0-7 plus P0-8 counts.

No failed slot is deleted, renamed into a new concept, or recycled. A semantic formula/sign/horizon change receives a new ID and new budget before any result.
