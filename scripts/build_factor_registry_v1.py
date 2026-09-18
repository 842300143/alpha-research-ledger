"""Build the deterministic P0-8 design registry and Markdown factor cards.

This script creates documentation only. It reads no market data and computes no
factor values, labels, rankings, or results.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "factor-zoo"
CARDS = OUT / "FACTOR_CARDS"

DEFAULT_TIMING = "AFTER_T_CLOSE; EARLIEST_T_PLUS_1_OPEN"
MARKET_TIMING = "AFTER_T_CLOSE_DERIVED_MARKET; EARLIEST_T_PLUS_1_OPEN"
GAP_TIMING = "THEORETICALLY_AT_T_OPEN; BATCH_CONTRACT_T_PLUS_1_OPEN"

PRICE_RISKS = [
    "PARTIAL_ACTION_FACTOR_COVERAGE_ACTION_AWARE_SUBSET_ONLY",
    "CURRENT_CAPTURE_NON_PIT_UNIVERSE",
    "T_PLUS_1_EXECUTION_ONLY",
]
ACTIVITY_RISKS = [
    "RAW_VOLUME_SPLIT_AND_PROVIDER_SEMANTICS",
    "PARTIAL_HISTORICAL_TRADABILITY_STATE",
    "CURRENT_CAPTURE_NON_PIT_UNIVERSE",
]
MARKET_RISKS = PRICE_RISKS + ["DERIVED_EQUAL_WEIGHT_MARKET_INHERITS_UNIVERSE_BIAS"]

factors: list[dict] = []


def add(
    factor_id: str,
    canonical_name: str,
    family: str,
    concept: str,
    formula: str,
    fields: list[str],
    lookback: str,
    hypothesis: str,
    *,
    parameter_group: str | None = None,
    variant_role: str = "SINGLE",
    direction: str = "HIGHER_EXPECTED_BETTER",
    turnover: str = "MEDIUM",
    sensitivity: str = "Daily-batch delay, next-open gap, and synthetic cost assumptions.",
    related: list[str] | None = None,
    risks: list[str] | None = None,
    readiness: str = "LIMITED",
    abstraction: str = "ATOMIC",
    provenance: list[str] | None = None,
    stage: str = "P0_8B",
    timing: str = DEFAULT_TIMING,
    literature: str = "Common daily-bar factor construct; common usage is not empirical validation here.",
    derived: list[str] | None = None,
) -> None:
    common_tests = [
        "P0_8A_SYNTHETIC_FORMULA_AND_LAG_FIXTURE",
        "P0_8A_FULL_WINDOW_MISSINGNESS_AND_TIMING_CHECK",
    ]
    if stage == "P0_8B":
        common_tests += [
            "P0_8B_PRIMARY_AND_FIXED_NORMALIZATION_IC_RANKIC",
            "P0_8B_FOLD_SIGN_STABILITY_AND_DECAY_5_20_60",
            "P0_8B_TOP20_TURNOVER_COST_2X_COST_AND_DRAWDOWN",
            "P0_8B_COVERAGE_MISSINGNESS_REGIME_AND_FDR",
            "P0_8C_CORRELATION_OVERLAP_CLUSTER_AND_RESIDUAL_INFORMATION",
        ]
    else:
        common_tests += [
            "P0_8D_PARENT_AND_PARENT_COMBINATION_RESIDUAL_TEST",
            "P0_8D_INCREMENTAL_COST_STABILITY_AND_REGIME_TEST",
        ]
    factors.append(
        {
            "factor_id": factor_id,
            "canonical_name": canonical_name,
            "family": family,
            "concept": concept,
            "parameterization_group": parameter_group or factor_id,
            "variant_role": variant_role,
            "formula_pseudocode": formula,
            "required_raw_fields": fields,
            "derived_inputs": derived or ["adjusted OHLC/returns and rolling statistics exactly as referenced"],
            "lookback_input_horizon": lookback,
            "signal_availability_timing": timing,
            "expected_direction": direction,
            "hypothesis": hypothesis,
            "literature_common_usage_note": literature,
            "expected_turnover": turnover,
            "potential_execution_sensitivity": sensitivity,
            "likely_related_redundant_factors": related or [],
            "pit_lookahead_risks": risks or PRICE_RISKS,
            "data_readiness_status": readiness,
            "abstraction": abstraction,
            "provenance": provenance or ["P0_8_CANONICAL_DAILY_BAR_TAXONOMY"],
            "planned_tests": common_tests,
            "lifecycle": "DISCOVERED",
            "definition_status": "DRAFT_DESIGN",
            "evaluation_stage": stage,
        }
    )


# Momentum (5)
for fid, name, h, role in [
    ("FZ1_MOM_001", "Adjusted total return 20", 20, "SHORT"),
    ("FZ1_MOM_002", "Adjusted total return 60", 60, "MEDIUM"),
    ("FZ1_MOM_003", "Adjusted total return 120", 120, "LONG"),
]:
    add(fid, name, "MOMENTUM", "TOTAL_RETURN_MOMENTUM", f"adj_close[t] / adj_close[t-{h}] - 1", ["close", "adj_factor"], f"{h} sessions", "Persistent underreaction may make past relative winners continue to outperform.", parameter_group="PG_MOM_TOTAL_RETURN", variant_role=role, related=["PG_REV_TOTAL_RETURN", "PG_TREND_PRICE_SMA"], turnover="HIGH" if h == 20 else "MEDIUM", provenance=["STANDARD_MOMENTUM", "P0_7C_MOMENTUM_LINEAGE"])
add("FZ1_MOM_004", "Skip-recent 120-to-20 momentum", "MOMENTUM", "SKIP_RECENT_MOMENTUM", "adj_close[t-20] / adj_close[t-120] - 1", ["close", "adj_factor"], "120 sessions with latest 20 excluded", "Longer underreaction may persist after removing the most recent month where reversal can dominate.", related=["PG_MOM_TOTAL_RETURN", "PG_REV_TOTAL_RETURN"], turnover="LOW")
add("FZ1_MOM_005", "Return acceleration 20 versus 60", "MOMENTUM", "MOMENTUM_ACCELERATION", "log1p(ret20)/20 - log1p(ret60)/60", ["close", "adj_factor"], "60 sessions", "A recent increase in the per-session return trend may identify strengthening information diffusion.", related=["PG_MOM_TOTAL_RETURN", "FZ1_TRD_003"], turnover="HIGH", abstraction="TRANSFORMED")

# Reversal (5)
for fid, name, h, role in [
    ("FZ1_REV_001", "Adjusted reversal 5", 5, "SHORT"),
    ("FZ1_REV_002", "Adjusted reversal 20", 20, "MEDIUM"),
]:
    add(fid, name, "REVERSAL", "TOTAL_RETURN_REVERSAL", f"-(adj_close[t] / adj_close[t-{h}] - 1)", ["close", "adj_factor"], f"{h} sessions", "Short-horizon price pressure or overreaction may partially reverse.", parameter_group="PG_REV_TOTAL_RETURN", variant_role=role, related=["PG_MOM_TOTAL_RETURN", "FZ1_REV_003"], turnover="VERY_HIGH" if h == 5 else "HIGH", provenance=["STANDARD_REVERSAL", "P0_7C_REVERSAL_LINEAGE"])
add("FZ1_REV_003", "Medium reversal excluding latest 5", "REVERSAL", "MEDIUM_REVERSAL_EX_RECENT", "-(adj_close[t-5] / adj_close[t-20] - 1)", ["close", "adj_factor"], "20 sessions; latest 5 excluded", "Inventory or behavioral correction in the preceding medium window may differ from very-short microstructure reversal.", related=["PG_REV_TOTAL_RETURN"], turnover="HIGH", provenance=["P07E_REV_MEDIUM_EX5_20"])
add("FZ1_REV_004", "Largest one-day gain reversal 20", "REVERSAL", "EXTREME_GAIN_REVERSAL", "-max(r1[t-19:t])", ["close", "adj_factor"], "20 sessions", "A single extreme positive move may contain transitory attention or price pressure that reverses.", related=["FZ1_DTR_005", "FZ1_DST_005"], turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_REV_005", "Three-day run-up reversal", "REVERSAL", "VERY_SHORT_RUNUP_EXHAUSTION", "-(adj_close[t] / adj_close[t-3] - 1)", ["close", "adj_factor"], "3 sessions", "Very short run-ups may exhaust temporary demand and mean-revert.", related=["FZ1_REV_001"], turnover="VERY_HIGH")

# Trend (6)
for fid, name, h, role in [
    ("FZ1_TRD_001", "Price above SMA 20", 20, "SHORT"),
    ("FZ1_TRD_002", "Price above SMA 60", 60, "MEDIUM"),
]:
    add(fid, name, "TREND", "PRICE_TO_MOVING_AVERAGE", f"adj_close[t] / mean(adj_close[t-{h-1}:t]) - 1", ["close", "adj_factor"], f"{h} sessions", "A price above its trailing equilibrium may indicate a persistent trend.", parameter_group="PG_TREND_PRICE_SMA", variant_role=role, related=["PG_MOM_TOTAL_RETURN", "FZ1_POS_005"], turnover="HIGH" if h == 20 else "MEDIUM", provenance=["STANDARD_TREND", "P0_7C_TREND_LINEAGE"])
add("FZ1_TRD_003", "Dual moving-average trend 20/60", "TREND", "DUAL_MOVING_AVERAGE", "mean(adj_close[t-19:t]) / mean(adj_close[t-59:t]) - 1", ["close", "adj_factor"], "60 sessions", "A short average above a medium average indicates persistent trend state rather than one endpoint return.", related=["PG_TREND_PRICE_SMA", "FZ1_MOM_005"], turnover="MEDIUM")
add("FZ1_TRD_004", "Log-price regression slope 60", "TREND", "REGRESSION_TREND_SLOPE", "OLS_slope(log(adj_close[t-59:t]) ~ 0..59) * 252", ["close", "adj_factor"], "60 sessions", "A distributed regression slope may measure trend with less endpoint sensitivity.", related=["FZ1_TRD_005", "FZ1_EFF_001"], turnover="MEDIUM", abstraction="TRANSFORMED")
add("FZ1_TRD_005", "Trend t-statistic 60", "TREND", "REGRESSION_TREND_SIGNIFICANCE", "OLS_slope_t_stat(log(adj_close[t-59:t]) ~ 0..59)", ["close", "adj_factor"], "60 sessions", "A statistically coherent trend may be more repeatable than a noisy slope of the same size.", related=["FZ1_TRD_004", "FZ1_EFF_002"], turnover="MEDIUM", abstraction="TRANSFORMED")
add("FZ1_TRD_006", "Positive-return day share 20", "TREND", "TREND_PERSISTENCE", "mean(1[r1>0] over t-19:t) - 0.5", ["close", "adj_factor"], "20 sessions", "Broad day-by-day participation may distinguish persistent trends from single jumps.", related=["FZ1_DST_003", "FZ1_EFF_005"], turnover="HIGH")

# Volatility (6)
for fid, name, h, role in [
    ("FZ1_VOL_001", "Negative realized volatility 20", 20, "SHORT"),
    ("FZ1_VOL_002", "Negative realized volatility 60", 60, "MEDIUM"),
]:
    add(fid, name, "VOLATILITY", "LOW_REALIZED_VOLATILITY", f"-std(r1[t-{h-1}:t]) * sqrt(252)", ["close", "adj_factor"], f"{h} sessions", "Lower realized volatility may proxy stable demand, constrained leverage, or the low-risk anomaly.", parameter_group="PG_VOL_REALIZED", variant_role=role, related=["PG_DTR_DOWNSIDE_VOL", "FZ1_MKT_005"], turnover="HIGH" if h == 20 else "MEDIUM", provenance=["STANDARD_LOW_VOLATILITY", "P0_7C_LOWVOL_LINEAGE"])
add("FZ1_VOL_003", "Negative EWMA volatility 20", "VOLATILITY", "LOW_EWMA_VOLATILITY", "-sqrt(252 * EWMA_lambda0.94(r1^2,20))", ["close", "adj_factor"], "20 sessions; lambda 0.94", "Recency-weighted low volatility may capture current risk state faster than an equal-weight estimator.", related=["PG_VOL_REALIZED", "FZ1_VR_001"], turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_VOL_004", "Negative volatility-of-volatility 60", "VOLATILITY", "VOLATILITY_STABILITY", "-std(rolling_std_10(r1)[t-59:t])", ["close", "adj_factor"], "69 sessions", "Stable volatility may be less exposed to latent event risk than an equally low but unstable volatility level.", related=["PG_VOL_REALIZED", "FZ1_RNG_004"], turnover="MEDIUM", abstraction="TRANSFORMED")
add("FZ1_VOL_005", "Negative idiosyncratic volatility 60", "VOLATILITY", "LOW_IDIOSYNCRATIC_VOLATILITY", "-std(residual_OLS(r1 ~ equal_weight_market_r1) over 60)", ["close", "adj_factor"], "60 sessions", "Lower market-adjusted residual risk may contain information distinct from total volatility.", related=["FZ1_MKT_005", "PG_VOL_REALIZED"], turnover="MEDIUM", risks=MARKET_RISKS, abstraction="TRANSFORMED", timing=MARKET_TIMING)
add("FZ1_VOL_006", "Negative intraday range volatility 20", "VOLATILITY", "LOW_INTRADAY_RANGE_VOLATILITY", "-mean(log(adj_high/adj_low)^2 over 20)", ["high", "low", "adj_factor"], "20 sessions", "Daily high-low range supplies a close-independent proxy for realized variability.", related=["FZ1_RNG_002", "PG_VOL_REALIZED"], turnover="HIGH")

# Downside / tail risk (5)
for fid, name, h, role in [
    ("FZ1_DTR_001", "Negative downside deviation 20", 20, "SHORT"),
    ("FZ1_DTR_002", "Negative downside deviation 60", 60, "MEDIUM"),
]:
    add(fid, name, "DOWNSIDE_TAIL_RISK", "LOW_DOWNSIDE_VOLATILITY", f"-std(min(r1,0) over t-{h-1}:t) * sqrt(252)", ["close", "adj_factor"], f"{h} sessions", "Lower downside variability may be rewarded separately from symmetric low volatility.", parameter_group="PG_DTR_DOWNSIDE_VOL", variant_role=role, related=["PG_VOL_REALIZED", "FZ1_DTR_003"], turnover="HIGH" if h == 20 else "MEDIUM", provenance=["STANDARD_DOWNSIDE_RISK", "P0_7C_DOWNSIDE_VOL_LINEAGE"])
add("FZ1_DTR_003", "Negative semivariance share 60", "DOWNSIDE_TAIL_RISK", "DOWNSIDE_SEMIVARIANCE_SHARE", "-sum(min(r1,0)^2)/sum(r1^2) over 60", ["close", "adj_factor"], "60 sessions", "A larger fraction of variance from losses may indicate asymmetric risk not visible in total volatility.", related=["PG_DTR_DOWNSIDE_VOL", "FZ1_DST_005"], turnover="MEDIUM", abstraction="TRANSFORMED")
add("FZ1_DTR_004", "Negative maximum drawdown 60", "DOWNSIDE_TAIL_RISK", "RECENT_DRAWDOWN_SEVERITY", "max_drawdown(adj_close[t-59:t])", ["close", "adj_factor"], "60 sessions", "Securities with shallower recent path drawdowns may carry lower distress or crash exposure.", related=["FZ1_POS_003", "FZ1_COND_004"], turnover="MEDIUM", abstraction="TRANSFORMED")
add("FZ1_DTR_005", "Expected shortfall quality proxy 120", "DOWNSIDE_TAIL_RISK", "TAIL_LOSS_SEVERITY", "mean(worst ceil(0.05*120) r1 values over 120)", ["close", "adj_factor"], "120 sessions", "Less severe realized left-tail losses produce a higher score and may identify a distinct defensive dimension.", related=["FZ1_DTR_003", "FZ1_DST_005"], turnover="LOW", abstraction="TRANSFORMED")

# Range / ATR / compression (6)
add("FZ1_RNG_001", "Negative normalized ATR 20", "RANGE_ATR_COMPRESSION", "LOW_TRUE_RANGE", "-mean(max(adj_high-adj_low,abs(adj_high-prev_adj_close),abs(adj_low-prev_adj_close))/prev_adj_close over 20)", ["high", "low", "close", "adj_factor"], "21 sessions", "Lower true range may capture stable price discovery beyond close-to-close volatility.", related=["FZ1_VOL_006", "FZ1_RNG_004"], turnover="HIGH")
add("FZ1_RNG_002", "Negative Parkinson range volatility 20", "RANGE_ATR_COMPRESSION", "LOW_PARKINSON_VOLATILITY", "-sqrt(252*mean(log(adj_high/adj_low)^2)/(4*log(2)))", ["high", "low", "adj_factor"], "20 sessions", "High-low information may estimate volatility more efficiently than closes when daily bars are reliable.", related=["FZ1_VOL_006", "PG_VOL_REALIZED"], turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_RNG_003", "Negative Garman-Klass volatility 20", "RANGE_ATR_COMPRESSION", "LOW_GARMAN_KLASS_VOLATILITY", "-sqrt(252*mean(0.5*log(H/L)^2-(2*log(2)-1)*log(C/O)^2))", ["open", "high", "low", "close", "adj_factor"], "20 sessions", "OHLC structure may separate intraday variance from close-to-close noise.", related=["FZ1_RNG_002", "FZ1_VOL_006"], turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_RNG_004", "Range compression 5 versus 60", "RANGE_ATR_COMPRESSION", "RANGE_COMPRESSION", "-(mean((adj_high-adj_low)/adj_close over 5) / mean(... over prior 60) - 1)", ["high", "low", "close", "adj_factor"], "65 sessions", "Unusually compressed recent range may precede information release or trend expansion.", related=["FZ1_RNG_006", "FZ1_COND_003"], turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_RNG_005", "Negative Bollinger bandwidth 20", "RANGE_ATR_COMPRESSION", "PRICE_BAND_COMPRESSION", "-4*std(adj_close,20)/mean(adj_close,20)", ["close", "adj_factor"], "20 sessions", "Narrow normalized price bands indicate compression distinct from raw return volatility scale.", related=["FZ1_RNG_004", "FZ1_VOL_001"], turnover="HIGH")
add("FZ1_RNG_006", "Range expansion 5 versus 20", "RANGE_ATR_COMPRESSION", "RANGE_EXPANSION", "mean((adj_high-adj_low)/adj_close over 5) / mean(... over 20) - 1", ["high", "low", "close", "adj_factor"], "20 sessions", "Recent range expansion may identify active price discovery and short-lived continuation.", related=["FZ1_RNG_004", "FZ1_PVR_006"], turnover="VERY_HIGH", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC")

# Liquidity (6)
for fid, name, h, role in [
    ("FZ1_LIQ_001", "Negative Amihud illiquidity 20", 20, "SHORT"),
    ("FZ1_LIQ_002", "Negative Amihud illiquidity 60", 60, "MEDIUM"),
]:
    add(fid, name, "LIQUIDITY", "LOW_RETURN_PER_AMOUNT_ILLIQUIDITY", f"-mean(abs(r1)/(amount+1e-12) over {h})", ["close", "amount", "adj_factor"], f"{h} sessions", "Lower price impact per traded amount may indicate more resilient liquidity, although the premium sign is an empirical question.", parameter_group="PG_LIQ_AMIHUD", variant_role=role, related=["FZ1_LIQ_006", "FZ1_TOV_001"], risks=PRICE_RISKS+ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH" if h == 20 else "MEDIUM", provenance=["STANDARD_AMIHUD", "P0_7C_ILLIQUIDITY_LINEAGE"])
add("FZ1_LIQ_003", "Log average amount 20", "LIQUIDITY", "TRADING_AMOUNT_LEVEL", "log1p(mean(amount[t-19:t]))", ["amount"], "20 sessions", "Higher traded amount may proxy ease of execution and persistent investor attention.", related=["FZ1_VOLM_001", "FZ1_TOV_001"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="MEDIUM", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", derived=["rolling amount statistics"])
add("FZ1_LIQ_004", "Negative zero-activity frequency 20", "LIQUIDITY", "TRADING_CONTINUITY", "-mean(1[volume<=0 or amount<=0] over 20)", ["volume", "amount"], "20 sessions", "Continuous activity may indicate better implementability and lower latent trading friction.", related=["FZ1_LIQ_003"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="LOW", derived=["rolling activity-state indicators"])
add("FZ1_LIQ_005", "Negative amount coefficient of variation 20", "LIQUIDITY", "LIQUIDITY_STABILITY", "-std(amount,20)/(mean(amount,20)+1e-12)", ["amount"], "20 sessions", "Stable trading amount may signal persistent liquidity rather than event-driven bursts.", related=["FZ1_TOV_005", "FZ1_VOLM_004"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH", abstraction="TRANSFORMED", derived=["rolling amount mean and standard deviation"])
add("FZ1_LIQ_006", "Negative return per turnover 20", "LIQUIDITY", "TURNOVER_SCALED_PRICE_IMPACT", "-mean(abs(r1)/(turnover+1e-12) over 20)", ["close", "turnover", "adj_factor"], "20 sessions", "Lower return movement per turnover may proxy deeper liquidity when amount scale is heterogeneous.", related=["PG_LIQ_AMIHUD", "FZ1_TOV_001"], risks=PRICE_RISKS+ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH", abstraction="TRANSFORMED")

# Turnover dynamics (5)
add("FZ1_TOV_001", "Negative mean turnover 20", "TURNOVER_DYNAMICS", "LOW_TURNOVER_LEVEL", "-mean(turnover[t-19:t])", ["turnover"], "20 sessions", "Low turnover may proxy neglected securities or a liquidity/attention premium.", related=["FZ1_LIQ_003", "FZ1_TOV_002"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="MEDIUM", provenance=["P0_7C_LOW_TURNOVER_LINEAGE"], derived=["rolling turnover mean"])
add("FZ1_TOV_002", "Negative turnover persistence deviation 20/60", "TURNOVER_DYNAMICS", "TURNOVER_PERSISTENCE", "-abs(mean(turnover,20)/mean(turnover,60)-1)", ["turnover"], "60 sessions", "Turnover near its medium baseline may indicate stable participation, while large deviations may be transient.", related=["FZ1_TOV_001", "FZ1_TOV_003"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH", abstraction="TRANSFORMED", provenance=["P07C_LIQ_TURN_PERSIST60"])
add("FZ1_TOV_003", "Signed abnormal turnover contraction 5/prior60", "TURNOVER_DYNAMICS", "SIGNED_TURNOVER_INNOVATION", "-log((mean(turnover,t-4:t)+1e-12)/(mean(turnover,t-64:t-5)+1e-12))", ["turnover"], "65 sessions", "Recent attention contraction may be favorable if abnormal activity contains transitory demand.", related=["FZ1_TOV_002", "FZ1_VOLM_003"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH", abstraction="TRANSFORMED", provenance=["P07E_LIQ_SIGNED_ABTURN_5V60"])
add("FZ1_TOV_004", "Negative turnover trend slope 20", "TURNOVER_DYNAMICS", "TURNOVER_TREND", "-OLS_slope(log1p(turnover[t-19:t]) ~ 0..19)", ["turnover"], "20 sessions", "Declining attention may identify neglected names, while rising attention may reflect crowded transitory demand.", related=["FZ1_TOV_003", "FZ1_VOLM_003"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_TOV_005", "Negative turnover variability 20", "TURNOVER_DYNAMICS", "TURNOVER_STABILITY", "-std(turnover,20)/(mean(turnover,20)+1e-12)", ["turnover"], "20 sessions", "Stable turnover may identify durable liquidity/attention rather than event bursts.", related=["FZ1_LIQ_005", "FZ1_VOLM_004"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH", abstraction="TRANSFORMED")

# Raw / relative volume (5)
add("FZ1_VOLM_001", "Log average raw volume 20", "RAW_RELATIVE_VOLUME", "RAW_VOLUME_LEVEL", "log1p(mean(volume[t-19:t]))", ["volume"], "20 sessions", "Persistent volume level may proxy attention and tradability, subject to security scale and split limitations.", related=["FZ1_LIQ_003"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="MEDIUM", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", derived=["rolling volume mean"])
add("FZ1_VOLM_002", "Relative volume current/20", "RAW_RELATIVE_VOLUME", "CURRENT_RELATIVE_VOLUME", "log((volume[t]+1)/(mean(volume[t-19:t])+1))", ["volume"], "20 sessions", "Unusually high current participation may confirm information or indicate short-lived attention.", related=["FZ1_PVR_004", "FZ1_TOV_003"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="VERY_HIGH", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", derived=["rolling volume mean"])
add("FZ1_VOLM_003", "Volume trend 5/prior60", "RAW_RELATIVE_VOLUME", "VOLUME_TREND", "log((mean(volume,t-4:t)+1)/(mean(volume,t-64:t-5)+1))", ["volume"], "65 sessions", "A sustained change in raw activity may indicate changing information arrival.", related=["FZ1_TOV_003", "FZ1_VOLM_002"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", derived=["rolling volume means"])
add("FZ1_VOLM_004", "Negative volume variability 20", "RAW_RELATIVE_VOLUME", "VOLUME_STABILITY", "-std(volume,20)/(mean(volume,20)+1e-12)", ["volume"], "20 sessions", "Stable activity may be more implementable and less event-driven than volatile volume.", related=["FZ1_LIQ_005", "FZ1_TOV_005"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="HIGH", abstraction="TRANSFORMED", derived=["rolling volume mean and standard deviation"])
add("FZ1_VOLM_005", "Volume autocorrelation 60", "RAW_RELATIVE_VOLUME", "VOLUME_PERSISTENCE", "corr(log1p(volume[s]),log1p(volume[s-1])) over s=t-58:t", ["volume"], "60 sessions", "Persistent activity may distinguish stable investor participation from isolated bursts.", related=["FZ1_TOV_002", "FZ1_VOLM_004"], risks=ACTIVITY_RISKS, readiness="READY_WITH_WARNINGS", turnover="LOW", abstraction="TRANSFORMED", derived=["lagged log-volume series"])

# Price-volume relation (6)
add("FZ1_PVR_001", "Return-volume correlation 20", "PRICE_VOLUME_RELATION", "PRICE_VOLUME_CORRELATION", "corr(r1,delta(log1p(volume))) over 20", ["close", "volume", "adj_factor"], "21 sessions", "Positive co-movement between returns and activity may indicate confirmation; negative co-movement may indicate distribution.", parameter_group="PG_PVR_CORRELATION", variant_role="SHORT", related=["FZ1_PVR_002", "FZ1_VOLM_002"], risks=PRICE_RISKS+ACTIVITY_RISKS, direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", abstraction="TRANSFORMED")
add("FZ1_PVR_002", "Return-volume correlation 60", "PRICE_VOLUME_RELATION", "PRICE_VOLUME_CORRELATION", "corr(r1,delta(log1p(volume))) over 60", ["close", "volume", "adj_factor"], "61 sessions", "Medium-horizon price-volume co-movement may reveal durable accumulation or distribution.", parameter_group="PG_PVR_CORRELATION", variant_role="MEDIUM", related=["FZ1_PVR_001"], risks=PRICE_RISKS+ACTIVITY_RISKS, turnover="LOW", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", abstraction="TRANSFORMED")
add("FZ1_PVR_003", "On-balance-volume slope 20", "PRICE_VOLUME_RELATION", "ON_BALANCE_VOLUME_TREND", "OLS_slope(cumsum(sign(r1)*volume) over 20)", ["close", "volume", "adj_factor"], "20 sessions", "Volume signed by price direction may identify accumulation not visible in return alone.", related=["FZ1_PVR_004", "FZ1_TRD_004"], risks=PRICE_RISKS+ACTIVITY_RISKS, turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_PVR_004", "Volume-confirmed momentum 20", "PRICE_VOLUME_RELATION", "VOLUME_CONFIRMED_MOMENTUM", "rank_cs(ret20) * rank_cs(log((volume[t]+1)/(mean(volume,20)+1)))", ["close", "volume", "adj_factor"], "20 sessions", "Momentum accompanied by abnormal activity may reflect stronger information diffusion than price movement alone.", related=["FZ1_MOM_001", "FZ1_VOLM_002"], risks=PRICE_RISKS+ACTIVITY_RISKS, turnover="VERY_HIGH", abstraction="TRANSFORMED", provenance=["P0_7C_PRICE_VOLUME_LINEAGE"])
add("FZ1_PVR_005", "Price-volume divergence 20", "PRICE_VOLUME_RELATION", "PRICE_VOLUME_DIVERGENCE", "rank_cs(ret20) - rank_cs(volume_5_to_20_change)", ["close", "volume", "adj_factor"], "20 sessions", "A price move unsupported by activity may be fragile and more likely to reverse.", related=["FZ1_PVR_004", "FZ1_REV_002"], risks=PRICE_RISKS+ACTIVITY_RISKS, turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_PVR_006", "Chaikin money-flow proxy 20", "PRICE_VOLUME_RELATION", "MONEY_FLOW_LOCATION_VOLUME", "sum(((2*C-H-L)/(H-L))*volume,20)/(sum(volume,20)+1e-12)", ["high", "low", "close", "volume", "adj_factor"], "20 sessions", "Closing location weighted by volume may distinguish accumulation from distribution inside daily ranges.", related=["FZ1_BAR_001", "FZ1_PVR_003"], risks=PRICE_RISKS+ACTIVITY_RISKS, turnover="HIGH", abstraction="TRANSFORMED")

# Gap / open-close (5)
add("FZ1_GAP_001", "Negative overnight gap 1", "GAP_OPEN_CLOSE", "OVERNIGHT_GAP_REVERSAL", "-(adj_open[t]/adj_close[t-1]-1)", ["open", "close", "adj_factor"], "2 sessions", "Overnight price pressure may partially reverse after the open.", related=["FZ1_GAP_003", "FZ1_REV_001"], turnover="VERY_HIGH", timing=GAP_TIMING, sensitivity="Opening auction gap and t+1 batch delay; cannot trade the observed t open in V1.")
add("FZ1_GAP_002", "Negative mean overnight gap 5", "GAP_OPEN_CLOSE", "OVERNIGHT_GAP_LEVEL", "-mean(adj_open[s]/adj_close[s-1]-1 over last 5)", ["open", "close", "adj_factor"], "6 sessions", "Repeated overnight gaps may represent persistent pressure whose sign differs from intraday information.", related=["FZ1_GAP_001", "FZ1_GAP_004"], turnover="VERY_HIGH", timing=GAP_TIMING)
add("FZ1_GAP_003", "Gap reversal after large gap 5", "GAP_OPEN_CLOSE", "GAP_SHOCK_REVERSAL", "-gap[t] * abs_zscore_time(gap[t], prior20)", ["open", "close", "adj_factor"], "21 sessions", "Unusually large overnight shocks may overreact and reverse more strongly than ordinary gaps.", related=["FZ1_GAP_001", "FZ1_REV_004"], turnover="VERY_HIGH", timing=GAP_TIMING, abstraction="TRANSFORMED")
add("FZ1_GAP_004", "Overnight gap momentum 20", "GAP_OPEN_CLOSE", "OVERNIGHT_INFORMATION_MOMENTUM", "sum(log(adj_open[s]/adj_close[s-1]) over 20)", ["open", "close", "adj_factor"], "21 sessions", "Persistent overnight returns may reflect information incorporated outside the trading session.", related=["FZ1_GAP_002", "FZ1_MOM_001"], turnover="HIGH", timing=GAP_TIMING)
add("FZ1_GAP_005", "Overnight minus intraday return 20", "GAP_OPEN_CLOSE", "OVERNIGHT_INTRADAY_DECOMPOSITION", "sum(overnight_log_return,20)-sum(log(adj_close/adj_open),20)", ["open", "close", "adj_factor"], "21 sessions", "The balance of overnight and intraday returns may distinguish information from trading-session pressure.", related=["FZ1_GAP_004", "FZ1_BAR_002"], turnover="HIGH", abstraction="TRANSFORMED")

# Intraday daily-bar structure (5)
add("FZ1_BAR_001", "Close location value", "INTRADAY_DAILY_BAR", "CLOSE_LOCATION", "(2*adj_close-adj_high-adj_low)/(adj_high-adj_low)", ["high", "low", "close", "adj_factor"], "1 session", "Closing near the daily high may indicate persistent demand within the session.", related=["FZ1_PVR_006", "FZ1_POS_001"], turnover="VERY_HIGH")
add("FZ1_BAR_002", "Intraday open-close return", "INTRADAY_DAILY_BAR", "INTRADAY_RETURN", "adj_close/adj_open-1", ["open", "close", "adj_factor"], "1 session", "Within-session price movement may carry information distinct from overnight gaps.", related=["FZ1_GAP_005", "FZ1_BAR_001"], turnover="VERY_HIGH")
add("FZ1_BAR_003", "Body-to-range conviction 20", "INTRADAY_DAILY_BAR", "CANDLE_BODY_CONVICTION", "mean((adj_close-adj_open)/(adj_high-adj_low) over 20)", ["open", "high", "low", "close", "adj_factor"], "20 sessions", "Consistent signed candle bodies may indicate directional conviction rather than noisy ranges.", related=["FZ1_BAR_001", "FZ1_TRD_006"], turnover="HIGH")
add("FZ1_BAR_004", "Negative upper-shadow share 20", "INTRADAY_DAILY_BAR", "UPPER_REJECTION", "-mean((adj_high-max(adj_open,adj_close))/(adj_high-adj_low) over 20)", ["open", "high", "low", "close", "adj_factor"], "20 sessions", "Frequent upper rejection may signal supply and weaker subsequent relative performance.", related=["FZ1_BAR_005", "FZ1_POS_004"], turnover="HIGH")
add("FZ1_BAR_005", "Lower-shadow support share 20", "INTRADAY_DAILY_BAR", "LOWER_SUPPORT", "mean((min(adj_open,adj_close)-adj_low)/(adj_high-adj_low) over 20)", ["open", "high", "low", "close", "adj_factor"], "20 sessions", "Frequent recovery from intraday lows may indicate support and resilient demand.", related=["FZ1_BAR_004", "FZ1_POS_004"], turnover="HIGH")

# Price position (5)
for fid, name, h, role in [
    ("FZ1_POS_001", "N-day range position 20", 20, "SHORT"),
    ("FZ1_POS_002", "N-day range position 60", 60, "MEDIUM"),
]:
    add(fid, name, "PRICE_RANGE_POSITION", "CLOSE_IN_N_DAY_RANGE", f"(adj_close[t]-min(adj_low,{h}))/(max(adj_high,{h})-min(adj_low,{h}))", ["high", "low", "close", "adj_factor"], f"{h} sessions", "A close near the top of its recent range may indicate trend persistence; near-bottom position may indicate weakness or reversal.", parameter_group="PG_POS_RANGE", variant_role=role, related=["PG_BRK_HIGH_DISTANCE", "PG_TREND_PRICE_SMA"], turnover="HIGH" if h == 20 else "MEDIUM", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC")
add("FZ1_POS_003", "Percentile price position 252", "PRICE_RANGE_POSITION", "LONG_HORIZON_PRICE_POSITION", "percentile_rank(adj_close[t] within adj_close[t-251:t])", ["close", "adj_factor"], "252 sessions", "Long-horizon location may separate persistent leaders from distressed laggards.", related=["FZ1_DTR_004", "FZ1_BRK_005"], turnover="LOW", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC")
add("FZ1_POS_004", "Symmetric distance to 20-day extremes", "PRICE_RANGE_POSITION", "EXTREME_PROXIMITY_BALANCE", "(distance_from_low20-distance_from_high20)/(range20+1e-12)", ["high", "low", "close", "adj_factor"], "20 sessions", "Relative proximity to the high versus low summarizes local directional pressure.", related=["FZ1_BAR_004", "FZ1_BAR_005", "PG_BRK_HIGH_DISTANCE"], turnover="HIGH")
add("FZ1_POS_005", "Price versus rolling VWAP proxy 20", "PRICE_RANGE_POSITION", "PRICE_TO_VWAP_PROXY", "adj_close[t]/(sum(amount,20)/sum(volume,20) adjusted to validated units)-1", ["close", "amount", "volume", "adj_factor"], "20 sessions", "Price above the volume-weighted transaction proxy may indicate profitable holder positioning or trend.", related=["PG_TREND_PRICE_SMA", "FZ1_PVR_003"], risks=PRICE_RISKS+ACTIVITY_RISKS+["VWAP_PROXY_REQUIRES_UNIT_VALIDATION"], turnover="HIGH", readiness="LIMITED", abstraction="TRANSFORMED")

# High/low breakout (5)
for fid, name, h, role in [
    ("FZ1_BRK_001", "Distance to prior high 20", 20, "SHORT"),
    ("FZ1_BRK_002", "Distance to prior high 60", 60, "MEDIUM"),
]:
    add(fid, name, "HIGH_LOW_BREAKOUT", "DISTANCE_TO_PRIOR_HIGH", f"adj_close[t]/max(adj_high[t-{h}:t-1])-1", ["high", "close", "adj_factor"], f"{h+1} sessions", "Proximity to or penetration of a prior high may indicate breakout continuation.", parameter_group="PG_BRK_HIGH_DISTANCE", variant_role=role, related=["PG_POS_RANGE", "FZ1_BRK_004"], turnover="HIGH" if h == 20 else "MEDIUM")
add("FZ1_BRK_003", "Distance above prior low 20", "HIGH_LOW_BREAKOUT", "DISTANCE_FROM_PRIOR_LOW", "adj_close[t]/min(adj_low[t-20:t-1])-1", ["low", "close", "adj_factor"], "21 sessions", "Distance from a recent low distinguishes recovery strength from proximity to breakdown.", related=["FZ1_POS_004", "FZ1_DTR_004"], turnover="HIGH", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC")
add("FZ1_BRK_004", "Prior-high breakout indicator 60", "HIGH_LOW_BREAKOUT", "BREAKOUT_EVENT", "1[adj_close[t] > max(adj_high[t-60:t-1])]", ["high", "close", "adj_factor"], "61 sessions", "A clean break above a medium-term high may reveal new information or demand.", related=["FZ1_BRK_002", "FZ1_COND_003"], turnover="VERY_HIGH")
add("FZ1_BRK_005", "New-high frequency 60", "HIGH_LOW_BREAKOUT", "BREAKOUT_PERSISTENCE", "mean(1[adj_close[s]>=rolling_prior_high20[s]] over 60)", ["high", "close", "adj_factor"], "80 sessions", "Repeated new highs may identify persistent leadership rather than a single breakout.", related=["FZ1_BRK_004", "FZ1_POS_003"], turnover="MEDIUM", abstraction="TRANSFORMED")

# Distribution shape (5)
add("FZ1_DST_001", "Negative return skewness 60", "DISTRIBUTION_SHAPE", "RETURN_SKEWNESS", "-skew(r1[t-59:t])", ["close", "adj_factor"], "60 sessions", "Return asymmetry may proxy lottery demand or crash exposure; lower positive skew is expected to be less overpriced.", related=["FZ1_DST_005", "FZ1_DTR_005"], turnover="MEDIUM", abstraction="TRANSFORMED")
add("FZ1_DST_002", "Negative excess kurtosis 60", "DISTRIBUTION_SHAPE", "LOW_TAIL_THICKNESS", "-excess_kurtosis(r1[t-59:t])", ["close", "adj_factor"], "60 sessions", "Lower realized tail thickness may identify more stable return distributions.", related=["FZ1_DTR_005", "FZ1_VOL_004"], turnover="MEDIUM", abstraction="TRANSFORMED")
add("FZ1_DST_003", "Up-minus-down day balance 20", "DISTRIBUTION_SHAPE", "RETURN_SIGN_BALANCE", "mean(1[r1>0]-1[r1<0] over 20)", ["close", "adj_factor"], "20 sessions", "A broad excess of positive days may indicate persistent demand beyond total return magnitude.", related=["FZ1_TRD_006", "FZ1_EFF_005"], turnover="HIGH")
add("FZ1_DST_004", "Negative median absolute return deviation 20", "DISTRIBUTION_SHAPE", "ROBUST_RETURN_DISPERSION", "-median(abs(r1-median(r1)) over 20)", ["close", "adj_factor"], "20 sessions", "Low robust dispersion may capture stable risk while reducing sensitivity to single jumps.", related=["FZ1_VOL_001", "FZ1_DST_002"], turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_DST_005", "Negative-tail versus positive-tail balance 60", "DISTRIBUTION_SHAPE", "TAIL_ASYMMETRY", "mean(top10pct(r1))-abs(mean(bottom10pct(r1)))", ["close", "adj_factor"], "60 sessions", "More favorable realized right-tail than left-tail behavior may distinguish upside optionality from crash exposure.", related=["FZ1_DST_001", "FZ1_DTR_005"], turnover="MEDIUM", abstraction="TRANSFORMED")

# Market/beta/residual (6)
for fid, name, h, role in [
    ("FZ1_MKT_001", "Negative market beta 60", 60, "MEDIUM"),
    ("FZ1_MKT_002", "Negative market beta 252", 252, "LONG"),
]:
    add(fid, name, "MARKET_BETA_RESIDUAL", "LOW_EQUAL_WEIGHT_MARKET_BETA", f"-cov(r1,market_r1,{h})/(var(market_r1,{h})+1e-12)", ["close", "adj_factor"], f"{h} sessions", "Lower beta to the eligible equal-weight market may capture a defensive dimension.", parameter_group="PG_MKT_BETA", variant_role=role, related=["FZ1_MKT_006", "PG_VOL_REALIZED"], risks=MARKET_RISKS, turnover="MEDIUM" if h == 60 else "LOW", timing=MARKET_TIMING, abstraction="TRANSFORMED")
add("FZ1_MKT_003", "Residual momentum 60", "MARKET_BETA_RESIDUAL", "MARKET_ADJUSTED_MOMENTUM", "sum(OLS_residual(r1~market_r1) over 60)", ["close", "adj_factor"], "60 sessions", "Market-adjusted persistent return may be more stock-specific than raw momentum.", related=["FZ1_MOM_002", "FZ1_MKT_004"], risks=MARKET_RISKS, turnover="MEDIUM", timing=MARKET_TIMING, abstraction="TRANSFORMED")
add("FZ1_MKT_004", "Residual reversal 20", "MARKET_BETA_RESIDUAL", "MARKET_ADJUSTED_REVERSAL", "-sum(OLS_residual(r1~market_r1) over 20)", ["close", "adj_factor"], "20 sessions", "Stock-specific price pressure may reverse after removing common market movement.", related=["FZ1_REV_002", "FZ1_MKT_003"], risks=MARKET_RISKS, turnover="HIGH", timing=MARKET_TIMING, abstraction="TRANSFORMED")
add("FZ1_MKT_005", "Negative idiosyncratic volatility 60 residual", "MARKET_BETA_RESIDUAL", "LOW_RESIDUAL_RISK", "-std(OLS_residual(r1~market_r1) over 60)", ["close", "adj_factor"], "60 sessions", "Low stock-specific risk may be distinct from raw low volatility.", related=["FZ1_VOL_005", "FZ1_MKT_001"], risks=MARKET_RISKS, turnover="MEDIUM", timing=MARKET_TIMING, abstraction="TRANSFORMED")
add("FZ1_MKT_006", "Negative downside beta 120", "MARKET_BETA_RESIDUAL", "LOW_DOWNSIDE_BETA", "-cov(r1,market_r1 | market_r1<0,120)/(var(market_r1 | market_r1<0)+1e-12)", ["close", "adj_factor"], "120 sessions", "Lower sensitivity in negative market sessions may identify defensive asymmetry not captured by full beta.", related=["PG_MKT_BETA", "PG_DTR_DOWNSIDE_VOL"], risks=MARKET_RISKS, turnover="LOW", timing=MARKET_TIMING, abstraction="TRANSFORMED")

# Rolling correlation (4)
for fid, name, h, role in [
    ("FZ1_COR_001", "Negative market return correlation 20", 20, "SHORT"),
    ("FZ1_COR_002", "Negative market return correlation 60", 60, "MEDIUM"),
    ("FZ1_COR_003", "Negative market return correlation 120", 120, "LONG"),
]:
    add(fid, name, "ROLLING_CORRELATION", "LOW_MARKET_CORRELATION", f"-corr(r1, equal_weight_market_r1 over {h})", ["close", "adj_factor"], f"{h} sessions", "Lower correlation to the eligible market may supply diversification and distinct information.", parameter_group="PG_COR_MARKET", variant_role=role, related=["PG_MKT_BETA", "FZ1_MKT_005"], risks=MARKET_RISKS, turnover="HIGH" if h == 20 else "MEDIUM" if h == 60 else "LOW", timing=MARKET_TIMING, abstraction="TRANSFORMED")
add("FZ1_COR_004", "Return versus market-breadth-change correlation 60", "ROLLING_CORRELATION", "BREADTH_SENSITIVITY", "corr(r1, delta(equal_weight_positive_return_share) over 60)", ["close", "adj_factor"], "61 sessions", "Sensitivity to changes in market breadth may distinguish broad-beta exposure from idiosyncratic behavior.", related=["PG_COR_MARKET", "FZ1_MKT_001"], risks=MARKET_RISKS, turnover="MEDIUM", timing=MARKET_TIMING, direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", abstraction="TRANSFORMED")

# Efficiency / trend-to-noise (5)
for fid, name, h, role in [
    ("FZ1_EFF_001", "Kaufman efficiency ratio 20", 20, "SHORT"),
    ("FZ1_EFF_002", "Kaufman efficiency ratio 60", 60, "MEDIUM"),
]:
    add(fid, name, "PRICE_EFFICIENCY_TREND_NOISE", "DIRECTIONAL_EFFICIENCY", f"abs(adj_close[t]-adj_close[t-{h}])/sum(abs(delta(adj_close)) over {h})", ["close", "adj_factor"], f"{h} sessions", "A price path with less back-and-forth noise may represent more efficient information diffusion.", parameter_group="PG_EFF_KAUFMAN", variant_role=role, related=["FZ1_TRD_004", "FZ1_EFF_003"], turnover="HIGH" if h == 20 else "MEDIUM", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", abstraction="TRANSFORMED")
add("FZ1_EFF_003", "Signed path efficiency 20", "PRICE_EFFICIENCY_TREND_NOISE", "SIGNED_DIRECTIONAL_EFFICIENCY", "(adj_close[t]-adj_close[t-20])/sum(abs(delta(adj_close)) over 20)", ["close", "adj_factor"], "20 sessions", "Signed efficient movement combines trend direction with path smoothness.", related=["FZ1_EFF_001", "FZ1_MOM_001"], turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_EFF_004", "Variance ratio 20/5", "PRICE_EFFICIENCY_TREND_NOISE", "RETURN_VARIANCE_RATIO", "var(r5 over 20)/(5*var(r1 over 20)+1e-12)", ["close", "adj_factor"], "25 sessions", "Variance aggregation above or below a random-walk benchmark may reveal continuation or mean reversion.", related=["FZ1_EFF_005", "FZ1_REV_001"], turnover="HIGH", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", abstraction="TRANSFORMED")
add("FZ1_EFF_005", "Return-sign autocorrelation 20", "PRICE_EFFICIENCY_TREND_NOISE", "RETURN_SIGN_PERSISTENCE", "corr(sign(r1[s]),sign(r1[s-1])) over 20", ["close", "adj_factor"], "21 sessions", "Positive sign persistence indicates continuation while negative persistence indicates reversal microstructure.", related=["FZ1_DST_003", "FZ1_EFF_004"], turnover="HIGH", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", abstraction="TRANSFORMED")

# Volatility-return relation (4)
add("FZ1_VR_001", "Negative volatility momentum 5/60", "VOLATILITY_RETURN_RELATION", "VOLATILITY_STATE_CHANGE", "-(std(r1,5)/(std(r1,60)+1e-12)-1)", ["close", "adj_factor"], "60 sessions", "A recent volatility contraction may indicate stabilization; expansion may signal unresolved information.", related=["FZ1_VOL_003", "FZ1_RNG_004"], turnover="VERY_HIGH", abstraction="TRANSFORMED")
add("FZ1_VR_002", "Risk-adjusted return 20", "VOLATILITY_RETURN_RELATION", "RETURN_TO_RISK", "ret20/(std(r1,20)*sqrt(20)+1e-12)", ["close", "adj_factor"], "20 sessions", "Return achieved with less realized risk may be more persistent than raw momentum.", related=["FZ1_MOM_001", "FZ1_TRD_005"], turnover="HIGH", abstraction="TRANSFORMED")
add("FZ1_VR_003", "Upside-minus-downside volatility balance 60", "VOLATILITY_RETURN_RELATION", "VOLATILITY_ASYMMETRY", "std(max(r1,0),60)-std(min(r1,0),60)", ["close", "adj_factor"], "60 sessions", "More upside than downside variation may indicate favorable asymmetric information.", related=["PG_DTR_DOWNSIDE_VOL", "FZ1_DST_005"], turnover="MEDIUM", abstraction="TRANSFORMED")
add("FZ1_VR_004", "Return-absolute-return correlation 60", "VOLATILITY_RETURN_RELATION", "RETURN_VOLATILITY_FEEDBACK", "corr(r1,abs(r1)) over 60", ["close", "adj_factor"], "60 sessions", "The sign of return-volatility feedback distinguishes upside excitement from downside risk concentration.", related=["FZ1_DST_001", "FZ1_VR_003"], turnover="MEDIUM", direction="HIGHER_EXPECTED_BETTER_DIAGNOSTIC", abstraction="TRANSFORMED")

# Conditional prototypes (4) -- definitions are design-only until P0-8D.
add("FZ1_COND_001", "Reversal conditional on high-liquidity state", "CONDITIONAL_REGIME", "LIQUIDITY_STATE_X_REVERSAL", "rank_cs(-ret20) active only when archetype_liquidity_state is HIGH", ["close", "amount", "volume", "turnover", "adj_factor"], "parent lookbacks plus training-fitted state", "Reversal may be more executable and less distress-driven in high-liquidity states.", related=["PG_REV_TOTAL_RETURN", "LIQUIDITY_ARCHETYPE_TBD"], risks=PRICE_RISKS+ACTIVITY_RISKS, readiness="DEFERRED_TO_P0_8D", abstraction="CONDITIONAL", stage="P0_8D", timing="P0_8D_ONLY_AFTER_STATE_FREEZE", turnover="HIGH", provenance=["P0_8_CONDITIONAL_PROTOTYPE"])
add("FZ1_COND_002", "Momentum conditional on low-volatility state", "CONDITIONAL_REGIME", "VOLATILITY_STATE_X_MOMENTUM", "rank_cs(ret60) active only when archetype_volatility_state is LOW", ["close", "adj_factor"], "parent lookbacks plus training-fitted state", "Momentum may persist more reliably when stock-specific or market volatility is subdued.", related=["PG_MOM_TOTAL_RETURN", "VOLATILITY_ARCHETYPE_TBD"], risks=MARKET_RISKS, readiness="DEFERRED_TO_P0_8D", abstraction="CONDITIONAL", stage="P0_8D", timing="P0_8D_ONLY_AFTER_STATE_FREEZE", turnover="MEDIUM", provenance=["P0_8_CONDITIONAL_PROTOTYPE"])
add("FZ1_COND_003", "Breakout conditional on volume expansion", "CONDITIONAL_REGIME", "VOLUME_CONFIRMATION_X_BREAKOUT", "rank_cs(distance_to_prior_high60) * rank_cs(relative_volume) after parent archetype freeze", ["high", "close", "volume", "adj_factor"], "65 sessions", "A breakout with expanding activity may contain more information than either parent alone.", related=["FZ1_BRK_002", "FZ1_VOLM_003"], risks=PRICE_RISKS+ACTIVITY_RISKS, readiness="DEFERRED_TO_P0_8D", abstraction="CONDITIONAL", stage="P0_8D", timing="P0_8D_ONLY_AFTER_STATE_FREEZE", turnover="VERY_HIGH", provenance=["P0_8_CONDITIONAL_PROTOTYPE"])
add("FZ1_COND_004", "Low-volatility factor conditional on market drawdown", "CONDITIONAL_REGIME", "MARKET_DRAWDOWN_X_LOW_VOL", "rank_cs(-vol60) active only when lagged equal_weight_market_drawdown60 is HIGH", ["close", "adj_factor"], "60 sessions plus market state", "The defensive low-volatility dimension may be strongest during broad market stress.", related=["PG_VOL_REALIZED", "FZ1_DTR_004"], risks=MARKET_RISKS, readiness="DEFERRED_TO_P0_8D", abstraction="CONDITIONAL", stage="P0_8D", timing="P0_8D_ONLY_AFTER_STATE_FREEZE", turnover="MEDIUM", provenance=["P0_8_CONDITIONAL_PROTOTYPE"])


EXPECTED_COUNTS = {
    "MOMENTUM": 5,
    "REVERSAL": 5,
    "TREND": 6,
    "VOLATILITY": 6,
    "DOWNSIDE_TAIL_RISK": 5,
    "RANGE_ATR_COMPRESSION": 6,
    "LIQUIDITY": 6,
    "TURNOVER_DYNAMICS": 5,
    "RAW_RELATIVE_VOLUME": 5,
    "PRICE_VOLUME_RELATION": 6,
    "GAP_OPEN_CLOSE": 5,
    "INTRADAY_DAILY_BAR": 5,
    "PRICE_RANGE_POSITION": 5,
    "HIGH_LOW_BREAKOUT": 5,
    "DISTRIBUTION_SHAPE": 5,
    "MARKET_BETA_RESIDUAL": 6,
    "ROLLING_CORRELATION": 4,
    "PRICE_EFFICIENCY_TREND_NOISE": 5,
    "VOLATILITY_RETURN_RELATION": 4,
    "CONDITIONAL_REGIME": 4,
}


def stable_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def write_card(item: dict) -> None:
    def bullets(values: list[str]) -> str:
        return "\n".join(f"- `{value}`" for value in values) if values else "- None declared"

    text = f"""# {item['factor_id']} — {item['canonical_name']}

