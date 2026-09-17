# Artifact Index

Large artifacts stay in the execution or artifact storage plane. This ledger records identifiers and provenance, not payload copies.

## Required reference fields

- Task ID
- Experiment ID
- Artifact ID
- Artifact type
- Alpha Factory commit SHA
- Report path
- Dataset ID and hash
- Storage location or repository-relative path
- Evidence class: `EMPIRICAL`, `DOCUMENTED`, `SYNTHETIC`, or `UNKNOWN`
- Integrity hash where applicable
- Producing date and status
- Related research decision IDs

## Index

| Artifact ID | Task ID | Experiment ID | Type | Alpha Factory commit | Path/location | Dataset ID/hash | Evidence class | Decision IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `P0_6E_DATASET_MANIFEST` | `P0_6E_FREE_DATA_EXPANSION_V1` | None | Dataset manifest | `69be29e41ddfdf815685f64d697465032c4a9891` | `research/free_daily_v1/DATASET_MANIFEST.json` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `EMPIRICAL` | ADR-0001; ADR-0007 |
| `P0_6E_FEATURE_READINESS` | `P0_6E_FREE_DATA_EXPANSION_V1` | None | Feature-readiness contract | `69be29e41ddfdf815685f64d697465032c4a9891` | `research/free_daily_v1/FEATURE_READINESS.json` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `EMPIRICAL` inputs plus `DOCUMENTED` scope decisions | ADR-0001; ADR-0005 |
| `P0_6E_RESULT_REPORT` | `P0_6E_FREE_DATA_EXPANSION_V1` | None | Final report | `69be29e41ddfdf815685f64d697465032c4a9891` | `reports/P0_6E_FREE_DATA_EXPANSION_REPORT.md` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `EMPIRICAL` | ADR-0001 |
| `P0_6E_COVERAGE_MATRIX` | `P0_6E_FREE_DATA_EXPANSION_V1` | None | Coverage report | `69be29e41ddfdf815685f64d697465032c4a9891` | `reports/P0_6E_FREE_DATA_COVERAGE_MATRIX.md` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `EMPIRICAL`, `DERIVED`, and `UNKNOWN` as row-labelled | ADR-0001 |
| `P0_6E_SURVIVORSHIP_AUDIT` | `P0_6E_FREE_DATA_EXPANSION_V1` | None | Survivorship audit | `69be29e41ddfdf815685f64d697465032c4a9891` | `reports/P0_6E_SURVIVORSHIP_AUDIT.md` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `EMPIRICAL` with retained PIT uncertainty | ADR-0001 |
| `P0_6E_DATA_QUALITY` | `P0_6E_FREE_DATA_EXPANSION_V1` | None | Data-quality report | `69be29e41ddfdf815685f64d697465032c4a9891` | `reports/P0_6E_DATA_QUALITY_REPORT.md` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `EMPIRICAL` | ADR-0001 |
| `P0_6E_RESOURCE_REPORT` | `P0_6E_FREE_DATA_EXPANSION_V1` | None | Resource report | `69be29e41ddfdf815685f64d697465032c4a9891` | `reports/P0_6E_RESOURCE_REPORT.md` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `EMPIRICAL` | ADR-0001 |
| `P0_6E_CHECKPOINT` | `P0_6E_FREE_DATA_EXPANSION_V1` | None | Completion checkpoint | `52c6a7eb506bb8848f1a643c469978d28804738c` | `reports/P0_6E_CHECKPOINT.json` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `EMPIRICAL` | ADR-0001; ADR-0007 |
| `P0_7C_DESIGN_SPEC` | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | Not assigned | Research task specification | Not started | `tasks/planned/P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1.md` in this ledger | Bound to `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `DOCUMENTED` | ADR-0004; ADR-0005; ADR-0007 |
