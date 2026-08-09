<!-- org-project-routing:start -->
# Project routing

- **GitHub organization:** [benefactor-cc](https://github.com/benefactor-cc)
- **Canonical GitHub Project:** [benefactor-cc-project](https://github.com/orgs/benefactor-cc/projects/1) (project 1)
- **Canonical Linear project:** [github.com/benefactor-cc](https://linear.app/denman/project/githubcombenefactor-cc-6bef502a1ef0)
- **Organization documentation repository:** [benefactor-cc/.github](https://github.com/benefactor-cc/.github)

## Source-of-truth boundaries

GitHub is authoritative for repositories, commits, pull requests, reviews, CI checks, releases, deployable artifacts, and runtime evidence. Linear is authoritative for product planning, priorities, ownership, dependencies, milestones, and status reporting. The GitHub Project is the organization-level execution board and should contain the governance issue maintained by this repository.

## Change and merge policy

Documentation branches must be reviewed through pull requests and merged after checks pass. Concurrent edits are reconciled semantically against the latest default branch: this managed routing block is regenerated while all unrelated prose outside the block is preserved. Do not resolve conflicts by blindly choosing one side.
<!-- org-project-routing:end -->

## Execution snapshot — 2026-08-08

### Reusable package family — certified

The package-family program tracked by Linear `DEN-2510` is complete. The canonical DAG is:

```text
benefactor-interfaces
        |
        v
benefactor-lib
     |       \
     v        v
benefactor-clients
        |
        v
benefactor-cli
```

`benefactor-interfaces` remains the only wire/schema owner. Clients import interfaces and lib; CLI imports interfaces, lib, and clients. The machine-readable graph is `benefactor-monorepo/docs/package-family.json`.

All three formerly planned repositories now exist as private `benefactor-cc` repositories, passed exact-head CI, publish root-owned Zed artifacts, and are exact submodules in `benefactor-monorepo`.

| Package | Feature merge | Clean-consumer gate merge | Current provenance `main` | Current artifact |
| --- | --- | --- | --- | --- |
| `benefactor-lib` | `41e9e79049739da2ae8db9b2d37c9be5f547e2a6` | `d4095f53ae8e6d4428c8b885ad0141bc2aed30a4` | `d4095f53ae8e6d4428c8b885ad0141bc2aed30a4` | `9029388106` / `sha256:24a7a858a6cd38488ae1af615a3dd44d351f88ef137de550ae43b47cdc5164dd` |
| `benefactor-clients` | `c98e7986accae727bcf1780f4891c019bc987f5c` | `def343cef837d1fd055933e5e116a52f7b4b8bfb` | `0ebda97dbc2bb85d63da5f940010c86b4ee303ed` | `9029982235` / `sha256:be63802ecdadd258e03302f75ea25e9a4d403201e7589fb488043e1a50cbfb80` |
| `benefactor-cli` | `3470b8585ae89784351638c81d2f3242a69100a2` | `368278b090772963c263f648e8c298d7c32b8292` | `29d9efdf8caa145ec77cabf9bd61e280706ecab6` | `9029981144` / `sha256:3930e0bfa8b0a484930b584cdc4d40f70603f32c87122d1d02380cd161dac2b9` |

The clean-consumer gates do more than pack: every exact Zed tarball is extracted into a fresh directory and the applicable Rust/WASM/TypeScript or CLI build/test/contract suite is rerun from the artifact contents before `SHA256SUMS` and the artifact bundle are uploaded.

The clients and CLI current mains are provenance-only follow-ups: their runtime/API sources and package versions did not change. `benefactor-clients#3` repinned its immutable lib evidence to the clean-consumer-certified lib main, and `benefactor-cli#3` repinned its lib/clients evidence to the clean-consumer-certified mains. Both exact heads passed their full repository and clean-consumer Zed CI before merge.

### Superproject integration

- `benefactor-monorepo#8` migrated lib, clients, and CLI from README placeholders to mode-`160000` gitlinks and merged as `8f2b3e0df3cfeb53a40329965f7e3a4faeec2342`.
- `benefactor-monorepo#9` repinned those gitlinks to the permanent clean-consumer-certified package mains and merged as `b4908bed0a377d5dbdc162e47cd7a07cf2de2743`.
- `benefactor-monorepo#10` advanced clients/CLI to the provenance-synchronized mains and aligned README/boundary evidence; exact-head contract and repository-hygiene checks passed; merge `4d1ce015e9bb3477fa041a3d0aaf1dc7ee3b534c`.

Current gitlinks:

- lib → `d4095f53ae8e6d4428c8b885ad0141bc2aed30a4`
- clients → `0ebda97dbc2bb85d63da5f940010c86b4ee303ed`
- CLI → `29d9efdf8caa145ec77cabf9bd61e280706ecab6`

Provisioning GitHub issues `.github#7`, `#8`, and `#9` are closed. Linear `DEN-2512`, `DEN-2513`, `DEN-2514`, and parent `DEN-2510` are Done. `DEN-3227` records the final clean-consumer/provenance repin evidence.

### Package ownership boundaries

Permanent CI and repository contracts preserve these responsibilities:

- **interfaces:** schemas and wire contracts;
- **lib:** deterministic validation/transformation only; no network, live credential, database-write, outreach, or deployment ownership;
- **clients:** bounded transport mechanics—URL/path safety, deadlines, redirect refusal, response ceilings, bearer safety, typed failures, retry classification—without CRM/campaign/persistence policy;
- **CLI:** flags-2-env-compatible orchestration through the package family, env-only bearer configuration, stable human/JSON output, stable exit codes, and explicit dry-run for mutation plans; no direct provider/database/HTTP implementation.

Rust is primary. Lib and clients also certify TypeScript/WASM-compatible surfaces. Every package owns root `.zpkg.toml` and `.zpkg.lock`, uses immutable-pinned read-only Actions, and produces checksum-addressed artifacts. Downstream provenance records must identify the reviewed package mains represented by the superproject gitlinks.

### Merged dependency maintenance

- `backend.rs#19` upgraded the immutable `docker/login-action` reference after successful exact-head backend CI; merge `71870054849adaed7a5a1fb10d1b17e68654ea54`.
- `benefactor-cc-mcp-server.rs#15` upgraded the immutable `taiki-e/install-action` reference after successful exact-head MCP CI; merge `930e9d6f4f597d2bdab6947251ded44f1f272248`.

### Consent-gated Gmail service-account lane

`benefactor-sendgrid-outreach#10` merged the optional exact-batch Gmail delivery lane as `b6007e2871c672b98c629b6e386fcaa5e6ff4d26`. It requires an active `consent_status='opted_in'` marketing record, an exact `CONTACT_BATCH_ID`, shared Postgres reminder/throttle/event ledgers, HTTPS one-click unsubscribe, explicit live confirmation, and a delegated Workspace mailbox with only the `gmail.send` scope.

Follow-up PR `benefactor-sendgrid-outreach#11` repaired externally merged correctness gaps and merged as `7e4129dd0a98cd515c1b8a165a2c109f8032b233` after successful exact-head repository CI. Code readiness does **not** authorize a production campaign. `DEN-833` remains the operational source of truth for the reviewed recipient manifest, dry run, credentialed canary, reconciliation, and explicit stop/continue decision.

### Separate infrastructure lanes

The completed package-family program did **not** mutate Cloudflare, DNS, databases, deployments, or outreach production state. `benefactor-web-server.rs`, `benefactor-api-server.rs`, and `benefactor-infra` remain separate repository/service workstreams. Cloudflare activation must stay scoped to `benefactor-infra` and requires exact Benefactor account/zone/tunnel verification before any write.

### Board hygiene

- Attach exact PR heads, merge commits, artifact IDs/digests, and clean-consumer evidence to the matching Linear item.
- Interfaces own wire contracts; downstream packages import them rather than copying generated schemas.
- Keep application/deployment work separate from package certification.
- Mutating and outreach actions remain explicit and dry-run-first.
- Never store PATs, API tokens, R2 credentials, live provider credentials, expiring artifact URLs, or write-capable bootstrap workflows in permanent CI or project documentation.
