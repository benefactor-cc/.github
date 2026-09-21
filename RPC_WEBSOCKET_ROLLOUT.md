# RPC / WebSocket rollout contract

This document is the cross-repository gate for enabling authoritative `.ores-ws.toml` RPC ingress in Benefactor API roles.

## Current state

- `benefactor-web-server.rs` and `benefactor-admin-web-server.rs` are web roles. They may consume the canonical WebSocket runtime as RPC clients, but they must fail closed if `.ores-ws.toml` enables authoritative ingress.
- `benefactor-api-server.rs` and `benefactor-admin-api-server.rs` are the only Benefactor roles that may eventually enable authoritative WebSocket RPC ingress.
- Neither API repository currently exposes the canonical generated `api-docs` / `ores-stack` RPC dispatcher. Therefore `.ores-ws.toml` must remain `enabled = false` in both API roles until the dispatcher gates below are satisfied.
- WebSocket RPC is a transport projection of the same semantic operation runtime used by HTTP and Lambda. It is not a second handler implementation.

## Required implementation order

1. **Adopt canonical operation source layout.**
   - Move or wrap write operations behind `#[ores_operation(...)]` handlers compatible with current `ORESoftware/api-docs` and `ORESoftware/ores-stack` generation.
   - Preserve existing wire behavior while migration is in progress.
   - Keep one stable operation key per semantic operation.

2. **Generate and commit canonical `rpc.rs`.**
   - Use deterministic `ores-stack rpc sync` / stack-sync tooling; do not hand-author generated dispatcher files.
   - Generated files must carry the canonical generated marker and remain generator-owned.
   - CI must run the equivalent `--check` path and fail on stale generated output.

3. **Make HTTP and Lambda call the same operation runtime.**
   - HTTP route adapters decode/validate transport input, construct the typed operation context, and invoke the semantic handler.
   - Lambda adapters do the same.
   - No HTTP-only business logic may be duplicated into WebSocket code.

4. **Add authenticated WebSocket transport projection.**
   - Load canonical `.ores-ws.toml` via `ores-websocket` runtime config.
   - Authenticate the connection using the same Shared Auth identity boundary required by the API role before dispatch is permitted.
   - Refuse forwarded identity when `trust_forwarded_identity = false`.
   - Route admitted `rpc.call` frames into the generated dispatcher by stable `operation_key`.
   - Apply canonical bounded JSON codec, duplicate-key rejection, JavaScript safe-integer parity, frame/message limits, family admission, connection limits, and heartbeat/inbound-frame timeout.

5. **Preserve one error model.**
   - Semantic operation errors map through the same canonical RPC error taxonomy regardless of HTTP, Lambda, or WebSocket transport.
   - Authentication/admission errors remain transport-boundary errors and do not masquerade as handler failures.
   - Logs must redact credentials and sensitive payloads.

6. **Enable only after conformance is green.**
   - `.ores-ws.toml` remains `enabled = false` until exact-head evidence proves generated dispatcher freshness, HTTP/RPC semantic parity, authenticated WS dispatch, codec regressions, and clean shutdown/backpressure behavior.
   - Enable public API and admin API independently. Admin ingress must remain isolated to its admin network/VPC boundary.

## Repository-specific first moves

### `benefactor-admin-api-server.rs`

This repository is already a focused Rust admin API surface and should be the first Benefactor dispatcher canary. Add one small existing admin operation to the canonical operation layout, generate its `rpc.rs`, prove HTTP and generated RPC call the same handler, then add WebSocket dispatch while keeping `.ores-ws.toml` disabled.

### `benefactor-api-server.rs`

The public API currently concentrates substantial behavior in `src/application.rs`. Do not bolt a second WebSocket handler tree onto that module. First extract a small write operation behind the canonical typed operation boundary, generate `rpc.rs`, and migrate incrementally. Existing HTTP behavior remains the compatibility baseline during extraction.

## Acceptance tests

A repository may set `.ores-ws.toml` to `enabled = true` only when all of the following are true:

- `ores-stack ... --check` reports generated RPC sources current.
- Every WebSocket-dispatchable operation has one stable operation key and one semantic handler.
- The same operation fixture produces semantically identical success/error output through HTTP, Lambda where applicable, and WebSocket RPC.
- Unknown operation keys fail closed without invoking application code.
- Unauthenticated connections cannot dispatch RPC calls.
- Forwarded identity is rejected when prohibited by config.
- Oversized frames/messages, duplicate JSON keys, and unsafe integers are rejected by the canonical codec.
- Disabled message families are rejected.
- Connection-count and heartbeat/inbound-frame timeout policy are enforced.
- Cancellation/streaming behavior is deterministic for operations that declare it.
- Graceful shutdown stops new admission and drains or terminates active RPC work within a bounded interval.
- No test or build path requires cross-organization private Git credentials merely to resolve canonical runtime packages; use immutable public Zed distribution snapshots for those dependencies.

## Non-goals

- Web roles do not host authoritative application RPC WebSocket ingress.
- WebSocket transport does not define a second operation schema or error taxonomy.
- Generated `rpc.rs` is not edited by hand.
- Lockfiles are resolver-generated; checksums or dependency entries are never fabricated manually.
