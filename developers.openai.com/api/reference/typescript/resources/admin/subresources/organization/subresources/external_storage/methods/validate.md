<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/external_storage/methods/validate/ -->

## Validate an external storage configuration

`client.admin.organization.externalStorage.validate(stringexternalStorageID, RequestOptionsoptions?): ExternalStorageConfiguration`

**post** `/organization/external_storage/{external_storage_id}/validate`

Validate one customer-managed external storage configuration.

- `externalStorageID: string`

- `ExternalStorageConfiguration`

  - `id: string`

  - `created_at: number`

  - `geography: string`

  - `object: "organization.external_storage"`

    - `"organization.external_storage"`

  - `project_id: string`

  - `provider: AwsExternalStorageProvider | AzureExternalStorageProvider | GcpExternalStorageProvider`

    - `AwsExternalStorageProvider`

      - `account_id: string`

      - `bucket: string`

      - `external_id: string`

      - `region: string`

      - `role_arn: string`

      - `type: "aws"`

        - `"aws"`

    - `AzureExternalStorageProvider`

      - `account_name: string`

      - `container: string`

      - `region: string`

      - `resource_group: string`

      - `subscription_id: string`

      - `tenant_id: string`

      - `type: "azure"`

        - `"azure"`

    - `GcpExternalStorageProvider`

      - `audience: string`

      - `bucket: string`

      - `region: string`

      - `type: "gcp"`

        - `"gcp"`

      - `workload_identity_pool_id: string`

      - `workload_identity_project_number: string`

      - `workload_identity_provider_id: string`

  - `status: "pending" | "validated" | "unhealthy"`

    - `"pending"`

    - `"validated"`

    - `"unhealthy"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const externalStorageConfiguration = await client.admin.organization.externalStorage.validate(
  'extstorage_123',
);

console.log(externalStorageConfiguration.id);

  "geography": "geography",
  "object": "organization.external_storage",
  "project_id": "project_id",
  "provider": {
    "account_id": "account_id",
    "bucket": "bucket",
    "external_id": "external_id",
    "region": "region",
    "role_arn": "role_arn",
    "type": "aws"
  "status": "pending"
