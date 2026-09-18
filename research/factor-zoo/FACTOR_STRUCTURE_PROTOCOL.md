# P0-8C Factor Structure Protocol

## Objective

Describe the shape of the factor space, not produce a long RankIC leaderboard. P0-8C uses only Stage-1 through-2023 evidence from P0-8B and the exact frozen surviving score streams.

## Four relationship layers

### A. Signal correlation

For every pair, compute daily cross-sectional Spearman correlation on matched eligible rows, then retain mean, median, absolute mean, fold values, matched rows/dates, and coverage. Do not fill missing pairs. A pair needs at least 60 matched dates and 60 securities per sufficient date aggregate.

### B. IC-time-series correlation

Correlate the pair's daily RankIC series on matched dates using Pearson and Spearman measures. This asks whether factors succeed and fail together even when raw scores differ.

### C. Portfolio overlap

Compute Top-20 holdings intersection, union, Jaccard, directional overlap, and fold distributions on matched rebalance dates under `TOP20_EQUAL_WEIGHT`.

### D. Residual / conditional information

For Factor B against Factor A or a frozen representative set, fit OLS using ranked factor scores on the other Stage-1 folds, with intercept, no label, and no penalty; apply to the held-out fold. Retain held-out residual RankIC, sign count, coverage, turnover, and cost. Multivariate residualization is allowed only against already selected representatives in deterministic cluster order.

## Graph and clustering

Build a multiplex Factor Graph:

- node: factor ID, family, abstraction, lifecycle, stability, turnover, cost, coverage, and simplicity;
- signal edge: absolute mean signal correlation >= 0.80;
- shared-efficacy edge: absolute IC-series correlation >= 0.75 and Top-20 Jaccard >= 0.60;
- overlap edge: Top-20 Jaccard >= 0.80;
- residual edge attribute: retained residual RankIC and pass/fail, never used alone to create an edge.

Also run average-linkage hierarchical clustering on distance `1 - abs(mean signal Spearman)`. Cut at distance 0.20, corresponding to absolute signal correlation 0.80. Missing distances deny the pair from automatic same-cluster assignment. Deterministic graph community detection may be reported with a frozen seed as a diagnostic cross-check; it cannot override residual evidence.

PCA may report variance concentration and loading stability. It is diagnostic only and cannot automatically promote a component or Alpha.

## Redundancy rule

A factor is `REDUNDANT` relative to its cluster representative when:

1. it has a hard signal, shared-efficacy, or overlap edge to the representative; and
2. cross-fitted residual mean RankIC is below 0.005, or below 25% of the factor's original mean RankIC; and
3. fewer than two of three Stage-1 residual folds are positive.

Missing residual evidence is `UNKNOWN`, never redundant by default and never favorable for pool entry.

## Archetype representative selection

Within each cluster, choose one representative by this lexicographic order:

1. passes stability and multiplicity controls;
2. greater positive-fold count, then higher minimum-fold RankIC;
3. lower turnover per rebalance;
4. lower frozen-cost drag;
5. broader coverage and fewer missing observations;
6. simpler abstraction (`ATOMIC` before `TRANSFORMED` before `CONDITIONAL`);
7. shorter formula description and fewer raw fields;
8. ascending factor ID.

Historical return and mean RankIC break no tie before the criteria above. The representative is not automatically an Alpha Pool member.

## Cluster record

Every cluster/archetype must retain:

- cluster ID, representative, and all members;
- families/concepts and common mechanism;
- within-cluster signal and IC correlations;
- portfolio overlap distribution;
- residual-information decisions;
- representative-selection trace;
- unknown or conflicting evidence;
- Stage-2 validation status when later opened.

## Outputs

- pairwise signal-correlation table;
- IC-series-correlation table;
- Top-20 overlap table;
- residualization table;
- hierarchical-cluster artifact and deterministic graph artifact;
- cluster/archetype registry;
- Factor Graph/Map in machine-readable JSON plus a human-readable report;
- frozen representatives and the exact P0-8D-eligible archetype pairs.
