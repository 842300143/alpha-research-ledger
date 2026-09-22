# Next Research Work

## Current state

`INTEGRATION02_REQUAL_CORPORATE_ACTION_V1` is complete under ADR-0031. The corrected Ridge F1/S123 V2 system, CAQUAL02 event evidence, ELECTION01 self-financing policy, PITPRICE01 price/capital contracts, and INTEGRATION01 runtime/portfolio engine now share one versioned baseline. EXPOSURE01 V1 remains invalid for selection. The program is waiting for an exact controller directive.

## Recommended next direction

Choose exact, separately bounded EXPOSURE02 and PORTFOLIO02 scopes. Any replay must use the corrected exact system, RMB 50,000 primary capital, raw execution prices, and a per-run `EXACT_FOR_THIS_REPLAY` holding-path gate. Neither direction is currently authorized, and neither may imply a future test, broker order, payment or live deployment.

## Protected intervals

The 2024–2025 interval is `SEALED`. The 2026 protected holdout is `SEALED / UNACCESSED / UNCONSUMED`. Any later access requires a separate exact directive and the repository's pre-access manifest and one-run controls. REQUAL01, CAQUAL02, ELECTION01, historical CAD01/CAD02/MODEL01, EXPOSURE01 V1 and PITPRICE01 records remain frozen.
