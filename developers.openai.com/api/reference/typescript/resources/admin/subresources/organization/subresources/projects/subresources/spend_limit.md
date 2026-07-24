<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/ -->

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

# Spend Limit

##### [Retrieve project spend limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve)

client.admin.organization.projects.spendLimit.retrieve(stringprojectID, RequestOptionsoptions?): [ProjectSpendLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

GET/organization/projects/{project\_id}/spend\_limit

##### [Update project spend limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update)

client.admin.organization.projects.spendLimit.update(stringprojectID, SpendLimitUpdateParams { currency, interval, threshold\_amount } body, RequestOptionsoptions?): [ProjectSpendLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

POST/organization/projects/{project\_id}/spend\_limit

##### [Delete project spend limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete)

client.admin.organization.projects.spendLimit.delete(stringprojectID, RequestOptionsoptions?): [ProjectSpendLimitDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/spend\_limit

##### ModelsExpand Collapse

ProjectSpendLimit { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the project level.

currency: (string & {}) | "USD"

(string & {})

"USD"

"USD"

enforcement: Enforcement { status }

status: (string & {}) | "inactive" | "enforcing"

(string & {})

"inactive" | "enforcing"

"inactive"

"enforcing"

interval: (string & {}) | "month"

(string & {})

"month"

"month"

object: "project.spend\_limit"

The object type, which is always `project.spend_limit`.

threshold\_amount: number

ProjectSpendLimitDeleted { deleted, object }

Confirmation payload returned after deleting a project hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "project.spend\_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.
