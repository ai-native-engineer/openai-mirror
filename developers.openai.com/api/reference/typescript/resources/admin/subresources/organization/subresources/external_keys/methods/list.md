<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/external_keys/methods/list/ -->

## List the external key configs registered on the user's organization

`client.admin.organization.externalKeys.list(ExternalKeyListParamsquery?, RequestOptionsoptions?): CursorPage<ExternalKey>`

**get** `/organization/external_keys`

List the external key configs registered on the user's organization

- `query: ExternalKeyListParams`

  - `after?: string | null`

  - `limit?: number`

    `minimum: 0`, `maximum: 100`

  - `order?: "asc" | "desc"`

    - `"asc"`

    - `"desc"`

  - `purpose?: "ekm" | "psp_decryption"`

    Filter by key purpose. When omitted, returns keys of all purposes.

    - `"ekm"`

    - `"psp_decryption"`

- `ExternalKey`

  - `id: string`

  - `api_project_ids: Array<string>`

  - `created_at: number`

  - `name: string`

  - `object: string`

  - `type: string`

  - `workspace_id: string`

  - `audience?: string`

  - `external_id?: string`

  - `key_name?: string`

  - `key_version?: string`

  - `kms_arn?: string`

  - `kms_key_location?: string`

  - `kms_key_name?: string`

  - `kms_key_ring_name?: string`

  - `kms_key_version?: string`

  - `kms_project_id?: string`

  - `purpose?: "ekm" | "psp_decryption"`

    - `"ekm"`

    - `"psp_decryption"`

  - `role_arn?: string`

  - `tenant_id?: string`

  - `vault_uri?: string`

  - `workload_identity_pool_id?: string`

  - `workload_identity_project_number?: string`

  - `workload_identity_provider_id?: string`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const externalKey of client.admin.organization.externalKeys.list()) {
  console.log(externalKey.id);

  "data": [
      "api_project_ids": [
        "string"
      "object": "object",
      "type": "type",
      "workspace_id": "workspace_id",
      "audience": "audience",
      "external_id": "external_id",
      "key_name": "key_name",
      "key_version": "key_version",
      "kms_arn": "kms_arn",
      "kms_key_location": "kms_key_location",
      "kms_key_name": "kms_key_name",
      "kms_key_ring_name": "kms_key_ring_name",
      "kms_key_version": "kms_key_version",
      "kms_project_id": "kms_project_id",
      "purpose": "ekm",
      "role_arn": "role_arn",
      "tenant_id": "tenant_id",
      "vault_uri": "vault_uri",
      "workload_identity_pool_id": "workload_identity_pool_id",
      "workload_identity_project_number": "workload_identity_project_number",
      "workload_identity_provider_id": "workload_identity_provider_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
