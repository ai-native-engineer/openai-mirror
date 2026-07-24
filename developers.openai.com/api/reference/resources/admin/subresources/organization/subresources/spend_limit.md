<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/spend_limit/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

# Spend Limit

##### [Retrieve organization spend limit](/api/reference/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve)

GET/organization/spend\_limit

##### [Update organization spend limit](/api/reference/resources/admin/subresources/organization/subresources/spend_limit/methods/update)

POST/organization/spend\_limit

##### [Delete organization spend limit](/api/reference/resources/admin/subresources/organization/subresources/spend_limit/methods/delete)

DELETE/organization/spend\_limit

##### ModelsExpand Collapse

OrganizationSpendLimit object { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the organization level.

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

object: "organization.spend\_limit"

The object type, which is always `organization.spend_limit`.

threshold\_amount: number

OrganizationSpendLimitDeleted object { deleted, object }

Confirmation payload returned after deleting an organization hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "organization.spend\_limit.deleted"

The object type, which is always `organization.spend_limit.deleted`.
