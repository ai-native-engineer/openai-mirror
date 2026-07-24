<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/ -->

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

# Spend Limit

##### [Retrieve project spend limit](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve)

$ openai admin:organization:projects:spend-limit retrieve

GET/organization/projects/{project\_id}/spend\_limit

##### [Update project spend limit](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update)

$ openai admin:organization:projects:spend-limit update

POST/organization/projects/{project\_id}/spend\_limit

##### [Delete project spend limit](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete)

$ openai admin:organization:projects:spend-limit delete

DELETE/organization/projects/{project\_id}/spend\_limit

##### ModelsExpand Collapse

project\_spend\_limit: object { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the project level.

currency: string or "USD"

"USD"

enforcement: object { status }

status: string or "inactive" or "enforcing"

"inactive"

"enforcing"

interval: string or "month"

"month"

object: "project.spend\_limit"

The object type, which is always `project.spend_limit`.

threshold\_amount: number

project\_spend\_limit\_deleted: object { deleted, object }

Confirmation payload returned after deleting a project hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "project.spend\_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.
