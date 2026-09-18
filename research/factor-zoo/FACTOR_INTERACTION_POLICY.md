# P0-8D Factor Interaction Policy

## Entry gate

Interactions are prohibited until P0-8C freezes the Factor Graph, archetypes, representatives, and residual evidence. Atomic definitions do not receive interaction variants merely because they performed well.

An interaction may enter the registry only when at least one of these is documented before result access:

- a clear economic or behavioral mechanism;
- complementary graph position across archetypes;
- a precise conditional hypothesis;
- residual analysis indicating state-dependent information.

Every entry must name both parents, interaction type, formula, direction, state threshold, timing, falsification rule, and expected incremental mechanism.

## Allowed forms

1. `NUMERIC_A_X_B`: product of centered within-date ranks.
2. `A_CONDITIONAL_ON_B_STATE`: A active only in a training-fitted or explicitly fixed B state.
3. `A_RESIDUAL_CONDITIONED_BY_B`: cross-fitted residual or state-specific residual, with no outcome label in residualization.
4. `RANK_COMBINATION`: fixed arithmetic rank combination justified by complementary archetypes.

These forms are distinct configurations. Trying more than one form for the same pair consumes separate slots and requires separate mechanisms.

## Budget

- Maximum registered interactions: 12.
- Maximum per unordered archetype pair: 2.
- Maximum conditional prototypes promoted from the draft registry: 4.
- Fold attempts in Stage 1: 12 x 3 = 36 maximum; unused slots remain `NOT_REGISTERED_BY_DESIGN` and cannot be recycled.
- Stage 2 attempts: only frozen Stage-1 survivors x 2.
- Brute-force pair enumeration: `NO`.
- New thresholds, neighboring states, alternate signs, alternate weights, and new interaction forms after results: `NO`.

The four design prototypes—liquidity-state x reversal, volatility-state x momentum, volume-confirmation x breakout, and market-drawdown-state x low-vol—are hypotheses only. P0-8C evidence must still satisfy the entry gate; no prototype is guaranteed a slot.

## Evaluation

An interaction must pass the P0-8B standalone gates and additionally:

- retain residual mean RankIC >= 0.005 with at least two of three positive folds against each parent and their arithmetic rank combination;
- avoid signal correlation >= 0.80 and Top-20 Jaccard >= 0.80 with either parent unless residual evidence clearly passes;
- strictly improve at least one of minimum-fold RankIC, drawdown, positive regime share, or turnover-adjusted net value without breaching the other hard gates;
- remain positive under 2x synthetic cost;
- preserve its predeclared state/mechanism across folds.

Failure against either parent is retained as `REPACKAGING_REJECTED`. Conditional success confined to an insufficient cell is `UNKNOWN`, not survival.

## Examples, not pre-authorization

- liquidity state x reversal;
- volatility state x momentum;
- volume confirmation x breakout;
- range compression x trend.

The exact parents must be P0-8C representatives. These examples do not authorize all four or any neighboring formulation.
