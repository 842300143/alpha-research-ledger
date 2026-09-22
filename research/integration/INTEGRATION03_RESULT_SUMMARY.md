# INTEGRATION03 result summary

`INTEGRATION03_20D_RESEARCH_BASELINE_FREEZE_V1` completed as `PASS_WITH_WARNINGS / CURRENT_20D_RESEARCH_BASELINE_V1_FROZEN`.

Alpha Factory work commit is `204bf7513e8baff852ef290734a548e4391ddb69` and normal master merge is `5655926d199ed294028af8c37de22d451c17a46d`. Research Ledger work commit is `930f1582ad7e8e349c029e8de4f49ecd4d8046d2` and normal main merge is `64079e57c7e06c951b994a4dd739cb391cb651e1`.

- Corrected model: `REQUAL01_RIDGE_F1_S123_V2` on `FREE_DAILY_PIT_V2`.
- Target and rebalance: 20 sessions each; the target horizon is a direct design assumption, not an empirical selection.
- Candidates: ordered Top20.
- Provisional sizing: RankWeight, RMB 59,600.99 / +19.20198% at 50k/1x.
- Canonical comparator: EqualWeight, RMB 57,445.71 / +14.89142% at 50k/1x.
- Cost warning: at 50k/2x, EqualWeight RMB 52,155.30 exceeds RankWeight RMB 52,112.89.
- ScoreTilt: evaluated, not promoted.
- Exposure: AlwaysInvest retained; cash RMB 50,000.00; Trend60 RMB 46,117.88 and rejected only for this frozen 20D system.
- Historical failure and repair lineage: preserved additively.
- SHORTLIST01: separate and not integrated.
- Validation: 18/18 independent checks and 8/8 Integration03 tests.
- Later-period access, replay, new Alpha research, broker orders and production action: none.

Exact machine-readable authority remains the Alpha Factory manifest, registry, Horizon audit, lineage file, checkpoint and report. Production champion is `NONE`; confirmed Alpha is `NO`.
