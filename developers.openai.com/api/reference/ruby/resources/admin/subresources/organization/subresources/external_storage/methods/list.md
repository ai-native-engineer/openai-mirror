<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/external_storage/methods/list/ -->

## List external storage configurations

`admin.organization.external_storage.list(**kwargs) -> CursorPage<ExternalStorageConfiguration>`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

- `after: String`

  Return external storage configurations after this ID.

- `limit: Integer`

- `order: :asc | :desc`

  - `:asc`

  - `:desc`

- `project_id: String`

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

page = openai.admin.organization.external_storage.list

puts(page)

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
