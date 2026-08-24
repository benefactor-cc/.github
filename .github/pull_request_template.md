## Linear

- Issue or project: https://linear.app/denman/project/githubcombenefactor-cc-6bef502a1ef0

## Change summary

Describe the user-visible behavior, affected repositories and components,
compatibility impact, rollout or roll-forward path, and rollback constraints.
Mark non-applicable checks as `N/A` with a reason.

## Review path

- [ ] All commits are on a non-default branch and this pull request is the only proposed path into the default branch.
- [ ] No generated tool, bot, migration runner, or deployment process writes directly to `main`, `master`, or another protected default branch.
- [ ] The change is small enough to review, or its staged rollout and follow-up pull requests are identified.

## Scope, ownership, and dependencies

- [ ] The change is focused and does not silently cross repository ownership boundaries.
- [ ] Shared functionality is imported from its owning repository instead of copied into a local implementation.
- [ ] Cross-repository dependencies are pinned by an immutable commit, lockfile, or released Zed package.
- [ ] Public contracts are generated from canonical schemas and consumer compatibility was checked.
- [ ] Breaking changes include migration, rollback, and staged rollout notes.

## SQL, persistence, and state

- [ ] No SQL changes, or every declaration has a stable organization/domain namespace and an explicit owning repository.
- [ ] Declarations use the registered logical namespace `<organization>.<domain>` and stable `<domain>_` prefixes where a shared PostgreSQL schema such as `public` is required.
- [ ] Domain SQL may remain with its owning organization, but identity, ordering, checksums, drift detection, and promotion are registered through `declarative-migrations`.
- [ ] JSON Schema, generated language interfaces, ORM models, fixtures, and migration declarations were updated and checked deterministically together.
- [ ] Application startup validates schema compatibility and does not apply production DDL.
- [ ] Destructive changes, backfills, tenant isolation, RLS/authorization, idempotency, and state-machine invariants have evidence.

## Infrastructure and security

- [ ] No `*-infra` repository is introduced as a Git submodule under `*-monorepo/apps`.
- [ ] Application manifests remain app-owned; cluster composition is delegated to `oresoftware/k8s-cluster` and shared components to `oresoftware/k8s-libs-and-shared-defs`.
- [ ] Workloads use least privilege, restricted pod security, explicit network policy and egress, non-root execution, immutable images, probes, and bounded resources where applicable.
- [ ] Secrets, credentials, personal data, user content, and sensitive telemetry are excluded from source, logs, fixtures, and build artifacts.
- [ ] Authentication and authorization failures are fail closed, and sensitive operations are auditable.
- [ ] Destructive and cross-runtime tests run in the corresponding `*-test` organization or an isolated e2e environment, with teardown evidence.

## Validation and observability

- [ ] Zed lifecycle hooks run deterministic format, lint, build, contract, and publish checks without bypassing language-native validation.
- [ ] Unit, integration, adversarial, migration, and end-to-end tests cover the changed behavior in the appropriate test organization.
- [ ] ORES OTEL trace and correlation propagation is present where applicable, with secret and user-content capture disabled by default.
- [ ] Conflicts were resolved semantically using both sides, relevant history, and cross-repository context.
- [ ] No destructive, policy-bypass, or history-rewriting operation was executed or recommended.

## Validation evidence and residual risk

List exact commands, hosted check links, fixtures, migration or drift results,
deployment evidence, known limitations, monitoring, and the reversible
roll-forward plan.

- [ ] Logs and traces exclude secrets and user content by default and preserve tenant boundaries.
