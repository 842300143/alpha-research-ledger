# Alpha Factory Commit Index

This index links research intent to immutable execution state in `D:\alpha-factory`. Never invent or abbreviate an unknown SHA.

## Conventions

| Field | Meaning |
| --- | --- |
| Task ID | Stable controller task identifier |
| Experiment IDs | One or more registered experiment identifiers |
| Start commit | Full Alpha Factory SHA defining the task's starting state |
| End commit | Full Alpha Factory SHA containing the completed task state |
| Reports | Repository-relative paths to authoritative reports |
| Dataset ID/hash | Versioned dataset identity and immutable hash where available |
| Decision IDs | ADR or decision records changed by the evidence |

## Index

| Task ID | Experiment IDs | Start commit | End commit | Reports | Dataset ID/hash | Decision IDs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `P0_6E_FREE_DATA_EXPANSION_V1` | None; data phase only | `cf45be007afd168d8ad40746cfe1b16c3e0d2360` | `52c6a7eb506bb8848f1a643c469978d28804738c` | `reports/P0_6E_FREE_DATA_EXPANSION_REPORT.md`; `reports/P0_6E_CHECKPOINT.json`; supporting coverage, quality, survivorship, and resource reports | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | ADR-0001; ADR-0007 | `P0_6E_PASS_WITH_WARNINGS` / `COMPLETE` |
| `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | 27 registered configurations in the frozen Alpha V1 registry | `95dc8e3c5b895fe7bf47135536e0ed4843b73471` | `7e13a5129abfd5c0c4a56d37c1b1cd9c63a73138` | `reports/P0_7C_LONG_HORIZON_ALPHA_RESEARCH_REPORT.md`; `reports/P0_7C_CHECKPOINT.json`; Formula, ML, Portfolio, Pool, overlap, multiple-testing, regime, leakage, and Validator artifacts | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5` | ADR-0004; ADR-0005; ADR-0007; ADR-0008; ADR-0009; ADR-0010 | `P0_7C_PASS_WITH_WARNINGS` / `COMPLETE` |
| `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | Exact 17 frozen P0-7C OOS survivors; zero new predictive configurations | `76568528ed1a7c70d6b0a93b76924d7cb943dc94` | `cb3f4fe1e87f6a3e49bd8d59d3d8a76f19a4f8e0` | `reports/P0_7D_ALPHA_POOL_QUALIFICATION_REPORT.md`; `reports/P0_7D_CHECKPOINT.json`; redundancy, ML Formula-span, multiple-testing, and Generation-2 handoff reports | `FREE_DAILY_V1` / `5edea16aa003a37d4b71609ed8108ec77ae9f483fe918f54abc221316b57a8b5`; result `d06b21fe5bcea2b394be0d6b7a09006a2518aaf37d04933631b4a5b49fbcb360` | ADR-0008; ADR-0009; ADR-0010; ADR-0011 | `P0_7D_PASS_WITH_WARNINGS` / `COMPLETE` |
| `P0_7E_ALPHA_RESEARCH_V2` | 3 Formula candidates + 4 ElasticNet family ablations | `f3523ac72ed6995f3d0342d6b28d25fb5f78fb4b` | `c37ab3caf0c50c100906503d17d05fd5f78e2e24` | `reports/P0_7E_ALPHA_RESEARCH_V2_FINAL.md`; `research/alpha_v2/results/RESULT_BUNDLE.json`; `state/checkpoints/P0_7E_ALPHA_RESEARCH_V2.json` | `FREE_DAILY_V1`; result `bd2b6bc841ed948237ddac98777d43d38f89a28e27d9d5de99bee4d9031746d4`; freeze `7399a25d212caa7b1a6c68c8f7ac8a362fbffeefd6d92f9168ca0b902f9364b8` | ADR-0011; ADR-0012; ADR-0013; ADR-0014 | `P0_7E_PASS_WITH_WARNINGS` / `COMPLETE` |

## Backfill rule

Backfill from Alpha Factory's committed evidence. A backfill should cite the source path or Git command used to verify the SHA and must not reinterpret frozen results.

For P0-6E, controller authorization was committed at `67591334d7289c6d6685b6538568241591512f2b`, execution activated at the indexed start commit, the substantive dataset/result was committed at `69be29e41ddfdf815685f64d697465032c4a9891`, and the final state checkpoint was committed at the indexed end commit.

For P0-7C, the protocol and pre-execution manifests were frozen at the indexed start commit, substantive results were committed at `a881bd956c70088100f85999e7f0f4f965777a25`, and the final state checkpoint was committed at the indexed end commit.

For P0-7D, the protocol was frozen at the indexed start commit, substantive qualification results were committed at `a5c3d5b75b0fe2ac17bb7a37a7ba516f71bd1f63`, and the final state checkpoint was committed at the indexed end commit.

For P0-7E, the protocol was frozen at the indexed start commit, three implementation-only corrections were committed without changing research definitions, substantive results were committed at `27793d974110758ccf83848aed3d9354341b7e3f`, and the final state checkpoint was committed at the indexed end commit.
