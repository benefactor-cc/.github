# Benefactor platform integration contract

The machine-readable policy in
[`architecture/platform-integrations.json`](../architecture/platform-integrations.json)
is the organization-wide minimum for reusable Benefactor code. It connects four
independent capabilities without making any Benefactor repository a source copy
of another organization.

## Observability: `ores-otel`

Services and clients emit ORES-compatible `next-loggers/v1` structured records
and OpenTelemetry signals through application-owned sinks. A library may create
records or spans, but it must not install a global provider, choose an exporter,
or flush and shut down a provider it does not own. Telemetry is bounded,
redacted, and best effort; it never controls the success of a write or request.

Until `oresoftware/next-loggers` and `ores-otel/ores-interfaces` resolve from the
public Zed registry, consumers keep the adapter boundary and audited source
revision explicit. They must not manufacture a registry entry or lockfile.

## Synchronization: `opto-sync`

`benefactor-sync` remains the owner of Benefactor entity policy and wraps the
certified Opto Sync engine. Mobile Flutter uses SQLite for the local row plus
outbox transaction. Web clients use IndexedDB or SQLite/Wasm with the same
durability rule.

Benefactor intentionally overrides any timestamp last-write-wins default:
`createdAt`, `updatedAt`, and `syncedAt` are metadata. Conflicts are detected by
`baseRevision`, authoritative row `revision`, and ordered change cursor. Nested
JSON/JSONB values use structural deep equality and the single Rust three-way
merge core; shallow object comparison is forbidden.

## Authentication: `shared-auth` plus Supabase

Human bearer authentication races Shared Auth verification against direct
Supabase user verification. The first verified identity wins, one failed arm
does not erase a success from the other, both definite invalid results produce
an unauthenticated result, and every uncertain or contradictory result fails
closed as degraded.

Authorization is deliberately asymmetric. Shared Auth roles may satisfy a
privileged role policy. A directly verified Supabase identity proves identity
only and has no privileged local roles. Machine credentials are never accepted
by an ordinary human guard.

## Dependency management: `zed-pkg`

Zed is the polyglot package and artifact resolver. Reusable package roots carry
both `.zpkg.toml` and `.zpkg.lock`; CI validates both and uses frozen installs.
An audited Git commit in this policy records what was reviewed, but it is not a
substitute for an immutable package resolution in a consumer lockfile.

If the public registry cannot resolve a dependency, the truthful state is
`pending-public-registry`. Consumers retain their injection boundary and fail
closed in production configuration rather than committing a locally seeded or
hand-written lock entry.
