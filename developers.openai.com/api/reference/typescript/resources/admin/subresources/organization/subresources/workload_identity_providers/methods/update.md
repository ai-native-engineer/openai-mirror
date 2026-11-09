<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/update/ -->

## Update Platform workload identity provider

`client.admin.organization.workloadIdentityProviders.update(stringworkloadIdentityProviderID, WorkloadIdentityProviderUpdateParamsbody?, RequestOptionsoptions?): WorkloadIdentityProvider`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

- `workloadIdentityProviderID: string`

  `minLength: 1`

- `body: WorkloadIdentityProviderUpdateParams`

  - `attribute_transformations?: Array<AttributeTransformation>`

    `maxItems: 20`

    - `attribute: string`

      `minLength: 1`, `maxLength: 256`

    - `expression: string`

      `minLength: 1`, `maxLength: 4096`

  - `audience?: string`

    `minLength: 1`

  - `description?: string | null`

  - `enabled?: boolean`

  - `issuer?: string`

    `minLength: 1`

  - `name?: string`

    `minLength: 1`

  - `verification?: DiscoveryVerificationParam | UploadedJwksVerificationParam`

    - `DiscoveryVerificationParam`

      - `discovery_url: string | null`

      - `type: "discovery"`

        - `"discovery"`

    - `UploadedJwksVerificationParam`

      - `jwks: Record<string, unknown>`

      - `type: "uploaded_jwks"`

        - `"uploaded_jwks"`

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

const workloadIdentityProvider = await client.admin.organization.workloadIdentityProviders.update(
  'x',
);

console.log(workloadIdentityProvider.id);

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
