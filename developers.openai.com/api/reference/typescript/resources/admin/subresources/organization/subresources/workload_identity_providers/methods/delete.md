<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/delete/ -->

## Delete Platform workload identity provider

`client.admin.organization.workloadIdentityProviders.delete(stringworkloadIdentityProviderID, RequestOptionsoptions?): WorkloadIdentityProviderDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

- `workloadIdentityProviderID: string`

  `minLength: 1`

- `WorkloadIdentityProviderDeleted`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.workload_identity_provider.deleted"`

    - `"organization.workload_identity_provider.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const workloadIdentityProviderDeleted =
  await client.admin.organization.workloadIdentityProviders.delete('x');

console.log(workloadIdentityProviderDeleted.id);

  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"
