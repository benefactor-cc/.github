# benefactor-cc organization defaults

This public `.github` repository contains organization-wide community health files, contributor guidance, shared agent policy, and an explicit repository-relationship contract.

See [`PROJECT_AND_REPOSITORY_MAP.md`](PROJECT_AND_REPOSITORY_MAP.md) for the Linear/GitHub source-of-truth model, repository ownership, outreach safety boundaries, and zed-pkg dependency direction.

Repository-local policy wins when it is stricter or more specific. Existing project history must be preserved during consolidation and conflict resolution.

<!-- ore-org-baseline:begin -->
## Organization-wide defaults

This public repository is the canonical source for GitHub-supported community-health fallbacks, organization profile content, contribution guidance, public security/support policy, issue and pull-request templates, and agent-governance declarations for [`benefactor-cc`](https://github.com/benefactor-cc).

## Canonical organization links

- GitHub organization: https://github.com/benefactor-cc
- Public organization defaults: https://github.com/benefactor-cc/.github
- Canonical Linear project: https://linear.app/denman/project/githubcombenefactor-cc-6bef502a1ef0
- Fleet tracking issue: https://github.com/ORESoftware/k8s-cluster/issues/1222

## Safety baseline

All Git conflicts must be resolved semantically with full historical, repository-wide, organization-wide, and relevant external-organization context. Automated agents are hard-denied from destructive or history-rewriting operations, including all forms of `git stash`, `git reset`, `git clean`, `git filter-repo`, force pushing, destructive deletion, data or infrastructure teardown, credential revocation, and policy bypass.

## GitHub inheritance boundary

GitHub can use supported community-health files from a public organization `.github` repository as fallbacks and can render `profile/README.md` on the organization page. `agents.md`, `AGENTS.md`, Copilot instructions, workflows, settings, rulesets, branch protections, permissions, and secrets are not automatically inherited merely because they exist here. Each repository must carry or synchronize compatible local policy and explicitly call reusable workflows where enforcement is required.

Generated managed-policy version: `2026-08-08`.
<!-- ore-org-baseline:end -->
