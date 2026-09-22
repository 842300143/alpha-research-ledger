# ADR-0041: Accept Exposure02 canonical composition V2 disposition

- Status: ACCEPTED
- Date: 2026-09-22
- Task: `EXPOSURE02_CANONICAL_COMPOSITION_REPLAY_V2`
- Supersedes: ADR-0040 active execution state only

## Decision

Accept the additive V2 replay as `PASS_WITH_WARNINGS / ALWAYS_INVEST_RETAINED`. The immutable Exposure02 V2 strategy contract and EVALRECON01 canonical execution contract were composed without rewriting either parent. All 12 new one-use slots completed once with matching result hashes.

The primary RMB 50,000 / 1x full-calendar post-cost terminal wealth is:

- P0 AlwaysInvest: RMB 57,445.71 / 14.89142%;
- P1 AlwaysCash: RMB 50,000.00 / 0.00000%;
- P2 Trend60: RMB 46,117.88 / -7.76424%.

Retain P0 AlwaysInvest under the preregistered terminal-wealth objective and simplicity rule. P2's cash gate did not improve the objective. The result remains selection-contaminated modeled research evidence and is not independent Alpha confirmation or production evidence.

## Integrity and validation

P0 exactly reproduces the EVALRECON01 canonical anchor, including the 2021-07-05 target of 1,100 shares for `000008.SZ`. Every path records exactly 36 strategic allocation calls, zero off-grid reallocations and `HOLDING_PATH_EVENT_COVERAGE_GATE=EXACT_FOR_THIS_REPLAY`. Portfolio02 was not rerun or modified.

Focused tests pass 16/16 and the additive independent validator passes 41/41. A retained mechanical validator-publication failure (`KeyError: score_gate`) was repaired only through an in-memory compatibility view; no market replay was rerun and no result, manifest, strategy or execution contract changed. The full isolated suite is 294 PASS / 18 inherited FAIL / 1 warning; a full-suite PASS is not claimed.

## Evidence

- Alpha Factory result work commit: `489a37206674813c6b56983a88702a485dc99776`.
- Report: `D:/alpha-factory-exposure02-canonical-v2/reports/EXPOSURE02_CANONICAL_COMPOSITION_REPLAY_V2.md`.
- Checkpoint: `D:/alpha-factory-exposure02-canonical-v2/state/checkpoints/EXPOSURE02_CANONICAL_COMPOSITION_REPLAY_V2.json`.
- Diagnostics: `research/exposure02_canonical_composition_v2/DIAGNOSTICS.json` at Alpha Factory result commit.
- Independent validator: 41 PASS / 0 FAIL.

## Boundaries and next direction

V1 remains terminal and unchanged. Portfolio02 remains valid and unchanged. The 2024-2025 and 2026 intervals stayed sealed. No new Alpha research, broker order, payment, credential, deployment, destructive Git, force push or history rewrite occurred.

Next is `EXPOSURE02_PORTFOLIO02_INTEGRATION_DIRECTION`. A separate exact directive is required before any metadata integration, combined replay, new search, later-period access or production promotion.
