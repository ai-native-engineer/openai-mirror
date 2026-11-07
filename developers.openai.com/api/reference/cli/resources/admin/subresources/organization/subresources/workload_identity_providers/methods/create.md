<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/create/ -->

## Create Platform workload identity provider

`$ openai admin:organization:workload-identity-providers create`

**post** `/organization/workload_identity_providers`

Register an OIDC provider for keyless project service-account authentication.

- `--audience: string`

  `minLength: 1`

- `--issuer: string`

  `minLength: 1`

- `--name: string`

  `minLength: 1`

- `--type: "oidc"`

- `--attribute-transformation: optional array of object { attribute, expression }`

  `maxItems: 20`

- `--description: optional string`

- `--enabled: optional boolean`

- `--verification: optional object { discovery_url, type }  or object { jwks, type }`

- `workload_identity_provider: object { id, attribute_transformations, audience, 9 more }`

  - `id: string`

  - `attribute_transformations: array of object { attribute, expression }`

    - `attribute: string`

    - `expression: string`

  - `audience: string`

  - `created_at: number`

  - `description: string`

  - `enabled: boolean`

  - `issuer: string`

  - `name: string`

  - `object: "organization.workload_identity_provider"`

  - `type: "oidc"`

  - `updated_at: number`

  - `verification: object { discovery_url, type }  or object { jwks, type }`

    - `discovery: object { discovery_url, type }`

      - `discovery_url: string`

      - `type: "discovery"`

    - `uploaded_jwks: object { jwks, type }`

      - `jwks: map[unknown]`

      - `type: "uploaded_jwks"`

```cli
openai admin:organization:workload-identity-providers create \
  --admin-api-key 'My Admin API Key' \
  --audience x \
  --issuer x \
  --name x \
  --type oidc

  "attribute_transformations": [
      "attribute": "attribute",
      "expression": "expression"
  "audience": "audience",
  "enabled": true,
  "issuer": "issuer",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
