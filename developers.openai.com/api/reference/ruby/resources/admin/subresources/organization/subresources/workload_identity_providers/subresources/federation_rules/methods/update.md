<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/update/ -->

## Update Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.update(workload_identity_federation_rule_id, **kwargs) -> FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

- `workload_identity_provider_id: String`

  `minLength: 1`

- `workload_identity_federation_rule_id: String`

  `minLength: 1`

- `attribute_matchers: Hash[Symbol, String | bool | Integer | Float]`

  - `String = String`

  - `UnionMember1 = bool`

  - `UnionMember2 = Integer | Float`

    - `Integer = Integer`

    - `Float = Float`

- `description: String`

- `enabled: bool`

- `name: String`

- `permissions: DefaultPermissionsParam{ type} | RestrictedPermissionsParam{ scopes, type}`

  - `class DefaultPermissionsParam`

    - `type: :service_account_default`

      - `:service_account_default`

  - `class RestrictedPermissionsParam`

    - `scopes: Array[String]`

      `minItems: 1`

    - `type: :restricted`

      - `:restricted`

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

federation_rule = openai.admin.organization.workload_identity_providers.federation_rules.update(
  "x",
  workload_identity_provider_id: "x"

puts(federation_rule)

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
