<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/external_keys/methods/delete/ -->

## Delete an external key config for the user's organization

`admin.organization.external_keys.delete(external_key_id) -> ExternalKey`

**delete** `/organization/external_keys/{external_key_id}`

Delete an external key config for the user's organization

- `external_key_id: String`

- `class ExternalKey`

  - `id: String`

  - `api_project_ids: Array[String]`

  - `created_at: Integer`

  - `name: String`

  - `object: String`

  - `type: String`

  - `workspace_id: String`

  - `audience: String`

  - `external_id: String`

  - `key_name: String`

  - `key_version: String`

  - `kms_arn: String`

  - `kms_key_location: String`

  - `kms_key_name: String`

  - `kms_key_ring_name: String`

  - `kms_key_version: String`

  - `kms_project_id: String`

  - `purpose: :ekm | :psp_decryption`

    - `:ekm`

    - `:psp_decryption`

  - `role_arn: String`

  - `tenant_id: String`

  - `vault_uri: String`

  - `workload_identity_pool_id: String`

  - `workload_identity_project_number: String`

  - `workload_identity_provider_id: String`

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_key = openai.admin.organization.external_keys.delete("external_key_id")

puts(external_key)

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
