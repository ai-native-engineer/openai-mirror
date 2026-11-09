<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/workload_identity_providers/ -->

# Workload Identity Providers

## Create Platform workload identity provider

`admin.organization.workload_identity_providers.create(**kwargs) -> WorkloadIdentityProvider`

**post** `/organization/workload_identity_providers`

Register an OIDC provider for keyless project service-account authentication.

### Parameters

- `audience: String`

  `minLength: 1`

- `issuer: String`

  `minLength: 1`

- `name: String`

  `minLength: 1`

- `type: :oidc`

  - `:oidc`

- `attribute_transformations: Array[AttributeTransformation{ attribute, expression}]`

  `maxItems: 20`

  - `attribute: String`

    `minLength: 1`, `maxLength: 256`

  - `expression: String`

    `minLength: 1`, `maxLength: 4096`

- `description: String`

- `enabled: bool`

- `verification: Discovery{ discovery_url, type} | UploadedJwks{ jwks, type}`

  - `class Discovery`

    - `discovery_url: String`

    - `type: :discovery`

      - `:discovery`

  - `class UploadedJwks`

    - `jwks: Hash[Symbol, untyped]`

    - `type: :uploaded_jwks`

      - `:uploaded_jwks`

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

workload_identity_provider = openai.admin.organization.workload_identity_providers.create(
  audience: "x",
  issuer: "x",
  name: "x",
  type: :oidc
)

puts(workload_identity_provider)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Delete Platform workload identity provider

`admin.organization.workload_identity_providers.delete(workload_identity_provider_id) -> WorkloadIdentityProviderDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

### Parameters

- `workload_identity_provider_id: String`

  `minLength: 1`

### Returns

- `class WorkloadIdentityProviderDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.workload_identity_provider.deleted"`

    - `:"organization.workload_identity_provider.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

workload_identity_provider_deleted = openai.admin.organization.workload_identity_providers.delete("x")

puts(workload_identity_provider_deleted)
```

#### 200 — Example

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"
}
```

## List Platform workload identity providers

`admin.organization.workload_identity_providers.list(**kwargs) -> CursorPage<WorkloadIdentityProvider>`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

### Parameters

- `after: String`

  `minLength: 1`

- `limit: Integer`

  `minimum: 1`, `maximum: 100`

- `order: :asc | :desc`

  - `Order = :asc | :desc`

    - `:asc`

    - `:desc`

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.workload_identity_providers.list

puts(page)
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "attribute_transformations": [
        {
          "attribute": "attribute",
          "expression": "expression"
        }
      ],
      "audience": "audience",
      "created_at": 0,
      "description": "description",
      "enabled": true,
      "issuer": "issuer",
      "name": "name",
      "object": "organization.workload_identity_provider",
      "type": "oidc",
      "updated_at": 0,
      "verification": {
        "discovery_url": "discovery_url",
        "type": "discovery"
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve Platform workload identity provider

`admin.organization.workload_identity_providers.retrieve(workload_identity_provider_id) -> WorkloadIdentityProvider`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Retrieve an OIDC provider in the authenticated organization.

### Parameters

- `workload_identity_provider_id: String`

  `minLength: 1`

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

workload_identity_provider = openai.admin.organization.workload_identity_providers.retrieve("x")

puts(workload_identity_provider)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Update Platform workload identity provider

`admin.organization.workload_identity_providers.update(workload_identity_provider_id, **kwargs) -> WorkloadIdentityProvider`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

### Parameters

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

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

workload_identity_provider = openai.admin.organization.workload_identity_providers.update("x")

puts(workload_identity_provider)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Domain Types

### Workload Identity Provider

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

### Workload Identity Provider Deleted

- `class WorkloadIdentityProviderDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.workload_identity_provider.deleted"`

    - `:"organization.workload_identity_provider.deleted"`

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
