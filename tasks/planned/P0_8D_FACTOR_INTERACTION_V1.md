# P0_8D_FACTOR_INTERACTION_V1 — bounded disposition of frozen pairs

- Task ID: `P0_8D_FACTOR_INTERACTION_V1`
- Directive: `EXECUTE_P0_8D_FACTOR_INTERACTION_V1`
- Status: `SPEC_FROZEN_FOR_SEPARATE_EXECUTION`; this Ledger task does not execute research.
- Execution repository: `D:\alpha-factory`.
- Source Alpha Factory commit: `6180b4e2d8f2dfa258b0aaee5b71ba6e75915ec0`.
- Frozen P0-8C result bundle hash: `995efd57f952c9ddfb5527f992225764bb7ce22814f7a28478492f66e04e9c12`.
- Frozen P0-8D handoff hash: `2502ac870d0767db8839665ca664251e7652b7e493e7c6986719f993486ccb4c`.
- Dataset: `FREE_DAILY_V1`, hash `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` (inherited; do not load for this design task).
- Evidence classification: P0-8C relationships are `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`; this specification is `DOCUMENTED`; modeled costs are `SYNTHETIC`.

## 1. Authoritative sources and entry gates

Verify the two self hashes above against `research/factor_structure_v1/results/RESULT_BUNDLE.json` and `research/factor_structure_v1/handoff/P0_8D_HANDOFF.json`. Require P0-8C `P0_8C_PASS_WITH_WARNINGS`, 27 survivor factors, 16 archetypes, the exact 12 ordered handoff pairs, and a clean worktree. Bind the P0-8C `ARCHETYPE_REGISTRY.json`, `RESIDUAL_INFORMATION.json`, and `FACTOR_GRAPH.json` without altering them. Also bind the P0-8A factor freeze, P0-8B factor results and fold/split/cost contract, and `FREE_DAILY_V1` feature-readiness evidence before any future score evaluation.

Governing Ledger documents are `research/factor-zoo/P0_8_ROADMAP.md`, `FACTOR_INTERACTION_POLICY.md`, `FACTOR_STRUCTURE_PROTOCOL.md`, `FACTOR_EVALUATION_PROTOCOL.md`, `FACTOR_PREPROCESSING_POLICY.md`, `FACTOR_TIMING_CONTRACT.md`, and `MULTIPLE_TESTING_POLICY_V2.md`, plus `decisions/ADR-0010-SEAL-2026-HOLDOUT-DURING-GENERATION2.md`, `ADR-0012-GENERATION2-MECHANISM-ORTHOGONALITY.md`, `ADR-0013-LAST-MAJOR-ITERATION-BEFORE-HOLDOUT.md`, and `ADR-0014-GENERATION2-FACTOR-ZOO-RESEARCH-POLICY.md`.

The P0-8C handoff is *pair eligibility evidence*, not an interaction-definition registry. Its only per-pair rationale is `CROSS_CLUSTER_NO_HARD_REDUNDANCY_EDGE`. Neither it nor the governing policy selects a unique interaction form, signed formula, orientation, or state threshold for any pair. The factor-card hypotheses suggest mechanisms but cannot uniquely resolve these design choices. Therefore all 12 pair slots receive a terminal `NOT_EXECUTABLE_IN_V1` disposition before predictive access. This is a negative design result, not an empirical rejection or evidence that interactions do not exist. No form or formula may be chosen later under this V1 directive.

## 2. Exact ordered candidate population and disposition

The following IDs reserve the exact handoff order. They are *pair-slot IDs*, not registered executable interaction hypotheses. `A/B archetype` comes from the frozen P0-8C archetype registry. Every row has the same structural provenance: frozen P0-8C handoff, cross-cluster representatives with no hard redundancy edge. The mechanism column is a pre-result question derived from parent factor-card concepts, not a claim of observed state dependence.

