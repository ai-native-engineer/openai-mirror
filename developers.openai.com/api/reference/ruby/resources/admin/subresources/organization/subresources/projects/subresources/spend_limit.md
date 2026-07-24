<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/ -->

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

# Spend Limit

##### [Retrieve project spend limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve)

admin.organization.projects.spend\_limit.retrieve(project\_id) -> [ProjectSpendLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

GET/organization/projects/{project\_id}/spend\_limit

##### [Update project spend limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update)

admin.organization.projects.spend\_limit.update(project\_id, \*\*kwargs) -> [ProjectSpendLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

POST/organization/projects/{project\_id}/spend\_limit

##### [Delete project spend limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete)

admin.organization.projects.spend\_limit.delete(project\_id) -> [ProjectSpendLimitDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/spend\_limit

##### ModelsExpand Collapse

class ProjectSpendLimit { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the project level.

currency: String | :USD

String = String

Currency = :USD

enforcement: Enforcement{ status}

status: String | :inactive | :enforcing

String = String

Status = :inactive | :enforcing

:inactive

:enforcing

interval: String | :month

String = String

Interval = :month

object: :"project.spend\_limit"

The object type, which is always `project.spend_limit`.

threshold\_amount: Integer

class ProjectSpendLimitDeleted { deleted, object }

Confirmation payload returned after deleting a project hard spend limit.

deleted: bool

Whether the hard spend limit was deleted.

object: :"project.spend\_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.
