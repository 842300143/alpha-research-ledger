# ADR-0024: INTEGRATION01 unified PITPRICE / PIPELINE / PORTFOLIO baseline

- Status: Reviewed engineering integration; execution merged, Ledger normal merge pending.
- Controller directive: `ALPHA-INTEGRATION01-PITPRICE-PIPELINE-PORTFOLIO-V1`.
- Execution base: `37fd3ccfe00e9df9fafd40f139f6e2d1baa4f163`.
- Ledger base: `e9dfeab1b95e3654eec72b9143f8414a78ee8090`.
- Execution work commit: `62daaa7319eb06de8333f150049377286450da36`.
- Execution normal merge commit: `e4758907dd246e812a2e56f35ff41defc3c7f116`.
- Formal execution report: `reports/INTEGRATION01_PITPRICE_PIPELINE_PORTFOLIO_V1.md`.
- Formal execution checkpoint: `state/checkpoints/INTEGRATION01_PITPRICE_PIPELINE_PORTFOLIO_V1.json`.

PITPRICE01 and ADR-0021 remain the semantic authority for raw execution price, causal as-of analytical price, realized target return, capital, and the upstream hard gate. PIPELINE01 and PORTFOLIO01 enter as engineering components. Their isolated state files did not overwrite the current shared state. The PIPELINE01 branch's ADR-0020 number conflicted with main's EXPOSURE01 ADR-0020; its decision is preserved as ADR-0022 here. ADR-0023 records PORTFOLIO01.

`UPSTREAM_MODEL_INVARIANT=NO`. CAD01/CAD02/MODEL01 and Ridge F1/S123 remain frozen historical results, but Ridge is `SUPERSEDED_FOR_FORWARD_SELECTION_PENDING_REQUALIFICATION`, allowed only as an explicit research fixture. There is no current production prediction champion. EXPOSURE01 V1 is `INVALID_FOR_SELECTION`; no replay or policy promotion occurred.

The machine-readable PITPRICE01 capital contract fixes RMB 50,000 as primary and RMB 1,000,000 as scaling diagnostic. Missing capital contract or scenario fails closed. The canonical data contract separates `RAW_EXECUTION_PRICE`, `ASOF_ANALYTICAL_PRICE` and `REALIZED_TOTAL_RETURN_TARGET` and protects earlier as-of artifacts from future appends. Account and holding capability remains `TOTAL_RETURN_APPROX_ONLY`; exact historical executable wealth awaits dated cash/share/rights event evidence and CAQUAL01. Portfolio real-market evaluation is blocked.

PIPELINE01 retains `ENGINE_READY_WITH_PERF_WARNING` on synthetic evidence: about 3.736 s full feature and 5.634 s one-day incremental on its tiny fixture; real-scale performance is `UNKNOWN`. No Alpha search, CAD/MODEL rerun, EXPOSURE01 replay, market return comparison, protected-row access or trading was performed by this integration. The 2024–2025 and 2026 market intervals remain sealed for this task. Next recommended independent work is REQUAL01 and CAQUAL01, each with its own contract and gates.

Independent Reviewer: `PASS_WITH_WARNINGS`, no hard failure. The local source-drift quick check uses file size and modification time; ingested canonical rows and run payloads are content hashed. Owner test matrix: 57 PASS / 0 FAIL. The Reviewer separately ran 20 read-only synthetic tests (one temporary-file-writing test was left to the owner run).