| Pair-slot ID | Factor A / archetype | Factor B / archetype | Mechanism question from parent cards | Terminal reason |
| --- | --- | --- | --- | --- |
| `P08D_INT_01` | `FZ1_TOV_001` / `C13` | `FZ1_TOV_004` / `C15` | Does the low-turnover neglect signal depend on whether attention is trending down? | Level/trend orientation, form, and signed rule are not selected. |
| `P08D_INT_02` | `FZ1_TOV_001` / `C13` | `FZ1_TOV_003` / `C14` | Does baseline neglect change the meaning of a recent signed turnover innovation? | Baseline/innovation orientation, form, and signed rule are not selected. |
| `P08D_INT_03` | `FZ1_LIQ_005` / `C08` | `FZ1_TOV_004` / `C15` | Does stable trading liquidity distinguish persistent neglect from a temporary attention trend? | A conditional gate, product, and residual form are all plausible; no state rule is frozen. |
| `P08D_INT_04` | `FZ1_LIQ_005` / `C08` | `FZ1_TOV_003` / `C14` | Does liquidity stability change the interpretation of abrupt turnover contraction? | A conditional gate, product, and residual form are all plausible; no state rule is frozen. |
| `P08D_INT_05` | `FZ1_LIQ_005` / `C08` | `FZ1_TOV_001` / `C13` | Is the neglect signal different when trading amount is stable? | The cards do not select which factor conditions the other or a threshold. |
| `P08D_INT_06` | `FZ1_TOV_003` / `C14` | `FZ1_TOV_004` / `C15` | Does a recent attention innovation matter differently under a longer attention trend? | Horizon interaction form and signed state are not selected. |
| `P08D_INT_07` | `FZ1_BAR_004` / `C01` | `FZ1_TOV_004` / `C15` | Does upper-price rejection have a different implication as turnover attention changes? | The cards do not select rising or falling attention as the state or the form. |
| `P08D_INT_08` | `FZ1_DST_001` / `C04` | `FZ1_GAP_004` / `C06` | Does return asymmetry distinguish durable overnight information from lottery demand? | The cards do not select an asymmetry state, threshold, or signed formula. |
| `P08D_INT_09` | `FZ1_COR_004` / `C03` | `FZ1_TOV_003` / `C14` | Does breadth sensitivity alter the meaning of a turnover innovation? | A market-state direction and exact conditional or product form are not selected. |
| `P08D_INT_10` | `FZ1_DST_001` / `C04` | `FZ1_MKT_002` / `C09` | Does defensive market beta change the interpretation of return asymmetry? | Direction of dependence, state threshold, and form are not selected. |
| `P08D_INT_11` | `FZ1_BAR_004` / `C01` | `FZ1_MKT_002` / `C09` | Does defensive market beta change the meaning of upper-price rejection? | Direction of dependence, state threshold, and form are not selected. |
| `P08D_INT_12` | `FZ1_DST_001` / `C04` | `FZ1_TOV_004` / `C15` | Does changing attention alter a return-asymmetry signal? | Attention-state orientation, threshold, and form are not selected. |

For **each** listed slot: `interaction_type = NONE`; `formula = NONE`; `direction = NONE`; `state_definition = NONE`; `threshold = NONE`; `execution_status = NOT_EXECUTABLE_IN_V1`. The pair eligibility reason remains `CROSS_CLUSTER_NO_HARD_REDUNDANCY_EDGE`. The expected evaluation unit, had a valid interaction been registered, would be a symbol-date centered within-date rank score with a 20-session primary forward label, three annual WF1-WF3 terminal fold records, and the fixed 5/60-session diagnostics. No such score or label is computed under this V1 specification.

## 3. Definition and comparator rule

An executable interaction would require **before any result access** one unique immutable record per pair: ID, A and B, archetypes, graph/residual provenance, economic or behavioral mechanism, one of the four allowed forms (`NUMERIC_A_X_B`, `A_CONDITIONAL_ON_B_STATE`, `A_RESIDUAL_CONDITIONED_BY_B`, `RANK_COMBINATION`), exact formula, direction, fixed or training-only state rule and threshold where applicable, timing, preprocessing, falsification rule, and incremental mechanism. No pair meets that complete registration gate in V1. A later proposal requires a separate new directive and budget decision; this V1 cannot silently fill the blanks.

For an otherwise valid future registration, parent comparators are each frozen signed centered percentile rank `s_A = rank_pct(A)-0.5` and `s_B = rank_pct(B)-0.5`, on the common eligible symbol-date rows. The fixed simple-addition comparator is `0.5*(s_A+s_B)` with higher favorable; no fitted weights or result-driven reranking. Compare interaction against **A**, **B**, and this arithmetic rank combination on matched rows/folds. Improvement of the addition over A is never true-interaction evidence. Signal residualization against A, B, and addition must be cross-fitted without using outcome labels in the fit.

## 4. Timing, data, and isolation

Only WF1-WF3 through 2023 are eligible for P0-8D discovery/evaluation. The primary label contract is the unchanged 20-session cross-sectional-median-relative adjusted return from `t+1` eligible open to `t+20` adjusted close, with 5/60-session decay diagnostics inside folds. Factor and any state at `t` use only information available after `t` close; earliest portfolio entry is `t+1` eligible open. Full parent lookbacks, action-aware eligibility, positive required adjustment paths, within-date ranking, missingness without imputation, and training-only fitted preprocessing remain mandatory. A threshold must never use held-out or future data. The existing non-PIT and incomplete-survivorship limitations remain warnings on claims.

