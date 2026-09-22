# EVALRECON01 common-baseline reconciliation V1

Status: `COMPLETE / PASS_WITH_WARNINGS / COMMON_BASELINE_RECONCILED`  
Controller directive: `ALPHA-EVALRECON01-COMMON-BASELINE-RECONCILIATION-V1`  
Mode: `CORRECTNESS_RECONCILIATION_ONLY`

The task reconciled the committed Exposure02 V2 P0 AlwaysInvest + EqualWeight terminal wealth of RMB 58,123.84 with the committed Portfolio02 EqualWeight + AlwaysInvest terminal wealth of RMB 57,445.71.

The first divergence is the 2021-07-05 decision / 2021-07-06 account day and is caused by allocator-reserve config drift. A second Exposure02 implementation defect performs non-grid dynamic reallocation after a rejected exit. Under the authority-bound contract, all exact components and daily states within the frozen tolerance reconcile to the Portfolio02 path at RMB 57,445.71.

Alpha Factory formal work commit: `7189c2201e6bf1d6350eb5f67820a8f29128f61b`. Result publication commit: `c403312bd8397b3999ec1e0505688ecb814b9571`. See ADR-0037 and `research/exposure/EVALRECON01_RESULT_SUMMARY.md`.

Exposure02's frozen winner is not carried forward; a separate controller directive is required for an exact frozen-roster replay. Portfolio02 requires no correctness replay. No predecessor artifact, winner, later-period seal, broker, payment, credential, or production state changed.
