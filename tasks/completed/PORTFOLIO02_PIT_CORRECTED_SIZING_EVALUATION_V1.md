# PORTFOLIO02 PIT-corrected sizing evaluation V1

- Status: `COMPLETE`
- Outcome: `RANK_WEIGHT_PROVISIONAL`
- Execution branch: `codex/portfolio02-pit-corrected-sizing-v1`
- Ledger branch: `codex/portfolio02-pit-corrected-sizing-v1`
- Alpha Factory result commit: `c4d49d782cc34c5666fc5f581f9d45ca45096ab8`
- Research Ledger source commit: `ef1f1d1ca1ae51231816101ab519099dd7549870`
- Next: `CONTROLLER_JOINT_DIRECTION`

The task evaluated only EqualWeight, canonical RankWeight and within-date ScoreTilt on the identical corrected Ridge F1/S123 V2 Top20 under AlwaysInvest, exact event-aware account semantics and the primary pre-frozen integer target allocator. The fixed 15-attempt queue completed without retry. RankWeight won the only selection-eligible metric: RMB 50,000, 1x-cost terminal wealth of RMB 59,600.99 versus RMB 57,445.71 for EqualWeight and RMB 56,813.97 for ScoreTilt.

All holding paths are `EXACT_FOR_THIS_REPLAY`; validator is 16 PASS / 0 FAIL and the repository suite is 259 PASS. EqualWeight narrowly leads RankWeight under 2x costs, so RankWeight remains provisional and cost-sensitive. The 1m, Greedy, fractional, bimonthly and concentration outputs are diagnostic only.

Evidence remains selection contaminated. No Exposure02 output, Cash Gate, joint policy, 2024–2025 data, 2026 data, broker action or production deployment was used. Exact execution artifacts are in the Alpha Factory report, checkpoint, result bundle and diagnostics at the commit above.
