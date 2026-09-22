# CAQUAL01 result summary

Alpha Factory work commit `30aabd4b63f3ab26b8b6ab322638e6a0b489fd6a` completed the bounded free-first BaoStock qualification for 72 securities over 2019-2023.

Empirical result: 280 canonical dividend events; 287 material adjustment discontinuities; 280 matched, seven unmatched, zero ambiguous; 65 symbols with changes and four symbols with unresolved potentially holding-relevant changes. Capability remains `TOTAL_RETURN_APPROX_ONLY`. Exact event-aware execution is not qualified.

The result separates 328 raw BaoStock factor records from the 287 PITPRICE material discontinuities; 45 provider records have no same-date comparable-preclose discontinuity. Synthetic holding-ledger fixtures passed, but they do not fill empirical gaps. Paid data is not required now; the next targeted candidate is Tushare `dividend` + `adj_factor`, with `stk_seasoned` or free issuer/exchange announcements for issuance/rights terms. No Tushare call, payment, future-row access, EXPOSURE V2 or return comparison occurred.
