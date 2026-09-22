# ADR-0028: Target the seven CAQUAL01 event gaps

- Date: 2026-09-21
- Status: Accepted / Active
- Controller directive: `ALPHA-CAQUAL02-UNRESOLVED-EVENT-CLOSURE-V1`
- Alpha Factory base work commit: `30aabd4b63f3ab26b8b6ab322638e6a0b489fd6a`
- Alpha Factory base state commit: `0c399a201a8dac8cefabe190b9487d66237b63b9`
- Research Ledger base commit: `cf925366564a40b70661b40ea438980eac61f610`

## Decision

Authorize only the exact four-symbol/seven-date free-official-source follow-up left by CAQUAL01. Execute it in isolated additive `caqual02` worktrees without merging shared main. Preserve CAQUAL01 and its 280 matched events.

## Evidence and gates

Official issuer/SZSE/CNINFO evidence has priority. A factor ratio or date proximity cannot establish an event. Historical event facts may reconstruct an already-realized holding account but cannot enter predictive features. Automatic entitlements need exact cash/share transforms; elective rights/subscription actions need an unresolved future `PARTICIPATE`/`DECLINE` controller policy.

`EXACT_EVENT_AWARE` is available only if every gap is reliably explained, every automatic entitlement is executable, no investor election remains unhandled, and the CAQUAL01 matched-event contract remains valid. Otherwise use `EVENT_DATA_COMPLETE_POLICY_REQUIRED` for complete elective data awaiting policy, or retain `TOTAL_RETURN_APPROX_ONLY` for unknown/contradictory evidence.

## Boundaries

No market-wide scan, paid data, credential-sensitive access, Alpha research, strategy-return comparison, REQUAL01 feature injection, EXPOSURE/portfolio replay, 2024-2025/2026 market-row access, broker operation, or branch merge is authorized.
