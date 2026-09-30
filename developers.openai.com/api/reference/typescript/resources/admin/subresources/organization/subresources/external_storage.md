<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/external_storage/ -->

# External Storage

## Create an external storage configuration

`client.admin.organization.externalStorage.create(ExternalStorageCreateParamsbody, RequestOptionsoptions?): ExternalStorageConfiguration`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

### Parameters

- `body: ExternalStorageCreateParams`

  - `project_id: string`

  - `provider: Aws | Azure | Gcp`

    - `Aws`

      - `bucket: string`

      - `role_arn: string`

      - `type: "aws"`

        - `"aws"`

    - `Azure`

      - `account_name: string`

      - `container: string`

      - `resource_group: string`

      - `subscription_id: string`

      - `tenant_id: string`

      - `type: "azure"`

        - `"azure"`

    - `Gcp`

      - `bucket: string`

      - `type: "gcp"`

        - `"gcp"`

      - `workload_identity_pool_id: string`

      - `workload_identity_project_number: string`

      - `workload_identity_provider_id: string`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const externalStorageConfiguration = await client.admin.organization.externalStorage.create({
  project_id: 'proj_123',
  provider: {
    bucket: 'bucket',
    role_arn: 'role_arn',
    type: 'aws',
  },
});

console.log(externalStorageConfiguration.id);
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Delete an external storage configuration

`client.admin.organization.externalStorage.delete(stringexternalStorageID, RequestOptionsoptions?): ExternalStorageDeleted`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

### Parameters

- `externalStorageID: string`

### Returns

- `ExternalStorageDeleted`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.external_storage.deleted"`

    - `"organization.external_storage.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const externalStorageDeleted = await client.admin.organization.externalStorage.delete(
  'extstorage_123',
);

console.log(externalStorageDeleted.id);
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.external_storage.deleted"
}
```

## List external storage configurations

`client.admin.organization.externalStorage.list(ExternalStorageListParamsquery?, RequestOptionsoptions?): CursorPage<ExternalStorageConfiguration>`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

### Parameters

- `query: ExternalStorageListParams`

  - `after?: string | null`

    Return external storage configurations after this ID.

  - `limit?: number`

  - `order?: "asc" | "desc"`

    - `"asc"`

    - `"desc"`

  - `project_id?: string | null`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const externalStorageConfiguration of client.admin.organization.externalStorage.list()) {
  console.log(externalStorageConfiguration.id);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
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
      },
      "status": "pending"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Get an external storage configuration

`client.admin.organization.externalStorage.retrieve(stringexternalStorageID, RequestOptionsoptions?): ExternalStorageConfiguration`

**get** `/organization/external_storage/{external_storage_id}`

Get one customer-managed external storage configuration.

### Parameters

- `externalStorageID: string`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const externalStorageConfiguration = await client.admin.organization.externalStorage.retrieve(
  'extstorage_123',
);

console.log(externalStorageConfiguration.id);
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Validate an external storage configuration

`client.admin.organization.externalStorage.validate(stringexternalStorageID, RequestOptionsoptions?): ExternalStorageConfiguration`

**post** `/organization/external_storage/{external_storage_id}/validate`

Validate one customer-managed external storage configuration.

### Parameters

- `externalStorageID: string`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const externalStorageConfiguration = await client.admin.organization.externalStorage.validate(
  'extstorage_123',
);

console.log(externalStorageConfiguration.id);
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Domain Types

### Aws External Storage Provider

- `AwsExternalStorageProvider`

  - `account_id: string`

  - `bucket: string`

  - `external_id: string`

  - `region: string`

  - `role_arn: string`

  - `type: "aws"`

    - `"aws"`

### Azure External Storage Provider

- `AzureExternalStorageProvider`

  - `account_name: string`

  - `container: string`

  - `region: string`

  - `resource_group: string`

  - `subscription_id: string`

  - `tenant_id: string`

  - `type: "azure"`

    - `"azure"`

### External Storage Configuration

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

### External Storage Deleted

- `ExternalStorageDeleted`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.external_storage.deleted"`

    - `"organization.external_storage.deleted"`

### Gcp External Storage Provider

- `GcpExternalStorageProvider`

  - `audience: string`

  - `bucket: string`

  - `region: string`

  - `type: "gcp"`

    - `"gcp"`

  - `workload_identity_pool_id: string`

  - `workload_identity_project_number: string`

  - `workload_identity_provider_id: string`
