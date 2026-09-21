# ADR-0025: CAQUAL01 retains total-return approximation

- Date: 2026-09-21
- Status: Accepted
- Controller directive: `ALPHA-CAQUAL01-CORPORATE-ACTION-EVENT-QUALIFICATION-V1`
- Alpha Factory work commit: `30aabd4b63f3ab26b8b6ab322638e6a0b489fd6a`
- Formal report: `reports/ALPHA_CAQUAL01_CORPORATE_ACTION_EVENT_QUALIFICATION_V1.md`

## Decision

Do not upgrade the bounded 72-security 2019-2023 holding ledger to `EXACT_EVENT_AWARE`. Retain `CORPORATE_ACTION_LEDGER_CAPABILITY=TOTAL_RETURN_APPROX_ONLY` and keep exact account/NAV replay fail-closed.

## Evidence

BaoStock provided 280 unique dated dividend events from 283 raw rows and 328 adjustment-factor records. The PITPRICE-authoritative comparable-preclose source contains 287 material factor discontinuities. Exactly 280 reconcile to cash/share event terms; seven have no event entitlement and zero are field-ambiguous. The seven unresolved changes span four symbols and are potentially holding-relevant. Forty-five additional BaoStock factor records have no same-date PITPRICE discontinuity and are retained as provider metadata/non-material records rather than counted as changes. BaoStock's returned schema also lacks rights subscription quantity, price, exercise and cash-debit mechanics.

## Consequences

No event is inferred from a factor. The synthetic `CorporateActionEventContract` may be integrated only as a disabled/fail-closed contract while unresolved events remain. EXPOSURE V2, real-market portfolio evaluation and exact wealth claims stay blocked independently of REQUAL01.

No paid data is required now. The next bounded step is a four-symbol/seven-date cross-source qualification: Tushare `dividend` and `adj_factor`, plus `stk_seasoned` or issuer/SZSE/CNINFO implementation announcements for issuance/rights evidence. Tushare documentation currently states at least 2,000 points for the structured interfaces; no token or interface was used, and no purchase is authorized or recommended before the free targeted path is exhausted.

## Boundaries

The result is `EMPIRICAL` for the current BaoStock capture and frozen PITPRICE rows, `SYNTHETIC` for holding-ledger fixtures, `DOCUMENTED` for alternative-provider fields and permissions, and `UNKNOWN` for the seven missing entitlement causes. The task accessed no 2024-2025 or 2026 market rows, strategy returns, broker operations, payment or protected evaluation.
