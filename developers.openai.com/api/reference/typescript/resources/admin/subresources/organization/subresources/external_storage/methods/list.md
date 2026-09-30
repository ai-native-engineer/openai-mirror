<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/external_storage/methods/list/ -->

## List external storage configurations

`client.admin.organization.externalStorage.list(ExternalStorageListParamsquery?, RequestOptionsoptions?): CursorPage<ExternalStorageConfiguration>`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

- `query: ExternalStorageListParams`

  - `after?: string | null`

    Return external storage configurations after this ID.

  - `limit?: number`

  - `order?: "asc" | "desc"`

    - `"asc"`

    - `"desc"`

  - `project_id?: string | null`

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

// Automatically fetches more pages as needed.
for await (const externalStorageConfiguration of client.admin.organization.externalStorage.list()) {
  console.log(externalStorageConfiguration.id);

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
