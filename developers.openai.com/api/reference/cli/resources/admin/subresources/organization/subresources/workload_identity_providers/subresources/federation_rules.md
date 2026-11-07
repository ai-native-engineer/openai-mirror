<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/ -->

# Federation Rules

## Create Platform workload identity federation rule

`$ openai admin:organization:workload-identity-providers:federation-rules create`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

### Parameters

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--attribute-matchers: map[string or boolean or number or number]`

- `--project-id: string`

  `minLength: 1`

- `--service-account-id: string`

  `minLength: 1`

- `--description: optional string`

- `--enabled: optional boolean`

- `--name: optional string`

- `--permissions: optional object { type }  or object { scopes, type }`

### Returns

- `federation_rule: object { id, attribute_matchers, created_at, 9 more }`

  - `id: string`

  - `attribute_matchers: map[string or boolean or number or number]`

    - `union_member_0: string`

    - `union_member_1: boolean`

    - `union_member_2: number or number`

      - `union_member_0: number`

      - `union_member_1: number`

  - `created_at: number`

  - `description: string`

  - `enabled: boolean`

  - `name: string`

  - `object: "organization.workload_identity_federation_rule"`

  - `permissions: object { type }  or object { scopes, type }`

    - `service_account_default: object { type }`

    - `restricted: object { scopes, type }`

      - `scopes: array of string`

      - `type: "restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Example

```cli
openai admin:organization:workload-identity-providers:federation-rules create \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x \
  --attribute-matchers '{foo: string}' \
  --project-id x \
  --service-account-id x
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

`$ openai admin:organization:workload-identity-providers:federation-rules delete`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

### Parameters

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--workload-identity-federation-rule-id: string`

  `minLength: 1`

### Returns

- `federation_rule_deleted: object { id, deleted, object }`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.workload_identity_federation_rule.deleted"`

### Example

```cli
openai admin:organization:workload-identity-providers:federation-rules delete \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x \
  --workload-identity-federation-rule-id x
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

`$ openai admin:organization:workload-identity-providers:federation-rules list`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

### Parameters

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--after: optional string`

  `minLength: 1`

- `--limit: optional number`

  `minimum: 1`, `maximum: 100`

- `--order: optional "asc" or "desc"`

- `--service-account-id: optional string`

  `minLength: 1`

### Returns

- `PlatformFederationRuleListResource: object { data, first_id, has_more, 2 more }`

  - `data: array of FederationRule`

    - `id: string`

    - `attribute_matchers: map[string or boolean or number or number]`

      - `union_member_0: string`

      - `union_member_1: boolean`

      - `union_member_2: number or number`

        - `union_member_0: number`

        - `union_member_1: number`

    - `created_at: number`

    - `description: string`

    - `enabled: boolean`

    - `name: string`

    - `object: "organization.workload_identity_federation_rule"`

    - `permissions: object { type }  or object { scopes, type }`

      - `service_account_default: object { type }`

      - `restricted: object { scopes, type }`

        - `scopes: array of string`

        - `type: "restricted"`

    - `project_id: string`

    - `service_account_id: string`

    - `updated_at: number`

    - `workload_identity_provider_id: string`

  - `first_id: string`

  - `has_more: boolean`

  - `last_id: string`

  - `object: "list"`

### Example

```cli
openai admin:organization:workload-identity-providers:federation-rules list \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x
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

`$ openai admin:organization:workload-identity-providers:federation-rules retrieve`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Retrieve a federation rule owned by the authenticated organization and provider.

### Parameters

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--workload-identity-federation-rule-id: string`

  `minLength: 1`

### Returns

- `federation_rule: object { id, attribute_matchers, created_at, 9 more }`

  - `id: string`

  - `attribute_matchers: map[string or boolean or number or number]`

    - `union_member_0: string`

    - `union_member_1: boolean`

    - `union_member_2: number or number`

      - `union_member_0: number`

      - `union_member_1: number`

  - `created_at: number`

  - `description: string`

  - `enabled: boolean`

  - `name: string`

  - `object: "organization.workload_identity_federation_rule"`

  - `permissions: object { type }  or object { scopes, type }`

    - `service_account_default: object { type }`

    - `restricted: object { scopes, type }`

      - `scopes: array of string`

      - `type: "restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Example

```cli
openai admin:organization:workload-identity-providers:federation-rules retrieve \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x \
  --workload-identity-federation-rule-id x
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

`$ openai admin:organization:workload-identity-providers:federation-rules update`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

### Parameters

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--workload-identity-federation-rule-id: string`

  `minLength: 1`

- `--attribute-matchers: optional map[string or boolean or number or number]`

- `--description: optional string`

- `--enabled: optional boolean`

- `--name: optional string`

- `--permissions: optional object { type }  or object { scopes, type }`

### Returns

- `federation_rule: object { id, attribute_matchers, created_at, 9 more }`

  - `id: string`

  - `attribute_matchers: map[string or boolean or number or number]`

    - `union_member_0: string`

    - `union_member_1: boolean`

    - `union_member_2: number or number`

      - `union_member_0: number`

      - `union_member_1: number`

  - `created_at: number`

  - `description: string`

  - `enabled: boolean`

  - `name: string`

  - `object: "organization.workload_identity_federation_rule"`

  - `permissions: object { type }  or object { scopes, type }`

    - `service_account_default: object { type }`

    - `restricted: object { scopes, type }`

      - `scopes: array of string`

      - `type: "restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Example

```cli
openai admin:organization:workload-identity-providers:federation-rules update \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x \
  --workload-identity-federation-rule-id x
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

- `federation_rule: object { id, attribute_matchers, created_at, 9 more }`

  - `id: string`

  - `attribute_matchers: map[string or boolean or number or number]`

    - `union_member_0: string`

    - `union_member_1: boolean`

    - `union_member_2: number or number`

      - `union_member_0: number`

      - `union_member_1: number`

  - `created_at: number`

  - `description: string`

  - `enabled: boolean`

  - `name: string`

  - `object: "organization.workload_identity_federation_rule"`

  - `permissions: object { type }  or object { scopes, type }`

    - `service_account_default: object { type }`

    - `restricted: object { scopes, type }`

      - `scopes: array of string`

      - `type: "restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Federation Rule Deleted

- `federation_rule_deleted: object { id, deleted, object }`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.workload_identity_federation_rule.deleted"`
