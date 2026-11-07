<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/list/ -->

## List Platform workload identity providers

`client.admin.organization.workloadIdentityProviders.list(WorkloadIdentityProviderListParamsquery?, RequestOptionsoptions?): CursorPage<WorkloadIdentityProvider>`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

- `query: WorkloadIdentityProviderListParams`

  - `after?: string`

    `minLength: 1`

  - `limit?: number`

    `minimum: 1`, `maximum: 100`

  - `order?: "asc" | "desc"`

    - `"asc" | "desc"`

      - `"asc"`

      - `"desc"`

- `WorkloadIdentityProvider`

  - `id: string`

  - `attribute_transformations: Array<AttributeTransformation>`

    - `attribute: string`

    - `expression: string`

  - `audience: string`

  - `created_at: number`

  - `description: string | null`

  - `enabled: boolean`

  - `issuer: string`

  - `name: string`

  - `object: "organization.workload_identity_provider"`

    - `"organization.workload_identity_provider"`

  - `type: "oidc"`

    - `"oidc"`

  - `updated_at: number`

  - `verification: Discovery | UploadedJwks`

    - `Discovery`

      - `discovery_url: string | null`

      - `type: "discovery"`

        - `"discovery"`

    - `UploadedJwks`

      - `jwks: Record<string, unknown>`

      - `type: "uploaded_jwks"`

        - `"uploaded_jwks"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const workloadIdentityProvider of client.admin.organization.workloadIdentityProviders.list(

)) {
  console.log(workloadIdentityProvider.id);

  "data": [
      "attribute_transformations": [
          "attribute": "attribute",
          "expression": "expression"
      "audience": "audience",
      "enabled": true,
      "issuer": "issuer",
      "object": "organization.workload_identity_provider",
      "type": "oidc",
      "updated_at": 0,
      "verification": {
        "discovery_url": "discovery_url",
        "type": "discovery"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
