<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/ -->

# Federation Rules

## Create Platform workload identity federation rule

`client.admin.organization.workloadIdentityProviders.federationRules.create(stringworkloadIdentityProviderID, FederationRuleCreateParamsbody, RequestOptionsoptions?): FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

### Parameters

- `workloadIdentityProviderID: string`

  `minLength: 1`

- `body: FederationRuleCreateParams`

  - `attribute_matchers: Record<string, string | boolean | number | number>`

    - `string`

    - `boolean`

    - `number | number`

      - `number`

      - `number`

  - `project_id: string`

    `minLength: 1`

  - `service_account_id: string`

    `minLength: 1`

  - `description?: string`

  - `enabled?: boolean`

  - `name?: string`

  - `permissions?: ServiceAccountDefault | Restricted`

    - `ServiceAccountDefault`

      - `type: "service_account_default"`

        - `"service_account_default"`

    - `Restricted`

      - `scopes: Array<string>`

        `minItems: 1`

      - `type: "restricted"`

        - `"restricted"`

### Returns

- `FederationRule`

  - `id: string`

  - `attribute_matchers: Record<string, string | boolean | number | number>`

    - `string`

    - `boolean`

    - `number | number`

      - `number`

      - `number`

  - `created_at: number`

  - `description: string | null`

  - `enabled: boolean`

  - `name: string | null`

  - `object: "organization.workload_identity_federation_rule"`

    - `"organization.workload_identity_federation_rule"`

  - `permissions: ServiceAccountDefault | Restricted`

    - `ServiceAccountDefault`

      - `type: "service_account_default"`

        - `"service_account_default"`

    - `Restricted`

      - `scopes: Array<string>`

      - `type: "restricted"`

        - `"restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const federationRule =
  await client.admin.organization.workloadIdentityProviders.federationRules.create('x', {
    attribute_matchers: { foo: 'string' },
    project_id: 'x',
    service_account_id: 'x',
  });

console.log(federationRule.id);
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

`client.admin.organization.workloadIdentityProviders.federationRules.delete(stringworkloadIdentityFederationRuleID, FederationRuleDeleteParamsparams, RequestOptionsoptions?): FederationRuleDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

### Parameters

- `workloadIdentityFederationRuleID: string`

  `minLength: 1`

- `params: FederationRuleDeleteParams`

  - `workload_identity_provider_id: string`

    `minLength: 1`

### Returns

- `FederationRuleDeleted`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.workload_identity_federation_rule.deleted"`

    - `"organization.workload_identity_federation_rule.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const federationRuleDeleted =
  await client.admin.organization.workloadIdentityProviders.federationRules.delete('x', {
    workload_identity_provider_id: 'x',
  });

console.log(federationRuleDeleted.id);
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

`client.admin.organization.workloadIdentityProviders.federationRules.list(stringworkloadIdentityProviderID, FederationRuleListParamsquery?, RequestOptionsoptions?): CursorPage<FederationRule>`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

### Parameters

- `workloadIdentityProviderID: string`

  `minLength: 1`

- `query: FederationRuleListParams`

  - `after?: string`

    `minLength: 1`

  - `limit?: number`

    `minimum: 1`, `maximum: 100`

  - `order?: "asc" | "desc"`

    - `"asc" | "desc"`

      - `"asc"`

      - `"desc"`

  - `service_account_id?: string`

    `minLength: 1`

### Returns

- `FederationRule`

  - `id: string`

  - `attribute_matchers: Record<string, string | boolean | number | number>`

    - `string`

    - `boolean`

    - `number | number`

      - `number`

      - `number`

  - `created_at: number`

  - `description: string | null`

  - `enabled: boolean`

  - `name: string | null`

  - `object: "organization.workload_identity_federation_rule"`

    - `"organization.workload_identity_federation_rule"`

  - `permissions: ServiceAccountDefault | Restricted`

    - `ServiceAccountDefault`

      - `type: "service_account_default"`

        - `"service_account_default"`

    - `Restricted`

      - `scopes: Array<string>`

      - `type: "restricted"`

        - `"restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const federationRule of client.admin.organization.workloadIdentityProviders.federationRules.list(
  'x',
)) {
  console.log(federationRule.id);
}
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

