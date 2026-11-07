<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/ -->

# Federation Rules

## Create Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.create(workload_identity_provider_id, **kwargs) -> FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

### Parameters

- `workload_identity_provider_id: String`

  `minLength: 1`

- `attribute_matchers: Hash[Symbol, String | bool | Integer | Float]`

  - `String = String`

  - `UnionMember1 = bool`

  - `UnionMember2 = Integer | Float`

    - `Integer = Integer`

    - `Float = Float`

- `project_id: String`

  `minLength: 1`

- `service_account_id: String`

  `minLength: 1`

- `description: String`

- `enabled: bool`

- `name: String`

- `permissions: ServiceAccountDefault{ type} | Restricted{ scopes, type}`

  - `class ServiceAccountDefault`

    - `type: :service_account_default`

      - `:service_account_default`

  - `class Restricted`

    - `scopes: Array[String]`

      `minItems: 1`

    - `type: :restricted`

      - `:restricted`

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

federation_rule = openai.admin.organization.workload_identity_providers.federation_rules.create(
  "x",
  attribute_matchers: {foo: "string"},
  project_id: "x",
  service_account_id: "x"
)

puts(federation_rule)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Delete Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.delete(workload_identity_federation_rule_id, **kwargs) -> FederationRuleDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

### Parameters

- `workload_identity_provider_id: String`

  `minLength: 1`

- `workload_identity_federation_rule_id: String`

  `minLength: 1`

### Returns

- `class FederationRuleDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.workload_identity_federation_rule.deleted"`

    - `:"organization.workload_identity_federation_rule.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

federation_rule_deleted = openai.admin.organization.workload_identity_providers.federation_rules.delete(
  "x",
  workload_identity_provider_id: "x"
)

puts(federation_rule_deleted)
```

#### 200 — Example

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"
}
```

## List Platform workload identity federation rules

`admin.organization.workload_identity_providers.federation_rules.list(workload_identity_provider_id, **kwargs) -> CursorPage<FederationRule>`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

### Parameters

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

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.workload_identity_providers.federation_rules.list("x")

puts(page)
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "attribute_matchers": {
        "foo": "string"
      },
      "created_at": 0,
      "description": "description",
      "enabled": true,
      "name": "name",
      "object": "organization.workload_identity_federation_rule",
      "permissions": {
        "type": "service_account_default"
      },
      "project_id": "project_id",
      "service_account_id": "service_account_id",
      "updated_at": 0,
      "workload_identity_provider_id": "workload_identity_provider_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.retrieve(workload_identity_federation_rule_id, **kwargs) -> FederationRule`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Retrieve a federation rule owned by the authenticated organization and provider.

### Parameters

- `workload_identity_provider_id: String`

  `minLength: 1`

- `workload_identity_federation_rule_id: String`

  `minLength: 1`

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

federation_rule = openai.admin.organization.workload_identity_providers.federation_rules.retrieve(
  "x",
  workload_identity_provider_id: "x"
)

puts(federation_rule)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Update Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.update(workload_identity_federation_rule_id, **kwargs) -> FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

### Parameters

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

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

federation_rule = openai.admin.organization.workload_identity_providers.federation_rules.update(
  "x",
  workload_identity_provider_id: "x"
)

puts(federation_rule)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Domain Types

### Federation Rule

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

### Federation Rule Deleted

- `class FederationRuleDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.workload_identity_federation_rule.deleted"`

    - `:"organization.workload_identity_federation_rule.deleted"`
