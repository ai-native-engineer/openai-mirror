<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_limit/ -->

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

# Spend Limit

##### [Retrieve organization spend limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve)

client.admin.organization.spendLimit.retrieve(RequestOptionsoptions?): [OrganizationSpendLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

GET/organization/spend\_limit

##### [Update organization spend limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_limit/methods/update)

client.admin.organization.spendLimit.update(SpendLimitUpdateParams { currency, interval, threshold\_amount } body, RequestOptionsoptions?): [OrganizationSpendLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

POST/organization/spend\_limit

##### [Delete organization spend limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_limit/methods/delete)

client.admin.organization.spendLimit.delete(RequestOptionsoptions?): [OrganizationSpendLimitDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/spend\_limit

##### ModelsExpand Collapse

OrganizationSpendLimit { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the organization level.

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

object: "organization.spend\_limit"

The object type, which is always `organization.spend_limit`.

threshold\_amount: number

OrganizationSpendLimitDeleted { deleted, object }

Confirmation payload returned after deleting an organization hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "organization.spend\_limit.deleted"

The object type, which is always `organization.spend_limit.deleted`.
