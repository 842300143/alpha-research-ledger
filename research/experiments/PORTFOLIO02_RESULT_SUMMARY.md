# PORTFOLIO02 result summary

`PORTFOLIO02_PIT_CORRECTED_SIZING_EVALUATION_V1` closes as `RANK_WEIGHT_PROVISIONAL` at Alpha Factory commit `c4d49d782cc34c5666fc5f581f9d45ca45096ab8`.

| Primary 50k / 1x | Terminal wealth | Net return | MDD | Turnover | Fills |
| --- | ---: | ---: | ---: | ---: | ---: |
| EqualWeight | RMB 57,445.71 | 14.89142% | -18.33094% | 43.20692 | 855 |
| RankWeight | RMB 59,600.99 | 19.20198% | -18.61791% | 53.17298 | 999 |
| ScoreTilt | RMB 56,813.97 | 13.62794% | -17.32050% | 45.98902 | 980 |

The result is `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED`, with `SYNTHETIC` research-account cost/execution assumptions. The fixed corrected model, Top20 candidates, AlwaysInvest exposure, election policy, costs and primary allocator were invariant. All 15 holding paths passed exact event coverage. The validator reports 16 PASS / 0 FAIL.

At 50k/2x costs, EqualWeight ends at RMB 52,155.30 and RankWeight at RMB 52,112.89. This nonselective reversal prevents a stronger claim. RankWeight also has the narrowest average position breadth (18.22 names), the highest Top5 capital fraction (42.78%) and the most unallocatable candidates, although it leaves the least average cash under the primary allocator.

See Alpha Factory `reports/PORTFOLIO02_PIT_CORRECTED_SIZING_EVALUATION_V1.md`, `state/checkpoints/PORTFOLIO02_PIT_CORRECTED_SIZING_EVALUATION_V1.json`, and `research/portfolio02/results/RESULT_BUNDLE.json`. No Exposure02 result substance, Cash Gate, later-period row or production action entered this evaluation.
