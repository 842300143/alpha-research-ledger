# ADR-0016: Bounded Exploratory Combinatorial Search

- Status: Accepted for `CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1`
- Date: 2026-09-20
- Controller directive: `EXECUTE_CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1`

## Context

P0-8C froze 16 archetypes and 12 pair leads. P0-8D0 investigated those 12 and issued zero executable Interaction Cards under ADR-0015's mechanism-led preregistration gate. A separate question remains: whether bounded symbolic combinations of the 16 frozen signals improve a specified forward prediction model. The earlier ordered ten-item residual diagnostic is not an independent dimension proof and is not the only input to this new question.

## Decision

Authorize CAD01 as a **new, separately named `EXPLORATORY_SEARCH` namespace** with its own cumulative budget, grammar, model, time split, attempt ledger, and stop rule as frozen in `research/combinatorial-discovery/CAD_RESEARCH_CONTRACT_V1.md` and the execution repository's machine-readable contract. Multiple reasonable expressions inside that preregistered grammar may be explored; a financial narrative need not uniquely imply each formula. Purely empirical variants are labeled `EMPIRICAL_HYPOTHESIS` with no invented causal story. No extra external raw data field is introduced by a combination. Existing P0-8D and P0-8D0 dispositions, budgets, and frozen artifacts stay unchanged. This decision does not activate P0-8D, P0-8E/F/G, or any protected interval.

CAD01 evaluates representation novelty, matched model-relative increment, and separate synthetic-cost economic increment. OII is a project shorthand, not a new established statistic. All 2019–2023 findings inherit prior selection and are at most `EXPLORATORY_CANDIDATE`. The 2024–2025 Generation-2 test interval remains locked for this task and had already been used by Generation-1. The 2026 holdout remains sealed.

## Persistence and synchronization

One worker may repair the documented input-placeholder readiness deadlock in a finite maintenance audit, then resume ordinary execution only after normal `worker_start` says `READY:YES`. A local commit in each repository is an exact local evidence anchor even if a bounded GitHub push fails from a transient network error. In that case record `SYNC_PENDING` with the unpublished SHAs and retry at most twice without force push or overwriting divergent remote history. Remote publication is not a prerequisite for internally consistent local work. This policy replaces the earlier operational implication that successful push was necessary to continue; it does not weaken frozen-hash, test, checkpoint, or protected-data gates.

## Evidence and limits

- `DOCUMENTED`: this decision, CAD01 contract, official prior-work map, and source audit.
- `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`: historical P0-8B/C outcomes and any CAD01 matched prediction result.
- `SYNTHETIC`: the cost and vector execution diagnostic.
- `UNKNOWN`: independent forward validity, PIT and survivorship completeness, real execution, impact, and production readiness.

The exact resume entry is `ALPHA-CAD-RESUME` plus both repository paths. The worker must recover state, manifest, attempts, elapsed budget, and next action from Git and files, not from chat memory.
