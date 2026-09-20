# ADR-0017: CAD02 bounded synergy calibration and system freeze

- Status: Accepted for `CAD02_SYNERGY_CALIBRATION_AND_SYSTEM_FREEZE_V1`
- Controller directive: `EXECUTE_CAD02_SYNERGY_CALIBRATION_AND_SYSTEM_FREEZE_V1`
- Research protocol committed before new eight-system metrics: `research/combinatorial-discovery/CAD02_PROTOCOL.md` at Ledger commit `1dc9bbaa569a3e387d1aefe08c2e9e6c0e8f1cf1`

CAD01's three archived candidates were selected on reused 2019–2023 research history. CAD02 may diagnose search selection with ten fixed N0 and ten fixed N1 simulations and compare exactly eight systems formed from the CAD01 16-feature Ridge baseline and subsets of those three candidates. The limits are six cumulative hours for predictive-only calibration and two cumulative hours for 24 logical system-fold fits plus one three-fold reproduction. It adds no real expression, model family, hyperparameter choice, or dynamic trading rule. The exact ASTs, candidate identities, simulation parameters, seeds, hard gates, tie rule, cost rules, and future-test boundary are frozen in the cited protocol and Alpha Factory `research/cad02/PROTOCOL.md`.

This decision follows the CAD01 results. It cannot turn CAD01 into a preregistered independent test or make the selected CAD02 system a confirmed Alpha. `2024–2025` stays locked for this task, and the protected `2026` interval stays sealed. Any later test requires a separate complete-system manifest and controller directive; the old P0-8D/P0-8D0 disposition remains unchanged.

Evidence labels: `DOCUMENTED` decision and protocol; `SYNTHETIC` simulation and cost fills; `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` paired prediction on 2019–2023; `UNKNOWN` independent forward validity and production execution.
