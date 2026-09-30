<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/external_storage/ -->

# External Storage

## Create an external storage configuration

`admin.organization.external_storage.create(**kwargs) -> ExternalStorageConfiguration`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

### Parameters

- `project_id: String`

- `provider: Aws{ bucket, role_arn, type} | Azure{ account_name, container, resource_group, 3 more} | Gcp{ bucket, type, workload_identity_pool_id, 2 more}`

  - `class Aws`

    - `bucket: String`

    - `role_arn: String`

    - `type: :aws`

      - `:aws`

  - `class Azure`

    - `account_name: String`

    - `container: String`

    - `resource_group: String`

    - `subscription_id: String`

    - `tenant_id: String`

    - `type: :azure`

      - `:azure`

  - `class Gcp`

    - `bucket: String`

    - `type: :gcp`

      - `:gcp`

    - `workload_identity_pool_id: String`

    - `workload_identity_project_number: String`

    - `workload_identity_provider_id: String`

### Returns

- `class ExternalStorageConfiguration`

  - `id: String`

  - `created_at: Integer`

  - `geography: String`

  - `object: :"organization.external_storage"`

    - `:"organization.external_storage"`

  - `project_id: String`

  - `provider: AwsExternalStorageProvider | AzureExternalStorageProvider | GcpExternalStorageProvider`

    - `class AwsExternalStorageProvider`

      - `account_id: String`

      - `bucket: String`

      - `external_id: String`

      - `region: String`

      - `role_arn: String`

      - `type: :aws`

        - `:aws`

    - `class AzureExternalStorageProvider`

      - `account_name: String`

      - `container: String`

      - `region: String`

      - `resource_group: String`

      - `subscription_id: String`

      - `tenant_id: String`

      - `type: :azure`

        - `:azure`

    - `class GcpExternalStorageProvider`

      - `audience: String`

      - `bucket: String`

      - `region: String`

      - `type: :gcp`

        - `:gcp`

      - `workload_identity_pool_id: String`

      - `workload_identity_project_number: String`

      - `workload_identity_provider_id: String`

  - `status: :pending | :validated | :unhealthy`

    - `:pending`

    - `:validated`

    - `:unhealthy`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_storage_configuration = openai.admin.organization.external_storage.create(
  project_id: "proj_123",
  provider: {bucket: "bucket", role_arn: "role_arn", type: :aws}
)

puts(external_storage_configuration)
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

`admin.organization.external_storage.delete(external_storage_id) -> ExternalStorageDeleted`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

### Parameters

- `external_storage_id: String`

### Returns

