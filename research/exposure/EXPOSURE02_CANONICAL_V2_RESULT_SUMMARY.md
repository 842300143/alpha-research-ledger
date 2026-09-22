# Exposure02 canonical composition V2 result summary

`EXPOSURE02_CANONICAL_COMPOSITION_REPLAY_V2` completed at Alpha Factory commit `489a37206674813c6b56983a88702a485dc99776` as `PASS_WITH_WARNINGS / ALWAYS_INVEST_RETAINED`.

The V2 child directly loaded the frozen 36-date Exposure02 strategy grid and used EVALRECON01's canonical execution authority. P0 / RMB 50,000 / 1x reproduced RMB 57,445.71 and 14.89142%; P1 cash ended at RMB 50,000.00; P2 Trend60 ended at RMB 46,117.88 and -7.76424%. P0 remains the exposure policy under the frozen primary terminal-wealth rule.

All 12 one-use slots completed once. Every path has 36 strategic calls, zero off-grid strategic reallocations and exact holding-path event coverage. Focused tests pass 16/16; independent validation passes 41/41. The retained validator-interface publication failure changed no market result. Portfolio02 was not rerun or modified, and later intervals remained sealed.

Evidence is `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED_MODELED_EXECUTION`; it is not independent confirmation, production evidence or trading authorization. See ADR-0041 and the exact Alpha Factory report/checkpoint.
