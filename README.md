# alpha-research-ledger

Research / Controller / Knowledge / History plane for Alpha Factory.

This repository preserves what was tried, why it was tried, what failed, what changed, and which evidence changed a decision. It is the durable research source of truth; chat history is not.

## Repository boundary

| Repository | Role |
| --- | --- |
| `D:\alpha-research-ledger` | Research direction, task specifications, hypotheses, decisions, reviews, and history |
| `D:\alpha-factory` | Execution, code, data pipelines, experiment runs, and result artifacts |

Do not run market experiments here and do not connect the repositories with Git submodules. Link work across repositories with task IDs, experiment IDs, Alpha Factory commit SHAs, report paths, artifact IDs, and dataset IDs or hashes.

## Research lineage

```text
INBOX
  -> PAPER / IDEA
  -> HYPOTHESIS
  -> EXPERIMENT
  -> TASK
  -> alpha-factory execution
  -> RESULT
  -> REVIEW
  -> DECISION
  -> next hypothesis
```

Every material experiment must be traceable backward to why it exists and forward to the decision it changed. Negative results and abandoned paths are retained.

## Current direction

- Build an automated Alpha Research Factory, Portfolio Engine, and Execution Engine.
- Use a five-layer architecture: Data, Alpha Discovery, Alpha Evaluation, Portfolio, Execution.
- Strengthen the currently weak Alpha Discovery and Portfolio layers.
- Build a pool of weak, predictive, stable, low-correlated, post-cost usable signals rather than search for one magic strategy.
- Follow `FREE FIRST`: pay only when the free research path exposes a specific, valuable bottleneck.
- Treat protected Blind evaluation as a controlled, non-repeatable resource.
- Execute the P0-8 Factor Zoo program as a canonical factor-space and structure-discovery effort, not a highest-return search.
- Keep the 2026 protected holdout sealed through the P0-8 research sequence.

Start with [state/CURRENT.md](state/CURRENT.md), [state/NEXT.md](state/NEXT.md), and [state/RESEARCH_PRINCIPLES.md](state/RESEARCH_PRINCIPLES.md).
