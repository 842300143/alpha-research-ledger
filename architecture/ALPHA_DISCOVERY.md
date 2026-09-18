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

P0-7E was the last major **Generation-1** discovery iteration on 2019-2025. ADR-0014 does not reopen or tune P0-7E; it authorizes a materially different Generation-2 canonical factor-space program with preregistered definitions, budgets, factor structure, and cumulative selection accounting. P0-8 results remain selection-contaminated research evidence and do not authorize protected-holdout access.

## P0-8 discovery sequence

`taxonomy -> canonical definitions -> no-result implementation freeze -> atomic evaluation -> factor map/archetypes -> limited hypothesis-led interactions -> Alpha Pool V2 -> sparse simple model`.

The 103-definition design contains 99 atomic/transformed factors and four conditional prototypes. Parameter variants are explicitly grouped and counted. Size, Value, Quality, industry, text/event, order-book, and deep/RL directions have zero current budget.
