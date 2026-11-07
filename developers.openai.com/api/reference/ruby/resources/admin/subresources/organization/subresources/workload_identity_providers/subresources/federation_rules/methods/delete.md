<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/delete/ -->

## Delete Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.delete(workload_identity_federation_rule_id, **kwargs) -> FederationRuleDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

- `workload_identity_provider_id: String`

  `minLength: 1`

- `workload_identity_federation_rule_id: String`

  `minLength: 1`

- `class FederationRuleDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.workload_identity_federation_rule.deleted"`

    - `:"organization.workload_identity_federation_rule.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

federation_rule_deleted = openai.admin.organization.workload_identity_providers.federation_rules.delete(
  "x",
  workload_identity_provider_id: "x"

puts(federation_rule_deleted)

  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"
