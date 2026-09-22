# EVALRECON01 common-baseline reconciliation — Research Ledger summary

`EVALRECON01_COMMON_BASELINE_RECONCILIATION_V1` completed at Alpha Factory formal work commit `7189c2201e6bf1d6350eb5f67820a8f29128f61b`, with result publication commit `c403312bd8397b3999ec1e0505688ecb814b9571`.

The theoretically common historical paths were not semantically identical. The first difference is the 2021-07-05 decision: Exposure02 allocator reserve drift produced 1,200 shares of `000008.SZ` versus Portfolio02's 1,100. After the reserve mapping is repaired, Exposure02 still performs a non-grid dynamic reallocation after a rejected exit on 2021-09-01. The common contract fixes the reserve mapping and makes rejection terminal for that execution day, carrying holdings to the next one of 36 scheduled decisions.

`CANONICAL_COMMON_BASELINE_V1` equals the Portfolio02 common path and ends at RMB 57,445.71, net 14.89142%, from RMB 50,000. It contains 872 orders, 17 rejections, 855 fills, 287 event checks, and 727 daily rows with `EXACT_FOR_THIS_REPLAY`. All exact component hashes match except daily fee-field serialization; its maximum numeric difference is `2.842170943040401e-14`, below the frozen `1e-8` tolerance. Independent Validator V2 passes 21/21.

Disposition under ADR-0037: Portfolio02 remains valid. Exposure02 V2 is retained historically but requires a separate exact frozen-roster replay before its winner can be used forward. No winner was selected or changed by EVALRECON01. Evidence remains selection-contaminated research with modeled execution costs; no production claim follows.

Primary execution evidence:

- `D:/alpha-factory-evalrecon01/reports/EVALRECON01_COMMON_BASELINE_RECONCILIATION_V1.md`
- `D:/alpha-factory-evalrecon01/state/checkpoints/EVALRECON01_COMMON_BASELINE_RECONCILIATION_V1.json`
- `D:/alpha-factory-evalrecon01/research/evalrecon01/CANONICAL_COMMON_BASELINE_V1.json`
- `D:/alpha-factory-evalrecon01/research/evalrecon01/VALIDATOR_RESULT_V2.json`

The 2024-2025 and 2026 market intervals remained sealed. No new Alpha, tuning, broker, payment, credential, production, or destructive action occurred.
