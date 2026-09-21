# INTEGRATION01 PITPRICE / PIPELINE / PORTFOLIO V1

Status: `REVIEWED_ENGINEERING_INTEGRATION`; execution merged, Research Ledger normal merge pending.

Controller directive `ALPHA-INTEGRATION01-PITPRICE-PIPELINE-PORTFOLIO-V1` reconciled PITPRICE01 causal price and capital authority with the isolated PIPELINE01 incremental runtime and PORTFOLIO01 sizing engine. Alpha Factory work commit `62daaa7319eb06de8333f150049377286450da36` was merged normally to `master` as `e4758907dd246e812a2e56f35ff41defc3c7f116`.

The integrated runtime fails closed on missing or mismatched price and capital contracts, keeps raw execution price separate from as-of analytical price and realized target return, requires explicit primary or scaling-diagnostic capital, and exposes desired target shares without creating broker orders. Ridge F1/S123 is a superseded research fixture pending REQUAL01. Exact executable wealth and real-market portfolio evaluation remain blocked while account capability is `TOTAL_RETURN_APPROX_ONLY`, pending CAQUAL01.

Independent review returned `PASS_WITH_WARNINGS`; the nonblocking warning is that the source-drift quick check uses file size and modification time, while ingested rows and run payloads are content hashed. The owner suite passed 57 tests with zero failures. The reviewer separately passed 20 read-only synthetic tests; one temporary-file-writing case was covered by the owner suite.

No Alpha research, CAD/MODEL rerun, EXPOSURE01 replay, market return evaluation, protected-row access, trading, payment or credential-sensitive external action occurred. The 2024–2025 test interval and protected 2026 holdout remained sealed. Formal artifacts are `reports/INTEGRATION01_PITPRICE_PIPELINE_PORTFOLIO_V1.md`, `state/checkpoints/INTEGRATION01_PITPRICE_PIPELINE_PORTFOLIO_V1.json`, execution ADR documentation, and Ledger ADR-0024.

Next recommended parallel directions are separately preregistered REQUAL01 and CAQUAL01 tasks. This record does not authorize either task.
