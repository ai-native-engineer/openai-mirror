<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/retrieve/ -->

> For the complete documentation index, see [llms.txt](/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

## Retrieve Platform workload identity provider

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Retrieve an OIDC provider in the authenticated organization.

### Path Parameters

- `workload_identity_provider_id: string`

  `minLength: 1`

- `WorkloadIdentityProvider object { id, attribute_transformations, audience, 9 more }`

  - `id: string`

  - `attribute_transformations: array of object { attribute, expression }`

    - `attribute: string`

    - `expression: string`

  - `audience: string`

  - `created_at: integer`

  - `description: string or null`

  - `enabled: boolean`

  - `issuer: string`

  - `name: string`

  - `object: "organization.workload_identity_provider" (default: "organization.workload_identity_provider")`

    - `"organization.workload_identity_provider"`

  - `type: "oidc" (default: "oidc")`

    - `"oidc"`

  - `updated_at: integer`

  - `verification: DiscoveryVerification { discovery_url, type }  or UploadedJwksVerification { jwks, type }`

    - `DiscoveryVerification object { discovery_url, type }`

      - `discovery_url: string or null`

      - `type: "discovery" (default: "discovery")`

        - `"discovery"`

    - `UploadedJwksVerification object { jwks, type }`

      - `jwks: map[unknown]`

      - `type: "uploaded_jwks" (default: "uploaded_jwks")`

        - `"uploaded_jwks"`

```http
curl https://api.openai.com/v1/organization/workload_identity_providers/$WORKLOAD_IDENTITY_PROVIDER_ID \
    -H "Authorization: Bearer $OPENAI_ADMIN_KEY"

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

```http
curl -X GET "https://api.openai.com/v1/organization/workload_identity_providers/wip_example" \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY"

#### Response example

  "object": "organization.workload_identity_provider",
  "id": "wip_example",
  "type": "oidc",
  "name": "CI provider",
  "issuer": "https://issuer.example.com",
  "audience": "openai",
  "verification": {
    "type": "discovery",
    "discovery_url": null
  "description": null,
  "attribute_transformations": [],
  "enabled": true,
  "created_at": 1793664000,
  "updated_at": 1793664000
