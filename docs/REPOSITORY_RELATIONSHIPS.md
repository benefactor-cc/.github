<!-- ore-org-baseline:begin -->
# Repository relationships for `benefactor-cc`

This file is rendered from `repository-relationships.json`. The JSON registry is authoritative.

- Audience: `public`
- Repositories represented: **3**
- Relationships represented: **3**
- Inventory digest: `sha256:91a773469926499ddf4e3c3bf6016870a0e617543f36f5c023a471ef5cbc269a`

## Immutable routing identity

| Field | Value |
|---|---|
| Mapping ID | `context:benefactor-cc` |
| GitHub owner ID | `265349385` |
| Linear project ID | `e1db74d7-4fa3-4580-851d-ca8fc8145127` |
| Linear team ID | `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc` |

## Repositories

| Repository | Visibility | Roles | Archived |
|---|---|---|---|
| `benefactor-cc/.github` | `public` | `community-health`, `governance`, `relationship-registry` | no |
| `benefactor-cc/benefactor-cc.github.io` | `public` | `documentation-site` | no |
| `benefactor-cc/benfactor-cc` | `public` | `repository` | no |

## Relationships

| From | Type | To | Status | Required |
|---|---|---|---|---|
| `benefactor-cc/.github` | `governs` | `benefactor-cc/benefactor-cc.github.io` | `declared` | yes |
| `benefactor-cc/.github` | `governs` | `benefactor-cc/benfactor-cc` | `declared` | yes |
| `benefactor-cc/benefactor-cc.github.io` | `documents` | `benefactor-cc/.github` | `inferred` | no |

## Editing relationships

Put reviewed public declarations in `repository-relationships.manual.json`; do not edit the generated registry directly.
Private repository names and private-only relationships belong in the private `approved-private-registry` mirror.
Inferred edges are advisory and must remain visibly labeled until reviewed.
<!-- ore-org-baseline:end -->
