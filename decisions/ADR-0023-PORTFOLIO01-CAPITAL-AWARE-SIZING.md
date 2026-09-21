# ADR-0023: PORTFOLIO01 capital-aware sizing engine

- Status: Integrated engineering component under ADR-0024.
- Isolated execution result: `02c1202aa91f6910af935c4d02140d5e95bf7721`; close `917221bb992aac2a1c06b87ff37fe8cf5d69c7ec`.
- Isolated Ledger record: `915f9d72e5a6a9ef27369877e70366977855469d`.
- Evidence: `DOCUMENTED` architecture and `SYNTHETIC` 216-cell matrix, 216 constraint passes. Real-market performance and exact executable wealth remain `UNKNOWN`.

Candidate Selection chooses Top20. Position Sizing separately applies EqualWeight, RankWeight or within-date ScoreTilt. Exposure is an independent scalar, and CapitalAllocator converts continuous weights to integer target shares by GreedyRoundLot or IntegerTargetApproximation. Desired shares are not orders or fills. The 5% Top20 EqualWeight mass is only a baseline arithmetic result, not a final investment rule.

The generic allocator receives explicit capital, cash, holdings, prices and lot rules; it has no 50k or 1m default. Integration binds the PITPRICE01 capital contract to 50k primary and 1m scaling diagnostic. Historical action data currently qualifies only for `TOTAL_RETURN_APPROX_ONLY`. Real-market portfolio evaluation and exact cash/share wealth remain blocked pending REQUAL01 and CAQUAL01 evidence. No return comparison or new Alpha result follows from the synthetic matrix.
