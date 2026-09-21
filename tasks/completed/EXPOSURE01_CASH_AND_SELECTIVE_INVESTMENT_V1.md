# EXPOSURE01 Cash and Selective Investment V1

## Completion (2026-09-21)

`INCONCLUSIVE_CORRECTNESS_GATE` at Alpha Factory work commit `87b4bbe2f87081b46182ffb1c2dd18a8aa78b198`. All six preregistered continuous-account policy/cost replays completed, but a hard as-of price-basis failure invalidated terminal wealth and policy selection. Validator 71 PASS / one FAIL; independent Reviewer confirmed the factor leakage and found no other hard order-path failure. See Ledger ADR-0020 and `research/exposure/EXPOSURE01_RESULT_SUMMARY.md`; exact execution report/checkpoint paths above. No V1 slot was replayed, no 2024–2025 or 2026 row accessed, and no test or trading was authorized.

Directive `EXECUTE_EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1` under ADR-0019. Alpha Factory: `D:\alpha-factory`, starting at `aeebb5493e2805d1fcaea81cfb6fdc64f3014b90`. Ledger: `D:\alpha-research-ledger`, starting at `e335d575e39d9cfd561bfa131fb17f0a7f5ef0c8`.

Use the exact MODEL01 Ridge F1/S123 freeze and 72-security subset. First audit the relative target and raw score scale. Preregister P0 always invest, P1 always cash, and no more than two simple cash gates; freeze policy code and manifest before return access. Use one continuous same-calendar account simulator for all policies, 1x/2x costs, true cash state and delayed exits, no fold reset, no leverage. Return complete-calendar terminal wealth, exposure, orders, two-month diagnostics, profit concentration, risk, independent order-path review, validator and checkpoint. Use a cumulative 7,200-second hard wall. A missing usable second gate is an explicit omission, not a search invitation.

Preserve `SELECTION_CONTAMINATED_RESEARCH`, CAD02 `LIMITED_DIAGNOSTIC`, and synthetic execution warnings. Do not change Ridge, C123, hyperparameters or MODEL01 selection. Do not access 2024–2025 or 2026, call an external LLM/API, send orders, buy data, or expand the policy roster after results. Close via Alpha Factory worker protocol and record exact final commit/report paths here.
