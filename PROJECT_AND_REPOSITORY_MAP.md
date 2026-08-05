# Benefactor project and repository map

This document maps the `benefactor-cc` GitHub organization to its Linear project and defines ownership boundaries for the contact-discovery and outreach system.

## Sources of truth

- Linear project `github.com/benefactor-cc` owns scope, priority, status, dependencies, acceptance criteria, and cross-repository sequencing.
- GitHub repositories and pull requests own implementation, review, CI evidence, and release history.
- GitHub Projects may mirror issues and pull requests for organization-facing visibility, but must not become an independent backlog. When fields disagree, reconcile GitHub to Linear.

Every material pull request should cite its Linear issue. Every completed Linear issue should link the merged pull request and bounded validation evidence. Never place credentials, contact exports, recipient addresses, message bodies, browser session state, or provider tokens in GitHub, Linear, CI artifacts, or logs.

## Outreach ownership

| Workstream | Linear owner | Repository owners | Boundary |
|---|---|---|---|
| ICP query generation, provider/browser discovery, normalization, verification, provenance, deduplication, HubSpot/RDS staging, and pre-outreach dry run | DEN-260 | `ORESoftware/k8s-cluster`, `benefactor-automations`, Benefactor backend and interfaces | Cannot authorize or send outbound messages |
| Canonical recipient manifest, human approval, canary/staged campaign, SendGrid execution, delivery/reply reconciliation, and final evidence | DEN-833 | `benefactor-sendgrid-outreach`, Benefactor backend and interfaces | Campaign-control source of truth |
| Consent-gated Gmail transport through Google Apps Script and a narrow Cloudflare gateway | DEN-2490 | `benefactor-gas` | Consumes only server-approved manifests and rechecks/claims every recipient; preview by default |
| Shared contact, suppression, outbox, and synchronization contracts | Related shared communications issues | `benefactor-interfaces`, `benefactor-sync` | Terminal suppression and idempotency remain authoritative across transports |

A transport must not infer consent, select recipients from a raw export, or weaken terminal suppression, unsubscribe, complaint, hard-bounce, customer, active-opportunity, prior-response, or cooldown precedence.

## Repository responsibilities

- `benefactor-automations`: data preparation and browser automation. It may produce reviewed candidates and CRM imports, but does not decide that a recipient may be contacted.
- `benefactor-interfaces`: canonical database, JSON Schema, Rust, Dart, and shared record contracts.
- `benefactor-sync`: product synchronization contracts and the Benefactor facade over Opto-Sync.
- `benefactor-sendgrid-outreach`: guarded SendGrid campaign path under DEN-833.
- `benefactor-gas`: guarded Gmail Apps Script transport and Cloudflare gateway under DEN-2490.
- `benefactor-e2e`: cross-repository contract and browser tests.
- `benefactor-cc-mcp-server.rs`: agent-facing tools; it must preserve the same authorization and privacy boundaries.
- `ORESoftware/k8s-cluster`: private cluster orchestration, browser workers, protected administration workflows, and deployment evidence.

## zed-pkg dependency direction

```text
benefactor-interfaces
        ↑
benefactor-automations

benefactor-interfaces ─┐
benefactor-sync ────────┼──> benefactor-gas
                       └──> guarded Gmail transport

benefactor-sendgrid-outreach
        └── consumes the same canonical eligibility and manifest boundary
```

Deployable applications and transports may depend on stable contracts and shared synchronization packages. Discovery code must not depend on a delivery transport. Lockfiles are committed; unresolved or mutable dependency state fails closed.

## Git and review conventions

- Include the Linear identifier in branch names, for example `agent/den-2490-consent-gated-gmail-transport`.
- PR titles and bodies must cite the issue and describe validation, rollback, privacy, consent, and data-retention effects.
- Resolve conflicts semantically: preserve current contracts, tested safety gates, immutable Action pins, and the complete intent of both branches.
- Merge only after required checks pass and unresolved review threads are closed.
- Keep contact data and secrets out of source and collaboration systems even when a repository is private.

## Current execution chain

1. DEN-260 owns the discovery and pre-outreach foundation.
2. DEN-833 remains the campaign-control parent for approved contacts and staged execution.
3. DEN-2490 provisions and implements `benefactor-gas` as a second guarded transport.
4. No Gmail or SendGrid bulk run is complete until the exact reviewed manifest, canary results, delivery/reply reconciliation, and final counts are attached to DEN-833 without exposing contact data.
