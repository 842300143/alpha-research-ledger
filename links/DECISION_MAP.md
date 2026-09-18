# Decision Map

This map connects active research decisions to the phases and artifacts they govern. The ADR files remain authoritative.

| Decision | Status | Governs | Primary linked evidence |
| --- | --- | --- | --- |
| ADR-0001 Free First | Accepted | Data and model spending sequence | P0-6E checkpoint; P0-7C checkpoint |
| ADR-0002 Five-Layer Architecture | Accepted | L1-L5 ownership and interfaces | `architecture/FIVE_LAYER_ARCHITECTURE.md` |
| ADR-0003 Defer RD-Agent API | Accepted / Deferred | Credentialed RD-Agent/LLM work | Alpha Factory P0-4D state |
| ADR-0004 Alpha Pool, Not One Magic Strategy | Accepted | Pool objective and marginal contribution | P0-7C pool artifacts; P0-7D design |
| ADR-0005 Simple ML Before Deep Models | Accepted | Model-complexity ladder | P0-7C ML report |
| ADR-0006 Separate Research and Execution Repositories | Accepted | Repository boundary and cross-links | Commit and artifact indexes |
| ADR-0007 Supersede Old P0-7B Blind | Accepted | Historical Blind preservation | P0-7C leakage/holdout audit |
| ADR-0008 Top-20 Equal Weight Baseline V1 | Accepted | Portfolio comparisons and P0-7D constructor | P0-7C portfolio report |
| ADR-0009 Qualify Pool Before Broad Search | Accepted | P0-7D sequencing and zero-new-search rule | P0-7C pool qualification and audit |
| ADR-0010 Seal 2026 During Generation-2 | Accepted | P0-7D, P0-7E, and future holdout access | P0-7C checkpoint and leakage/holdout audit |
| ADR-0011 ElasticNet as Research Anchor | Accepted | Anchor claims and P0-7E comparison policy | P0-7D pool, qualification, and Validator artifacts |
| ADR-0012 Generation 2 Mechanism/Orthogonality | Accepted | P0-7E seven-configuration budget and promotion gates | P0-7D redundancy, Formula-span, and forward-addition evidence |
| ADR-0013 Last Major Iteration Before Holdout | Accepted | Post-P0-7E stop rule and holdout-decision sequencing | Cumulative search and P0-7D selection accounting |
| ADR-0014 Generation-2 Factor Zoo Research Policy | Accepted | P0-8 canonical factor-space program; scoped interpretation of ADR-0013 | P0-7E completion, FREE_DAILY_V1 capability, P0-8 charter and registry |

## Current decision path

`P0_7C_PASS_WITH_WARNINGS` -> `P0_7D_PASS_WITH_WARNINGS` -> `P0_7E_PASS_WITH_WARNINGS` -> ADR-0014 -> `P0_8A_FACTOR_ZOO_BUILD_V1` -> P0-8B evaluation -> P0-8C Factor Map -> bounded P0-8D interactions -> P0-8E/P0-8F structured selection -> P0-8G final research freeze -> separate protected-holdout adequacy/go-no-go.

No decision in this map authorizes protected-holdout access, RD-Agent/LLM use, payment, broker binding, trading, or production deployment.
