# ADR-0020: EXPOSURE01 V1 inconclusive on as-of price basis

- Status: Accepted result disposition
- Execution work commit: `87b4bbe2f87081b46182ffb1c2dd18a8aa78b198`
- Formal report: `reports/EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1.md`
- Checkpoint: `state/checkpoints/EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1.json`
- Independent review: `research/exposure01/REVIEW.md`
- Validator: `research/exposure01/VALIDATOR.json`, 71 PASS / one hard FAIL

EXPOSURE01 V1 finished three frozen policies and six 1x/2x continuous-account replays on 72 securities and 727 common 2021–2023 sessions, with 36 fixed 20-session signal dates. All six completed once in 18.713 seconds of the 7,200-second cumulative hard wall. The pre-result policy commit was `58bf0e546352aac322d4fc194e97a5bae8f27a71`; its separate manifest commit was `025f553d75ad83b395790efc2a7cb2f5aa6ea868`.

The hard correctness gate failed. The execution code multiplied raw prices by FREE_DAILY_V1 adjustment factors that are backward end-normalized from the full dataset endpoint; bounded 2019–2023 rows therefore encode later corporate-action links. On 2023-12-29, 51 of 72 subset factors were nonunit. Prices, 100-adjusted-unit lot sizing, cash and NAV were affected. The six wealth outcomes are retained as **invalid diagnostics**, not an empirical policy winner. Formal selection is `INCONCLUSIVE`; no gate or always-invest baseline is promoted. The independent Reviewer found no additional hard order-path error and confirmed a large conservative-planner exposure gap: P0 targeted investment on 726 days but averaged 63.91% actual stock exposure.

A forward as-of factor derived only from prior raw close and current comparable preclose requires a new preregistered corrective experiment, manifest and attempt accounting. Do not rerun or replace V1's completed slots. Keep Ridge F1/S123 unchanged, CAD02 calibration `LIMITED_DIAGNOSTIC` (15/20 complete, one incomplete, 2,297.160-second old overrun), and all 2019–2023 comparisons `SELECTION_CONTAMINATED_RESEARCH`. The 2024–2025 interval was used by Generation-1 but not accessed by EXPOSURE01; the 2026 protected interval was not accessed. No future test, broker action or trading is authorized.
