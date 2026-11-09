<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/external_keys/methods/list/ -->

## List the external key configs registered on the user's organization

`$ openai admin:organization:external-keys list`

**get** `/organization/external_keys`

List the external key configs registered on the user's organization

- `--after: optional string`

- `--limit: optional number`

  `minimum: 0`, `maximum: 100`

- `--order: optional "asc" or "desc"`

- `--purpose: optional "ekm" or "psp_decryption"`

  Filter by key purpose. When omitted, returns keys of all purposes.

- `ListExternalKeysResource: object { data, first_id, has_more, 2 more }`

  - `data: array of ExternalKey`

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

  - `first_id: string`

  - `has_more: boolean`

  - `last_id: string`

  - `object: "list"`

```cli
openai admin:organization:external-keys list \
  --admin-api-key 'My Admin API Key'

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
