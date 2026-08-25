# Benefactor web/API connection patterns

Status: organization architecture guidance, tracked by [DEN-4266](https://linear.app/denman/issue/DEN-4266/document-benefactor-cc-webapi-connection-patterns).

This policy applies to traditional customer/admin web/BFF, benefits/entitlements API, payments, reporting, and background services.

## Four supported avenues

| Avenue | Appropriate use | Boundary |
| --- | --- | --- |
| Direct database read | Named non-sensitive public/reference or independently rebuilt aggregate projection with a measured need | Never identity, beneficiary/private data, entitlement, eligibility, grant, payment, authorization, or writes; require distinct `SELECT`-only, `READ ONLY`, non-owner, `NOBYPASSRLS` access |
| Stateless HTTP/JSON | Default synchronous web-to-API path | Required for private reads, eligibility/entitlement decisions, grants, payments, administration, and every mutation |
| Stateful TCP | Measured authorized status/subscription stream with no beneficiary or payment authority | Never entitlement, eligibility, grant, payment, persistence, or authorization authority; require ADR, mTLS/delegated identity, bounded frames, deadlines, backpressure, and reconnect policy |
| NATS/message queue | Durable post-commit disbursement effects, exports, reconciliation, and notifications | Never login, eligibility, entitlement approval, payment authorization, or immediate response; require transactional outbox and idempotent consumers |

HTTP is the default. Entitlements, eligibility, grants, payments, and beneficiary-private data never use a direct web-server database path.

## Decision and ownership

1. Customer/beneficiary-private data, product authorization, eligibility, entitlements, grants, payments, and all mutations use HTTP.
2. Immediate authoritative answers use HTTP with typed/versioned interfaces, bounded bodies/timeouts, correlation context, and idempotency.
3. Durable post-commit effects are inserted into a transactional outbox and delivered through NATS.
4. A measured non-authoritative status stream may use TCP after an ADR and API authorization.
5. Direct reads remain limited to documented public/reference or reproducible aggregate projections under a restricted role.

The web/BFF owns HTML, secure opaque sessions, CSRF, and authorization-code plus PKCE. The API owns product authorization, eligibility and entitlement decisions, payment orchestration, and state changes. A core/data package owns typed mappings and transaction helpers. The canonical migration repository owns DDL; services verify compatibility and never migrate production at boot.

Shared Auth proves identity and assurance, not Benefactor eligibility, entitlement, grant, or payment permission. Validate realm, issuer, audience, tenant, app/client, scopes, session, freshness, and assurance. Protected introspection uses a separate service credential and carries the user's token only in the body. Never log bearer tokens, cookies, codes, PKCE verifiers, beneficiary data, payment details, gift-card codes, or raw introspection results.

Use immutable dependency revisions. `opto-sync` supports only declared synchronization/outbox workflows, `ores-otel` propagates bounded redacted telemetry, and `zed-pkg` records dependency provenance. None may bypass API authorization or entitlement ownership.

## Operational and payment requirements

- Bound bodies, frames, deadlines, retries, queues, and buffers; propagate trace and correlation context.
- Require mutation idempotency and duplicate-safe message consumers.
- A redirect is not settlement evidence; only a signature-verified, replay-safe, deduplicated provider webhook may advance payment state.
- Fail closed; never replace failed API authorization or eligibility with a direct query.
- Code comments identify the avenue and the beneficiary/entitlement constraint it satisfies.
- Every TCP or direct-read exception has an ADR, owner, measurements, and review/expiry date.

This document is the durable organization policy; repository ADRs may impose stricter controls.
