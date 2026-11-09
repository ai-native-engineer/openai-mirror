<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/external_keys/ -->

# External Keys

## Add an external key config for an organization

`$ openai admin:organization:external-keys create`

**post** `/organization/external_keys`

Add an external key config for an organization

### Parameters

- `--external-id: string`

  The ExternalID that OpenAI will pass in the AssumeRole call for the customer's AWS account. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

- `--kms-arn: string`

  The Key Management System ARN for the master key you manage

- `--name: string`

  A friendly name to identify this config

- `--role-arn: string`

  The Role ARN that OpenAI will assume to call your KMS

- `--type: "aws" or "gcp" or "azure"`

- `--purpose: optional "ekm" or "psp_decryption"`

- `--audience: string`

  The aud field in the identity token OpenAI will pass in the call to the customer's GCP STS. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

- `--kms-key-location: string`

  The region where your Key Management System master key is located

- `--kms-key-name: string`

  The name of the Key Management System master key you manage

- `--kms-key-ring-name: string`

  The Key Management System key ring for the master key you manage

- `--kms-project-id: string`

  The string GCP project name where your KMS resides

- `--workload-identity-pool-id: string`

  The pool containing the Workload Identity provider that you registered for OpenAI

- `--workload-identity-project-number: string`

  The numeric GCP project number where you registered OpenAI's workload identity

- `--workload-identity-provider-id: string`

  The Workload Identity provider that you registered for OpenAI

- `--kms-key-version: optional string`

  An exact CryptoKeyVersion number. Required for PSP decryption; not accepted for EKM.

- `--key-name: string`

  The name of the Azure Key Vault master key that you manage

  `maxLength: 127`

- `--tenant-id: string`

  Your Azure tenant UUID

- `--vault-uri: string`

  The URI of the Azure vault containing the master key you manage

- `--key-version: optional string`

  An exact Azure Key Vault key version. Required for PSP decryption; not accepted for EKM.

### Returns

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

### Example

```cli
openai admin:organization:external-keys create \
  --admin-api-key 'My Admin API Key' \
  --external-id external_id \
  --kms-arn kms_arn \
  --name name \
  --role-arn arn:aws:iam::123456789012:role/example-role \
  --type aws \
  --audience audience \
  --kms-key-location kms_key_location \
  --kms-key-name kms_key_name \
  --kms-key-ring-name kms_key_ring_name \
  --kms-project-id kms_project_id \
  --workload-identity-pool-id workload_identity_pool_id \
  --workload-identity-project-number workload_identity_project_number \
  --workload-identity-provider-id workload_identity_provider_id \
  --key-name key_name \
  --tenant-id tenant_id \
  --vault-uri vault_uri
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
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
}
```

## Delete an external key config for the user's organization

`$ openai admin:organization:external-keys delete`

**delete** `/organization/external_keys/{external_key_id}`

Delete an external key config for the user's organization

### Parameters

- `--external-key-id: string`

### Returns

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

### Example

```cli
openai admin:organization:external-keys delete \
  --admin-api-key 'My Admin API Key' \
  --external-key-id external_key_id
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
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
}
```

## List the external key configs registered on the user's organization

`$ openai admin:organization:external-keys list`

**get** `/organization/external_keys`

List the external key configs registered on the user's organization

### Parameters

- `--after: optional string`

- `--limit: optional number`

  `minimum: 0`, `maximum: 100`

- `--order: optional "asc" or "desc"`

- `--purpose: optional "ekm" or "psp_decryption"`

  Filter by key purpose. When omitted, returns keys of all purposes.

### Returns

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

### Example

```cli
openai admin:organization:external-keys list \
  --admin-api-key 'My Admin API Key'
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "api_project_ids": [
        "string"
      ],
      "created_at": 0,
      "name": "name",
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
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an external key registration

`$ openai admin:organization:external-keys retrieve`

**get** `/organization/external_keys/{external_key_id}`

Retrieve a stored external key registration for the user's organization.

### Parameters

- `--external-key-id: string`

### Returns

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

### Example

```cli
openai admin:organization:external-keys retrieve \
  --admin-api-key 'My Admin API Key' \
  --external-key-id external_key_id
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
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
}
```

## Validate an external key config for the user's organization

`$ openai admin:organization:external-keys validate`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

### Parameters

- `--external-key-id: string`

### Returns

- `AdminOrganizationExternalKeyValidateResponse: object { status }`

  - `status: string`

### Example

```cli
openai admin:organization:external-keys validate \
  --admin-api-key 'My Admin API Key' \
  --external-key-id external_key_id
```

#### 200 — Example

```json
{
  "status": "status"
}
```

## Domain Types

### External Key

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
