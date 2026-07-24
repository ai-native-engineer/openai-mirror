<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Spend Limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_limit)

# Delete organization spend limit

admin.organization.spend\_limit.delete() -> [OrganizationSpendLimitDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/spend\_limit

Delete the organization’s hard spend limit.

class OrganizationSpendLimitDeleted { deleted, object }

Confirmation payload returned after deleting an organization hard spend limit.

deleted: bool

Whether the hard spend limit was deleted.

object: :"organization.spend\_limit.deleted"

The object type, which is always `organization.spend_limit.deleted`.

### Delete organization spend limit

Ruby

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

organization_spend_limit_deleted = openai.admin.organization.spend_limit.delete

puts(organization_spend_limit_deleted)

    "object": "organization.spend_limit.deleted",
    "deleted": true

    "object": "organization.spend_limit.deleted",
    "deleted": true
