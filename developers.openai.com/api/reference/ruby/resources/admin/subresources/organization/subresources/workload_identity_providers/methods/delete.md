<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/delete/ -->

## Delete Platform workload identity provider

`admin.organization.workload_identity_providers.delete(workload_identity_provider_id) -> WorkloadIdentityProviderDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

- `workload_identity_provider_id: String`

  `minLength: 1`

- `class WorkloadIdentityProviderDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.workload_identity_provider.deleted"`

    - `:"organization.workload_identity_provider.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

workload_identity_provider_deleted = openai.admin.organization.workload_identity_providers.delete("x")

puts(workload_identity_provider_deleted)

  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"
