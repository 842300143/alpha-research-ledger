# EVALRECON01 common-baseline reconciliation V1

Controller directive: `ALPHA-EVALRECON01-COMMON-BASELINE-RECONCILIATION-V1`  
Mode: `CORRECTNESS_RECONCILIATION_ONLY`  
Execution repository: `D:\alpha-factory-evalrecon01`  
Research repository: `D:\alpha-research-ledger-evalrecon01`

Reconcile the committed Exposure02 V2 P0 AlwaysInvest + EqualWeight terminal wealth of RMB 58,123.84 with the committed Portfolio02 EqualWeight + AlwaysInvest terminal wealth of RMB 57,445.71. Verify exact Git provenance and compare the 36 decision dates, prediction inputs, Top20 ordering, continuous and integer targets, orders/fills, corporate actions, and every daily cash/share/NAV state from RMB 50,000.

Create an additive `COMMON_BASELINE_CONTRACT.json`, classify the first divergence and root cause, determine `CANONICAL_COMMON_BASELINE_V1` by correctness authority rather than return, and replay only the necessary common baseline. Exact equality is preferred; any residual beyond deterministic account tolerance fails closed. Historical results and winner selections remain frozen.

Keep 2024-2025 and 2026 deny-before-load sealed. No model, factor, Top20, EqualWeight, capital, actual cost, corporate-action, or election-policy change; no tuning, new Alpha, broker, payment, credential, production, destructive Git, or history rewrite.
