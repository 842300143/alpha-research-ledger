# Next Research Work

## Active task

`EVALRECON01_COMMON_BASELINE_RECONCILIATION_V1` under directive `ALPHA-EVALRECON01-COMMON-BASELINE-RECONCILIATION-V1`.

## Goal

Explain and eliminate the RMB 678.13 discrepancy between the committed Exposure02 V2 P0 AlwaysInvest + EqualWeight and Portfolio02 EqualWeight + AlwaysInvest paths through one authority-bound common baseline and only the necessary correctness-equivalent replay.

## Required result

Bind exact Git/source hashes; compare all 36 decision dates, predictions, Top20 ordering, continuous and integer targets, orders/fills, corporate-action paths, and daily cash/share/NAV states; identify the first divergence and root cause; publish `CANONICAL_COMMON_BASELINE_V1`; and determine which historical task requires a separate minimal replay without automatically changing either winner.

## Protected boundaries

Frozen predecessor results remain unchanged. No new Alpha, tuning, winner selection, 2024-2025 or 2026 access, broker action, payment, credential action, production action, destructive Git action, or history rewrite.
