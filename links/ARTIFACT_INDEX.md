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
| `P0_7C_COMPLETED_SPEC` | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | 27 frozen configurations | Completed task specification | `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138` | `tasks/completed/P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1.md` in this ledger | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | `DOCUMENTED` design plus linked `EMPIRICAL_RESEARCH_ONLY` result | ADR-0004; ADR-0005; ADR-0007 |
| `P0_7C_RESULT_BUNDLE` | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | 27 frozen configurations | Canonical result bundle | `a881bd956c70088100f85999e7f0f4f965777a25` | `research/alpha_v1/results/RESULT_BUNDLE.json` | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`; bundle `30f0879579906af2d341a9053f9090b19616fbd3facd7415461b5ae247329444` | `EMPIRICAL_RESEARCH_ONLY` | ADR-0008; ADR-0009; ADR-0010 |
| `P0_7C_RESULT_REPORT` | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | 27 frozen configurations | Final research report | `a881bd956c70088100f85999e7f0f4f965777a25` | `reports/P0_7C_LONG_HORIZON_ALPHA_RESEARCH_REPORT.md` | Same P0-7C binding | `EMPIRICAL_RESEARCH_ONLY`, with `SYNTHETIC` cost/execution and `UNKNOWN` production limits | ADR-0008; ADR-0009; ADR-0010 |
| `P0_7C_CHECKPOINT` | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | 27 frozen configurations | Completion checkpoint | `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138` | `reports/P0_7C_CHECKPOINT.json` | Same P0-7C binding | `EMPIRICAL_RESEARCH_ONLY` | ADR-0008; ADR-0009; ADR-0010 |
| `P0_7C_POOL_QUALIFICATION` | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | 17 OOS survivors | Provisional pool qualification | `a881bd956c70088100f85999e7f0f4f965777a25` | `research/alpha_v1/registry/POOL_QUALIFICATION.json`; `research/alpha_v1/registry/ALPHA_POOL.json` | Strict pool empty; historical nine-name list provisional | `EMPIRICAL_RESEARCH_ONLY_WITH_PROTOCOL_WARNING` | ADR-0009 |
| `P0_7C_POOL_AUDIT` | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | 27 frozen configurations | Correlation, overlap, and descriptive incremental audit | `a881bd956c70088100f85999e7f0f4f965777a25` | `research/alpha_v1/diagnostics/POOL_OVERLAP_INCREMENTAL_AUDIT.json`; `research/alpha_v1/diagnostics/SIGNAL_CORRELATION.json` | Audit `9121c1984a237f7555171fea15bca882febfc4284e26a44c1527456ab4878f62` | `EMPIRICAL_RESEARCH_ONLY`; incremental ordering was descriptive, not a promotion rule | ADR-0009 |
| `P0_7C_VALIDATOR` | `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | 27 frozen configurations | Independent Validator result | `a881bd956c70088100f85999e7f0f4f965777a25` | `research/alpha_v1/VALIDATOR_RESULT.json` | 23 PASS / 7 UNKNOWN / 0 FAIL | `EMPIRICAL_RESEARCH_ONLY` | ADR-0009; ADR-0010 |
| `P0_7D_COMPLETED_SPEC` | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | Exact 17 P0-7C survivors | Completed task specification | `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0` | `tasks/completed/P0_7D_ALPHA_POOL_QUALIFICATION_V1.md` in this ledger | Bound to P0-7D result `d06b21fe5bcea2b394be0d6b7a09006a2518aaf37d04933631b4a5b49fbcb360` | `DOCUMENTED` design plus linked `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` result | ADR-0008; ADR-0009; ADR-0010; ADR-0011 |
| `P0_7D_RESULT_BUNDLE` | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | Exact 17 survivors | Canonical qualification result | `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63` | `research/alpha_pool_v1/results/RESULT_BUNDLE.json` | File SHA-256 `8c282beda55425c25b3641a90b01b9c46198f0ffab57dbd43428eda1819afac8`; payload `d06b21fe5bcea2b394be0d6b7a09006a2518aaf37d04933631b4a5b49fbcb360` | `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` | ADR-0011; ADR-0012 |
| `P0_7D_ALPHA_POOL_V1` | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | `P07C_ML_ENET_A010_L50` | Research-only Alpha Pool | `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63` | `research/alpha_pool_v1/results/ALPHA_POOL_V1.json` | File SHA-256 `af67c4baa6796bae252123456c43ee3b8ad432cba6a8c9c5c65f4420f5ccf56b` | `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` | ADR-0011 |
| `P0_7D_QUALIFICATION_TABLE` | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | 17 dispositions | Qualification table | `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63` | `research/alpha_pool_v1/results/QUALIFICATION_TABLE.json` | File SHA-256 `90da38a36e60e2c6f2e815d59a39ceb0850096ca0a6b1eebe37b55a270fc9a6a` | `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` | ADR-0011; ADR-0012 |
| `P0_7D_REDUNDANCY_TABLE` | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | 136 pairs | Redundancy table | `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63` | `research/alpha_pool_v1/results/REDUNDANCY_TABLE.json` | File SHA-256 `eb6923fdee21446733097399ea71e1bbb5a0008535d044cf86f61a886f1fcea9` | `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` | ADR-0012 |
| `P0_7D_ML_FORMULA_SPAN` | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | 9 ML survivors | ML Formula-span decomposition | `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63` | `research/alpha_pool_v1/results/ML_FORMULA_SPAN.json` | File SHA-256 `2e3b16e6aa9a6e46c2a4e59ab7e06c0b28cd0be0415e75cb3a26bd0d7871d983` | `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` | ADR-0011; ADR-0012 |
| `P0_7D_VALIDATOR` | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | Exact 17 survivors | Independent Validator | `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63` | `research/alpha_pool_v1/VALIDATOR_RESULT.json` | 16 PASS / 4 UNKNOWN / 0 FAIL; file SHA-256 `fd2bbd946f8c357e4166b124879ab76b15b919fa6892ea6f1c7988cf040f805c` | `EMPIRICAL` controls with retained `UNKNOWN` claims | ADR-0011; ADR-0013 |
| `P0_7D_CHECKPOINT` | `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | Exact 17 survivors | Completion checkpoint | `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0` | `reports/P0_7D_CHECKPOINT.json` | File SHA-256 `e19f94b7cc74032700ed84896628e3af26b90ac674afaf2a72627ee23a7b2dc3` | `EMPIRICAL_RESEARCH_ONLY_SELECTION_CONTAMINATED` | ADR-0011; ADR-0012; ADR-0013 |
| `P0_7E_DESIGN_SPEC` | `P0_7E_ALPHA_RESEARCH_V2` | 7 preregistered configurations | Research task specification | Not started | `tasks/planned/P0_7E_ALPHA_RESEARCH_V2.md` in this ledger | Bound to P0-7D result `d06b21fe5bcea2b394be0d6b7a09006a2518aaf37d04933631b4a5b49fbcb360` | `DOCUMENTED` | ADR-0011; ADR-0012; ADR-0013 |
