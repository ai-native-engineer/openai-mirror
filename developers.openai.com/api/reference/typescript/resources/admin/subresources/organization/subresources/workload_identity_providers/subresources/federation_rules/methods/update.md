<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/update/ -->

## Update Platform workload identity federation rule

`client.admin.organization.workloadIdentityProviders.federationRules.update(stringworkloadIdentityFederationRuleID, FederationRuleUpdateParamsparams, RequestOptionsoptions?): FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

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
  await client.admin.organization.workloadIdentityProviders.federationRules.update('x', {
    workload_identity_provider_id: 'x',
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
