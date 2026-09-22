# ADR-0031: INTEGRATION02 corrected research and corporate-action baseline

- Date: 2026-09-22
- Status: Accepted / Complete
- Controller directive: `ALPHA-INTEGRATION02-REQUAL-CORPORATE-ACTION-V1`
- Alpha Factory base: `c4e68d35e8ca231a31bc01bb76e61e1bd70f1c3a`
- Research Ledger base: `236e8a227927806c1adb3338d017cc646ac4f712`
- Alpha Factory work commit: `c5235189d866aa05c52f7e6802ae482b4a1b9972`
- Alpha Factory integration state commit: `df5f374eefb7204a2705282dd8b4445d6ee9859e`
- Alpha Factory normal merge commit: `b17b33bbaec09573e8b14af710830340a9aba392`
- Research Ledger normal merge commit: `70ca84a11f6dc1dea7dbadec04ed13c0cf775315`

## Decision

Accept the versioned Integration02 baseline that combines INTEGRATION01 runtime/portfolio engineering, REQUAL01 corrected research, CAQUAL02 complete event evidence, and ELECTION01 self-financing rights policy.

The current system is corrected Ridge F1/S123 V2, exact version `REQUAL01_RIDGE_F1_S123_V2`, status `PROVISIONAL_RESEARCH_SYSTEM`. The historical pre-PIT Ridge F1/S123 system remains `SUPERSEDED`. `PRODUCTION_CHAMPION=NONE` and `TEST_CONFIRMED=NO`. Evidence remains `SELECTION_CONTAMINATED_RESEARCH`.

Record `CORPORATE_ACTION_LEDGER_CAPABILITY=EXACT_EVENT_AWARE_UNDER_FROZEN_ELECTION_POLICY`. This is a generic engineering capability, not blanket replay authorization. Exact wealth is allowed only when the concrete run establishes `HOLDING_PATH_EVENT_COVERAGE_GATE=EXACT_FOR_THIS_REPLAY`, including complete event terms, record-date holdings, a terminal frozen-policy election, and registrar-booked entitlement where fractional allocation cannot be known locally.

Primary deployment capital is RMB 50,000. RMB 1,000,000 remains an explicit scaling diagnostic and cannot be substituted as a default.

## Evidence and warning disposition

PIT correction changed values, but full requalification preserved the factor lifecycle, 16-archetype structure, three CAD candidates, S123, and Ridge F1 selection. Corrected CAD02 calibration completed 20/20. The 14 REQUAL impact warnings are classified as `IMPACT_EXPLANATION_UNRESOLVED_ONLY`; they describe proof of old-versus-corrected numerical/coverage changes, not undefined corrected semantics. The warning is retained because two affected factors enter the current system.

CAQUAL02 closes all seven prior event-data gaps: four reference events are ledger no-ops and three are rights offerings. ELECTION01 freezes `SELF_FINANCING_PARTICIPATE_IF_CASH_AVAILABLE_V1` as primary and `DECLINE_ALL_RIGHTS_V1` as diagnostic only. Rights use existing free cash, permit legal cash-limited partial participation, debit atomically, and credit shares only on the official date. Ordinary 100-share trading-lot rules never infer rights entitlement.

The Alpha Factory full suite passes 250/250; the independent Integration02 validator passes 13/13. The earlier ELECTION01 aggregate of 230 pass / 3 fail / 9 error was rerun before Integration02 changes as 242/242 pass, leaving no remaining failure/error to classify.

## Boundaries

No real-market wealth replay, Exposure policy run, Portfolio winner selection, new Alpha research, 2024-2025 market-row access, 2026 access, broker order, payment, credential action, or production deployment occurred. Integration02 does not authorize EXPOSURE02 or PORTFOLIO02. The next controller direction must bound those phases separately and preserve the corrected system, capital, price, event, election, and protected-date gates.
