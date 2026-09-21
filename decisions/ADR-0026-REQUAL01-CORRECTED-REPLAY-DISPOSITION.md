# ADR-0026: REQUAL01 corrected replay disposition

- Status: Accepted / Complete
- Date: 2026-09-21
- Execution work commit: `9eb913aef4812cf6acb18e13ea66e947c16a427c`
- Result hash: `bf8c5bdb58f90db49767458578670a42a66607287a911ff9f7dcfed32c29a3f2`

Close `REQUAL01_PIT_CORRECTED_RESEARCH_REPLAY_V1` as `PASS_WITH_WARNINGS`. The additive `FREE_DAILY_PIT_V2` replay used 87,408 rows, 72 symbols, and only 2019-01-02 through 2023-12-29. The unchanged 97-factor / 291-attempt protocol retained 27 P0-8B survivors with zero lifecycle changes. P0-8C retained 16 clusters, 16 archetypes and 10 estimated dimensions. CAD01 retained three candidates after 131 evaluations; CAD02 selected `S123` after eight fixed systems, 24 system-fold attempts and 20 complete calibration runs; MODEL01 retained `RIDGE_F1` / `F1` after 30 attempts.

The corrected provisional system is numerically/system equivalent to the old provisional Ridge F1/S123 system, but the old artifact remains historical and is superseded for forward selection by the corrected additive freeze. The replay reuses discovery years, so its evidence ceiling remains `SELECTION_CONTAMINATED_RESEARCH`; it is correctness requalification, not independent confirmation or production evidence.

The independent validator reports 18 PASS / 3 warnings / 0 unknown / 0 fail, and all 184 Alpha Factory repository tests pass. Old result namespaces remained hash-identical. No interaction, Exposure, Portfolio winner selection, 2024–2025 or 2026 market access, payment, broker action or real trading occurred.

This decision resolves the PITPRICE01 upstream requalification gate only. Exact RMB 50,000 cash/share wealth qualification remains blocked on separately directed CAQUAL01 event entitlements. No account replay or later-period access is authorized.
