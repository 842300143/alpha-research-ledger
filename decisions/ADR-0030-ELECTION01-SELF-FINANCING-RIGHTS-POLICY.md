# ADR-0030: ELECTION01 self-financing rights policy

- Date: 2026-09-21
- Status: Accepted / Complete
- Controller directive: `ALPHA-ELECTION01-SELF-FINANCING-RIGHTS-POLICY-V1`
- Alpha Factory base: `56b9c486ea7b1c81627b93936718b1af4f0b5f26`
- Research Ledger base: `7469d9798312812cdd7ca047423fd52feda8a771`
- Alpha Factory result work commit: `f10c25887ad5f1170fc48b711888bb8fdc41d879`

## Decision

Authorize isolated account-policy engineering on the committed CAQUAL02 result lineage. Freeze `SELF_FINANCING_PARTICIPATE_IF_CASH_AVAILABLE_V1` as the primary hypothetical policy: establish rights from record-date holdings, decide at the first valid subscription session, use only existing free cash, subscribe fully or partially up to the official entitlement, debit/reserve cash atomically, and credit shares only on the official listing date. Freeze `DECLINE_ALL_RIGHTS_V1` as sensitivity-only and exclude it from primary selection.

Official Shenzhen filings specify a one-share minimum book/subscription unit and a cross-holder precise allocation procedure for sub-share rights. The engine must not apply the ordinary 100-share A-share trading lot. If a nominal entitlement is fractional, exact replay requires the registrar-booked account entitlement; a local floor or round-up is forbidden.

## Evidence and claim boundary

CAQUAL02 remains authoritative for the three event identities and economic terms. ELECTION01 may add only operational unit/fraction semantics needed by the policy interface. `EXACT_EVENT_AWARE_UNDER_FROZEN_ELECTION_POLICY` means exact under this stated hypothetical policy and complete account inputs; it does not assert what a real historical investor chose.

No wealth replay, profit comparison, policy winner search, Alpha/CAD/model research, Exposure, Portfolio evaluation, 2024-2025/2026 market-row access, broker operation, payment, credential use, REQUAL01 mutation, or branch merge is authorized.

## Result

The primary and diagnostic policies are implemented as a separate account-event layer. All three CAQUAL02 contracts are complete and policy-executable. Twenty-four ELECTION01 synthetic tests and 46 focused ELECTION01/CAQUAL02/Portfolio01 tests passed with zero failures. The account engine blocks negative cash, duplicate subscription, double spending, subscription above entitlement, and pre-listing credit. `HOLDING_PATH_EVENT_COVERAGE_GATE` is exact only with complete event, frozen-policy, record-date, and registrar-allocation inputs; otherwise it fails closed.

Set `CORPORATE_ACTION_LEDGER_CAPABILITY=EXACT_EVENT_AWARE_UNDER_FROZEN_ELECTION_POLICY`. This remains a hypothetical-policy claim, not an assertion about actual historical investor behavior.
