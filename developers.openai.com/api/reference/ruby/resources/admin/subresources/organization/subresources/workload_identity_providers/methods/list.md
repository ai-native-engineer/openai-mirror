<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/list/ -->

## List Platform workload identity providers

`admin.organization.workload_identity_providers.list(**kwargs) -> CursorPage<WorkloadIdentityProvider>`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

- `after: String`

  `minLength: 1`

- `limit: Integer`

  `minimum: 1`, `maximum: 100`

- `order: :asc | :desc`

  - `Order = :asc | :desc`

    - `:asc`

    - `:desc`

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

page = openai.admin.organization.workload_identity_providers.list

puts(page)

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
