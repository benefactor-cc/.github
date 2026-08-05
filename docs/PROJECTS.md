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

## Execution snapshot — 2026-08-05

### Reusable package-family contract

`benefactor-monorepo#6` merged as `fdb1977edcbaed63a04b0ccced0fe6d67c97cc78` after successful exact-head CI. The superproject now carries a contract-tested integration boundary for:

```text
benefactor-interfaces
  -> benefactor-lib
  -> benefactor-clients (also imports interfaces)
  -> benefactor-cli (imports interfaces, lib, and clients)
```

The machine-readable source of truth is `benefactor-monorepo/docs/package-family.json`. It records repository names, dependency edges, roles, language surfaces, provisioning state, and root Zed package requirements. CI enforces:

- an exact nine-entry application/package inventory;
- an acyclic package graph;
- Rust-primary implementations;
- TypeScript/WASM surfaces where declared;
- root `.zpkg.toml` and `.zpkg.lock` ownership;
- interfaces as the only wire/schema owner;
- deterministic, network-free shared lib behavior;
- bounded clients without campaign/CRM policy ownership;
- a flags-2-env-compatible, dry-run-first CLI boundary;
- placeholder-only source policy until standalone repositories are reviewed and pinned as submodules.

### Repository provisioning lanes

`benefactor-interfaces` already exists and has certified Rust, Dart, JSON Schema, and Zed artifacts. The following repositories remain genuinely absent and must not be represented as created:

| Repository | GitHub issue | Linear issue | Dependency |
| --- | --- | --- | --- |
| `benefactor-lib` | `.github#7` | `DEN-2512` | interfaces |
| `benefactor-clients` | `.github#8` | `DEN-2513` | interfaces + lib |
| `benefactor-cli` | `.github#9` | `DEN-2514` | interfaces + lib + clients |

The parent delivery record is `DEN-2510`. Children preserve the real order: `DEN-2512` blocks `DEN-2513`, and both block `DEN-2514`.

Repository creation could not be executed in the active ChatGPT runtime because the available GitHub app connector does not expose creation, the `gh` binary is absent, apt has no package metadata for it, and outbound DNS is disabled. The merged contract and placeholders intentionally keep source out of the wrong repository and fail closed until actual repos and reviewed `main` commits exist.

### Merged dependency maintenance

- `backend.rs#19` upgraded the immutable `docker/login-action` reference after successful exact-head backend CI; merge `71870054849adaed7a5a1fb10d1b17e68654ea54`.
- `benefactor-cc-mcp-server.rs#15` upgraded the immutable `taiki-e/install-action` reference after successful exact-head MCP CI; merge `930e9d6f4f597d2bdab6947251ded44f1f272248`.

### Package acceptance boundary

A provisioning lane is complete only when:

1. the standalone repository exists under `benefactor-cc` with reviewed visibility;
2. dependencies use immutable interface/lib/client identities instead of copied source;
3. native, TypeScript, and WASM tests required by that package pass on one exact head;
4. immutable-pinned, read-only CI and Nix/dev-shell support exist;
5. root Zed package and clean-consumer tests pass;
6. the placeholder is replaced by a reviewed `main` submodule pin;
7. Linear and GitHub Project 1 contain exact PR, merge, package, and provenance evidence.

### Board hygiene

- Keep repository provisioning distinct from implementation and release completion.
- Do not mark placeholders or planning issues as created repositories.
- Attach exact PR heads, merge commits, Zed artifacts, and clean-consumer evidence to the matching Linear item.
- Interfaces own wire contracts; downstream packages import them.
- Lib remains deterministic and network-free; clients own transport policy; CLI routes through both.
- Mutating and outreach commands remain explicit and dry-run-first.
- Never store PATs, live credentials, expiring artifact URLs, or write-capable bootstrap workflows in permanent CI or project documentation.