`client.admin.organization.workloadIdentityProviders.federationRules.retrieve(stringworkloadIdentityFederationRuleID, FederationRuleRetrieveParamsparams, RequestOptionsoptions?): FederationRule`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Retrieve a federation rule owned by the authenticated organization and provider.

### Parameters

- `workloadIdentityFederationRuleID: string`

  `minLength: 1`

- `params: FederationRuleRetrieveParams`

  - `workload_identity_provider_id: string`

    `minLength: 1`

### Returns

- `FederationRule`

  - `id: string`

  - `attribute_matchers: Record<string, string | boolean | number | number>`

    - `string`

    - `boolean`

    - `number | number`

      - `number`

      - `number`

  - `created_at: number`

  - `description: string | null`

  - `enabled: boolean`

  - `name: string | null`

  - `object: "organization.workload_identity_federation_rule"`

    - `"organization.workload_identity_federation_rule"`

  - `permissions: ServiceAccountDefault | Restricted`

    - `ServiceAccountDefault`

      - `type: "service_account_default"`

        - `"service_account_default"`

    - `Restricted`

      - `scopes: Array<string>`

      - `type: "restricted"`

        - `"restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const federationRule =
  await client.admin.organization.workloadIdentityProviders.federationRules.retrieve('x', {
    workload_identity_provider_id: 'x',
  });

console.log(federationRule.id);
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

`client.admin.organization.workloadIdentityProviders.federationRules.update(stringworkloadIdentityFederationRuleID, FederationRuleUpdateParamsparams, RequestOptionsoptions?): FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

### Parameters

- `workloadIdentityFederationRuleID: string`

  `minLength: 1`

- `params: FederationRuleUpdateParams`

  - `workload_identity_provider_id: string`

    Path param

    `minLength: 1`

  - `attribute_matchers?: Record<string, string | boolean | number | number>`

    Body param

    - `string`

    - `boolean`

    - `number | number`

      - `number`

      - `number`

  - `description?: string | null`

    Body param

  - `enabled?: boolean`

    Body param

  - `name?: string | null`

    Body param

  - `permissions?: DefaultPermissionsParam | RestrictedPermissionsParam`

    Body param

    - `DefaultPermissionsParam`

      - `type: "service_account_default"`

        - `"service_account_default"`

    - `RestrictedPermissionsParam`

      - `scopes: Array<string>`

        `minItems: 1`

      - `type: "restricted"`

        - `"restricted"`

### Returns

- `FederationRule`

  - `id: string`

  - `attribute_matchers: Record<string, string | boolean | number | number>`

    - `string`

    - `boolean`

    - `number | number`

      - `number`

      - `number`

  - `created_at: number`

  - `description: string | null`

  - `enabled: boolean`

  - `name: string | null`

  - `object: "organization.workload_identity_federation_rule"`

    - `"organization.workload_identity_federation_rule"`

  - `permissions: ServiceAccountDefault | Restricted`

    - `ServiceAccountDefault`

      - `type: "service_account_default"`

        - `"service_account_default"`

    - `Restricted`

      - `scopes: Array<string>`

      - `type: "restricted"`

        - `"restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const federationRule =
  await client.admin.organization.workloadIdentityProviders.federationRules.update('x', {
    workload_identity_provider_id: 'x',
  });

console.log(federationRule.id);
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

- `FederationRule`

  - `id: string`

  - `attribute_matchers: Record<string, string | boolean | number | number>`

    - `string`

    - `boolean`

    - `number | number`

      - `number`

      - `number`

  - `created_at: number`

  - `description: string | null`

  - `enabled: boolean`

  - `name: string | null`

  - `object: "organization.workload_identity_federation_rule"`

    - `"organization.workload_identity_federation_rule"`

  - `permissions: ServiceAccountDefault | Restricted`

    - `ServiceAccountDefault`

      - `type: "service_account_default"`

        - `"service_account_default"`

    - `Restricted`

      - `scopes: Array<string>`

      - `type: "restricted"`

        - `"restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

### Federation Rule Deleted

- `FederationRuleDeleted`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.workload_identity_federation_rule.deleted"`

    - `"organization.workload_identity_federation_rule.deleted"`
