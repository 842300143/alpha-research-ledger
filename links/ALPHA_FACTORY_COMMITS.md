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
| `P0_7D_ALPHA_POOL_QUALIFICATION_V1` | Exact 17 frozen P0-7C OOS survivors | `NOT_STARTED` | `NOT_STARTED` | Ledger design: `tasks/planned/P0_7D_ALPHA_POOL_QUALIFICATION_V1.md` | Bound to P0-7C result bundle `30f0879579906af2d341a9053f9090b19616fbd3facd7415461b5ae247329444`; no new dataset | ADR-0008; ADR-0009; ADR-0010 | `DESIGN_READY` / `NOT_YET_EXECUTED` |

## Backfill rule

Backfill from Alpha Factory's committed evidence. A backfill should cite the source path or Git command used to verify the SHA and must not reinterpret frozen results.

For P0-6E, controller authorization was committed at `67591334d7289c6d6685b6538568241591512f2b`, execution activated at the indexed start commit, the substantive dataset/result was committed at `69be29e41ddfdf815685f64d697465032c4a9891`, and the final state checkpoint was committed at the indexed end commit.

For P0-7C, the protocol and pre-execution manifests were frozen at the indexed start commit, substantive results were committed at `a881bd956c70088100f85999e7f0f4f965777a25`, and the final state checkpoint was committed at the indexed end commit.
