<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/external_storage/methods/retrieve/ -->

## Get an external storage configuration

`admin.organization.external_storage.retrieve(external_storage_id) -> ExternalStorageConfiguration`

**get** `/organization/external_storage/{external_storage_id}`

Get one customer-managed external storage configuration.

- `external_storage_id: String`

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

external_storage_configuration = openai.admin.organization.external_storage.retrieve("extstorage_123")

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
