<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/create/ -->

## Create Platform workload identity federation rule

`client.admin.organization.workloadIdentityProviders.federationRules.create(stringworkloadIdentityProviderID, FederationRuleCreateParamsbody, RequestOptionsoptions?): FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

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
