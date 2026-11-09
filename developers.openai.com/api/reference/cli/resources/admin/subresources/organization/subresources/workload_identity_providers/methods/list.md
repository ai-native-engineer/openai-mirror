<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/list/ -->

## List Platform workload identity providers

`$ openai admin:organization:workload-identity-providers list`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

- `--after: optional string`

  `minLength: 1`

- `--limit: optional number`

  `minimum: 1`, `maximum: 100`

- `--order: optional "asc" or "desc"`

- `PlatformProviderListResource: object { data, first_id, has_more, 2 more }`

  - `data: array of WorkloadIdentityProvider`

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

  - `first_id: string`

  - `has_more: boolean`

  - `last_id: string`

  - `object: "list"`

```cli
openai admin:organization:workload-identity-providers list \
  --admin-api-key 'My Admin API Key'

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
