# MODEL01 fixed model-capacity comparison

**Later objective note (ADR-0019):** MODEL01's RankIC-based choice is complete and unchanged; it does not establish the tax-and-fee-adjusted terminal-wealth optimum. ElasticNet F0's prior modeled net outcome is approximately 0.000422 above Ridge F1 and is retained as an alternative clue only. EXPOSURE01 fixes Ridge F1/S123 and tests cash exposure on 2019–2023 under a separate objective. The 2024–2025 tranche was previously used in Generation-1 work, so no project-wide unseen-data claim is made.

**EXPOSURE01 disposition (ADR-0020):** Alpha Factory work commit `87b4bbe2f87081b46182ffb1c2dd18a8aa78b198` closed the exposure comparison as `INCONCLUSIVE_CORRECTNESS_GATE`: the account consumed backward end-normalized adjustment factors containing later corporate-action links. The six EXPOSURE01 wealth outputs are invalid for selection. MODEL01's frozen Ridge F1/S123, 16 PASS / zero FAIL validator, RankIC selection and `COMPLETE_NO_MODEL_UPGRADE` outcome are untouched; EXPOSURE01's failure is not a retroactive model re-selection. See `research/exposure/EXPOSURE01_RESULT_SUMMARY.md`.

- Task: `MODEL01_MODEL_CAPACITY_BAKEOFF_V1`
- Directive: `EXECUTE_MODEL01_MODEL_CAPACITY_BAKEOFF_V1`
- Alpha Factory pre-result code commit: `89563d7470403827c2bb893f6ae09423f6d0e47a`
- Alpha Factory pre-execution manifest commit: `482ba84cf757d1c21ab0ea538eef97101be40e21`
- Alpha Factory result work commit: `7565127615202c3edbc6d43458ac941d7a217282`
- Formal report: `reports/MODEL01_MODEL_CAPACITY_BAKEOFF_V1.md`
- Formal checkpoint: `state/checkpoints/MODEL01_MODEL_CAPACITY_BAKEOFF_V1.json`
- Selected freeze: `research/model01/SYSTEM_FREEZE.json`, SHA-256 `d7dcd4a2ebf930e805fc14fc9e059b4bd126b2c7b0054f4451ef8e559893deb7`
- Result/validator: `research/model01/RESULT.json`, `research/model01/VALIDATOR.json`

All five predeclared families, Ridge, ElasticNet, additive GAM, fixed-pair GA2M, and shallow LightGBM, completed F0 and F1 over WF1–WF3: ten systems and thirty terminal fold attempts, with zero failure and zero unavailable model. The 2019–2023 common panel and CAD02 Ridge F0/F1 prediction/cost metrics reproduced exactly. The Independent Validator reported 16 PASS / 0 FAIL. Successor child-process wall enforcement passed focused timeout, restart and clock-rollback tests; the historical CAD02 overrun and incomplete calibration are unchanged.

On F0, ElasticNet improved mean paired RankIC versus Ridge F0 by 0.032065; GAM, GA2M and LightGBM did not. C1/C2/C3's within-family F1−F0 paired gains were Ridge +0.031643, ElasticNet +0.002642, GAM +0.025942, GA2M +0.012030, and LightGBM +0.015470. The increment was positive in all three folds for Ridge, GAM, GA2M and LightGBM, while small and absent in one fold for ElasticNet. It was not fully absorbed by the fixed pair basis or shallow tree. This is representation evidence on reused discovery history, without a causal market interpretation.

ElasticNet F1 had the highest mean RankIC, but its 0.003064 advantage over Ridge F1 did not exceed the pre-frozen >0.005 complexity premium. The selected system is `RIDGE_F1`, identical to CAD02 S123; disposition `COMPLETE_NO_MODEL_UPGRADE`. The selected system is `PROVISIONAL_MODEL_REPRESENTATION_SYSTEM_V1`, not confirmed Alpha. Costs are synthetic, the panel lacks full PIT and survivorship certification, and all results inherit CAD01/CAD02 selection contamination. Cross-model consistency is not independent confirmation.

`CALIBRATION_EVIDENCE=LIMITED_DIAGNOSTIC`: 15 of 20 CAD02 runs complete, one incomplete, 2,297.160-second recorded wall overrun. No remaining seed was run. `2024_2025_ACCESSED=NO`; `2026_ACCESSED=NO`; `TEST_AUTHORIZED=NO`. The next step is controller direction, not test execution.