- `class ExternalStorageDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.external_storage.deleted"`

    - `:"organization.external_storage.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_storage_deleted = openai.admin.organization.external_storage.delete("extstorage_123")

puts(external_storage_deleted)
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

`admin.organization.external_storage.list(**kwargs) -> CursorPage<ExternalStorageConfiguration>`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

### Parameters

- `after: String`

  Return external storage configurations after this ID.

- `limit: Integer`

- `order: :asc | :desc`

  - `:asc`

  - `:desc`

- `project_id: String`

### Returns

- `class ExternalStorageConfiguration`

  - `id: String`

  - `created_at: Integer`

  - `geography: String`

  - `object: :"organization.external_storage"`

    - `:"organization.external_storage"`

  - `project_id: String`

  - `provider: AwsExternalStorageProvider | AzureExternalStorageProvider | GcpExternalStorageProvider`

    - `class AwsExternalStorageProvider`

      - `account_id: String`

      - `bucket: String`

      - `external_id: String`

      - `region: String`

      - `role_arn: String`

      - `type: :aws`

        - `:aws`

    - `class AzureExternalStorageProvider`

      - `account_name: String`

      - `container: String`

      - `region: String`

      - `resource_group: String`

      - `subscription_id: String`

      - `tenant_id: String`

      - `type: :azure`

        - `:azure`

    - `class GcpExternalStorageProvider`

      - `audience: String`

      - `bucket: String`

      - `region: String`

      - `type: :gcp`

        - `:gcp`

      - `workload_identity_pool_id: String`

      - `workload_identity_project_number: String`

      - `workload_identity_provider_id: String`

  - `status: :pending | :validated | :unhealthy`

    - `:pending`

    - `:validated`

    - `:unhealthy`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.external_storage.list

puts(page)
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

`admin.organization.external_storage.retrieve(external_storage_id) -> ExternalStorageConfiguration`

**get** `/organization/external_storage/{external_storage_id}`

Get one customer-managed external storage configuration.

### Parameters

- `external_storage_id: String`

### Returns

- `class ExternalStorageConfiguration`

  - `id: String`

  - `created_at: Integer`

  - `geography: String`

  - `object: :"organization.external_storage"`

    - `:"organization.external_storage"`

  - `project_id: String`

  - `provider: AwsExternalStorageProvider | AzureExternalStorageProvider | GcpExternalStorageProvider`

    - `class AwsExternalStorageProvider`

      - `account_id: String`

      - `bucket: String`

      - `external_id: String`

      - `region: String`

      - `role_arn: String`

      - `type: :aws`

        - `:aws`

    - `class AzureExternalStorageProvider`

      - `account_name: String`

      - `container: String`

      - `region: String`

      - `resource_group: String`

      - `subscription_id: String`

      - `tenant_id: String`

      - `type: :azure`

        - `:azure`

    - `class GcpExternalStorageProvider`

      - `audience: String`

      - `bucket: String`

      - `region: String`

      - `type: :gcp`

        - `:gcp`

      - `workload_identity_pool_id: String`

      - `workload_identity_project_number: String`

      - `workload_identity_provider_id: String`

  - `status: :pending | :validated | :unhealthy`

    - `:pending`

    - `:validated`

    - `:unhealthy`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_storage_configuration = openai.admin.organization.external_storage.retrieve("extstorage_123")

puts(external_storage_configuration)
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

`admin.organization.external_storage.validate(external_storage_id) -> ExternalStorageConfiguration`

**post** `/organization/external_storage/{external_storage_id}/validate`

Validate one customer-managed external storage configuration.

### Parameters

- `external_storage_id: String`

### Returns

- `class ExternalStorageConfiguration`

  - `id: String`

  - `created_at: Integer`

  - `geography: String`

  - `object: :"organization.external_storage"`

    - `:"organization.external_storage"`

  - `project_id: String`

  - `provider: AwsExternalStorageProvider | AzureExternalStorageProvider | GcpExternalStorageProvider`

    - `class AwsExternalStorageProvider`

      - `account_id: String`

      - `bucket: String`

      - `external_id: String`

      - `region: String`

      - `role_arn: String`

      - `type: :aws`

        - `:aws`

    - `class AzureExternalStorageProvider`

      - `account_name: String`

      - `container: String`

      - `region: String`

      - `resource_group: String`

      - `subscription_id: String`

      - `tenant_id: String`

      - `type: :azure`

        - `:azure`

    - `class GcpExternalStorageProvider`

      - `audience: String`

      - `bucket: String`

      - `region: String`

      - `type: :gcp`

        - `:gcp`

      - `workload_identity_pool_id: String`

      - `workload_identity_project_number: String`

      - `workload_identity_provider_id: String`

  - `status: :pending | :validated | :unhealthy`

    - `:pending`

    - `:validated`

    - `:unhealthy`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_storage_configuration = openai.admin.organization.external_storage.validate("extstorage_123")

puts(external_storage_configuration)
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

- `class AwsExternalStorageProvider`

  - `account_id: String`

  - `bucket: String`

  - `external_id: String`

  - `region: String`

  - `role_arn: String`

  - `type: :aws`

    - `:aws`

### Azure External Storage Provider

- `class AzureExternalStorageProvider`

  - `account_name: String`

  - `container: String`

  - `region: String`

  - `resource_group: String`

  - `subscription_id: String`

  - `tenant_id: String`

  - `type: :azure`

    - `:azure`

### External Storage Configuration

- `class ExternalStorageConfiguration`

  - `id: String`

  - `created_at: Integer`

  - `geography: String`

  - `object: :"organization.external_storage"`

    - `:"organization.external_storage"`

  - `project_id: String`

  - `provider: AwsExternalStorageProvider | AzureExternalStorageProvider | GcpExternalStorageProvider`

    - `class AwsExternalStorageProvider`

      - `account_id: String`

      - `bucket: String`

      - `external_id: String`

      - `region: String`

      - `role_arn: String`

      - `type: :aws`

        - `:aws`

    - `class AzureExternalStorageProvider`

      - `account_name: String`

      - `container: String`

      - `region: String`

      - `resource_group: String`

      - `subscription_id: String`

      - `tenant_id: String`

      - `type: :azure`

        - `:azure`

    - `class GcpExternalStorageProvider`

      - `audience: String`

      - `bucket: String`

      - `region: String`

      - `type: :gcp`

        - `:gcp`

      - `workload_identity_pool_id: String`

      - `workload_identity_project_number: String`

      - `workload_identity_provider_id: String`

  - `status: :pending | :validated | :unhealthy`

    - `:pending`

    - `:validated`

    - `:unhealthy`

### External Storage Deleted

- `class ExternalStorageDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.external_storage.deleted"`

    - `:"organization.external_storage.deleted"`

### Gcp External Storage Provider

- `class GcpExternalStorageProvider`

  - `audience: String`

  - `bucket: String`

  - `region: String`

  - `type: :gcp`

    - `:gcp`

  - `workload_identity_pool_id: String`

  - `workload_identity_project_number: String`

  - `workload_identity_provider_id: String`
