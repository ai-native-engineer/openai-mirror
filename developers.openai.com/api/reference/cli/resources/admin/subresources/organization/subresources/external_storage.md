<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/external_storage/ -->

# External Storage

## Create an external storage configuration

`$ openai admin:organization:external-storage create`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

### Parameters

- `--project-id: string`

- `--provider: object { bucket, role_arn, type }  or object { account_name, container, resource_group, 3 more }  or object { bucket, type, workload_identity_pool_id, 2 more }`

### Returns

- `external_storage_configuration: object { id, created_at, geography, 4 more }`

  - `id: string`

  - `created_at: number`

  - `geography: string`

  - `object: "organization.external_storage"`

  - `project_id: string`

  - `provider: AwsExternalStorageProvider or AzureExternalStorageProvider or GcpExternalStorageProvider`

    - `aws_external_storage_provider: object { account_id, bucket, external_id, 3 more }`

      - `account_id: string`

      - `bucket: string`

      - `external_id: string`

      - `region: string`

      - `role_arn: string`

      - `type: "aws"`

    - `azure_external_storage_provider: object { account_name, container, region, 4 more }`

      - `account_name: string`

      - `container: string`

      - `region: string`

      - `resource_group: string`

      - `subscription_id: string`

      - `tenant_id: string`

      - `type: "azure"`

    - `gcp_external_storage_provider: object { audience, bucket, region, 4 more }`

      - `audience: string`

      - `bucket: string`

      - `region: string`

      - `type: "gcp"`

      - `workload_identity_pool_id: string`

      - `workload_identity_project_number: string`

      - `workload_identity_provider_id: string`

  - `status: "pending" or "validated" or "unhealthy"`

    - `"pending"`

    - `"validated"`

    - `"unhealthy"`

### Example

```cli
openai admin:organization:external-storage create \
  --admin-api-key 'My Admin API Key' \
  --project-id proj_123 \
  --provider '{bucket: bucket, role_arn: role_arn, type: aws}'
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

`$ openai admin:organization:external-storage delete`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

### Parameters

- `--external-storage-id: string`

### Returns

- `external_storage_deleted: object { id, deleted, object }`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.external_storage.deleted"`

### Example

```cli
openai admin:organization:external-storage delete \
  --admin-api-key 'My Admin API Key' \
  --external-storage-id extstorage_123
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

`$ openai admin:organization:external-storage list`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

### Parameters

- `--after: optional string`

  Return external storage configurations after this ID.

- `--limit: optional number`

- `--order: optional "asc" or "desc"`

- `--project-id: optional string`

### Returns

- `ExternalStorageListResource: object { data, first_id, has_more, 2 more }`

  - `data: array of ExternalStorageConfiguration`

    - `id: string`

    - `created_at: number`

    - `geography: string`

    - `object: "organization.external_storage"`

    - `project_id: string`

    - `provider: AwsExternalStorageProvider or AzureExternalStorageProvider or GcpExternalStorageProvider`

      - `aws_external_storage_provider: object { account_id, bucket, external_id, 3 more }`

        - `account_id: string`

        - `bucket: string`

        - `external_id: string`

        - `region: string`

        - `role_arn: string`

        - `type: "aws"`

      - `azure_external_storage_provider: object { account_name, container, region, 4 more }`

        - `account_name: string`

        - `container: string`

        - `region: string`

        - `resource_group: string`

        - `subscription_id: string`

        - `tenant_id: string`

        - `type: "azure"`

      - `gcp_external_storage_provider: object { audience, bucket, region, 4 more }`

        - `audience: string`

        - `bucket: string`

        - `region: string`

        - `type: "gcp"`

        - `workload_identity_pool_id: string`

        - `workload_identity_project_number: string`

        - `workload_identity_provider_id: string`

    - `status: "pending" or "validated" or "unhealthy"`

      - `"pending"`

      - `"validated"`

      - `"unhealthy"`

  - `first_id: string`

  - `has_more: boolean`

  - `last_id: string`

  - `object: "list"`

### Example

```cli
openai admin:organization:external-storage list \
  --admin-api-key 'My Admin API Key'
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

`$ openai admin:organization:external-storage retrieve`

**get** `/organization/external_storage/{external_storage_id}`

Get one customer-managed external storage configuration.

### Parameters

- `--external-storage-id: string`

### Returns

