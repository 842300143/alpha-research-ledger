# L1 Data Layer

## Objective

Provide multi-year, historical-universe-aware research data with explicit point-in-time and survivorship properties.

## Required properties

- Stable dataset ID, version, and immutable hash.
- Provider, acquisition time, coverage, schema, adjustment, and calendar metadata.
- Historical constituent and listing/delisting treatment where available.
- Clear distinction between documented provider behavior and empirically validated behavior.
- Quality checks for duplicates, gaps, prices, volumes, corporate actions, and temporal leakage.
- Reproducible normalized and research-ready representations.

## Current work

`P0_6E_FREE_DATA_EXPANSION_V1` is the active Alpha Factory execution task. Its commits, reports, artifacts, and resulting dataset identifiers must be linked after completion.

## Boundary

Raw market data and large generated datasets belong outside ordinary Git history and must not be copied into this ledger.
