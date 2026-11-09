<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/external_keys/methods/retrieve/ -->

## Retrieve an external key registration

`$ openai admin:organization:external-keys retrieve`

**get** `/organization/external_keys/{external_key_id}`

Retrieve a stored external key registration for the user's organization.

- `--external-key-id: string`

- `external_key: object { id, api_project_ids, created_at, 21 more }`

  - `id: string`

  - `api_project_ids: array of string`

  - `created_at: number`

  - `name: string`

  - `object: string`

  - `type: string`

  - `workspace_id: string`

  - `audience: optional string`

  - `external_id: optional string`

  - `key_name: optional string`

  - `key_version: optional string`

  - `kms_arn: optional string`

  - `kms_key_location: optional string`

  - `kms_key_name: optional string`

  - `kms_key_ring_name: optional string`

  - `kms_key_version: optional string`

  - `kms_project_id: optional string`

  - `purpose: optional "ekm" or "psp_decryption"`

    - `"ekm"`

    - `"psp_decryption"`

  - `role_arn: optional string`

  - `tenant_id: optional string`

  - `vault_uri: optional string`

  - `workload_identity_pool_id: optional string`

  - `workload_identity_project_number: optional string`

  - `workload_identity_provider_id: optional string`

```cli
openai admin:organization:external-keys retrieve \
  --admin-api-key 'My Admin API Key' \
  --external-key-id external_key_id

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
