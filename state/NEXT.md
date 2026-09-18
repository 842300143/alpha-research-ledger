# Next Research Work

## Controller direction

`P0_8A_FACTOR_ZOO_BUILD_V1`

Status: `DESIGN_READY` / `NOT_YET_EXECUTED`

The exact specification is `tasks/planned/P0_8A_FACTOR_ZOO_BUILD_V1.md`. A later controller may direct Alpha Factory to implement and freeze the library. This ledger commit performs design only and authorizes neither predictive evaluation nor protected-holdout access.

## Required activation gates

- Verify Alpha Factory P0-7E result commit `27793d974110758ccf83848aed3d9354341b7e3f` and completion checkpoint `c37ab3caf0c50c100906503d17d05fd5f78e2e24` in linear ancestry.
- Bind `FREE_DAILY_V1` dataset hash `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` and actual price/adjustment schemas.
- Bind exact ledger registry, cards, timing, preprocessing, taxonomy, ADR-0014, and P0-8A spec hashes.
- Create a pre-build manifest before implementation/correctness evidence.
- Predicate-deny all rows after 2025-12-31 before conversion or materialization.

## P0-8A bounds

- Draft definitions: 103.
- P0-8B atomic/transformed definitions: 99 maximum after implementation gates.
- P0-8D conditional prototypes: four; compile/schema only in P0-8A.
- Predictive configurations, labels, IC, rankings, portfolios, outcomes: zero.
- Allowed evidence: synthetic/unit/property tests, schema inspection, and bounded through-2025 no-value PASS/FAIL spot checks.
- Size, Value, Quality, industry, paid data, RD-Agent/LLM, broker, trading: zero budget.
- Protected 2026 access: zero.

## Required output

Produce immutable code/config/registry/card hashes, field and parameterization audits, timing/preprocessing audits, correctness tests, a no-results audit, a holdout deny-before-load audit, complete per-factor build states, Independent Validator output, and `P0_8A_FACTOR_ZOO_FREEZE.json`.

## Stop rule

Do not start P0-8B in the same task. If a definition cannot be implemented from actual fields, retain it as `DENIED_NOT_READY` and do not substitute a new factor to preserve the count. If an integrity gate fails, repair only the named implementation defect under unchanged research definitions.

## After P0-8A

Prepare a separate exact P0-8B directive binding the frozen eligible factor IDs and a maximum 297 Stage-1 factor-fold attempts. P0-8B uses 2021-2023 only. P0-8C freezes factor structure before P0-8D interactions and before the one-pass 2024-2025 internal reuse-validation tranche.
