<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Delete project spend limit

admin.organization.projects.spend\_limit.delete(project\_id) -> [ProjectSpendLimitDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/spend\_limit

Delete a project’s hard spend limit.

##### ParametersExpand Collapse

project\_id: String

class ProjectSpendLimitDeleted { deleted, object }

Confirmation payload returned after deleting a project hard spend limit.

deleted: bool

Whether the hard spend limit was deleted.

object: :"project.spend\_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.

### Delete project spend limit

Ruby

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

project_spend_limit_deleted = openai.admin.organization.projects.spend_limit.delete("proj_123")

puts(project_spend_limit_deleted)

    "object": "project.spend_limit.deleted",
    "deleted": true

    "object": "project.spend_limit.deleted",
    "deleted": true
