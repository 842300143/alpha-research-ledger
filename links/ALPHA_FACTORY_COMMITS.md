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
| `P0_6E_FREE_DATA_EXPANSION_V1` | `UNKNOWN / TO_BACKFILL` | `UNKNOWN / TO_BACKFILL` | `UNKNOWN / TO_BACKFILL` | `UNKNOWN / TO_BACKFILL` | `UNKNOWN / TO_BACKFILL` | `PENDING` | `ACTIVE` |
| `P0_7C_LONG_HORIZON_ALPHA_RESEARCH_V1` | `NOT_ASSIGNED` | `NOT_STARTED` | `NOT_STARTED` | `NOT_STARTED` | `SUBJECT_TO_P0_6E_RESULTS` | `PENDING` | `DRAFT_ONLY` |

## Backfill rule

Backfill from Alpha Factory's committed evidence. A backfill should cite the source path or Git command used to verify the SHA and must not reinterpret frozen results.
