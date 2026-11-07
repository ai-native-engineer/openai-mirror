<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/external_keys/methods/create/ -->

## Add an external key config for an organization

`$ openai admin:organization:external-keys create`

**post** `/organization/external_keys`

Add an external key config for an organization

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
