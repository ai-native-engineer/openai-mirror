<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/list/ -->

## List Platform workload identity federation rules

`admin.organization.workload_identity_providers.federation_rules.list(workload_identity_provider_id, **kwargs) -> CursorPage<FederationRule>`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

- `workload_identity_provider_id: String`

  `minLength: 1`

- `after: String`

  `minLength: 1`

- `limit: Integer`

  `minimum: 1`, `maximum: 100`

- `order: :asc | :desc`

  - `Order = :asc | :desc`

    - `:asc`

    - `:desc`

- `service_account_id: String`

  `minLength: 1`

- `class FederationRule`

  - `id: String`

  - `attribute_matchers: Hash[Symbol, String | bool | Integer | Float]`

    - `String = String`

    - `UnionMember1 = bool`

    - `UnionMember2 = Integer | Float`

      - `Integer = Integer`

      - `Float = Float`

  - `created_at: Integer`

  - `description: String`

  - `enabled: bool`

  - `name: String`

  - `object: :"organization.workload_identity_federation_rule"`

    - `:"organization.workload_identity_federation_rule"`

  - `permissions: ServiceAccountDefault{ type} | Restricted{ scopes, type}`

    - `class ServiceAccountDefault`

      - `type: :service_account_default`

        - `:service_account_default`

    - `class Restricted`

      - `scopes: Array[String]`

      - `type: :restricted`

        - `:restricted`

  - `project_id: String`

  - `service_account_id: String`

  - `updated_at: Integer`

  - `workload_identity_provider_id: String`

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.workload_identity_providers.federation_rules.list("x")

puts(page)

  "data": [
      "attribute_matchers": {
        "foo": "string"
      "enabled": true,
      "object": "organization.workload_identity_federation_rule",
      "permissions": {
        "type": "service_account_default"
      "project_id": "project_id",
      "service_account_id": "service_account_id",
      "updated_at": 0,
      "workload_identity_provider_id": "workload_identity_provider_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
