<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

# Spend Limit

##### [Retrieve project spend limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve)

GET/organization/projects/{project\_id}/spend\_limit

##### [Update project spend limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update)

POST/organization/projects/{project\_id}/spend\_limit

##### [Delete project spend limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete)

DELETE/organization/projects/{project\_id}/spend\_limit

##### ModelsExpand Collapse

ProjectSpendLimit object { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the project level.

currency: string or "USD"

string

"USD"

enforcement: object { status }

status: string or "inactive" or "enforcing"

string

"inactive" or "enforcing"

"inactive"

"enforcing"

interval: string or "month"

string

"month"

object: "project.spend\_limit"

The object type, which is always `project.spend_limit`.

threshold\_amount: number

ProjectSpendLimitDeleted object { deleted, object }

Confirmation payload returned after deleting a project hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "project.spend\_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.
