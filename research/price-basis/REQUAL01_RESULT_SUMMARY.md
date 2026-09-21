# REQUAL01 PIT-corrected research replay result

- Status: `PASS_WITH_WARNINGS`
- Evidence: `SELECTION_CONTAMINATED_RESEARCH`
- Alpha Factory work commit: `9eb913ac4bff3739c063a9b3f782bf68c74b98f8`
- Result hash: `bf8c5bdb58f90db49767458578670a42a66607287a911ff9f7dcfed32c29a3f2`
- Dataset: `FREE_DAILY_PIT_V2`, hash `2a37246c2bfd33176384568dda2ea6bef85edb29900c3fbab80875fefde06383`
- Scope: 87,408 rows, 72 symbols, `20190102..20231229`

## Corrected chain

- Factor impact: 14 exactly invariant, 37 provably scale invariant, 32 numerically changed, 14 unresolved.
- Target impact: 58 exact-rank row changes on 28 dates.
- P0-8B: 97 factors, 291 attempts, 27 survivors, zero lifecycle changes; result hash `f5c330fde4b7105362147ba7b78ba9896950e69b6f18dcfbf9faf1a42f0e05b5`.
- P0-8C: 16 clusters, 16 archetypes, 10 estimated dimensions, no structure change and zero interaction experiments; result hash `a3c1d8e6e932132b485fe4f7919913b66aae3ecc2fc08f727d0bd16ae3fe5127`.
- CAD01: 160 proposed, 131 evaluated, three candidates, `STAGNATION_RULE`; result hash `fdc6c3445149585f9720ac5e312658a14ed83747b98a966082d8b56553f00a67`.
- CAD02: 8 fixed systems, 24 system-fold attempts, `S123` selected, 20/20 calibration runs complete; result hash `6acbb875a28f5151f1528c0348805e909c1f3b87958746d6a14c497e0620b346`.
- MODEL01: 30 attempts, `RIDGE_F1` / `F1` retained, `COMPLETE_NO_MODEL_UPGRADE`; result hash `596a9b21a700e26fd9ad4fc2cee09a64050fe0dd259a7d9fcd7aad91604ccfde2`.

## Disposition and boundaries

The corrected system is numerically/system equivalent to the old provisional Ridge F1/S123 system. The old artifact is nevertheless `SUPERSEDED_FOR_FORWARD_SELECTION`; future authorized work must bind the corrected additive freeze. Validator: 18 PASS / 3 warnings / 0 unknown / 0 fail. All 184 repository tests pass.

This replay is not independent confirmation. It did not run interactions, Exposure, Portfolio winner selection, 2024–2025, 2026, payment, broker action or trading. Exact RMB 50,000 cash/share qualification remains blocked on CAQUAL01 event entitlements.

Authoritative Alpha Factory artifacts:

- `reports/REQUAL01_PIT_CORRECTED_RESEARCH_REPLAY_V1.md`
- `state/checkpoints/REQUAL01_PIT_CORRECTED_RESEARCH_REPLAY_V1.json`
- `research/requal01/results/RESULT_BUNDLE.json`
- `research/requal01/results/OLD_VS_CORRECTED_RESEARCH_MAP.json`
- `research/requal01/VALIDATOR.json`
