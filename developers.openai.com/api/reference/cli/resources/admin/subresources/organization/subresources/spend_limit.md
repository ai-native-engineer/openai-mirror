<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/spend_limit/ -->

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

# Spend Limit

##### [Retrieve organization spend limit](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve)

$ openai admin:organization:spend-limit retrieve

GET/organization/spend\_limit

##### [Update organization spend limit](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_limit/methods/update)

$ openai admin:organization:spend-limit update

POST/organization/spend\_limit

##### [Delete organization spend limit](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_limit/methods/delete)

$ openai admin:organization:spend-limit delete

DELETE/organization/spend\_limit

##### ModelsExpand Collapse

organization\_spend\_limit: object { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the organization level.

currency: string or "USD"

"USD"

enforcement: object { status }

status: string or "inactive" or "enforcing"

"inactive"

"enforcing"

interval: string or "month"

"month"

object: "organization.spend\_limit"

The object type, which is always `organization.spend_limit`.

threshold\_amount: number

organization\_spend\_limit\_deleted: object { deleted, object }

Confirmation payload returned after deleting an organization hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "organization.spend\_limit.deleted"

The object type, which is always `organization.spend_limit.deleted`.
