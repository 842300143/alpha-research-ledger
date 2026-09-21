# CAQUAL01 corporate-action event qualification V1

Status: `COMPLETE / TOTAL_RETURN_APPROX_ONLY`.

Controller directive `ALPHA-CAQUAL01-CORPORATE-ACTION-EVENT-QUALIFICATION-V1` was executed in isolated `codex/caqual01` worktrees from Alpha Factory base `9ef1d605d132b550f43cdc75a309c20fe03dc4ef` and Ledger base `1d49b4783edeb6d4454ef4fbf465fd99e34080fc`. Alpha Factory work commit: `30aabd4b63f3ab26b8b6ab322638e6a0b489fd6a`.

The free anonymous BaoStock SDK completed exactly 432 bounded calls for the frozen 72 securities and 2019-2023: 360 `query_dividend_data(yearType=operate)` calls and 72 `query_adjust_factor` calls. It returned 283 dividend rows, including three exact duplicates, for 280 canonical events; and 328 provider factor records. Against the frozen PITPRICE comparable-preclose discontinuity source, there were 287 material factor changes across 65 symbols: 280 matched, seven unmatched and zero ambiguous. The unmatched changes affect `000029.SZ`, `000049.SZ`, `000065.SZ`, and `000088.SZ`. No missing entitlement was inferred from a factor ratio.

The exact gate therefore failed and `CORPORATE_ACTION_LEDGER_CAPABILITY=TOTAL_RETURN_APPROX_ONLY`. Seventeen synthetic holding-ledger tests and 20 deterministic validation checks passed the fail-closed contract. Exact replay, EXPOSURE V2 and strategy-return comparison did not run. Tushare was documentation-only and was not called; paid data is not required now. The next targeted provider path is Tushare `dividend` + `adj_factor`, with `stk_seasoned` or issuer/exchange announcements for issuance/rights evidence. Any Tushare access still requires existing permission/points; no purchase is recommended before the targeted free path is exhausted.

Formal execution artifacts: `reports/ALPHA_CAQUAL01_CORPORATE_ACTION_EVENT_QUALIFICATION_V1.md`, `research/caqual01/CORPORATE_ACTION_EVENT_CONTRACT.json`, `research/caqual01/DATA_GAP_REPORT.md`, `research/caqual01/evidence/MATERIAL_FACTOR_EVENT_RECONCILIATION.json`, and the CAQUAL01 checkpoint. No 2024-2025 or 2026 market row, broker action, payment, external LLM or protected evaluation was accessed.
