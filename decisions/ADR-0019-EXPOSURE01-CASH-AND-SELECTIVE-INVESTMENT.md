# ADR-0019: EXPOSURE01 cash and selective investment

- Status: Accepted for `EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1`
- Controller directive: `EXECUTE_EXPOSURE01_CASH_AND_SELECTIVE_INVESTMENT_V1`
- Execution start HEAD: `aeebb5493e2805d1fcaea81cfb6fdc64f3014b90`
- Ledger start HEAD: `e335d575e39d9cfd561bfa131fb17f0a7f5ef0c8`
- Frozen MODEL01 system: `research/model01/SYSTEM_FREEZE.json`, SHA-256 `d7dcd4a2ebf930e805fc14fc9e059b4bd126b2c7b0054f4451ef8e559893deb7`

Authorize a bounded 2019–2023 research comparison of always invest, always cash, and at most two preregistered binary exposure gates using the frozen Ridge F1/S123 selection signal. The primary endpoint is continuous-account, same-calendar, post-cost compounded terminal wealth. A large cash fraction is allowed. Two-month windows diagnose concentration and do not add independent folds. Selection stability and risk remain evidence limits, not a replacement objective. The original MODEL01 RankIC winner rule and result remain historical and unchanged.

The model predicts 20-session return relative to the same-date median, not absolute profit. Ridge F1 has 16 frozen representatives plus C1/C2/C3 with unchanged ASTs, signs, preprocessing, training and 20-session selection grid. ElasticNet F0 is an alternative clue, approximately 0.000422 higher in the prior modeled net-return summary, but is neither a new selected model nor an authorized experiment here. The specific gate forms, costs, account semantics, missingness, test suite, queue and stop rule must be committed before exposure returns. A gate lacking a comparable raw score or usable inputs may be omitted with a reason.

The 72-security subset is the scope; the 3,207-security database is not the tested universe. Only 2019–2023 and earlier as-of warm-up are allowed. The 2024–2025 tranche was used in Generation-1 research, so it is not project-wide unseen data; EXPOSURE01 does not access it. The 2026 protected interval also stays sealed. All new policy comparisons are `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`; fills and costs are `SYNTHETIC`. CAD02 calibration stays `LIMITED_DIAGNOSTIC`: 15/20 complete, one incomplete, 2,297.160 seconds over its old wall cap. MODEL01's successor hard timeout does not repair those results. No broker, payment, external LLM, or future-test authorization follows.

References: [Moreira and Muir, *Volatility-Managed Portfolios*](https://onlinelibrary.wiley.com/doi/10.1111/jofi.12513) motivates studying exposure management but does not prove this cash switch; [Cawley and Talbot, *On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation*](https://www.jmlr.org/papers/v11/cawley10a.html) motivates the fixed small roster and cautious interpretation.
