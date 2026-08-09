# `benefactor-cc` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **3**
- Private repository names withheld: **11**
- Relationship edges: **5**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/benefactor-cc/.github) | `organization_governance` | `active` |
| [`benefactor-cc.github.io`](https://github.com/benefactor-cc/benefactor-cc.github.io) | `site` | `active` |
| [`benfactor-cc`](https://github.com/benefactor-cc/benfactor-cc) | `uncategorized` | `active` |

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `benefactor-cc/.github` | `governs` | `benefactor-cc/benefactor-cc.github.io` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `benefactor-cc/.github` | `governs` | `benefactor-cc/benfactor-cc` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `organization://benefactor-cc` | `coordinates_via` | `capability://fiducia-cloud/distributed-coordination` | `platform-default` / `explicit-platform-decision`: locks, leases, idempotency, elections, schedules, budgets, and task claims |
| `organization://benefactor-cc` | `authenticates_via` | `capability://shared-auth/human-identity` | `platform-default` / `explicit-platform-decision`: platform human identity and session authority |
| `organization://benefactor-cc` | `packaged_via` | `platform://zed-pkg` | `platform-default` / `platform-policy`: Zed resolves artifacts while submodules compose editable source |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
