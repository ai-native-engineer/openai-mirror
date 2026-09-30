<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/external_storage/methods/create/ -->

## Create an external storage configuration

`admin.organization.external_storage.create(**kwargs) -> ExternalStorageConfiguration`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

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

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_storage_configuration = openai.admin.organization.external_storage.create(
  project_id: "proj_123",
  provider: {bucket: "bucket", role_arn: "role_arn", type: :aws}

puts(external_storage_configuration)

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
