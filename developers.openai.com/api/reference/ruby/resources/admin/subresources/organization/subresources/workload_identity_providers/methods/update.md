<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/update/ -->

## Update Platform workload identity provider

`admin.organization.workload_identity_providers.update(workload_identity_provider_id, **kwargs) -> WorkloadIdentityProvider`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

- `workload_identity_provider_id: String`

  `minLength: 1`

- `attribute_transformations: Array[AttributeTransformation{ attribute, expression}]`

  `maxItems: 20`

  - `attribute: String`

    `minLength: 1`, `maxLength: 256`

  - `expression: String`

    `minLength: 1`, `maxLength: 4096`

- `audience: String`

  `minLength: 1`

- `description: String`

- `enabled: bool`

- `issuer: String`

  `minLength: 1`

- `name: String`

  `minLength: 1`

- `verification: DiscoveryVerificationParam{ discovery_url, type} | UploadedJwksVerificationParam{ jwks, type}`

  - `class DiscoveryVerificationParam`

    - `discovery_url: String`

    - `type: :discovery`

      - `:discovery`

  - `class UploadedJwksVerificationParam`

    - `jwks: Hash[Symbol, untyped]`

    - `type: :uploaded_jwks`

      - `:uploaded_jwks`

- `class WorkloadIdentityProvider`

  - `id: String`

  - `attribute_transformations: Array[AttributeTransformation{ attribute, expression}]`

    - `attribute: String`

    - `expression: String`

  - `audience: String`

  - `created_at: Integer`

  - `description: String`

  - `enabled: bool`

  - `issuer: String`

  - `name: String`

  - `object: :"organization.workload_identity_provider"`

    - `:"organization.workload_identity_provider"`

  - `type: :oidc`

    - `:oidc`

  - `updated_at: Integer`

  - `verification: Discovery{ discovery_url, type} | UploadedJwks{ jwks, type}`

    - `class Discovery`

      - `discovery_url: String`

      - `type: :discovery`

        - `:discovery`

    - `class UploadedJwks`

      - `jwks: Hash[Symbol, untyped]`

      - `type: :uploaded_jwks`

        - `:uploaded_jwks`

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

workload_identity_provider = openai.admin.organization.workload_identity_providers.update("x")

puts(workload_identity_provider)

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
