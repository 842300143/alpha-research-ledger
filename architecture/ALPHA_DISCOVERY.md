# L2 Alpha Discovery

## Objective

Produce diverse, economically plausible candidate signals for controlled evaluation.

## Research tracks

1. Formula alpha with transparent definitions and baseline comparisons.
2. Simple ML for nonlinear factor interactions, using interpretable baselines before deep models.
3. Later Agent/LLM-assisted discovery when incremental value justifies API cost.
4. Later text and event data after data lineage and evaluation controls are mature.

## Current priorities

- Use `P07C_ML_ENET_A010_L50` as a research anchor, not an independently confirmed Alpha.
- Run exactly three P0-7E Formula candidates: signed abnormal turnover, medium reversal excluding the most recent five sessions, and one very-short-reversal x abnormal-turnover interaction.
- Test LowVol through fixed robustness views rather than another window search.
- Decompose the anchor with coefficient stability, family exposure, four ablations, and Formula-span residual information; do not tune `alpha` or `l1_ratio`.
- Keep LightGBM, deep models, Size, Value, Quality, and broad parameter search at zero P0-7E budget.

## Entry criteria for evaluation

A candidate needs an ID, economic intuition, signal definition, expected direction, horizon, required data, confounders, and falsification criteria. Discovery does not confer acceptance.

P0-7E is the last major discovery iteration on 2019-2025. Later work must use the frozen final pool and a separate protected-holdout decision or introduce materially new external evidence; disappointing results do not reopen Generation N.
