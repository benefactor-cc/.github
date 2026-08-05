# benefactor-cc organization handbook

> Shared operating defaults for repositories maintained under **benefactor-cc**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

benefactor-cc maintains customer, relationship, outreach, and operational automation software. This `.github` repository is the canonical home for organization-wide community health files, reusable templates, engineering policy, and planning links.

## Repository contract

Each active repository must document purpose, ownership, maturity, supported environments, development and test commands, authoritative schemas and integrations, release and rollback procedures, compatibility policy, and GitHub Project/Linear links. Customer-facing systems should also document consent and authorization, data provenance, deduplication, rate limits, provider constraints, human-review gates, retention, deletion, retries, and auditability.

## Change and review workflow

1. Anchor work in an issue, Linear item, or documented maintenance objective.
2. Keep branches and pull requests focused.
3. Explain motivation, scope, customer and data impact, abuse risk, validation, compatibility, migration, and rollback.
4. Test permission, duplicate, opt-out, rate-limit, retry, partial-failure, and deletion paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless commit structure materially improves auditability.

## Evidence and quality

Pull requests should include reproducible commands, synthetic or sanitized fixtures, expected and observed results, negative-path coverage, documentation updates, and CI or local-equivalent evidence. Integration changes require provider-policy and consumer impact analysis.

## Security and data

Never commit credentials, customer records, contact details, provider tokens, production identities, or sensitive logs. Use synthetic or irreversibly sanitized fixtures. Follow `SECURITY.md` for private vulnerability reporting and pin dependencies and actions where reproducibility or supply-chain integrity matters.

## Documentation and decisions

Keep examples executable and sanitized, links current, assumptions explicit, and data-flow boundaries clear. Record privacy, consent, retention, provider, compatibility, and operational decisions that future maintainers would otherwise have to rediscover.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profiles, descriptions, topics, and READMEs are current.
- [ ] Contribution, security, support, governance, issue, and PR guidance is present.
- [ ] Data provenance, authorization, retention, deletion, and opt-out behavior is documented.
- [ ] Required checks reflect privacy, abuse, integration, and supply-chain risk.
- [ ] Stale repositories are archived or clearly marked.
- [ ] Project links resolve and completed work is reflected in GitHub and Linear.
