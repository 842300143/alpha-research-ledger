# Factor Card Schema

The machine-readable registry is `FACTOR_REGISTRY_V1.json`. Every entry must contain the following fields before P0-8A can freeze it.

| Field | Type | Rule |
| --- | --- | --- |
| factor_id | string | Stable `FZ1_...` identifier; never reused |
| canonical_name | string | Human-readable exact definition name |
| family | enum/string | One taxonomy family |
| concept | string | Mechanism-level concept, shared across canonical variants where appropriate |
| parameterization_group | string | Groups variants of one concept |
| variant_role | enum | `SINGLE`, `SHORT`, `MEDIUM`, `LONG`, or named mechanism role |
| formula_pseudocode | string | Deterministic formula using lagged/current daily inputs only |
| required_raw_fields | string[] | Must exist in `FREE_DAILY_V1`; derived fields are not listed as raw |
| derived_inputs | string[] | Any adjusted prices, returns, market composites, or rolling statistics |
| lookback_input_horizon | string | Exact sessions and full-history requirements |
| signal_availability_timing | string | Contracted availability and earliest tradable time |
| expected_direction | enum/string | Predeclared signed hypothesis; `HIGHER_EXPECTED_BETTER` unless explicitly diagnostic |
| hypothesis | string | Economic, behavioral, or statistical reason plus falsifiable expectation |
| literature_common_usage_note | string | Common-use note; not an empirical claim |
| expected_turnover | enum | `LOW`, `MEDIUM`, `HIGH`, `VERY_HIGH`, or `UNKNOWN` |
| potential_execution_sensitivity | string | Gap, delay, liquidity, suspension, or cost sensitivity |
| likely_related_redundant_factors | string[] | IDs/groups/families expected to overlap |
| pit_lookahead_risks | string[] | Timing, current-capture, adjustment, universe, or derived-market risks |
| data_readiness_status | enum | `READY_WITH_WARNINGS`, `LIMITED`, or `DEFERRED_TO_P0_8D` in V1 |
| abstraction | enum | `ATOMIC`, `TRANSFORMED`, or `CONDITIONAL` |
| provenance | string[] | Prior experiment, standard construct, or new registered mechanism |
| planned_tests | string[] | Fixed protocol checks; no factor-specific metric shopping |
| lifecycle | enum | Initial value `DISCOVERED`; later governed transitions only |
| definition_status | enum | `DRAFT_DESIGN`, then `FROZEN_P0_8A` after code/hash verification |
| evaluation_stage | enum | `P0_8B` for atomic/transformed; `P0_8D` for conditional |

## Lifecycle

```text
DISCOVERED
  -> EVALUATED
     -> SURVIVED
     -> UNSTABLE
     -> REDUNDANT
     -> COST_KILLED
     -> REGIME_SPECIFIC
     -> REJECTED
```

`INVALID_IMPLEMENTATION`, `DENIED_DATA_GATE`, and `UNKNOWN_INSUFFICIENT_COVERAGE` are terminal evidence states for the registered attempt; they do not return budget. `REDUNDANT` does not mean economically false; it means the tested definition did not establish distinct information under the frozen structure protocol.

## Freeze semantics

`DRAFT_DESIGN` means the research definition is reviewable but not executable for predictive evidence. P0-8A must bind normalized JSON, formula code, tests, field schema, timing decisions, universe, and preprocessing hashes. Once `FROZEN_P0_8A`, any semantic change creates a new factor ID and consumes new budget; typo-only additive corrections must be documented and must not follow result access.
