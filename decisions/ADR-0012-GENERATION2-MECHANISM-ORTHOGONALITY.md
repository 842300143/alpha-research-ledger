# ADR-0012: Make Generation 2 Mechanism- and Orthogonality-First

- Status: Accepted
- Date: 2026-09-17

## Context

P0-7D reduced 17 broad survivors to 10 non-redundant candidates and one pool member. Nine forward additions failed. Seven variants were redundant. Three ElasticNet variants added Formula-relative RankIC, while Ridge and all four LightGBM variants failed incremental classification. This shifts the problem from finding another standalone survivor to finding information not already represented by the anchor.

## Decision

P0-7E is a bounded mechanism-refinement and orthogonal-discovery task. It registers exactly three new Formula candidates and four fixed ElasticNet feature-family ablations, for seven predictive configurations and 35 fold attempts. Failures consume budget; no slot is recycled. LightGBM, deep models, Size, Value, Quality, RD-Agent/LLMs, paid data, and broad or dense grids receive zero budget.

Candidate promotion requires anchor-relative residual information, non-redundancy, fold stability, and matched post-cost incremental contribution. Standalone strength is insufficient. Top-20 equal weight remains Portfolio Baseline V1; one membership-buffer challenger is allowed to change only turnover control.

## Evidence

- `EMPIRICAL_RESEARCH_ONLY`: P0-7D found only one accepted forward member and rejected nine additions.
- `EMPIRICAL_RESEARCH_ONLY`: all four LightGBM variants failed Formula-relative incremental classification.
- `EMPIRICAL_RESEARCH_ONLY`: top-20 equal weight beat the prior complex constructor in 6/6 matched P0-7C comparisons.
- `DOCUMENTED`: a fixed budget and anchor-relative gate reduce new researcher degrees of freedom.

## Consequences

Generation 2 cannot expand into parameter sweeps after results are observed. LowVol is tested through fixed robustness views instead of window substitution. ElasticNet is explained with coefficient stability, family exposure, ablations, and residual analysis; hyperparameters remain frozen.

## Revisit condition

Revisit model or family scope only after P0-7E closes and a later independent result, not another 2019-2025 search, identifies a specific missing mechanism.
