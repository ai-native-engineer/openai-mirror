<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/ -->

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

# Spend Limit

##### [Retrieve project spend limit](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve)

admin.organization.projects.spend\_limit.retrieve(strproject\_id)  -> [ProjectSpendLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema))

GET/organization/projects/{project\_id}/spend\_limit

##### [Update project spend limit](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update)

admin.organization.projects.spend\_limit.update(strproject\_id, SpendLimitUpdateParams\*\*kwargs)  -> [ProjectSpendLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema))

POST/organization/projects/{project\_id}/spend\_limit

##### [Delete project spend limit](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete)

admin.organization.projects.spend\_limit.delete(strproject\_id)  -> [ProjectSpendLimitDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/spend\_limit

##### ModelsExpand Collapse

class ProjectSpendLimit: …

Represents a hard spend limit configured at the project level.

currency: Union[str, Literal["USD"]]

str

Literal["USD"]

enforcement: Enforcement

status: Union[str, Literal["inactive", "enforcing"]]

str

Literal["inactive", "enforcing"]

"inactive"

"enforcing"

interval: Union[str, Literal["month"]]

str

Literal["month"]

object: Literal["project.spend\_limit"]

The object type, which is always `project.spend_limit`.

threshold\_amount: int

class ProjectSpendLimitDeleted: …

Confirmation payload returned after deleting a project hard spend limit.

deleted: bool

Whether the hard spend limit was deleted.

object: Literal["project.spend\_limit.deleted"]

The object type, which is always `project.spend_limit.deleted`.
