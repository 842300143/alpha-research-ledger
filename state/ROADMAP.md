# Roadmap

## Near term

1. `P0_6E_FREE_DATA_EXPANSION_V1`: `COMPLETE` / `P0_6E_PASS_WITH_WARNINGS`.
2. `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1`: `DESIGN_READY` / `NOT_YET_EXECUTED`.
3. On controller direction, execute the bounded Formula, simple-ML, Portfolio, and Alpha Pool protocol using 2021-2025 walk-forward OOS while denying Alpha access to 2026.
4. Preserve the old P0-7B Blind as `SUPERSEDED_UNCONSUMED`; never execute it.

## Later

- P0-7D concept: one-run protected recent-holdout evaluation after P0-7C candidates and all dependencies are frozen.
- Mature portfolio construction: ensemble weighting, risk modeling, cost-aware optimization, and regime allocation.
- Expand discovery to Agent/LLM and text/event data only after simpler paths establish a specific incremental need.
- Revisit paid-data validation and production-grade point-in-time/action coverage only when P0-7C exposes a quantified blocker.
- Use Shadow execution before any later broker integration.
- Paper trading remains later and requires separate execution and risk controls.

## Protected boundary

The old P0-7B interval is `SUPERSEDED_UNCONSUMED`; `BLIND_CONSUMED = FALSE`. The new 2026 P0-7C holdout must remain unavailable to ordinary research. Neither holdout may be consumed through roadmap work without its separate, hash-bound task.
