# CAQUAL02 targeted event closure result

Evidence classification: official filing terms are `DOCUMENTED`; bounded local price/factor rows are `EMPIRICAL`; reconciliation calculations and ledger fixtures are analytical or `SYNTHETIC` and do not convert filing claims into empirical observations.

Alpha Factory work commit `5b056c223b6789f62f3da4b43c88d35841606bdd` resolves the seven CAQUAL01 data gaps as four non-entitlement reference-data events for `000029.SZ` and three elective rights offerings for `000049.SZ`, `000065.SZ`, and `000088.SZ`. All seven factor/preclose changes reconcile at the frozen tick/tolerance. CAQUAL01's 280 matches remain intact, so event-data coverage is 287/287 with zero unknown or contradictory rows.

Capability is `EVENT_DATA_COMPLETE_POLICY_REQUIRED`. The data layer is complete, but exact historical account replay requires the account's real `PARTICIPATE`/`DECLINE` choice for each held rights offering. Participation also requires exact subscribed quantity and cash-debit date; nominal ratios do not authorize an inferred fractional allocation. No paid-data gap remains.

The event ledger and holding-path gate are for historical execution accounting only. Event facts are prohibited from predictive feature or signal injection. No Alpha, return, exposure, portfolio, future-interval, broker, purchase, credential, or production action occurred.