- Family: `{item['family']}`
- Concept: `{item['concept']}`
- Parameterization group: `{item['parameterization_group']}` / `{item['variant_role']}`
- Abstraction: `{item['abstraction']}`
- Definition status: `{item['definition_status']}`
- Evaluation stage: `{item['evaluation_stage']}`
- Lifecycle: `{item['lifecycle']}`

## Formula

`{item['formula_pseudocode']}`

Lookback/input horizon: {item['lookback_input_horizon']}.

## Inputs and timing

Raw fields:

{bullets(item['required_raw_fields'])}

Derived inputs:

{bullets(item['derived_inputs'])}

Availability: `{item['signal_availability_timing']}`.

## Hypothesis

Direction: `{item['expected_direction']}`.

{item['hypothesis']}

Common-use note: {item['literature_common_usage_note']}

## Implementation profile

- Expected turnover: `{item['expected_turnover']}`
- Execution sensitivity: {item['potential_execution_sensitivity']}
- Data readiness: `{item['data_readiness_status']}`

Likely related/redundant factors:

{bullets(item['likely_related_redundant_factors'])}

PIT/lookahead risks:

{bullets(item['pit_lookahead_risks'])}

Provenance:

{bullets(item['provenance'])}

## Planned tests

{bullets(item['planned_tests'])}
"""
    (CARDS / f"{item['factor_id']}.md").write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    counts = Counter(item["family"] for item in factors)
    assert dict(counts) == EXPECTED_COUNTS, (counts, EXPECTED_COUNTS)
    assert len(factors) == 103, len(factors)
    assert len({item["factor_id"] for item in factors}) == len(factors)
    assert sum(item["evaluation_stage"] == "P0_8B" for item in factors) == 99
    assert sum(item["evaluation_stage"] == "P0_8D" for item in factors) == 4

    concepts = {item["concept"] for item in factors}
    groups = {item["parameterization_group"] for item in factors}
    payload = {
        "schema_version": "FACTOR_REGISTRY_V1_DRAFT",
        "program": "P0_8_FACTOR_ZOO_AND_FACTOR_STRUCTURE_DISCOVERY_V1",
        "created_date": "2026-09-18",
        "definition_status": "DRAFT_DESIGN_REQUIRES_P0_8A_CODE_HASH_FREEZE",
        "dataset_id": "FREE_DAILY_V1",
        "dataset_hash": "5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5",
        "protected_holdout": "2026-01-05..2026-09-15 SEALED_UNACCESSED_UNCONSUMED",
        "factor_count": len(factors),
        "atomic_transformed_count": 99,
        "conditional_prototype_count": 4,
        "concept_count": len(concepts),
        "parameterization_group_count": len(groups),
        "family_counts": EXPECTED_COUNTS,
        "formula_conventions": {
            "r1": "adj_close[t]/adj_close[t-1]-1",
            "retH": "adj_close[t]/adj_close[t-H]-1",
            "adjusted_ohlc": "raw OHLC multiplied by the same-date frozen adj_factor convention",
            "market_r1": "equal-weight mean r1 of the frozen same-date eligible universe",
            "rank_cs": "same-date average-tie percentile rank on eligible non-missing observations",
            "rolling_windows": "backward-looking, include t, and require the full declared window",
            "zero_denominator": "observation is missing/denied unless the formula explicitly adds epsilon",
            "execution": "signal after t close; earliest entry t+1 eligible open",
        },
        "factors": factors,
    }
    encoded = stable_json(payload)
    payload_hash = hashlib.sha256(encoded.encode("utf-8")).hexdigest()

    OUT.mkdir(parents=True, exist_ok=True)
    CARDS.mkdir(parents=True, exist_ok=True)
    (OUT / "FACTOR_REGISTRY_V1.json").write_text(encoded, encoding="utf-8", newline="\n")
    for item in factors:
        write_card(item)

    rows = "\n".join(
        f"| [{item['factor_id']}](FACTOR_CARDS/{item['factor_id']}.md) | {item['canonical_name']} | {item['family']} | {item['concept']} | {item['data_readiness_status']} | {item['evaluation_stage']} |"
        for item in factors
    )
    index = f"""# Factor Registry V1 Index

- Status: `DRAFT_DESIGN`; P0-8A code/hash freeze required before predictive evaluation.
- Registry SHA-256: `{payload_hash}`
- Definitions: {len(factors)}
- Atomic/transformed P0-8B definitions: 99
- Conditional P0-8D prototypes: 4
- Concepts: {len(concepts)}
- Parameterization groups: {len(groups)}
- Protected 2026 holdout: `SEALED / UNACCESSED / UNCONSUMED`

| Factor ID | Canonical name | Family | Concept | Readiness | Stage |
| --- | --- | --- | --- | --- | --- |
{rows}
"""
    (OUT / "FACTOR_REGISTRY_V1.md").write_text(index, encoding="utf-8", newline="\n")
    print(json.dumps({"factor_count": len(factors), "concept_count": len(concepts), "parameterization_group_count": len(groups), "registry_sha256": payload_hash}, sort_keys=True))


if __name__ == "__main__":
    main()
