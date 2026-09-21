# ADR-0021: PITPRICE01 stops before exposure replay

- Status: Accepted result disposition
- Controller directive: `ALPHA-PITPRICE01-ASOF-PRICE-BASIS-REPAIR-V1`
- Alpha Factory work commit: `e622bae101329a4b4f365d3354ff11e115ccc046`
- Formal report: `reports/PITPRICE01_ASOF_PRICE_BASIS_REPAIR_V1.md`
- Checkpoint: `state/checkpoints/PITPRICE01_ASOF_PRICE_BASIS_REPAIR_V1.json`
- Independent review: `research/pitprice01/REVIEW.md`
- Stop validator: `research/pitprice01/VALIDATOR.json`, `PASS_STOP_GATE`

PITPRICE01 audited the EXPOSURE01 V1 capital provenance first. The project charter at bootstrap commit `89b19ef` specified RMB 50,000 as the initial capital model. RMB 1,000,000 entered P0-7C's synthetic research-cost convention at `95dc8e3` and was explicitly set in the EXPOSURE01 V1 config/protocol at `58bf0e5`. The V1 manifest bound that config by hash but did not expose capital or primary/diagnostic scenario roles. Primary root cause: `STATE_PROPAGATION_FAILURE`; missing machine-readable capital enforcement and ADR-0019's capital omission contributed. A new additive contract freezes RMB 50,000 primary and RMB 1,000,000 scaling diagnostic before any later repaired replay.

The active FREE_DAILY_V1 price path is BaoStock raw daily OHLC (`adjustflag=3`) plus locally derived backward dataset-end-normalized links from comparable `preclose`; it is not Tushare's provider `adj_factor` feed. A new price contract/API separates raw execution prices, as-of analytical prices and realized label returns. On a predicate-bounded 2019–2023 audit of 87,408 rows and 72 symbols, the old/new adjustment relation was symbol-constant mathematically. The implemented floating-point sign/rank path nevertheless changed four frozen base feature ranks, C1/C3, 58 target ranks, three target positive directions, Ridge F1 scores, and Top20 on five of 36 fixed exposure signal dates. The audit refit on the original basis exactly reproduced frozen MODEL01 scores. Therefore `UPSTREAM_MODEL_INVARIANT=NO` and the required disposition is `UPSTREAM_RESEARCH_REQUALIFICATION_REQUIRED`.

The FREE_DAILY_V1 action links are a BaoStock price-return proxy, not dated cash dividends, share bonuses/splits and rights entitlements. Exact cash/share account replay remains data-limited. No EXPOSURE01 V2 manifest, attempt or result was created; no policy was selected. Keep all V1 wealth and exposure numbers invalid for selection and leave CAD01/CAD02/MODEL01 frozen historical results unchanged. No 2024–2025 or 2026 market rows, broker orders or external LLM calls were used. PIPELINE01 worktree remained untouched.

A future upstream requalification and entitlement-data effort needs a separate exact controller directive, new namespace, budgets and hard evidence gates. This ADR does not authorize automatic CAD/MODEL reruns, EXPOSURE01 V2, future tests or trading.
