# L5 Execution Engine

## Objective

Convert portfolio targets into realistic orders and measured fills under China-market constraints.

## Required modeling

- T+1 restrictions.
- Price limits and non-tradable states.
- Commissions, taxes, and other fees.
- Slippage and market impact assumptions.
- Partial fills, rejected orders, and stale targets.
- Liquidity and capacity limits.

## Progression

1. Deterministic simulation with explicit assumptions.
2. Shadow execution with reconciliation and operational controls.
3. Later broker integration only with explicit human authorization and risk controls.

Research records live here; execution code and run artifacts live in Alpha Factory.