WF4/WF5 and 2024-2025 Stage 2 are closed for selection, thresholds, form choices, and ranking. The 2026 holdout is `SEALED / UNACCESSED / UNCONSUMED`, including features, labels, coverage, and normalization. No ML, dynamic allocation, Alpha Pool promotion, new atomic factor, parameter change, or additional pair is authorized.

## 5. Budget and cumulative multiplicity

- Frozen pair slots: **12**. Executable registered interactions: **0**. Candidate replacements: **0**.
- Maximum hypothetical Stage-1 volume from the policy: `12 × 3 = 36` fold attempts. Actual V1 predictive attempts: **0**. All 12 slots terminate `NOT_EXECUTABLE_IN_V1`; their 36 associated fold positions are `NOT_REGISTERED_BY_DESIGN`, not transferable to other pairs or formulations.
- Inherited P0-7C/P0-7E: 34 predictive configurations and 170 fold attempts; P0-7A's separate 26 executed records and 17 aborted registrations remain separately reported; P0-7D has 136 pair decisions and 45 held-out Formula-span reconstructions.
- P0-8B actual: 97 definitions, 291 fold attempts, including retained failures; P0-8C actual: 351 pair assessments and 26 residual decisions. Do not reset or subtract these because V1 has no executable interaction.
- The P0-8B shared 1,000-permutation, moving-block-bootstrap, and BH-FDR procedures are inherited methodological controls. With **zero registered P0-8D hypotheses**, a P0-8D interaction p-value, BH family, or bootstrap interval is `NOT_APPLICABLE_NO_EXECUTABLE_HYPOTHESES`. Do not claim a multiplicity PASS from this absence. A later interaction spec must freeze its statistical family and randomization schedule before any results.

## 6. Evaluation and lifecycle contract

For every **future separately authorized executable** interaction, retain matched A, B, addition, and interaction RankIC; incremental and cross-fitted residual RankIC against each; three fold signs and minimum fold; sample/conditional-state coverage, prevalence and cell sizes; signal correlation and Top-20 overlap with both parents; turnover; gross, frozen-cost, and 2x-cost Top-20 diagnostics; drawdown; 5/20/60-session decay; predeclared regime cells; readiness limitations; and all terminal failures. Apply the P0-8B standalone gates plus the interaction policy's residual mean RankIC `>= 0.005` with at least two positive folds against A, B, and addition, redundancy exception, one strict operational improvement without other hard-gate breach, and positive 2x-cost behavior. Conditional cells below the protocol minimum are `UNKNOWN`.

V1 has no executable interaction and therefore **none** may be classified `TRUE_INTERACTION`, `PARTIAL_INTERACTION`, `SIMPLE_ADDITIVE`, `REDUNDANT`, `UNSTABLE`, `COST_KILLED`, or empirically `REJECTED`. All 12 have the pre-result terminal design classification `NOT_EXECUTABLE_IN_V1`; no positive or negative predictive inference follows. In a later separately frozen protocol, failure versus either parent is `REPACKAGING_REJECTED`, insufficient conditional coverage is `UNKNOWN_INSUFFICIENT_COVERAGE`, and passing standalone/additive value without a distinct residual increment is `SIMPLE_ADDITIVE`, never `TRUE_INTERACTION`.

## 7. Required V1 execution artifacts and validator

The separate Alpha Factory worker may produce only a no-result disposition registry with all 12 ordered slots and their reasons, a machine-readable and human-readable interaction map containing **zero accepted interaction edges**, inherited accounting, a Validator result, a formal report/checkpoint, and a P0-8E handoff stating zero accepted interactions and the frozen 16 archetypes. It must not load labels, score streams, or outcome-bearing fold results to populate missing definitions. P0-8E can later decide whether to validate archetypes alone; P0-8D must not run it.

Independent Validator checks exact ordered 12-pair population and self hashes; no substitutions; all 12 `NOT_EXECUTABLE_IN_V1`; zero executable formulas, predictive attempts, and interaction metrics; provenance retained; no threshold/form/sign choice after results; WF4/WF5 and 2026 isolation; timing contract; cumulative accounting; zero ML/dynamic allocation; reproducibility of the empty interaction map; and complete zero-interaction P0-8E handoff. A claimed true interaction or metric without a pre-result executable definition is an integrity **FAIL**.

## 8. Stop condition

Close after the no-result disposition and Validator as `P0_8E_HANDOFF_READY / WAIT_FOR_CONTROLLER_DIRECTION`, with all inherited claim limitations and zero accepted interactions. Do not auto-run P0-8E. If source hash, pair count/order, or policy binding differs, fail closed before producing even the disposition handoff. This specification never authorizes predictive P0-8D computation.
