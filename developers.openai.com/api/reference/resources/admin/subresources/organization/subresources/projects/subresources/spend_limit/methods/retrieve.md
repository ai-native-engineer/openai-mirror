<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Retrieve project spend limit

GET/organization/projects/{project\_id}/spend\_limit

Get a project’s hard spend limit.

##### Path ParametersExpand Collapse

project\_id: string

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

### Retrieve project spend limit

HTTP

curl https://api.openai.com/v1/organization/projects/proj_abc/spend_limit \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "project.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

    "object": "project.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"
