# Research Direction Session — 2026-09-16

## Scope

Durable decisions, evidence summaries, tradeoffs, and project lessons from the research-direction discussion. This record does not contain hidden chain-of-thought.

## Decisions

- Alpha Factory is not a single-strategy project.
- Adopt the five-layer architecture: Data, Alpha Discovery, Alpha Evaluation, Portfolio, Execution.
- Treat L2 Alpha Discovery and L4 Portfolio Construction as the current weak layers.
- Prioritize China-market liquidity effects as a research theme.
- Use ML first to study nonlinear factor interactions, beginning with simple baselines.
- Prefer an Alpha Pool of weak, stable, low-correlated, post-cost usable signals over one magic strategy.
- Build multiple-testing and overfitting controls into the research process.
- Turn papers into explicit hypotheses and controlled experiments rather than treating published claims as local evidence.
- Apply the `FREE FIRST` policy.
- Defer RD-Agent API use until a bounded pilot can justify its incremental cost.

## Evidence summary

- `DOCUMENTED`: controller direction establishes the policies and current layer priorities above.
- `DOCUMENTED`: RD-Agent is installed, while the LLM-backed pilot is paused for lack of credentials.
- `UNKNOWN`: no empirical evidence in this session establishes the profitability of liquidity, nonlinear ML, or any current signal.
- Exact historical execution evidence remains in `D:\alpha-factory` and must be linked by commit and report.

## Tradeoffs

- Free-first preserves budget but may delay access to premium coverage or automated LLM workflows.
- Simple models improve auditability but may miss structure that more flexible models can capture.
- Alpha Pool construction increases diversification opportunities but raises evaluation, correlation, and portfolio-design demands.
- Strong multiple-testing controls reduce false discoveries but slow promotion of candidates.

## Project lessons

- Architecture and research lineage should outlive any particular strategy or tool.
- A paper is a source of hypotheses, not empirical proof for this market and dataset.
- Negative results, blocks, and deferred paths are reusable knowledge.
- Portfolio contribution and execution feasibility matter alongside standalone predictive metrics.
