<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/external_keys/methods/retrieve/ -->

## Retrieve an external key registration

`client.admin.organization.externalKeys.retrieve(stringexternalKeyID, RequestOptionsoptions?): ExternalKey`

**get** `/organization/external_keys/{external_key_id}`

Retrieve a stored external key registration for the user's organization.

- `externalKeyID: string`

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

const externalKey = await client.admin.organization.externalKeys.retrieve('external_key_id');

console.log(externalKey.id);

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
