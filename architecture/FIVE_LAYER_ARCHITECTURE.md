# Five-Layer Architecture

| Layer | Purpose | Core concerns |
| --- | --- | --- |
| L1 Data | Build the research substrate | Multi-year history, historical universe, PIT and survivorship awareness |
| L2 Alpha Discovery | Generate candidate signals | Formula alpha, ML, later Agent/LLM, later text/event data |
| L3 Alpha Evaluation | Reject fragile candidates | IC/RankIC, stability, robustness, decay, correlation, costs, multiple testing, protected Blind |
| L4 Portfolio | Convert accepted signals into holdings | Ensemble, risk model, transaction-cost-aware optimization, regime allocation |
| L5 Execution | Convert holdings into feasible orders and fills | T+1, price limits, fees, slippage, fills, Shadow, later broker integration |

## Current weakness

L2 Alpha Discovery and L4 Portfolio Construction are currently the weakest layers. L1 work remains an active dependency; L3 controls and L5 realism must not be weakened to accelerate L2 or L4.

## Flow

Each layer produces versioned inputs for the next layer and evidence for the research ledger. A downstream result cannot repair upstream data leakage or missing point-in-time integrity.
