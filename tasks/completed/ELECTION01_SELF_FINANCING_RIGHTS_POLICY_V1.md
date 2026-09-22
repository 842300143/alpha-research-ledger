# ELECTION01 self-financing rights policy V1

Status: `COMPLETE / EXACT_EVENT_AWARE_UNDER_FROZEN_ELECTION_POLICY`.

Controller directive `ALPHA-ELECTION01-SELF-FINANCING-RIGHTS-POLICY-V1` completed in isolated execution and Research Ledger worktrees. Alpha Factory result work commit: `f10c25887ad5f1170fc48b711888bb8fdc41d879`.

`SELF_FINANCING_PARTICIPATE_IF_CASH_AVAILABLE_V1` is the frozen primary hypothetical policy. It snapshots record-date entitlement, elects at the first valid subscription session, uses only existing free cash, permits a maximum affordable partial subscription, debits cash atomically, and delays share credit until the official listing date. `DECLINE_ALL_RIGHTS_V1` is sensitivity-only and cannot enter primary winner selection.

The event layer uses a one-share subscription/book unit, not the ordinary 100-share trade lot. A fractional nominal entitlement requires the registrar-booked balance because the official precise algorithm depends on cross-holder ordering. All three CAQUAL02 events are contract-complete and policy-executable. The capability is `EXACT_EVENT_AWARE_UNDER_FROZEN_ELECTION_POLICY`, conditional on complete holding-path account inputs.

Twenty-four ELECTION01 synthetic tests and 46 focused ELECTION01/CAQUAL02/Portfolio01 tests passed. The repository-wide diagnostic retained 3 failures and 9 errors in untouched legacy data/hash/environment paths; it was not reclassified as a task pass.

No real-market wealth replay, return comparison, Alpha research, Exposure, Portfolio winner evaluation, later market-row access, broker action, payment, credential use, REQUAL01 mutation, or branch merge occurred. Next: `WAIT_FOR_REQUAL01_AND_CONTROLLER_INTEGRATION`.
