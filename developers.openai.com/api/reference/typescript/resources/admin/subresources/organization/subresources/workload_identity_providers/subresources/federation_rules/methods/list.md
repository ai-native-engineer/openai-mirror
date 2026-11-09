<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/list/ -->

## List Platform workload identity federation rules

`client.admin.organization.workloadIdentityProviders.federationRules.list(stringworkloadIdentityProviderID, FederationRuleListParamsquery?, RequestOptionsoptions?): CursorPage<FederationRule>`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

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

// Automatically fetches more pages as needed.
for await (const federationRule of client.admin.organization.workloadIdentityProviders.federationRules.list(
  'x',
)) {
  console.log(federationRule.id);

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