- `external_storage_configuration: object { id, created_at, geography, 4 more }`

  - `id: string`

  - `created_at: number`

  - `geography: string`

  - `object: "organization.external_storage"`

  - `project_id: string`

  - `provider: AwsExternalStorageProvider or AzureExternalStorageProvider or GcpExternalStorageProvider`

    - `aws_external_storage_provider: object { account_id, bucket, external_id, 3 more }`

      - `account_id: string`

      - `bucket: string`

      - `external_id: string`

      - `region: string`

      - `role_arn: string`

      - `type: "aws"`

    - `azure_external_storage_provider: object { account_name, container, region, 4 more }`

      - `account_name: string`

      - `container: string`

      - `region: string`

      - `resource_group: string`

      - `subscription_id: string`

      - `tenant_id: string`

      - `type: "azure"`

    - `gcp_external_storage_provider: object { audience, bucket, region, 4 more }`

      - `audience: string`

      - `bucket: string`

      - `region: string`

      - `type: "gcp"`

      - `workload_identity_pool_id: string`

      - `workload_identity_project_number: string`

      - `workload_identity_provider_id: string`

  - `status: "pending" or "validated" or "unhealthy"`

    - `"pending"`

    - `"validated"`

    - `"unhealthy"`

### Example

```cli
openai admin:organization:external-storage retrieve \
  --admin-api-key 'My Admin API Key' \
  --external-storage-id extstorage_123
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

`$ openai admin:organization:external-storage validate`

**post** `/organization/external_storage/{external_storage_id}/validate`

Validate one customer-managed external storage configuration.

### Parameters

- `--external-storage-id: string`

### Returns

- `external_storage_configuration: object { id, created_at, geography, 4 more }`

  - `id: string`

  - `created_at: number`

  - `geography: string`

  - `object: "organization.external_storage"`

  - `project_id: string`

  - `provider: AwsExternalStorageProvider or AzureExternalStorageProvider or GcpExternalStorageProvider`

    - `aws_external_storage_provider: object { account_id, bucket, external_id, 3 more }`

      - `account_id: string`

      - `bucket: string`

      - `external_id: string`

      - `region: string`

      - `role_arn: string`

      - `type: "aws"`

    - `azure_external_storage_provider: object { account_name, container, region, 4 more }`

      - `account_name: string`

      - `container: string`

      - `region: string`

      - `resource_group: string`

      - `subscription_id: string`

      - `tenant_id: string`

      - `type: "azure"`

    - `gcp_external_storage_provider: object { audience, bucket, region, 4 more }`

      - `audience: string`

      - `bucket: string`

      - `region: string`

      - `type: "gcp"`

      - `workload_identity_pool_id: string`

      - `workload_identity_project_number: string`

      - `workload_identity_provider_id: string`

  - `status: "pending" or "validated" or "unhealthy"`

    - `"pending"`

    - `"validated"`

    - `"unhealthy"`

### Example

```cli
openai admin:organization:external-storage validate \
  --admin-api-key 'My Admin API Key' \
  --external-storage-id extstorage_123
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

- `aws_external_storage_provider: object { account_id, bucket, external_id, 3 more }`

  - `account_id: string`

  - `bucket: string`

  - `external_id: string`

  - `region: string`

  - `role_arn: string`

  - `type: "aws"`

### Azure External Storage Provider

- `azure_external_storage_provider: object { account_name, container, region, 4 more }`

  - `account_name: string`

  - `container: string`

  - `region: string`

  - `resource_group: string`

  - `subscription_id: string`

  - `tenant_id: string`

  - `type: "azure"`

### External Storage Configuration

- `external_storage_configuration: object { id, created_at, geography, 4 more }`

  - `id: string`

  - `created_at: number`

  - `geography: string`

  - `object: "organization.external_storage"`

  - `project_id: string`

  - `provider: AwsExternalStorageProvider or AzureExternalStorageProvider or GcpExternalStorageProvider`

    - `aws_external_storage_provider: object { account_id, bucket, external_id, 3 more }`

      - `account_id: string`

      - `bucket: string`

      - `external_id: string`

      - `region: string`

      - `role_arn: string`

      - `type: "aws"`

    - `azure_external_storage_provider: object { account_name, container, region, 4 more }`

      - `account_name: string`

      - `container: string`

      - `region: string`

      - `resource_group: string`

      - `subscription_id: string`

      - `tenant_id: string`

      - `type: "azure"`

    - `gcp_external_storage_provider: object { audience, bucket, region, 4 more }`

      - `audience: string`

      - `bucket: string`

      - `region: string`

      - `type: "gcp"`

      - `workload_identity_pool_id: string`

      - `workload_identity_project_number: string`

      - `workload_identity_provider_id: string`

  - `status: "pending" or "validated" or "unhealthy"`

    - `"pending"`

    - `"validated"`

    - `"unhealthy"`

### External Storage Deleted

- `external_storage_deleted: object { id, deleted, object }`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.external_storage.deleted"`

### Gcp External Storage Provider

- `gcp_external_storage_provider: object { audience, bucket, region, 4 more }`

  - `audience: string`

  - `bucket: string`

  - `region: string`

  - `type: "gcp"`

  - `workload_identity_pool_id: string`

  - `workload_identity_project_number: string`

  - `workload_identity_provider_id: string`
