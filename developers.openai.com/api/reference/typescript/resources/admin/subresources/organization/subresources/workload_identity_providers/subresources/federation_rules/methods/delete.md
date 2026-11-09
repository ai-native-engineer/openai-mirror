<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/delete/ -->

## Delete Platform workload identity federation rule

`client.admin.organization.workloadIdentityProviders.federationRules.delete(stringworkloadIdentityFederationRuleID, FederationRuleDeleteParamsparams, RequestOptionsoptions?): FederationRuleDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

- `workloadIdentityFederationRuleID: string`

  `minLength: 1`

- `params: FederationRuleDeleteParams`

  - `workload_identity_provider_id: string`

    `minLength: 1`

- `FederationRuleDeleted`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.workload_identity_federation_rule.deleted"`

    - `"organization.workload_identity_federation_rule.deleted"`

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

  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"
