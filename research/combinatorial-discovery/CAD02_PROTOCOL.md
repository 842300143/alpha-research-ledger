# CAD02 controller research protocol

Controller directive: `EXECUTE_CAD02_SYNERGY_CALIBRATION_AND_SYSTEM_FREEZE_V1`. This protocol is frozen after viewing CAD01 results and before any new real CAD02 joint comparison. It is not retrospective CAD01 preregistration. Exact execution rules, seeds, budgets, candidates, model, screening, selection, and test boundary are in `D:/alpha-factory/research/cad02/PROTOCOL.md`; the execution commit SHA will be appended to the CAD02 result summary.

Research decision: compare only baseline plus subsets of the three archived CAD01 candidates. Run N0/N1 predictive-search calibration on the original queue under six cumulative hours; compare eight fixed systems under two cumulative hours; keep 2024–2025 and 2026 sealed. Synthetic calibration is diagnostic, not market confirmation. All 2019–2023 outcomes are selection contaminated. Preserve old P0-8D0 and CAD01 frozen artifacts.

Prior work checked: [AlphaGen](https://arxiv.org/abs/2306.12964) motivates downstream model increment; [Cawley/Talbot](https://www.jmlr.org/papers/v11/cawley10a.html) documents selection overfitting; [White](https://onlinelibrary.wiley.com/doi/10.1111/1468-0262.00152) motivates data-snooping caution. No claim of implementing White's RC or Hansen's SPA.

Evidence class: `DOCUMENTED` protocol. No new real CAD02 result existed at this freeze.
