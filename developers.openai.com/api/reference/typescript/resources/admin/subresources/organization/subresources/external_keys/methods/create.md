<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/external_keys/methods/create/ -->

## Add an external key config for an organization

`client.admin.organization.externalKeys.create(ExternalKeyCreateParamsbody, RequestOptionsoptions?): ExternalKey`

**post** `/organization/external_keys`

Add an external key config for an organization

- `ExternalKeyCreateParams = AwsExternalKeyParams | GcpExternalKeyParams | AzureExternalKeyParams`

  - `ExternalKeyCreateParamsBase`

    - `external_id: string`

      The ExternalID that OpenAI will pass in the AssumeRole call for the customer's AWS account. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

    - `kms_arn: string`

      The Key Management System ARN for the master key you manage

    - `name: string`

      A friendly name to identify this config

    - `role_arn: string`

      The Role ARN that OpenAI will assume to call your KMS

    - `type: "aws"`

      - `"aws"`

    - `purpose?: "ekm" | "psp_decryption"`

      - `"ekm"`

      - `"psp_decryption"`

  - `AwsExternalKeyParams extends ExternalKeyCreateParamsBase`

  - `GcpExternalKeyParams`

    - `audience: string`

      The aud field in the identity token OpenAI will pass in the call to the customer's GCP STS. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

    - `kms_key_location: string`

      The region where your Key Management System master key is located

    - `kms_key_name: string`

      The name of the Key Management System master key you manage

    - `kms_key_ring_name: string`

      The Key Management System key ring for the master key you manage

    - `kms_project_id: string`

      The string GCP project name where your KMS resides

    - `name: string`

      A friendly name to identify this config

    - `type: "gcp"`

      - `"gcp"`

    - `workload_identity_pool_id: string`

      The pool containing the Workload Identity provider that you registered for OpenAI

    - `workload_identity_project_number: string`

      The numeric GCP project number where you registered OpenAI's workload identity

    - `workload_identity_provider_id: string`

      The Workload Identity provider that you registered for OpenAI

    - `kms_key_version?: string`

      An exact CryptoKeyVersion number. Required for PSP decryption; not accepted for EKM.

    - `purpose?: "ekm" | "psp_decryption"`

      - `"ekm"`

      - `"psp_decryption"`

  - `AzureExternalKeyParams`

    - `key_name: string`

      The name of the Azure Key Vault master key that you manage

      `maxLength: 127`

    - `name: string`

      A friendly name to identify this config

    - `tenant_id: string`

      Your Azure tenant UUID

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      The URI of the Azure vault containing the master key you manage

    - `key_version?: string`

      An exact Azure Key Vault key version. Required for PSP decryption; not accepted for EKM.

    - `purpose?: "ekm" | "psp_decryption"`

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

const externalKey = await client.admin.organization.externalKeys.create({
  external_id: 'external_id',
  kms_arn: 'kms_arn',
  name: 'name',
  role_arn: 'arn:aws:iam::123456789012:role/example-role',
  type: 'aws',
});

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
