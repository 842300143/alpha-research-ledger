# CAD01 Combinatorial Discovery Pilot V1 — Research Ledger summary

Status: `EXPLORATORY_PILOT_COMPLETE`. Evidence: `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` for matched historical prediction metrics; `SYNTHETIC` for modeled portfolio execution and costs. These are three exploratory hypotheses, zero confirmed Alpha. The single real run stopped on the frozen `STAGNATION_RULE`; no expansion or rerun is authorized by this summary.

## Immutable references

| Item | Reference |
| --- | --- |
| Dataset | `FREE_DAILY_V1` hash `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` |
| P0-8C result payload | `995efd57f952c9ddfb5527f992225764bb7ce22814f7a28478492f66e04e9c12` |
| P0-8C handoff payload | `2502ac870d0767db8839665ca664251e7652b7e493e7c6986719f993486ccb4c` |
| Alpha Factory maintenance | `f4295368e43f6396a64307d4888140752a71ae56` |
| Alpha Factory pre-result code/policy | `a9f1dbc74471df1d55fce06588d169dc14973940` |
| Alpha Factory manifest/queue | `419dc0e0b35454934cef23f4c0536c10b6405d16` |
| Alpha Factory result work | `df327bfbd653864368a817eef7e64006b6575022` |
| Exact manifest SHA-256 | `7499d1fe58330a1c319edf68b2665f6495a7f79a6e258a9df8f8b7ee8f5490f3` |
| Result self-hash | `d58a4fe4031465b2f7405834684184d67c5e9115e48cbe6d5765ea5329173d56` |

The execution report is `D:\alpha-factory\reports\CAD01_COMBINATORIAL_DISCOVERY_PILOT_V1.md`. The exact machine-readable record is in `D:\alpha-factory\research\cad01\{manifests,state,results}`. The Ledger source audit, prior-art map, contract, and ADR-0016 precede the real result.

## Used budget and output

The fixed queue held 160 proposals under a 2,048 cap. The run processed/evaluated 131, reserved three additional fixed lower-order controls, and used 134 of 256 label evaluations and 402 fold attempt slots. The persisted search clock recorded 622.125 of 14,400 seconds. All 131 processed attempts ended `EVALUATED`: zero invalid, zero duplicate, zero failed. Twenty-nine scheduled proposals remained unprocessed after the predeclared stagnation stop. Three of ten allowed modeled cost rechecks ran, and three of five allowed exploratory candidate archives were created. The last 64 attempts contained no newly qualified candidate.

| Candidate | Form and parent factors | Paired mean daily delta RankIC | Modeled cumulative net return delta, 1x / 2x costs |
| --- | --- | ---: | ---: |
| `CAD-3f302a5c4861399a445f` | triple product: `FZ1_COR_004`, `FZ1_DST_001`, `FZ1_LIQ_005` | 0.01263434 | +0.09492504 / +0.08972195 |
| `CAD-e42009bab4f0a0b0ae2b` | pair product: `FZ1_BAR_005`, `FZ1_GAP_005` | 0.00823890 | +0.12761321 / +0.12132432 |
| `CAD-e0b9139948ec2367c77b` | triple product: `FZ1_COR_004`, `FZ1_GAP_005`, `FZ1_VOL_004` | 0.00789611 | +0.04123545 / +0.03774109 |

All three had 45,949 matched evaluation rows out of 45,949 baseline rows, positive paired deltas in all three folds, and passed the predeclared fixed lower-order control. The return deltas are decimal differences in compounded net modeled returns, not realized orders or percent returns. Exact fold, uncertainty, formula, and cost details are in the candidate archive. The independent reviewer verified manifest, source, result, ledger, referenced data-artifact hashes, budgets, and all 393 primary fold label-end boundaries without reading market rows.

## Limits and next boundary

This discovery data and its 16 base signals were selected through earlier historical research. The full 160-proposal synthetic null search yielded 44 apparent screen passes and 19 control passes despite zero true Alpha. CAD01's own thresholds, moving-block intervals, and the historical P0-8B BH-FDR result do not grant a confirmatory error rate for this search. `2024–2025 accessed: NO`, `2026 accessed: NO`, and `external LLM/API calls: 0` are supported by the pinned loader/code path and recorded metadata, not independent operating-system telemetry. The old P0-8D/P0-8D0 12 investigated pairs remain zero executable and unrun. A future task may design a complete-system freeze from these existing artifacts; it must not silently restart CAD01 or open a test interval.
