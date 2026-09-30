<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/external_storage/methods/validate/ -->

## Validate an external storage configuration

`$ openai admin:organization:external-storage validate`

**post** `/organization/external_storage/{external_storage_id}/validate`

Validate one customer-managed external storage configuration.

- `--external-storage-id: string`

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

```cli
openai admin:organization:external-storage validate \
  --admin-api-key 'My Admin API Key' \
  --external-storage-id extstorage_123

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
