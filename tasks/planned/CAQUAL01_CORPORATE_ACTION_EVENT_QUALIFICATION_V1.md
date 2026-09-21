# CAQUAL01 corporate-action event qualification V1

Status: `ACTIVE`

Controller directive: `ALPHA-CAQUAL01-CORPORATE-ACTION-EVENT-QUALIFICATION-V1`.

Execution repository base: `9ef1d605d132b550f43cdc75a309c20fe03dc4ef` on isolated branch/worktree `codex/caqual01`. Research Ledger base: `1d49b4783edeb6d4454ef4fbf465fd99e34080fc` on isolated branch/worktree `codex/caqual01`.

Goal: under the free-first policy, empirically determine whether BaoStock `query_dividend_data` plus `query_adjust_factor` provides complete dated cash/share entitlements for every material adjustment-factor discontinuity affecting the frozen 72-security 2019-2023 replay. Capability upgrades to `EXACT_EVENT_AWARE` only if all potentially holding-relevant material factor changes reconcile without inferred entitlements; otherwise retain `TOTAL_RETURN_APPROX_ONLY` or classify `INSUFFICIENT`.

Boundaries: fetch only the frozen 72 symbols and years 2019-2023. Do not open 2024-2025 or 2026 market rows; run EXPOSURE V2; rerun CAD/MODEL; compare strategy returns; purchase data; call unauthorized paid interfaces; trade; or alter frozen PITPRICE01, REQUAL01, PIPELINE01, CAD01/CAD02/MODEL01, or EXPOSURE01 evidence. Raw provider payloads and large data remain outside Git; only bounded normalized evidence, hashes, summaries, contracts, tests, and reports may be committed.

Required evidence: complete provider field inventory; fetch snapshot hashes; normalized event table; adjustment-factor discontinuity table; deterministic reconciliation classes; holding-relevant unresolved-event audit; synthetic holding-ledger fixtures for cash, stock, reserve transfer, multi-event, ex-date holding, record-date trading, no-event, and unmatched-jump fail-closed behavior; `CorporateActionEventContract`; PIPELINE/PITPRICE timing/provenance integration contract; and, if insufficient, a `DATA_GAP_REPORT` plus documentation-only next-provider comparison. Tushare permissions and points may be documented but no unauthorized or paid call is permitted.

Evidence labels remain `EMPIRICAL`, `DOCUMENTED`, `SYNTHETIC`, and `UNKNOWN`. A provider claim is never promoted to empirical evidence, and no entitlement may be inferred solely from a factor ratio.

Stop after an evidence-backed capability decision, execution/report/checkpoint commits, Research Ledger result/ADR update, and repository close gates. Exposure V2 remains out of scope regardless of the qualification result.
