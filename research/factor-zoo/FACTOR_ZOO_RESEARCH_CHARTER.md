# P0-8 Factor Zoo Research Charter

- Program: `P0-8 FACTOR ZOO & FACTOR STRUCTURE DISCOVERY V1`
- Dataset: `FREE_DAILY_V1`
- Design date: 2026-09-18
- Mode: research governance and design only
- Protected holdout: `2026-01-05..2026-09-15` / `SEALED / UNACCESSED / UNCONSUMED`

## Research question

How many mutually independent, repeatable, predictive factor dimensions can be constructed from the fields actually available in `FREE_DAILY_V1`, and what correlation, conditional, redundancy, and incremental relationships connect them?

The objective is not to find the highest-return strategy. A valid result may be that many formulas collapse into a few archetypes, disappear after cost, or have no stable predictive information.

## Unit distinctions

| Unit | Meaning | Accounting rule |
| --- | --- | --- |
| Factor Concept | Economic, behavioral, or statistical idea | Count once even when it has canonical horizons |
| Factor Formula | Exact deterministic transformation | One registered definition and hash |
| Parameterization | A mechanism-meaningful setting of a formula | Counts against the configuration budget |
| Factor Family | Taxonomic grouping, not evidence of independence | Never counted as a predictive result |
| Interaction | Predeclared relationship between established archetypes | Separate P0-8D budget; not atomic-factor budget |
| Portfolio Strategy | Holdings/weighting/execution rule applied to a score | Separate from factor definition and IC evidence |

Adjacent horizons are not independent concepts. Canonical short, medium, and long variants are allowed only when each represents a declared mechanism or holding scale and all variants consume budget.

## Evidence contract

- `EMPIRICAL`: field coverage, schema, data-quality, and completed P0-7 result artifacts.
- `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`: all factor and strategy evidence produced from reused 2019-2025 data.
- `DOCUMENTED`: taxonomy, registry, hypotheses, preprocessing, timing, evaluation, structure, interaction, budgets, and roadmap.
- `SYNTHETIC`: modeled costs, slippage, fills, and any derived execution assumptions.
- `UNKNOWN`: independent confirmation, certified PIT/survivorship, authoritative historical limits, empirical impact, capacity, production, and real trading.

No P0-8 result may be relabelled independent confirmation. No vendor statement becomes empirical evidence without validation.

## Current data boundary

The canonical raw price table contains `trade_date`, `symbol`, OHLC, `preclose`, `volume`, `amount`, `turnover`, provider `pct_change`, `trade_status`, `st_status`, `suspension_status`, price-basis/provenance fields, and a partial `adj_factor` table. Formula implementation must derive adjusted OHLC from raw OHLC and the factor; provider `pct_change` is not a substitute for action-aware returns.

The executable research universe remains the frozen action-aware subset unless a later separately governed data repair changes the feature-readiness contract. Size, Value, Quality, industry classifications, authoritative historical daily limits, and complete PIT state are absent or not ready.

## Generation-1 inheritance

- Final Generation-1 anchor: `P07C_ML_ENET_A010_L50`.
- Final constructor: `TOP20_EQUAL_WEIGHT`.
- Strict pool: one member.
- Cumulative predictive history: 34 configurations and 170 fold attempts, plus P0-7D qualification degrees of freedom.
- P0-7E: all three Formula candidates passed standalone evidence and failed the complete anchor-relative incremental gate; the buffer challenger was not promoted.

The anchor is a comparator in P0-8E/P0-8F, not a taxonomy boundary. Historical failures remain visible and do not prohibit testing materially different canonical concepts under the new registry.

## Program invariants

1. Define and hash factors before predictive results.
2. Use only actual fields; unavailable families receive zero budget.
3. Deny protected 2026 data before materialization.
4. Retain failed, denied, invalid, and cost-killed records.
5. Do not recycle budget or create neighboring variants after results.
6. Separate atomic evaluation, structure discovery, interactions, pool selection, and model combination.
7. Build the factor map before any interaction or sparse multifactor stage.
8. Prefer stability, simplicity, low turnover/cost, broad coverage, and residual information over historical return alone.
9. Treat null findings and few-dimensional structure as successful answers.

## Staged 2019-2025 use

P0-8 introduces a procedural separation that reduces future leakage but does not create an independent holdout:

- `R1_STRUCTURE_RESEARCH`: WF1-WF3 / 2021-2023 for atomic screening and factor-structure discovery.
- `R2_INTERNAL_REUSE_VALIDATION`: WF4-WF5 / 2024-2025, opened once only after factor lifecycle, cluster, archetype, and interaction rules are frozen.
- 2019-2020 supplies warmup/training history where required.

The second tranche is called internal reuse validation because those years already influenced Generation-1 research. It is not Blind and cannot support independent-confirmation claims.

## Definition-freeze gate

This design publishes 103 draft canonical definitions: 99 atomic/transformed definitions and four conditional prototypes reserved for P0-8D. `P0-8A` must implement formulas, run no-label correctness tests, verify field/timing behavior, and freeze exact code/config/registry hashes. Predictive evaluation is prohibited until that gate passes.

## Success criteria

P0-8 succeeds if it answers, with retained evidence:

1. how many meaningful canonical factors can be built;
2. which families show stable predictive information;
3. which successful formulas share one information cluster;
4. how many independent predictive dimensions remain;
5. which factors retain residual information;
6. which effects are regime-specific;
7. which are killed by turnover or cost;
8. which hypothesis-led interactions add information;
9. whether Alpha Pool V2 is richer than the singleton anchor; and
10. whether a simple sparse model adds stable value from structured representatives.

Zero survivors, zero interactions, or an unchanged singleton anchor are valid outcomes.
