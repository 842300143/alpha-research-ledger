# ADR-0027: CAQUAL02 event data complete; account policy required

- Date: 2026-09-21
- Status: Accepted / Complete
- Controller directive: `ALPHA-CAQUAL02-UNRESOLVED-EVENT-CLOSURE-V1`
- Alpha Factory result work commit: `9bad5b9a5023e2d71f318a933a5d519ad4e8e0fc`
- Research Ledger activation commit: `06387d5` (full hash retained in Git history)

## Decision

Accept the seven-row CAQUAL02 closure as complete event-data qualification. Record four `000029.SZ` frozen dates as `EXPLAINED_NON_ENTITLEMENT_EVENT` ledger no-ops and the three remaining dates as `EXPLAINED_ELECTIVE_ACTION` rights offerings. Preserve the prior 280 CAQUAL01 matches and set combined event-data coverage to 287/287.

Set `CORPORATE_ACTION_LEDGER_CAPABILITY=EVENT_DATA_COMPLETE_POLICY_REQUIRED`. Do not label the generic account `EXACT_EVENT_AWARE` while a held rights event lacks the account's actual election. `PARTICIPATE` requires exact subscribed/allocated quantity and debit date; `DECLINE` is a no-op. The controller may later bind actual account decisions, but this ADR does not choose a policy or optimize it from returns.

## Evidence basis

Official issuer, SZSE, and CNINFO filings document suspension and rights terms. Bounded FREE_DAILY_V1 target-window rows empirically record the seven preclose/factor movements and zero-trade suspension states. All seven analytical reconciliations pass the frozen tolerances. These labels remain distinct: vendor/issuer claims are `DOCUMENTED`, local rows are `EMPIRICAL`, and fixture/account transforms are `SYNTHETIC`.

## Data and execution consequences

- `PAID_DATA_REQUIRED=NO`; no exact paid-data gap remains.
- `HOLDING_PATH_EVENT_COVERAGE_GATE` returns `EXACT_FOR_THIS_REPLAY`, `UNRESOLVED_EVENT_INTERSECTS_HOLDING`, or `NON_IMPACTING_FOR_THIS_REPLAY` for a concrete holding path.
- Unknown/contradictory held events and unbound elective decisions block exact NAV and orders.
- The event ledger is historical accounting only and may not enter predictive features, signals, or forecasts.
- CAQUAL01 evidence remains frozen; CAQUAL02 is additive.

## Boundaries retained

No market-wide scan, paid/credential access, Alpha or return research, REQUAL01 feature injection, EXPOSURE/portfolio replay, 2024-2025/2026 market-row access, broker operation, shared-main modification, or isolated-branch merge was authorized or performed.
