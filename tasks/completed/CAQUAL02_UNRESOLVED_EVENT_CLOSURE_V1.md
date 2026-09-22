# CAQUAL02 unresolved-event closure V1

Status: `COMPLETE / EVENT_DATA_COMPLETE_POLICY_REQUIRED`.

Controller directive `ALPHA-CAQUAL02-UNRESOLVED-EVENT-CLOSURE-V1` was executed only in isolated `codex/caqual02-unresolved-event-closure-v1` worktrees. Alpha Factory work commit: `9bad5b9a5023e2d71f318a933a5d519ad4e8e0fc`.

All seven frozen CAQUAL01 gaps are classified from free official issuer/SZSE/CNINFO evidence plus bounded empirical FREE_DAILY_V1 observations. The four `000029.SZ` dates are `EXPLAINED_NON_ENTITLEMENT_EVENT`: zero-trade reference-price/factor oscillations during continuous suspension, exactly toggling the RMB 0.20 effect of the already-recorded 2019-05-21 dividend. They are ledger `NO_OP` records. `000049.SZ` 2023-12-08, `000065.SZ` 2022-04-14, and `000088.SZ` 2020-08-19 are `EXPLAINED_ELECTIVE_ACTION` rights offerings with documented record/subscription/ex/listing dates, price, nominal ratio, realized issue quantity, and exact reference-price reconciliation.

The prior 280 CAQUAL01 matches remain unchanged. Counts are 287 of 287 event-data explanations, zero unresolved, and zero contradictory. Paid data is not required. Generic capability is `EVENT_DATA_COMPLETE_POLICY_REQUIRED`, not `EXACT_EVENT_AWARE`, because a historical account holding any rights action must provide `PARTICIPATE` or `DECLINE`; participation also requires exact subscribed shares and actual debit date.

Automatic cash, stock-dividend, and reserve-to-stock transforms; an elective policy interface; duplicate/contradiction handling; and the exact three-outcome `HOLDING_PATH_EVENT_COVERAGE_GATE` are implemented. Seventeen focused tests, 70 combined focused tests, and 12 independent validator checks passed. No full-market scan, predictive or return research, REQUAL01 mutation, paid/credential access, later market-row access, broker action, or branch merge occurred.

Formal artifacts: `reports/ALPHA_CAQUAL02_UNRESOLVED_EVENT_CLOSURE_V1.md`, `research/caqual02/evidence/EVENT_RESULTS.json`, `research/caqual02/evidence/SOURCE_RECEIPTS.json`, `research/caqual02/evidence/FACTOR_RECONCILIATION.json`, `research/caqual02/evidence/EVENT_LEDGER_CONTRACT.json`, `research/caqual02/evidence/HOLDING_PATH_EVENT_COVERAGE_GATE.json`, and `state/checkpoints/CAQUAL02_UNRESOLVED_EVENT_CLOSURE_V1.json` in Alpha Factory.
