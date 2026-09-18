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

`P0_6E_FREE_DATA_EXPANSION_V1` completed as `P0_6E_PASS_WITH_WARNINGS`. `FREE_DAILY_V1` is sufficient for a bounded next research iteration under its feature-readiness contract, but remains non-PIT and not production-ready. Exact commits, reports, artifacts, dataset identity, and limitations are recorded in `links/` and the completed task record.

## Boundary

Raw market data and large generated datasets belong outside ordinary Git history and must not be copied into this ledger.

## P0-8 field contract

P0-8 is restricted to actual daily price, bar, activity, turnover, status, provenance, and partial adjustment-factor fields recorded by `FREE_DAILY_V1`. Adjusted-price factors operate only on the frozen action-aware subset. Equal-weight market and breadth series are limited derived composites, not an external certified index. Industry and daily market-cap history are absent, so industry/Size neutralization is unavailable. The Factor Zoo may not approximate unavailable fundamentals with price or turnover proxies.
