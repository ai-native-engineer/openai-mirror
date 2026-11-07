<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/update/ -->

## Update Platform workload identity provider

`$ openai admin:organization:workload-identity-providers update`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--attribute-transformation: optional array of object { attribute, expression }`

  `maxItems: 20`

- `--audience: optional string`

  `minLength: 1`

- `--description: optional string`

- `--enabled: optional boolean`

- `--issuer: optional string`

  `minLength: 1`

- `--name: optional string`

  `minLength: 1`

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
openai admin:organization:workload-identity-providers update \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x

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
